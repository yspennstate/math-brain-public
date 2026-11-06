#!/usr/bin/env python3
"""memory_pull.py - bring memories other computers filed into this computer's memory folder. Insert-only.

When one brain runs on several computers, each computer files its memories into its own folder and one of them (or
each in turn) pushes them to a shared repository. A memory filed on computer A is dark to recall on computer B until
something copies it across. This is that copy, in its smallest safe form.

Sources (pick one):
    --repo owner/name --folder path/in/repo   a GitHub repository, read over the API with fleet_board's auth
                                              (defaults: BRAIN_MEMORY_REPO, BRAIN_MEMORY_FOLDER, branch main or
                                              BRAIN_MEMORY_BRANCH); one GraphQL query names the folder's tree,
                                              one gzipped call lists it (skipped when the tree is the one the last
                                              complete run saw, kept in BRAIN_MEMORY_PULL_TREES), and the missing
                                              bodies come 40 to a GraphQL query, each checked against its blob id
    --from-dir PATH                           any folder of memory files: a clone of the shared repository, a
                                              network share, a synced drive

What it does: compares the source with this computer's memory folder (BRAIN_MEM_DIR, else the folder
spread_recall.py names) and writes each file that is MISSING here, newest slug date first, at most --max per run
(default 200). A file that already exists here is never touched (it is opened with O_EXCL), so a local edit is never
overwritten and nothing is ever deleted. Files without frontmatter, names that are not memory slugs, and the shared
indexes (MEMORY.md, INDEX_ARCHIVE.md, MISTAKES.md: each computer keeps its own) are skipped. When anything arrived,
it runs `bm25.py refresh` so recall sees the new files within seconds. Dry run by default; --apply writes.

    python3 memory_pull.py --from-dir ../shared-memories/memory            what would arrive
    python3 memory_pull.py --repo you/brain-memories --folder memory --apply
    python3 memory_pull.py --max 50 --apply
"""
import base64, hashlib, json, os, re, subprocess, sys, time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

NAME = re.compile(r"^[a-z0-9][a-z0-9_.\-]{2,200}\.md$")
SKIP = {"MEMORY.md", "INDEX_ARCHIVE.md", "MISTAKES.md"}   # indexes and shared logs are each computer's own
STATE = os.environ.get("BRAIN_MEMORY_PULL_STATE") or os.path.join(
    os.path.expanduser("~"), ".claude", "fleet_board", "memory_pull_state.json")
TREE_STATE = os.environ.get("BRAIN_MEMORY_PULL_TREES") or os.path.join(os.path.dirname(STATE), "memory_pull_trees.json")


def mem_dir():
    if os.environ.get("BRAIN_MEM_DIR"):
        return os.environ["BRAIN_MEM_DIR"]
    try:
        import spread_recall
        return spread_recall.MEM
    except Exception:
        return None


def blob_id(data):
    """The id git gives a file's bytes."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


class DirSource:
    def __init__(self, path):
        self.path = path

    def names(self):
        return {n: None for n in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, n))}

    def read(self, name):
        with open(os.path.join(self.path, name), "rb") as fh:
            return fh.read()


class RepoSource:
    """A folder of a GitHub repository, read over the API. Four things keep it fast on a big folder:
    - the folder's tree id comes from ONE GraphQL query; when it equals the last run's and that run brought in
      everything, the listing is not read at all (the tree state file, keyed by repository, branch, folder and
      memory folder);
    - the tree listing is asked gzipped (a 31k-entry listing is about 13 MB of JSON and 2.5 MB gzipped; on a slow
      line the uncompressed read is the one that times out);
    - the bodies of the missing files come GQL_CHUNK per GraphQL query, each kept only when it hashes back to its
      blob id, with the REST blob read as the fallback for any that does not (a binary, truncated or non-UTF-8 file);
    - a status 0 (no network, a socket timeout) is retried after RETRY_WAITS seconds before it counts as a failure.
    When the GraphQL query itself fails, the listing goes the plain REST way (the parent's contents, then the tree).
    """
    GQL_CHUNK = 40
    RETRY_WAITS = (15, 45)
    BASE = "https://api.github.com"

    def __init__(self, repo, folder, branch, state=None, mem=None):
        import fleet_board  # its api() and token() carry this computer's GitHub auth
        self.api, self.token = fleet_board.api, fleet_board.token
        self.repo, self.folder, self.branch = repo, folder.strip("/"), branch
        self.state = state or TREE_STATE
        self.key = "%s@%s:%s>%s" % (repo, branch, self.folder, mem or "")
        self.sleep, self.log = time.sleep, print
        self.tree = None        # the folder's tree id once listed whole; None means do not record this run
        self.unchanged = False  # True when the listing was skipped
        self.shas, self.bodies = {}, {}

    def _retry(self, call, what):
        """`call(k)` is try k (0-based); a status other than 0 is returned at once."""
        for k in range(len(self.RETRY_WAITS) + 1):
            st, r = call(k)
            if st != 0 or k == len(self.RETRY_WAITS):
                return st, r
            self.log("%s: status 0 (try %d of %d); retrying in %d s"
                     % (what, k + 1, len(self.RETRY_WAITS) + 1, self.RETRY_WAITS[k]))
            self.sleep(self.RETRY_WAITS[k])

    def _gql(self, query):
        st, r = self._retry(lambda k: self.api("POST", "/graphql", body={"query": query},
                                               timeout=60 if k == 0 else 120), "graphql")
        if st != 200 or not isinstance(r, dict) or r.get("errors") or "data" not in r:
            raise RuntimeError("graphql status %s" % st)
        return r["data"]

    def get_gz(self, url, timeout):
        """(status, json) for a GET asked gzipped; status 0 on a network error or a short read."""
        import gzip, urllib.error, urllib.request
        req = urllib.request.Request(self.BASE + url, headers={
            "Authorization": "Bearer " + self.token(), "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28", "Accept-Encoding": "gzip"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if (r.headers.get("Content-Encoding") or "").lower() == "gzip":
                    raw = gzip.decompress(raw)
                return r.status, json.loads(raw or b"{}")
        except urllib.error.HTTPError as e:
            return e.code, {}
        except Exception as e:   # say what it was: a short read is not "no network"
            self.log("GET %s: %r" % (url[-50:], e))
            return 0, {}

    def _all_state(self):
        try:
            with open(self.state, encoding="utf-8") as fh:
                d = json.load(fh)
            return d if isinstance(d, dict) else {}
        except (OSError, ValueError):
            return {}

    def finish(self, complete):
        """Record this run's tree id; `complete` says every file at the source is now here."""
        if not self.tree:
            return
        allst = self._all_state()
        allst[self.key] = {"tree": self.tree, "complete": bool(complete), "at": round(time.time())}
        try:
            os.makedirs(os.path.dirname(self.state) or ".", exist_ok=True)
            with open(self.state + ".tmp", "w", encoding="utf-8") as fh:
                json.dump(allst, fh)
            os.replace(self.state + ".tmp", self.state)
        except OSError:
            pass

    def names(self):
        owner, name = self.repo.split("/")
        try:
            d = self._gql('query { repository(owner: "%s", name: "%s") { object(expression: "%s:%s") { oid } } }'
                          % (owner, name, self.branch, self.folder))
            tree = ((d.get("repository") or {}).get("object") or {}).get("oid")
        except RuntimeError as e:
            self.log("%s; listing over REST" % e)
            return self._names_rest()
        if not tree:
            raise RuntimeError("memory folder not on %s" % self.branch)
        self.tree = tree
        last = self._all_state().get(self.key) or {}
        if last.get("tree") == tree and last.get("complete"):
            self.unchanged = True
            return {}
        st, r = self._retry(lambda k: self.get_gz("/repos/%s/git/trees/%s" % (self.repo, tree),
                                                  timeout=120 if k == 0 else 180), "tree listing")
        if st != 200 or "tree" not in r:
            raise RuntimeError("tree listing failed: %s" % st)
        return self._take(r)

    def _names_rest(self):
        parent, leaf = self.folder.rsplit("/", 1) if "/" in self.folder else ("", self.folder)
        st, items = self.api("GET", "/repos/%s/contents/%s?ref=%s" % (self.repo, parent, self.branch), timeout=30)
        if st != 200 or not isinstance(items, list):
            raise RuntimeError("parent listing failed: %s" % st)
        sha = next((i["sha"] for i in items if i.get("name") == leaf and i.get("type") == "dir"), None)
        if not sha:
            raise RuntimeError("memory folder not on %s" % self.branch)
        st, r = self.api("GET", "/repos/%s/git/trees/%s" % (self.repo, sha), timeout=60)
        if st != 200 or "tree" not in r:
            raise RuntimeError("tree listing failed: %s" % st)
        self.tree = sha
        return self._take(r)

    def _take(self, r):
        if r.get("truncated"):
            self.log("warning: the tree listing was truncated; some files will wait for a later run")
            self.tree = None    # a truncated listing is never recorded as complete
        self.shas = {e["path"]: e["sha"] for e in r["tree"] if e.get("type") == "blob"}
        return dict(self.shas)

    def prefetch(self, names):
        """Read the bodies of `names`, GQL_CHUNK per GraphQL query. A body that does not hash back to its blob id is
        left for read() to fetch by REST; a failed query leaves its whole chunk to read()."""
        owner, name = self.repo.split("/")
        todo = [(n, self.shas[n]) for n in names if self.shas.get(n) and n not in self.bodies]
        for i in range(0, len(todo), self.GQL_CHUNK):
            part = todo[i:i + self.GQL_CHUNK]
            q = " ".join('b%d: object(oid: "%s") { ... on Blob { text isBinary isTruncated } }' % (k, s)
                         for k, (_, s) in enumerate(part))
            try:
                d = self._gql('query { repository(owner: "%s", name: "%s") { %s } }' % (owner, name, q))["repository"]
            except (RuntimeError, KeyError, TypeError) as e:
                self.log("%s; %d bodies left to the one-by-one read" % (e, len(part)))
                continue
            for k, (n, s) in enumerate(part):
                b = (d or {}).get("b%d" % k) or {}
                if b.get("text") is None or b.get("isBinary") or b.get("isTruncated"):
                    continue
                data = b["text"].encode("utf-8")
                if blob_id(data) == s:   # the text field is decoded; keep it only if it hashes back
                    self.bodies[n] = data

    def read(self, name):
        if name in self.bodies:
            return self.bodies.pop(name)
        sha = self.shas.get(name)
        if sha:
            st, r = self._retry(lambda k: self.api("GET", "/repos/%s/git/blobs/%s" % (self.repo, sha), timeout=60),
                                "blob")
            if st == 200 and r.get("encoding") == "base64":
                return base64.b64decode(r["content"])
        st, r = self.api("GET", "/repos/%s/contents/%s/%s?ref=%s" % (self.repo, self.folder, name, self.branch),
                         timeout=30)
        if st != 200 or "content" not in r:
            raise RuntimeError("fetch failed: %s" % st)
        return base64.b64decode(r["content"])


def slug_date(name):
    m = re.search(r"(\d{4})_(\d\d)_(\d\d)\.md$", name)
    return m.groups() if m else ("", "", "")


def pull(source, mem, apply=False, cap=200, refresh=True, out=print):
    files = source.names()
    out("memory folder: %s" % mem)
    if getattr(source, "unchanged", False):
        out("the source folder is unchanged since the last run that brought in everything; nothing to read")
        return []
    local = set(os.listdir(mem))
    missing = [n for n in files if NAME.match(n) and n not in SKIP and n not in local]
    missing.sort()
    missing.sort(key=slug_date, reverse=True)   # newest first, so a capped run takes the fresh ones
    out("%d files at the source, %d here, %d at the source and missing here" % (len(files), len(local), len(missing)))
    complete = True
    if cap and len(missing) > cap:
        out("taking the newest %d this run (--max); the rest come on later runs" % cap)
        missing = missing[:cap]
        complete = False
    if apply and missing and hasattr(source, "prefetch"):
        source.prefetch(missing)
    wrote = []
    for n in missing:
        out(("  pull " if apply else "  would pull ") + n)
        if not apply:
            continue
        try:
            body = source.read(n)
        except Exception as e:
            out("    %s" % e)
            complete = False
            continue
        if not body.lstrip(b"\xef\xbb\xbf").startswith(b"---"):
            out("    skipped: no frontmatter")
            continue
        try:
            fd = os.open(os.path.join(mem, n), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)   # never overwrite
        except FileExistsError:
            continue
        with os.fdopen(fd, "wb") as fh:
            fh.write(body)
        wrote.append(n)
    if apply and wrote and refresh:
        bm = os.path.join(HERE, "bm25.py")
        if os.path.exists(bm):
            try:
                subprocess.run([sys.executable, bm, "refresh"], capture_output=True, timeout=600,
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            except Exception as e:
                out("bm25 refresh failed: %r" % e)
    if apply:
        out("wrote %d" % len(wrote))
        if hasattr(source, "finish"):
            source.finish(complete)
    return wrote


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)

    def opt(flag, default=None):
        return a[a.index(flag) + 1] if flag in a and a.index(flag) + 1 < len(a) else default

    apply = "--apply" in a
    cap = int(opt("--max", "200"))
    mem = mem_dir()
    if not mem or not os.path.isdir(mem):
        sys.exit("memory folder not found (set BRAIN_MEM_DIR)")
    if opt("--from-dir"):
        source = DirSource(opt("--from-dir"))
    else:
        repo = opt("--repo", os.environ.get("BRAIN_MEMORY_REPO"))
        folder = opt("--folder", os.environ.get("BRAIN_MEMORY_FOLDER"))
        if not repo or not folder:
            sys.exit("name a source: --from-dir PATH, or --repo owner/name --folder path (or BRAIN_MEMORY_REPO "
                     "and BRAIN_MEMORY_FOLDER)")
        source = RepoSource(repo, folder, opt("--branch", os.environ.get("BRAIN_MEMORY_BRANCH", "main")), mem=mem)
    wrote = pull(source, mem, apply=apply, cap=cap, refresh="--no-refresh" not in a)
    if apply:
        try:
            os.makedirs(os.path.dirname(STATE), exist_ok=True)
            with open(STATE, "w", encoding="utf-8") as fh:
                json.dump({"last": datetime.now(timezone.utc).isoformat(), "wrote": len(wrote),
                           "at": time.strftime("%Y-%m-%d %H:%M %z")}, fh)
        except OSError:
            pass


if __name__ == "__main__":
    if "-h" in sys.argv[1:] or "--help" in sys.argv[1:]:
        print((__doc__ or "").strip() or "usage: python %s" % os.path.basename(__file__))
        raise SystemExit(0)
    main()

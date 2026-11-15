"""Land a scanned commit's paths on origin/main through GitHub's Git Data API, as ONE commit.

Called by push_paths.sh after the git push lost the tip race (main moves about once a minute; a git retry costs a
22 s fetch plus the push hooks on the loaded box, so it loses again). Here a retry is a tree + commit + ref update,
about two seconds. The content is read from the scanned commit C0 (never from disk), so what lands is what the
secret scan saw. Before each try the new tip is compared with the tip the scan was built on: a path a peer changed
in between is refused, as push_paths.sh's own retry refuses it. The ref moves only by fast-forward (force false).

usage: push_paths_gitdata.py SLUG BASE C0 MSG path1 [path2 ...]     token in env PP_TOK
exit 0 landed / 3 refused or failed / 4 the API itself is unusable here (caller may try another route)
"""
import base64, threading, concurrent.futures, http.client, json, os, subprocess, sys, time, urllib.error, urllib.request

API = "https://api.github.com/repos/"

# 9 Nov (an agent): one row per process at exit in ~/.claude/fleet_board/rest_calls.jsonl, the same file
# fleet_board.py writes, so the hourly 5000-call core quota can be summed by script. Counting only; no behaviour change.
import atexit as _atexit, collections as _collections
_TALLY = _collections.Counter()
_REFUSED = [0]


_WRITTEN = _collections.Counter()
_REFUSED_WRITTEN = [0]


def _tally_row(partial=False):
    """Append the calls made since the last row (rows are deltas: sum them). Also written before every rate-limit wait
    (11 Nov): a pusher killed by `timeout` mid-wait never reached atexit, so its calls were never logged."""
    delta = _TALLY - _WRITTEN
    if not delta:
        return
    try:
        rec = {"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "pid": os.getpid(), "script": "push_paths_gitdata.py",
               "argv1": (sys.argv[1] if len(sys.argv) > 1 else ""),
               "rest": sum(v for k, v in delta.items() if k != "lock_wait_s" and not k.startswith("gql:")),
               "gql": sum(v for k, v in delta.items() if k.startswith("gql:")),
               "refused": _REFUSED[0] - _REFUSED_WRITTEN[0], "by": dict(delta.most_common(12))}
        if partial:
            rec["partial"] = True
        _WRITTEN.update(delta)
        _REFUSED_WRITTEN[0] = _REFUSED[0]
        d = os.environ.get("PP_TALLY_DIR") or os.path.join(os.path.expanduser("~"), ".claude", "fleet_board")
        with open(os.path.join(d, "rest_calls.jsonl"), "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec) + chr(10))
    except Exception:  # noqa: BLE001
        pass


_atexit.register(_tally_row)


# GitHub's secondary limit allows about 80 content-creating requests a minute. On 1 Nov eight parallel blob uploads ran
# near 150 a minute; after ~600 of them every request came back 403 and a 150-path batch gave up. So every POST/PATCH
# waits its turn (POST_GAP apart, about 70 a minute), and a rate-limit 403/429 is waited out, not treated as a refusal.
POST_GAP = float(os.environ.get("PP_POST_GAP", "0.85"))
_pace_lock = threading.Lock()
_last_post = [0.0]


def _pace():
    with _pace_lock:
        wait = _last_post[0] + POST_GAP - time.time()
        if wait > 0:
            time.sleep(wait)
        _last_post[0] = time.time()


def _rate_wait(e, txt, n):
    """Seconds to wait when this error is a rate limit, else None."""
    if e.code not in (403, 429):
        return None
    h = e.headers or {}
    ra, rem, reset = h.get("Retry-After"), h.get("X-RateLimit-Remaining"), h.get("X-RateLimit-Reset")
    if not (ra or rem == "0" or "rate limit" in txt.lower()):
        return None
    try:
        s = float(ra) if ra else (float(reset) - time.time() + 2 if rem == "0" and reset else 60.0 * (n + 1))
    except ValueError:
        s = 60.0 * (n + 1)
    return min(max(s, 5.0), 300.0)


def call(slug, method, path, body=None, tries=3, rate_waits=4):
    url = API + slug + path
    data = json.dumps(body).encode() if body is not None else None
    i = n = 0
    while True:
        if method != "GET":
            _pace()
        _key = "/".join(path.split("?")[0].split("/")[:3])
        _TALLY[method + " " + ("/compare" if _key.startswith("/compare/") else _key)] += 1
        q = urllib.request.Request(url, data=data, method=method, headers={
            "Authorization": "token " + os.environ["PP_TOK"], "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"})
        try:
            with urllib.request.urlopen(q, timeout=120) as r:
                return r.status, json.load(r)
        except urllib.error.HTTPError as e:
            txt = e.read()[:300].decode("utf-8", "replace")
            s = _rate_wait(e, txt, n)
            if s is not None:
                _REFUSED[0] += 1
            if s is not None and n < rate_waits:
                print("gitdata: rate limited (http %s), waiting %d s" % (e.code, s), flush=True)
                _tally_row(partial=True)
                time.sleep(s); n += 1; continue
            i += 1
            if (e.code >= 500 or e.code in (408, 499)) and i < tries:
                time.sleep(2 + 3 * (i - 1)); continue
            return e.code, {"message": txt}
        except (urllib.error.URLError, TimeoutError, OSError, http.client.HTTPException, ValueError) as e:
            # 7 Nov 08:35: IncompleteRead (an HTTPException, not an OSError) on a 1.2 MB reply escaped and failed a
            # batch whose 155 paths had in fact landed; a cut-off reply is retried like any network error
            i += 1
            if i < tries:
                time.sleep(2 + 3 * (i - 1)); continue
            return 0, {"message": str(e)}


class _LocalRefLock:
    """One ref race at a time on this machine (11 Nov). In the hour to 01:20 thirty pushers here made 207 tries at the
    main ref for at most 30 landings; each lost try costs six REST calls (ref, compare, commit, tree, commit, patch) and
    most were lost to another pusher on this same laptop. The 5,000-an-hour quota every agent shares hit zero at 01:22.
    An OS file lock (freed by the OS if the holder dies) around one try lets local pushers take turns; a pusher that
    cannot get it within PP_LOCK_WAIT seconds (default 60) goes ahead without it, as before, so a stuck holder never blocks a push."""
    WAIT = float(os.environ.get("PP_LOCK_WAIT", "60"))

    def __enter__(self):
        self.fh, t0 = None, time.time()
        try:
            d = os.path.join(os.path.expanduser("~"), ".claude", "fleet_board")
            os.makedirs(d, exist_ok=True)
            fh = open(os.path.join(d, "gitdata_ref.lock"), "a+b")
        except OSError:
            return self
        while True:
            try:
                if os.name == "nt":
                    import msvcrt
                    fh.seek(0)
                    msvcrt.locking(fh.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
                self.fh = fh
                break
            except OSError:
                if time.time() - t0 >= self.WAIT:
                    print("gitdata: local push lock busy %.0f s; going ahead without it" % (time.time() - t0), flush=True)
                    fh.close()
                    return self
                time.sleep(0.25 + (os.getpid() % 7) * 0.05)
        w = time.time() - t0
        if w >= 1:
            print("gitdata: waited %.0f s for the local push lock" % w, flush=True)
        _TALLY["lock_wait_s"] += int(w)
        return self

    def __exit__(self, *exc):
        if self.fh is not None:
            try:
                if os.name == "nt":
                    import msvcrt
                    self.fh.seek(0)
                    msvcrt.locking(self.fh.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(self.fh, fcntl.LOCK_UN)
            except OSError:
                pass
            self.fh.close()
            self.fh = None
        return False


def _tip_blobs_graphql(slug, tip, paths):
    """{path: blob sha or None} at `tip` in ONE GraphQL request, or None if it failed. GraphQL has its own hourly
    allowance; the REST core one is shared by every agent on the token and was spent on 1 Nov, when 30 contents GETs
    waited out four rate limits and the push gave up."""
    owner, name = slug.split("/", 1)
    parts = ['p%d: object(expression: %s) { oid }' % (i, json.dumps("%s:%s" % (tip, p))) for i, p in enumerate(paths)]
    q = "query { repository(owner: %s, name: %s) { %s } }" % (json.dumps(owner), json.dumps(name), " ".join(parts))
    _TALLY["gql:query"] += 1
    req = urllib.request.Request("https://api.github.com/graphql", data=json.dumps({"query": q}).encode(),
                                 method="POST", headers={"Authorization": "bearer " + os.environ["PP_TOK"]})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.load(r)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, http.client.HTTPException) as e:
        print("gitdata: graphql %s" % str(e)[:120]); return None
    repo = (d.get("data") or {}).get("repository")
    if d.get("errors") or not isinstance(repo, dict):
        print("gitdata: graphql errors %s" % str(d.get("errors"))[:160]); return None
    return {p: (repo.get("p%d" % i) or {}).get("oid") for i, p in enumerate(paths)}


def _drop_landed(slug, tip, hit, paths, items, entries, known):
    """A path "changed since the scan" whose blob at `tip` IS our scanned blob was landed by us - an earlier run of this
    push whose wrapper was killed while the lander went on (6 Nov 07:13: the low-memory reaper took the shell, the
    orphan landed, and the retry refused rc 3 on its own commit). Drop those from the push; return what is still a
    real peer change. `known` maps path -> blob sha from a compare listing; otherwise the tip is asked."""
    now_of = dict(known or {})
    missing = [p for p in hit if not now_of.get(p)]
    if missing:
        got = _tip_blobs_graphql(slug, tip, missing) or {}
        now_of.update({p: got.get(p) for p in missing})
    ours = {p for p in hit if now_of.get(p) and now_of[p] == entries[p][1]}
    if ours:
        print("gitdata: %d path(s) already hold our scanned blob at the tip (an earlier run landed them): %s"
              % (len(ours), sorted(ours)[:3]))
    return (sorted(set(hit) - ours), [p for p in paths if p not in ours],
            [it for it in items if it["path"] not in ours])


def _changed_at_tip(slug, base, tip, paths):
    """Our paths whose blob at `tip` differs from the one at `base`, or None when a lookup failed. The base blobs come
    from the local clone (the scan was built on base); the tip's from one GraphQL request, else one contents GET a path."""
    from urllib.parse import quote
    was_of = {}
    for p in paths:
        r = subprocess.run(["git", "rev-parse", "--verify", "-q", "%s:%s" % (base, p)], capture_output=True)
        was_of[p] = r.stdout.decode().strip() or None
    now_of = _tip_blobs_graphql(slug, tip, paths)
    if now_of is not None:
        return sorted(p for p in paths if now_of[p] != was_of[p])
    hit = []
    for p in paths:
        was = was_of[p]
        st, d = call(slug, "GET", "/contents/%s?ref=%s" % (quote(p), tip))
        if st == 404:
            now = None
        elif st == 200 and isinstance(d, dict) and d.get("sha"):
            now = d["sha"]
        else:
            print("gitdata: contents %s http %s" % (p, st))
            return None
        if now != was:
            hit.append(p)
    return sorted(hit)


# The GraphQL lane (11 Nov). The REST core quota (5,000 an hour, every agent and computer on the token) read 5000 of
# 5000 used at 01:22 and again at 02:37 while the GraphQL allowance stood at 1 of 5000: in the hour to 02:42 the
# pushers on this laptop spent 1,554 REST calls for at most 49 landings, each lost ref race costing six. Here a try is
# two GraphQL requests (the tip with our paths' blobs, then createCommitOnBranch with expectedHeadOid), the file
# contents ride in the mutation so no blob uploads, and nothing draws on the REST quota. The REST lane below is kept
# for what this one cannot carry: a mode other than 100644, a large batch, or GraphQL itself refusing.
GQL = "https://api.github.com/graphql"
GQL_MAX_BYTES = int(float(os.environ.get("PP_GQL_MAX_BYTES", "20000000")))
GQL_MAX_PATHS = int(os.environ.get("PP_GQL_MAX_PATHS", "200"))


def _gql(query, variables=None, timeout=180):
    """(data, errors, http status) for one GraphQL request; never raises. Counted under gql:* in the tally."""
    _TALLY["gql:" + ("mutation" if query.lstrip().startswith("mutation") else "query")] += 1
    body = {"query": query}
    if variables is not None:
        body["variables"] = variables
    req = urllib.request.Request(GQL, data=json.dumps(body).encode(), method="POST",
                                 headers={"Authorization": "bearer " + os.environ["PP_TOK"]})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.load(r)
        if not isinstance(d, dict):
            return None, [{"type": "BAD_REPLY", "message": str(d)[:200]}], 200
        return d.get("data"), d.get("errors"), 200
    except urllib.error.HTTPError as e:
        txt = e.read()[:300].decode("utf-8", "replace")
        return None, [{"type": "HTTP_%s" % e.code, "message": txt}], e.code
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, http.client.HTTPException) as e:
        return None, [{"type": "NETWORK", "message": str(e)[:200]}], 0


def _gql_kind(errs):
    """stale / rate / network / other, from a GraphQL error list."""
    txt = " ".join("%s %s" % (e.get("type", ""), e.get("message", "")) for e in (errs or []) if isinstance(e, dict))
    low = txt.lower()
    # GitHub words a moved tip two ways: STALE_DATA "Expected branch to point to ..." when the tip had moved before
    # the request, and FORBIDDEN "is at <oid> but expected <oid>" when it moved while the commit was being made
    # (11 Nov 03:46; the REST contents API answers that race with HTTP 409 and the same text). Read as "other", the
    # second wording sent the push to the REST lane: 32 REST calls where two more GraphQL requests would have done.
    if "STALE_DATA" in txt or "expected branch to point to" in low or ("is at " in low and " but expected " in low):
        return "stale", txt
    if "RATE_LIMITED" in txt or "rate limit" in low or "HTTP_403" in txt or "HTTP_429" in txt:
        return "rate", txt
    # 408 and 499 are GitHub giving up on a slow request (a 2 MB commit on 11 Nov 06:30, empty body): the commit may
    # or may not have landed, exactly as with a 5xx. Read as "other" they sent the push to the REST lane.
    if "NETWORK" in txt or "HTTP_5" in txt or "HTTP_408" in txt or "HTTP_499" in txt:
        return "network", txt
    return "other", txt


def _gql_real_errors(errs):
    """The errors that are failures. GitHub answers a path that is absent at the tip with a null field AND a NOT_FOUND
    error naming that field (seen on the real API, 11 Nov); for a new file that is the answer, not a failure."""
    out = []
    for e in errs or []:
        pth = e.get("path") if isinstance(e, dict) else None
        last = str(pth[-1]) if pth else ""
        if isinstance(e, dict) and e.get("type") == "NOT_FOUND" and "target" in (pth or []) \
                and last[:1] == "f" and last[1:].isdigit():
            continue
        out.append(e)
    return out


def _land_graphql(slug, base, msg, paths, entries, at_base):
    """Land `paths` as ONE commit through GraphQL. Returns 0 landed (or already there), 3 refused, or None when this
    lane cannot carry the push (the caller goes on to the REST lane).

    The same rules as the REST lane: the content is the scanned commit's blobs (each hashed here and compared with the
    scanned blob id before anything is sent); a path whose blob at the tip differs from the base is a peer's change and
    refuses the push, unless the tip already holds our scanned blob (an earlier run landed it); the branch moves only
    from the tip that was checked (expectedHeadOid), never by force. After the landing the commit's own blobs and modes
    are read back in the mutation's reply and must be the scanned ones."""
    import hashlib
    if os.environ.get("PP_GQL", "1") == "0":
        return None
    if len(paths) > GQL_MAX_PATHS:
        return None
    for p in paths:
        # createCommitOnBranch cannot set a file mode: a new file lands 100644 and this lane does not ask what happens
        # to an existing executable or link, so anything but a plain file on both sides goes to the REST lane
        if entries[p][0] != "100644" or (at_base.get(p) and at_base[p][0] != "100644"):
            return None
    blobs, total = {}, 0
    for p in paths:
        raw = subprocess.run(["git", "cat-file", "blob", entries[p][1]], capture_output=True).stdout
        total += len(raw)
        if total > GQL_MAX_BYTES:
            return None
        if hashlib.sha1(b"blob %d\x00" % len(raw) + raw).hexdigest() != entries[p][1]:
            print("gitdata: graphql lane: the local blob for %s does not hash to its scanned id; using the REST lane" % p)
            return None
        blobs[p] = base64.b64encode(raw).decode()
    owner, name = slug.split("/", 1)
    head, _, rest = msg.partition("\n")
    message = {"headline": head.strip()}
    if rest.strip():
        message["body"] = rest.strip("\n")
    net = 0
    for attempt in range(1, 31):
        with _LocalRefLock():
            fields = " ".join("f%d: file(path: %s) { oid mode }" % (i, json.dumps(p)) for i, p in enumerate(paths))
            data, errs, _st = _gql('query { repository(owner: %s, name: %s) { ref(qualifiedName: "refs/heads/main") '
                                   '{ target { ... on Commit { oid %s } } } } }'
                                   % (json.dumps(owner), json.dumps(name), fields))
            tgt = (((data or {}).get("repository") or {}).get("ref") or {}).get("target") or {}
            tip = tgt.get("oid")
            errs = _gql_real_errors(errs)
            if errs or not tip:
                kind, txt = _gql_kind(errs)
                if kind == "network" and net < 3:
                    net += 1; time.sleep(3); continue
                print("gitdata: graphql tip read failed (%s: %s); using the REST lane" % (kind, txt[:140]), flush=True)
                return None
            now_of = {p: (tgt.get("f%d" % i) or {}).get("oid") for i, p in enumerate(paths)}
            ours = [p for p in paths if now_of[p] == entries[p][1]]
            hit = sorted(p for p in paths if p not in ours and now_of[p] != (at_base.get(p) or (None, None))[1])
            if hit:
                print("gitdata REFUSED: a peer changed %s since the scan; merge their change first" % hit[:3]); return 3
            if ours:
                print("gitdata: %d path(s) already hold our scanned blob at the tip (an earlier run landed them): %s"
                      % (len(ours), sorted(ours)[:3]))
                paths = [p for p in paths if p not in ours]
                if not paths:
                    print("gitdata: every path already holds our scanned blob at main %s; nothing to land" % tip); return 0
                fields = " ".join("f%d: file(path: %s) { oid mode }" % (i, json.dumps(p)) for i, p in enumerate(paths))
            inp = {"branch": {"repositoryNameWithOwner": slug, "branchName": "main"}, "message": message,
                   "expectedHeadOid": tip,
                   "fileChanges": {"additions": [{"path": p, "contents": blobs[p]} for p in paths]}}
            _pace()
            data, errs, _st = _gql("mutation($input: CreateCommitOnBranchInput!) { createCommitOnBranch(input: $input) "
                                   "{ commit { oid changedFilesIfAvailable %s } } }" % fields, {"input": inp})
            com = ((data or {}).get("createCommitOnBranch") or {}).get("commit") or {}
            if com.get("oid"):
                bad = [p for i, p in enumerate(paths)
                       if (com.get("f%d" % i) or {}).get("oid") != entries[p][1]
                       or (com.get("f%d" % i) or {}).get("mode") not in (None, 33188)]
                if bad:
                    print("gitdata REFUSED: commit %s LANDED but %s does not hold the scanned blob as a plain file; "
                          "look at it now" % (com["oid"], bad[:3]))
                    return 3
                n = com.get("changedFilesIfAvailable")
                note = "" if n is None or n <= len(paths) else " WARNING: the commit changed %d files" % n
                print("pushed %d path(s) by GraphQL as one commit %s onto %s (try %d)%s"
                      % (len(paths), com["oid"], tip, attempt, note))
                return 0
            kind, txt = _gql_kind(errs)
            if kind == "stale":
                print("gitdata: graphql try %d: the tip moved; retrying on the new tip" % attempt, flush=True)
            elif kind == "network" and net < 3:
                # the commit may have landed although the reply was lost: the next read of the tip shows our blobs
                net += 1
                print("gitdata: graphql try %d: %s; reading the tip again" % (attempt, txt[:120]), flush=True)
                time.sleep(3)
            else:
                print("gitdata: graphql commit failed (%s: %s); using the REST lane" % (kind, txt[:160]), flush=True)
                return None
        time.sleep(1)
    print("gitdata: gave up after 30 graphql tries"); return 3


def main():
    slug, base, c0, msg = sys.argv[1:5]
    paths = sys.argv[5:]
    out = subprocess.run(["git", "ls-tree", "-z", c0, "--"] + paths, capture_output=True).stdout.decode("utf-8")
    entries = {}
    for rec in filter(None, out.split("\0")):
        meta, p = rec.split("\t", 1)
        mode, typ, sha = meta.split()
        if typ == "blob":
            entries[p] = (mode, sha)
    if set(entries) != set(paths):
        print("gitdata REFUSED: the scanned commit lacks %s" % sorted(set(paths) - set(entries))[:3]); return 3
    # Only paths that differ from the base go up (2 Nov): push_paths.sh hands over every NAMED path, and a memory mirror
    # names hundreds of which a few changed. Each unchanged one cost a blob POST, about 70 a minute, and the account's
    # 5,000-an-hour REST quota drained at 75-160 calls a minute (2 Nov 02:35-02:47). An unchanged path stays as the tip
    # has it; if a peer changed it since, their version stands, which is what a push of no change should do.
    out = subprocess.run(["git", "ls-tree", "-z", base, "--"] + paths, capture_output=True).stdout.decode("utf-8")
    at_base = {}
    for rec in filter(None, out.split("\0")):
        meta, p = rec.split("\t", 1)
        mode, typ, sha = meta.split()
        at_base[p] = (mode, sha)
    same = {p for p in paths if at_base.get(p) == entries[p]}
    if same:
        paths = [p for p in paths if p not in same]
        print("gitdata: %d of %d path(s) already match the base; %d to land" % (len(same), len(same) + len(paths),
                                                                             len(paths)))
    if not paths:
        print("gitdata: nothing to land: every path already matches the base"); return 0
    # GraphQL first (11 Nov): it has its own hourly allowance and a lost race costs two requests, not six.
    grc = _land_graphql(slug, base, msg, paths, entries, at_base)
    if grc is not None:
        return grc
    # The blobs, once: GitHub hashes them the git way, so each returned sha must be the scanned blob id.
    # Eight uploads at once (1 Nov): one at a time took ~3 s each, 7-8 minutes for a 150-path batch.
    def up(p):
        mode, sha = entries[p]
        raw = subprocess.run(["git", "cat-file", "blob", sha], capture_output=True).stdout
        st, d = call(slug, "POST", "/git/blobs", {"content": base64.b64encode(raw).decode(), "encoding": "base64"})
        return p, sha, st, d
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:   # paced by _pace(); 4 keep the gap filled
        results = list(ex.map(up, paths))
    for p, sha, st, d in results:
        if st in (401, 403, 404):
            print("gitdata unusable: blobs http %s %s" % (st, d.get("message", "")[:120])); return 4
    for p, sha, st, d in results:
        if st != 201 or d.get("sha") != sha:
            print("gitdata REFUSED: blob for %s came back http %s sha %s, scanned %s" % (p, st, d.get("sha"), sha)); return 3
    items = [{"path": p, "mode": entries[p][0], "type": "blob", "sha": entries[p][1]} for p in paths]
    # The last tip at which none of our paths differed from base. A retry after a lost ref race only has to check
    # ok_tip...tip, a minute of peer commits, instead of base...tip again (1 Nov: 30 per-path GETs under the rate
    # limit took longer than main stays still, so every retry lost the race).
    ok_tip = base
    for attempt in range(1, 31):
        with _LocalRefLock():   # one ref race at a time on this machine (11 Nov)
            st, ref = call(slug, "GET", "/git/ref/heads/main")
            if st != 200:
                print("gitdata: ref read http %s" % st); time.sleep(3); continue
            tip = ref["object"]["sha"]
            if tip != ok_tip:
                st, cmp = call(slug, "GET", "/compare/%s...%s" % (ok_tip, tip))
                if st != 200:
                    print("gitdata: compare http %s" % st); time.sleep(3); continue
                files = cmp.get("files") or []
                if cmp.get("status") not in ("ahead", "identical"):
                    print("gitdata REFUSED: main is %s of the scanned base (rewound?)" % cmp.get("status")); return 3
                if len(files) >= 300:
                    # compare lists at most 300 files, so on a busy main it cannot say whether a peer touched ours
                    # (1 Nov: every push of a 27-path batch was refused here). Ask the tip for each of our paths instead.
                    hit = _changed_at_tip(slug, base, tip, paths)
                    if hit is None:
                        print("gitdata REFUSED: %d files changed since the scan and a per-path check failed" % len(files))
                        return 3
                    if hit:
                        hit, paths, items = _drop_landed(slug, tip, hit, paths, items, entries, None)
                    if hit:
                        print("gitdata REFUSED: a peer changed %s since the scan; merge their change first" % hit[:3]); return 3
                    if not paths:
                        print("gitdata: every path already holds our scanned blob at main %s; nothing to land" % tip); return 0
                    files = []
                hit = sorted({f["filename"] for f in files} & set(paths))
                if hit:
                    hit, paths, items = _drop_landed(slug, tip, hit, paths, items, entries,
                                                     {f["filename"]: f.get("sha") for f in files})
                if hit:
                    print("gitdata REFUSED: a peer changed %s since the scan; merge their change first" % hit[:3]); return 3
                if not paths:
                    print("gitdata: every path already holds our scanned blob at main %s; nothing to land" % tip); return 0
                ok_tip = tip
            st, com = call(slug, "GET", "/git/commits/" + tip)
            if st != 200:
                print("gitdata: commit read http %s" % st); time.sleep(3); continue
            st, tree = call(slug, "POST", "/git/trees", {"base_tree": com["tree"]["sha"], "tree": items})
            if st != 201:
                print("gitdata: tree http %s %s" % (st, tree.get("message", "")[:120])); time.sleep(3); continue
            st, new = call(slug, "POST", "/git/commits", {"message": msg, "tree": tree["sha"], "parents": [tip]})
            if st != 201:
                print("gitdata: commit http %s %s" % (st, new.get("message", "")[:120])); time.sleep(3); continue
            st, upd = call(slug, "PATCH", "/git/refs/heads/main", {"sha": new["sha"], "force": False}, tries=1)
            if st == 200:
                # the landed commit must change exactly the named paths
                st, chk = call(slug, "GET", "/compare/%s...%s" % (tip, new["sha"]))
                got = {f["filename"] for f in (chk.get("files") or [])} if st == 200 else None
                note = "" if got is None or got <= set(paths) else " WARNING: also changed %s" % sorted(got - set(paths))[:3]
                print("pushed %d path(s) by the Git Data API as one commit %s onto %s (try %d)%s"
                      % (len(paths), new["sha"], tip, attempt, note))
                return 0
            print("gitdata: ref update try %d http %s (the tip moved); retrying on the new tip" % (attempt, st))
        time.sleep(1)
    print("gitdata: gave up after 30 ref tries"); return 3


if __name__ == "__main__":
    sys.exit(main())

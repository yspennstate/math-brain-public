"""test_memory_pull.py - memory_pull copies only what is missing, never overwrites, never deletes, and its repository
source keeps its speedups: an unchanged tree is not listed again, the listing is read gzipped, bodies come 40 to a
GraphQL query and are kept only when they hash back to their blob id, and a status 0 is retried.

    python test_memory_pull.py [PATH_TO_memory_pull.py]

Runs in a temporary folder with a directory source, a fake repository source and a local HTTP server; no network,
no installed brain.
"""
if "-h" in __import__("sys").argv[1:] or "--help" in __import__("sys").argv[1:]:
    print((__doc__ or "").strip() or "usage: python %s" % __import__("os").path.basename(__file__))
    raise SystemExit(0)
import base64
import gzip
import http.server
import importlib.util
import json
import os
import re
import shutil
import sys
import tempfile
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(HERE, "memory_pull.py")
sys.path.insert(0, os.path.dirname(PATH))
spec = importlib.util.spec_from_file_location("memory_pull_under_test", PATH)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
FAILS = []
TOTAL = [0]


def run(name, ok):
    TOTAL[0] += 1
    print("%s  %s" % ("PASS" if ok else "FAIL", name))
    if not ok:
        FAILS.append(name)


def note(desc):
    return ("---\nname: x\ndescription: %s\n---\n\nbody\n" % desc).encode()


def write(folder, name, body):
    with open(os.path.join(folder, name), "wb") as fh:
        fh.write(body)


def read(folder, name):
    with open(os.path.join(folder, name), "rb") as fh:
        return fh.read()


def fresh(root, name):
    p = os.path.join(root, name)
    os.makedirs(p)
    return p


root = tempfile.mkdtemp(prefix="memory_pull_test_")
src, here = fresh(root, "src"), fresh(root, "here")
write(src, "alpha_fact_2026_01_05.md", note("alpha"))
write(src, "beta_fact_2026_03_01.md", note("beta"))
write(src, "shared_fact_2026_02_01.md", note("theirs"))
write(src, "no_front_matter_2026_02_02.md", b"just text\n")
write(src, "MEMORY.md", b"- index line\n")
write(src, "Bad Name.md", note("bad"))
write(here, "shared_fact_2026_02_01.md", note("mine"))
write(here, "local_only_2026_01_01.md", note("local"))
quiet = lambda *_: None

# 1. dry run writes nothing
got = M.pull(M.DirSource(src), here, apply=False, refresh=False, out=quiet)
run("1 a dry run writes nothing", got == [] and sorted(os.listdir(here)) == ["local_only_2026_01_01.md",
                                                                          "shared_fact_2026_02_01.md"])
# 2. apply copies the missing memories, newest slug date first
got = M.pull(M.DirSource(src), here, apply=True, refresh=False, out=quiet)
run("2 the missing memories arrive, newest first: %s" % got,
    got == ["beta_fact_2026_03_01.md", "alpha_fact_2026_01_05.md"])
# 3. a local file with the same name keeps its own content
run("3 a local edit is never overwritten", read(here, "shared_fact_2026_02_01.md") == note("mine"))
# 4. nothing local is deleted
run("4 a file only here stays", os.path.exists(os.path.join(here, "local_only_2026_01_01.md")))
# 5. indexes, bad names and files without frontmatter are skipped
run("5 MEMORY.md, a bad name and a file without frontmatter are skipped",
    not any(os.path.exists(os.path.join(here, n)) for n in ("MEMORY.md", "Bad Name.md", "no_front_matter_2026_02_02.md")))
# 6. a second run is a no-op
run("6 a second run copies nothing", M.pull(M.DirSource(src), here, apply=True, refresh=False, out=quiet) == [])
# 7. the cap takes the newest first
got = M.pull(M.DirSource(src), fresh(root, "here2"), apply=True, cap=1, refresh=False, out=quiet)
run("7 --max 1 takes the newest: %s" % got, got == ["beta_fact_2026_03_01.md"])


class FakeRepo(M.RepoSource):
    """The repository source with its network replaced: GraphQL answers the folder's tree id and blob texts, the
    gzipped listing and the REST blob read answer from `files`. `zero` makes the next N calls return status 0."""

    def __init__(self, files, state, tree="T1", bad=(), zero=0, gql_down=False):
        self.repo, self.folder, self.branch = "o/r", "notes/memory", "main"
        self.state, self.key = state, "fake"
        self.tree, self.unchanged, self.shas, self.bodies = None, False, {}, {}
        self.files, self.tree_id, self.bad, self.zero, self.gql_down = files, tree, set(bad), zero, gql_down
        self.calls, self.slept = [], []
        self.sleep, self.log = self.slept.append, quiet
        self.ids = {n: M.blob_id(b) for n, b in files.items()}

    def _zero(self):
        if self.zero:
            self.zero -= 1
            return True
        return False

    def api(self, method, url, body=None, timeout=30):
        if url == "/graphql":
            q = body["query"]
            if self.gql_down:
                self.calls.append("gql-down")
                return 403, {}
            if self._zero():
                self.calls.append("gql-0")
                return 0, {}
            if "expression:" in q:
                self.calls.append("gql-tree")
                return 200, {"data": {"repository": {"object": {"oid": self.tree_id}}}}
            self.calls.append("gql-blobs")
            by_id = {i: n for n, i in self.ids.items()}
            rep = {}
            for k, s in re.findall(r'b(\d+): object\(oid: "([0-9a-f]+)"\)', q):
                n = by_id[s]
                text = self.files[n].decode("utf-8")
                rep["b" + k] = {"text": text + ("tampered" if n in self.bad else ""), "isBinary": False,
                                "isTruncated": False}
            return 200, {"data": {"repository": rep}}
        if url.startswith("/repos/o/r/git/blobs/"):
            self.calls.append("rest-blob")
            s = url.rsplit("/", 1)[1]
            n = next(n for n, i in self.ids.items() if i == s)
            return 200, {"encoding": "base64", "content": base64.b64encode(self.files[n]).decode()}
        if url.startswith("/repos/o/r/contents/notes?"):
            self.calls.append("rest-parent")
            return 200, [{"name": "memory", "type": "dir", "sha": self.tree_id}]
        if url == "/repos/o/r/git/trees/%s" % self.tree_id:
            self.calls.append("rest-tree")
            return 200, self._listing()
        raise AssertionError("unexpected call " + url)

    def _listing(self):
        return {"tree": [{"path": n, "type": "blob", "sha": self.ids[n]} for n in self.files]}

    def get_gz(self, url, timeout):
        if self._zero():
            self.calls.append("gz-0")
            return 0, {}
        assert url == "/repos/o/r/git/trees/%s" % self.tree_id, url
        self.calls.append("gz-tree")
        return 200, self._listing()


many = {"m%02d_fact_2026_04_%02d.md" % (i, 1 + i % 28): note("m%d" % i) for i in range(45)}
many["MISTAKES.md"] = b"log\n"
st1 = os.path.join(root, "trees.json")

# 8. one GraphQL query names the tree, one gzipped call lists it, 45 bodies come in two GraphQL queries
here3 = fresh(root, "here3")
fake = FakeRepo(many, st1)
got = M.pull(fake, here3, apply=True, refresh=False, out=quiet)
run("8 tree by GraphQL, listing gzipped, 45 bodies in 2 queries, nothing by REST: %s" % fake.calls,
    len(got) == 45 and fake.calls == ["gql-tree", "gz-tree", "gql-blobs", "gql-blobs"]
    and all(read(here3, n) == many[n] for n in got))
# 9. the same tree again: no listing, no bodies
fake = FakeRepo(many, st1)
got = M.pull(fake, here3, apply=True, refresh=False, out=quiet)
run("9 an unchanged tree after a complete run is not listed: %s" % fake.calls,
    got == [] and fake.calls == ["gql-tree"] and fake.unchanged)
# 10. a new tree is listed again
fake = FakeRepo(dict(many, **{"new_fact_2026_05_01.md": note("n")}), st1, tree="T2")
got = M.pull(fake, here3, apply=True, refresh=False, out=quiet)
run("10 a changed tree is listed and only the new file read: %s" % got,
    got == ["new_fact_2026_05_01.md"] and fake.calls == ["gql-tree", "gz-tree", "gql-blobs"])
# 11. a body that does not hash back to its blob id is read by REST
here4 = fresh(root, "here4")
two = {"a_fact_2026_06_01.md": note("a"), "b_fact_2026_06_02.md": note("b")}
fake = FakeRepo(two, os.path.join(root, "t4.json"), bad=["a_fact_2026_06_01.md"])
got = M.pull(fake, here4, apply=True, refresh=False, out=quiet)
run("11 a tampered GraphQL body is dropped and the file read by REST: %s" % fake.calls,
    sorted(got) == sorted(two) and fake.calls.count("rest-blob") == 1
    and read(here4, "a_fact_2026_06_01.md") == two["a_fact_2026_06_01.md"])
# 12. status 0 is retried after 15 s and 45 s; a capped run is not recorded complete
here5 = fresh(root, "here5")
st5 = os.path.join(root, "t5.json")
fake = FakeRepo(two, st5, zero=2)
got = M.pull(fake, here5, apply=True, cap=1, refresh=False, out=quiet)
fake2 = FakeRepo(two, st5)
got2 = M.pull(fake2, here5, apply=True, refresh=False, out=quiet)
run("12 status 0 twice is waited out (%s), a capped run is listed again next time: %s"
    % (fake.slept, fake2.calls),
    fake.slept == [15, 45] and len(got) == 1 and len(got2) == 1 and "gz-tree" in fake2.calls)
# 13. GraphQL refused: the plain REST listing and one-by-one reads still bring everything in
here6 = fresh(root, "here6")
fake = FakeRepo(two, os.path.join(root, "t6.json"), gql_down=True)
got = M.pull(fake, here6, apply=True, refresh=False, out=quiet)
run("13 with GraphQL refused the REST path brings everything: %s" % fake.calls,
    sorted(got) == sorted(two) and "rest-parent" in fake.calls and fake.calls.count("rest-blob") == 2)
# 14. get_gz itself: a gzipped answer from a real HTTP server is decompressed and parsed
payload = {"tree": [{"path": "x_2026_01_01.md", "type": "blob", "sha": "0" * 40}] * 2000}
body = gzip.compress(json.dumps(payload).encode())
seen = {}


class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        seen["enc"] = self.headers.get("Accept-Encoding")
        self.send_response(200)
        self.send_header("Content-Encoding", "gzip")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


srv = http.server.HTTPServer(("127.0.0.1", 0), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
real = M.RepoSource.__new__(M.RepoSource)
real.BASE, real.token, real.log = "http://127.0.0.1:%d" % srv.server_address[1], (lambda: "t"), quiet
st, r = real.get_gz("/repos/o/r/git/trees/T", timeout=10)
srv.shutdown()
run("14 get_gz asks for gzip and decodes it (%d bytes on the wire for %d of JSON)"
    % (len(body), len(json.dumps(payload))),
    st == 200 and r == payload and seen.get("enc") == "gzip")
shutil.rmtree(root, ignore_errors=True)
print("%d of %d controls pass (%s)" % (TOTAL[0] - len(FAILS), TOTAL[0], PATH))
sys.exit(1 if FAILS else 0)

"""persist_batches.py - split the dream persist's staged set into parts the secret scanner can hold.

    python persist_batches.py plan <repo> <out_dir> [--max-bytes N] [--max-paths N] -- <owned path> [...]
    python persist_batches.py --selftest

scan_secrets.py refuses (exit 2) a staged set of more than 25,000 objects or 256 MB. That bound is right for one
night's work and wrong after a stall: on 9 Nov 2026 local main had sat 19 days behind, the persist staged those 19 days
at once, the scan answered "Git objects exceeded the bounded total scan size", and the persist aborted - as it would
have every night after, because the set only grows. `plan` reads what is staged under the owned paths
(`git diff --cached --raw HEAD`), packs the paths in name order into parts under --max-bytes of new content and
--max-paths paths, and writes each part as <out_dir>/batch_NNNN.nul, a NUL-separated literal pathspec list for
`git add -A --pathspec-from-file=F --pathspec-file-nul` and `git commit --only --pathspec-from-file=F
--pathspec-file-nul`. run_dream.ps1 commits every part but the last after the same staged scan, and sends the last one
through its ordinary path. The scanner is not loosened and nothing is committed unscanned.

It prints `BATCHES n` and one `BATCH i <paths> <bytes> <file>` line per part. Exit 0 on success (n may be 0 or 1, in
which case there is nothing to split); anything else means no usable plan.
"""
import os
import shutil
import subprocess
import sys
import tempfile

NOWIN = 0x08000000 if os.name == "nt" else 0
ZERO = "0" * 40
MAX_BYTES = 160 * 1024 * 1024       # the scanner's total is 256 MB; a part stays well under it
MAX_PATHS = 12000                   # the scanner's object count is 25,000


def git(repo, args, inp=None, env=None):
    e = dict(os.environ)
    e["GIT_NO_LAZY_FETCH"] = "1"
    if env:
        e.update(env)
    p = subprocess.run(["git", "-C", repo] + args, input=inp, capture_output=True, creationflags=NOWIN, env=e)
    if p.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args[:4]), p.stderr.decode("utf-8", "replace")[:200]))
    return p.stdout


def staged_entries(repo, owned):
    out = git(repo, ["--literal-pathspecs", "-c", "core.quotepath=false", "diff", "--cached", "--raw", "-z",
                     "--no-abbrev", "--no-renames", "HEAD", "--"] + list(owned))
    parts = out.split(b"\0")
    rows = []
    i = 0
    while i + 1 < len(parts) and parts[i].startswith(b":"):
        meta = parts[i][1:].decode("ascii").split()
        if len(meta) == 5:
            rows.append((parts[i + 1], meta[3]))
        i += 2
    return rows


def sizes(repo, oids):
    want = sorted(set(o for o in oids if o != ZERO))
    if not want:
        return {}
    out = git(repo, ["cat-file", "--batch-check"], ("\n".join(want) + "\n").encode("ascii"))
    have = {}
    for line in out.decode("ascii", "replace").splitlines():
        f = line.split()
        if len(f) == 3 and f[1] == "blob":
            have[f[0]] = int(f[2])
        elif len(f) == 3:
            have[f[0]] = 0                      # a submodule or tree entry adds no blob bytes
        else:
            raise RuntimeError("a staged object is not in this clone: " + line[:80])
    return have


def plan(repo, out_dir, owned, max_bytes=MAX_BYTES, max_paths=MAX_PATHS):
    rows = sorted(staged_entries(repo, owned))
    size = sizes(repo, [oid for _p, oid in rows])
    batches, cur, cur_bytes = [], [], 0
    for path, oid in rows:
        n = size.get(oid, 0)
        if cur and (cur_bytes + n > max_bytes or len(cur) + 1 > max_paths):
            batches.append((cur, cur_bytes))
            cur, cur_bytes = [], 0
        cur.append(path)
        cur_bytes += n
    if cur:
        batches.append((cur, cur_bytes))
    os.makedirs(out_dir, exist_ok=True)
    print("BATCHES %d" % len(batches))
    for i, (paths, nbytes) in enumerate(batches):
        name = os.path.join(out_dir, "batch_%04d.nul" % i)
        tmp = name + ".tmp"
        with open(tmp, "wb") as fh:
            fh.write(b"\0".join(paths) + b"\0")
        os.replace(tmp, name)
        print("BATCH %d %d %d %s" % (i, len(paths), nbytes, name))
    return 0


def selftest():
    fails = []
    n = [0]

    def check(name, cond, detail=""):
        n[0] += 1
        if not cond:
            fails.append(name + (" :: " + str(detail)[:300] if detail else ""))
        print(("ok   " if cond else "FAIL ") + name)

    ident = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t",
             "GIT_COMMITTER_EMAIL": "t@example.invalid", "GIT_CONFIG_NOSYSTEM": "1"}

    def g(repo, *args):
        return git(repo, list(args), env=ident).decode("utf-8", "replace")

    def write(repo, rel, text):
        p = os.path.join(repo, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)

    root = tempfile.mkdtemp(prefix="persist_batches_")
    try:
        repo = os.path.join(root, "r")
        os.makedirs(repo)
        g(repo, "init", "-q", "-b", "main")
        for i in range(6):
            write(repo, "own/a/f%d.md" % i, "base %d\n" % i)
        write(repo, "own/gone.md", "to be deleted\n")
        write(repo, "other/peer.txt", "peer base\n")
        g(repo, "add", "-A")
        g(repo, "commit", "-q", "-m", "base")
        base = g(repo, "rev-parse", "HEAD").strip()

        big = "x" * 1000
        for i in range(6):
            write(repo, "own/a/f%d.md" % i, "edit %d %s\n" % (i, big))
        for i in range(5):
            write(repo, "own/b/new [%d].md" % i, "new %d %s\n" % (i, big))      # brackets: pathspecs must stay literal
        os.remove(os.path.join(repo, "own/gone.md"))
        write(repo, "other/peer.txt", "peer staged\n")
        g(repo, "add", "-A", "--", "own")
        g(repo, "add", "--", "other/peer.txt")                                   # a peer's staged path, not ours

        out_dir = os.path.join(root, "parts")
        import io
        from contextlib import redirect_stdout
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = plan(repo, out_dir, ["own"], max_bytes=3500, max_paths=4)
        lines = buf.getvalue().splitlines()
        check("plan exit 0", rc == 0)
        files = sorted(f for f in os.listdir(out_dir) if f.endswith(".nul"))
        check("header names the part count", lines[0] == "BATCHES %d" % len(files), lines[:2])
        check("more than one part", len(files) >= 3, files)
        listed = []
        ok_bounds = True
        for ln in lines[1:]:
            f = ln.split(" ", 4)
            if int(f[2]) > 4 or int(f[3]) > 3500:
                ok_bounds = False
        for name in files:
            data = open(os.path.join(out_dir, name), "rb").read()
            listed += [p.decode("utf-8") for p in data.split(b"\0") if p]
        check("every part is inside both bounds", ok_bounds, lines)
        want = sorted(["own/a/f%d.md" % i for i in range(6)] + ["own/b/new [%d].md" % i for i in range(5)]
                      + ["own/gone.md"])
        check("the parts cover every staged owned path exactly once", sorted(listed) == want, listed)
        check("the peer's staged path is in no part", "other/peer.txt" not in listed)

        # the sequence run_dream.ps1 uses: each part but the last is added and committed alone
        for k, name in enumerate(files[:-1]):
            pf = os.path.join(out_dir, name)
            g(repo, "reset", "-q", "--", "own")
            g(repo, "--literal-pathspecs", "add", "-A", "--pathspec-from-file=" + pf, "--pathspec-file-nul")
            staged_now = sorted(p for p in g(repo, "-c", "core.quotepath=false", "diff", "--cached", "--name-only",
                                             "--", "own").splitlines() if p)
            part = sorted(p.decode("utf-8") for p in open(pf, "rb").read().split(b"\0") if p)
            check("part %d: exactly its paths are staged" % k, staged_now == part, (staged_now, part))
            g(repo, "--literal-pathspecs", "commit", "-q", "--only", "-m", "part %d" % k,
              "--pathspec-from-file=" + pf, "--pathspec-file-nul")
        g(repo, "reset", "-q", "--", "own")
        g(repo, "add", "-A", "--", "own")
        rest = sorted(p for p in g(repo, "-c", "core.quotepath=false", "diff", "--cached", "--name-only", "--",
                                   "own").splitlines() if p)
        last = sorted(p.decode("utf-8") for p in open(os.path.join(out_dir, files[-1]), "rb").read().split(b"\0") if p)
        check("after the parts, what is left staged is the last part", rest == last, (rest, last))
        g(repo, "commit", "-q", "--only", "-m", "last", "--", "own")
        check("one commit per part", g(repo, "rev-list", "--count", base + "..HEAD").strip() == str(len(files)))
        check("the owned tree in HEAD equals the working tree", g(repo, "status", "--porcelain", "--", "own").strip() == "")
        check("the deletion was committed", "own/gone.md" not in g(repo, "ls-tree", "-r", "--name-only", "HEAD"))
        check("the peer's path is still staged and uncommitted",
              g(repo, "diff", "--cached", "--name-only").strip() == "other/peer.txt"
              and g(repo, "show", "HEAD:other/peer.txt") == "peer base\n")

        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = plan(repo, os.path.join(root, "parts2"), ["own"])
        check("nothing staged under the owned paths gives zero parts", rc == 0 and buf.getvalue().strip() == "BATCHES 0",
              buf.getvalue())
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print("%s: %d checks, %d failed" % ("PASS" if not fails else "FAIL", n[0], len(fails)))
    for f in fails:
        print("  " + f)
    return 1 if fails else 0


def main():
    a = sys.argv[1:]
    if a == ["--selftest"]:
        return selftest()
    if len(a) >= 5 and a[0] == "plan" and "--" in a:
        cut = a.index("--")
        opts, owned = a[3:cut], a[cut + 1:]
        max_bytes, max_paths = MAX_BYTES, MAX_PATHS
        i = 0
        while i + 1 < len(opts):
            if opts[i] == "--max-bytes":
                max_bytes = int(opts[i + 1])
            elif opts[i] == "--max-paths":
                max_paths = int(opts[i + 1])
            i += 2
        if not owned:
            raise RuntimeError("no owned paths given")
        return plan(a[1], a[2], owned, max_bytes, max_paths)
    print(__doc__.split("\n\n")[0], file=sys.stderr)
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print("persist_batches: " + str(exc)[:300], file=sys.stderr)
        sys.exit(3)

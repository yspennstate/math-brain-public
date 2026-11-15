"""Fixture test for dream_tree_replay.py's held-log rule (2026-11-10).

    python test_replay_held.py [dir holding dream_tree_replay.py]

Several local commits each snapshot a .jsonl log that main also changed. The replay must carry a snapshot only when
it has a line the tree does not hold, replace an older carried snapshot that a newer one contains, and keep carrying
every other kind of file exactly as before.
"""
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = sys.argv[1] if len(sys.argv) > 1 else HERE
NOWIN = 0x08000000 if os.name == "nt" else 0
FAILS = []
N = [0]
CARRY = "12_cognitive_architecture/sync_carried/"


def run(args, cwd=None, ok=True, env=None):
    e = dict(os.environ)
    e.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t",
              "GIT_COMMITTER_EMAIL": "t@example.invalid", "GIT_CONFIG_NOSYSTEM": "1"})
    e.pop("DREAM_SYNC_MIRRORS", None)
    if env:
        e.update(env)
    p = subprocess.run(args, cwd=cwd, env=e, capture_output=True, creationflags=NOWIN)
    if ok and p.returncode != 0:
        raise RuntimeError("%s -> %d %s" % (" ".join(args[:6]), p.returncode, p.stderr.decode("utf-8", "replace")[:300]))
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def git(repo, *args, **kw):
    return run(["git", "-C", repo] + list(args), **kw)


def check(name, cond, detail=""):
    N[0] += 1
    if not cond:
        FAILS.append(name + (" :: " + str(detail)[:400] if detail else ""))
    print(("ok   " if cond else "FAIL ") + name)


def write(repo, rel, text):
    p = os.path.join(repo, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def commit(repo, msg):
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", msg)
    return git(repo, "rev-parse", "HEAD")[1].strip()


def show(repo, rev, path):
    rc, out, _ = git(repo, "show", rev + ":" + path, ok=False)
    return out if rc == 0 else None


def rows(tag, lo, hi):
    return "".join('{"k": "%s%d"}\n' % (tag, i) for i in range(lo, hi))


def main():
    root = tempfile.mkdtemp(prefix="replay_held_")
    try:
        origin = os.path.join(root, "origin.git")
        a = os.path.join(root, "writer")
        b = os.path.join(root, "reader")
        run(["git", "init", "-q", "--bare", "-b", "main", origin])
        run(["git", "clone", "-q", origin, a])
        git(a, "checkout", "-q", "-b", "main", ok=False)
        old = rows("old", 0, 6)
        write(a, "logs/P.jsonl", old)
        write(a, "logs/Q.jsonl", rows("q", 0, 4))
        write(a, "logs/R.jsonl", rows("r", 0, 4))
        write(a, "06_math/y.md", "y base\nline\n")
        commit(a, "base")
        git(a, "push", "-q", "origin", "HEAD:main")
        run(["git", "clone", "-q", origin, b])

        # local: three snapshots of P (grow, grow, shrink), Q rewritten with lines main keeps, R with a new line,
        # y.md with only lines main also has (a non-log file: the rule must not touch it)
        write(b, "logs/P.jsonl", old + rows("new", 0, 2))
        write(b, "logs/Q.jsonl", rows("q", 2, 4) + rows("q", 0, 2))
        write(b, "06_math/y.md", "y LOCAL\nline\n")
        l1 = commit(b, "local one")
        write(b, "logs/P.jsonl", old + rows("new", 0, 5))
        write(b, "logs/R.jsonl", rows("r", 0, 4) + rows("rnew", 0, 1))
        l2 = commit(b, "local two")
        write(b, "logs/P.jsonl", old + rows("new", 0, 3))
        l3 = commit(b, "local three")

        # main: P becomes another machine's short file and the old lines move to a split part; Q and R grow
        write(a, "logs/P.jsonl", rows("elsewhere", 0, 2))
        write(a, "logs/P.p01.jsonl", old)
        write(a, "logs/Q.jsonl", rows("q", 0, 4) + rows("qmain", 0, 2))
        write(a, "logs/R.jsonl", rows("r", 0, 4) + rows("rmain", 0, 2))
        write(a, "06_math/y.md", "y MAIN\nline\ny LOCAL\n")
        commit(a, "main moves on")
        git(a, "push", "-q", "origin", "HEAD:main")
        git(b, "fetch", "-q", "origin")
        onto = git(b, "rev-parse", "origin/main")[1].strip()

        rc, out, err = run([sys.executable, "-s", os.path.join(TOOLS, "dream_tree_replay.py"), b, onto], ok=False)
        lines = [l for l in out.splitlines() if l.strip()]
        check("replay exit 0", rc == 0, out + err)
        head = lines[-1] if lines else ""
        check("last line is a commit id", len(head) == 40 and all(c in "0123456789abcdef" for c in head), out)
        if rc != 0 or len(head) != 40:
            raise RuntimeError("replay did not produce a head; stopping")

        p1, p2, p3 = (CARRY + l[:10] + "/logs/P.jsonl" for l in (l1, l2, l3))
        check("P keeps main's version at its path", show(b, head, "logs/P.jsonl") == rows("elsewhere", 0, 2))
        check("the newest snapshot with new lines is carried whole",
              show(b, head, p2) == old + rows("new", 0, 5))
        check("an older snapshot the newer one contains is gone", show(b, head, p1) is None)
        check("a later snapshot with no line of its own is not carried", show(b, head, p3) is None)
        # the third local commit adds nothing once its snapshot is held, so it is dropped like any empty commit
        check("two commits remain", git(b, "rev-list", "--count", onto + ".." + head)[1].strip() == "2", out)
        mid = head
        first = git(b, "rev-parse", head + "~1")[1].strip()
        check("the first replayed commit did carry its snapshot (it had lines nothing held)",
              show(b, first, p1) == old + rows("new", 0, 2))
        check("the second replayed commit replaced it", show(b, mid, p1) is None and show(b, mid, p2) is not None)
        check("Q: every local line is on main, nothing carried",
              show(b, head, CARRY + l1[:10] + "/logs/Q.jsonl") is None)
        check("Q keeps main's version", show(b, head, "logs/Q.jsonl") == rows("q", 0, 4) + rows("qmain", 0, 2))
        check("R: one line main lacks, the local version is carried",
              show(b, head, CARRY + l2[:10] + "/logs/R.jsonl") == rows("r", 0, 4) + rows("rnew", 0, 1))
        check("a non-log file is carried even when main holds each of its lines",
              show(b, head, CARRY + l1[:10] + "/06_math/y.md") == "y LOCAL\nline\n")
        check("the output names the held rule", any("already holds" in l for l in lines), out)
        _, changed, _ = git(b, "diff", "--name-only", onto, head)
        want = sorted([CARRY + "README.md", p2, CARRY + l2[:10] + "/logs/R.jsonl", CARRY + l1[:10] + "/06_math/y.md"])
        check("against main the replay adds only the carried copies that hold something", sorted(changed.split()) == want,
              changed)
        # every local line is somewhere in the result
        have = set()
        for path in git(b, "ls-tree", "-r", "--name-only", head)[1].split():
            if path.endswith(".jsonl"):
                have |= set((show(b, head, path) or "").splitlines())
        local_lines = set()
        for c in (l1, l2, l3):
            for path in ("logs/P.jsonl", "logs/Q.jsonl", "logs/R.jsonl"):
                local_lines |= set((show(b, c, path) or "").splitlines())
        check("no local log line is lost", local_lines <= have, sorted(local_lines - have)[:5])

        spec = importlib.util.spec_from_file_location("dtr", os.path.join(TOOLS, "dream_tree_replay.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        check("a blob that is not in the store holds nothing (the doubt ends in a carry)",
              mod._held_log(b, head, "logs/P.jsonl", "1" * 40) == (False, []))
        check("an empty log is not called held",
              mod._held_log(b, head, "logs/P.jsonl", git(b, "hash-object", "-w", "--stdin", ok=False)[1].strip() or "0" * 40)
              == (False, []))
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print("%s: %d checks, %d failed" % ("PASS" if not FAILS else "FAIL", N[0], len(FAILS)))
    for f in FAILS:
        print("  " + f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())

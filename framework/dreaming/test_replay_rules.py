"""Fixture test for dream_tree_replay.py's published / carried rules (2026-11-10).

    python test_replay_rules.py [dir holding dream_tree_replay.py]

A local commit and main both edit ordinary files. The replay must keep main's version at each path, lose no local
bytes that main never had (they go under sync_carried/<commit>/), and still replay clean commits unchanged.
"""
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


def main():
    root = tempfile.mkdtemp(prefix="replay_fixture_")
    try:
        origin = os.path.join(root, "origin.git")
        a = os.path.join(root, "writer")
        b = os.path.join(root, "reader")
        run(["git", "init", "-q", "--bare", "-b", "main", origin])
        run(["git", "clone", "-q", origin, a])
        git(a, "checkout", "-q", "-b", "main", ok=False)
        body = "".join("line %d\n" % i for i in range(1, 9))
        for name in ("x", "y", "z", "w", "v"):
            write(a, "06_math/%s.md" % name, "%s base\n%s" % (name, body))
        commit(a, "base")
        git(a, "push", "-q", "origin", "HEAD:main")
        run(["git", "clone", "-q", origin, b])

        # the local commit (never pushed as a commit): x gets bytes that main also receives through another path,
        # y gets bytes main never has, z is deleted, v is edited only here
        write(b, "06_math/x.md", "x LOCAL-ONE\n" + body)
        write(b, "06_math/y.md", "y LOCAL-ONLY\n" + body)
        os.remove(os.path.join(b, "06_math/z.md"))
        write(b, "06_math/v.md", "v base\n" + body + "v local tail\n")
        l1 = commit(b, "local one")
        write(b, "06_math/w.md", "w base\n" + body + "w local tail\n")
        l2 = commit(b, "local two")
        write(b, "06_math/y.md", "y LOCAL-AGAIN\n" + body)
        l3 = commit(b, "local three")

        # main: publishes the same x bytes, then edits x again; edits y and z its own way
        write(a, "06_math/x.md", "x LOCAL-ONE\n" + body)
        commit(a, "x as the session pushed it")
        write(a, "06_math/x.md", "x MAIN-TWO\n" + body)
        write(a, "06_math/y.md", "y MAIN\n" + body)
        write(a, "06_math/z.md", "z MAIN\n" + body)
        commit(a, "main moves on")
        git(a, "push", "-q", "origin", "HEAD:main")
        git(b, "fetch", "-q", "origin")
        onto = git(b, "rev-parse", "origin/main")[1].strip()
        head_before = git(b, "rev-parse", "HEAD")[1].strip()

        rc, out, err = run([sys.executable, "-s", os.path.join(TOOLS, "dream_tree_replay.py"), b, onto], ok=False)
        lines = [l for l in out.splitlines() if l.strip()]
        check("replay exit 0", rc == 0, out + err)
        head = lines[-1] if lines else ""
        check("last line is a commit id", len(head) == 40 and all(c in "0123456789abcdef" for c in head), out)
        if rc != 0 or len(head) != 40:
            raise RuntimeError("replay did not produce a head; stopping")
        check("the replay moved no ref", git(b, "rev-parse", "HEAD")[1].strip() == head_before)
        check("the new head descends from main", git(b, "merge-base", "--is-ancestor", onto, head, ok=False)[0] == 0)
        check("three commits replayed", git(b, "rev-list", "--count", onto + ".." + head)[1].strip() == "3", out)

        check("published: x keeps main's newer version", show(b, head, "06_math/x.md") == "x MAIN-TWO\n" + body)
        check("published: x's local bytes are not carried (main already had them)",
              show(b, head, CARRY + l1[:10] + "/06_math/x.md") is None)
        check("carried: y keeps main's version at its path", show(b, head, "06_math/y.md") == "y MAIN\n" + body)
        check("carried: y's local bytes are under sync_carried/<commit>/",
              show(b, head, CARRY + l1[:10] + "/06_math/y.md") == "y LOCAL-ONLY\n" + body)
        check("carried: a later local edit of the same file is carried under its own commit",
              show(b, head, CARRY + l3[:10] + "/06_math/y.md") == "y LOCAL-AGAIN\n" + body)
        check("carried: the folder explains itself", (show(b, head, CARRY + "README.md") or "").startswith("# sync_carried"))
        check("deleted locally, edited on main: main's version stays", show(b, head, "06_math/z.md") == "z MAIN\n" + body)
        check("a file only the local commit edited keeps the local edit",
              show(b, head, "06_math/v.md") == "v base\n" + body + "v local tail\n")
        check("a clean later commit replays unchanged",
              show(b, head, "06_math/w.md") == "w base\n" + body + "w local tail\n")
        check("the output names the published rule", any("already published" in l for l in lines), out)
        check("the output names the carried rule", any("carried the local version" in l for l in lines), out)
        _, changed, _ = git(b, "diff", "--name-only", onto, head)
        want = sorted([CARRY + "README.md", CARRY + l1[:10] + "/06_math/y.md", CARRY + l3[:10] + "/06_math/y.md",
                       "06_math/v.md", "06_math/w.md"])
        check("against main the replay changes only the local-only edits and the carried copies",
              sorted(changed.split()) == want, changed)
        _, msgs, _ = git(b, "log", "--format=%s", onto + ".." + head)
        check("commit messages kept", msgs.split("\n")[:3] == ["local three", "local two", "local one"], msgs)
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print("%s: %d checks, %d failed" % ("PASS" if not FAILS else "FAIL", N[0], len(FAILS)))
    for f in FAILS:
        print("  " + f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())

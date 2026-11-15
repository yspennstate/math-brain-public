"""Fixture test for dream_sync_index.py absent / undo and dream_sync_facts.py in a blob:none clone.

    python test_absent_move.py [dir holding the two helpers]

Builds a bare origin, a writer clone (another computer) and a partial reader clone (this computer), then checks that
the move brings the reader to the new main without writing or downloading the files it never held.
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


def run(args, cwd=None, env=None, ok=True, inp=None):
    e = dict(os.environ)
    e.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t",
              "GIT_COMMITTER_EMAIL": "t@example.invalid", "GIT_CONFIG_NOSYSTEM": "1"})
    if env:
        e.update(env)
    p = subprocess.run(args, cwd=cwd, env=e, capture_output=True, input=inp, creationflags=NOWIN)
    if ok and p.returncode != 0:
        raise RuntimeError("%s -> %d %s" % (" ".join(args[:6]), p.returncode, p.stderr.decode("utf-8", "replace")[:300]))
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def git(repo, *args, **kw):
    return run(["git", "-C", repo] + list(args), **kw)


def check(name, cond, detail=""):
    N[0] += 1
    if not cond:
        FAILS.append(name + (" :: " + str(detail)[:300] if detail else ""))
    print(("ok   " if cond else "FAIL ") + name)


def write(repo, rel, text):
    p = os.path.join(repo, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def commit_push(repo, msg):
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", msg)
    git(repo, "push", "-q", "origin", "HEAD:main")


def has_blob(repo, oid):
    rc, _, _ = git(repo, "cat-file", "-e", oid, ok=False, env={"GIT_NO_LAZY_FETCH": "1"})
    return rc == 0


def flags(repo):
    _, out, _ = git(repo, "ls-files", "-v")
    return {l[2:]: l[0] for l in out.splitlines() if len(l) > 2}


def oid(repo, rev, path):
    return git(repo, "rev-parse", rev + ":" + path)[1].strip()


def absent(repo, old, target, stem):
    rc, _, err = run([sys.executable, "-s", os.path.join(TOOLS, "dream_sync_index.py"), "absent", repo, old, target,
                      stem + ".staged", stem + ".undo"], ok=False)
    staged = []
    if rc == 0:
        staged = [l for l in open(stem + ".staged", encoding="utf-8").read().splitlines() if l]
    return rc, sorted(staged), err


def main():
    root = tempfile.mkdtemp(prefix="absent_fixture_")
    try:
        origin = os.path.join(root, "origin.git")
        a = os.path.join(root, "writer")
        b = os.path.join(root, "reader")
        run(["git", "init", "-q", "--bare", "-b", "main", origin])
        git(origin, "config", "uploadpack.allowfilter", "true")
        git(origin, "config", "uploadpack.allowanysha1inwant", "true")
        run(["git", "clone", "-q", origin, a])
        git(a, "checkout", "-q", "-b", "main", ok=False)
        write(a, "01_ai_consciousness/a.md", "a1\n")
        write(a, "12_x/keep.txt", "keep1\n")
        write(a, "README.md", "readme\n")
        commit_push(a, "base")
        url = "file:///" + origin.replace("\\", "/")
        run(["git", "clone", "-q", "--filter=blob:none", url, b])
        rc, out, _ = git(b, "config", "remote.origin.promisor")
        check("reader is a partial clone", out.strip() == "true", out)

        # night 1: the writer adds outputs the reader never held, a memory file, a top-level file, and edits keep.txt
        write(a, "12_x/other/out1.txt", "out1 v1\n")
        write(a, "12_x/other/out2.txt", "out2 v1\n")
        write(a, "12_x/other/held.txt", "held v1\n")
        write(a, "01_ai_consciousness/new.md", "new1\n")
        write(a, "TOP.md", "top\n")
        write(a, "12_x/keep.txt", "keep2\n")
        commit_push(a, "night 1")
        git(b, "fetch", "-q", "origin")
        old = git(b, "rev-parse", "HEAD")[1].strip()
        target = git(b, "rev-parse", "origin/main")[1].strip()
        write(b, "12_x/other/held.txt", "held v1\n")           # an untracked copy the reader does hold
        o1 = oid(b, target, "12_x/other/out1.txt")
        check("night 1: incoming blob is not here before the move", not has_blob(b, o1))

        # facts helper must not download while answering
        pf = os.path.join(root, "paths.txt")
        tsv = os.path.join(root, "facts.tsv")
        _, names, _ = git(b, "diff", "--name-only", old, target)
        open(pf, "w", encoding="utf-8", newline="\n").write(names)
        rc, _, err = run([sys.executable, "-s", os.path.join(TOOLS, "dream_sync_facts.py"), b, target, pf, tsv], ok=False)
        check("facts helper exit 0", rc == 0, err)
        rows = {r.split("\t")[0]: r.split("\t") for r in open(tsv, encoding="utf-8").read().splitlines()}
        check("facts: incoming id of an absent file is the target's", rows["12_x/other/out1.txt"][4] == o1, rows)
        check("facts: absent file reported as not existing, untracked", rows["12_x/other/out1.txt"][1:3] == ["0", "0"])
        check("facts: held copy has local id equal to incoming", rows["12_x/other/held.txt"][3] ==
              rows["12_x/other/held.txt"][4] != "", rows["12_x/other/held.txt"])
        check("facts: answering downloaded nothing", not has_blob(b, o1))

        rc, staged, err = absent(b, old, target, os.path.join(root, "n1"))
        check("night 1: absent exit 0", rc == 0, err)
        check("night 1: only the two files outside the kept trees and not on disk are indexed",
              staged == ["12_x/other/out1.txt", "12_x/other/out2.txt"], staged)
        # the held untracked copy blocks reset --keep unless it is indexed in place (the sync's `stage` mode does that)
        sp = os.path.join(root, "stage_paths.txt")
        open(sp, "w", encoding="utf-8", newline="\n").write("12_x/other/held.txt\n")
        run([sys.executable, "-s", os.path.join(TOOLS, "dream_sync_index.py"), "stage", b, old, target, sp,
             os.path.join(root, "s1.staged"), os.path.join(root, "s1.undo")])
        rc, _, err = git(b, "reset", "-q", "--keep", target, ok=False)
        check("night 1: reset --keep accepted", rc == 0, err)
        check("night 1: absent files were not written", not os.path.exists(os.path.join(b, "12_x/other/out1.txt"))
              and not os.path.exists(os.path.join(b, "12_x/other/out2.txt")))
        check("night 1: absent blobs were not downloaded", not has_blob(b, o1))
        check("night 1: memory tree and top-level files were written",
              open(os.path.join(b, "01_ai_consciousness/new.md")).read() == "new1\n"
              and os.path.exists(os.path.join(b, "TOP.md")))
        check("night 1: tracked file updated", open(os.path.join(b, "12_x/keep.txt")).read() == "keep2\n")
        fl = flags(b)
        check("night 1: absent files carry skip-worktree", fl.get("12_x/other/out1.txt") == "S"
              and fl.get("12_x/other/out2.txt") == "S", fl)
        check("night 1: held file is an ordinary tracked file", fl.get("12_x/other/held.txt") == "H", fl)
        _, st, _ = git(b, "status", "--porcelain")
        check("night 1: status clean", st.strip() == "", st)
        check("night 1: HEAD is the target", git(b, "rev-parse", "HEAD")[1].strip() == target)

        # night 2: the writer edits one absent file, deletes another, adds a third
        write(a, "12_x/other/out1.txt", "out1 v2\n")
        os.remove(os.path.join(a, "12_x/other/out2.txt"))
        write(a, "12_x/other/out3.txt", "out3 v1\n")
        commit_push(a, "night 2")
        git(b, "fetch", "-q", "origin")
        old, target = target, git(b, "rev-parse", "origin/main")[1].strip()
        o1b = oid(b, target, "12_x/other/out1.txt")
        rc, staged, err = absent(b, old, target, os.path.join(root, "n2"))
        check("night 2: absent exit 0", rc == 0, err)
        check("night 2: the edited absent file and the new one are indexed", staged ==
              ["12_x/other/out1.txt", "12_x/other/out3.txt"], staged)
        rc, _, err = git(b, "reset", "-q", "--keep", target, ok=False)
        check("night 2: reset --keep accepted", rc == 0, err)
        fl = flags(b)
        check("night 2: edited absent file still unwritten, flagged, not downloaded",
              not os.path.exists(os.path.join(b, "12_x/other/out1.txt")) and fl.get("12_x/other/out1.txt") == "S"
              and not has_blob(b, o1b), fl)
        check("night 2: deleted absent file left the index", "12_x/other/out2.txt" not in fl, fl)
        check("night 2: index entry is the target's", git(b, "ls-files", "-s", "12_x/other/out1.txt")[1].split()[1] == o1b)
        _, st, _ = git(b, "status", "--porcelain")
        check("night 2: status clean", st.strip() == "", st)

        # night 3: the move is refused (a local edit of a tracked incoming file); undo must put the index back
        write(a, "12_x/other/out1.txt", "out1 v3\n")
        write(a, "12_x/other/out4.txt", "out4 v1\n")
        write(a, "12_x/keep.txt", "keep3\n")
        commit_push(a, "night 3")
        git(b, "fetch", "-q", "origin")
        old, target = target, git(b, "rev-parse", "origin/main")[1].strip()
        write(b, "12_x/keep.txt", "local edit\n")
        before = git(b, "ls-files", "-s", "-v")[1]
        stem = os.path.join(root, "n3")
        rc, staged, err = absent(b, old, target, stem)
        check("night 3: absent exit 0", rc == 0, err)
        check("night 3: two paths indexed", staged == ["12_x/other/out1.txt", "12_x/other/out4.txt"], staged)
        rc, _, err = git(b, "reset", "-q", "--keep", target, ok=False)
        check("night 3: reset --keep refused", rc != 0)
        rc, _, err = run([sys.executable, "-s", os.path.join(TOOLS, "dream_sync_index.py"), "undo", b, stem + ".undo"],
                         ok=False)
        check("night 3: undo exit 0", rc == 0, err)
        after = git(b, "ls-files", "-s", "-v")[1]
        check("night 3: index is exactly as before (entries and flags)", before == after,
              "\n" + before + "\n---\n" + after)
        check("night 3: nothing staged", git(b, "diff", "--cached", "--name-only")[1].strip() == "")
        _, st, _ = git(b, "status", "--porcelain")
        check("night 3: status shows only the local edit", st.strip() == "M 12_x/keep.txt", st)
        check("night 3: HEAD unmoved", git(b, "rev-parse", "HEAD")[1].strip() == old)

        # reading an absent file on demand still works (the blob is fetched only then)
        rc, out, _ = git(b, "show", "HEAD:12_x/other/out1.txt", ok=False)
        check("an absent file can still be read on demand", rc == 0 and out == "out1 v2\n", out)
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print("%s: %d checks, %d failed" % ("PASS" if not FAILS else "FAIL", N[0], len(FAILS)))
    for f in FAILS:
        print("  " + f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())

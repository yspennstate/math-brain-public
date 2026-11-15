"""Fixture test for dream_tree_replay.py's batched index write (2026-11-10).

    python test_replay_batch.py [dir holding the new dream_tree_replay.py [the older dream_tree_replay.py to compare]]

A local commit and main both edit a set of memory-mirror files, and the live memory folder holds a third version of
each. The replay must resolve every one to the live bytes, in one index write. Checked three ways: the stored bytes
equal the live files; the tree equals the tree the older per-file tool builds on the same fixture; and with
core.autocrlf on, where the batch is not exact, the tool falls back and stores what `git add` would store.
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = sys.argv[1] if len(sys.argv) > 1 else HERE
OLD = sys.argv[2] if len(sys.argv) > 2 else None
NOWIN = 0x08000000 if os.name == "nt" else 0
FAILS = []
N = [0]
PREFIX = "01_ai_consciousness/claude/memory/"
NAMES = ["alpha_one.md", "beta two.md", "gamma.md", "delta_crlf.md", "epsilon.md", "zeta.md"]
UNAMES = ["alpha_one.md", "beta two.md", "gamma_café.md", "delta_crlf.md"]


def run(args, cwd=None, ok=True, env=None, inp=None):
    e = dict(os.environ)
    e.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t",
              "GIT_COMMITTER_EMAIL": "t@example.invalid", "GIT_CONFIG_NOSYSTEM": "1"})
    e.pop("DREAM_SYNC_MIRRORS", None)
    e.pop("DREAM_REPLAY_PROGRESS", None)
    if env:
        e.update(env)
    p = subprocess.run(args, cwd=cwd, env=e, capture_output=True, creationflags=NOWIN, input=inp)
    if ok and p.returncode != 0:
        raise RuntimeError("%s -> %d %s" % (" ".join(args[:6]), p.returncode, p.stderr.decode("utf-8", "replace")[:300]))
    return p.returncode, p.stdout, p.stderr.decode("utf-8", "replace")


def git(repo, *args, **kw):
    rc, out, err = run(["git", "-C", repo] + list(args), **kw)
    return rc, out.decode("utf-8", "replace"), err


def check(name, cond, detail=""):
    N[0] += 1
    if not cond:
        FAILS.append(name + (" :: " + str(detail)[:400] if detail else ""))
    print(("ok   " if cond else "FAIL ") + name)


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)


def commit(repo, msg):
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", msg)
    return git(repo, "rev-parse", "HEAD")[1].strip()


def blob_bytes(repo, rev, path):
    rc, out, _ = run(["git", "-C", repo, "cat-file", "blob", "%s:%s" % (rev, path)], ok=False)
    return out if rc == 0 else None


def build(root, tag, autocrlf, NAMES=NAMES):
    origin = os.path.join(root, tag + "_origin.git")
    a = os.path.join(root, tag + "_writer")
    b = os.path.join(root, tag + "_reader")
    live = os.path.join(root, tag + "_live")
    run(["git", "init", "-q", "--bare", "-b", "main", origin])
    run(["git", "clone", "-q", origin, a])
    git(a, "checkout", "-q", "-b", "main", ok=False)
    git(a, "config", "core.autocrlf", "false")
    body = b"".join(b"line %d\n" % i for i in range(1, 9))
    for n in NAMES + ["quiet.md"]:
        write(os.path.join(a, PREFIX, n), n.encode("utf-8") + b" base\n" + body)
    write(os.path.join(a, "06_math", "plain.md"), b"plain base\n" + body)
    commit(a, "base")
    git(a, "push", "-q", "origin", "HEAD:main")
    run(["git", "clone", "-q", origin, b])
    git(b, "config", "core.autocrlf", "false")
    for n in NAMES:
        write(os.path.join(b, PREFIX, n), n.encode("utf-8") + b" LOCAL\n" + body)
    write(os.path.join(b, "06_math", "plain.md"), b"plain base\n" + body + b"local tail\n")
    commit(b, "local one")
    for n in NAMES[:3]:
        write(os.path.join(b, PREFIX, n), n.encode("utf-8") + b" LOCAL AGAIN\n" + body)
    commit(b, "local two")
    for n in NAMES:
        write(os.path.join(a, PREFIX, n), n.encode("utf-8") + b" MAIN\n" + body)
    commit(a, "main moves on")
    git(a, "push", "-q", "origin", "HEAD:main")
    git(b, "fetch", "-q", "origin")
    for n in NAMES:
        data = n.encode("utf-8") + b" LIVE\n" + body + b"live tail\n"
        if n == "delta_crlf.md":
            data = data.replace(b"\n", b"\r\n")
        write(os.path.join(live, n), data)
    git(b, "config", "core.autocrlf", "true" if autocrlf else "false")
    onto = git(b, "rev-parse", "origin/main")[1].strip()
    return b, live, onto


def replay(tool, repo, onto, live, env=None):
    rc, out, err = run([sys.executable, "-s", tool, repo, onto, live, PREFIX], ok=False, env=env)
    lines = [l for l in out.decode("utf-8", "replace").splitlines() if l.strip()]
    head = lines[-1] if lines else ""
    return rc, head, out.decode("utf-8", "replace") + err


def main():
    root = tempfile.mkdtemp(prefix="replay_batch_")
    new = os.path.join(TOOLS, "dream_tree_replay.py")
    try:
        b, live, onto = build(root, "p", autocrlf=False)
        before = git(b, "rev-parse", "HEAD")[1].strip()
        prog = os.path.join(root, "progress.txt")
        rc, head, text = replay(new, b, onto, live, env={"DREAM_REPLAY_PROGRESS": prog})
        check("replay exit 0", rc == 0, text)
        check("last line is a commit id", len(head) == 40, text)
        if rc != 0 or len(head) != 40:
            print(text[:1500])
            raise RuntimeError("no head; stopping")
        for n in NAMES:
            with open(os.path.join(live, n), "rb") as fh:
                want = fh.read()
            check("stored bytes are the live bytes: " + n.encode("ascii", "replace").decode(),
                  blob_bytes(b, head, PREFIX + n) == want)
        check("an untouched memory file keeps main's bytes",
              (blob_bytes(b, head, PREFIX + "quiet.md") or b"").startswith(b"quiet.md base"))
        check("a clean local edit is replayed", (blob_bytes(b, head, "06_math/plain.md") or b"").endswith(b"local tail\n"))
        check("the replay moved no ref", git(b, "rev-parse", "HEAD")[1].strip() == before)
        check("one commit on top of main: the second resolves to the same live bytes and is dropped as empty",
              git(b, "rev-list", "--count", onto + ".." + head)[1].strip() == "1")
        with open(prog, encoding="utf-8") as fh:
            plines = fh.read().splitlines()
        check("progress file has one line per commit", len(plines) == 2 and " 1/2 " in plines[0] and " 2/2 " in plines[1],
              plines)
        if OLD:
            rc2, head2, text2 = replay(OLD, b, onto, live)
            check("older tool replays the same fixture", rc2 == 0 and len(head2) == 40, text2)
            t1 = git(b, "rev-parse", head + "^{tree}")[1].strip()
            t2 = git(b, "rev-parse", head2 + "^{tree}")[1].strip() if rc2 == 0 else ""
            check("same tree as the older per-file tool", t1 == t2 and len(t1) == 40, t1 + " " + t2)

        # a memory file with a non-ASCII name among the conflicts (the older tool declines here)
        b3, live3, onto3 = build(root, "u", autocrlf=False, NAMES=UNAMES)
        rc, head, text = replay(new, b3, onto3, live3)
        check("non-ASCII name: replay exit 0", rc == 0 and len(head) == 40, text)
        if rc == 0 and len(head) == 40:
            for n in UNAMES:
                with open(os.path.join(live3, n), "rb") as fh:
                    want = fh.read()
                check("non-ASCII fixture: stored bytes are the live bytes: " + n.encode("ascii", "replace").decode(),
                      blob_bytes(b3, head, PREFIX + n) == want)

        # autocrlf on: the batch is not exact, so the tool must store what `git add` stores (CRLF folded to LF)
        b2, live2, onto2 = build(root, "c", autocrlf=True)
        rc, head, text = replay(new, b2, onto2, live2)
        check("autocrlf fixture: replay exit 0", rc == 0 and len(head) == 40, text)
        if rc == 0 and len(head) == 40:
            got = blob_bytes(b2, head, PREFIX + "delta_crlf.md")
            want = git(b2, "hash-object", "--path", PREFIX + "delta_crlf.md", "--",
                       os.path.join(live2, "delta_crlf.md"))[1].strip()
            have = git(b2, "rev-parse", head + ":" + PREFIX + "delta_crlf.md")[1].strip()
            check("autocrlf fixture: the blob is the one git add would store", have == want, have + " " + want)
            check("autocrlf fixture: CRLF was folded", got is not None and b"\r\n" not in got)
            if OLD:
                rc2, head2, text2 = replay(OLD, b2, onto2, live2)
                t1 = git(b2, "rev-parse", head + "^{tree}")[1].strip()
                t2 = git(b2, "rev-parse", head2 + "^{tree}")[1].strip() if rc2 == 0 else ""
                check("autocrlf fixture: same tree as the older tool", t1 == t2 and len(t1) == 40, t1 + " " + t2)
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print(("PASS %d" % N[0]) if not FAILS else ("FAIL %d of %d" % (len(FAILS), N[0])))
    for f in FAILS:
        print("  " + f)
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())

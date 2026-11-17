"""test_safe_push_scanned_sha.py - safe_push.py publishes the commit it scanned (28 Sep).

    python test_safe_push_scanned_sha.py [OLD_SAFE_PUSH.py]

Everything happens in a temporary folder: a bare repository stands in for the remote, and a clone of it is where
safe_push runs. No real repository or remote is touched.
 P1 HEAD on a feature branch while the local main points at another commit that was never scanned: safe_push --branch
    main scans origin/main..HEAD and the remote's main afterwards is HEAD, and the other commit is not on the remote.
 P2 a push that is not a fast-forward of the scanned lower bound is refused and the remote does not move.
 P3 a fetch that fails (the remote is gone) is refused before any scan or push.
With OLD_SAFE_PUSH.py (the file before this change), P1 must fail: it pushes the local main, which was never scanned.
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
NEW = os.path.join(HERE, "safe_push.py")
OLD = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None   # safe_push runs inside the clone
NOWIN = 0x08000000 if os.name == "nt" else 0
ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never", GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
           GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
fails, ran = [], []
P1_SEEN = {}     # what P1 saw, so the negative control can assert the defect itself and not only "P1 did not pass"


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def rmtree(path):
    """git marks its objects read-only; Windows refuses to delete those without clearing the bit first"""
    import stat

    def clear(func, name, _exc):
        os.chmod(name, stat.S_IWRITE)
        func(name)
    shutil.rmtree(path, onexc=clear)


def git(cwd, *args):
    p = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True, env=ENV, creationflags=NOWIN)
    if p.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args), p.stderr.strip()))
    return p.stdout.strip()


def commit(repo, name, text):
    with open(os.path.join(repo, name), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    git(repo, "add", name)
    git(repo, "commit", "-q", "-m", "add " + name)
    return git(repo, "rev-parse", "HEAD")


def setup(td, tag):
    remote = os.path.join(td, tag + "_remote.git")
    clone = os.path.join(td, tag + "_clone")
    git(td, "init", "-q", "--bare", "-b", "main", remote)
    git(td, "clone", "-q", remote, clone)
    git(clone, "checkout", "-q", "-b", "main")
    commit(clone, "base.txt", "base\n")
    git(clone, "push", "-q", "origin", "main")
    return remote, clone


def safe_push(tool, clone, *args):
    p = subprocess.run([sys.executable, tool] + list(args), cwd=clone, capture_output=True, text=True, env=ENV,
                       creationflags=NOWIN)
    return p.returncode, p.stdout + p.stderr


def remote_main(remote):
    return git(remote, "rev-parse", "refs/heads/main")


def p1(tool, td, tag):
    remote, clone = setup(td, tag + "_p1")
    other = commit(clone, "local_main_only.txt", "never scanned\n")        # local main moves; never scanned
    git(clone, "checkout", "-q", "-b", "feature", "origin/main")
    head = commit(clone, "scanned.txt", "scanned\n")
    rc, out = safe_push(tool, clone, "--message", "unused", "--branch", "main")
    tip = remote_main(remote)
    ok = rc == 0 and tip == head and tip != other
    P1_SEEN[tag] = {"rc": rc, "published_unscanned": tip == other}
    return ok, "%s P1 HEAD on a feature branch, local main elsewhere: rc %d, remote main is %s (scanned HEAD %s, local main %s)" % (
        tag, rc, "the scanned HEAD" if tip == head else ("the unscanned local main" if tip == other else tip[:9]),
        head[:9], other[:9])


def p2(tool, td, tag):
    remote, clone = setup(td, tag + "_p2")
    helper = os.path.join(td, tag + "_p2_helper")
    git(td, "clone", "-q", remote, helper)
    moved = commit(helper, "someone_else.txt", "moved the remote\n")
    git(helper, "push", "-q", "origin", "HEAD:refs/heads/main")
    before = remote_main(remote)
    commit(clone, "mine.txt", "mine\n")                                    # built on the old tip: not a fast-forward
    rc, out = safe_push(tool, clone, "--message", "unused", "--branch", "main")
    ok = rc != 0 and remote_main(remote) == before == moved
    return ok, "%s P2 not a fast-forward: rc %d, remote unmoved %s" % (tag, rc, remote_main(remote) == before)


def p3(tool, td, tag):
    remote, clone = setup(td, tag + "_p3")
    commit(clone, "late.txt", "late\n")
    rmtree(remote)
    rc, out = safe_push(tool, clone, "--message", "unused", "--branch", "main")
    ok = rc != 0 and "fetch" in out.lower() and "scanning" not in out.lower()
    return ok, "%s P3 the remote is gone: rc %d, refused before scanning %s" % (tag, rc, "scanning" not in out.lower())


def main():
    td = tempfile.mkdtemp(prefix="safe-push-test-")
    try:
        for fn in (p1, p2, p3):
            ok, what = fn(NEW, td, "live")
            check(ok, what)
        if OLD:
            ok, what = p1(OLD, td, "before_28sep")
            seen = P1_SEEN["before_28sep"]
            # the defect itself: the old tool exits 0 and publishes the commit it never scanned (a crash is not the defect)
            check(seen["rc"] == 0 and seen["published_unscanned"],
                  "N1 the tool before this change publishes the unscanned commit (the check can fail): "
                  + what.split(": ", 1)[1])
    finally:
        shutil.rmtree(td, ignore_errors=True)
    print("FAIL" if fails else "PASS", "- %d checks, %d failed" % (len(ran), len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

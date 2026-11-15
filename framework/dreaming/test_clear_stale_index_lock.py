"""test_clear_stale_index_lock.py [--lib FILE] - controls for Clear-StaleIndexLock in dream_git_sync.ps1.

Every arm builds a throwaway repository, puts .git/index.lock in a known state and runs the function through
clear_lock_probe.ps1. Arms:
  NOLOCK       no lock                                             -> nothing to do
  FRESH        a lock a few seconds old                            -> left alone (too young)
  STALE        a 30-minute-old lock nobody holds                   -> set aside by rename, the bytes kept
  HELD         a 30-minute-old lock another process holds open     -> left alone
  GITLIVE      a real git (update-index --stdin) holding its lock  -> left alone: a live git does hold the file open
  ELDER        a lock nobody holds, a git older than it alive      -> left alone under the hour
  ELDERWAIVED  the same past the hour limit                        -> set aside
Prints PASS/FAIL per arm and a last line "PASS - N controls, 0 failed". Exit 0 only when every arm passes.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

NOWIN = 0x08000000 if os.name == "nt" else 0
HERE = os.path.dirname(os.path.abspath(__file__))
PS = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"


def git(repo, *args, **kw):
    return subprocess.run(["git", "-C", repo] + list(args), capture_output=True, creationflags=NOWIN, timeout=120, **kw)


def make_repo(root, name):
    repo = os.path.join(root, name)
    os.makedirs(repo)
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "t@example.invalid")
    git(repo, "config", "user.name", "t")
    with open(os.path.join(repo, "a.txt"), "w") as fh:
        fh.write("a\n")
    git(repo, "add", "a.txt")
    git(repo, "commit", "-q", "-m", "a")
    return repo


def probe(lib, repo, mn=10, mx=60, back=0):
    p = subprocess.run([PS, "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", os.path.join(HERE, "clear_lock_probe.ps1"),
                        "-Lib", lib, "-Repo", repo, "-Min", str(mn), "-Max", str(mx), "-SetBackMinutes", str(back)],
                       capture_output=True, creationflags=NOWIN, timeout=300)
    out = p.stdout.decode("utf-8", "replace").strip().splitlines()
    for line in reversed(out):
        if line.startswith("{"):
            return json.loads(line)
    return {"error": (p.stderr.decode("utf-8", "replace") or "no output")[:300]}


def lock_of(repo):
    return os.path.join(repo, ".git", "index.lock")


def asides(repo):
    return [n for n in os.listdir(os.path.join(repo, ".git")) if n.startswith("index.lock.stale_removed_")]


def live_git(repo):
    """A real git that takes the index lock and then waits on its stdin."""
    p = subprocess.Popen(["git", "-C", repo, "update-index", "--stdin"], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL, creationflags=NOWIN)
    return p


def end_git(p):
    try:
        p.stdin.close()
        p.wait(timeout=60)
    except Exception:
        p.kill()


def main():
    lib = os.path.join(HERE, "dream_git_sync.ps1")
    if "--lib" in sys.argv:
        lib = os.path.abspath(sys.argv[sys.argv.index("--lib") + 1])
    root = tempfile.mkdtemp(prefix="clearlock_")
    fails = 0
    n = 0

    def judge(name, r, ok, why=""):
        nonlocal fails, n
        n += 1
        if not ok:
            fails += 1
        print("%s  %s: %s %s" % ("PASS" if ok else "FAIL", name, json.dumps(r)[:330], why))

    try:
        # NOLOCK
        repo = make_repo(root, "nolock")
        r = probe(lib, repo)
        judge("NOLOCK", r, r.get("present") is False and r.get("cleared") is False and not asides(repo))

        # FRESH
        repo = make_repo(root, "fresh")
        open(lock_of(repo), "wb").close()
        r = probe(lib, repo)
        judge("FRESH", r, r.get("present") is True and r.get("cleared") is False and r.get("lock_left") is True
              and "under" in r.get("reason", ""))

        # STALE
        repo = make_repo(root, "stale")
        with open(lock_of(repo), "wb") as fh:
            fh.write(b"partial index bytes")
        r = probe(lib, repo, back=30)
        kept = asides(repo)
        body = open(os.path.join(repo, ".git", kept[0]), "rb").read() if kept else b""
        st = git(repo, "add", "a.txt")
        judge("STALE", r, r.get("cleared") is True and r.get("lock_left") is False and len(kept) == 1
              and body == b"partial index bytes" and st.returncode == 0, "git add after rc=%s" % st.returncode)

        # HELD
        repo = make_repo(root, "held")
        open(lock_of(repo), "wb").close()
        holder = open(lock_of(repo), "rb")
        try:
            r = probe(lib, repo, back=30)
        finally:
            holder.close()
        judge("HELD", r, r.get("cleared") is False and r.get("lock_left") is True and "holds the lock open" in r.get("reason", ""))

        # GITLIVE
        repo = make_repo(root, "gitlive")
        p = live_git(repo)
        try:
            for _ in range(100):
                if os.path.exists(lock_of(repo)):
                    break
                time.sleep(0.1)
            had = os.path.exists(lock_of(repo))
            r = probe(lib, repo, back=30)
        finally:
            end_git(p)
        judge("GITLIVE", r, had and r.get("cleared") is False and r.get("lock_left") is True
              and "holds the lock open" in r.get("reason", ""), "git took the lock: %s" % had)

        # ELDER / ELDERWAIVED: a git older than the lock, alive, in another repository
        other = make_repo(root, "other")
        p = live_git(other)
        try:
            time.sleep(7)
            repo = make_repo(root, "elder")
            open(lock_of(repo), "wb").close()
            r = probe(lib, repo, mn=0, mx=60)
            judge("ELDER", r, r.get("cleared") is False and r.get("lock_left") is True and "older than the lock" in r.get("reason", ""))
            r = probe(lib, repo, mn=0, mx=0)
            judge("ELDERWAIVED", r, r.get("cleared") is True and r.get("lock_left") is False and len(asides(repo)) == 1)
        finally:
            end_git(p)
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print("%s - %d controls, %d failed" % ("PASS" if fails == 0 else "FAIL", n, fails))
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

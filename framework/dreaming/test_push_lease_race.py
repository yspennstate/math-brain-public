"""test_push_lease_race.py - a push helper publishes nothing its scan did not cover, even when the remote is rewound
under it (28 Sep 2026).

    python test_push_lease_race.py [--dir DIR_WITH_THE_TOOLS] [--old DIR_WITH_THE_OLD_TOOLS]

The tools: safe_push.py, sliced_scan_push.py, gated_push.py, push_paths.sh (the dream folder's) and push_paths_py.py
(the brain-repo helper of an agent). Each runs on a copy whose scanner path points at a recorder beside it that
runs the real scanner and logs the range; in the RACE arm the recorder also rewinds the remote's main from A to its
parent R after the first clean scan, the moment B06 r63 used. Everything is in a temporary folder with a bare remote.
For every run: newly reachable = the commits the remote's main reaches afterwards that it did not reach before the tool
started; certified = the commits of every range the scanner was given. A success with a newly reachable commit outside
the certified set is a failure. Arms:
 RACE    remote main at A (fetched), B to publish, the remote rewound to R after the scan: nothing uncertified becomes
         reachable (the tool refuses, or re-certifies on the new tip and publishes that)
 STALE   the remote already rewound to R before the tool starts, this clone's tracking ref still at A: the same rule
 NORMAL  nothing moves: B (or the commit the tool builds) is published and certified
With --old, each tool before this change must fail RACE, and sliced_scan_push and gated_push STALE too (the check can
fail). safe_push and push_paths already fetched first, so their STALE arm is not a control.
"""
import os
import shutil
import stat
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.abspath(sys.argv[sys.argv.index("--dir") + 1]) if "--dir" in sys.argv else HERE
OLD = os.path.abspath(sys.argv[sys.argv.index("--old") + 1]) if "--old" in sys.argv else None
SCANNER = os.path.join(os.path.expanduser("~"), ".claude", "dreaming", "scan_secrets.py")
BASH = shutil.which("bash") or r"C:\Program Files\Git\bin\bash.exe"
NOWIN = 0x08000000 if os.name == "nt" else 0
ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never", GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
           GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
fails, ran = [], []

RECORDER = '''import os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "scanned.log"), "a", encoding="utf-8") as fh:
    fh.write(" ".join(sys.argv[1:]) + "\\n")
rc = subprocess.run([sys.executable, %r] + sys.argv[1:]).returncode
race = os.path.join(here, "race.txt")
if rc == 0 and os.path.exists(race):
    remote, r = open(race, encoding="utf-8").read().split()
    subprocess.run(["git", "--git-dir", remote, "update-ref", "refs/heads/main", r], check=True)
    os.remove(race)
sys.exit(rc)
''' % SCANNER

# (file name in DIR, the constant lines to point at the recorder and the fixture's clone)
SCANNER_LINES = {
    "safe_push.py": [('SCANNER = r"~\\.claude\\dreaming\\scan_secrets.py"', 'SCANNER = r"{rec}"')],
    "sliced_scan_push.py": [('REPO = r"~\\brain-repo"', 'REPO = r"{clone}"'),
                            ('SCANNER = r"~\\.claude\\dreaming\\scan_secrets.py"', 'SCANNER = r"{rec}"')],
    "gated_push.py": [('REPO = os.path.abspath(os.path.join(HERE, "..", ".."))', 'REPO = r"{clone}"'),
                      ('SCAN = os.path.join(HERE, "scan_secrets.py")', 'SCAN = r"{rec}"')],
    "push_paths.sh": [("python ~/.claude/dreaming/scan_secrets.py", 'python "{rec_posix}"')],
    "push_paths_py.py": [('REPO = r"~\\brain-repo"', 'REPO = r"{clone}"'),
                         ('SCAN = os.path.expanduser(r"~\\.claude\\dreaming\\scan_secrets.py")', 'SCAN = r"{rec}"')],
}


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def rmtree(path):
    def clear(func, name, _exc):
        os.chmod(name, stat.S_IWRITE)
        func(name)
    shutil.rmtree(path, onexc=clear)


def git(cwd, *args):
    p = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True, env=ENV, creationflags=NOWIN)
    if p.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args), p.stderr.strip()))
    return p.stdout.strip()


def commit(repo, name):
    with open(os.path.join(repo, name), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(name + "\n")
    git(repo, "add", name)
    git(repo, "commit", "-q", "-m", "add " + name)
    return git(repo, "rev-parse", "HEAD")


def prepare(td, tag, tooldir, tool):
    remote, clone, tdir = (os.path.join(td, tag + x) for x in ("_remote.git", "_clone", "_tool"))
    os.makedirs(tdir)
    rec = os.path.join(tdir, "scan_secrets.py")
    with open(rec, "w", encoding="utf-8") as fh:
        fh.write(RECORDER)
    src = io_read(os.path.join(tooldir, tool))
    for old, new in SCANNER_LINES[tool]:
        assert src.count(old) == 1, (tool, old)
        src = src.replace(old, new.format(rec=rec, clone=clone, rec_posix=rec.replace("\\", "/")))
    path = os.path.join(tdir, tool)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(src)
    git(td, "init", "-q", "--bare", "-b", "main", remote)
    git(td, "clone", "-q", remote, clone)
    hook = os.path.join(clone, ".git", "hooks", "pre-push")
    if os.path.exists(hook):
        os.remove(hook)                       # the tool alone is under test, not a template's hook
    git(clone, "checkout", "-q", "-b", "main")
    r = commit(clone, "r.txt")
    a = commit(clone, "a.txt")
    git(clone, "push", "-q", "origin", "main")
    return remote, clone, tdir, path, r, a


def io_read(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return fh.read()


def run_tool(tool, path, clone):
    if tool == "safe_push.py":
        with open(os.path.join(clone, "b.txt"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("b\n")
        cmd = [sys.executable, "-X", "utf8", path, "--message", "add b", "--paths", "b.txt"]
    elif tool in ("sliced_scan_push.py", "gated_push.py"):
        commit(clone, "b.txt")
        cmd = [sys.executable, "-X", "utf8", path]
    elif tool == "push_paths.sh":
        with open(os.path.join(clone, "b.txt"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("b\n")
        cmd = [BASH, path.replace("\\", "/"), clone.replace("\\", "/"), "add b", "b.txt"]
    else:
        with open(os.path.join(clone, "b.txt"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("b\n")
        cmd = [sys.executable, "-X", "utf8", path, "add b", "b.txt"]
    p = subprocess.run(cmd, cwd=clone, capture_output=True, text=True, env=ENV, creationflags=NOWIN, timeout=600)
    return p.returncode, (p.stdout + p.stderr).strip()


def arm(td, tooldir, tool, mode):
    tag = "%s_%s" % (tool.split(".")[0], mode)
    remote, clone, tdir, path, r, a = prepare(td, tag, tooldir, tool)
    if mode == "STALE":
        git(remote, "update-ref", "refs/heads/main", r)
    if mode == "RACE":
        with open(os.path.join(tdir, "race.txt"), "w", encoding="utf-8") as fh:
            fh.write("%s %s" % (remote, r))
    rc, out = run_tool(tool, path, clone)
    after = git(remote, "rev-parse", "refs/heads/main")
    # the remote's main just before the tool's own publish: R in RACE (a peer rewound it during the run) and in STALE,
    # A in NORMAL; what the tool made reachable is everything the new main reaches beyond it
    start = r if mode in ("RACE", "STALE") else a
    newly = set(git(remote, "rev-list", after, "--not", start).split()) if after != start else set()
    certified = set()
    log = os.path.join(tdir, "scanned.log")
    if os.path.exists(log):
        for line in io_read(log).splitlines():
            parts = line.split()
            if len(parts) == 2 and parts[0] == "--range":
                certified |= set(git(clone, "rev-list", parts[1]).split())
    missed = newly - certified
    return {"rc": rc, "moved": after != start, "newly": newly, "missed": missed,
            "a_reached": a in newly, "out": out[-240:]}


def run_all(tooldir, label):
    td = tempfile.mkdtemp(prefix="lease_race_")
    res = {}
    try:
        for tool in SCANNER_LINES:
            if not os.path.exists(os.path.join(tooldir, tool)):
                continue
            for mode in ("RACE", "STALE", "NORMAL"):
                x = arm(td, tooldir, tool, mode)
                if mode == "NORMAL":
                    ok = x["rc"] == 0 and x["moved"] and not x["missed"]
                else:
                    ok = not x["missed"]
                res[(tool, mode)] = (ok, "%s %s %s: rc %d, remote main moved %s, newly reachable %d, missed %d%s" % (
                    label, tool, mode, x["rc"], x["moved"], len(x["newly"]), len(x["missed"]),
                    " (A made reachable again unscanned)" if x["a_reached"] and x["missed"] else ""))
    finally:
        rmtree(td)
    return res


def main():
    new = run_all(DIR, "new")
    for key in sorted(new):
        check(*new[key])
    if OLD:
        old = run_all(OLD, "before 28 Sep 16:xx")
        for (tool, mode), (ok, what) in sorted(old.items()):
            want_fail = mode == "RACE" or (mode == "STALE" and tool in ("sliced_scan_push.py", "gated_push.py"))
            if want_fail:
                check(not ok, "N " + what.split(" ", 4)[-1] + " -> the tool before this change fails, the check can fail")
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

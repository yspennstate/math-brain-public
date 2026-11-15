"""test_push_with_resync_lease.py - the nightly dream's Push-WithResync publishes nothing its certification did not cover,
even when the remote is rewound between the last check and the push (28 Sep 2026, an agent; scheduled audit
account03/B06 r55, R51-B06-PUSH-WITH-RESYNC-UNLEASED-REWIND-38).

    python test_push_with_resync_lease.py [--lib DREAM_GIT_SYNC.ps1] [--old PRE_28_SEP.ps1] [--old-stale PRE_14_OCT.ps1]

Each arm builds R <- A <- B in a temporary clone with a bare remote whose main is A, records A..B as certified, then
calls Push-WithResync(B, base A) through a hidden PowerShell. Every range the function certifies is recorded too.
Newly reachable = what the remote's main reaches afterwards and did not before; it must lie inside the certified set.
 NORMAL   nothing moves: B is published
 REWIND   the remote is rewound to R before the push, one attempt: nothing is published (B06's reproduction)
 RESYNC   the same rewind, two attempts, the advertised main is R: the retry certifies R..B and publishes B
 FORWARD  the remote moved to C (a child of A), two attempts, advertised C: B is replayed onto C, certified, published
With --old, the function before this change must publish A uncertified in REWIND (the check can fail).

STALE arms (14 Oct 2026, an agent-r): the caller certified C..B against a main C that a peer pushed after B was
built on A, so B does not descend from its certified base. Before the change the function blocked the push and the
night's commit stayed local (eight October dreams).
 STALE     base C, advertised C, two attempts: B is replayed onto C, C..B' certified, B' published, C kept
 STALE1    the same with one attempt: nothing is published and the remote stays at C
 STALEFWD  base C, but main moved on to D (a child of C) before the re-sync: B is replayed onto D and published
In every arm of the new function nothing the remote had before is lost from its main.
With --old-stale (the function before 14 Oct, e.g. dream_git_sync.ps1.bak_stalebase_20261014), STALE must leave the
commit local (N2: the case this change exists for). --old takes the function before 28 Sep
(dream_git_sync.ps1.bak_r55lease_20260928) for N1.
"""
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile

if __name__ == "__main__" and ("-h" in sys.argv[1:] or "--help" in sys.argv[1:]):
    print(__doc__)
    sys.exit(0)

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.abspath(sys.argv[sys.argv.index("--lib") + 1]) if "--lib" in sys.argv else os.path.join(HERE, "dream_git_sync.ps1")
OLD = os.path.abspath(sys.argv[sys.argv.index("--old") + 1]) if "--old" in sys.argv else None
OLD_STALE = os.path.abspath(sys.argv[sys.argv.index("--old-stale") + 1]) if "--old-stale" in sys.argv else None
PS = shutil.which("powershell") or r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
NOWIN = 0x08000000 if os.name == "nt" else 0
ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never", GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
           GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
fails, ran = [], []

DRIVER = r'''param([string]$Lib, [string]$Repo, [string]$PushUrl, [string]$Sha, [string]$Base, [string]$AdvOid,
      [int]$Attempts, [string]$Log)
$ErrorActionPreference = 'Continue'
. $Lib
$adv = [pscustomobject]@{ Oid = $AdvOid; PushUrl = $PushUrl }
$getAdv = { $adv }.GetNewClosure()
$logPath = $Log
$certify = { param($range) Add-Content -LiteralPath $logPath -Value $range; $true }.GetNewClosure()
$r = Push-WithResync -Repo $Repo -PushUrl $PushUrl -CommitSha $Sha -BaseOid $Base -GetAdvertised $getAdv -Certify $certify `
    -Attempts $Attempts -SleepSeconds 0 -Logger { param($m) Write-Host "LOG $m" }
Write-Host ("RESULT " + ($r | ConvertTo-Json -Compress))
'''


# The stand-in for merge_branch_api.py: the same arguments and exit codes, the merge made on the local bare remote.
FAKE_TOOL = r'''import subprocess, sys
remote, branch, want, msgfile = sys.argv[1:5]
base = sys.argv[5] if len(sys.argv) > 5 else ""
def g(*a):
    r = subprocess.run(["git", "-C", remote] + list(a), capture_output=True, text=True, creationflags=0x08000000)
    return r.returncode, r.stdout.strip()
rc, got = g("rev-parse", "refs/heads/" + branch)
if rc != 0 or got != want:
    print("refused: branch is at %s" % got[:12]); sys.exit(4)
rc, main = g("rev-parse", "refs/heads/main")
if base:
    rc, _ = g("merge-base", "--is-ancestor", base, main)
    if rc != 0:
        print("refused: main does not contain the certified base"); sys.exit(4)
rc, tree = g("merge-tree", "--write-tree", main, want)
if rc != 0:
    print("conflict: status 409"); sys.exit(3)
rc, m = g("commit-tree", tree.splitlines()[0], "-p", main, "-p", want, "-m", "merge")
rc2, _ = g("update-ref", "refs/heads/main", m, main)
if rc != 0 or rc2 != 0:
    print("status 500"); sys.exit(4)
print("merged: status 201, merge commit %s, parents %s %s" % (m, main[:12], want[:12])); sys.exit(0)
'''


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
    r = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True, env=ENV, creationflags=NOWIN)
    if r.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args[:3]), r.stderr.strip()[-300:]))
    return r.stdout.strip()


def commit(repo, name, body=None):
    with open(os.path.join(repo, name + ".txt"), "w", encoding="utf-8") as fh:
        fh.write((body or name) + "\n")
    git(repo, "add", name + ".txt")
    git(repo, "commit", "-q", "-m", name)
    return git(repo, "rev-parse", "HEAD")


def setup(td):
    """R <- A on the remote's main, B on A in the clone. Returns (clone, remote, R, A, B)."""
    tmpl = os.path.join(td, "empty_template")
    os.makedirs(tmpl)
    remote = os.path.join(td, "remote.git")
    git(td, "init", "-q", "--bare", "--template=" + tmpl, "-b", "main", remote)
    clone = os.path.join(td, "clone")
    git(td, "init", "-q", "--template=" + tmpl, "-b", "main", clone)
    r = commit(clone, "R")
    a = commit(clone, "A")
    git(clone, "push", "-q", remote, "main:refs/heads/main")
    b = commit(clone, "B")
    return clone, remote, r, a, b


def commit_path(repo, path, body, msg):
    full = os.path.join(repo, *path.split("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(body + "\n")
    git(repo, "add", path)
    git(repo, "commit", "-q", "-m", msg)
    return git(repo, "rev-parse", "HEAD")


def reach(repo, tip):
    return set(git(repo, "rev-list", tip).split()) if tip else set()


def merge_is_honest(repo, m, p1, p2):
    """m's tree equals git's merge of p1 and p2, except conflicted paths, which must hold p1's blob."""
    r = subprocess.run(["git", "-C", repo, "merge-tree", "--write-tree", "--name-only", "--no-messages", p1, p2],
                       capture_output=True, text=True, creationflags=NOWIN)
    lines = [l.strip() for l in r.stdout.splitlines() if l.strip()]
    if r.returncode not in (0, 1) or not lines:
        return False
    conflicted = set(lines[1:]) if r.returncode == 1 else set()
    diff = subprocess.run(["git", "-C", repo, "diff", "--name-only", lines[0], m], capture_output=True, text=True,
                          creationflags=NOWIN).stdout.split()
    for path in diff:
        if path not in conflicted:
            return False
        mine = subprocess.run(["git", "-C", repo, "rev-parse", "%s:%s" % (m, path)], capture_output=True, text=True,
                              creationflags=NOWIN).stdout.strip()
        main = subprocess.run(["git", "-C", repo, "rev-parse", "%s:%s" % (p1, path)], capture_output=True, text=True,
                              creationflags=NOWIN).stdout.strip()
        if mine != main:
            return False
    return True


def certified(clone, ranges):
    out = set()
    for rg in ranges:
        rg = rg.strip()
        if rg:
            out |= set(git(clone, "rev-list", rg).split())
    return out


def run_arm(lib, mode):
    td = tempfile.mkdtemp(prefix="push_resync_%s_" % mode.lower())
    try:
        clone, remote, r, a, b = setup(td)
        log = os.path.join(td, "certified.log")
        adv, attempts, base, c, d = a, 1, a, None, None
        env = dict(ENV)
        if mode.startswith("BRANCH"):
            tool = os.path.join(td, "fake_merge_tool.py")
            with open(tool, "w", encoding="utf-8") as fh:
                fh.write(FAKE_TOOL)
            env["DREAM_MERGE_TOOL"] = tool
            if mode == "BRANCHOFF":
                env["DREAM_BRANCH_MERGE"] = "0"
            if mode == "BRANCHREWIND":
                git(remote, "update-ref", "refs/heads/main", r)
                adv = r
            else:                                    # a peer pushed C on A; one attempt, so no re-sync is tried
                other = os.path.join(td, "other")
                git(td, "clone", "-q", "--template=" + os.path.join(td, "empty_template"), remote, other)
                if mode == "BRANCHVIEWS":
                    # both sides rebuilt the same generated view: the conflict resolves to main's (the peer's) view
                    b = commit_path(clone, "01_ai_consciousness/brain/VIEW.md", "the dream's view", "B with a view")
                    c = commit_path(other, "01_ai_consciousness/brain/VIEW.md", "the peer's view", "C with a view")
                else:
                    c = commit(other, "B", "the peer's own B") if mode == "BRANCHCONFLICT" else commit(other, "C")
                git(other, "push", "-q", "origin", "main:refs/heads/main")
                adv = c
        if mode in ("REWIND", "RESYNC"):
            git(remote, "update-ref", "refs/heads/main", r)
            adv, attempts = r, (2 if mode == "RESYNC" else 1)
        if mode in ("FORWARD", "STALE", "STALE1", "STALEFWD"):
            other = os.path.join(td, "other")
            git(td, "clone", "-q", "--template=" + os.path.join(td, "empty_template"), remote, other)
            c = commit(other, "C")
            git(other, "push", "-q", "origin", "main:refs/heads/main")
            git(clone, "fetch", "-q", remote, "main:refs/remotes/o/main")
            adv, attempts = c, 2
            if mode.startswith("STALE"):
                base = c                             # the caller certified C..B: B was built on A before C landed
                attempts = 1 if mode == "STALE1" else 2
            if mode == "STALEFWD":
                d = commit(other, "D")               # main moves on again after the certification
                git(other, "push", "-q", "origin", "main:refs/heads/main")
                adv = d
        with open(log, "w", encoding="utf-8") as fh:
            fh.write("%s..%s\n" % (base, b))         # the caller's own certification of base..B
        before = git(remote, "rev-parse", "refs/heads/main")
        drv = os.path.join(td, "driver.ps1")
        with open(drv, "w", encoding="utf-8-sig") as fh:
            fh.write(DRIVER)
        # PowerShell dot-sources only a .ps1 path, and a backup copy of the library carries another suffix
        lib_ps1 = os.path.join(td, "lib_under_test.ps1")
        shutil.copyfile(lib, lib_ps1)
        p = subprocess.run([PS, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File", drv, "-Lib", lib_ps1,
                            "-Repo", clone, "-PushUrl", remote, "-Sha", b, "-Base", base, "-AdvOid", adv,
                            "-Attempts", str(attempts), "-Log", log], capture_output=True, text=True, env=env,
                           creationflags=NOWIN, timeout=600)
        out = p.stdout + p.stderr
        res = None
        for line in out.splitlines():
            if line.startswith("RESULT ") and line[7:].strip():
                res = json.loads(line[7:])
        if res is None:                     # the function did not return: counted as not pushed, with its output shown
            res = {"Pushed": False, "_error": out.strip()[-300:]}
        after = git(remote, "rev-parse", "refs/heads/main")
        newly = reach(remote, after) - reach(remote, before)
        lost = reach(remote, before) - reach(remote, after)
        cert = certified(clone, open(log, encoding="utf-8").read().splitlines())
        # a merge commit the server made: two parents, each already on main before or inside the certified set
        # 2026-11-10: the dream now makes that merge itself before the side branch (its first parent the fetched main),
        # and the server's merge has that local merge as a parent, so acceptance runs to a fixed point. A merge counts
        # only if its tree is git's own merge of its parents, a conflicted path carrying the FIRST parent's (main's) blob.
        held = reach(remote, before) | cert
        merges = set()
        grew = True
        while grew:
            grew = False
            for m in newly - cert - merges:
                par = git(remote, "rev-list", "--parents", "-n", "1", m).split()[1:]
                if len(par) == 2 and all(p in held for p in par) and merge_is_honest(remote, m, par[0], par[1]):
                    merges.add(m)
                    held.add(m)
                    grew = True
        side = [l.split("\t")[-1] for l in git(remote, "for-each-ref", "--format=%(objectname)\t%(refname)").splitlines()
                if "dream-sync-" in l]
        return {"pushed": bool(res.get("Pushed")), "after": after, "a": a, "b": b, "r": r, "c": c, "d": d,
                "merges": merges, "side": side, "via": bool(res.get("Merge")),
                "view": subprocess.run(["git", "-C", remote, "show", after + ":01_ai_consciousness/brain/VIEW.md"], capture_output=True, text=True,
                                       creationflags=NOWIN).stdout.strip(),
                "newly": newly, "lost": lost, "uncertified": newly - cert - merges,
                "log": [l for l in out.splitlines() if l.startswith("LOG ")][-3:]}
    finally:
        rmtree(td)


def main():
    for lib, label in ((LIB, "new"), (OLD, "old"), (OLD_STALE, "old-stale")):
        if not lib:
            continue
        for mode in ("NORMAL", "REWIND", "RESYNC", "FORWARD", "STALE", "STALE1", "STALEFWD",
                     "BRANCH", "BRANCHVIEWS", "BRANCHREWIND", "BRANCHCONFLICT", "BRANCHOFF"):
            if (label == "old" and mode != "REWIND") or (label == "old-stale" and mode != "STALE"):
                continue
            x = run_arm(lib, mode)
            short = {k: (v[:7] if isinstance(v, str) else v) for k, v in x.items() if k in ("pushed", "after")}
            if label == "new":
                if mode == "NORMAL":
                    ok = x["pushed"] and x["after"] == x["b"] and not x["uncertified"]
                elif mode == "BRANCH":
                    # main moved to C and the one push attempt was refused: the server merges the side branch, main
                    # holds both B and C under one merge commit, and the side branch is gone
                    # (two merges since 10 Nov: the dream's local merge onto the fetched main, then the server's)
                    ok = (x["pushed"] and x["via"] and 1 <= len(x["merges"]) <= 2 and x["after"] in x["merges"]
                          and x["b"] in x["newly"] and not x["uncertified"] and not x["side"])
                elif mode == "BRANCHVIEWS":
                    ok = (x["pushed"] and x["via"] and x["after"] in x["merges"] and x["b"] in x["newly"]
                          and not x["uncertified"] and not x["side"] and x["view"] == "the peer's view")
                elif mode == "BRANCHREWIND":
                    # main rewound below the certified base: no side branch is pushed and nothing is merged
                    ok = not x["pushed"] and x["after"] == x["r"] and not x["newly"] and not x["side"]
                elif mode in ("BRANCHCONFLICT", "BRANCHOFF"):
                    ok = not x["pushed"] and x["after"] == x["c"] and not x["newly"] and not x["side"]
                elif mode == "REWIND":
                    ok = not x["pushed"] and x["after"] == x["r"] and not x["newly"]
                elif mode == "STALE1":
                    ok = not x["pushed"] and x["after"] == x["c"] and not x["newly"]
                elif mode in ("STALE", "STALEFWD"):
                    # B' is a new commit on the advertised main, so neither B nor the old main is the tip
                    ok = (x["pushed"] and not x["uncertified"] and x["newly"] and x["after"] not in (x["b"], x["c"], x["d"]))
                else:
                    ok = x["pushed"] and not x["uncertified"] and x["after"] != x["r"]
                ok = bool(ok) and not x["lost"]
                check(ok, "%s %s: %s, newly reachable %d, uncertified %d, lost %d %s" % (
                    label, mode, short, len(x["newly"]), len(x["uncertified"]), len(x["lost"]), x["log"] if not ok else ""))
            elif mode == "REWIND":
                check(x["pushed"] and len(x["uncertified"]) >= 1,
                      "N1 old REWIND: the function before 28 Sep publishes %d commit(s) no certification covered "
                      "(pushed %s): the defect B06 found" % (len(x["uncertified"]), x["pushed"]))
            else:
                check(not x["pushed"] and not x["newly"],
                      "N2 old STALE: the function before 14 Oct leaves the commit local (pushed %s, newly reachable "
                      "%d): the block eight October dreams hit" % (x["pushed"], len(x["newly"])))
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

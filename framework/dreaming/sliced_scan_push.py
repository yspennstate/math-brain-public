#!/usr/bin/env python3
"""Certify the unpushed range of the memories repo in bounded slices, then push.
Same guarantee as safe_push.py (nothing pushes unless every byte of the range
scanned clean), sliced commit-by-commit so the scanner's per-run size bound is
respected instead of exceeded. Endpoints pinned once up front; the push targets
the exact scanned tip. Fails closed on any slice not printing the clean line.
The lower bound comes from a fetch made here, the tip must be a fast-forward of it, and the push holds the remote to
it (--force-with-lease): before 28 Sep the base was whatever the tracking ref last saw, and after a rewind of the
remote a push from it made commits reachable that no slice had scanned (account02/B06 r63/r64)."""
import os
import subprocess
import sys

REPO = r"~\brain-repo"
SCANNER = r"~\.claude\dreaming\scan_secrets.py"
os.environ["GIT_TERMINAL_PROMPT"] = "0"
os.environ["GCM_INTERACTIVE"] = "never"
os.chdir(REPO)

def git(*args):
    p = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    if p.returncode:
        print("git", args, "failed:", (p.stderr or p.stdout).strip()[:300])
        sys.exit(3)
    return p.stdout.strip()

git("fetch", "-q", "origin", "main")
base = git("rev-parse", "origin/main")
tip = git("rev-parse", "main")
if subprocess.run(["git", "merge-base", "--is-ancestor", base, tip]).returncode != 0:
    print("origin/main is not an ancestor of main - rebase first; nothing pushed")
    sys.exit(3)
commits = git("rev-list", "--reverse", "%s..%s" % (base, tip)).split()
print("pinned base %s tip %s | %d commits" % (base[:10], tip[:10], len(commits)))

prev = base
for i, c in enumerate(commits, 1):
    p = subprocess.run([sys.executable, SCANNER, "--range", "%s..%s" % (prev, c)],
                       capture_output=True, text=True)
    out = (p.stdout + p.stderr).strip()
    clean = "secret scan clean" in out
    print("slice %2d/%d %s..%s : %s" % (i, len(commits), prev[:8], c[:8],
                                        "clean" if clean else "NOT CLEAN"))
    if not clean:
        print(out[-600:])
        print("REFUSING TO PUSH - slice did not certify.")
        sys.exit(2)
    prev = c

if prev != tip:
    print("slice walk did not end at the pinned tip - refusing.")
    sys.exit(2)

p = subprocess.run(["git", "push", "--force-with-lease=refs/heads/main:%s" % base, "origin",
                    "%s:refs/heads/main" % tip], capture_output=True, text=True)
print((p.stdout + p.stderr).strip()[-400:])
if p.returncode:
    print("PUSH FAILED")
    sys.exit(3)
new_remote = git("ls-remote", "origin", "main").split()[0]
print("remote main now:", new_remote[:12], "| matches scanned tip:", new_remote == tip)

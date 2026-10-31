"""safe_push.py - commit, scan, push, with the scan pinned to fixed object IDs.

WHY THIS EXISTS (2026-08-20). The standing rule is that every push gets a secret scan first. The
usual one-liner does this:

    git commit ... && python scan_secrets.py --range "$(git rev-parse origin/main)..$(git rev-parse HEAD)" && git push

and on a machine where several agents share the repo that is a race. `origin/main` can move between
the two `rev-parse` calls, and scan_secrets then aborts with "Git repository identity changed during
the scan". Because the `&&` chain treats the scan's failure as just another non-zero exit - or worse,
because the scan is on its own line and the push runs regardless - THE PUSH CAN GO OUT UNSCANNED.
That happened once here; the retroactive scan came back clean, but the guarantee had already been
lost, and a clean result after the fact is luck rather than process.

The fix is to resolve both endpoints ONCE, up front, and to make a scan that did not return "clean"
a hard stop rather than a warning.

Usage:
    python safe_push.py --message "commit message" [--paths PATH ...] [--remote origin] [--branch main]
    python safe_push.py --scan-only          # scan unpushed work without committing or pushing

Exit codes: 0 pushed (or nothing to do), 2 scan not clean or scan errored, 3 git failure.
Nothing is pushed unless the scan printed exactly "secret scan clean", and what is pushed is the scanned commit itself
(pushed as SHA:refs/heads/BRANCH, then read back with ls-remote; 28 Sep, fleet02/B06 R24). The push holds the remote
to the scanned lower bound (--force-with-lease=refs/heads/BRANCH:BASE on a fast-forward): if the remote's branch is not
exactly BASE when git updates it - moved on, or rewound after the fetch - git refuses, because a rewind would make
reachable again commits this scan never covered (28 Sep, fleet02/B06 r63/r64).
"""
import argparse
import os
import subprocess
import sys

SCANNER = os.path.expanduser(r"~\.claude\dreaming\scan_secrets.py")

# Unattended/agent use: never let fetch or push block on an interactive credential
# prompt (the same GIT_TERMINAL_PROMPT-alone-is-insufficient hang found and fixed
# in run_dream.ps1, 2026-08-24 - GCM_INTERACTIVE=never is the piece that matters).
os.environ["GIT_TERMINAL_PROMPT"] = "0"
os.environ["GCM_INTERACTIVE"] = "never"


def git(*args, check=True):
    p = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    if check and p.returncode != 0:
        sys.stderr.write("git %s failed:\n%s\n%s\n" % (" ".join(args), p.stdout, p.stderr))
        sys.exit(3)
    return p.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--message")
    ap.add_argument("--paths", nargs="*", default=None)
    ap.add_argument("--remote", default="origin")
    ap.add_argument("--branch", default="main")
    ap.add_argument("--scan-only", action="store_true")
    a = ap.parse_args()

    if not a.scan_only and not a.message:
        sys.stderr.write("--message is required unless --scan-only\n")
        sys.exit(3)

    # A HELD SHARED INDEX (27 Oct 2026): the dream's own `git reset` kept .git/index.lock from 07:03 to
    # past 10:30 on a stalled disk and every `git add` here died on it. push_paths.sh already pushes named files through
    # a private index on the freshly fetched tip (scan, lease, peer-moved refusal), so hand the files to it.
    lock = os.path.join(git("rev-parse", "--absolute-git-dir"), "index.lock")
    if not a.scan_only and a.paths and os.path.exists(lock):
        top = git("rev-parse", "--show-toplevel")
        rels = [os.path.relpath(os.path.abspath(p), top).replace("\\", "/") for p in a.paths]
        print("index.lock is held by another git process; pushing the named files with push_paths.sh")
        return subprocess.call(["bash", os.path.join(os.path.dirname(os.path.abspath(__file__)), "push_paths.sh"),
                                top, a.message] + rels)

    if not a.scan_only:
        if a.paths:
            git("add", "--", *a.paths)
        else:
            git("add", "-u")
        staged = subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode
        if staged == 0:
            print("nothing staged; not committing")
        else:
            git("commit", "-q", "-m", a.message)

    # resolve BOTH endpoints once, before anything else can move them. The fetch must succeed: without it the lower
    # bound is whatever the tracking ref last saw (28 Sep, fleet02/B06 R24).
    f = subprocess.run(["git", "fetch", a.remote, a.branch], capture_output=True, text=True)
    if f.returncode != 0:
        sys.stderr.write("fetch of %s/%s failed - refusing to push against a stale lower bound:\n%s\n"
                         % (a.remote, a.branch, (f.stdout + f.stderr).strip()))
        return 3
    base = git("rev-parse", "%s/%s" % (a.remote, a.branch))
    head = git("rev-parse", "HEAD")
    if base == head:
        print("nothing to push (%s/%s == HEAD)" % (a.remote, a.branch))
        return 0

    print("scanning %s..%s" % (base[:9], head[:9]))
    p = subprocess.run([sys.executable, SCANNER, "--range", "%s..%s" % (base, head)],
                       capture_output=True, text=True)
    out = (p.stdout or "") + (p.stderr or "")
    sys.stdout.write(out if out.endswith("\n") else out + "\n")
    if p.returncode != 0 or "secret scan clean" not in out:
        sys.stderr.write("SCAN DID NOT COME BACK CLEAN - refusing to push.\n"
                         "If this is the concurrent-repo race, re-run; the endpoints are pinned so a\n"
                         "retry resolves them afresh. Do NOT push around this.\n")
        return 2

    if a.scan_only:
        # 2026-09-03: this flag used to skip only the commit and then push anyway - a check that
        # publishes is not a check. Scan-only means scan only.
        print("scan-only: %s..%s is clean; not pushing" % (base[:9], head[:9]))
        return 0

    # PUBLISH EXACTLY WHAT WAS SCANNED (28 Sep, fleet02/B06 R24, R24-B06-SAFE-PUSH-SCANS-HEAD-BUT-PUSHES-BRANCH).
    # `git push REMOTE BRANCH` sent the local branch ref, and on a detached HEAD, another branch or a worktree that is
    # not the commit scanned above. The push now names the scanned commit, and only a fast-forward of the scanned
    # lower bound is allowed.
    if subprocess.run(["git", "merge-base", "--is-ancestor", base, head]).returncode != 0:
        sys.stderr.write("%s/%s is not an ancestor of HEAD - rebase first; nothing pushed\n" % (a.remote, a.branch))
        return 3
    r = subprocess.run(["git", "push", "--force-with-lease=refs/heads/%s:%s" % (a.branch, base), a.remote,
                        "%s:refs/heads/%s" % (head, a.branch)], capture_output=True, text=True)
    sys.stdout.write(r.stdout + r.stderr)
    if r.returncode != 0:
        sys.stderr.write("push failed (rejected? re-pull and retry; never force shared history)\n")
        return 3
    remote_tip = git("ls-remote", a.remote, "refs/heads/%s" % a.branch, check=False).split("\t")[0]
    if remote_tip != head:
        sys.stderr.write("the remote's %s is %s after the push, not the scanned %s - look before trusting it\n"
                         % (a.branch, remote_tip[:9] or "unreadable", head[:9]))
        return 3
    print("pushed %s..%s (remote verified)" % (base[:9], head[:9]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

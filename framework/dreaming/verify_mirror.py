#!/usr/bin/env python3
"""verify_mirror.py - keep the repo's machinery mirror honest (the restore path rots quietly).

The brain's MACHINERY lives at ~/.claude (dreaming/*, wake_brain.ps1, brain_startup.md); the repo
carries a mirror under 12_cognitive_architecture/ that exists so RESTORE.md can rebuild a dead
laptop. Tonight's finding (2026-07-09): the mirror is synced BY HAND, so it drifts - sessions
copy what they remember to copy, forget the rest, and sometimes edit the repo side directly.
The memory corpus already syncs mechanically every dream; this does the same for the machinery.

  python verify_mirror.py                  # report drift, change nothing (exit 0 always)
  python verify_mirror.py --sync-to-repo   # copy live -> repo for drifted/missing machinery

Scope: code + prompts only (*.py, *.ps1, *.vbs, dream_prompt*.md + the two wake singletons).
Runtime state (tsv/npz/jsonl/logs/agenda/views) is deliberately out of scope - the corpus
robocopy and the scripts that own those files handle them. Sync direction is live -> repo,
never the reverse; a repo-side file NEWER than live is loudly flagged instead of overwritten
blindly (someone worked on the mirror - reconcile by hand, that's a human call).
"""
import hashlib
import io
import os
import shutil
import sys
import time

HOME = os.path.expanduser("~")
LIVE_DR = os.path.join(HOME, ".claude", "dreaming")
REPO = os.path.join(HOME, "brain-repo", "12_cognitive_architecture")
REPO_DR = os.path.join(REPO, "dreaming")

SINGLETONS = [
    (os.path.join(HOME, ".claude", "wake_brain.ps1"), os.path.join(REPO, "wake_brain.ps1")),
    (os.path.join(HOME, ".claude", "brain_startup.md"), os.path.join(REPO, "brain_startup.md")),
]


def _machinery(d):
    out = []
    try:
        for fn in sorted(os.listdir(d)):
            p = os.path.join(d, fn)
            if not os.path.isfile(p):
                continue
            if fn.endswith((".py", ".ps1", ".vbs")) or fn.startswith("dream_prompt"):
                out.append(fn)
    except Exception:
        pass
    return out


def _uncovered_subdirs():
    """Report machinery in SUBDIRECTORIES, which this mirror does not carry.

    _machinery() uses os.listdir, a flat read, so every subdirectory of dreaming/ is
    outside the mirror by construction - not by anyone's decision. That was recorded on
    2026-07-15 for error_graph/ and graph_fire/ and left open; by 2026-08-10 it had grown
    to include job_cycle/ (the session-handover system) and network/, with 132
    subdirectory .py against 215 mirrored at top level and three directories carrying no
    backup at all.

    This only COUNTS them. Syncing would mean deciding which build outputs belong in the
    repository - strong_nodes/runtime is content-addressed generations - and that is the
    owner's call, not a mirror maintainer's. But an unreported gap grows silently, which
    is exactly what happened for three weeks, so the number is printed every run.
    """
    skip = ("__pycache__", ".pytest_cache", "state", "logs", "strong_nodes")
    found = {}
    for dirpath, dirnames, filenames in os.walk(LIVE_DR):
        if dirpath == LIVE_DR:
            dirnames[:] = [d for d in dirnames if d not in skip]
            continue
        rel = os.path.relpath(dirpath, LIVE_DR).replace(os.sep, "/")
        if any(part in skip for part in rel.split("/")):
            continue
        n = sum(1 for f in filenames if f.endswith((".py", ".ps1", ".vbs")))
        if n:
            mirrored = os.path.isdir(os.path.join(REPO_DR, rel.replace("/", os.sep)))
            found[rel] = (n, mirrored)
    return found


def _sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        # Discovery is not execution: this script writes, so a help request must
        # exit before any work. See script_help_flag_can_execute_work.
        print(__doc__ or os.path.basename(__file__))
        return
    sync = "--sync-to-repo" in sys.argv[1:]
    pairs = [(os.path.join(LIVE_DR, fn), os.path.join(REPO_DR, fn)) for fn in _machinery(LIVE_DR)]
    pairs += SINGLETONS
    same = synced = 0
    drift, repo_newer, missing_repo = [], [], []
    for live, repo in pairs:
        fn = os.path.basename(repo)
        if not os.path.exists(live):
            continue
        if not os.path.exists(repo):
            missing_repo.append(fn)
            if sync:
                try:
                    shutil.copyfile(live, repo)
                    synced += 1
                except Exception as e:
                    print("verify_mirror: copy FAILED for %s: %s" % (fn, e))
            continue
        if _sha(live) == _sha(repo):
            same += 1
            continue
        if os.path.getmtime(repo) > os.path.getmtime(live) + 2:
            repo_newer.append(fn)   # repo side edited directly - do NOT clobber, a human reconciles
            continue
        drift.append(fn)
        if sync:
            try:
                shutil.copyfile(live, repo)
                synced += 1
            except Exception as e:
                print("verify_mirror: copy FAILED for %s: %s" % (fn, e))

    bits = ["verify_mirror: %d in sync" % same]
    if drift:
        bits.append(("SYNCED live->repo: " if sync else "DRIFT (live newer): ") + ", ".join(drift))
    if missing_repo:
        bits.append(("added to repo: " if sync else "missing in repo: ") + ", ".join(missing_repo))
    if repo_newer:
        bits.append("REPO-SIDE NEWER (left alone - reconcile by hand): " + ", ".join(repo_newer))
    print("; ".join(bits))
    # an orphan on the repo side (machinery retired live) is information, not an action
    orphans = [fn for fn in _machinery(REPO_DR) if not os.path.exists(os.path.join(LIVE_DR, fn))]
    if orphans:
        print("verify_mirror: repo-only (retired live? delete by hand if truly dead): " + ", ".join(orphans))

    # Coverage, not an action: this mirror is flat, so subdirectory machinery is outside
    # the restore path it exists to protect. Printed every run because the gap grew
    # unnoticed from two directories to five between 2026-07-15 and 2026-08-10.
    subs = _uncovered_subdirs()
    if subs:
        total = sum(n for n, _ in subs.values())
        worst = sorted(subs.items(), key=lambda kv: -kv[1][0])[:4]
        print("verify_mirror: NOT COVERED (this mirror is flat) - %d machinery file(s) in "
              "%d subdirectory(ies): %s"
              % (total, len(subs),
                 ", ".join("%s(%d%s)" % (rel, n, "" if mirrored else ", no repo dir")
                           for rel, (n, mirrored) in worst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

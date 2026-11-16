---
name: dream_sync_deleted_3055_local_copies_fallback_then_absent_mark_2026_11_15
description: "Files vanished from the shared brain clone during a dream? 15 Nov 02:55: the sync's in-place index step failed silently, the fallback deleted 3,055 identical copies, the absent step then marked them not held so reset wrote none back. Fixed e165c29942f3: copies are moved aside and put back; control test_dream_sync_dropback.py"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T03:59:52+02:00
  status: verified
  evidence: "dream_20261114_184112.log lines 1945-1946; test_dream_sync_dropback.py fixed 15/15, old 10/10; commit e165c29942f3"
  lesson: true
---

On 15 Nov 2026 at 02:55-03:01 (workstation clock) the dream's git sync (`Sync-LocalMainToAdvertised` in
`~/.claude/dreaming/dream_git_sync.ps1`) moved the shared brain clone from bc60e44 to ba56de8 over 7,789 incoming
commits and deleted 3,055 local files. Five sessions lost working files; two files written during those six minutes
lost bytes that were on no other machine (ab4_run.py, gpu_legs_r.py). It was not the GitHub offload tool: its ledger
shows only picture sessions in that minute.

**How it happened.** Three steps, each sound alone:
1. The move hashes every local copy of an incoming file. A copy equal to the incoming version is "identical".
2. `dream_sync_index.py stage` should set those index entries in place so the files never move. That night it failed
   (exit code not zero, stderr thrown away), the log said "0 files indexed in place", and the script fell back to its
   old road: delete the identical copies and let `git reset --keep` write them again.
3. Since 10 Nov the `absent` step marks every incoming path with no file on disk as not held (skip-worktree), so the
   move downloads nothing this computer never had. It ran after the delete, saw 3,055 paths with no file, and marked
   them. `git reset --keep` then wrote none of them back.
Tracked files edited here to the incoming bytes were parked, reverted and overwritten on the strength of a hash taken
six minutes earlier, so a rewrite in between was lost.

**The fix (commit e165c29942f3, backup dream_git_sync.ps1.bak_dropback_1115):** a copy the move must take out of the
way is moved to `<park dir>_drop` and put back afterwards on both the success and the refused road, local bytes
winning; a parked file whose bytes no longer give the hash taken at the start is kept at its newest bytes and logged;
`stage` is tried twice, four seconds apart, and its failure is logged with the last error line; the not-held mark is
cleared on every file that is on disk after the move. Control `test_dream_sync_dropback.py <script dir> <work dir>
fixed|old`: 15 of 15 on the fix, and 10 of 10 faults reproduced on the old script. The older controls
test_dream_sync_present.py and test_absent_move.py still pass.

**What would change this:** the next dream log. Read its `sync:` lines: "in-place index step failed (...)" names why
`stage` fails (the guess is another git process holding the index; "unable to write new index file" appeared at 03:16
the same night); a line "their bytes stay in ..._drop" means a put-back failed and the files are in that folder.

**The general lesson:** a fallback that deletes, followed by a later step that reads "no file" as "never had it", is a
delete with no undo. When two repairs are added weeks apart to the same road, test them together with the first one
failing.


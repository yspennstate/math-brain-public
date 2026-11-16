---
name: dream_sync_dropped_commits_made_during_its_replay_2026_11_13
description: "Commits vanished from local main of the brain clone at 06:21 (reset to a rebuilt tip)? The dream sync read HEAD once and reset past commits made during its replay; fixed 13 Nov 07:21 with a catch-up replay and a second look before the move; a lost uncommitted edit was not reproduced"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T07:25:04+02:00
  status: verified
  evidence: "old code replay_window 6 of 12 (bug reproduced); fix 12/12, 12/12, 8/8, 7/7, 12/12 plus older tests; landed 13 Nov 07:21; mirror commit 0ef345e48cfc"
---

**What happened.** At 06:21 on 13 Nov 2026 local main of the brain clone was reset to 7fb616b8b5f, a rebuilt copy of the 05:57 tip. Three commits made in the checkout while the dream's sync was running fell off main: 99fdc8fffa9, 22e2c8aab43, f4788ac6a2f. Their owners put the content back by hand (an agent in e419ad5027c, an agent in 1e975d27352). an agent also reported an edit to a tracked file, written at 06:20, as lost.

**Cause.** `Sync-LocalMainToAdvertised` in `~/.claude/dreaming/dream_git_sync.ps1` read HEAD once, replayed the local commits onto the advertised main with `dream_tree_replay.py` (many minutes on this workstation), prepared the index, and then ran `git reset --keep` to the replayed head. A commit made after that first read was not in the replay, so the reset moved main past it. `--keep` refuses on a dirty incoming file but says nothing about commits.

**Fix, landed 13 Nov 07:21.**
- `dream_tree_replay.py` takes `DREAM_REPLAY_SINCE` (a full commit id) and `DREAM_REPLAY_HEAD`, and replays only that range; without them it behaves as before.
- `dream_git_sync.ps1` has a new function `Add-LateLocalCommits`. After the replay a catch-up loop (at most five rounds) replays whatever was committed meanwhile; if that fails the checkout is not touched and the next cycle retries. Just before the move there is a second look: a late commit on a file that is not incoming is carried over, a late commit on an incoming file means the move is not tried.
- Backups beside the live files: `dream_git_sync.ps1.bak_catchup_20261113`, `dream_tree_replay.py.bak_catchup_20261113`. A dream that was already running keeps the old functions until its next start (run_dream.ps1 dot-sources the file once).

**Test.** `~/.claude/dreaming/test_dream_sync_late_commits.py <script dir> <work dir> <case>` builds a scratch origin and checkout and injects a commit or an edit in the middle of the sync. On the old code: replay_window 6 of 12 (the late commit and its file are gone after the move, the bug reproduced). On the fix: replay_window 12 of 12, prep_disjoint 12 of 12, prep_clash 8 of 8, prep_edit 7 of 7, scene_0621 12 of 12; the older tests still pass (test_dream_sync_present moved 14 of 14, test_replay_batch 21, test_replay_held 18, test_replay_rules 18).

**The second half: the lost uncommitted edit.** Not reproduced. With HEAD right, `git reset --keep` refuses the move when an incoming tracked file carries an uncommitted edit, and the edit stays (case prep_edit). On the old code, a late commit plus an uncommitted edit to the same file also made the move refuse (old scene_0621, 8 of 12: move refused, edit kept). So the edit of 06:20 most likely sat in a file of one of the three dropped commits: the file was clean when the move ran, and the move put the older version back. To chase it further one needs the path of the file.

**How to apply.** If commits vanish from local main of the brain clone again, read `git reflog` for a `reset: moving to` line and the dream log for "were made here while the sync was replaying" or "so the move was not tried". The first line means the fix carried the commits; the second means the move was held for the next cycle. Lost commits stay reachable from the reflog; put them back by path, never by reset. One wrong check in my own first test (it wanted a new incoming file on disk, which the sync indexes without writing, by design) cost a re-run: read the design before asserting what a fixture must leave on disk.


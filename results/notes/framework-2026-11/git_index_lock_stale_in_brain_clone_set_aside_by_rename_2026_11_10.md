---
name: git_index_lock_stale_in_brain_clone_set_aside_by_rename_2026_11_10
description: "Every git write in the brain clone fails with 'index.lock exists' and no git is running? 10 Nov: a 0-byte lock 53 min old. Stale = older than 30 min AND no git process alive; set it aside by rename to index.lock.stale_removed_<stamp>, never delete, never touch a fresh one. push_paths.sh pushes never meet it."
metadata:
  node_type: memory
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T07:43:26+02:00
  status: provisional
  evidence: ""
  modified: 2026-11-11T05:18:55.133Z
---

Every git write in the brain clone fails with "index.lock exists" and no git is running - what to do?
On 10 Nov 2026 07:09 the shared clone (~\the private repository) held a 0-byte .git/index.lock
written at 06:16:48, 53 minutes old, with no git process alive. Some git call had been killed or timed out while it
held the index. Until it went, every `git add`, `commit`, `reset` or checkout in that clone would refuse, and the
dream's persist step would have met it at 10:30.

What I did, and the rule: set it aside by rename, never delete it and never touch a fresh one.
- Stale means BOTH: older than 30 minutes AND no git process started in the last 6 hours
  (Get-Process git, StartTime). Either test alone is not enough: a long repack holds a lock for an hour.
- Rename to index.lock.stale_removed_<yyyyMMdd_HHmmss> beside it (the dream's own convention in run_dream.ps1,
  lines ~971-995), so the evidence stays and the step is reversible.
- If the lock is fresh or a git is alive: stop and wait. Do not retry in a loop.

Pushes that go through push_paths.sh never meet this lock: it builds its commit in its own index file. That is also
why a stale lock can sit unnoticed for an hour while pushes keep landing.

Where it is built in: scratch sync_by_hand_scratch.ps1 (the by-hand run of Sync-LocalMainToAdvertised) does this check
before it starts.

Related: [[dream_catchup_merged_in_scanned_parts_2026_11_10]], [[dream_replay_index_rewrite_per_file_2026_11_10]].
Status: verified (one lock, set aside, the move that followed wrote the index).

Second case, 11 Nov 2026 (an agent): a 108 MB index.lock (a whole new index, written in full) from 03:48:17, still
there at 07:15, 207 minutes. Its writer was gone, but the "no git started in 6 hours" test could not pass: a repack of the
same clone had been running since 21:48 the night before (pack.threads=2, its multi-pack-index write since 03:52), and
repack never takes index.lock. So the age-plus-no-git test alone would have waited out a nine-hour repack while every
plain add/commit failed (claim_and_push.sh gave up after five minutes; an agent reported it the same hour).
The decisive test is the one in [[rename_is_the_safe_test_for_a_stale_lock_2026_08_20]]: rename succeeded, so no handle
was open; the lock went to index.lock.stale_removed_20261111_071515 under a mesh exclusive claim.
How to apply: old (> 30 min) AND the rename test passes is enough, whatever unrelated git (repack, gc, fetch, a
private-index push) is alive. A git that could own it is one whose cwd/-C is this clone AND that writes the index
(add, commit, reset, checkout, status refresh, merge, rebase).


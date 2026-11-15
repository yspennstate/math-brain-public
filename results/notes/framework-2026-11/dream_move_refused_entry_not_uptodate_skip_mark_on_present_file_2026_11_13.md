---
name: dream_move_refused_entry_not_uptodate_skip_mark_on_present_file_2026_11_13
description: "Dream move refused, 'Entry ... not uptodate. Cannot merge', commits LOCAL ONLY since 10 Nov? A skip-worktree entry whose file is on disk; sync now clears the mark (25f1f54c)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T00:57:31+02:00
  status: provisional
  evidence: "controls 11/11 refused (old) and 14/14 moved (new) on a scratch repo; live clone not yet seen (first run: next dream after 00:55 on 13 Nov)"
---

Question this answers: the dream log says "moving the checkout was refused ... tonight's commit stays LOCAL ONLY"
and git said "error: Entry '<path>' not uptodate. Cannot merge." What is refusing, and what fixes it?

What happened (10 to 13 Nov 2026). Local main of the brain clone forked from GitHub's main on 10 Nov 11:45 and never
caught up: 74 local commits by 00:40 on 13 Nov, with 2,157 paths in them that GitHub's main did not hold (2,093 of
them the nightly memory mirror under 01_ai_consciousness/claude/memory). Each night the replay onto the advertised
main worked and the next step, `git reset --keep <target>` in dream_git_sync.ps1, was refused.

Cause. Since 10 Nov the sync indexes incoming files this computer does not hold at the target's entry and marks them
skip-worktree with a zero stat (dream_sync_index.py absent), so the move writes nothing for them. When a file later
appears on disk at such a path (a session writes it, a push lane leaves its copy, a restore puts it back), the mark
stays. core.sparseCheckout is unset in this clone, so `git reset --keep` compares a marked entry with the file, sees a
file against a zero stat, and refuses the whole move when the target changes that path. `git diff` and `git status`
skip marked entries, so the sync's facts helper and its parking rules never list the file, and the log could only say
"a locally modified file is among the incoming changes".

Measured 13 Nov 00:44, read-only: 576,059 index entries, 172,069 marked, 8 of those with the file on disk. Three
blocked the move, each holding exactly the incoming bytes: 08_other/career_yitz8/board_sweep_20261110/web/WEB_EMS_ADS.tsv,
12_cognitive_architecture/brain_graph/bin/live_membrane.py, 12_cognitive_architecture/dreaming/gh_offload/gh_offload.py.
Three more were the task checklist's own files (CHECKLIST.md, ledger.jsonl, state.json), live and different from every
commit: edits no git command was showing.

Fix (installed 13 Nov 00:55, brain commit 25f1f54c26c6). dream_sync_index.py has a new subcommand `present`: it clears
the mark on every marked entry whose file exists, and refreshes the stat of an entry whose file holds the index's own
bytes. dream_git_sync.ps1 calls it (Clear-SkipMarkOnPresentFiles) just before it lists the incoming paths, and logs
"N file(s) the index marked as not held on this computer are on disk". After that the file is an ordinary tracked
file and the existing rules for edited files apply (same bytes as incoming: indexed in place; a live working file:
kept at its local bytes). Originals kept as *.bak_skipmark_20261113.

Controls (test_dream_sync_present.py, a scratch origin and checkout, the real Sync-LocalMainToAdvertised): with the
old scripts the move is refused, 11 of 11 checks; with the new ones it goes through, 14 of 14 (incoming-bytes file
untouched, clean file updated, third-version file kept and shown as edited, a marked path with no file stays marked,
a new incoming file is not written).

Not yet seen on the live clone: tonight's dream had loaded the old script before the install and was refused again at
00:55. The first live run is the next dream. It holds if the log shows the "mark was cleared" line and "local main
rebased onto the advertised main", and local_only_check.py then finds about 0 paths absent on origin/main. If the move
is refused again, read "git said:" in the log line: it names the entry.

How to apply: when a move is refused with "Entry ... not uptodate", run `git ls-files -v -- <path>`; a leading S with
the file present on disk is this case. Never reset, stash or check out in the clone by hand to get past it.


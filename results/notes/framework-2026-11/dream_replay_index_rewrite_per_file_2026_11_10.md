---
name: dream_replay_index_rewrite_per_file_2026_11_10
description: "[PROVISIONAL] Dream sync never finished replaying a big backlog (push blocked since 21 Oct)? dream_tree_replay.py rewrote the 50 MB index once per conflicted file (11 of 86 commits in 95 min) and declined on a non-ASCII conflicted name; batched --index-info + merge-tree -z: 63 commits in 13.6 min"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T06:40:09+02:00
  status: provisional
  evidence: ""
---

Why did the dream's sync never finish replaying a large backlog onto main (the nightly push blocked from 21 Oct)?
Two faults in `~/.claude/dreaming/dream_tree_replay.py`, found 10 Nov 2026 by running it on the real brain clone
with a progress file, not by reading it.

1. One index rewrite per conflicted file. `resolve_from_live` called `git update-index --add --cacheinfo` once per
   path. Every call rewrites the whole index (49.7 MB, about 377,000 entries on the brain clone), and each git call
   on that clone costs 2 to 6 s (7,428 packs). A commit with a few hundred memory-mirror conflicts took an hour.
   Measured: 11 of 86 commits in 95 minutes, then stopped by hand in the 12th commit after 56 minutes.
   Fix: hash all live files in one `git hash-object -w --no-filters --stdin-paths` (only when core.autocrlf is off
   and no converting attribute is set; the first two paths are also hashed the per-path way and a difference sends
   every path back to the per-path call), then ONE `git update-index -z --index-info` for the whole commit.
   Measured after: all 63 pending commits (23 more were already upstream as identical patches) replayed onto main in
   13.6 minutes; 2,900 memory-mirror conflicts resolved from the live files; exit 0.
2. A non-ASCII file name among the conflicts declined the whole replay. `git merge-tree --name-only` without `-z`
   prints such a name quoted with octal escapes; the quoted name matched no live file, so the tool said
   "conflicted on ..." and exited 3. Fix: `-z` and split on NUL.

Also added: env `DREAM_REPLAY_PROGRESS=<file>` gets one line per commit (k/N, commit, base, conflicts resolved so far),
so a slow replay can be told from a hung one.

Proof: `test_replay_batch.py` PASS 24 (same tree as the old per-file tool on ASCII names, live bytes stored, non-ASCII
fixture, autocrlf fallback stores what `git add` stores, progress lines); `test_replay_rules.py` PASS 18 on the patched
tool; the real run above.

How to apply: a tool that loops `git update-index` (or any index-writing git call) per path is quadratic on a big
index; batch through `--index-info`. Any git output parsed for path names needs `-z`. A long silent job on this clone
gets a progress file before it is trusted. Sibling sites checked: `--cacheinfo` appears nowhere else in the dreaming
folder's code paths (one recipe text in brain_checkout_guard.py), `merge-tree` only in this tool.

Related: [[the_dreams_sync_refused_edited_copies_and_could_skip_a_commit_2026_09_23]],
[[dream_sync_worktree_fallback_checked_out_356k_files_for_a_day_2026_11_04]],
[[dream_commit_over_256mb_total_needs_split_big_commit_2026_11_07]],
[[dream_rem_died_on_weekly_limits_arms_now_by_live_usage_codex_last_2026_11_10]].
Status: provisional until a nightly dream has pushed with the landed tool.


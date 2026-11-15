---
name: dream_catchup_merged_in_scanned_parts_2026_11_10
description: "Dream push blocked since 21 Oct: the 86 local commits reached GitHub main as merge 7d2359a02332 - replayed, cut by path into two parts each scanned clean, pushed to a side branch, merged on the server; 162.5 MB of redundant carried prompt-log snapshots dropped first"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T07:10:40+02:00
  status: provisional
  evidence: ""
---

How did the 86 dream commits stuck on the laptop since 21 Oct reach GitHub, and what almost went up with them?
They are on main of brain-repo as merge commit 7d2359a02332 (10 Nov 2026 07:02 local; parents
f5f56d70a9b1 = main at that moment, 274b521c5e48 = the catch-up). Verified afterwards by a separate fetch: main
contains the merge and the catch-up, 7,770 paths came in, the side branch is deleted.

The route, each step a tool in the scratch folder that lands in ~/.claude/dreaming:
1. Replay the local commits onto main with the batched dream_tree_replay.py (63 commits, 13.6 min; 23 more were
   already upstream as identical patches).
2. Squash the replayed chain to one tree (build_squash.py), then cut that tree into parts by path under the secret
   scanner's bounds (build_parts.py --budget; scanner refuses over 25,000 objects, 64 MB an object, 256 MB a range).
   Two parts: 170.0 MB / 13 paths and 157.5 MB / 7,757 paths.
3. Scan each part with scan_secrets.py --range A..B, reading the exit code directly; a part is pushed only when its
   own line says rc=0 and exactly one output line "secret scan clean" (publish_parts.sh refuses otherwise).
4. Push the parts in order to a NEW side branch (never force), then merge that branch into main on the server with
   POST /repos/<slug>/merges (merge_branch_api.py). The server makes the merge commit atomically, so no peer push can
   be lost to a race; 409 would have meant a real conflict (main had touched none of the catch-up's paths).
5. Verify as its own later step (ls-remote, fetch, merge-base --is-ancestor), then delete the side branch.

What the smell test caught before the push: the first build (three parts, 490 MB, all scanned clean) carried seven
snapshots of two monthly prompt logs under sync_carried/, 195 MB. Six of them (162.5 MB) held no line that another
file in the same tree did not hold: the October copies were inside PROMPTS_2026-10.jsonl / .p01 / .p02, the older
November copies inside the newest one. drop_held_carried.py proved that line by line and dropped them. One November
copy stays (sync_carried/95f7037382/.../PROMPTS_2026-11.jsonl, 32.3 MB, 24,802 lines): main's own
PROMPTS_2026-11.jsonl is another computer's 47 KB file and the laptop's live prompts/archive folder is gone, so that
carried copy is the only place the laptop's November prompt log exists on GitHub.

The rule that came out of it, now in dream_tree_replay.py (fixture test_replay_held.py, 18 checks): a .jsonl log is
carried only when it has a line that no same-stem sibling and no carried copy holds, and an older carried copy goes
when a newer one contains it. Any other file type is carried as before; a blob that would need a fetch counts as
holding nothing.

How to apply: a clean secret scan says nothing about whether the bytes belong. Before a large push, list the largest
paths and ask what each one is. A backlog too big for one scan is cut by path into parts that each scan clean, goes
to a side branch, and is merged on the server.

Related: [[dream_replay_index_rewrite_per_file_2026_11_10]], [[dream_commit_over_256mb_total_needs_split_big_commit_2026_11_07]],
[[the_brain_repo_outgrew_git_pushes_every_landing_goes_by_the_api_gist_2026_11_02]],
[[dream_rem_died_on_weekly_limits_arms_now_by_live_usage_codex_last_2026_11_10]].
Status: verified for the merge; the landed tools are provisional until a nightly dream has pushed with them.


---
name: diag31_trace_codex_brain_losses_were_second_memory_not_surfaced_2026_11_09
description: "[PROVISIONAL] Mostly recall reach (DIAG31 trace): on D08/D13 all 12 Codex brain runs surfaced one of two gold memories, never both; grep had both in 10 of 12; joins lose the second memory (both surfaced Claude 22/72, Codex 29/72)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T13:04:23+04:00
  status: provisional
  evidence: "keys_private/diag31/trace31.py counts with a 200-decoy-name control; DIAG31 results 70e1103977"
---

Recall reach, mostly (DIAG31 trace, 9 Nov 13:04). On the two DIAG31 items where Codex grep beat Codex brain by 4-5 points (D08, D13), every one of the 12 Codex brain runs surfaced exactly one of the item's two gold memories and never both, while Codex grep had both names in its transcript in 6 of 6 and 4 of 6 runs. On the third (D02, -6) both arms had both names in 4 of 6 runs, so that loss is in reading or joining, not surfacing.

How it was measured: a gold memory counts as seen when its file name appears anywhere in the run transcript (keys_private/diag31/trace31.py, private, prints counts only). Control with 200 random snapshot names that are not gold: brain runs show 1-5 of 200 (about 2%), so a name in a brain transcript means recall returned it. Codex grep runs show 17-84 of 200 (8-42%): it prints broad rg -l listings, so for Codex grep "seen" overstates what it read; its gold rate (15-24 of 24 a run) is still well above its decoy rate. Claude grep is narrow (6-8 of 24 gold, 0-4 of 200 decoys), which fits its low score (28.5 of 72).

Per run, brain recall surfaced about 14 of the 24 gold memories for either runtime (Claude 10-17, Codex 12-16). Across the 12 plants, runs where recall surfaced both memories of an item: Claude 22 of 72, Codex 29 of 72. The second memory of a two-memory join is where recall loses; that is the recall target for the next improvement, and a join item bank like DIAG31's is the test for it.

Related: [[diag31_fresh_joins_claude_brain_beats_grep_11p5_codex_loses_5p5_2026_11_09]], [[brain_arm_misses_are_surfacing_misses_seen_426_of_479_unseen_23_of_331_2026_11_09]], [[hunt_clue_recall_reach_3pct_alone_agent_rewording_65pct_2026_11_09]].


---
name: diag30_codex_brain_vs_grep_single_memory_4p5_exclusion_not_the_cause_2026_11_09
description: "No (DIAG30): Codex brain 46.5 vs grep 42.0 of 72 on single-memory items with test memories hidden (+4.5, pooled with DIAG24 +2.5); the exclusion does not explain DIAG29, grep's drop on join items does"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T11:35:39+04:00
  status: provisional
  evidence: "DIAG30 blind grade, marks hashed 11:33:37 before runmap; PREREG 3f07a4e6ad, results 38201a05fd; rows recompute equal"
---

No (DIAG30, 9 Nov 11:08-11:33). Hiding test-result memories from recall does not explain Codex's DIAG29 jump. On DIAG21's single-memory items (12 plants, 6 controls, of 72), Codex gpt-6.1-sol high with brain recall (eachhi, 48+ questions, BRAIN_RECALL_EXCLUDE on) scored 46.5 against grep's 42.0: +4.5, items 5 higher / 2 lower / 5 tied, under the bar of 9. The pre-registered prediction was +5. Strict line +3.0. Pooled with DIAG24 (same items, no exclusion, 12 runs an arm): 45.0 against 42.5, +2.5 (6/3/3).

What it means: the brain arm is stable across these items with or without the exclusion (DIAG24 43.5, DIAG28 47.5, DIAG30 46.5). What changes between DIAG29 and here is grep: 27.0 of 66 when the two causes sit in two memories (DIAG29), 42.0 when both sit in one memory. On Codex the brain's edge over grep is joining memories, not finding one. Claude, by contrast, beat grep on single-memory items too (+13 to +18.5, DIAG21-DIAG25).

For the next test: put the effort on join items, or harder single-memory items where grep's name and keyword search falls short; pooled single-memory items with Codex are a tie.

Graph: brain-graph-full-2026-11-07 (11,982,982 directed + 4,828,684 co pairs = 16,811,666 edges), live sidecar link walk 243,689 rows, brain.py sha 05e65f47622f. Grading: one blind sheet, marks hashed 11:33:37 before the runmap opened, mark sums cross-checked (177 = 93 + 84 plant points; 71 controls), rows recompute equal. 12 of 12 runs valid. One leak hit was a name hit (this session's id in a math memory's originSessionId line): kept in the primary line, voided in the strict line. Wave 3 ran two arms at a time instead of four, at another agent's request for bandwidth; nothing was stopped.

Results: the private brain repository 12_cognitive_architecture/brain_improvement/DIAG30_20261109 (PREREG 3f07a4e6ad, results 38201a05fd). Related: [[diag29_codex_brain_beats_grep_joins_pooled_11p7_read_each_no_gain_2026_11_09]], [[diag24_codex_brain_ties_grep_six_runs_0p5_pooled_2p7_of_72_2026_11_09]], [[diag28_codex_reword_advice_minus_4p5_of_72_2026_11_09]], [[diag27_claude_brain_beats_grep_join_items_18_of_66_2026_11_09]].


---
name: diag31_fresh_joins_claude_brain_beats_grep_11p5_codex_loses_5p5_2026_11_09
description: "[PROVISIONAL] Claude yes, Codex no (DIAG31): fresh two-memory items, Claude brain 40.0 vs grep 28.5 (+11.5), Codex brain 38.0 vs grep 43.5 (-5.5) of 72; Codex's DIAG29 join gap was its item set"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T13:02:35+04:00
  status: provisional
  evidence: "the private brain repository 12_cognitive_architecture/brain_improvement/DIAG31_20261109 results 70e1103977"
---

Claude yes, Codex no (DIAG31, 9 Nov 11:55-13:01). On 18 fresh items no earlier test used (12 planted faults whose two causes sit in two different memories, 6 clean controls, of 72), Claude claude-opus-5-5 high with brain recall (eachhi, 48+ questions) scored 40.0 against grep's 28.5: +11.5, items 9 higher / 0 lower / 3 tied, past the bar of 9. Codex gpt-6.1-sol high with brain recall scored 38.0 against grep's 43.5: -5.5, items 3 higher / 6 lower / 3 tied. The pre-registered prediction was both passing (Claude near +15, Codex near +10).

What it means: Claude's edge on joining two memories replicates on fresh items (DIAG27 had +18.0 on DIAG16's items). Codex's DIAG29 gap (+18.5 on the same DIAG16 items) does not: it was that item set. The two brain arms were close (Claude 80, Codex 76 of 144 plant points); the gap between runtimes is grep (Codex 87, Claude 57). Codex is a much better grepper than Claude on these items, so the brain adds little for Codex and a lot for Claude. Claude's brain runs also took half the time of its grep runs (2.4 vs 4.9 min mean); Codex brain 5.3 vs grep 4.5 min.

For the next test: trace the three items where Codex grep beat Codex brain by 4-6 points (D02, D08, D13 in DIAG31's numbering) in the transcripts: did recall miss a gold memory, or did Codex read it and not join it? Pooling Codex join results (DIAG16/26/29 on one item set, DIAG31 on another) should be done item-set-aware.

Graph: brain-graph-full-2026-11-07 (11,982,982 directed + 4,828,684 co pairs = 16,811,666 edges), live sidecar link walk 244,281 rows, brain.py sha 8b9b76618520 at launch (the PREREG named 05e65f47622f; another agent edited brain.py between them, recorded as a deviation). BRAIN_RECALL_EXCLUDE on for both runtimes. 24 of 24 runs valid, no leak hits, all brain runs 64-80 questions, so strict and per-protocol lines equal the primary. Rulings hashed 12:01:13 before any sheet existed; marks hashed 12:59:35 and 13:00:40 before the runmaps opened; mark sums cross-checked (Claude 137 = 80 + 57, Codex 163 = 76 + 87; controls 36/36 in all four cells); rows recompute equal.

Results: the private brain repository 12_cognitive_architecture/brain_improvement/DIAG31_20261109 (PREREG abc48ca5c8, results 70e1103977). Related: [[diag27_claude_brain_beats_grep_join_items_18_of_66_2026_11_09]], [[diag29_codex_brain_beats_grep_joins_pooled_11p7_read_each_no_gain_2026_11_09]], [[diag30_codex_brain_vs_grep_single_memory_4p5_exclusion_not_the_cause_2026_11_09]], [[diag25_claude_brain_beats_grep_six_runs_18p5_pooled_17_of_72_2026_11_09]].


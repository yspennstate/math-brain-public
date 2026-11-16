---
name: diag25_claude_brain_beats_grep_six_runs_18p5_pooled_17_of_72_2026_11_09
description: "[VERIFIED] Yes (DIAG25): Claude brain arm 44.0 vs grep 25.5 of 72 over six runs each, +18.5, 12/0/0 items; pooled with DIAG22 +17.0. Codex ties on the same items; the gap is Claude grep's"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T08:48:53+04:00
  status: provisional
  evidence: ""
---

Yes, and more runs made it larger (DIAG25, 9 Nov 2026, a second machine). With six runs a cell, Claude's brain arm (eachhi: recall with the 48+ question advice) scored 44.0 and plain grep over the frozen memory copy 25.5 (plant points of 72, scaled to 3 runs, bar 9): +18.5, items 12 higher / 0 lower / 0 tied. Pooled with DIAG22's three runs a cell on the same 18 items: eachhi 41.7, grep 24.7, +17.0 over nine runs each (11/0/1).

Claude lines on these items: DIAG21 +13, DIAG22 +14, DIAG25 +18.5. Codex lines: +1, +7, +0.5, pooled +2.7. So the brain beats grep for Claude and ties for Codex, and the gap is grep's: Codex grep reaches about 43 of 72, Claude grep about 25, recall brings both to about 44.

Prediction (PREREG before runs): H1 holds, near +11, pooled near +12. Direction right, size low by 7.

Validity: 12 of 12 runs valid; eachhi asked 56 to 72 questions (compliant); leak check clean; deny control 131 checks 0 wrong, 2 wrong unpatched; marks hashed 08:47 before the runmap opened; mark sum 139 equals 88 + 51; pooled DIAG22 rows re-add to its published 37 and 23. eachhi runs 2-3 min, grep runs 4-17 min.

How to apply: when quoting a brain-vs-grep result, name the runtime. For Claude agents the recall arm is worth it on diagnosis items like these; for Codex, test items where in-file search cannot reach the answer before claiming a gain.

Results: brain-repo 12_cognitive_architecture/brain_improvement/DIAG25_20261109 (0055e30ef6; PREREG d3c2a235d5).

Related: [[diag24_codex_brain_ties_grep_six_runs_0p5_pooled_2p7_of_72_2026_11_09]] (the Codex twin of this run), [[diag21_brain_48q_beats_grep_claude_13_codex_ties_1_of_72_2026_11_09]] (first Claude +13), [[diag22_grep_name_listing_not_claudes_gap_brain_beats_grepls_10_and_19_2026_11_09]] (the rows pooled here), [[diag23_hashed_names_cost_grep_nothing_claude_26_28_codex_42_41_of_72_2026_11_09]] (grep's score does not come from file names), [[pgrep_guard_matched_own_launch_shell_and_grep_v_grep_hid_grep_arm_2026_11_09]] (two traps hit launching this run).


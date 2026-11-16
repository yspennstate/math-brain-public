---
name: diag33_coused_pairs_no_lift_claude_minus_4p2_codex_plus_0p5_of_72_2026_11_09
description: "[VERIFIED] No (DIAG33): two causes in really co-used memories did not widen brain's lead over grep; Claude brain-grep +10.5 R vs +14.7 shuffled (interaction -4.2/72), Codex -2.0 vs -2.5 (+0.5); brain still beats grep for Claude"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T15:58:00+04:00
  status: provisional
  evidence: "brain-repo 12_cognitive_architecture/brain_improvement/DIAG33_20261109/RESULTS.md (75a04a16b8)"
---

Question: when a fault's two causes sit in two memories that really were used together (graph co-use pairs, weight 4.1-24.5), does the brain arm's lead over grep grow, compared with the same 24 memories paired at random?

Answer: no, for either runtime (DIAG33, 9 Nov 2026, 48 runs, 46 valid, graded blind, marks hashed before unblinding).

- Claude Opus 5.5 high: brain - grep = +10.5 on co-used pairs, +14.7 on shuffled; interaction -4.2 of 72 (bar 9). Brain beat grep in both banks, as in DIAG25-31.
- Codex gpt-6.1-sol high: -2.0 and -2.5; interaction +0.5. Brain ties grep, as in DIAG24/26/30.
- Strict and per-protocol variants give the same verdicts.
- Brain-arm points barely changed between banks (Claude 25.5 vs 25.2, Codex 26.5 vs 29.0). Claude's negative interaction comes from its grep arm doing better on R (15.0 vs 10.5).
- Both gold memories reached the brain arm more often on co-used pairs (23 of 144 item-runs vs 9 of 132), matching the recall-only check (partner in top 8: 82 of 200 vs word search 45, shuffled 0-1), but too rarely to move points.
- Median seconds per run: Claude brain 145-175, Claude grep 239-246, Codex 242-300.

Lesson for next tests: the graph's co-use signal helps recall reach the second memory on its own, but agent scores on two-cause items are not limited by that reach. Codex still does not gain from the brain arm on these items.

Harness fix found while grading: apply_validity17.py (copied since DIAG17) named its project folder DIAG18, and reaudit cut violations to 200 chars, so the own-tool-output ruling never fired after DIAG18. Fixed in the diag33 copies (RUN-based folder, full command). DIAG31/32 had no voids of that kind. Any harness copied from diag31/32 should take the fixed version.

Public: brain-repo 12_cognitive_architecture/brain_improvement/DIAG33_20261109/ (PREREG.md 793de2a3b9, RESULTS.md and rows 75a04a16b8). Graph: brain-graph-full-2026-11-07, 16,811,666 edges; brain.py 05e65f47622f.


Related: follows [[jr2_join_items_random_pairs_4_of_55_linked_graph_cannot_help_2026_11_09]] (random pairs, so the graph could not help; this test gave it real pairs), [[diag31_fresh_joins_claude_brain_beats_grep_11p5_codex_loses_5p5_2026_11_09]] (same harness and items shape), [[diag32_codex_join_sentence_plus_3p5_of_72_surfacing_unchanged_27_26_2026_11_09]] (Codex prompt change, also inside the bar), [[jr1_join_recall_no_query_rule_lifts_second_memory_4_of_43_2026_11_09]] (second-memory reach).

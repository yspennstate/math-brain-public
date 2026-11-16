---
name: diag20_asking_48_plus_beats_default_claude_5_codex_3p5_of_54_below_bar_2026_11_09
description: "Not by the bar (DIAG20): 48+ questions vs the default brain arm, Claude +5 (38 v 33 of 54), Codex +3.5 (+1.0 with a false void back); bar +9, predicted, held. Don't cap low; no 48 floor needed"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:43:16+04:00
  status: provisional
  evidence: "brain-repo 12_cognitive_architecture/brain_improvement/DIAG20_20261109 commit 5a2034c904; prereg 4a5ff03ea4"
---

Question: past the default, does asking the brain for more questions (48 or more) help the brain arm?

Not by the pre-registered bar (DIAG20, 9 Nov, DIAG18's frozen items, 9 plants and 6 controls, 10 tool calls, full store brain-graph-full-2026-11-07 with 16,811,666 edges, 3 runs per arm per runtime, graded blind, marks hashed before unblinding):
- Claude: eachhi 38 vs default each 33 of 54, +5 (items 4 higher, 1 lower, 4 tied; sign test p 0.375). Bar +9.
- Codex: eachhi 37.5 vs each 34, +3.5 on two valid eachhi runs; +1.0 with a falsely voided run put back (sensitivity).
- The prereg predicted both below bar (Claude about +3, Codex about 0). It held.

The curve for Claude with DIAG19: 26 at 16 questions or fewer, 33 at the default (24 to 30 questions), 38 at 48 or more. Claude's eachhi arm scored 38 in both tests. Extra questions surfaced about two more planted notes per run (10.3 to 12.3 of 18), which fits [[brain_arm_misses_are_surfacing_misses_seen_426_of_479_unseen_23_of_331_2026_11_09]]. Codex's default already asked 56 and 61 questions in two of three runs, so it had little room to move.

How to apply: tell agents not to cap recall low ([[diag19_question_cap_16_costs_claude_12_codex_10_of_54_2026_11_09]]); do not put a 48-question floor into the brain-arm prompt on this evidence. A 5-point gain at n=3 runs is not separable from noise; a test that wants to see it needs more runs or fresh items.

Harness: the DIAG19 slug false positive (a `brain.py node` slug containing "subprocess") voided a Codex run again, because apply_validity17.py has its own copy of the recall rule. Fixed in both places after scoring.

Results: brain-repo 12_cognitive_architecture/brain_improvement/DIAG20_20261109 (prereg 4a5ff03ea4, results 5a2034c904).


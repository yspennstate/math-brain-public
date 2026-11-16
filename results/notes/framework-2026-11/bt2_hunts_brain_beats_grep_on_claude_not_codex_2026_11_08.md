---
name: bt2_hunts_brain_beats_grep_on_claude_not_agent_11_08
description: "On Claude yes, on Codex no (8 Nov, BT2): strict stations of 120, Claude brain 31 vs grep 13 (paired 23/5, p 0.0009), Codex brain 67 vs grep 77 (9/19, p 0.087); budget cut post hoc; Codex grep 64% so bank too easy; BT3 enforces live"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:01:51+04:00
  status: verified
  evidence: "12_cognitive_architecture/brain_improvement/bt2_2026_11_08/RESULTS.md b2c0479e85; grade_budget.py"
---

Does the brain beat grep on scavenger hunts under a 12-command budget? On Claude yes, on Codex no (8 Nov, BT2, graded 13:0x, results pushed b2c0479e85 to 12_cognitive_architecture/brain_improvement/bt2_2026_11_08; ALL_TESTS row 4af5795cc0).

30 hunts, 120 ordered stations (40 two-memory joins, 20 corrected values), six arms. Brain graph brain-graph-full-2026-11-07, 376,111 nodes, 16.8M edges (partial-brain against the 1 Nov reference). Strict count (SCORING.md: every simple command counts), stations out of 120:
- Claude opus-5-5 high: brain 31, grep 13, bare 0. Paired 23 brain only, 5 grep only, 8 both, sign test p = 0.0009.
- Codex gpt-6.1-sol high: brain 67, grep 77, bare 13. Paired 9 / 19 / 58, p = 0.087.
Plain count (one per command run): Claude 76 / 50 / 3, Codex 74 / 77 / 50. Dropping the 11 hunts flagged for naming the controller session leaves 19 hunts and the same picture (Claude 20 vs 8, Codex 49 vs 57). The strict void rule changes only the bare arms.

Why the split: the budget was cut after the fact, not enforced live. Codex arms use few commands (median strict 17 brain, 13 grep), so the cut barely touched them, and Codex grep solved 64%, above the 30-60% band; for Codex the bank is too easy. Claude arms ran long (median 38 brain, 54 grep), so the cut removed most of grep's work and less of the brain's.

How to apply: quote BT2 per runtime, never pooled. Do not claim a brain advantage for Codex from it. BT3 (DESIGN_BT3.md, settled 13:0x) enforces the budget live with one counter for both runtimes, builds a harder blind bank calibrated on a reserve set against Codex grep, and drops bare.

Related: [[still_gate_blind_live_1_and_0_of_40_v2_20_and_29_2026_11_08]] - another brain-vs-bare result from the same day's fleet; [[codex_blind_brief_override_in_first_message_hooks_off_0_outside_paths_2026_11_08]] - how the Codex arms were kept blind.

[[bt2_arm_audit_missed_home_rooted_search_grader_ignored_budget_2026_11_08]] - the audit and grader fixes this grade ran under.

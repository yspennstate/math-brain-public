---
name: diag35_recall_floor_8_no_lift_claude_plus_4_codex_plus_3p75_of_72_2026_11_09
description: "[PROVISIONAL] No (DIAG35): floor of 8 recall results showed 41-67% more gold memories but only +4.0 Claude, +3.75 Codex of 72 (bar 9); ~0.29 points per extra gold shown"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T18:19:00+04:00
  status: provisional
  evidence: "private brain repository, 12_cognitive_architecture/brain_improvement/DIAG35_20261109/RESULTS.md@1e65539bca"
---

Does a floor of 8 recall results per question (BRAIN_EACH_MIN=8) lift brain-arm points on two-cause fault items? No (DIAG35, 9 Nov 2026), not by the bar of 9 of 72.

eachmin8 minus default eachhi, points of 72 scaled to 3 runs: Claude Opus 5.5 high +3.0 (R) and +5.0 (X), mean +4.0; Codex gpt-6.1-sol high +5.5 (R) and +2.0 (X), mean +3.75. 48/48 runs valid, controls 36/36 per cell. STRICT (void every leak hit): Claude R +4.3, Codex X +0.3. PP: Claude X +5.6.

The floor reached every call: 8.0 results per question in all four cells vs 2.9-3.8 default. Gold memories shown per run rose 41-67% (Claude 7.8->11.0, 6.0->10.0; Codex 10.3->16.2, 8.3->13.7 of 24). Points per run rose only 0.7-1.9. Pooled: 18.5 more gold shown per run bought 5.3 points, about 0.29 points per extra gold memory shown.

Where the loss sits (conv35.py, private): a cause whose gold memory was shown was earned 57% (Claude floor) / 60% (Codex floor) of the time, 58% / 71% at default; not shown, 15% / 24%. At 8 per question the gold memory still never appeared for 162 of 288 Claude causes and 109 of 288 Codex causes. Surfacing is still the larger loss, and ranks 4-8 convert worse than the top 3. Next lever: ranking the mechanism-naming memory into the top three, not list length.

Graph: brain-graph-full-2026-11-07, 16,811,666 edges, lambda 0.30. Graded blind, marks hashed 18:16 +04 before run maps opened. One R leak hit (a recall-tuning memory row) was ruled keep after hashing but before run maps were opened; the X one before sheets were read.

Results: the private brain repository 12_cognitive_architecture/brain_improvement/DIAG35_20261109/ (commit 1e65539bca).


Related: [[diag34_each8_lists_no_lift_claude_plus_3p25_codex_plus_1_of_72_2026_11_09]] - same question, where only one cell's lists grew; DIAG35 forced the length everywhere and got the same small gain.
Related: [[brain_arm_points_follow_surfacing_agents_rarely_open_codex_gap_is_grep_2026_11_09]] - surfacing rose here but points barely followed.

---
name: diag36_graph_dial_holds_tuned_gain_reverses_held_out_2026_11_09
description: "[VERIFIED] No (DIAG36): graph off +35 top-3 gold on tuned banks but -17 on held-out; dial stays 0.30"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T22:02:55+04:00
  status: verified
  evidence: "DIAG36_offline_ranking_20261109 commits 07419b62aa, 985da8ad2c, 883e4b0be5"
---

No (DIAG36, 9 Nov 23:12, final): no ranking setting beats the live default on both the tuned and the held-out set, so the graph dial stays at 0.30 and no agent arm was run.

Offline replay of every recall question the brain arms asked (DIAG34/35: all 96 runs; held-out DIAG30-32: all 30 runs, gold disjoint), depth 50, every setting back to back on the same run with a repeat of the default as noise floor (repeat matched on every run). Store brain-graph-full-2026-11-09, 17,343,916 edges, 386,583 nodes.

Top-3 gold change vs default, summed over runs (better/worse/same):
- graph off: tuned +35 (35/13/48; Claude +15, Codex +20), held-out -17 (4/16/10)
- lambda 0.15: tuned +25 (23/2/71), held-out -9 (2/9/19)
- qsem weight 0.15: tuned -8, held-out -10
Top 8 barely moves on tuned (-5, -1, +4) and loses on held-out (-6, -1, -5). Default top-3 gold per run: 7.7 tuned, 13.7 held-out.

**Why:** the tuned-bank gain from turning the graph down is a property of that bank; on fresh banks the graph is worth 17 top-3 gold over 30 runs. Losses on the tuned bank are one-off third-slot swaps, no hub memory crowding.

**How to apply:** tune a ranking dial only with a held-out bank and paired back-to-back runs (see [[recall_ab_separate_passes_read_moving_index_2026_11_09]]); a gain on the bank you looked at is not evidence. Follows [[diag35_recall_floor_8_no_lift_claude_plus_4_codex_plus_3p75_of_72_2026_11_09]]. Rows on GitHub: 12_cognitive_architecture/brain_improvement/DIAG36_offline_ranking_20261109/ (final commit 883e4b0be5).


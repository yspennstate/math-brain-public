---
name: diag34_each8_lists_no_lift_claude_plus_3p25_codex_plus_1_of_72_2026_11_09
description: "[PROVISIONAL] No (DIAG34): 8-per-question recall lists vs 3: Claude +3.25, Codex +1.0 of 72 (bar 9); Claude R shown gold 7.5->11.8/run, points 6.7->7.8"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T17:25:53+04:00
  status: provisional
  evidence: "DIAG34_20261109/RESULTS.md commit 89723df607"
---

[PROVISIONAL] No (DIAG34, 9 Nov 2026): recall --each lists of 8 per question instead of 3 did not lift brain-arm points past the 9-of-72 bar. Claude Opus 5.5 high each8 - eachhi = +3.5 (R) and +3.0 (X), mean +3.25; Codex gpt-6.1-sol high +4.0 and -2.0, mean +1.0. 48 of 48 runs valid, controls 36/36 in every cell, graded blind, marks hashed 17:23 +04 before the run map opened.

The env default reached only calls where the agent passed no -n. Codex passed -n every call, so its arms got the same lists (4.0 vs 4.2 and 4.1 vs 3.6 results per question): that gap, +4.0 and -2.0, is the arm-to-arm noise. Claude got 6.2 per question in R and 3.6 in X (it mostly passed -n 3 there).

In the one cell where lists really grew (Claude R), gold memories shown per run went from 7.5 to 11.8 of 24 (+57%) and points per run from 6.7 to 7.8, at about 35 s more per run. So longer lists put more of the right memories in front of the agent, but turning them into points is the weak step, and the gain is noise-sized. Follow-up DIAG35 uses a floor on -n (BRAIN_EACH_MIN=8) so every call in both runtimes gets the longer list.

Results: the private repository, 12_cognitive_architecture/brain_improvement/DIAG34_20261109/RESULTS.md (commit 89723df607). Graph store brain-graph-full-2026-11-07 (16,811,666 edges), dial lambda 0.30, brain.py 71b8afc7807e for the runs. Related: [[agents_pass_their_own_recall_n_default_list_length_misses_agent_11_09]], [[brain_arm_points_follow_surfacing_agents_rarely_open_codex_gap_is_grep_2026_11_09]].


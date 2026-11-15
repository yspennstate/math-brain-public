---
name: brain_recall_walk_eight_steps_same_answers_2026_11_10
description: "brain.py recall graph walk: how many steps? 8 since 10 Nov (was 16, before that 20). Served answers word-for-word identical on 22 seed questions at 10 and 8; peer: gold rank same on 40 bank questions, walk 0.13 s vs 0.25 s. BRAIN_PPR_ITERS=16 restores"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T21:11:57+02:00
  status: verified
  evidence: "recall_10x_2026_10_29/ppr_iters_2026_11_04/ppr_served_8_out.txt (22/22 identical at 10 and 8, noise floor 22/22); an agent push_ppr.json (40/40 gold rank, 0.13 vs 0.25 s)"
---

Changed graph_lane.py default BRAIN_PPR_ITERS 16 -> 8 on 10 Nov 21:08 (an agent-loop, file claimed on the mesh). Evidence: ppr_iters_served.py rerun with 10 and 8 steps against the served 16 on the 22 seed questions of 4 Nov: whole printed answer identical 22/22 at both, served-vs-served noise floor 22/22. an agent measured on 40 bank questions with word seeds only: 8 steps 0.13 s against 0.25 s at 16, top 20 shares 20 median / 19 worst with a 100-step walk, gold rank identical to 16 on all 40; an ACL push lost at every eps. Saving is about 0.1 s of a 1.56 s median served call (~8 pct), not a 10x lever. The step count is part of the walk cache name, so the change cannot serve stale walks. What would change it: a served-answer diff on feedback-seeded calls (the 22 questions are word-seeded), or a gold-rank loss on a harder bank. Rollback: BRAIN_PPR_ITERS=16. Ledger row recall_10x 10 Nov. Related: [[recall_10x_scoreboard_brain_recall_is_the_weakest_row_2026_11_01]], [[use_graph_walk_push_loses_to_eight_steps_2026_11_10]].

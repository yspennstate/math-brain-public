---
name: t307_one_step_dsm_finds_hidden_line_2026_11_01
description: [PROVISIONAL] T307: one large first-layer DSM gradient step on hidden-line data reaches oracle error + d/N (d=2..64); early-stopped GD stays lazy; Adam leaks off span
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T01:15:32+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T307 target 2 (1 Nov, an agent), pushed 0b4e9b7 to research-repo (research_pushes/2026-11-01-loop-T307-hidden-subspace), card claim_0d4f863d51a2486ab59809380c6c2b9d.

At N=1000 and d=64: one-step 0.0039 (alignment 0.992), oracle 0.0009, early-stopped heavy-ball GD 0.134 (alignment 0.10, random level), random features 0.19. At 4x the data the one-step excess over the oracle falls 3.8x.

Two traps worth keeping:
- Adam is not rotation-equivariant. In a hidden-subspace test it lets the output leave the label span and makes GD look as bad as random features. Use plain or heavy-ball GD for any subspace or equivariance claim.
- A one-step estimator that normalizes gradient rows gives 0/0 on dead ReLU units. Keep the initial row there.

Related: [[t319_fixed_width_depth_growth_stops_2026_11_01]], [[t390_score_matching_weight_are_closed_form_2026_11_01]].

---
name: t399_path_star_first_step_globality_2l_minus_1_2026_11_01
description: [PROVISIONAL] T399: path-star first-step k-way choice carries zero info in any 2l-2 tokens; globality >= 2l-1
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T22:10:10+04:00
  status: provisional
  evidence: ""
---

Path-star k arms of length l, random edge order, random labels. Target Y = rank of goal arm's s-edge among s-edges (removes the candidate-set leak a label target has; a label target has globality 1 trivially). Any T of <= 2l-2 tokens: I(Y;X_T)=0 exactly (tail-swap involution at a safe cut). Exact enumeration (2,2),(3,2),(2,3): first info at 2l-1 tokens, not 2l as guessed: an s-edge's parent token is redundant because the edge whose child is a_1 must be an s-edge. Later teacher-forced and reverse-order targets: one-edge lookups, globality 2. Separation in globality only; SQ bound (target 2) and the upper side for growing l are open. Grouped-by-arm order gives globality 1. Note research_pushes/2026-11-01-t399-path-star-globality (4a23a7e0), move 199d2f46. Method kin: exact small-case enumeration before claiming a threshold, as in [[t297_two_large_steps_stay_one_spike_rank1_truncation_exact_2026_10_31]]. Status: provisional (proof unreviewed).

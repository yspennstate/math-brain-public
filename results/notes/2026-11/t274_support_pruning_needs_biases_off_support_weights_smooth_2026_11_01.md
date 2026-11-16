---
name: t274_support_pruning_needs_biases_off_support_weights_smooth_2026_11_01
description: [PROVISIONAL] T274: same-init support-pruned subnet beats the full net 160/160 checkpoints only with trained biases; without them the full net wins late
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T22:34:21+04:00
  status: provisional
  evidence: ""
---

T274 target 1 numerics (research-repo research_pushes/2026-11-01-t274-support-pruning, move 16929bd6). Two-layer ReLU m=64, online SGD, k=5 sparse single-index teacher, d=400, 4 seeds, 2 teachers. With trained biases the pruned subnetwork from the same init is at or below the full net at 160/160 checkpoints and hits the full net's final error 2-4x sooner. Without biases it is ahead early but loses late (leap1 5-8/20 checkpoints; 7/8 runs never reach the full net's final error). Mechanism: given x_S each neuron sees w_S.x + r_j xi, a Gaussian-smoothed ReLU, and the off-support population gradient is a shrinkage proportional to w_{S^c} (Stein), not zero; bias-free ReLUs aligned with beta span only {z,|z|}, so the smoothing supplies the curvature. The dossier's 'same population dynamics, only noise' coupling sketch is wrong as stated. Measurement: dominance.txt in the note. Related [[t277_g_of_quadratic_form_is_csq_easy_above_op_norm_floor_2026_11_01]].

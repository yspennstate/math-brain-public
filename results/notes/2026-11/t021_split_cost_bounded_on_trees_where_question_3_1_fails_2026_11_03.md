---
name: t021_split_cost_bounded_on_trees_where_question_3_1_fails_2026_11_03
description: [PROVISIONAL] T021 FEI: do the trees that refute Han's Q3.1 also break the entropy split (GMP (21))? No - D_k/I_k converges (4.50 nats eps 1/4, 2.93 nats eps .01, L<=40) while Q_k -> infinity; brain main 6895b702
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T03:35:05+02:00
  status: provisional
  evidence: ""
---

Block recursion for D_k = H(f) - (H(f+)+H(f-))/2 on alternating read-once trees: D' = P[D - Phi(c0^2,c1^2) + Phi(4mu^2,c1^2)] - P^2 Phi(4mu^2,c1^2) + Phi(c0'^2,c1'^2), Phi 1-homogeneous pair entropy. Equal to truth-table D on 15 trees n<=16 (err 1.4e-15). D_k/I_k -> 4.5017 / 2.9290 nats to L = 40 while Q_k = 45.6 / 78.4. So only the sqrt(ab) relaxation fails; the loss is the S=empty pair (f^(empty)^2 ~ 1 vs f^(k)^2 = I^2, Phi ~ I^2 ln(1/I^2) but sqrt ~ I). SCAR: Phi cancels to O(c1^2), so mpmath at 50 digits silently lost the value past L = 20 (2.928977 -> 2.922859 blip); rerun at 1500 digits fixed it - size dps to the smallest squared coefficient, not to the answer. Convergence numerical only. Files rows/T021/exp/q31/q31_tree_entropy.*, card local_agent_T021_split_cost_bounded_on_trees_where_question_3_1_fails_20261103, edge 4. [[t021_han_question_3_1_is_false_alternating_read_once_trees_2026_11_03]]

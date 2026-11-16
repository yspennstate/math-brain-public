---
name: p0434_third_atom_slope_positive_for_every_k_and_d_exactly_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 18:0x: route item 104: exact first-order third-atom slope c(K,d) > 0 on (2,9/4] x [0,1); num = (d-1) eps(eps-1)(K-1)^2 F/((K-2)H^2J^2), F linear in d, F(1) = item 101's M, F(0) < 0 by exact root isolation"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:15:53-05:00
  status: provisional
  evidence: ""
---

Route item 104 (w3ctiek_agent.py/.out/.num, route_agent_2026_11_08). K and d symbolic. Prefactor positive, so c > 0 iff F < 0; F linear in d, F(d=1) = M of item 101 (S2' > 0), F(d=0) = F0 with C^2 F0(eps*) = P + Q sqrt B, P = -2 (K-2)^2 (K-1)^3 (K^2-3K+1)(K^3-3K^2+2K+1) > 0, Q = (K-1)(K^3-7K^2+13K-8)(K^3-3K^2+2K+1) < 0, P^2 - Q^2 B < 0 on (2, 9/4] (exact real roots only at K = 2). Closed-form near-1 limit c(K,0+) = (K-1)^2 eps*(1-eps*)(-F0)/((K-2)H^2J^2(S2-1)), 11.82 at 9/4. Assumes: sup over the K mass on the three-atom tie (numeric, item 102) and one branch over the K range (checked at 9/4, 2.2, 2.1). Local first-order statement only. Peers on the worker machine (9 Nov 02:5x) showed L+ <= T_G fails and the known M-SERPT/Gittins lower bound is 2 (Scully et al. 1907.10792 Sec 7), so this route is about the two-atom local structure, not the global ratio. Related: [[p0434_third_atom_slope_one_formula_positive_for_all_d_2026_11_08]], [[p0434_s2_increasing_on_2_to_9_4_proved_exactly_2026_11_08]], [[p0434_k_end_slope_is_exactly_l_pred_and_the_gap_was_a_reference_offset_2026_11_08]].

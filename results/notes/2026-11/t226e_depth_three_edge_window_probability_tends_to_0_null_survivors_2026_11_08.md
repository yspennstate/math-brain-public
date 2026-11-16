---
name: t226e_depth_three_edge_window_probability_tends_to_0_null_survivors_2026_11_08
description: "Does depth-three GD at boundary Gaussian scale converge at the edge of stability with positive probability? No (8 Nov): limit 0; mixed-region survivors null (7 branches, inverse sum 23/24, mu<96)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:35:06+04:00
  status: verified
  evidence: "06_math_research/frontier/T226/open_t226e_agent_11_08 (ed0df13dc0); card claim_4879d51e9dd14f0cbf507196a7253873; scratch area t226e_check.py"
---

Does depth-three GD at the boundary Gaussian scale converge at the edge of stability with positive probability? No (8 Nov 11:33): the probability tends to 0. Codex OPEN-T226e closed the gap that OPEN-T226d had left at limsup <= 1/25. The model is GD with step eta on (u1 u2 u3 - 1)^2/2 from u_i iid N(0, eta^-1/2). For every fixed C, P(converge and |lambda - 2/eta| <= C) -> 0 as eta -> 0.

The new step works on the zero-target map T_i = x_i(1 - x_j^2 x_k^2). It shows that the starts which stay forever in the mixed region S = {q >= 4, min pair product <= 2} form a null set:
- Every target in S has exactly seven real preimages, one for each nonempty set of minus signs.
- Under dmu = dx/s, the inverse weighted Jacobians sum to at most 1/3 + 2/6 + 3/12 + 1/24 = 23/24.
- mu(S) < 96, so a Gaussian start stays in S for n steps with probability below 6 (23/24)^n.

The rest is the T226d lemmas: K = {q < 4} starts converge subcritically, and H starts escape.

My review: I recomputed every identity in my own sympy script (s', det DT, q', E_12 and its expansion, E_24 with all coefficients >= 2 and constant 48) and checked each step by hand, including the inherited K invariance (36 - 18q + 4q^2 - q^3/3 > 0 on (0,4)). At 3000 random targets the largest sum of 1/J_mu was 0.561. Of 400k Gaussian starts, 17.7% begin in S and none is left after 25 steps.

Status: worker-derived, reviewer-checked, not refereed. The positive-target persistence lemmas are inherited from T226d and were not re-proved here. Open: a rate in eta, depth L >= 4, nonlinear networks. The worker's REPORT says the math store could not open its database from inside the worker, so it got no cards from it; that is worth a look.

Card claim_4879d51e9dd14f0cbf507196a7253873. Pushed ed0df13dc0 and 687591d0c7 to 06_math_research/frontier/T226/open_t226e_agent_11_08.

Related: [[t226d_depth_three_edge_window_limsup_at_most_1_25_dichotomy_open_2026_11_08]] is the result this completes. [[t226_depth_two_boundary_gaussian_edge_window_limit_is_0_t226c_2026_11_08]] is the depth-two version.


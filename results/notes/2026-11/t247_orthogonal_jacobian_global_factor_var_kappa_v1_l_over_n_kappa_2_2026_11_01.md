---
name: t247_orthogonal_jacobian_global_factor_var_kappa_v1_l_over_n_kappa_2_2026_11_01
description: [PROVISIONAL] T247: orthogonal critical tanh Jacobian's global scale has Var log = kappa v1 L/n, kappa 1.38-2 (-> 2 as q*->0), carried by the length mode; vanishes at fixed L v1
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T00:13:03+04:00
  status: provisional
  evidence: ""
---

Written 2026-11-01 00:13 +0400; T247 move 8baaa7d5, files gf_* at 300acef0. Haar Q makes h_l uniform on its sphere given its length, so the scale noise is sphere-projected: per-layer noise P[f] is only 0.3-3% of v1; the variance comes from the length q_l relaxing at rate psi, amplified 1/(1-psi). kappa = 4/3 (length) + 2/3 (bias, sigma_b^2 ~ q*^3) at small q*. Measured/theory 0.84-1.04 on 15 cells, mean ~0.91. The shortfall is the net of three O(1/n) corrections, each amplified by the length mode (move 96f6f417): exact-sphere noise variance 0.74/0.86/0.96 of P[g] at n 32/64/256, the bias channel, and a fixed-point shift q/q* ~ 1 + 2/n (measured 1.048, 1.023). So kappa is the n -> infinity value, with relative error ~10/n. Trap: a Gaussian h_0 adds (2/n)(1-psi^L)^2 and swamped the first run (ratios 2.4-52 instead of ~1-2). Consequence: with V = L v1 fixed, Var -> 2V/n -> 0, unlike Gaussian weights (O(L/n)). Same radial mode as the psi^(2L) outlier in the T247 dossier Result 2; same off-sphere-init trap as any length-map fixed point.

Related: [[t246_deep_tanh_log_jacobian_var_2t_plus_var_log_yor_functional_2026_10_30]] is the Gaussian-weight counterpart: n Var/L -> 2 there with no v1 factor, against 2 v1 here, so orthogonal weights suppress the t-correction by v1.

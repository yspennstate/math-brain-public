---
name: d0047_carousel_pde_bulk_painleve_open_setup_verified_2026_11_14
description: "[PROVISIONAL] D0047 (Virag Operator limits Q9: derive sigma-PV for the bulk gap from the Brownian carousel PDE) still open 14 Nov - Rumanov has soft/hard edge only; ours: carousel PDE reduces to H(alpha, mu), mu = lam e^{-beta t/4}, matches the sine-kernel det to 6e-4 at beta=2"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T09:36:47+02:00
  status: provisional
  evidence: ""
---

D0047, from Virag, Operator limits of random matrices (ICM 2014), Question 9, PDF p.25. Literature, 14 Nov: two searches found Rumanov's Painleve derivations from the stochastic-operator PDEs only at the soft edge (1306.2117; beta = 6 in 1408.3847, quantum PII) and the hard edge (quantum PIII); nothing for the bulk.

Ours (simple, verified numerically), in 12_cognitive_architecture/math/trio_1011/op/D0047/NOTE.md (pushed bc7e4bfa):
- Gap probability = G(0, 0), with G_t + lam f G_alpha + 2 sin^2(alpha/2) G_alpha,alpha = 0 on [0, 2 pi], f = (beta/4) e^{-beta t/4}.
- G(2 pi) = 0; terminal G = 1 - alpha/(2 pi); no condition at alpha = 0.
- G depends only on (alpha, mu = lam e^{-beta t/4}): (beta/4) mu (H_alpha - H_mu) + 2 sin^2(alpha/2) H_alpha,alpha = 0; the gap is H(0, lam) at density 1/(2 pi).
- Backward Euler on 1200 points reproduces det(I - K_sine) on [0, L], L = 0.25..2, to within 6e-4.

Open step: a beta = 2 meaning for H(alpha, mu) with alpha != 0, and a Riccati/Lax structure in (alpha, mu); the same wall as the 8 Sep attempt D0047-A001. Related: [[c0002_dgff_intermediate_level_set_deviations_upper_tail_by_ahs_rate_and_fluctuations_open_2026_11_14]].

Off-axis profile (14 Nov 10:0x, NOTE.md section "The profile off alpha = 0"): with x = alpha/2pi, H(alpha, 2piL) = E(L+x) + O(x^3)
at beta=2 (slope and curvature match E', E'' to 1e-3 on two grids). Reason: the drift has total mass lambda, so an initial
angle is drift delivered as an atom at t=0. Beyond second order neither "L+g(x)" (g depends on L: 0.511/0.565/0.587 at x=1/2
for L=0/0.5/1) nor E[(1-N[-x,0])1{gap}] (negative at x=0.83) is the formula. Determinantal meaning still missing.

---
name: t413_gaussian_ct_fixed_point_is_product_of_cosines_sqrt_d_over_eps_2026_11_01
description: [PROVISIONAL] T413 target 2: on N(0, sigma^2 I) the CT population fixed point is a*(T) prod cos theta_n, so W2 >= sqrt(d) sigma (1 - exp(-Theta^2/2N)); equal angles attain it; N ~ sqrt(d)/eps, not d^(5/2)/eps
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T00:54:28+04:00
  status: provisional
  evidence: ""
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

Written 2026-11-01 00:54 +0400; T413 move 356cff4d, files f9e29fbf (ct_gauss.py/.txt). Recursion a_(n+1) = a_n (s^2 + t_n t_(n+1)) / (s^2 + t_(n+1)^2), with the per-step ratio the cosine of the angle between (s, t_n) and (s, t_(n+1)). CT always under-disperses. Measured N x err: equal-angle 1.213 vs floor 1.214, Karras 2.57, uniform-t 30.7 (s 1, T 80). Caveats: VE process, one scalar per time, Gaussian data; 2402.07802's metric and process differ. Related: [[t420_ising_rbm_ml_has_no_minimiser_hidden_copies_odd_spin_2026_11_01]] - same session, another exactly solvable population-optimum computation.

Update 2026-11-01 00:56: VP checked (move above, files ct_vp.*): same cosine law along (alpha_t sigma, beta_t), matches to 8 digits; DDPM uniform-time grid is 1.5-2.5x off optimal, VE uniform-t 25x.

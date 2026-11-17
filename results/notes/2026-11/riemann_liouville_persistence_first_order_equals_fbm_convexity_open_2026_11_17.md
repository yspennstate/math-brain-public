---
name: riemann_liouville_persistence_first_order_equals_fbm_convexity_open_2026_11_17
description: "[PROVISIONAL] Aurzada-Simon Conj. 7 (theta(beta) convex) CN0539: RL and fBM Lamperti correlations agree to O((H-1/2)^2) uniformly; Majumdar-Sire slope -1 at 0; no fractional-beta numerics; convexity needs theta(1/2)<=3/8"
metadata:
  type: project
  created: 2026-11-17
  created_at: 2026-11-17T03:50:03+02:00
  status: provisional
  evidence: ""
---

status: provisional. Catalogue CN0539 (Aurzada-Simon arXiv 1203.6554 Conjecture 7: beta -> theta(beta), the persistence exponent of fractionally integrated Brownian motion, is convex decreasing). Exact (Mandelbrot-Van Ness, folklore-level): sup_t |C_H(t) - E[L^H_0 L^H_t]| = O((H-1/2)^2), so the first H-derivatives at H=1/2 coincide: 2 sinh(t/2)(-log(1-e^{-t})). Heuristic (Majumdar-Sire PRL 77 (1996) 1420): theta'(0+) = -1, the integral is 2 pi; the same formula reproduces Molchan's fBM slope, so the bound theta(beta) >= 1/2 - beta (survey (3.9)) is tangent at 0. Not rigorous: the correlations' tails differ (e^{-t/2} against e^{-(1-H)t}). Literature numerics (Majumdar-Bray PRL 86 (2001) 3700, n = beta+1): theta(2)~0.231+-0.01, theta(inf)~0.1875; their IIA needs beta>1/2. No numerics for beta in (0,1/2]. Convexity needs 1/4 <= theta(1/2) <= 3/8. What would change it: a simulation of theta(1/2) with step extrapolation. Links: [[open_problem_catalogue_1128_probability_networks_computation_2026_11_16]] [[stenlund_a4_parity_condition_follows_from_sublinear_holding_gaps_2026_11_17]]

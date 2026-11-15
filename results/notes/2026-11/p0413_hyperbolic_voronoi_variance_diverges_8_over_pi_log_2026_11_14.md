---
name: p0413_hyperbolic_voronoi_variance_diverges_8_over_pi_log_2026_11_14
description: "[PROVISIONAL] P0413 (ideal PVT Q7.7, arXiv 2303.16831): lam Var(typical cell area) in H^2 does NOT converge: (8/pi)log(1/lam) - 6.85; E vol(C_d minus T_d(R1)) infinite in every d"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T15:34:39+02:00
  status: provisional
  evidence: ""
---

P0413, 14 Nov 2026, an agent. Question 7.7 of D'Achille-Curien-Enriquez-Lyons-Unel asks whether lam V_d(lam) has a finite limit equal to E vol(C_d \ T_d(R1)). (1) Proved for d=2 from the deposition model (Thm 1.4, Sec 5.4): E area(C_2 \ T_2(R1)) = int du dv/v^2 [1/(1+1/v-2I/pi) - 1/(1+1/v)], I(u,v) ~ 2/|u|, so it grows like (8/pi) log U in a window |u|<U: infinite. The same estimate gives infinity in every d (large o-containing discs, expected radius infinite). (2) Quadrature in area variables, lam^2 Var = int (p(t)-e^-t) dt, lens by Gauss-Bonnet: lam Var = 0.257, 1.661, 5.481, 10.846, 16.626, 22.469 at lam = 1..1e-5; increments per decade -> (8/pi) ln 10 = 5.863, so lam V_2 = (8/pi) log(1/lam) - 6.85 +- 0.03. Checks: lam=100 gives 0.27990 vs planar 0.2802; MC of p(t) agrees within 1-2 se at 7 points; node refinement 1e-9 (1e-3 rel at 1e-5). SCAR: p(t) has a tail to t ~ 1/lam (midpoint nucleus, cost ~2 sqrt(pi lam t)); a t-grid cut at 64 gave NEGATIVE variances at lam <= 0.01 with both grids agreeing - a grid-refinement check cannot catch a missing range, the pointwise MC and the sign did. Divergence of lam V_2 and its rate are numerical, not proved. Files and NOTE: brain-repo 12_cognitive_architecture/math/trio_1011/op/P0413 (commit e3024c1e).

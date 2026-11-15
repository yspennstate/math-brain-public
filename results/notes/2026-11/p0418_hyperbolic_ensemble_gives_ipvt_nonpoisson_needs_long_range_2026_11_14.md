---
name: p0418_hyperbolic_ensemble_gives_ipvt_nonpoisson_needs_long_range_2026_11_14
description: "[PROVISIONAL] P0418 (D'Achille-Khezeli Q7.2): the suggested alpha-hyperbolic ensemble gives the IPVT again as alpha->0; any process with Poisson-like correlations beyond (1-eps)log(1/lam) does; a new limit needs correlation at 2log(1/lam)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T17:47:26+02:00
  status: provisional
  evidence: ""
---

P0418, 14 Nov 2026, an agent, status provisional (written once, reread once, no independent audit).
Proved: on H^2, if rho_k <= C^k lam^k and rho_k/lam^k -> 1 uniformly on configurations in B(o, t+b) with pairwise distances >= (1-eps) t, t = log(1/lam)+O(1), then the shifted nuclei converge to the Poisson limit (factorial moments; bad tuples carry O(lam^eps)) and by D'Achille-Khezeli Prop 3.3 the Voronoi diagrams converge to the IPVT.
Corollary: BGZL22 (arXiv 2202.11687 Def 1.2) kernel is (alpha/pi)(1-|z|^2)^{(alpha-1)/2}(1-|w|^2)^{(alpha-1)/2}/(1-z wbar)^{alpha+1}; intensity alpha/(4pi) per hyperbolic area; normalized correlation sech^{2(alpha+1)}(d/2); Hadamard gives rho_k <= lam^k. So the natural candidate is a NEGATIVE answer: it gives the IPVT.
A non-IPVT limit needs pair correlation off 1 by order one at distance 2log(1/lam)+O(1). Mixed Poisson, bounded clusters, far offspring, Matern II all fail. Candidate left open: hard-core gas with exclusion 2log(1/lam)+c, whose limit is a hard-core horoball gas.
Files: 12_cognitive_architecture/math/trio_1011/op/P0418/NOTE.md, STATUS.md. Would change if: the DK Prop 3.3 proof needs more than convergence of shifted nuclei, or the H^2 IPVT is degenerate.

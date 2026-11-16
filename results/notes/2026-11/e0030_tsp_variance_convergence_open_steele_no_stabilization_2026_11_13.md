---
name: e0030_tsp_variance_convergence_open_steele_no_stabilization_2026_11_13
description: "E0030 (Chatterjee AoP 2019 open problem (2), Steele's conjecture: Var of the optimal TSP tour on n iid uniform points in [0,1]^2 converges to a constant) is open on 13 Nov 2026: arXiv check through Nov 2026 finds no variance-limit or CLT for the Euclidean TSP. Known: liminf Var > 0 (Rhee 1991, Chatterjee Thm 2.3) and Var bounded. The missing input is a stabilization/locality estimate for the optimal tour; the 2026 localization frameworks (Blaszczyszyn-Yogeshwaran-Yukich, Trauthwein-Yukich) do not verify it for TSP. Codex E0030A: conditional criteria plus torus numerics only"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T16:20:06.811Z
---

E0030, rank 40 on the 200 list. Source: Chatterjee, "A general method for lower bounds on fluctuations of random
variables", Ann. Probab. 47(4) (2019), arXiv 1706.04290v3, Section 3 open problem (2), PDF p.27. For n iid uniform
points in [0,1]^2, show Var(T_n) of the optimal tour length converges to a constant, and identify it. Chatterjee
attributes the conjecture to Steele.

Status 13 Nov 2026: open.
- Known: Var(T_n) is bounded above and below by positive constants in the plane (lower bound Rhee 1991, and Chatterjee
  Theorem 2.3, p.12, order n^{(d-2)/(2d)} fluctuations in every d >= 2). Convergence of the variance is the open part.
- My arXiv check, 13 Nov: abstract searches for traveling/travelling salesman with variance, fluctuations and central
  limit, "optimal tour" with random, "Euclidean functionals", and title "salesman" in math.PR, all through 2611. No
  paper proves a variance limit or a CLT for the optimal Euclidean tour. Recent TSP papers are about the mean constant
  beta: Dong-Cao 2610.02809 (bounds on beta), Gaudio-Guan 2602.11250 (upper bound on beta by band crossovers).
- The Codex run E0030A (06_math_research/referee_reports/2026-11-13/E0030A/REPORT.md, PARTIAL, unrefereed) checked the
  stabilization literature with theorem numbers: Penrose-Yukich 2001, Yukich LNM 2068 Thms 8.5/8.6, Chatterjee-Sen MST
  CLT, Kesten-Lee, Blaszczyszyn-Yogeshwaran-Yukich (May 2026 Lipschitz-localized statistics, Prop 5.3/Thm 5.4) and
  Trauthwein-Yukich (2026 second-order Poincare). None verifies a locality hypothesis for the optimal tour. Its own
  results: an elementary bound Var <= 8 on the square (<= 2 on the torus); Proposition 2, variance convergence for the
  Poisson torus/cube CONDITIONAL on an unproved L2 locality estimate for add-one costs, via an exactly solvable
  disconnected block surrogate; Proposition 3, conditional de-Poissonization; heuristic 2-opt/Or-opt torus tours up to
  n = 10000 with variance about 0.0346 (heuristic tours, not optimal ones; evidence of order-one fluctuations only).
- The obstruction is the one our 8 Sep first pass (E0030-A001) named: the TSP is not known to stabilize. Boundary
  functionals control the mean to O(sqrt n), which is the same order as the fluctuation, so they give nothing for the
  variance.
- Nearby, for matching instead of tours: Feng arXiv 2610.14337 (v2 3 Nov 2026) proves the sharp variance upper bound for
  Euclidean minimum matching. See [[e0031_euclidean_matching_fluctuation_lower_bound_open_feng_upper_2026_11_13]].

Related: [[p0359_brw_ray_local_time_spectrum_open_skiredj_berrada_liminf_positive_2026_11_13]] (previous item in this
loop).

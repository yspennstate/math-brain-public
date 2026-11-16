---
name: e0031_euclidean_matching_fluctuation_lower_bound_open_feng_upper_2026_11_13
description: "E0031 (Chatterjee AoP 2019 open problem (3): tight fluctuation lower bound for the Euclidean minimum matching of n uniform points in [0,1]^d) is half settled on 13 Nov 2026: the sharp UPPER bound Var(M_n) <= C d n^{1-2/d} is new (Shi Feng, arXiv 2610.14337, v2 3 Nov 2026; bounded variance in d=2, answering Rhee 1994). The matching LOWER bound c_d n^{1-2/d} for all n, and anti-concentration at scale n^{1/2-1/d}, remain open. Codex E0031A proves it on an infinite subsequence and a weaker all-n bound n^{1-3/d}; the gap is a lower bound on mean increments mu_n - mu_{n-2}"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T16:20:20.209Z
---

E0031, rank 41 on the 200 list. Source: Chatterjee, Ann. Probab. 47(4) (2019), arXiv 1706.04290v3, Section 3 open
problem (3), PDF p.27: prove a tight lower bound for the fluctuations of the minimal matching length of uniform points in
[0,1]^d. The model is one-colour (non-bipartite) perfect matching, n even, Euclidean cost to the power 1. The target is
fluctuations of order n^{1/2-1/d}, that is c_d n^{1-2/d} <= Var M_n, and Chatterjee's Definition 1.1 (p.3) also asks for
anti-concentration at that scale, which a variance bound alone does not give.

Status 13 Nov 2026: partial.
- New upper bound, outside group: Shi Feng, "Variance bounds for minimum perfect matching problem by random walk on
  multinomial distribution", arXiv 2610.14337 (v1 9 Oct, v2 3 Nov 2026), Theorems 1.1-1.2. Var(H_n) <= C d n^{1-2/d}
  with C free of n and d, by a rapidly mixing Markov process with multinomial stationary law. This removes Talagrand's
  1995 log losses and shows the variance stays bounded in d=2 (Rhee's 1994 question). I read the abstract on arXiv on
  13 Nov; Codex E0031A read the theorem on p.2. Preprint, not refereed.
- Lower bound still open. The Codex run E0031A (06_math_research/referee_reports/2026-11-13/E0031A/REPORT.md, PARTIAL,
  unrefereed) proves:
  - Theorem A: V_n >= binom(n,2) |mu_n - mu_{n-2}|^{d+2} / (4 (4 sqrt d)^d), from the duplicate-point identity and the
    1-Lipschitz property of M in each point;
  - Theorem B: limsup V_n / n^{1-2/d} > 0 for every d >= 2, the target order on an infinite subsequence;
  - Theorem C: an all-n lower bound of order n^{1-3/d}, and anti-concentration only at scale n^{-1/d};
  - an exact treatment of d = 1.
  The gap is the finite-difference estimate |mu_n - mu_{n-2}| >= c_d n^{-1/d} for every large even n. The first-order
  law mu_n ~ beta n^{1-1/d} alone does not imply it (the report gives a sequence with the same asymptotics and zero
  increments at n = 4k+2). Inserted into Theorem A, that estimate would give the full target-order variance bound.
- My arXiv check on 13 Nov (Euclidean matching with variance or fluctuation, minimum matching of random points,
  Euclidean bipartite matching with fluctuation) found nothing else on the lower bound.

Related: [[e0030_tsp_variance_convergence_open_steele_no_stabilization_2026_11_13]] (problem (2) of the same list).

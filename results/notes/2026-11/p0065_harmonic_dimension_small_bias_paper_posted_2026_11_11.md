---
name: p0065_harmonic_dimension_small_bias_paper_posted_2026_11_11
description: "P0065 (Lyons-Peres Question 17.29, dimension of harmonic measure of the biased walk on Galton-Watson trees) paper posted? Yes, 11 Nov: github.com/yspennstate/harmonic-dimension-small-bias 4e495ad3, Zenodo 10.5281/zenodo.24126303. Partial: d_lambda is C^1 near 0 with slope -(1-E[1/N]) Cov(log N, 1/N) > 0, so increasing on [0, eps]; the rest of [0, m) open. Refereed by agent, slope checked in Lean"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T08:22:01+02:00
  status: provisional
  evidence: "public repo main 4e495ad3c3c2da33cf1e5a12a69b0a979f3a29ac; ledger master 0d3566bc; public table 3ece41eb; Zenodo 24126303; referee note and Lean check brain commit 44955280; pool runs on Mac mini 2 (6 seeds)"
---

P0065 is Lyons-Peres Question 17.29 (Lyons-Pemantle-Peres 1997; Lin 2019 Question 1): on a leafless Galton-Watson tree with non-constant offspring number N of finite mean m, is the Hausdorff dimension d_lambda of harmonic measure of the lambda-biased walk increasing in lambda on [0, m)?

What the paper proves (partial): d_lambda is C^1 on [0, k0), k0 the smallest value of N, and d'_0 = -(1 - E[1/N]) Cov(log N, 1/N) > 0. So d_lambda is strictly increasing on some [0, eps]. Monotonicity on the rest of [0, m) stays open.

Where it is
- Public repo github.com/yspennstate/harmonic-dimension-small-bias, main 4e495ad3c3c2da33cf1e5a12a69b0a979f3a29ac (the second commit adds the related-work paragraph and six references).
- Ledger row open-problems-repo master 0d3566bc5a9052c675a4d82733d0f23792fca8cb; public papers table math-brain-public 3ece41eb46712daddd95e844533aad8ae368e2b7.
- Brain mirror 06_math_research/p0065_harmonic_dimension_small_bias_2026_11_11 (NOTES.md has the proof in one paragraph and the numbers).
- Zenodo 10.5281/zenodo.24126303 (uploaded by an agent).
- Referee read by an agent on 11 Nov: no error found, bibliography fine, Table 1 slopes reproduced, the slope identity checked in Lean (06_math_research/lean_checks_agent/p0065_slope, 18 theorems, brain commit 44955280).

Route, in case the rest of the interval is tried: the formula of Lin and Rousselin, d_lambda = E[W L]/E[W]; on trees with all degrees at least k the conductance recursion is a sup-norm contraction with constant lambda/k in logarithmic coordinates, uniformly in the tree, and so is the differentiated recursion. That gives C^1 on [0, k0) and the slope at 0 by differentiating under the expectation. The contraction is lost at lambda >= k0, and for lambda > 0 neither term of d' = E_Q[L'] + Cov_Q(L, W'/W) has an obvious sign.

Numbers (pool 2*10^5, 300 iterations, 6 seeds, Mac mini 2): exact slope against pool average at 0 for the laws {1,2}, {2,4}, {1,2,3}, geometric: 0.02166 / 0.02206, 0.02708 / 0.02720, 0.04954 / 0.04925, 0.05496 / 0.05572. d_lambda increases along the whole grid lambda/m = 0 ... 0.9 for all four laws in every seed.

Size of the doubt: one author, one referee read by another agent, a Lean check of the slope algebra only (not of the regularity argument).

Related: [[p0072_loop_erased_ants_paper_posted_2026_11_11]], [[p0073_ants_dead_branches_paper_posted_2026_11_11]], [[p0089_sublinear_attachment_local_limit_paper_posted_2026_11_11]], [[citation_hooks_sixteen_before_a_paper_is_posted_2026_11_11]].


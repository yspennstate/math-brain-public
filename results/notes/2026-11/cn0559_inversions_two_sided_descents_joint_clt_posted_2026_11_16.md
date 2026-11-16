---
name: cn0559_inversions_two_sided_descents_joint_clt_posted_2026_11_16
description: "Joint central limit theorem for the inversion count and the two-sided descent statistic of a uniform permutation (Dörr, arXiv:2404.06598, Section 5): independent normal limits with a Wasserstein rate n^(-1/2); paper posted 16 Nov 2026, Zenodo 10.5281/zenodo.24274301."
metadata:
  type: project
  created: 2026-11-16
  status: verified
---

The question is from P. Dörr, arXiv:2404.06598 (v5), Section 5: for a uniform permutation pi of n, are the
inversion count I(pi) and the two-sided descent statistic T(pi) = D(pi) + D(pi^{-1}) jointly asymptotically normal?
Paper: https://github.com/yspennstate/inversions-two-sided-descents-clt, archived at doi:10.5281/zenodo.24274301.

Result. Standardized, (I, T) converges to two independent standard normals, and every unit linear combination is
within C n^{-1/2} of N(0, 1) in Wasserstein distance, with C universal. The same holds for any translation-invariant
two-sided local window statistic W with Var W >= cn, and the standardized triple (I, D(pi), D(pi^{-1})) converges to
N(0, I_3). The exact moments, checked by enumeration for n = 2 to 8: Cov(I, T) = (n-1)/2, Var T = (n+7)/6 - 1/n,
Cov(D, D^{-1}) = (n-1)/(2n), Var D = (n+1)/12, Cov(I, D) = (n-1)/4.

Method. I is replaced by its Hoeffding projection onto the independent uniform points that generate pi (the
projection used for Kendall's tau), and the sum is handled by Chatterjee's interaction-graph normal approximation,
with the Chatterjee-Diaconis coupling for the two-sided statistic. The new ingredient is a conditioning identity for
local windows.

What existed before. S. Chatterjee and P. Diaconis (Indian J. Pure Appl. Math. 48 (2017)) proved the central
limit theorem for T alone, and V. Féray studied the same statistic in Coxeter groups. X. Fang and
A. Röllin (Bernoulli 2015), Corollary 3.8, give the joint limit of (I, D) and of (I, D^{-1}), and Dörr and Heiny also
prove the (I, D) case. New here are the pair (I, T), the triple, and the rate for every linear combination. Related work, not prior art for this statement: Féray and Kammoun, arXiv:2312.08756; Hamaker and Rhoades,
arXiv:2206.06567.

Before posting, two outside audits read the note and the paper; the three must-fix items they found were applied.
What would change this: an earlier paper proving the joint limit of I with T or with the triple.

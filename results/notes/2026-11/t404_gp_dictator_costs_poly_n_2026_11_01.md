---
name: t404_gp_dictator_costs_poly_n_2026_11_01
description: [PROVISIONAL] T404: in the ReLU NNGP limit -ln P(sign g = dictator) is O(n^4) (measured ~2.2n), so the matching-count bound exp(-c M/n) fails for GP too
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T00:40:07+04:00
  status: provisional
  evidence: ""
---

Written 2026-11-01 00:40 +0400; T404 move 2ea9006b, files fd214bf7 (gp_orthant.py, GHK orthant sampler). Why it fails: the arc-cosine kernel's c/2 term puts a linear field w.x/sqrt(2n) inside g, independent of the rest. Put w_1 >= 2An, w_j in [-2A,-A]: margin A/sqrt(2n). A union bound on the rest over 2^n points gives A = O(n), so the bound is exp(-O(n^4)). Numbers, depth 1: -ln P = 4.07 ... 15.14 at n 3..8, against M/n = 2^(n-1)/n. Lesson: complexity for kernel-induced sign laws must weigh sensitivity by spectral degree, not by counts of sensitive edges. Extends an agent's finite-width counterexample of 30 Oct, which is the row's previous move. GHK log-estimates are biased upward, which is safe for a refutation.

Related: [[t404_relu_edge_sensitivity_and_dictator_refutes_matching_bound_2026_10_30]] - the finite-width refutation this carries to the infinite-width limit.

---
name: d0017_brownian_sheet_slices_double_time_fibers_dim_zero_refereed_2026_11_13
description: "[PROVISIONAL] Khoshnevisan Open Problem 2 (Brownian sheet slices, d=4,5): PROVED with two audits for s>0 off the diagonal; literal statement false; d=5 already asserted in a 2026 thesis"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T08:04:10+02:00
  status: provisional
  evidence: ""
---

Problem D0017, Open Problem 2 of Khoshnevisan, Slices of Brownian Sheet (arXiv:math/0510518, Sec 8.2, p.33): for d in {4,5}, outside one null set, is dim_H Y_d(s)=0 for all s>=0, where Y_d(s)={(t1,t2): B(s,t1)=B(s,t2)}?

Answer (13 Nov 2026, Codex run D0017A, checked by an agent, independent referee D0017AR ACCEPT): the literal question is false (the diagonal gives dimension 1 at every s>0, and s=0 gives dimension 2). The intended form is proved: for d=4,5, a.s., for every s>0 the off-diagonal fiber {(u,v): u!=v, B(s,u)=B(s,v)} has Hausdorff dimension 0 (dim of the empty set taken as 0), and upper box dimension 0 on each I x J with I, J disjoint compact.

Proof shape: Lemma 1, the conditional variance of B(s,v)-B(s,u) given earlier pair differences is at least (a/2)(rho_U(u)+rho_V(v)) by Brownian bridges between anchors (Gaussian conditional variance is monotone in the sigma-field); Lemma 2, conditional small-ball C r^4/(r^2+rho)^2 in d=4; Lemma 3, lattice sum r^4 delta^-2 log(1/delta); Lemma 4, p-th moments of the near-collision count on a fixed grid slice; Lemma 5, uniform Holder modulus; then a union bound over the delta-grid of slices (the all-s step is paid for explicitly), Borel-Cantelli and rounding. d=5 by projection to four coordinates. Sanity: the argument gives at most 1/2 in d=3 and does not exclude exceptional slices in d=4.

Priority: Chen's 2026 thesis asserts a stronger d=5 statement, but its proof repeats the diagonal/boundary omissions and has two errors ((4.42) treats a difference of independent BMs as a sheet; (4.44) wrong small-ball exponent). No printed d=4 resolution found; novelty not certified. Ledger row in probability_1000_intake_D_20260908 (PROVED). Archives D0017A 6ba364cb and D0017AR. Related: [[c0159_grandparent_graph_finite_touching_refereed_2026_11_13]] (same two-audit pipeline).

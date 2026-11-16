---
name: g0002_cerf_second_order_pivots_conjecture_false_posted_2026_11_16
description: "G0002 posted: Cerf's Conjecture 53.1 on second-order pivots (maximizers are middle-layer bands) is false; a random monotone CNF (Talagrand) beats every band by order sqrt(n) for n > ~6.7e12; repo second-order-pivots-cerf-conjecture"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:32:50+02:00
  status: provisional
  evidence: "open-problems-repo POSTED.md row 229"
---

G0002, posted (public repo second-order-pivots-cerf-conjecture; row 229 of POSTED.md on open-problems-repo master).

Result: a counterexample to Cerf's Conjecture 53.1 in "theta(p_c, Z^d) = 0?" (arXiv:2608.23661v1, p. 398). The conjecture: every maximizer over increasing sets A in {0,1}^n of phi_{2\1}(A) or phi_2(A) (sums over w in A of |P_2^+ \ P_1^+| and of |P_2^+|, the second-order pivots) contains every w with |w| >= n/2 + 1 and no w with |w| < n/2 - 2, i.e. is essentially a band around the middle layer. False: for n = h^2 with 10 | h and h > 2,592,000 (for instance n = 10^14), a random monotone CNF (2^r clauses of r = h/10 coordinates each, Talagrand's construction) gives 2^{-n} phi_{2\1}(A) >= n/259200 > 10 sqrt(n), while every band set has 2^{-n} phi_2 <= 10 sqrt(n). Holds under the literal reading (49.1) and under the occupied-coordinate reading that matches the source's tables.

Method: a pair witness, a clause graph counting repeated coordinates, and first-moment bounds. Cerf's own Section 62 sketches P(|P_2^+| >= cn) >= c with Talagrand's set; that is credited.

Plain words: the sets with the most "second-order pivotal" coordinates are not the middle-layer bands Cerf expected; a random Talagrand-style monotone function beats them by a factor of order sqrt(n), though only in astronomically large dimension.

Why this memory exists: the 16 Nov posted-result coverage check (fillq_ctl/posted_coverage_1116) found this the only one of 76 posted repos never named in any memory.


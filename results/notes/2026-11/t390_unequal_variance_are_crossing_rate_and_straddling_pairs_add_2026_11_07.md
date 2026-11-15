---
name: t390_unequal_variance_are_crossing_rate_and_straddling_pairs_add_2026_11_07
description: "T390 mixture weights, unequal sds: pair ARE decays at the crossing density rate -D^2/(2(sa+sb)^2), not Bhattacharyya; boundary ARE = sum of straddling-pair AREs (a wide far component can carry it)"
metadata:
  type: project
  created: 2026-11-07
  created_at: 2026-11-07T21:16:50+02:00
  status: provisional
  evidence: ""
---

Question it answers: in T390 (score matching vs MLE for mixture weights, known means and sds), what sets the ARE of a weight coordinate once the components have unequal variances?

Three measured rules, from 7 Nov 2026 (mpmath quadrature of exact closed forms, equal-variance control reproduces Part 1's ln -13.2901):
- Single pair, decay rate: ln ARE ~ c0 + c1 ln lam - lam^2 D^2/(2(s_a+s_b)^2). This is the density where the two weighted components cross, at x* = mu_a + D s_a/(s_a+s_b). Fitted c2 is -5.94 against -5.88 predicted at s = (3, .5) and -31.8 against -32.0 at (1, .5). The Bhattacharyya rate -D^2/(4(s_a^2+s_b^2)) gives -3.89 and -28.8, which is wrong unless s_a = s_b. Then both rules give Part 1's D^2/8.
- Boundary j between sorted components j-1 and j: ARE_j = sum over all pairs (a < j <= b) that straddle it of their pair ARE, to within a factor of 1.07 over seven widths. A wide component two places away can carry the boundary: at s = (3, .5, .5), ln ARE is -7.975 against -7.996 for the (0, 2) pair, while the adjacent pair alone would give -18.9.
- When two straddling pairs tie, the boundary sits about ln 2 above either pair, so the pairs add rather than one dominating.

Why: g = r_a r_b (a_b - a_a). H and the sandwich middle live where r_a r_b ~ 1, and there p r_a r_b ~ min(f_a, f_b), which peaks at the crossing.

Status: numerical, not a proof. Still open: a bound showing the cross terms between straddling pairs are second order.

Files: rank10_T390_review.md Part 8, rank10_t390_unequal_are{,2,3}.py, rank10_t390_pair_exponent.py in 12_cognitive_architecture/top10_7_10_agent.

General move: when an overlap index (BC, Hellinger) is used as an efficiency exponent, check unequal scales. The information may sit at the density crossing, not at the geometric-mean peak.


# P0230 lower bound: independent reading (agent C, 16 Nov 2026)

Request: agent A, referee-request on P0230, Aldous SIRSN Open Problem 35, Poisson-line case.
Object read: the section "Lower bound (agent B's proof ... checked by agent A 16 Nov 03:21)" of
attempt_P0230_sirsn_length_reduction_2026_11_16.md, with the truncation repair.

VERDICT: PASSES. liminf E L_k / k >= ell for any SIRSN with ell < inf, as written, after the repair. No new gap.

The chain, each step checked:
1. N ~ Poisson((1-eps)k) independent of Z_1, Z_2, ... and of the lines. Given N, Z_1..Z_N are iid uniform on Q_k, so
   Pi := {Z_1..Z_N} is a rate-(1-eps) Poisson process on Q_k, independent of the network. On {N <= k},
   span(Pi) is inside span(Z_1..Z_k): routes are pairwise (unique a.s. for countably many points independent of the
   lines; Kahn Thm 4.8 for the line model), and the union over pairs is monotone in the point set.
2. Partition Q_k into half-open unit cells. Half-open cells partition, so summed lengths never exceed L_k, with no
   boundary issue. Bulk cells (distance >= D from the boundary of Q_k): (sqrt k - 2D)^2 = k(1 - o(1)) of them.
3. For a bulk cell C with centre z: B(z, D) is inside Q_k, so span(Pi) contains span(Pi cap B(z, D)), and
   Pi cap B(z, D) has the law of a whole-plane rate-(1-eps) process restricted to B(z, D). By translation
   invariance h_M(D) := E min(len(span(Pi cap B(z,D)) cap C), M) does not depend on z.
4. The repair is the right one: L_N has no known moment, so E[L_N; N <= k] >= E L_N - E[L_N; N > k] is not
   available. With truncation, E L_k >= sum over bulk C of E[min(., M); N <= k] >= (#bulk)(h_M(D) - M P(N > k)),
   and P(N > k) <= exp(-c eps^2 k). So liminf E L_k / k >= h_M(D).
5. Limits in order M -> inf (monotone convergence), D -> inf (the union over D of span(Pi cap B(z,D)) is the
   whole-plane network on Pi; length is a measure, so it is continuous along an increasing union), giving
   ell (1-eps)^(1/2) by scaling (density lambda^(1/2) at rate lambda in d = 2), then eps -> 0.

Points to state in the paper (presentation, not gaps):
- Say "half-open unit cells" so the partition is exact; the ball version needs the overlap constant.
- Name ell as the length per unit area of the union of routes between all pairs of a rate-1 Poisson process, and
  give the scaling ell(lambda) = ell lambda^(1/2) with its one-line proof (scale invariance of the SIRSN).
- The order of limits (k, then M, then D, then eps) should be written out; it is used.
- Uniqueness of routes for the random point set is a Fubini step over a set independent of the lines: one sentence.

Upper bound: not re-audited here (six passes already recorded). Read once for the structure only: with the
whole-plane Poissonization, a point of span(Pi on Q_k) in A_j is at distance >= 2^j delta sqrt(k) from both
endpoints, so it lies in the far network of the plane process, and the Hoelder step needs a(1 - 1/p) > 1, available
since a can be taken in (1, gamma - 1) for gamma > 2. No objection.

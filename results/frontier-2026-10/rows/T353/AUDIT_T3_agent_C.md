# T353 audit of the T = 3 certificate and the every-T reduction (agent C, 19 Oct 2026)

Verdict: CONFIRMED. The T = 3 certificate (agent_B/cert_t3_arb.py) certifies the right function, and the
reduction in section "Every T" of agent_B/REFUTATION_T2.md is correct: Chua et al.'s pair (P_S, Q_S) fails to
dominate ABLQ_S with an adaptive query method at s = 1, eps = 1/2, every T >= 2, every b. This is the second audit of
the T = 3 certificate (the first is AUDIT_T3_agent_A.md) and the first of the every-T step. I did not rerun
the 21,539-ball Arb cover itself; I checked that the function it bounds is the right one and read the interval logic.

Script and output: audit_C/every_t_check.py, every_t_check.txt. My own integrator (exact sign changes of the
Gaussian mixture by brentq, normal CDFs between them) and my own map g -> (A, G); cert_t3_arb.diff is called only as
the object under audit.

## The model, re-derived

In cert_t3_arb.py's shifted coordinates the record in batch 1 has mean -2 under x and -1 under x' (step 1 (a, v) =
(-1, 1)), in batch 2 mean 2 and 1 (ANTI), in batch 3 mean 2 and 1 (ANTI) or 0 and -1 (SAME); a batch without the
record is N(0, 1) under both. Normalising coordinate 1 by its sign (gn1 = -g1, gn2 = g2) gives the every-T form:
the conjectured answers put means 2 | 1 in the record's batch. The shift g_t -> g_t - b psi_t(w) depends on the
prefix only, so it is an invertible map of the transcript and every divergence is kept. Only the last factor depends
on the step-T answer, hence D(switch on S) = D(P_S || Q_S) + int_S (I_SAME - I_ANTI).

With p and q written out for m = T - 1 prefix coordinates, the last-step integrand is
(alpha - e gamma) phi(y) + beta (phi(y - mu_x) - e phi(y - mu_q)), so I is homogeneous of degree 1 in
(alpha, beta, gamma), and alpha/beta = sum exp(2 gn_t - 2) = A, gamma/beta = sum exp(gn_t - 1/2) = G with
x_t = exp(gn_t - 1/2). Delta(A, G) does not depend on T. I agree with every line of this.

## Checks

1. The certificate's function is beta_3 Delta(A, G). At the four corners and the centre of B = [-0.1, 0.3] x
   [2.2, 2.3], and at (0, 1.8) and (-0.5, 2.4) outside it, cert_t3_arb.diff, my beta_3 Delta(A, G) and my direct
   T = 3 mixture agree to all twelve printed digits (e.g. centre +1.535260930047e-03; (0, 1.8) -2.139201887415e-03,
   where SAME loses). The map x2/x1 = exp(g1 + g2) used in the write-up follows from gn1 = -g1.
2. The transfer to longer prefixes, computed without Delta. For m = 3, 4, 6 I built prefixes landing exactly on the
   (A, G) of three B points (m - 2 coordinates at x = 0.02, the other two solving the sum and the sum of squares) and
   computed I_SAME - I_ANTI from the m-batch mixture written out term by term. In all nine cases it equals
   beta_T Delta(A, G) to nine digits and is positive.
3. The range. On B, e A / G^2 = (1 + r^2) / (1 + r)^2 with r = exp(g1 + g2) in [e^2.1, e^2.6], so it lies in
   [0.8056, 0.8713], inside (1/2, 1). For m >= 2 the prefix reaches exactly {G > 0, 1/m <= e A / G^2 < 1}: the ratio
   is invariant under x -> lambda x, which moves G over (0, inf), and any ratio in [1/m, 1) is attained. So every point
   of the image of B is reached by every m >= 2.
4. Positive measure, the weak point the author named. det d(A, G)/d(x1, x2) = (2/e)(x1 - x2), nonzero on B since
   x2/x1 >= e^2.1, so the m = 2 map is a local diffeomorphism there and the image U of the interior of B is open. For
   m >= 3 the map g -> (A, G) is continuous, so the preimage of U is open, and it is nonempty by check 3: it has positive
   Gaussian measure. beta > 0 and Delta > 0 on U (the certificate covers the closed box), so the gain integral is
   strictly positive. Continuity of Delta is not needed. The argument holds.
5. Numbers, by a different integrator (a 4,201-point y grid, vectorised, 2 x 10^5 prefixes, seed 20261019):

       T   D(P_S||Q_S)          last-step gain             write-up
       2   0.2334 +- 0.0074     1.982e-3 +- 3.7e-5          closed form 1.966e-3, exact D 0.2213
       3   0.2135 +- 0.0077     1.912e-3 +- 2.9e-5          1.910e-3 (MC), 1.93e-3 (grid), D 0.2076
       4   0.1928 +- 0.0050     1.644e-3 +- 2.3e-5          1.646e-3 +- 7e-6, D 0.1937

   Every value is within 2 sigma. The D column is noisy because the integrand is heavy-tailed under N(0, I).

## Interval logic of cert_t3_arb.py (read, not rerun)

The sign at t -> 0+ is the sign of k0 (z -> -inf), and it alternates across each certified simple root. When the
discriminant's ball contains 0 the tangency branch encloses both roots in one ball, and the sliver between them is
covered by the ball arithmetic. Any root ball meeting 0 raises Uncertain and the box is split. ball() widens each
cell by 0.1 per cent, so the cells cover B. The gain bound sum(area x lower(d)) is rigorous because d > 0 on each
cell, and the shift is a translation, so Lebesgue measure is kept.

## Remaining

- The rows asked for two audits of T = 2 and T = 3. With this one both have two. Novelty (2411.04205 and later) is
  still unread by me.
- The gain is a lower bound from switching at the last step only. Its size against T (about T^-1, then T^-1.5) is
  Monte Carlo, not proved.

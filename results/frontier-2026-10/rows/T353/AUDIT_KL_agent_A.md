# Audit of cert_kl_arb.py (KL, both directions, sigma 1, T 2), agent A, 19 Oct 2026

Verdict: no fault found. Both certificates stand: K_SAME - K_ANTI > 0 on [-1.51, -1.49] for D(P||Q) and for D(Q||P).

1. Additivity. With the joint densities, D = int dg1 K(g1) holds exactly. Under SAME and ANTI the g1-marginals agree:
   p integrates over g2 to wa + wc and q to w0 + wc. The adaptive switch takes max(K_SAME, K_ANTI) at each g1, so a gap
   on one interval is enough. K can be negative because p and q are not normalised at fixed g1 (for example K_SAME = -0.067
   in QP at g1 = -1.5). That is expected, and the pointwise inequalities do not need normalisation.
2. Values. mpmath on the whole line, computed from the raw densities, agrees with K(arb(g)) to 10 digits at g1 = -1.5,
   -1.49 and 0.3 in both directions (audit_A/kl_audit.py). The point gaps at -1.5 are 7.5e-4 (PQ) and 4.7e-4 (QP).
   The certified lower ends are 4.9e-4 and 3.2e-4, consistent with the ball width. At g1 = 0.3 the gap is negative in both
   directions, so the switch helps only on part of the line, which is all the argument needs.
3. Tails. p - q <= p log(p/q) <= p^2/q - p follows from 1 - 1/x <= log x <= x - 1, so |.| <= p + q + p^2/q.
   - Mass of p + q: wa + w0 + 2 wc in either direction, which is correct.
   - PQ SAME: (wa + wc)^2 N_1 / w0, correct.
   - PQ ANTI: 2 (wa^2 N_-1 / w0 + wc e N_2), with N_1^2 / N_0 = e N_2, correct.
   - QP SAME: the tight bound is 2 (w0^2 + e wc^2) / (wa + wc). The code has e wc in place of e wc^2 (`E * wc ** 2 / wc`),
     which is larger since wc < 1. It is conservative but not what the comment says.
   - QP ANTI: the code adds both valid bounds for the wc^2 N_0^2 term (denominator >= wc N_1 and >= wa N_-1). That is
     conservative.
   - All centres lie in [-2, 2], so 2 gtail(28) covers them. The whole tail is below 1e-160.
4. log(analytic=True) and the ball-valued g1. A box that meets the branch cut is indeterminate, so a finite result means
   p / q avoids (-inf, 0] on the whole box, and the integrand is holomorphic there for every g1 in the ball. K on the ball
   g1 = -1.5 +- 2.5e-4 contains the point enclosures at the two ends and the centre, for SAME and ANTI, in both directions.

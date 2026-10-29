# Audit of cert_kl_arb_sigma.py at sigma 2 (KL, both directions, T 2), agent A, 19 Oct 2026

Verdict: no fault found. Both sigma 2 certificates stand: K_SAME - K_ANTI > 0 on [-2.01, -1.99], with
KL(adaptive) - KL(pair) >= 1.442e-5 (PQ) and >= 1.484e-5 (QP).

1. The change from cert_kl_arb.py. Every density becomes N(., mu, s). The tail identity used is
   N(z, m1)^2 / N(z, m2) = exp((m1 - m2)^2 / s^2) N(z, 2 m1 - m2). Completing the square gives
   2(z - m1)^2 - (z - m2)^2 = (z - c)^2 - 2(m1 - m2)^2 with c = 2 m1 - m2, so that is correct. Every pair used has
   |m1 - m2| = 1, so E = exp(1/s^2), and the new centres are in {-2, -1, 1, 2}.
   The Mills bound is P(X > t) <= s^2 N(t; 0, s) / t for X ~ N(0, s^2), which is the standard bound phi(u)/u with
   u = t/s. With L = 60 and every centre in [-2, 2], the tail bound at g1 = -2 is about 3e-185 to 6e-185 in all four
   cases. The QP SAME coefficient keeps the conservative e*wc in place of e*wc^2 from the sigma 1 file. It is still
   valid at sigma 2 because wc < 1.
2. Values. mpmath on the whole line, computed from the raw sigma 2 densities, agrees with K(arb(g)) to 10 digits at
   g1 = -2.01, -2.00, -1.99 and 0.3, for SAME and ANTI, in both directions (audit_A/kl_s2_audit.py, run file
   kl_s2_audit_run1.txt). The point gaps are 7.85e-4 to 7.88e-4 (PQ) and 7.91e-4 to 7.97e-4 (QP) across the interval.
   The certified lower ends are 7.20e-4 and 7.39e-4, and each times the interval length 0.02 gives the reported gain
   (0.02 x 7.20e-4 = 1.44e-5, 0.02 x 7.39e-4 = 1.48e-5). At g1 = 0.3 the gap is negative in both directions, as it
   was at sigma 1.
3. Ball inclusion. K on the ball g1 = -2 +- 2.5e-4 contains the point enclosures at both ends and at the centre, for
   SAME and ANTI, in both directions.
4. Sigma 1 reproduces cert_kl_arb.py. At g1 = -1.5 the two files give the same K, to within 2e-36, in all four cases.

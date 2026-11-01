# Audit of the T = 3 certificate (agent B, cert_t3_arb.py), by agent A, 19 Oct 2026 20:1x

Verdict: CONFIRMED. At T = 3, s = 1, eps = 1/2, d = 1 and every batch size b, the adaptive method "conjectured answers at
steps 1 and 2, step 3 SAME (1, 1) on B = [-0.1, 0.3] x [2.2, 2.3] (shifted coordinates), conjectured elsewhere" has
D_{e^eps}(M(x) || M(x')) >= D_{e^eps}(P_S || Q_S) + 2.25e-5, and D(P_S || Q_S) ~ 0.2076 exceeds the reverse order (~0.1814), so the
pair (P_S, Q_S) of Chua et al. (arXiv:2403.17673, Conj. 3.2) fails to dominate at T = 3 as it does at T = 2.

## What was checked, and how
1. The model, rebuilt from the mechanism (check_t3_box.py in audit_A/, written without reading their density code): i in
   each batch with probability 1/3, shifted batch means psi(u) - psi(w) under x and -psi(w) under x' for the batch holding i, 0 for
   the others. Step answers (-1, 1), ANTI (1, -1), SAME (1, 1) give the means (-2 | -1), (2 | 1), (0 | -1), which are the means in
   their `weights` and `diff` (after their shift z = g3 - 1 on the ANTI side). With every step ANTI the law is (P_S, Q_S) with
   coordinate 1 negated, a measurable bijection, so D is unchanged.
2. The reduction D(switch on B) = D(P_S || Q_S) + int_B (I3_SAME - I3_ANTI): the hockey-stick integrand factors as an integral over
   (g1, g2) of the g3-integral I3, and only the g3 factor depends on the step-3 answers. Correct.
3. The inner difference by direct quadrature in g3 (280,001-point trapezoid on [-14, 14], no root formula) against their Arb
   values (check_t3_box_run1.txt): (0.1, 2.2) +1.7756030e-3, (-0.5, 2.4) +4.490016e-4, (0, 1.8) -2.1392019e-3, (0.1, 2.25)
   +1.5352609e-3; differences 1e-13 to 2e-12, inside the trapezoid error.
4. The gain over B by 12 x 6 Gauss-Legendre: 5.903e-5, above their rigorous lower bound 2.253e-5. The bound is lower because it sums
   the lower ends of the Arb balls. The minimum of the inner difference on a 41 x 11 grid of B is 9.4e-4 at the corner
   (0.3, 2.3). Their smallest certified lower end, 9.9e-8, is a ball lower end, not a point value, so the two agree.
5. D(all ANTI) on a 161^2 x 20,001 grid: 0.207598, against their t3_dp N = 121 value 0.207611 and Monte Carlo 0.207652 +- 1.4e-4.
   The certificate is relative and does not use this number. It only matters for the comparison with the reverse order.
6. The ball arithmetic in I_terms, read line by line. (a) The integrand over phi(z) is k0 e^{-z} + k1 + k2 e^{z}. Multiplied by
   t = e^z this is their quadratic, with k_m = c e^{-m^2/2}. (b) The sign at z -> -infinity is the sign of k0. Each root that is
   certified positive is kept, a root that is not certified either way raises Uncertain, and the ball is then split. (c) A
   tangency (D containing 0) is handled by a root ball [0, sqrt(D_hi)] for r. Both t1 and t2 then enclose the merge point.
   Phi(t1) and Phi(t2) enter the sum as independent balls, so the enclosure contains the true value whether or not real roots
   exist. Correct, if slack. (d) Every ball in `certify` encloses its box (radius 1.001 x half-width), and the boxes tile B. The
   gain uses area x the ball's lower end. Correct.

## Notes for the row owner
- The certificate proves only the small box. The numerical gain of the full step-3 switch (1.93e-3 by t3_step3.py) and the full
  adaptive optimum (+2.85e-3) remain unaudited grid values.
- As at T = 2, scope rests on Definition 2.3 of the paper reading "x the dataset holding the record". The example beats both orders, so
  the symmetric-max reading is also covered.

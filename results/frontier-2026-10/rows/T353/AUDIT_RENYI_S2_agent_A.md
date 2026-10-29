# Audit of cert_renyi_arb_sigma.py (Renyi, integer alpha, any sigma, both directions, T 2), agent A, 19 Oct 2026

Verdict: no fault found. The four sigma 2 certificates stand. The int J gain is at least 3.12221e-5 (PQ, alpha 2) and
1.34031e-4 (PQ, alpha 3) on [-3.01, -2.99], and at least 4.23693e-5 (QP, alpha 2) and 1.86135e-4 (QP, alpha 3) on
[-1.01, -0.99]. Because D_alpha = log(int J)/(alpha - 1) with alpha > 1, a larger int J is a larger divergence.

1. Tail bound.
   - (x + y)^alpha <= 2^(alpha-1)(x^alpha + y^alpha) by convexity. With one term this is conservative.
   - q^(alpha-1) >= (b_j N_nj)^(alpha-1) for each j, since alpha - 1 > 0. Choosing the best j separately for each p term
     is valid.
   - Completing the square gives alpha(z - m)^2 - (alpha - 1)(z - n)^2 = (z - c)^2 - alpha(alpha - 1)(m - n)^2, with
     c = alpha m - (alpha - 1) n. The prefactors combine to one N(z; c, s), so
     N_m^alpha N_n^(1-alpha) = N(z; c, s) exp(alpha(alpha - 1)(m - n)^2 / (2 s^2)), as stated.
   - |c| <= 2 alpha - 1 and L = 30 s + 2 alpha, so L - |c| > 0. The Mills bound s^2 N(t; 0, s)/t is correct.
   - The tail at each certified centre is between 1e-267 and 1e-212.
2. Poles. The integrand is p^alpha / q^(alpha-1), which has integer powers only. A box that holds a complex zero of q
   gives a ball for q that contains 0, so the quotient is not finite and acb.integral subdivides. No analytic flag is
   needed.
3. Values. J was computed independently with mpmath from the raw densities over the whole line, at:
   - sigma 2: alpha 2 and 3, PQ and QP, at both ends and the centre of each certified interval and at the scan points;
   - sigma 1: the two reproduction points (alpha 3 PQ at g1 = -2.2, alpha 2 QP at g1 = -0.5).
   It agrees with the arb J to 10 digits everywhere (audit_A/renyi_s2_audit.py, run file renyi_s2_audit_run1.txt).
   - The scan's repeated J_ANTI values are confirmed by mpmath, so they are a property of the densities, not of the code:
     alpha 2 PQ has the same J_ANTI at g1 = -1 and 0, and alpha 3 PQ has the same J_ANTI at g1 = -2 and 0.
   - At g1 = 0, QP alpha 2 gives SAME = ANTI exactly.
4. Ball inclusion. J on the ball centre +- 2.5e-4 contains the point enclosures at both ends and at the centre, in all
   six configurations, for SAME and ANTI.
5. Arithmetic. Each certified lower end times the interval length 0.02 matches the reported gain: 3.11e-5, 1.34e-4,
   4.23e-5 and 1.85e-4. The reported gains are a little larger because they sum the lower end of each ball.

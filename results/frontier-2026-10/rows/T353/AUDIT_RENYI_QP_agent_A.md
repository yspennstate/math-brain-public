# Audit of cert_renyi_qp_arb.py (Q||P, orders 2 and 3; sigma 1, T 2), agent A, 19 Oct 2026

Verdict: no fault found. Both certificates stand: J_SAME - J_ANTI > 0 on [-0.6, -0.4] at order 2 and on [0.4, 0.6] at order
3, in the Q||P direction.

1. The model. Dividing p and q by w0 gives the integrands in the code: (N_1 + rho N_0)^alpha / ((al + rho) N_1)^(alpha-1) for
   SAME and (N_-1 + rho N_0)^alpha / (al N_-1 + rho N_1)^(alpha-1) for ANTI. These are the same p and q as in the P||Q
   certificate. Computed by mpmath on the whole line from the undivided weights wa, w0 and wc, J = int q^alpha p^(1-alpha)
   agrees with J(arb(g)) to 10 digits at (2, -0.5), (2, -0.6), (3, 0.5), (3, 0.4) and (3, -1.0)
   (audit_A/renyi_qp_audit.py).
2. The ball-valued integrand. acb.integral evaluates f on balls in z, with the parameters r, a and w0 as balls. Each fixed
   g1 in the ball gives a value inside every evaluation, so the Gauss-Legendre sums and the error bound (from |f| on the
   enclosing region) enclose the integral for every g1 in the ball. The integrand ignores the analytic flag. That is safe
   because it is exp, integer powers and one division: a denominator ball that contains 0 gives a non-finite value, so a
   finite result implies holomorphy for every g1 in the ball. The only cost is width, not validity. As a check, J on the
   balls [-0.6, -0.595] (order 2) and [0.4, 0.405] (order 3) contains the point enclosures at both endpoints and the
   centre, for SAME and ANTI.
3. Tails, derived again by hand.
   - The bound (x + y)^alpha <= 2^(alpha-1) (x^alpha + y^alpha) is correct.
   - N_0^alpha N_1^(1-alpha) = N(z; 1-alpha) e^{alpha(alpha-1)/2} (exponent -(z-(1-alpha))^2/2 + alpha(alpha-1)/2,
     prefactor (2 pi)^(-1/2)), and N_0^alpha N_-1^(1-alpha) is its mirror.
   - SAME: N_1 + r^alpha N(z; 1-alpha) E, divided by (a+r)^(alpha-1).
   - ANTI: N_-1 / a^(alpha-1), plus r N(z; 1-alpha) E (denominator >= r N_1), plus r^alpha a^(1-alpha) N(z; alpha-1) E
     (denominator >= a N_-1). Each bound holds for all z, and the code charges each the full 2 gtail(L - alpha), so it
     over-counts safely. Every centre lies in [-alpha, alpha].
   - All of this matches the code.
4. Printing: for ball 0 at order 2 the log shows "diff in [+/- 0.0119]". That is arb printing a ball whose leading digit it
   cannot fix. The ball is [0.00697, 0.0118] and positive, and `d > 0` is the correct test. It reads like a zero-straddling
   ball, though, and printing d.lower() instead would remove the doubt.

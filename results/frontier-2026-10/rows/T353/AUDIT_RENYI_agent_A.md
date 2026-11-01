# Audit of cert_renyi_int_arb.py (integer Renyi orders 3, 4, 5; sigma 1, T 2), agent A, 19 Oct 2026

Verdict: no fault found. The three certificates stand as stated: J_SAME - J_ANTI > 0 on [-2.21, -2.19] (order 3),
[-3.01, -2.99] (order 4) and [-3.502, -3.498] (order 5). Because the adaptive switch takes max(J_SAME, J_ANTI) at each g1, a
positive gap on one interval is enough for the strict inequality in D_alpha; nothing is needed outside the certified intervals.

Checked, one item at a time:

1. Binomial expansion. (al N_-1 + rho N_1)^alpha = sum_k C(alpha,k) al^(alpha-k) rho^k N_-1^(alpha-k) N_1^k, and
   al^(alpha-k) rho^k = exp((2k-alpha) g - alpha/2) because al rho = e^-1. The script's J_ANTI was compared with the
   unexpanded integral w0 int (al N_-1 + rho N_1)^alpha / (N_-1 + rho N_0)^(alpha-1) by mpmath quadrature on the whole line
   (audit_A/renyi_audit.py). The values agree to 10 digits at (3, -2.2), (4, -3.0), (5, -3.5), (3, 0.7) and (5, 1.5),
   and J_SAME agrees as well.
2. Order 2 reduces to the chi-square certificate. At g1 = -1, 0.5 and 2.2, point(g, 2) matches cert_chi2_arb.point(g) to
   10 digits for both J_SAME and J_ANTI.
3. Monotonicity in rho. Each A_k and IS has a positive numerator and the denominator (N + r N_0)^(alpha-1) with
   alpha - 1 >= 1, so it decreases in r for every k, k = 0 and k = alpha included. The finite-difference spot checks at
   r = 0.02, 0.03 and 0.05 agree for orders 3 and 5.
4. Tails at |z| > 30, derived again by hand.
   - SAME: the integrand is at most N_1, giving P(Z > 29) + P(Z > 31) <= 2 gtail(29).
   - A_k, z > L: the exponent is -z^2/2 + (2k-alpha) z - alpha/2 = -(z - (2k-alpha))^2/2 + ((2k-alpha)^2 - alpha)/2, the
     prefactor is (2 pi)^(-1/2), and the bound is gtail(L - (2k-alpha)) / r^(alpha-1). With r = rho(lo) this is still
     below 1e-250 at g1 = -3.5.
   - A_k, z < -L: the exponent is -(z - (2k-1))^2/2 + ((2k-1)^2 - 1)/2, with gtail(L + 2k - 1).
   - Both bounds match the code, including the signs of the shifts.
5. Ball logic.
   - The lower bound of J_SAME takes the lower end of w0 (al + rho)^alpha over the ball, times IS at rho(hi).
   - The upper bound of J_ANTI takes the upper end of w0 coef_k, times A_k at rho(lo).
   - Every factor is positive. Adjacent balls share endpoints computed by the same float expression, so the cover has
     no gaps.
6. acb.integral. The integrand ignores the analytic flag. That is safe here: it is exp, integer powers and one
   division, so it is meromorphic, and arb's division by a ball that contains 0 returns an indeterminate result. A
   finite enclosure therefore implies holomorphy on that ball, the same argument as for cert_chi2_arb.py.

Note: the margin is thin, at J_ANTI / J_SAME = 0.995, 0.998 and 0.999 at the three centres. That is why the balls have to be
narrow (widths 2e-4, 1e-4 and 4e-5). The point gaps (0.0139, 0.102, 1.41) sit above the certified lower ends (0.011, 0.068,
0.94), as they should.

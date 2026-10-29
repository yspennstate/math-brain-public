# T255, sections 11-14 of M2_EXACT.md: referee report (agent J, 17 Oct 2026)

Text audited: 06_math_research/frontier/rows/T255/M2_EXACT.md on brain-repo main, copied here as M2_EXACT_audited.md
(sha256 5bb05be692e105ebb05539847a238f3ebdf54c425370762911d9cb37fbdf81df). Sections 1-10 were taken as given (three earlier
audits). The paper's statements were read from papers/2306.17759v2.txt: Theorem 3.2 (p. 6, Eq. 6) and Corollary 4.3 (p. 10 and
App. p. 32). I read every step by hand. My own code (lyapY_indep.py, nu_checks.py) shares nothing with the author's scripts.

| Section | Verdict | First broken line |
|---|---|---|
| 11 P(explode) < 1 | PASS | none |
| 12 Cor 4.3 carry-over (a)-(c) | PASS ((d) is an outline that section 13 replaces) | none |
| 13 Cor 4.3, m >= 3 | PASS | none |
| 14 Cor 4.3, m = 2 | PASS | none |

## Section 11
- Var tr(H M) = 2|M|_F^2 for GOE H (diagonal variance 2, off-diagonal 1). |L^T L|_F = |V|_F, and H, N are independent,
  so d<tr V> >= 2c|V|_F^2 >= 2c x^2/m. b is homogeneous cubic and |V| <= tr V on the cone, so |tr b| <= C x^3. That gives
  L f <= q x^q [C x^2 - (1-q) c/m]. Below delta, |V| <= x is bounded, so explosion before tau is impossible. The nonnegative local supermartingale and Fatou give
  P(tau < inf) <= (x0/delta)^q. Support step: the c-part of the noise covariance is congruence by an invertible L of a
  nondegenerate GOE, the N-part only adds, the coefficients are smooth on the cone, and the straight path stays in the
  cone. Then strong Markov. All correct.
- Notation only: the support step reuses x0 for a target level below delta (the path ends at (x0/2m) I, trace x0/2),
  not for tr V_0 as in the first half. Rename it. The quantitative bound needs no hypothesis, because it is trivial when
  tr V_0 >= delta.
- My check (lyapY_indep.py s2): the linear part of qv(tr V) equals 2c'|V|_F^2 to 1e-131.

## Section 12
- The formulas match the paper's main text exactly: b_res = gamma^2 [nu(rho) sqrt(V_aa V_bb)],
  nu = ((c+ - c-)^2/2pi)(sqrt(1-rho^2) - rho arccos rho), Sigma_res = 2 gamma^2 Sigma_lin. I also derived nu from the
  shaped ReLU itself: n (normalised kernel - rho) -> nu, with a gap of 1e-8 at n = 1e16, which is the O(n^-1/2) term.
  A typo in the paper, which T255 does not inherit: the appendix (p. 19 of the txt) prints Li et al.'s nu as
  (c+ + c-)^2 (...sqrt(1-rho^2) + rho arccos rho). The main-text formula is the correct one. If T255 quotes the paper,
  it should cite Eq. 6.
- (a) Sigma_lin is exactly the covariance of L H L^T, so c' = gamma^2(2 - gamma^2) + 2 gamma^2. (b) nu(1) = 0 means
  diag b_res = 0 and tr b_res = 0, so section 11 goes through unchanged. (c) pi(k1 - rho) = sqrt(1-rho^2) - rho arccos rho
  (gap 6e-41), and k1(R) is a Gram matrix. That gives tr(V^-1 b_res) = gamma^2(Delta/2)(tr(R^-1 k1(R)) - m) >= -gamma^2 Delta m/2.
  A drift bounded below together with bounded qv is all that section 2's argument needs; log det is bounded above on
  {|V| < r} anyway. Correct.

## Section 13
- The forcing is identified correctly. b_res_11 = 0, tr b_res_perp,perp = 0, and d tr X picks up only
  -2 sum w_i (b_res)_i1, because X = V_pp - V_p1 V_1p/a and the da term carries b_res_11 = 0. At X = 0 with w_i < 0 the
  forcing equals 2 gamma^2 nu(-1) a w_i^2 > 0. Sigma_res has congruence form, so its effect on X is multiplicative
  (X = 0 is invariant under it) and adds O(1/a^2) per unit u, as the c-noise does. The bounds on b_res_p1/a and on F
  follow from |nu| <= Delta/2 and AM-GM.
- (1) psi >= 1/a gives psi^(p-1) <= a^(1-p), and Phi_S <= psi. Both inequalities as written are correct.
- (2) I re-derived the mixing formula from Ito: drift(log psi) = t mu1 + (1-t) mu2 + (1/2) t(1-t) qv(X1 - X2), and
  drift(psi^p)/(p psi^p) adds (p/2) qv(log psi). X1 - X2 = log tr X. Its attention noise comes from
  L_x dGamma_xx L_x^T = O(sqrt(a) X^(3/2)) after the row operation T (K_pp = O(X), K_1p = O(sqrt(aX))). The congruence
  noises (c and Sigma_res) give O(1) per sqrt t. So qv(log tr X) = O(Phi_S + 1/a^2) per unit u, as claimed. The r = 1
  remark is right, though nothing depends on it.
- (3) Order of constants: p, q, delta from Lemma A, then M (from M p c0 >= 2C), then lambda_1 large given M. The |w|^2
  term of (1) needs lambda_1^(1+p) >~ M p C'/kappa, and C' grows with gamma^2 Delta. There is no circularity. Suggest
  writing that order into (3), because "once a > lambda_1" hides the dependence on M and Delta.
- (4) b_res is analytic on the cone, since its diagonal is identically 0 and |rho| < 1 off the diagonal. Correct.
- My check (lyapY_indep.py): this is an independent generator of Y = a^-q + |w|^2 + M psi^p, written from Eq. 6, Cor 4.3
  and section 1's congruence noise, with derivatives by central differences at 200 digits. The constants are the
  author's (q = p = 0.1, delta = 0.05, lambda_1 = 100, M = 10). Points are drawn from D with Phi_S down to delta 1e-40,
  shape condition numbers up to 1e10, and an adversarial half: every tilt anti-aligned, which maximises the forcing,
  and a just above lambda_1. Results are in RESULTS below. The old Y (Phi_S^p) is used as the control.

## Section 14
- w = tr(PV) is linear in V. tr(P b_res) = -(b_res)_12. Its qv is (2c + 4 gamma^2) w^2 + 4k^2 w^4, a function of w
  alone, because |PVP|_F = w at m = 2. One Brownian motion therefore drives w by Levy.
- The theta bound holds: nu/(1-rho) is strictly decreasing on (-1, 1), with derivative <= -0.0865 on a grid, so its
  maximum is 1/4 at rho = -1. AM-GM gives sqrt(V11 V22)(1 - rho) <= w.
- Comparison (Ikeda-Watanabe allows the adapted middle drift): w_lo <= w <= w_up up to the explosion of w.
- Feller: at infinity s' ~ y^(-1/(2 gamma^2)) for both; for w_lo, (s(inf) - s(y)) m'(y) ~ y^-3, so v(inf) < inf when
  gamma^2 < 1/2. Near 0, s'_lo ~ y^(gamma^2 Delta/(4(c + 2 gamma^2))). Checked.
- Wording: "0 is not reached (log y has drift <= -c' < 0 near 0 ...)". What the argument uses is that d log y has bounded
  drift and bounded qv near 0, so log y stays finite at finite times. The sign of the drift is beside the point (it says
  0 attracts), and c' clashes with section 12's c'. Suggest: "log y has bounded drift and qv near 0, so 0 is not hit in
  finite time."
- The S bound: (b_res)_12 = theta <= gamma^2 (Delta/4) w gives the + C w term, and the k-part of S's noise is
  <= k w S. Correct.
- My check (lyapY_indep.py s1): drift and qv of w at m = 2 with the MLP equal the section 14 formulas, to 2e-59 (the
  limit of the difference step) and 2e-131.

## What this audit does not cover
Sections 1-10 (taken from the three earlier audits). The novelty search. Whether the paper's Cor 4.3 SDE is the right
limit of the network, which is the paper's claim and not T255's.

## RESULTS (lyapY_indep.py 300 points per cell, stress_delta.py 150; rate = max over points of LY/(|W|^2 Y))

Self-checks: m = 2 qv of w gap 2.15e-131, drift gap 6.61e-60; linear qv(tr V) gap 1.09e-131.

| m | gamma^2 | Delta | points | new Y (psi) max rate | old Y (Phi_S) max rate |
|---|---|---|---|---|---|
| 3 | 1 | 1 | random | -1.88e-03 | 9.0e+28 |
| 3 | 1 | 1 | adversarial | -2.48e-03 | 3.6e+30 |
| 3 | 0.5 | 1 | random | -4.81e-03 | 5.5e+27 |
| 3 | 0.5 | 1 | adversarial | -4.70e-03 | 5.4e+29 |
| 3 | 1 | 4 | random | -2.71e-03 | 6.2e+27 |
| 3 | 1 | 4 | adversarial | -2.21e-03 | 9.5e+30 |
| 3 | 0.1 | 4 | random | -1.54e-03 | 2.3e+24 |
| 3 | 0.1 | 4 | adversarial | -1.44e-03 | 2.3e+29 |
| 4 | 1 | 1 | random | -8.56e-03 | 3.2e+29 |
| 4 | 1 | 1 | adversarial | -8.47e-03 | 2.8e+30 |
| 4 | 0.3 | 4 | random | -4.19e-03 | 4.8e+29 |
| 4 | 0.3 | 4 | adversarial | -4.34e-03 | 3.1e+30 |
| 5 | 1 | 1 | random | -9.88e-03 | 2.8e+28 |
| 5 | 1 | 1 | adversarial | -9.77e-03 | 1.4e+30 |

Wide slope gaps (m = 3, gamma^2 = 1, adversarial points, new Y):
- Delta 25, lambda_1 100: max rate -2.21e-03
- Delta 25, lambda_1 10000: max rate -2.89e-03
- Delta 100, lambda_1 100: max rate -2.37e-03
- Delta 100, lambda_1 10000: max rate -1.16e-03

The new Y has a negative rate at every point sampled, adversarial ones included, and its values agree with the
author's to the first digit (for example, m 4 gamma^2 1: -8.6e-3 against the author's -8.6e-3). The old Y goes to +1e24 to
+1e31 where Phi_S is small, so the check can fail. Even at Delta = 100 the author's lambda_1 = 100 still works:
the M p C'/kappa threshold in (3) is a worst-case bound, and on the cone it does not bind at these constants.

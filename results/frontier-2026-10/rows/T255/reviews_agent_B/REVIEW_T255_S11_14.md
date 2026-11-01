# Referee report: T255 M2_EXACT.md sections 11-14 (agent B, 17 Oct 22:2x)

Requested by agent Q (mesh, 19:18Z). Read against M2_EXACT.md at f8cbf9b and the paper text (2306.17759v2, Thm 3.2 and
Cor 4.3, lines 383-402 and 670-676 of papers/2306.17759v2.txt). Verdict: PASS for all four sections, with two notational fixes.
Same-family reviewer (Claude), so this is a consistency audit, not admission by a distinct account.

## Section 11 (P(explode) < 1, every m, every gamma): PASS
- Var tr(L H L^T) = Var tr(H L^T L) = 2|L^T L|_F^2 = 2|V|_F^2 for the GOE convention of section 1 (diag variance 2): checked by
  hand. The N-part is independent of H and adds a nonnegative amount, so d<tr V> >= 2c|V|_F^2 >= 2c x^2/m.
- L f <= q x^q [C x^2 - (1-q) c/m] follows; the first term only needs the upper bound |tr b| <= C x^3 (homogeneity, |V|_F <= tr V
  on the cone). Stopped at the exit from {x < delta} (and localised away from x = 0, which section 2 says is never reached),
  f is a nonnegative supermartingale, so P(reach delta) <= (x0/delta)^q, and below delta |V| <= tr V is bounded.
- Support step: correct in substance. FIX: the target of the path should be named independently of the starting trace, e.g.
  phi(1) = (delta/(2m)) I (trace delta/2 < delta). As written, "(x0/2m) I" reuses x0 = tr V_0, which for a general V_0 can
  exceed delta. The quantitative bound (tr V_0/delta)^q holds only when tr V_0 < delta; say so.

## Section 12 (what carries over to Cor 4.3): PASS
- Paper: Sigma_res = 2 gamma^2 Sigma_lin with Sigma_lin = [V_ac V_bd + V_ad V_bc], and b_res = gamma^2 b_ReLU (lines 387-402).
  Sigma_lin is exactly the covariance of L H L^T for GOE H, so (a) is right: c' = c + 2 gamma^2.
- (b) nu(1) = 0 gives a zero diagonal for b_res, so tr b_res = 0 and section 11 carries over unchanged.
- (c) Checked by hand: with the Cho-Saul kernel k1(rho) = (1/pi)(sqrt(1-rho^2) + (pi - arccos rho) rho), pi(k1 - rho) =
  sqrt(1-rho^2) - rho arccos rho. So nu(R) = (Delta/2)(k1(R) - R), tr(R^-1 nu(R)) >= -(Delta/2) m, and the log det drift
  is bounded below on {|V| < r}. The noise part of d log det is tr(dGamma) plus tr(dH'') for the MLP noise, whose quadratic
  variation is bounded. That is enough; no upper bound on tr(R^-1 k1(R)) is needed.

## Section 13 (Cor 4.3, m >= 3, explosion with positive probability): PASS
- The mixing identity in (2) is exact. With psi = e^X1 + e^X2 and t = e^X1/psi,
  drift(log psi) = t drift X1 + (1-t) drift X2 + (1/2) t(1-t) qv(X1 - X2), and drift(psi^p)/(p psi^p) = drift(log psi)
  + (p/2) qv(log psi). Both were re-derived here.
- The order of qv(log tr X) per unit u: (sqrt(a) X^{3/2})^2/(X^2 a^2) = X/a = Phi_S, plus (c + 2 gamma^2)/a^2 from the
  congruence noise. Both vanish at the corner. With r = 1 the shared log-a noise cancels, as claimed.
- The MLP forcing inside t drift(X1) is F/psi <= C'(|w|^2/a + 1/a^2) per unit u (psi >= 1/a and psi >= Phi_S), which also
  vanishes at the corner. The |w|^2 a^(-1-p) term of (1) is absorbed by -kappa |w|^2 once a > lambda_1 is large. The rest of
  section 9's argument and the support step carry over (b_res is analytic for |rho| < 1, and the noise is >= c Sigma_lin).
- Independent numerical check (s13_indep.py, s13_out.jsonl in this folder). No code is shared with lyapY_mlp.py or gen.py.
  The covariance is written out entrywise:
  (c + 2 gamma^2)(V_ac V_bd + V_ad V_bc) + k^2 (V_ac Q_bd + V_ad Q_bc + V_bc Q_ad + V_bd Q_ac), Q = V P V P V, which is the
  covariance of L(dN K + K dN^T)L^T. The drift comes from the formula in section 1 plus the paper's b_res. Y has an exact
  sympy gradient and Hessian, mpmath runs at 110 digits, and the parameters are the author's (q = p = 0.1, M = 10,
  delta = 0.05, a in [1e2, 1e10], Phi_S down to 1e-40). There are 150 fresh points per cell, 30 pct of them with a
  near-degenerate X shape and 20 pct with w = 0. Max of LY/(|W|^2 Y) for the new Y:
      m3 g2 1 D1 -1.69e-3;  m3 g2 .5 D1 -4.66e-3;  m3 g2 1 D4 -2.19e-3;  m4 g2 1 D1 -8.59e-3;  m4 g2 .3 D4 -4.32e-3;
      m5 g2 1 D1 -9.87e-3;  m3 g2 .1 D1 -1.54e-3 (not in the author's table);  m6 g2 1 D2 -9.80e-3 (not in the author's table).
  The old Y (section 9's M Phi_S^p) with the MLP terms comes out between +4e24 and +1.2e27 in every cell. The forcing failure
  and the fix reproduce, and the magnitudes match the author's table (e.g. m4 g2 1 D1: -8.6e-3 in both).
- Caveat on independence: the check reuses section 1's drift and noise formulas. Those were checked against the finite
  network (cov_check.py, sdrift.py) and audited earlier, but they are not re-derived from the paper here.

## Section 14 (Cor 4.3, m = 2, threshold gamma^2 < 1/2): PASS
- tr(P b_res) = (B11 + B22)/2 - B12 = -B12 (the diagonal of b_res is zero), and nu >= 0 on [-1, 1] (h(rho) = sqrt(1-rho^2)
  - rho arccos rho has h' = -arccos rho <= 0 and h(1) = 0).
- nu <= (Delta/4)(1 - rho): h is convex (h'' = 1/sqrt(1-rho^2)) with h(1) = 0, so h(rho)/(1 - rho) is minus the slope of a
  chord ending at 1. That slope increases with rho, so the ratio is largest at rho = -1, where it equals pi/2. That gives
  (1/(2 pi))(pi/2) = 1/4. Proved, not only gridded.
- qv: |L^T P L|_F = e^T V e = w for m = 2, so the congruence noise gives (2c + 4 gamma^2) w^2. The total sigma(w)^2 is a function
  of w alone, so there is a single Brownian motion beta.
- The comparison is fine in the Ikeda-Watanabe form, which allows an adapted drift for the middle process
  (b_lo(w_t) <= kappa w^3 - theta_t <= b_up(w_t)) with the same sigma.
- Feller: the near-0 exponent of s'_lo is gamma^2 Delta/(4(c + 2 gamma^2)), re-derived. For w_up the exact
  s'_up = (2c' + 4k^2 y^2)^(-1/(4 gamma^2)), so at gamma^2 = 1/2, s(inf) = inf.
- FIX (typo): the drift of S is (gamma^2 w^2/(4 tau0^2)) S + 2 (b_res)_12. The second display drops the tau0^2. Also
  2 (b_res)_12 >= 0, and it is <= 2 gamma^2 (Delta/4) w by the theta bound, so the linear-SDE argument holds.
  tr V = w + S/2 (checked).

## For the row
Sections 11-14 settle targets 1-3 as stated (with section 9 and section 4): for every m >= 2 and gamma^2 in (0, 1], with or
without the shaped ReLU MLP, P(explode) is in (0, 1) when m >= 3 or when m = 2 and gamma^2 < 1/2, and is 0 when m = 2 and
gamma^2 >= 1/2. A distinct-account review is still owed before the dossier calls it admitted.

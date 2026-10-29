# T255 audit of M2_EXACT.md sections 4 and 9 (agent H, 17 Oct 2026 20:36)

Text audited: M2_EXACT.md at commit 5119446389d1, the 20:26 version. The author confirmed that sections 4 and 9 do not change
while this audit is open. I read none of the scripts in rows/T255. My checks use my own generator, gen_b1e.py, built from the
formulas in section 1 alone. It computes drift = Df[b] + (1/2) sum D^2 f[E, E] over the noise directions E. The c-part is
L(sqrt(c) G)L^T, with G running over a GOE basis. The attention part is L(k(F K + K F^T))L^T, with F running over the m^2 unit
matrices. Arithmetic is mpmath at 100 digits, with fourth-order differences taking steps of 1e-30 |V|/|E|. The scripts and logs
are in (local dir)

Scope: sections 4 and 9 taken as consequences of the section 1 SDE. Whether section 1 is Theorem 4.2 is weak point (b). The
author's cov_check.py tests it against the finite network. I did not re-derive section 1 from Eqs. 1 and 9 of the paper, and I
did not rerun that check.

## Section 4 (m = 2): PASS
- w = tr(PV) is autonomous. Over 24 random PD 2x2 matrices with gamma^2 in {0.2, 0.5, 0.9, 1}, its drift equals kappa w^3 and its
  quadratic variation equals 2cw^2 + 4k^2 w^4. The largest relative error is 8e-39.
- The scale density follows by hand from 2b/sigma^2 = 2 kappa y/(2c + 4k^2 y^2) and kappa/(4k^2) = 1/(4 gamma^2):
  s' = (2c + 4k^2 y^2)^(-1/(4 gamma^2)). It is integrable at infinity iff gamma^2 < 1/2.
- Feller's test, checked by hand: below gamma^2 = 1/6 the inner integrand grows like z^(1/(2g2)-4), so the product is O(y^-3).
  For 1/6 <= gamma^2 < 1/2 the inner integral converges, and s' is integrable. At gamma^2 = 1/6 there is a log factor, which is
  harmless. So v(inf) < inf on all of gamma^2 < 1/2. For gamma^2 >= 1/2, s(inf) = inf, so there is no explosion. 0 is natural
  (d log w has drift tending to -c), and the hitting formula P = s(w0)/s(inf) is standard.
- "V explodes iff w does": the drift of S = 1^T V 1 equals (gamma^2 w^2/(4 tau0^2)) S, with relative error 1e-38. Its noise is
  linear in S. Analytically, in the basis (1/sqrt2, e), V = [[A, b], [b, w]] with b^2 <= A w. Then r^T V r = 2 b^2 w <= S w^2,
  so the attention part of qv(S) is <= 4 k^2 w^2 S^2. Numerically qv(S)/(S(1+w))^2 <= 1.65. Also tr V = S/2 + w. The argument
  holds.

## Section 2 (needed by both): PASS
tr(V^{-1} dV) = tr dGamma and tr((V^{-1} dV)^2) = tr(dGamma^2) hold for dV = L dGamma L^T. Also
tr(V^{-1} b) = (gamma^2/tau0^2)(|W|^2/m + D^T v/m). The quadratic variations are polynomial in |V| (|K|_F^2 = tr(PVPV)). So
log det V cannot reach -inf before |V| leaves a ball.

## Section 9: PASS for m = 3..10, with one gap for general m and two small notes
Lemma A, checked independently in the large-scale limit (attention noise only, V_11 = 1e6, Phi_S = 1e-12 unless stated):
- (i) alpha_m: the generator's drift of log V_11 per unit u equals (f - B^2/2) m^2/(m-1)^2 to 10 digits at m = 3, 4, 5 and
  gamma^2 = 0.5, 1. Also 2f/B^2 = (m^2 - m - 1)/(2 gamma^2 (m-1)). At the corner, b_11 = f a^3 and qv(V_11) = B^2 a^4 exactly.
- (ii) mu_S: m in {3, 4, 5} x gamma^2 in {0.3, 0.5, 1}, 6 random transverse shapes per cell. The shapes are either well
  conditioned or have eigenvalues spread over 8 decades, with |w| in {0, 1e-6, 1e-3}. At w = 0 the generator equals
  (gamma^2/m^2)(gamma^2 - m(m-2)/(m-1)) to 8 digits for every shape. At |w| = 1e-3 the spread is <= 1.3e-4, so the error is
  O(|w|). qv(log Phi_S) per unit u is bounded and the same for every shape (4 gamma^2/m^2 at m = 3, for example).
  In Phi_S the error is O(Phi_S), with constant 0.06-0.22 at m = 3, 4 for Phi_S from 1e-6 to 1e-1. The drift is still
  negative at Phi_S = 0.1. With the c-noise included, the drift lies below mu_S by O(c/a^2): at a = 1e3 it is -0.0555566
  against -0.0555556. That is the helpful sign, as the text says.
- (iii) tilt: the drift of |w|^2 per unit u divided by |w|^2 is -2 kappa to 1e-4 at |w| = 1e-3 and to 1e-5 at |w| = 1e-5, with
  kappa = gamma^2 (m-2)/(2m(m-1)), at m = 3, 4. At w = 0 it equals a constant times Phi_S, the same for every shape
  (m = 3: 0.0278 at gamma^2 0.5 and 0.111 at 1; m = 4: 0.0156 and 0.0625). So the + C Phi_S term holds as stated.
- m = 6, 8, 10 (3 shapes per cell, condition up to 1e6, |w| 0 and 1e-4): mu_S exact at w = 0, error <= 3.5e-6 at |w| = 1e-4,
  qv = 4 gamma^4/m^2 per u, alpha_m exact to 12 digits (bigm.log).

The proof, step by step:
- The small-power drifts: drift(a^-q) = -q a^-q (drift log a - q qv/2), and similarly for Phi_S^p.
- Y = a^-q + |w|^2 + M Phi_S^p with M p |mu_S| >= 4C has drift <= 0 on D. Phi_S <= Phi_S^p when Phi_S < 1.
- On the exit boundary, Y >= y_0. So P(exit) <= Y_0/y_0 by optional stopping. Explosion inside D before exit is allowed.
- On {tau = inf}, the martingale law of large numbers in the u-clock and |W|^2 >= c' a^2 on D give finite real time.
- The support step: the c-part makes the diffusion nondegenerate on the PD cone (c = gamma^2(2 - gamma^2) > 0). Change the
  coefficients outside a compact neighbourhood of the path to bounded smooth ones, apply Stroock-Varadhan to the modified
  process, which agrees with the original until it exits. Then use the strong Markov property at T. That is standard.
- V* = lambda e_1 e_1^T + eta I has w = 0 and Phi_S = (m-1) eta/(lambda + eta), so it lies in D with Y small.
I found no error in this chain.

Notes:
1. (gap, for "every m >= 3") Lemma A is exact symbolically only at m = 3..7 with w = 0, and at m = 3 with general w. Elsewhere it
   is numerical: theirs at m = 4, 5, mine at m = 3, 4, 5 and 6, 8, 10. None of it is a proof for general m. As written, the
   theorem is proved for the m that were computed. For all m it needs either a closed-form derivation of the limits (i)-(iii)
   for general m (the corner computation is a finite expansion in X/a and w, so a general-m algebraic derivation should be
   within reach), or the statement restricted to the m covered.
2. (notation) The u-clock is not normalised the same way throughout. alpha_m = (f - B^2/2) m^2/(m-1)^2 carries 1/tau0^2 through
   f and B, while mu_S and kappa are written without tau0. They agree only for tau0 = 1, or with du = |W|^2 dt/tau0^2. My
   numbers use the second clock. No sign changes.
3. Weak point (c) is not a gap: localisation as above. Weak point (b) remains the author's check, which I did not redo.

Verdict: section 4 KEEP. Section 2 KEEP. Section 9 KEEP for each m with Lemma A established (m = 3..7 symbolically at w = 0, plus
the numerical uniformity above). FIX NEEDED before "every m >= 3" is claimed: a general-m derivation of Lemma A, or a narrower
statement.

## Addendum (20:38): Lemma A for general m, derived by hand. This closes note 1.
Attention part, large scale, u-clock du = |W|^2 dt/tau0^2. Write l_i = L e_i and g_j = L K e_j = V P l_j. The attention noise
directions are E = k(l_i g_j^T + g_j l_i^T).

At w = 0: V = diag(a, X), L = diag(sqrt a, Lx), x_i = column i of Lx, s_j = 1_p . x_j. Then:
- g_1 = (a^{3/2}(m-1)/m, -sqrt(a) X 1_p/m) and g_j = (-a s_j/m, O(X^{3/2})) for j >= 2.
- l_1 = sqrt(a) e_1, and l_i = (0, x_i) for i >= 2.
Hence:
- E_11 = 2k a^2 (m-1)/m (i = j = 1), and E_11 = O(a^{3/2} X^{1/2}) (i = 1, j >= 2). So drift log a = a^2(f - B^2/2) + O(aX).
- The large part of E_p1 is k a^{3/2} ((m-1)/m) x_i (i >= 2, j = 1). So sum |E_p1|^2/a = k^2 a^2 ((m-1)/m)^2 tr X (1 + O(X/a)).
- tr E_pp = 2k x_i . (g_j)_p = O(sqrt(a) X^{3/2}). The Schur complement X' = V_pp - V_p1 V_1p/V_11 therefore has negligible
  first-order noise, and qv(log Phi_S) -> qv(log a) = 4 gamma^4 (m-1)^2/(m^4 tau0^2) a^2.
  This matches the 4 gamma^2/m^2 per u measured above.
- tr b_pp = (gamma^2/tau0^2) a^2 (m-1)^2/m^4 tr X + O(a X^2). The D-term is O(aX^2), since D_p = -a(m-2)/m^2 + O(X).
So drift log tr X' = (a^2/tau0^2)((m-1)^2/m^4)(gamma^2 - gamma^4) + O(aX). Subtracting drift log a and dividing by
|W|^2 = a^2 ((m-1)/m)^2/tau0^2 gives:
    gamma^4/m^2 - gamma^2 (m-2)/(m(m-1)) = (gamma^2/m^2)(gamma^2 - m(m-2)/(m-1)) = mu_S,   for every m >= 3.
Only tr X appears at leading order. The error terms are quadratic forms in X divided by tr X (for example
1_p^T X 1_p <= (m-1) tr X), so the limit is uniform in the shape, with error O(Phi_S). That agrees with the measured
gap/Phi of 0.06-0.22.

General w: T = [[1, 0], [-w, I]] gives T V T^T = diag(a, X). The Schur complement is unchanged by this row operation, and
T L = diag(sqrt a, Lx) =: L0, so T E T^T = k L0 (F K + K F^T) L0^T with K = L0^T P_w L0, where P_w = T^{-T} P T^{-1} and P_0 = P.
The w = 0 computation goes through with P_w in place of P, and with the transformed drift T b T^T in place of b. Its
pp-block picks up an O(a^2 |w| tr X) term from (Tv)_p = a(w_i^2 - w_i) + X_ii. Every leading term is a linear form tr(M(w) X)
with M polynomial in w and M(0) as at w = 0, so the limit is mu_S + O(|w|) + O(Phi_S), uniformly in the shape. Measured above:
the error is about 1e-4 at |w| = 1e-3.

(i) at general m is the first bullet. (iii) at general m:
- At w = 0, b_p1/a = O(aX) per unit t, which is O(Phi_S) per unit u.
- The covariation of V_p1 with V_11, divided by a^2, is O(aX).
- qv(w) = sum |E_p1|^2/a^2 = k^2 a tr X ((m-1)/m)^2, which is O(Phi_S) per unit u. This is the measured constant times Phi_S.
  For example, at m = 3, gamma^2 = 1 the formula gives k^2 ((m-1)/m)^2/((m-1)/m)^2 = gamma^4/m^2 = 0.111, as measured.
- The contraction -2 kappa |w|^2 is the linearised u-flow, as the text says.

Revised verdict: sections 2, 4 and 9 KEEP for every m >= 3, provided the text replaces "argued from rational dependence" with a
general-m derivation such as the one above. That is a FIX of the write-up, not of the result. Note 2 (the tau0 clock) stands.

Agrees with agent A's note that mu_S and kappa need the 1/tau0^2 factor (my note 2). Section 10, added later, is not
audited here.

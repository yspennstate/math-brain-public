# Referee audit notes (started 02:14, 23 Sep 2026)

Targets, in order of audit:
 1. Lemma 1 (L^p via Rogozin + Ball)            [RESULTS 2, FOURIER 2.3]
 2. Lemma 2 + (3.1) (Fresnel)                   [RESULTS 3, FOURIER 3.1 steps 1-3]
 3. Theorem F                                    [RESULTS 4, FOURIER 3.1]
 4. Theorem H                                    [RESULTS 5, FOURIER 3.2 (MF)]
 5. Theorem D, D', D_k                           [RESULTS 6, FOURIER 1, 1.1, 1.2]
 6. Lemmas 3-4                                   [RESULTS 7]
 7. Theorem C                                    [RESULTS 7 end, COUNTEREX 4]
 8. Lemma 1.4 + sublevel corollary               [GEOM 1.4]
 9. Theorem 2.1 (n = 3)                          [GEOM 2]
10. Theorem 3.1 + C1-C6                          [GEOM 3]
11. Theorem 3.2                                  [GEOM 3.3]
12. Props 4.1, 4.2                               [GEOM 4]
13. Theorems 5.1, 5.2                            [GEOM 5.1]
14. Props 5.3, 5.4, 5.5                          [GEOM 5.2]

Severity scale: fatal (statement false or proof unrepairable as written), fixable (gap with a repair),
cosmetic (constant/typo/wording).


## Entry 1. Lemma 1 (L^p bound). Verdict: CORRECT.
Re-derived: for p = 2m, |g^|^{2m} = FT of (g*g~)^{*m} (FT of g~ is conj g^); |g^|^{2m} <= |g^|^2 in L^1
(Plancherel, g in L^2 since |g| <= f <= 1); (g*g~)^{*m} continuous; inversion at 0 gives
int |g^|^{2m} = 2 pi (g*g~)^{*m}(0) <= 2 pi (f*f~)^{*m}(0). Rogozin: sup density of a sum of 2m independent
variables with densities <= 1 is <= that of U_1+..+U_{2m}, U uniform [-1/2,1/2], attained at 0 (symmetric
unimodal), = (1/pi) int (sin u/u)^{2m} du <= sqrt(2/(2m)) (Ball). So int|g^|^{2m} <= 2 pi/sqrt m.
General p: m = floor(p/2) >= 1 and p/4 < (m+1)/2 <= m for EVERY p >= 2, so 2pi/sqrt(m) <= 4pi/sqrt(p) always
(the case split in RESULTS is unnecessary but harmless). Twisted version (g = e^{isx^2} f) identical.
Numerical check: see Entry N1.

## Entry 2. Lemma 2 and (3.1). Verdict: CORRECT.
int exp(-a u^2 + i u y) du = sqrt(pi/a) exp(-y^2/(4a)), and -y^2/(4a) = -(eps - i theta) y^2. Re a =
eps/(4(eps^2+theta^2)) > 0, |a| = 1/(4 sqrt(eps^2+theta^2)) -> 1/(4|theta|). (3.1): multiply the three
representations (theta_k = t lambda_k), Fubini is legitimate for eps > 0 (|e^{-a u^2}| integrable), take
moduli, drop e^{-Re a_k u_k^2} <= 1, then eps -> 0 by dominated convergence on the left; the right side does
not depend on eps. v_k need not be orthonormal; W any real measurable function. Nothing to fix.

## Entry 3. Theorem F. Verdict: CORRECT (constants recomputed).
<Vu,X> = sum_i <rho_i,u> X_i. Given X_J, W = sum_{i in I} B_ii X_i^2 + (linear in X_I) + const because B_II is
diagonal; so the X_I-expectation factorises into prod_i g_i^(<rho_i,u> + s_i(X_J)), g_i = e^{itB_ii x^2} f_i.
Tonelli moves int du inside E_{X_J}; bound uniform in X_J. u = G_I^{-1/2} w; unit e_i, c_i = rho_i^T G_I^{-1} rho_i,
sum c_i e_i e_i^T = I_3; geometric BL with F_i(sigma) = |g_i^(sqrt(c_i) sigma + s_i)|^{1/c_i}, int F_i =
c_i^{-1/2} int |g_i^|^{1/c_i} <= 4 pi (Lemma 1, p = 1/c_i >= 2). Rows with rho_i = 0 are dropped (factor <= 1).
|phi| <= prod_k (4 pi |t lambda_k|)^{-1/2} (4pi)^3 det(G_I)^{-1/2} = (4pi)^{3/2}|t|^{-3/2}(|l1l2l3| det G_I)^{-1/2}.
int min(1, K|t|^{-3/2}) = 6K^{2/3}; (1/2pi) 6 K^{2/3} = (3/pi)(4pi)(...)^{-1/3} = 12(...)^{-1/3}. Correct.
Implicit hypothesis: G_I invertible (needed to write G_I^{-1}); fine.

## Entry 4. Theorem H. Verdict: CORRECT, including arbitrary A_HH (hub diagonal is only a phase).
Given X_J = x_J: Q = X_I^T A_II X_I + <2A_IH X_H + l_I, X_I> + (terms in X_H, x_J only), l_I = 2A_IJ x_J + b_I.
So |phi(t|x_J)| <= E_{X_H} |Phi_I(t; 2A_IH X_H + l_I)| <= int_{R^H} |Phi_I(t; 2A_IH x_H + l_I)| dx_H (f_h <= 1).
The ONLY x_H-dependence of Phi_I is through the tilt, so y = 2t x_H (dx_H = (2|t|)^{-|H|} dy) gives
t<2A_IH x_H, X_I> = <A_IH y, X_I>. (3.1) on the rank-r part of A_II with W = X_I^T D X_I + <l_I,X_I> + t^{-1}<A_IH y,X_I>,
then the X_I-expectation factorises into prod_i |g_i^(<rho~_i,(u,y)> + t l_i)|, g_i = e^{itD_ii x^2} f_i, and BL on
R^{r+|H|} exactly as in F (the constant shift t l_i is a translate, harmless). Result as stated. Star check:
H = {h}, r = 0, G~ = sum c_i^2 = 1 gives (2|t|)^{-1} 4 pi = 2 pi/|t|. Correct. Note: the bound never uses
int f_h = 1, only f_h <= 1 (so it is lossy but valid). Stars invisible to Theorem D: every A_IJ of
c e_h^T + e_h c^T + lambda v v^T has rank <= 2 (checked: h in I gives e_h c_J^T + lambda v_I v_J^T).

## Entry 5. Theorem D. Verdict: CORRECT (Lieb normalisation, Cauchy-Binet, AM-GM, beta_j = 1 all checked).
Decoupling: |phi|^2 <= E_{X_I}|E_{X_J} e^{itQ}|^2 = E_{X_J,X_J'} e^{i(g(X_J)-g(X_J'))} E_{X_I} e^{2it X_I^T M W}; the
X_I-only terms cancel in Q(X_I,X_J) - Q(X_I,X_J'). W_j densities g_j = f_j*f~_j <= 1.
BL normalisation (BCCT): int prod F_k(B_k x)^{c_k} <= BL prod (int F_k)^{c_k}, BL^2 = sup prod lam_k^{c_k}/
det(sum c_k lam_k B_k^T B_k) (Lieb). With d_i = alpha_i lam_i, e_j = (1-beta_j) mu_j the ratio is
prod (d_i/alpha_i)^{alpha_i} prod (e_j/(1-beta_j))^{1-beta_j} / det(D_J + M^T D_I M). Checked on B = 1 (BL 1), B = 2
(BL 1/2). Scaling: sum alpha + sum (1-beta) = 3 + |J| - 3 = |J|.
Determinant: det(D + P) = sum_T det(P_TT) prod_{j not in T} e_j (diagonal + any matrix), Cauchy-Binet
det((M^T D_I M)_TT) = sum_S det(M_ST)^2 prod_S d_i; keep |T| = 3; weighted AM-GM with w_ST gives
>= Z prod d^alpha prod e^{1-beta}. This version needs no e_j > 0, so beta_j = 1 (j in every T of positive weight,
factor g_j dropped using g_j <= 1) is covered; the det D_J det(I + N^T N) route of RESULTS needs e_j > 0 but also
works by continuity. Then BL <= Z^{-1/2} prod alpha^{-alpha/2} prod (1-beta)^{-(1-beta)/2}.
L^p: ||h_i||_{1/alpha_i} = ((2|t|)^{-1} int|psi_i|^{1/alpha_i})^{alpha_i} <= (4 pi sqrt(alpha_i)/(2|t|))^{alpha_i}
(needs alpha_i <= 1/2); alpha^{alpha/2} cancels; (2 pi/|t|)^3. ||g_j||_q <= 1. -x log x <= 1 - x on [0,1] gives
e^{3/2}. |phi|^2 <= e^{3/2}(2pi)^3 |t|^{-3} Z^{-1/2}; density 6 sqrt(e) Z^{-1/6}. All constants reproduced.
Remark (ii) (arbitrary weight w): AM-GM with weights w gives exp(E_w log det^2 + H(w)); two row-disjoint minors
>= delta with w = 1/2 each give Z_eff >= 2 delta^2. Correct (column marginals may equal 1: allowed).
D': Jensen E F <= (E F^q)^{1/q}; q = 2h, a = 3/(4h); density (1/pi) (a/(a-1)) B^{1/a} = 6 sqrt(e)(2h)^{-1/2}(3-4h)^{-1}
Z^{-1/6}. Correct. D_k: |phi| <= B|t|^{-k/(2q)}, density 2 sqrt(e) a/(a-1) q^{-1/2} Z_k^{-1/(2k)}; q = 2, k = 5:
5 sqrt(2e) Z_5^{-1/10} = 11.658 Z_5^{-1/10}. Correct. "k = 1, 2 give levels 1, 2 via Esseen": standard but the
constants are not written anywhere (cosmetic gap).
Remark (iv) ("a dense perturbation cannot hurt Theorem D") is only about Z; a perturbation can move the
marginals alpha_i, so it is a heuristic, not a theorem (cosmetic).

## Entry 6. Lemmas 3-4 (RESULTS 7) and Lemma 1.5 (GEOM). Verdict: CORRECT; singular limit checked.
Lemma 3: density of dV^2 at w (V density <= 1): (f_V(r)+f_V(-r))/(2 sqrt(|d||w|)) <= (|d||w|)^{-1/2}. "for every s"
should read "for a.e. s" (cosmetic). Sublevel consequences re-derived with C = 4:
P(|Q-s|<=eps) <= (4 eps/sqrt|d|) E max(|s-R|,eps)^{-1/2} <= (4 eps H/sqrt|d|)(1 + (1/2) log_+(1/(H^2 eps))) using
int_0^{eps^{-1/2}} min(1, H/v) dv. Layer-cake identity E k_d(s-R) = int_0^inf P(0 < sign(d)(s-R) < 1/(|d|lam^2)) dlam
correct; substitution lam = mu/sqrt|d| gives C(H') |d|^{-1/2}.
Lemma 4 / 1.5: A invertible: (A/A_PP)^{-1} = (A^{-1})_{P^cP^c}; eigenvalues of A^{-1} in [-1,1] are a consecutive
block a..b (b-a+1 = k); interlacing beta_j in [alpha_{j+p}, alpha_j] subset [-1,1] for a <= j <= b-p gives k-p
eigenvalues of the Schur complement with |1/beta| >= 1 (beta != 0 since the Schur complement is invertible).
Singular A: A_eps = (A + eps I)/(1-eps). lambda >= 1 -> >= 1; lambda <= -1 -> modulus (|lambda|-eps)/(1-eps) >= 1;
|lambda| < 1 stays < 1 once eps < (1 - max_{lambda<1} lambda)/2. A_eps invertible except finitely many eps,
(A_eps)_PP invertible for small eps, Schur complement continuous in eps, and {sigma_m >= 1} closed (sigma_m = m-th
largest |eigenvalue| is continuous). The division by (1-eps) is exactly what keeps eigenvalue -1 at modulus 1.
Correct. RESULTS' phrase "perturbing the kernel of A" is vaguer but the GEOM version is complete.

## Entry 7. Theorem C (one-sheet side). Verdict: CORRECT for forms without linear terms outside range(A);
the statement "every indefinite rank-three form" needs that scope (FIXABLE-scope, see Finding C1).
Parametrisation: y = (sqrt s cos - t sin, sqrt s sin + t cos, t): y1^2+y2^2 = s + t^2, y3^2 = t^2, q = s. Bijective
onto {q = s} (t = y3, theta unique mod 2pi). d_theta y = (a,b,0), d_t y = (-sin,cos,1), cross product
(b, -a, a cos + b sin) = (b,-a,-t); grad q = 2(y1,y2,-y3) = 2(b,-a,-t) = 2N. dsigma/|grad q| = (1/2) dtheta dt. Correct.
General eigenvalues: in y-space the ruling direction is D^{-1} w_theta, |D^{-1}w|^2 = sin^2/l1 + cos^2/l2 + 1/mu;
line integral = (2D marginal density)/|D^{-1}w| <= 2/|D^{-1}w|; p(s) <= (l1 l2 mu)^{-1/2} int dtheta/|D^{-1}w_theta|
= int dtheta / sqrt(l2 mu sin^2 + l1 mu cos^2 + l1 l2) <= 2 pi/sqrt 2 = pi sqrt 2 when l1, l2, mu >= 1. Correct.
2D marginal: Y = R^T X with R orthonormal columns, so the projection of Y to any 2-plane is U^T X with U having
orthonormal columns: LPP/Ball bound 2. Linear terms IN the range are absorbed by translating Y; linear terms
outside the range make Q = q(Y) + beta Y_4 and the argument does not apply (no "one-sheet side" exists then).
Measure-theoretic point: the line-integral bound "<= 2" holds for a.e. line only, and for fixed theta the lines
used form a one-parameter family (null in the plane). Fix: smooth X_i -> X_i + eps G_i (densities stay <= 1,
Y_eps has continuous density, bound holds pointwise), then P(Q in (s1,s2)) <= liminf P(Q_eps in (s1,s2)). Cosmetic.
Gaussian check: p(0) = (pi/sqrt 2)(6/pi) = 3 sqrt 2 for (1,1,-1) with variance 1/12. Consistent.

## Entry 8. Lemma 1.4 + sublevel corollary. Verdict: CORRECT (every constant reproduced).
Branches w_eps(t) = eps sqrt(delta/mu+) cosh t e+ + sqrt(delta/|mu-|) sinh t e-: q = delta cosh^2 - delta sinh^2 + kappa.
Jacobian of (delta,t) -> w: eps (cosh^2 - sinh^2)/(2 sqrt(mu+|mu-|)) = eps/(2 sqrt D). u = (a+b)/2, v = (a-b)/2,
a perp b so |u|^2 = |v|^2 = delta Lambda/4. Tail: |u_i| >= rho0/sqrt2, |v_i| <= rho0 <= sqrt2|u_i|; for e^{2t} >= 2 sqrt2
(T1 = (3/4) log 2 = 0.5199): |v_i|e^{-t} <= |u_i|e^t/2, so |w_i'| >= |u_i|e^t/2 >= |w_i|/3, w_i monotone; substitution
y = w_i(t), dt <= 3 dy/|y| on {|y| >= m} one side; bathtub max of int h/|y| over 0<=h<=1, int h<=1 on [m,inf) is
log(1+1/m). T = max(T1, log(2/|u_i|)) makes m >= 1, tail <= 3 log 2. log(2/|u_i|) <= log(4 sqrt2/sqrt(delta Lambda))
= (1/2) log(32/(delta Lambda)). Branch total <= 2*0.5199 + 6 log 2 + log_+ = 5.1988 + log_+ <= 5.2 + log_+. Two branches,
factor 1/(2 sqrt D): claim. Lambda >= 2/sqrt D by AM-GM gives the second form. Sublevel: int_{-u}^{u} log_+(K/|tau-tau0|)
<= 2u(1 + log_+(K/u)) (rearrangement; centred value 2u(1+log(K/u)) for u <= K, 2K <= 2u otherwise). Correct.
Small imprecision downstream (Thm 3.1 proof): "sup_u (2 sqrt u/sqrt D)(6.2 + log_+(16 sqrt D/u)) = 49.6 D^{-1/4},
maximum at u = 16 sqrt D" - the displayed function is unbounded for u > 16 sqrt D; the true statement uses
phi <= 1 there (phi(u)/sqrt u <= u^{-1/2} < 0.25 D^{-1/4}). So alpha_1 <= 49.6 D^{-1/4} holds (cosmetic).

## Entry 9. Theorem 2.1 (n = 3) and Cor 2.2. Verdict: CORRECT (constant 20 holds).
Route (i): S = A/a_ii has S^{-1} = (A^{-1})_{jk,jk}, ||.|| <= 1, so D_S >= 1. Definite: phi_R(u) <= 2 pi u (Lemma 1.3,
K = 1), int min(1, 2pi v^{-2}) dv = 2 sqrt(2pi) = 5.013. Indefinite: for u <= 1, log_+(16 sqrt D/u) = log 16 +
(1/2) log D + log(1/u); (log D)/(2 sqrt D) <= 1/e. Constant is 6.2 + 2.7726 + 0.3679 = 9.3405, not 9.34 (cosmetic;
integral recomputed below). Route (ii): sum a_ii^2 < 0.27, sum_{i<j} a_ij^2 > 1.365, max a_ij^2 > 0.455,
D > 0.365. kappa(x) = (A/B) x^2 + ..., A/B = det A/det B = 1/(A^{-1})_kk, |.| >= 1. alpha_1(kappa(X_k)) <= 2 sqrt 2
(Lemma 1.2(ii)); E log_+ 1/|s-kappa| <= 2 log(2 sqrt2) + 2 = 4.079 (layer cake: int min(1, a e^{-tau/2}) dtau =
2 log a + 2 for a >= 1). p_Q <= D^{-1/2}(9.28 + log_+(16 sqrt D)): derivative negative for D > e^{-22}, value at
D = 0.365 is 19.12. Definite B: pi/sqrt(0.365) = 5.20. Cor 2.2: condition on X_{S^c}, rescale by gamma. Correct.

## Entry 10. Theorem 3.1 (pivot calculus) and C1-C6. Verdict: CORRECT; all six compositions re-proved.
(P1) type 1, K = |a|^{-1/2}; (P2) K = D^{-1/2}(5.2 + log_+ 16 sqrt D) using 5.2 + a + x <= (5.2 + a)(1 + x);
(P3) K = pi/sqrt D.
(C1) phi_xi(u) <= K'u(1+log(1/u)) (u <= 1), phi <= 1: int_0^inf min(1, phi(v^{-2})) <= 2v0 + 2K'/v0 <= 4 v0 with
v0^2 = K'(1 + 2 log v0); x = v0^2/K' satisfies x - log x = 1 + log K' and x/2 <= x - log x, so v0^2 <= 2K'(1+log K').
Result 4 sqrt2 sqrt(K'(1+logK')) <= 8 sqrt(...). (C2) int_{-u}^u |y+d|^{-1/2} dy <= 4 sqrt2 u/sqrt(max(|d|,u)) (three
cases |d| <= u, u < |d| < 2u, |d| >= 2u); E max(|s-xi|,u)^{-1/2} <= max(K',1)(1 + (1/2) log(1/u)). (C3) 1 + 2 log_+ K' + 2.
(C4) K(2u + 2u(1+log(1/u))) <= 4Ku(1+log(1/u)). (C5) 4K sqrt u. (C6) 2Ku; alpha_1 <= sqrt(2K) <= max(2K,1).
Independent sums: p_Q(y) = E p_{Q1}(y - Q2); phi_{xi1+Q2} <= phi_{Q2}. Correct.
Constants: K1 = max(2sqrt2 c^{-1/2}, sqrt(2pi) c^{-1/4}, 49.6 c^{-1/4}) <= 50 c^{-1/2}; level 2 via 2x2:
2(6.2 + log 16 + (1/2)log_+ D)/sqrt D <= 17.95 c^{-1/2}; via 1x1: 4sqrt2 * 50 c^{-1} = 282.8 c^{-1}; level 3 via 1x1:
8 sqrt(283) c^{-1} sqrt(1 + log 283 + log(1/c)) = 134.6 c^{-1} sqrt(6.645 + log(1/c)); via indefinite + level 1:
8.4 c^{-1/2}(10.82 + log(1/c)), always smaller. K3 = 135 c^{-1} sqrt(6.7 + log(1/c)) confirmed.
Centres: in (P1) the centre is a quadratic polynomial in X_{-i} with matrix M/m_ii and SOME linear terms; the
induction hypothesis is uniform in linear terms, so the recursion closes. 4-coordinate claim: entries of
(M/m_ii)_{jk} depend only on the {i,j,k} principal block (quotient property). Direct sums: proved by
induction on the first pivot (1x1 lowers the level of one summand; an indefinite 2x2 in one summand plus
level >= 1 in another gives level 3; definite 2x2 gives level 3 alone). Correct.
Table in GEOM Section 6: "2(X1X2+X3X4): K_3(1) ~ 91" is the (C3)-branch value 8.4(3 + 2 log 50) = 90.9, not the
displayed K_3(1) = 135 sqrt 6.7 = 349 (cosmetic mislabel).

## Entry 11. Theorem 3.2 (fixed n). Verdict: CORRECT; one inconsistent parenthesis.
If max|m_ii| < 1/(2m) then sum m_ii^2 < 1/(4m), sum_{i != j} m_ij^2 > 1 - 1/(4m) >= 3/4, max m_ij^2 > 3/(4m(m-1)),
|det| > 3/(4m^2) - 1/(4m^2) = 1/(2m^2). m = 1 is trivial. Constants: alpha_1 <= 49.6 (2n^2)^{1/4} = 58.98 sqrt n;
alpha_2 <= 4 sqrt2 sqrt(2n) 59 sqrt n = 472 n; level 3: 8 sqrt(2n) sqrt(472 n (1 + log(472 n))) = 245.8 n sqrt(7.157 + log n).
The final C_n = 250 n (8 + log n) is valid (sqrt(7.2 + x) <= 8 + x) but the summary's "(so <= 4.5*10^3 for n <= 6)"
matches the sharper intermediate 246 n sqrt(7.2 + log n) (= 4425 at n = 6), not 250 n(8 + log n) (= 14,690 at n = 6).
Cosmetic. The true growth of the proof's bound is O(n sqrt(log n)).

## Entry 12. Props 4.1, 4.2. Verdict: CORRECT.
4.1(a): Ostrowski (eig(S H S^T) = theta_k eig(H), theta in [sigma_min^2, sigma_max^2]) + Cor 2.2. (b): x_i^T = r^(i)T R_S^{-1};
Cramer: x_ik = det(R_S, row k replaced by r^(i)T)/det R_S, a ratio of 3x3 minors of R, |.| <= 1 by maximality;
||R_S^{-1}|| = ||R R_S^{-1}|| (isometry) <= Frobenius <= sqrt(3 + 3(n-3)) = sqrt(3(n-2)). 20 * 3(n-2) = 60(n-2).
4.2: Tropp's lower Chernoff: P(lmin <= (1-d) mu) <= 3 [e^{-d}/(1-d)^{1-d}]^{mu/L}, mu = 1/2, d = 1/2, L = eps:
3 (0.8578)^{1/(2eps)} = 3 e^{-0.0767/eps}; eps = 1/50: 0.0648, union 0.1297, prob >= 0.870. e_3(A_IJ^T A_IJ) =
det(Lambda)^2 det G_I det G_J >= 4^{-6}; exact rank 3 so p_m = 1 and alpha_i = leverage of row i of R_I in its column
space <= l_i/lambda_min(G_I) <= 4/50. Density <= 6 sqrt(e) * 4 = 39.6. Correct.

## Entry 13. Theorems 5.1, 5.2. Verdict: CORRECT. Each composition needs only the centre's small-ball function
(or, in 5.2, the centre's potential beta_1 / beta_2), and every centre is again a quadratic polynomial in original
coordinates whose matrix is the current Schur complement (>= k - |P| large eigenvalues by Lemma 1.5) with
arbitrary linear terms, which is exactly the class the hypotheses quantify over.
Tree (5.1): level 3: 1x1 -> (C1) with alpha_2(centre); indefinite 2x2 -> (C3) with alpha_1(centre); definite -> P3;
none -> Hyp_3. Level 2: 1x1 -> (C2) with alpha_1(centre); 2x2 -> (C4)/(C6); none -> Hyp_2. Level 1: 1x1 -> Lemma 1.2;
2x2 -> Lemma 1.3/1.4 (alpha_2 <= A implies alpha_1 <= max(1.213 A, 1): max_{u<=1} sqrt u (1 + log 1/u) = 2/sqrt e);
none -> Hyp_1. Depth <= 3.
5.2 sufficiency: with beta_2(Z) = sup_s E[|s-Z|^{-1/2}; |s-Z|<=1], beta_1(Z) = sup_s E log_+ 1/|s-Z|:
level 3 via 1x1: p <= |a|^{-1/2}(1 + beta_2(xi)); via indefinite 2x2: p <= K(1 + beta_1(xi)) (these replace C1 and C3,
one line each; GEOM says "the only new composition is ..." - slightly incomplete, cosmetic). Level 2 via 1x1:
beta_2(Q) <= 1 + (4/sqrt|a|)(1 + (1/2) beta_1(xi)) (re-derived from Lemma 1.2(ii): the v-integral splits at r^{-1/2}).
Level 2 via 2x2: alpha_2 -> beta_2 <= 1 + 3 alpha_2. Level 1: alpha_1 -> beta_1 <= 2 log_+ alpha_1 + 2.
Necessity: X_0 uniform on [-1/2,1/2]: density of 4X_0^2 is 1/(2 sqrt w) on (0,1]; p_{R+4X0^2}(s) = (1/2)E[|s-R|^{-1/2};
0 < s-R <= 1]. p_{U^2-V^2}(z) = 2 log((sqrt(1/4-|z|) + 1/2)/sqrt|z|) re-derived (int db/sqrt(b(b+z)) = 2 arcsinh
sqrt(b/z)); >= log(0.729/|z|) >= log(1/(4|z|)) for |z| <= 1/8, so p_{4(U^2-V^2)}(z) >= (1/4) log(1/|z|) for |z| <= 1/2.
"sup_s" in the necessity should be an essential supremum (or widen X_0 slightly): cosmetic.

## Entry 14. Props 5.3-5.5. Verdict: CORRECT.
5.3: density of L' = 2<w,X> + b_h is <= sqrt2/(2|w|) (the proof's sqrt2/|w| is a factor-2 overestimate; valid).
E min(1, 2u/|L'|) <= 4u rho + 4u rho log(1/(2u)) + 2u for u <= 1/2, trivial for 1/2 < u <= 1. Correct (constant could be
2 + 2 sqrt2/|w|).
5.4: coarea exchange (int dv sum_x psi/|d_x G| = int dx sum_v psi/|d_v G|) correct; |d_v F| = 2 sqrt(|lambda||H|) at both
roots; l = r - a x - beta; quadratic part [[-sF, a sF - 1],[a sF - 1, a - a^2 sF]], determinant a sF - 1 (recomputed);
U uniform(-1,1) has density 1/2 <= 1 so Lemma 1.3/1.4 apply (Psi uses K = 1, a harmless overestimate: 2 sqrt(pi) would do).
a = 0: int f_h((s-F)/(2t)) rho dv <= 2 * 4 |t|^{1/2}|lambda|^{-1/2}; int_{|t|<1} dt/(2|t|) * 8|t|^{1/2}|lambda|^{-1/2} = 16|lambda|^{-1/2};
roots with |t| >= 1 give <= 1/2 (one root). Correct. Scope: Q must depend on X_{-h} only through (L,V); a linear
term outside span(w,v) is NOT covered (stated in the hypothesis; the result is not uniform in linear terms).
5.5: conditional density <= 1/max(|c1|,|c2|); (L1,L2) density <= 2/(s1 s2); int_{|z|_inf<=1} dz/|z|_inf = int_0^1 8r/r dr = 8.
Total 1/2 + 8/(s1 s2). Correct; uniform in linear terms.
Remark 2 after 5.5 ("sublevel statement of Prop 5.3 is FALSE for small nonzero diagonal"): true only in the
"any other entries" generality. Explicit witness (not given in the file): A = (1/a)(a,w)(a,w)^T, i.e. A_{-h,-h} = ww^T/a;
Q = Z^2/a with Z = aX_h + <w,X>, P(|Q| <= u) ~ 2 sqrt(|a|u) p_Z(0) -> alpha_2 = infinity. This A has rank ONE.
For the genuine hub aX_h^2 + 2X_h L (A_{-h,-h} = 0, two eigenvalues ~ +-|w|), the centre -L^2/a has an
inverse-square-root density ~ sqrt|a| p_L(0)/sqrt|z| and the convolution with |a|^{-1/2}|z|^{-1/2} is a LOG
singularity of size ~ p_L(0) log(1/|s|): alpha_2 stays O(1/|w|) (heuristic; see numerics). So the remark overstates
the obstruction for the pure hub; it is correct as a statement about Prop 5.3's generality. Cosmetic/precision.

## Entry N. Numerical checks run (num1_constants.py, num2_ruled_hyperbola.py; outputs in *_out.txt)
N1 Lemma 1: int|g^|^p for 3 laws (uniform; 3 spread intervals; 10 small intervals) x twist s in {0,3} x
   p in {2,2.5,3,4.5,7}: all values <= 6.27 against 4pi/sqrt p in [4.75, 8.89]; twisting only lowers them.
N2 Theorem D determinant/AM-GM: 30 random M (4-6 x 3-5, a third with a heavy row), sup over (log d, log e) by
   BFGS from 6 starts of log[Z prod d^alpha prod e^{1-beta} / det(D_J + M^T D_I M)]: max found 0.0000 (attained
   exactly when |J| = 3, all beta_j = 1, where the inequality is an identity along a ray), never positive.
   Marginal formula alpha_i = sum_m p_m u_m(i)^2 agrees with brute force to 1e-15.
N3 constants: int_0^inf min(1, 2v^{-2}(c + 2 log_+ v)) = 10.8236 (c = 9.34) and 10.8237 (c = 9.3405): the 10.83 of
   Theorem 2.1 is safe. Route (ii) value 19.115. (C1) Lemma-1.6 ratio: sup_K [int]/sqrt(K(1+log K)) = 4.000 (at K = 1),
   claimed 8. Indefinite 2x2 alpha_1: sup_u min(u^{-1/2}, (2 sqrt u/sqrt D)(6.2 + log_+(16 sqrt D/u))) = 4.93 D^{-1/4},
   NOT 49.6 D^{-1/4}: the file's 49.6 is the value of the uncapped function at u = 16 sqrt D, where phi <= 1 already
   gives 0.25 D^{-1/4}. Valid but a factor 10 loose (cosmetic; K_1 could be max(2 sqrt2 c^{-1/2}, 4.93 c^{-1/4})).
N4 Theorem 5.2 necessity: MC confirms p_{U^2-V^2} formula; min_{0<z<=1/2}[p_{4(U^2-V^2)}(z) - (1/4)log(1/z)] = 0.267 >= 0.
N5 Prop 4.2: 3 e^{-0.0767*50} = 0.0648 (exact form agrees); simulation (n = 200 random frame, max leverage 0.061):
   failure frequency 0.0005.
N6 Theorem C: ruling formula p(s) = (1/2)(l1 l2 mu)^{-1/2} int dtheta int rho_Y(D^{-1}(sqrt s e_theta + t w_theta)) dt,
   computed exactly (line-box intersections, 4000 theta) vs 6M-sample Monte Carlo, three configurations (R = I
   uniform with (1,1,1) and (2,3,1.5); random rotation R with spread two-interval sets, (1,1.7,1.2)), s in
   {0.02,0.1,0.3,0.7}: agreement within MC error (e.g. 1.2034 vs 1.2009; 0.1442 vs 0.1431). Parametrisation and
   Jacobian (1/2) confirmed independently of the Hadamard check in COUNTEREXAMPLE_SEARCH.md.
N7 Lemma 1.4: alternating-bathtub adversary (exact best response in each coordinate on a 2e-3 grid, 12 rounds) for
   8 random B (|mu| in [e^-2, e^2]) and delta in {1e-1,1e-3,1e-5}: ratio adversarial/bound <= 0.583, increasing
   with log(1/delta) at the rate of the bound's log term (coefficient attained). No violation.

## Entry 15. A FALSE SHARED FACT (not one of the audited theorems).
BRIEF line 91: "Rudelson-Vershynin Lemma 3.1: |psi(s)| <= 1 - c s^2 for |s| <= 2 pi and <= sqrt(2 pi/|s|) beyond,
for any density <= 1." As a POINTWISE statement this is FALSE. RV Lemma 3.1 (rv15/main.tex line 507) bounds the
non-increasing REARRANGEMENT |phi_X|^*(t), i.e. the measure of {s : |psi(s)| > tau}; LITERATURE.md line 29 states it
correctly, the shared statement dropped the word. Counterexample: fix s0 > 0 and M with 1/M < 2 pi/s0; X uniform on
E = union_{k=1}^M [2 pi k/s0 - 1/(2M), 2 pi k/s0 + 1/(2M)] (density 1, measure 1). Then psi(s0) = sin(s0/(2M))/(s0/(2M)),
e.g. s0 = 100, M = 1000: psi(s0) = 0.99958 while sqrt(2 pi/100) = 0.25; the same construction makes |psi(s0)| -> 1 at
ANY fixed s0 != 0, so the small-s part fails pointwise too. No proof in RESULTS/GEOM/FOURIER uses the pointwise form
(checked by grep; the proofs use only the L^p Lemma 1), and no other wave-2 NOTES.md uses it (checked 02:5x).
Severity for anyone who uses it pointwise: FATAL. Correct usable forms: Lemma 1 (int |psi|^p <= 4 pi/sqrt p) or the
rearrangement bound |{s : |psi(s)| > sqrt(2 pi/T)}| <= T.

## Entry 16. Numerics on GEOM Remark 2 after Prop 5.5 (num3_hub_diag.py, num3_out.txt).
Pure hub Q = a X_h^2 + 2(L + beta) X_h, X_h uniform, L = <w,X'> with w = 1/sqrt(60) (rho_L(0) = 1.382), exact conditional
formula averaged over 2e6 samples of L, s = +-10^{-k}, k = 1..7, a in {0.2, 0.05, 0.01}, beta in {0, 0.1}:
p_Q(10^{-k}) = 1.6, 4.7, 7.9, 11.1, 14.3, 17.5, 20.8 (a = 0.2, beta = 0): increments 3.1-3.3 per decade = rho_L(0) log 10 (3.18).
A LOG singularity of coefficient rho_L(0), flat in a (a = 0.01 gives the same numbers). So alpha_2(Q) = O(rho_L(0)),
no sqrt(|a| u)/|w| term, for the pure hub. The rank-one witness A = (1/a)(a,w)(a,w)^T, Q = (a X_h + L)^2/a, gives
P(|Q|<=u)/(u(1+log 1/u)) = 1.1, 2.5, 6.1, 15.9, 42.5 for u = 10^{-2..-6} (grows like u^{-1/2}): alpha_2 = infinity.
Conclusion: the Remark's statement "the sublevel statement of Prop 5.3 is FALSE for small nonzero diagonal" is right
only in Prop 5.3's "any other entries" generality, and only through remainders that cancel the random centre
(-L'^2/(4a) + R nearly constant). Its stated mechanism ("on the event L' ~ 0 ... Q is a one-dimensional quadratic")
is wrong for the pure hub, where averaging over the random centre turns the square root into a logarithm.
This agrees with (C1) of wave2/08 NOTES (type-2 profile around R, uniform in a). Severity: cosmetic for the record
(it is a remark, not a PROVED item), but relevant to configuration (b) of the open list.

## Entry 17. Theorem H pointwise check (num4_thmH_pointwise.py, num4_out.txt).
Q = 2 X_h <g,X_I> + <r,X_I>^2 (+ a_hh X_h^2) (+ diagonal twist D on I), n = 60, g perp r unit, max leverage 0.13; bound
(2|t|)^{-1}(4 pi |t|)^{-1/2}(4 pi)^2 = 0.704, 0.249, 0.063, 0.022 at t = 10, 20, 50, 100. Uniform laws, no twist:
|phi| = 0.306, 0.114, 0.0296, 0.0107: ratio 0.43-0.48 at every t (so the t^{-3/2} rate is sharp and the constant is
within a factor ~2.1). a_hh = 3 (nonzero hub diagonal): 0.216, 0.099, 0.029, 0.011 - still below, as the proof says
(A_HH only a phase). Twist D = 2 sin(i) and comb laws: at the MC floor (7e-4). No violation.

## Entry 18. Correction to my Entry 13 remark on "sup_s" in Theorem 5.2 necessity: not even cosmetic.
s -> E log_+ 1/|s-R| is lower semicontinuous (Fatou; log_+ 1/|x| is lsc), and an lsc function bounded a.e. is bounded
everywhere. For Hyp'_2 use g(x) = |x|^{-1/2} 1{|x| < 1} (lsc) and note R has no atoms (non-constant polynomial of an
absolutely continuous vector), so E[g(s-R)] = E[|s-R|^{-1/2}; |s-R| <= 1]. So the sup over ALL s is legitimate.

(Clock note: entries 1-18 were written between 02:14 and 02:59 by the machine clock; earlier in-text stamps were removed.)

## Entry 19. The other PROVED items of FOURIER_ROUTE_REPORT.md (listed in RESULTS 7 as "further proved extensions").
All CORRECT; constants re-derived.
- Prop 2.5 (S3): c = V_0^T W has density <= 2^{3/2} (LPP; 1 if |J| = 3); z = 2t S_0 c; geometric BL + Lemma 1 give (4pi)^3;
  |phi|^2 <= 8 pi^3 kappa_J/(s1 s2 s3 |t|^3); density (3/pi) B^{2/3} = 6 kappa^{1/3}(s1 s2 s3)^{-1/3}.
- Theorem F (general r, orthonormal frame): (1/pi)(a/(a-1)) B^{1/a}, a = r/2, gives 4r/(r-2) prod|l|^{-1/r}; 12 at r = 3.
- Theorem MF = Theorem H with J empty: (2|t|)^{-|H|} prod (4pi|t l|)^{-1/2} (4pi)^{r+|H|} = (4pi)^{r/2+|H|} 2^{-|H|} |t|^{-(|H|+r/2)}
  prod|l|^{-1/2}. Examples: B = (4pi)^{3/2}/2, (3/pi) B^{2/3} = 7.57; two heavy coordinates 4pi^2/t^2, density 4. Correct.
- Prop H (Hoelder in t): all four table entries re-derived (Hausdorff-Young with int g^{3/2} <= int_0^{1/4} y^{-3/4} = 2.83 <= 4;
  Cauchy-Schwarz pair bound (pi/(|mu||t|))^{1/2}, L^3 mass 6 pi/|mu|; Theorem F r = 1 gives 24 pi/|l|; Plancherel 2 pi D).
  2(X1X2+X3X4+X5X6): (1/2pi) (6pi) = 3.
- Lemma 4.1: kernel (4pi)^{-1/2} Gamma((1-a)/2) Gamma(a/2)^{-1} (|tau|/2)^{a-1} re-derived (v = tau^2/(4u)); c_{1/2} = (2pi)^{-1/2},
  c_{1/4} = 0.14926. Tail formula 2 b B^{a/b}/(a(b-a)) correct.
- Lemma 4.2: M_{1/4} <= 4 (|y^2 - c| >= (y -+ sqrt c)^2 on each half-line; bathtub split m, 1-m, max at m = 1/2).
- Lemma 4.3: (a) split at sqrt|u|, each half <= 2 log(1 + 1/(2a)); (b) product completion re-expanded; kappa = 0.8047.
- Cor 4.4: (i) 8 sqrt2 |a|^{-1/2}|l1 l2|^{-1/4}; (ii) 6.09; (iii) Schur complement -2 X3^2, 4 sqrt2 kappa = 4.55; (iv) the bound
  int |y^2 - c|^{-1/2} f <= 2(4 + log_+(1/(4c))) re-derived (layer cake gives 5.66 + 1.414 log(1/(4c)), smaller), I - 2rr^T
  pivots 1/3, then -1 with Schur complement 3 (checked). (iv) is a sketch with implicit constants; "bounded" is correct.
- Prop 5.1 (dichotomy): within-L leverage <= l_i/lambda_min(G_L) <= 1/2, det G_L >= (2 delta)^3. Correct.
Scope remark: Theorem MF, like Theorem H, requires A_LL to be EXACTLY diagonal + rank r on L.

## Entry 20. Two small proved additions for the report (checked twice).
(P) Hub with ARBITRARY diagonal, remainder off the leaves. Q = G(X_h, X_K) + <2 X_h w + b, X_S>, {h}, S, K disjoint, G any
measurable function, w != 0. Given (X_h, X_K), Q is affine in X_S with slope vector g = 2X_h w + b, |g| >= 2|w||X_h - x0|
(x0 from the component of b along w; the orthogonal component only increases |g|). 1D marginal: <g, X_S> has density
<= sqrt2/|g|, so P(|Q - s| <= u | X_h, X_K) <= min(1, kappa u/|X_h - x0|), kappa = sqrt2/|w|. Bathtub in X_h (weight symmetric
decreasing about x0): phi_Q(u) <= 2 kappa u (1 + log_+(1/(2 kappa u))) (<= 1 always). Since u(1 + log 1/u) increases on (0,1],
alpha_2(Q) <= 2 kappa (1 + log_+(1/(2 kappa))). Uniform in a_hh = coefficient of X_h^2 inside G. Two hubs (same argument,
2D bathtub E|X_H - x0|^{-1} <= 2 sqrt pi): ||p_Q|| <= sqrt(2 pi)/sigma_min(A_{S,H}) for ANY A_HH when A_SS = A_SK = 0.
Consistency: num3 pure hub (G = a x^2 + 2 beta x) has log coefficient 1.38 <= 2 kappa = 2.83.
(E) Esseen with explicit constant: K(x) = (sin(x/2)/(x/2))^2 = int (1-|tau|)_+ e^{-i tau x} dtau, K >= K(1) = 0.91939 on
[-1,1], so P(|Z - s| <= u) <= 1.0877 u int_{|t| <= 1/u} |phi_Z|. |phi| <= min(1, B|t|^{-1/2}) => alpha_1 <= 4.36 B;
|phi| <= min(1, B/|t|) => alpha_2 <= 2.18 max(B, 1). Fills the "via Esseen" steps for D_k (k = 1, 2, 4 with q = 2) and F (r = 1, 2).

## Entry 21. Index of verdicts (pointer to the entries above).
correct: Lemma 1 (E1), Lemma 2/(3.1) (E2), Thm F (E3), Thm H/MF (E4, E17), Thm D, D', D_k (E5), Lemmas 3-4/1.5 (E6),
Lemma 1.4 (E8), Thm 2.1/Cor 2.2 (E9), Thm 3.1 + C1-C6 (E10), Thm 3.2 (E11), Props 4.1-4.2 (E12), Thms 5.1-5.2 (E13, E18),
Props 5.3-5.5 (E14), FOURIER Prop 2.5, Prop H, Lemmas 4.1-4.3, Cor 4.4, Prop 5.1 (E19).
correct with a scope restriction (fixable): Theorem C needs b in range(A) (E7).
overstated remark: G Remark 2 after Prop 5.5 (E14, E16, E20).
false shared fact: the pointwise Rudelson-Vershynin decay in the shared list of facts (E15).
cosmetic: 49.6 -> 4.93, (C1) 8 -> 4, 9.34 -> 9.3405, Thm 3.2 parenthesis, K_3(1) ~ 91 label, Prop 5.3 factor 2,
"every s" in Lemma 3, Esseen constants unwritten (E20 supplies), Thm 5.2's composition list (E13).
Not audited (external records): the pair theorem and FULL_MATRIX_PAIR_EXTENSION.md small-ball bound used in R 7
"Physical blocks"; plausible (D_1 with q = 2 plus a cross block of norm >= ||S||/4 gives a (rho/||S||)^{1/4} small ball).

## Entry 22. Last numerical checks (num5_propP.py, num6_linalg.py; outputs num5_out.txt, num6_out.txt).
N10 Proposition P (Entry 20) is sharp: with G(x) = -a x^2 (so Q = 2 X_h L, centres aligned), the ratio
P(|Q| <= u)/(u(1 + log 1/u)) for u = 1e-2..1e-7 climbs 2.18, 2.35, 2.45, 2.53, 2.62 (spread w) and to 2.62 for
w = (e1+e2)/sqrt2 (rho_L(0) = sqrt2), approaching 2 rho_L(0) <= 2 sqrt2 = 2.83 = the bound.
N11 Prop 4.1(b): over 300 random frames (n = 3..10, rows of very unequal size), min sigma_min(R_S)^2 * 3(n-2) = 2.33 >= 1.
N12 Lemma 1.5: 0 violations in 8000 random Schur complements (p = 1, 2), a quarter of them with singular A and some with
eigenvalues exactly +-1.

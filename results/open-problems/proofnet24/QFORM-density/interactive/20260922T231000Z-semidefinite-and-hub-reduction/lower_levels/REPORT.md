## Summary

(H1) and (H2) are both **PROVED**, in the forms the reduction needs (GEOM Theorem 5.2), uniformly in the linear and constant terms. So the whole conjecture now reduces to (H3). Status by result:

- **(H1) log form: PROVED** (Theorem A). The small-ball bound is 6.8 u^{1/4} and sup_s E log_+ 1/|s - Q| <= 12. It needs only max|m_ii| <= 1/2 and ||M|| >= 1.
- **(H1) stronger alpha_1 form: PROVED** (Theorem A'), for no c-pivot with c <= 2e-6.
- **(H2') (half-power integrability): PROVED** (Theorem C), with c_* = 1e-15 and constant 10^6. We do not claim alpha_2 for (H2).
- **Corollary D:** the conjecture holds if and only if, for some c > 0, (H3) holds for matrices with no c-pivot.

**Key new ideas**
1. D_1 needs no marginal condition at q = 2. With a random partition this gives (H1) in two lines.
2. **Orientation lemma.** If every entry of a block is small next to its Frobenius norm, then either all row shares or all column shares are at most h, for any h > 1/2. That is enough for the D_1 and D_2 bounds at a threshold below 1.
3. **Discriminant of a coordinate.** Conditioning on X_h and using GEOM Lemma 1.2(ii) turns (H2) for Q into a small-ball bound with exponent above 1/4 for one auxiliary form. Its matrix is the matrix of 2x2 minors through h. This handles hubs with any diagonal and any remainder, which is exactly where decoupling stops at the (H2) threshold.

**What was checked**
- The 2-marginal formula agrees with brute force to 3e-15, and the minors identity is exact.
- The D_1 and D_2 inequalities at the exponents used are never violated in Monte Carlo (ratios at most 0.41).
- Random partitions in the one-dominant-eigenvalue case give s_2 >= 0.59, against 1/32 needed, and best-orientation marginals below 0.04.
- The (H2') quantity for hubs with diagonal 0 to 0.1 and correlated or dense remainders stays between 0.3 and 6.4, with no growth as the diagonal shrinks.
- Nothing uses the pointwise form of Rudelson-Vershynin Lemma 3.1.
- **Limit of the checks:** the one-dominant-eigenvalue case could only be tested at moderate size (K up to 150, n = 500). Its real hypotheses (K >= 1e4, tiny weighted leverages) would need n around 10^8, so there it rests on the written proof.

**Most useful next step:** (H3) only, for no-c-pivot matrices with c as small as you like. The discriminant bound ||p_Q|| <= sup_s' E|Delta^(h) - s'|^{-1/2} settles it whenever N^(h) has two large eigenvalues. In the remaining hub cases the information is in the factor f_h(x_+-) that this bound throws away; a (H3) hub argument has to keep that factor.

---

# REPORT: the lower levels (H1) and (H2) hold in the no-pivot regime

## 0. Results

X_1, ..., X_n are independent with densities f_i <= 1 and characteristic functions psi_i. M is real symmetric, Q = X^T M X + b^T X + c, and phi_Q(t) = E exp(itQ). For a random variable Z put phi_Z(u) := sup_s P(|Z - s| <= u) and alpha_1(Z) = sup_{s,u} P(|Z-s| <= u)/sqrt(u). M has *no c-pivot* if |m_ii| < c and |m_ii m_jj - m_ij^2| < c for all i != j. Then m_ij^2 < c + c^2 <= 2c. O := M - diag(M) is the off-diagonal part, and r_i := (sum_{j != i} m_ij^2)^{1/2} is the off-diagonal row norm.

**Theorem A.** If max_i |m_ii| <= 1/2 and ||M|| >= 1, then for all b, c: phi_Q(u) <= 6.8 u^{1/4} for every u > 0, and sup_s E log_+(1/|s - Q|) <= 12.

**Theorem A'.** If M has no c-pivot with c <= 2e-6 and ||M|| >= 1, then alpha_1(Q) <= 25 for all b, c.

**Theorem B (discriminant theorem).** Let 0 < nu <= 1, and let M have no c-pivot with c <= nu/9. For a coordinate h let N^(h) be the matrix indexed by i, j != h with
  N^(h)_ij = -det M_{{h,i},{h,j}} = m_hi m_hj - m_hh m_ij.
If ||N^(h)_off||_F >= nu for some h, then for all b, c:
  sup_s E[|s - Q|^{-1/2}; |s - Q| <= 1] <= 5 + 69 (16.92/nu)^{1/3}.
Nothing is assumed about the eigenvalues of M, about m_hh, or about the other entries.

**Theorem C.** Let c_* = 1e-15. If M has no c_*-pivot and at least two eigenvalues of modulus >= 1, then for all b, c: sup_s E[|s - Q|^{-1/2}; |s - Q| <= 1] <= 10^6.

**Corollary D.** The conjecture holds if and only if there is c > 0 such that every M with no c-pivot and at least three eigenvalues of modulus >= 1 gives ||p_Q||_inf <= C, uniformly in b and c.

## 1. Tools

(T1) *Decoupling.* For disjoint I, J (all other coordinates conditioned on, which is lossless):
  |phi_Q(t)|^2 <= E_W F_t(W),   F_t(W) = prod_{i in I} |psi_i(2t (M_IJ W)_i)|,   W = X_J - X'_J.
Here X' is an independent copy, and W has independent coordinates with densities g_j <= 1. Linear terms, constants and the blocks M_II, M_JJ do not appear. I and J may be exchanged.

(T2) *L^p lemma* (RESULTS Lemma 1): int |psi_i|^p <= 4 pi/sqrt p for every real p >= 2.

(T3) *Volume-sampling Brascamp-Lieb* (RESULTS Theorem D; FOURIER section 1.2). Let A = M_IJ with rows a_i and k in {1, 2}. Put Z_k = e_k(A^T A) = sum_{|S|=|T|=k} det(A_ST)^2 > 0, and let alpha_i = sum_{S containing i, T} det(A_ST)^2 / Z_k be the row marginals (sum = k). If 1 <= q <= 2 and max_i alpha_i <= q/2, then
  E_W F_t^q <= e^{k/2} (2 pi/|t|)^k q^{-k/2} Z_k^{-1/2},
hence
  |phi_Q(t)| <= [e^{k/2} (2 pi)^k q^{-k/2} Z_k^{-1/2}]^{1/(2q)} |t|^{-k/(2q)}.
Proof as in the record. Apply BL to F_t^q with exponents alpha_i on the rows and 1 - beta_j on the g_j; the scaling condition is sum alpha + sum(1 - beta) = |J|. By Lieb's theorem, keeping the order-k terms in the diagonal-plus-PSD expansion of det(D_J + A^T D_I A), then Cauchy-Binet and weighted AM-GM with weights det(A_ST)^2/Z_k:
  BL <= Z_k^{-1/2} prod alpha_i^{-alpha_i/2} prod (1 - beta_j)^{-(1-beta_j)/2}.
(T2) with p = q/alpha_i >= 2 gives ||.||_{1/alpha_i} <= ((2|t|)^{-1} 4 pi (alpha_i/q)^{1/2})^{alpha_i}. The powers of alpha_i cancel, prod (1 - beta_j)^{-(1-beta_j)/2} <= e^{k/2}, and E F <= (E F^q)^{1/q} finishes. No pointwise bound on psi is used anywhere in this report.

(T4) *Esseen with the Fejer kernel.* K(x) = (sin(x/2)/(x/2))^2 = int (1-|tau|)_+ e^{i tau x} dtau is at least 0.9194 on [-1, 1], so
  P(|Z - s| <= u) <= 1.0877 u int_{|t| <= 1/u} |phi_Z(t)| dt.
Hence |phi_Z(t)| <= B|t|^{-beta} with 0 < beta < 1 gives phi_Z(u) <= 2.1754 B u^beta/(1 - beta).

(T5) (GEOM Lemma 1.2(ii).) If g(x) = a(x - m)^2 + kappa with a != 0, and X has density <= 1, then
  P(|g(X) - s| <= u) <= min{2 sqrt(2u/|a|), 4u/sqrt(|a| |s - kappa|)}.

(T6) (GEOM Theorem 5.2.) For a fixed c in (0, 1], the three statements
  (H1') >= 1 eigenvalue of modulus >= 1, no c-pivot  =>  sup_s E log_+ 1/|s - Q| <= H_1,
  (H2') >= 2  =>  sup_s E[|s-Q|^{-1/2}; |s-Q| <= 1] <= H_2,
  (H3)  >= 3  =>  ||p_Q||_inf <= H_3,
all uniform in b, c, imply the conjecture, with constants polynomial in 1/c. The conjecture implies all three.

(T7) *2-marginal formula.* Let G = A A^T have eigenvalues lambda_m = s_m^2 and unit eigenvectors u_m (the left singular vectors). Then
  alpha_i^(2) = (G_ii tr G - (G^2)_ii)/e_2(G) = sum_m p_m u_m(i)^2,   p_m = lambda_m (tr G - lambda_m)/e_2(lambda) in [0, 1].
Proof: by Cauchy-Binet, sum_T det(A_ST)^2 = det G_SS, and sum_{S containing i} det G_SS = sum_{i' != i} (G_ii G_i'i' - G_ii'^2) = G_ii tr G - (G^2)_ii.
Two consequences:
 (a) alpha_i <= |a_i|^2 e_1/e_2 <= 2|a_i|^2/s_2^2. Indeed e_2 = (1/2) sum_m lambda_m (e_1 - lambda_m) and every e_1 - lambda_m is >= lambda_2.
 (b) With S = s_1^2, T = sum_{m >= 2} s_m^2 and A_res = A - s_1 u_1 v_1^T: for m >= 2, p_m <= s_m^2(S + T)/(ST), since e_2 >= ST. Hence
  alpha_i <= u_1(i)^2 + |row_i(A_res)|^2 (1/T + 1/S).

## 2. The first volume and the orientation lemma

**Theorem 1.** Let I, J be disjoint, A = M_IJ != 0 and 1/2 <= h <= 1. If every row satisfies |a_i|^2 <= h ||A||_F^2, then
  |phi_Q(t)| <= [2 pi e^{1/2} (2h)^{-1/2} ||A||_F^{-1}]^{1/(4h)} |t|^{-1/(4h)}.
The same holds with columns in place of rows. For h = 1 there is no hypothesis.
*Proof.* The 1x1 minors are the entries, so Z_1 = ||A||_F^2 and alpha_i = |a_i|^2/Z_1. Apply (T3) with k = 1 and q = 2h. The column version exchanges I and J in (T1). QED

**Lemma 2 (orientation).** Let ||A||_F^2 = Z > 0, 1/2 < h < 1, and A_ij^2 <= (2h - 1) Z for all entries. Then every row share is <= h, or every column share is <= h.
*Proof.* Suppose row i has share > h and column j has share > h. Then Z >= |row_i|^2 + |col_j|^2 - A_ij^2 > 2hZ - A_ij^2, so A_ij^2 > (2h - 1)Z. QED

**Corollary 3.** Suppose there are disjoint I, J with ||M_IJ||_F >= rho and every entry of M_IJ satisfying m_ij^2 <= ||M_IJ||_F^2/2. Then phi_Q(u) <= K(rho) u^{1/3} for all u, uniformly in the linear terms, where K(rho) = 3.263 (8.46/rho)^{1/3}.
*Proof.* Lemma 2 with h = 3/4, then Theorem 1 at h = 3/4 in the good orientation: |phi| <= (8.46/rho)^{1/3} |t|^{-1/3}, since 2 pi e^{1/2} (2/3)^{1/2} = 8.46. Then (T4) with beta = 1/3. QED

## 3. Proof of Theorems A and A'

*Theorem A.* ||O||_F >= ||O|| >= ||M|| - max_i |m_ii| >= 1/2. Put each coordinate in I or J by an independent fair coin. Then E||M_IJ||_F^2 = sum_{i != j} m_ij^2 P(i in I, j in J) = ||O||_F^2/4 >= 1/16, so some partition has ||M_IJ||_F >= 1/4. Theorem 1 with h = 1 gives
  |phi_Q(t)| <= (4 * 2 pi e^{1/2} 2^{-1/2})^{1/4} |t|^{-1/4} <= 2.33 |t|^{-1/4},
and (T4) gives phi_Q(u) <= 6.76 u^{1/4}. Then
  E log_+ 1/|s - Q| = int_0^inf P(|s - Q| < e^{-tau}) dtau <= int_0^inf min(1, 6.76 e^{-tau/4}) dtau = 4 log 6.76 + 4 <= 12. QED

*Theorem A'.* Let F^2 = ||O||_F^2 >= (1 - c)^2 and eps = 1/100. Call i *heavy* if r_i^2 > eps F^2; there are fewer than 1/eps heavy coordinates. Put every heavy coordinate in J, and each light one in I or J by an independent fair coin xi_i. Let Z = ||M_IJ||_F^2. Then
  E Z >= (F^2 - sum over heavy-heavy pairs of m_ij^2)/4 >= (F^2 - 2c/eps^2)/4 >= (19/20) F^2/4,
since c <= eps^2 F^2/40. Z is affine in each xi_i with |dZ/dxi_i| <= r_i^2, so by Efron-Stein
  Var Z <= (1/4) sum over light i of r_i^4 <= (eps/4) F^4.
By Chebyshev, P(Z < EZ/2) <= 0.18. So some partition has Z >= F^2/9 and every row of M_IJ light, hence every share is <= eps F^2/Z <= 0.09 <= 1/2. Theorem 1 at h = 1/2 gives |phi_Q(t)| <= 5.6 |t|^{-1/2}. (T4) with decay exactly 1/2 carries no logarithm:
  P(|Q - s| <= u) <= 2.1754 u * 5.6 * 2 u^{-1/2} <= 25 sqrt(u). QED

## 4. The discriminant of a coordinate; proof of Theorem B

Fix a coordinate h. Put X' = X_{-h}, w = (m_hj)_{j != h}, a = m_hh, L = <w, X'> + b_h/2, and R' = Q - a X_h^2 - 2 X_h L, a quadratic polynomial in X' with matrix M' = M_{-h,-h}. So Q = a X_h^2 + 2 X_h L + R'. For s in R define the *discriminant*
  Delta_s := L^2 + a (s - R').
It is a quadratic polynomial in X' with quadratic part N := w w^T - a M' = N^(h), and arbitrary linear and constant parts. As an n x n matrix, N^(h) = m_h m_h^T - m_hh M with m_h = M e_h; its h-th row and column vanish. Its diagonal entries are N_ii = -(the 2x2 principal minor on {h, i}), so |N_ii| < c. Every entry satisfies |N_ij| <= 2c + c sqrt(2c) <= 3c.

**Lemma 4.** P(|Q - s| <= u | X') <= min{1, 2 sqrt2 u^{1/2} |a|^{-1/2}, 4u |Delta_s|^{-1/2}}. For a = 0 the middle term is omitted.
*Proof.* Given X', Q = g(X_h) with g(x) = a(x + L/a)^2 + kappa, kappa = R' - L^2/a, and |a| |s - kappa| = |Delta_s|. Apply (T5). For a = 0, g is affine with slope 2L and Delta_s = L^2, so the probability is at most min(1, u/|L|). QED

**Lemma 5.** Let I(Delta, a) := int_1^inf min{1, 2 sqrt2 v^{-1}|a|^{-1/2}, 4 v^{-2} |Delta|^{-1/2}} dv. Then:
 (i) I <= 4 |Delta|^{-1/4};
 (ii) if 0 < |a| <= 1 and |Delta| <= a^2, then I <= 2 sqrt2 |a|^{-1/2} (2 + (1/2) log_+(a^2/(4|Delta|)));
 (iii) E[|s - Q|^{-1/2}; |s - Q| <= 1] <= 1 + E I(Delta_s, a).
*Proof.*
(i) Put D = 4|Delta|^{-1/2}. If D <= 1 the integral is D <= 4|Delta|^{-1/4}. Otherwise split at sqrt D: the value is at most 2 sqrt D = 4|Delta|^{-1/4}.
(ii) Put A = 2 sqrt2 |a|^{-1/2} >= 1 and V = D/A, the crossover of A/v and D/v^2. When |Delta| <= a^2 we have V >= A/2. Bound the integrand by 1 on [1, A], by A/v on [A, V] and by D/v^2 beyond. The total is A(2 + log_+(V/A)), and V/A = |a|/(2|Delta|^{1/2}).
(iii) Write Y = |s - Q|^{-1/2} 1{|s-Q| <= 1}. Then E Y <= 1 + int_1^inf P(|s - Q| < v^{-2}) dv; use Lemma 4 and Tonelli. QED

*Proof of Theorem B.* A random partition of the coordinates of X' gives ||N_IJ||_F^2 >= ||N_off||_F^2/4 >= nu^2/4. Entries satisfy N_ij^2 <= 9c^2 <= nu^2/8, because c <= nu/9. Corollary 3, applied to the form Delta_s in the variables X' with rho = nu/2, gives sup_{s'} P(|Delta_s - s'| <= r) <= K_Delta r^{1/3} for all r > 0, with K_Delta = 3.263 (16.92/nu)^{1/3}. This holds uniformly in s, since s enters only the constant term. Using Lemma 5 (i):
  E[4 |Delta_s|^{-1/4}] <= 4 + 4 int_1^inf K_Delta v^{-4/3} dv = 4 + 12 K_Delta.
If a != 0 (so |a| < c <= 1), Lemma 5 (ii) gives
  E[I; |Delta_s| <= a^2] <= 2 sqrt2 |a|^{-1/2} K_Delta |a|^{2/3} (2 + (3/2) 4^{-1/3}) <= 8.35 K_Delta |a|^{1/6}.
Lemma 5 (iii) gives the total 1 + 4 + 12 K_Delta + 8.35 K_Delta <= 5 + 21 K_Delta. QED

For a = 0 this recovers GEOM Prop. 5.3 in integrated form. The hub diagonal enters only through N^(h), and the discriminant sees any cancellation between a and the remainder. Example: M = (1/a)(a, w)(a, w)^T - [[0, 0], [0, v v^T]] gives N = a v v^T. There the coordinate h is not a hub at all, and Theorem C handles the case through Lemma 8 below.

**Lemma 6 (tests).** Assume no c-pivot. For every h:
 (i) for every unit eigenpair (mu, v) of M, ||N^(h)_off||_F >= |mu| (|mu| v(h)^2 - |m_hh|) - c;
 (ii) ||N^(h)_off||_F >= r_h^2 - |m_hh| ||M|| - c.
*Proof.* ||N_off||_F >= ||N_off|| >= ||N|| - max_i |N_ii|.
(i) v^T N v = <m_h, v>^2 - m_hh v^T M v = mu^2 v(h)^2 - m_hh mu.
(ii) ||N|| >= ||m_h m_h^T|| - |m_hh| ||M|| and |m_h|^2 >= r_h^2. QED

## 5. Random partitions

Let eps_i be independent signs, I = {eps_i = 1}, J its complement. For eigenpairs (mu_k, v_k), k = 1, 2, put V = [v_1 v_2] and V(i) = (v_1(i), v_2(i)), and define
  B := V_I^T M_IJ V_J = G_I Lambda G_J + V_I^T (M_3)_IJ V_J,
where Lambda = diag(mu_1, mu_2), M_3 = sum_{k >= 3} mu_k v_k v_k^T, G_I = V_I^T V_I = (I + Sigma)/2, G_J = (I - Sigma)/2 and Sigma_kl = sum_i eps_i v_k(i) v_l(i). Then
  4 G_I Lambda G_J = Lambda + [Sigma, Lambda] - Sigma Lambda Sigma,
and
  4 V_I^T (M_3)_IJ V_J = -V^T diag(M_3) V - C^(3),   C^(3)_kl = sum_{i != j} eps_i eps_j v_k(i) (M_3)_ij v_l(j).
The linear chaos cancels because sum_{j != i} (M_3)_ij V(j) = -(M_3)_ii V(i). Also:
- E (C^(3)_kl)^2 <= 2 max_i v_k(i)^2 ||M_3||^2.
- E Sigma_kl^2 = sum_i v_k(i)^2 v_l(i)^2.
- [Sigma, Lambda] = [[0, s], [-s, 0]] with s = Sigma_12 (mu_2 - mu_1).
- det(Lambda + [Sigma, Lambda]) = mu_1 mu_2 + s^2.
Since ||V_I||, ||V_J|| <= 1, s_k(M_IJ) >= s_k(B).

**Lemma 7 (comparable eigenvalues, light rows).** Suppose |m_ii| <= c, 1 <= |mu_2| <= |mu_1| <= K, every r_i <= rho, c <= 1/(8(K+2)) and rho <= 3/(64(K+2)). With probability >= 11/16 the block A = M_IJ has s_2(A) >= sigma_A := 3/(32(K+2)) and all 2-marginals <= 1/2. Hence |phi_Q(t)| <= 2 pi sqrt(e) sigma_A^{-1} |t|^{-1}.
*Proof.* From (mu_k - m_ii) v_k(i) = sum_{j != i} m_ij v_k(j) we get |v_k(i)| <= rho/(1 - c). Equivalently to the expansion above, 4B = [[mu_1, s], [-s, mu_2]] - V^T D V - C, with D = diag M and C the chaos of O. Here ||V^T D V|| <= c and E||C||_F^2 <= 16 rho^4. With probability >= 11/16 (Chebyshev), |Sigma_12| <= 4 rho/(1-c) and ||C||_F <= 8 rho^2. On that event:
- |s| <= 1/2, so |det| >= 3/4 and the norm is <= K + 1/2;
- s_2(4B) >= 3/(4(K+2)) - c - 8 rho^2 >= 3/(8(K+2)).
Marginals: by (T7a) they are <= 2 rho^2/sigma_A^2 <= 1/2. Also Z_2 >= s_2^4. Now apply (T3) with k = 2, q = 1. QED

**Lemma 8 (one dominant eigenvalue, delocalised).** Suppose |m_ii| <= c, |m_ij| <= sqrt(2c) with c <= 1e-6. Order the eigenvalues by modulus with |mu_2| = 1 and K = |mu_1| >= 1e4, and suppose K v_1(i)^2 <= eta and v_2(i)^2 <= eta for all i, with eta <= 6e-5. Then some partition and some orientation give Z_2(M_IJ) >= 1 and all 2-marginals <= 0.6. Hence |phi_Q(t)| <= 6.5 |t|^{-5/6}, phi_Q(u) <= 84.8 u^{5/6}, and (H2') <= 129.
*Proof.*
Step 1 (singular values). By Chebyshev, with probability >= 53/64:
- |Sigma_11|, |Sigma_12| <= 8 sqrt(eta/K), |Sigma_22| <= 8 sqrt(eta) and ||C^(3)||_F <= 8 sqrt(eta);
- ||Sigma Lambda Sigma||_F <= 256 eta, since the mu_1 entries meet only Sigma_11 and Sigma_12;
- ||V^T diag(M_3) V|| <= c + 2 eta, since diag(M_3)_ii = m_ii - mu_1 v_1(i)^2 - mu_2 v_2(i)^2;
- s^2 <= 65 eta K.
So P = [[mu_1, s], [-s, mu_2]] has |det P| >= 0.996K and ||P|| <= 1.001K, hence s_2(P) >= 0.995. The error terms total at most 0.078, so s_2(A) >= s_2(B) >= 0.229 and s_1(A) >= 0.249K.
Step 2 (the top direction). Write A = mu_1 x y^T + E with x = (v_1)_I, y = (v_1)_J, E = (M - mu_1 v_1 v_1^T)_IJ and ||E|| <= 1. Put sigma_0 = K|x||y| >= 0.4996K. Here AA^T = sigma_0^2 x^ x^T^ + P' with ||P'|| <= 2 sigma_0 + 1. If u = cos(phi) x^ + sin(phi) z is the top eigenvector, then |lambda sin(phi)| = |z^T P' u| <= ||P'||. So sin angle(u_1, x^) <= 2.001/sigma_0, and likewise for the right vector v_1 against y^.
Step 3 (the residual). Consequences:
- u_1(i)^2 <= 2.7e-7;
- |row_i(A_res)| <= |row_i(E)| + 2.001 |x^_i| <= 1.001;
- every entry of A_res is at most sqrt(2c) + (sigma_0 + 1)(|x^_i| + 2.001/sigma_0)(|y^_j| + 2.001/sigma_0) <= 2.73e-3;
- ||A_res||_F >= s_2(A) >= 0.229.
Lemma 2 with h' = 0.51 therefore gives an orientation in which every residual share is <= 0.51. By (T7b), alpha_i <= 2.7e-7 + 0.51 + 1.7e-7 <= 0.6. Finally Z_2 >= s_1^2 s_2^2 >= 1. Now apply (T3) with k = 2, q = 1.2, then (T4). QED

## 6. Proof of Theorem C

Order |mu_1| >= |mu_2| >= 1. Replacing Q by Q/|mu_2| keeps "no c_*-pivot", and does not increase the (H2') quantity, because 1/|mu_2| <= 1. So assume |mu_2| = 1, and put K = |mu_1| = ||M||.

*Case K <= 1e4.* Let rho_A = 3/(64 * 10002).
- If some r_h > rho_A: Lemma 6(ii) gives ||N^(h)_off||_F >= rho_A^2 - c_*(1e4 + 1) >= rho_A^2/2 =: nu_A. Theorem B applies (c_* <= nu_A/9) and gives a bound <= 7.9e5.
- Otherwise Lemma 7 applies, and (T4) plus integration give a bound <= 7.5e3.

*Case K > 1e4.* Let nu_B = 5e-5.
- If |mu_k|(|mu_k| v_k(h)^2 - c_*) >= nu_B + 2c_* for some h and some k in {1, 2}: Lemma 6(i) gives ||N^(h)_off||_F >= nu_B, and Theorem B gives <= 4.8e3.
- Otherwise K v_1(i)^2 < c_* + (nu_B + 2c_*)/K <= 6e-5 and v_2(i)^2 < nu_B + 3c_* <= 6e-5 for every i. Lemma 8 applies and gives <= 129. QED

## 7. Corollary D, and what remains

*Proof of Corollary D.* If (H3) holds for no-c-pivot matrices, put c' = min(c, c_*). Theorems A and C give (H1') and (H2') at c'. (H3) at c' follows from (H3) at c, because no c'-pivot implies no c-pivot. (T6) then gives the conjecture. The converse is immediate. QED

Remarks.
1. *What was uncovered before, and is covered now.* At level 1: no statement that every no-pivot matrix has a usable block; D_1 at q = 2 needs none, and Theorem A' removes the marginal issue for alpha_1. At level 2:
   - hubs with 0 < |m_hh| < c coupled to an arbitrary remainder (Theorem B);
   - blocks whose 2-volume is carried by one row, whatever the partition (the eigen-test sends these to Theorem B);
   - one eigenvalue much larger than the second, where the 2-marginal of the second direction was uncontrolled (Lemma 8, via the orientation lemma applied after removing the top direction).
2. *Strength.* (H1) holds in the alpha_1 form. For (H2) only the half-power integrability is proved; alpha_2 is not claimed.
3. *Level 3 through the discriminant (proved, but limited).* Given X', the conditional density of Q at s is (f_h(x_+) + f_h(x_-))/(2 sqrt(Delta_s)) <= Delta_s^{-1/2}. Hence
   ||p_Q||_inf <= sup_{s'} E|Delta^(h) - s'|^{-1/2} <= 1 + (H2')(Delta^(h)),
   and N^(h) has no pivot (entries <= 3c, 2x2 minors <= 10c^2). So Theorem C gives a bounded density whenever some N^(h) has two eigenvalues of modulus >= 1. But all eigenvalues of N^(h) except one have modulus <= |m_hh| ||M|| < c||M||, so this needs an eigenvalue of M of size >~ 1/c. For hub plus rank one with m_hh = 0, N = w w^T has rank one and the bound diverges logarithmically; the discarded factor f_h(x_+-) is what GEOM Prop. 5.4 uses. (H3) remains open in the configurations listed in the record, and the lower levels add no obstruction.
4. The constants are far from optimal (c_* = 1e-15, H_2 <= 10^6).

## 8. Numerical checks (Python, below-normal priority, scripts in 07_lower_levels/num/)

- **check_D1q2.py.** E_W prod |psi_i|^2 against the Theorem 1 bound at q = 2 (uniform and spread-set laws, seven block types, t from 0.5 to 100): maximum ratio 0.41. The single-row value matches the hand prediction of 0.42.
- **check_linalg2.py.**
  - The 2-marginal formula agrees with brute-force enumeration of all 2x2 minors to 3e-15.
  - The identity N^(h) = -(minors) is exact, and the eigen-test holds.
  - Lemma 8-type families (n = 500, K = 30 to 150, a second eigenvalue, sub-threshold hubs, Wigner noise): s_2(M_IJ) >= 0.59; best-orientation marginals <= 0.037; the bound (T7b) is never violated.
- **check_Dk_q.py.** (T3) at k = 1, q = 3/2 and at k = 2, q = 1.2: maximum ratios 0.28 and 0.10.
- **check_hub_H2.py.** Exact conditional preimage lengths, sup over 25 values of s. The (H2') quantity is 6.30, 6.33, 6.41 for pure hubs with a = 0, 0.01, 0.1; 3.03, 2.40, 2.08 as a theta goes to 0.9; and 0.29 to 1.54 with dense twists. Spread-set laws give lower values. There is no growth as a goes to 0.

# Proof tree for the bounded-density conjecture

Every node below is labelled PROVED (with the reference), PARTIAL, or MISSING (with the exact statement that
would close it). "GEOM" is GEOMETRIC_ROUTE_REPORT.md, "FOUR" is FOURIER_ROUTE_REPORT.md, "RES" is RESULTS.md,
"REP" is the report of this folder (new proofs: Lemma 0, Theorems A, A', Lemmas M, M', O, Theorem LF, Theorem S,
Corollary S1, Lemma HR, Corollary HR). The harness did not allow a REPORT.md file here; the report was returned as
text to the coordinator, and the proofs are also in NOTES.md (sections N1-N5) in compressed form.

## 0. Setting, quantities, parameters

X has independent coordinates with densities <= 1; Q = X^T A X + b^T X + c_0; A has at least three eigenvalues
of modulus >= 1. For a random variable Z:
  alpha_1(Z) = sup_{s,u} P(|Z-s| <= u)/sqrt(u),   alpha_2(Z) = sup_{s,u<=1} P(|Z-s| <= u)/(u(1+log(1/u))),
  H'_1(Z) = sup_s E log_+ 1/|Z-s|,   H'_2(Z) = sup_s E[|Z-s|^{-1/2}; |Z-s| <= 1],   alpha_3(Z) = ||p_Z||_inf.
A symmetric M has no c-pivot if every |m_ii| < c and every 2x2 principal minor has modulus < c; then every
|m_ij| < eps := sqrt(2c). Write E = M - diag(M) (zero diagonal, ||M - E|| < c), r_i = |row_i(E)|, and
mu_0 = 1 - c (E has at least k eigenvalues of modulus >= mu_0 when M has k of modulus >= 1, by Weyl).

Parameters (all universal): c = 1/500 (pivot threshold; any c <= 1/500 works), rho_0 = heavy-row threshold
(rho_0 = mu_0/8.5 at level 2, mu_0/14.7 at level 3 for the existence statement; rho_0 = mu_0/100 for the normal
forms), eta = remainder size (Frobenius), theta = leverage bound of spread directions.

Fourier decay needed per level (REP Lemma 0): H'_1 needs |phi| <= B|t|^{-b} with some b > 0; H'_2 needs b > 1/2
(alpha_2 needs b = 1); a density needs b > 1. D_k(q) (FOUR 1.2): if some disjoint I, J have Z_k = e_k(A_IJ^T A_IJ)
and all k-volume marginals on I are <= q/2 (1 <= q <= 2), then |phi| <= C Z_k^{-1/(4q)} |t|^{-k/(2q)}; q = 2 is
always allowed, so any 1-volume gives b = 1/4, any 3-volume gives b = 3/4, any 5-volume gives b = 5/4.

## 1. Root: arbitrary A  ->  three no-pivot problems                                   [PROVED]

Pivot tree of depth <= 3 (GEOM Thm 3.1, 5.1, 5.2; Lemma 1.5 keeps >= k large eigenvalues at a level-k node).
  N3 (current Schur complement M_3, >= 3 large eigenvalues):
     definite 2x2 pivot (det >= c)                   -> density <= pi c^{-1/2}                       [PROVED]
     indefinite 2x2 pivot B                           -> N1 on M_3/B, composition (C3): needs H'_1  [PROVED]
     1x1 pivot a (|a| >= c)                            -> N2 on M_3/a, composition (C1): needs H'_2 [PROVED]
     no c-pivot                                        -> NP3
  N2: 2x2 pivot -> alpha_2 <= 19 c^{-1/2} [PROVED]; 1x1 pivot -> N1 (Lemma 1.2(ii) composition) [PROVED];
      no c-pivot -> NP2.
  N1: any c-pivot -> alpha_1 <= 50 c^{-1/2} [PROVED]; no c-pivot -> NP1.
Constants: K_3 = 135 c^{-1} sqrt(6.7 + log(1/c)) etc. The linear terms at each node are arbitrary, so every NP
statement must be uniform in them; every Fourier bound below is (decoupling removes linear terms and the diagonal).

## 2. NP1: one large eigenvalue, no pivot                                               [PROVED, REP Thm A, A']

 * H'_1 <= 12 for every no-c-pivot M (c <= 1/2) with an eigenvalue of modulus >= 1: a random partition gives
   E||M_IJ||_F^2 = ||E||_F^2/4 >= mu_0^2/4, and D_1(q = 2) has no marginal condition.            (REP Thm A)
 * Stronger, the sublevel form: alpha_1(Q) <= 28.1 for c <= 1/500 (REP Thm A'). Rows sorted by norm; if every
   tail row set L_k failed the 1-marginal test, the tails would decay geometrically and the Frobenius mass
   would sit in a k x k principal block with entries < eps, impossible once ||E||_F^2 >= 242 eps^2.
 * With the pivot branch: EVERY symmetric N with an eigenvalue of modulus >= Lambda has alpha_1 <= 1118 Lambda^{-1/2}
   for all linear terms. This closes the level-1 node in the strongest (sublevel) form.

## 3. NP2: two large eigenvalues, no pivot

 3.1 Light-rows Fourier LF_2 (REP Thm LF).                                              [PROVED]
     For any row set L with rho_L = max_{i in L} r_i and nu = singular values of E_{L,.}: if
     e_2(nu^2) >= 36 rho_L^2 e_1(nu^2), a partition I subset L, J = rest has Z_2 >= e_2(nu^2)/32 and all
     2-marginals on I <= 1/2, so |phi| <= 2 pi sqrt(e) Z_2^{-1/4}/|t| and alpha_2(Q) <= C (nu_1 nu_2)^{-1/2}.
     In particular: NO ROW OF NORM > mu_0/8.5  =>  NP2 closed.
 3.2 A heavy row h with m_hh = 0: GEOM Prop 5.3, alpha_2 <= 2 + 4 sqrt 2/|m_h|, whatever the rest.  [PROVED]
 3.3 A heavy row h with 0 < |m_hh| < c.                                                  [PARTIAL]
     Hub reduction (REP Lemma HR, new): for any M and any h, with a = m_hh, m = M_{h,-h},
         alpha_2(Q) <= 8K (2 + log_+ 1/(8K)),   K = alpha_1(Delta),
         Delta = (2<m, X'> + b_h)^2 + 4a(s - Q|_{X_h=0}(X')),   matrix of Delta = 4(m m^T - a M_{-h,-h}) = -4a (M/a).
     With NP1 in sublevel form (Section 2): K <= 1118 Lambda_N^{-1/2}, Lambda_N = ||4(m m^T - a M_{-h,-h})||
     >= 4(|m|^2 - |a| ||M_{-h,-h}||). So NP2 is PROVED for no-pivot M with ||M|| <= rho_0^2/(2c) (rho_0 = mu_0/8.5):
     alpha_2 <= 1.1e5.
     MISSING (M-BIG2): the same when ||M_{-h,-h}|| >= |m|^2/(2|a|) for every heavy row h, i.e. the hub is absorbed
     by a huge eigen-direction. Exact statement: for no-c-pivot M with >= 2 eigenvalues of modulus >= 1 and some
     row with |m_h| >= mu_0/8.5, H'_2(Q) <= C uniformly in ||M||. (Huge eigenvalues occur naturally at N2: Schur
     complements of a c-pivot have norm up to ||A||^2/c.) Likely route: the refined marginal bound
     alpha_i <= lev_i(top-K singular space) + (k/s_k^2)|row_i(B - B_K)|^2 (REP Lemma M') in LF, which sees huge
     spread directions with their leverage instead of their row norm.

## 4. NP3: three large eigenvalues, no pivot

 4.1 Fourier menu (FOUR 1, RES 6): D (3-volume, I-marginals <= 1/2), D' (<= h < 3/4), D_4 (< 1), D_5 (none). [PROVED]
 4.2 Light-rows Fourier LF_3 (REP Thm LF).                                              [PROVED]
     If e_3(nu^2) >= 72 rho_L^2 e_2(nu^2) for some row set L then Theorem D applies to a partition with I inside L
     (heavy rows go to the unconstrained side J), with Z_3 >= e_3(nu^2)/128 and ||p_Q|| <= 22.2 (nu_1 nu_2 nu_3)^{-1/3}.
     Sufficient: nu_3(E_{L,.}) >= 14.7 rho_L. In particular NO ROW OF NORM > mu_0/14.7  =>  NP3 closed.
     This contains the lead's no-hub sketch (LEAD_NOTES 02:4x) and needs no spectral gap, no leverage bound and no
     concentration: only first moments over the random partition, the overlap inequality (REP Lemma O) and the
     marginal bound (REP Lemma M). It also covers every configuration whose third Fourier direction is carried by
     hub COLUMNS seen from light rows (>= 3 hubs with independent rows; 1 hub + spread rank 2 with the hub row
     independent of it; Wigner blocks of any row size, since only the ratio e_3/e_2 enters).
 4.3 Structure when LF_3 fails for every L (REP Thm S).                                 [PROVED]
     Heavy set H = {r_i > rho_0}, light L. Then
       (a) H is nonempty (a row of norm > mu_0/14.7 exists);
       (b) if nu_2(E_{L,.}) >= 17 rho_0 then sum_{j>=3} nu_j^2 < 192 rho_0^2: the light rows are rank 2 plus a
           Frobenius remainder < 13.9 rho_0;
       (c) Weyl count mu_{j+|H|}^2 <= nu_j^2: |H| = 1 forces nu_2 >= mu_3, |H| >= 2 when nu_2 < 17 rho_0;
       (d) |H| <= N_0 forces ||E_HH||_F <= N_0 sqrt(2c): with few hubs the hub block is negligible.
 4.4 |H| = 1: normal form E = S + R, S of rank 3 on span(p1, p2) + e_h, ||R||_F < 19.6 rho_0 (REP Cor S1);
     p1, p2 spread (leverage <= 2 rho_0^2/mu_0^2). In the basis (e_h, w^, v) with w^ the hub direction inside
     span(p1, p2): Q = a X_h^2 + 2k X_h L + sigma L^2 + gamma V~^2 + X^T(D + R)X + linear,
     L = <w^, X>, V~ = <v + (beta/gamma) w^, X>, D diagonal with |d_i| < c.
       sigma = 0, R = 0 (D arbitrary): Theorem H, H = {h}, r = 1.                          [PROVED, RES 5]
       D = 0, R = 0 (sigma arbitrary): GEOM Prop 5.4.                                       [PROVED]
       sigma = 0, R != 0: the canonical open case of the brief.                              [MISSING (M-TW)]
       sigma != 0, D != 0 (even with R = 0):                                                 [MISSING (M-DEG)]
     (M-DEG) is new: Theorem H needs the hub column independent of the Fresnel directions and here it is not;
     absolute-value Fourier gives only |t|^{-1}; every off-diagonal block has rank 2. Simplest instance:
         Q = 4 X_h L + 2 L^2 + 2 V^2 + sum_i d_i X_i^2,   L, V orthonormal spread, 0 < |d_i| < c
     (core eigenvalues -1.236, 2, 3.236; numerically bounded, 1.45-1.67; REP Section 9). Conditioning on X_h
     reduces it to a DEFINITE spread rank-2 form plus a diagonal twist, so it would follow from
       (M-D2) sup of the density of lambda_1 <u,X>^2 + lambda_2 <v,X>^2 + sum d_i X_i^2 + <b,X> over spread
              orthonormal u, v (leverage <= theta), lambda_1, lambda_2 >= 1, |d_i| <= c, all b, is <= C(theta, c).
       (For d = 0 this is the 2D projection bound, <= pi sqrt 2.)
 4.5 |H| >= 2.
     (a) Two heavy rows h1, h2 with sigma_min(E_{{h1,h2}, rest}) >= sigma_0:
         A_HH = 0: GEOM Prop 5.5, density <= 1/2 + 8 sigma_0^{-2}, whatever the rest.     [PROVED]
         A_HH != 0 (entries < sqrt(2c)): MISSING (M-2H): Prop 5.5 with |A_HH| <= sqrt(2c).
     (b) All pairs of heavy rows ill-conditioned (pairwise angles <= sigma_0/rho_0): E_{H,.} = c w^T + relative error.
         |H| <= N_0: condition on H \ {h*}, h* = argmax |c_h|; this returns 4.4 with the hub coupling divided by at
         most sqrt(N_0), PROVIDED the reduced core keeps three eigenvalues of modulus >= mu_0/(C N_0). [PARTIAL]
         |H| > N_0 (a generalized hub spread over many coordinates, or many heavy rows with a large E_HH): MISSING
         (M-MH). Expected: Fourier with part of H on the I side, using REP Lemma M' instead of the row-norm bound.

## 5. The list of missing statements (the whole conjecture follows from these)

 (M-TW)  [level 3, one hub, sigma = 0] Theorem H robust to a remainder twist: for the normal form of 4.4 with
         sigma = 0 and ||R||_F <= eta, |phi(t)| <= C |t|^{-1-kappa} for 1 <= |t| <= 1/||R||_F (some kappa > 0).
         The range |t| >= 1/||R||_F is handled by Theorem D ONLY IF R has no row carrying more than ~1/3 of
         ||R||_F^2 (REP Section 10); otherwise that row is a smaller hub to be peeled into S first (M-PEEL).
 (M-PEEL) iterated peeling of sub-hubs of R with a convergent bookkeeping of constants.
 (M-DEG) [level 3, one hub, sigma != 0] the normal form of 4.4 with sigma != 0 and a diagonal twist, R = 0 first;
         implied by (M-D2).
 (M-2H)  [level 3] GEOM Prop 5.5 with a small nonzero hub block.
 (M-MH)  [level 3] many heavy rows (|H| > N_0), and the eigenvalue bookkeeping in 4.5(b).
 (M-BIG2) [level 2] the hub reduction when the hub is absorbed by a huge eigen-direction (Section 3.3).
Everything else in the tree is PROVED. In particular NP1 is closed in both forms, and NP2, NP3 are closed for
every no-pivot matrix without a row of norm > mu_0/8.5 (resp. mu_0/14.7), for every configuration whose light rows
carry three (resp. two) Fourier directions of size >= 14.7 (resp. 6) times their row norms, and NP2 is closed for
every no-pivot matrix of norm <= rho_0^2/(2c).

## 6. Composition checks (the coordinator's questions)

 * Uniformity in linear terms: every Fourier step is a bound on |phi| of the conditioned form, uniform in its
   linear and constant terms and in diag(M); the hub reduction is uniform because Delta_s depends on s only through
   a constant; Prop 5.3-5.5 and Theorem H are uniform by construction. No branch uses bounded moments.
 * The hub block M_HH never enters the Fourier step (I inside L). It enters only 4.5(a) (Prop 5.5 needs A_HH = 0) and
   4.5(b) with many heavy rows; with |H| <= N_0 it is negligible, ||E_HH||_F <= N_0 sqrt(2c) (REP Thm S(d)).
 * Lead's no-hub sketch vs LF: same conclusion (Theorem D on a random partition), different mechanism. LF uses
   only E over partitions of Z_3 and e_2 (no Chebyshev, no normalisation by |Lambda|^{-1/2}), allows heavy rows on
   the J side, and gives the structure of the failure regime (4.3) as a by-product.
 * Coordinator's chain "one hub + one spread direction + ||R||_F small, Theorem D for |t| >= 1/||R||_F": correct for
   sigma = 0 once R has no sub-hub (M-PEEL); it does not cover sigma != 0 (M-DEG), which fails already at R = 0.
 * Scale: all constants are uniform in ||M|| except 3.3 (M-BIG2) and 4.5(b); huge eigenvalues are not harmful for
   LF itself (only ratios e_k/e_{k-1} enter) but they are for the crude marginal bound.

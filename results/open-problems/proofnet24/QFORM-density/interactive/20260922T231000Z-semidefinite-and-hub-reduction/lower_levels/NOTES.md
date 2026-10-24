# NOTES - lower levels (H1), (H2) in the no-pivot regime

## Entry 1. What the reduction actually needs, and (H1) in full (PROVED, to be re-audited)

Needed (GEOM Thm 5.2): for M with no c-pivot,
 (H1') >= 1 eigenvalue |.| >= 1  =>  sup_s E log_+ 1/|s-R| <= H_1,
 (H2') >= 2                      =>  sup_s E[|s-R|^{-1/2}; |s-R| <= 1] <= H_2,
uniformly in b, c.  Sufficient small-ball forms (phi_R(u) := sup_s P(|R-s| <= u)):
 (H1') <= phi_R(u) <= C u^delta for ANY fixed delta > 0:  E log_+ 1/|s-R| = int_0^inf P(|R-s| < e^{-tau}) dtau
        <= (1 + log C)/delta.
 (H2') <= int_1^inf phi_R(v^{-2}) dv < inf, e.g. phi_R(u) <= C u^{1/2+delta}, or C u log(e/u) (alpha_2).
Fourier: Esseen with the Fejer kernel: P(|Z-s| <= u) <= 1.0877 u int_{|t|<=1/u} |phi_Z(t)| dt
 (K(x) = (sin(x/2)/(x/2))^2 = int (1-|tau|)_+ e^{i tau x} dtau >= 0.9194 on |x| <= 1).
 So |phi_R(t)| <= B |t|^{-beta}, beta in (0,1), gives phi_R(u) <= 2.18 B u^beta/(1-beta).

### Theorem 1 (D_1 with q = 2; no marginal condition). 
For disjoint I, J and M = A_IJ,  |phi_Q(t)| <= (sqrt(2e) pi)^{1/4} (|t| ||A_IJ||_F)^{-1/4}  for all t, all b, c.
Proof. Condition on the other coordinates. Decoupling: |phi|^2 <= E_W F, F = prod_{i in I} |psi_i(2t (MW)_i)|,
W = X_J - X_J' (indep. coords, densities g_j <= 1). Jensen: E F <= (E F^2)^{1/2}.  E F^2 is a BL integral with
H_i = |psi_i(2t .)|^2 along rows a_i (exponent alpha_i = |a_i|^2/Z), g_j along e_j (exponent 1 - beta_j,
beta_j = |col_j|^2/Z), Z = ||M||_F^2; scaling sum alpha + sum(1-beta) = |J|.  Lieb + diagonal-plus-PSD expansion
(keep |T| = 1 terms) + weighted AM-GM: BL <= Z^{-1/2} prod alpha_i^{-alpha_i/2} prod (1-beta_j)^{-(1-beta_j)/2}.
L^p lemma with p = 2/alpha_i >= 2 (ALWAYS, since alpha_i <= 1): ||H_i||_{1/alpha_i} <= ((2|t|)^{-1} 4 pi sqrt(alpha_i/2))^{alpha_i}.
Product: E F^2 <= sqrt(2e) pi |t|^{-1} Z^{-1/2}.  So |phi|^4 <= sqrt(2e) pi /(|t| ||M||_F).  QED.
Sanity checks done by hand: single row (direct Ball + Plancherel gives sqrt(2) pi/(|t||a|), weaker constant e^{1/2}
in BL), single column (Holder with p_i = |a|^2/a_i^2 gives sqrt(2) pi/(|t||a|)). Consistent.

### Corollary (H1) PROVED.  If ||M|| >= 1 and max_i |m_ii| <= c < 1 (no other hypothesis!), then with O = M - diag M,
||O||_F >= ||O|| >= 1 - c, and a uniformly random partition has E||O_IJ||_F^2 = ||O||_F^2/4, so some partition has
||A_IJ||_F >= (1-c)/2 =: rho.  Theorem 1 + Esseen:
   sup_s P(|R - s| <= u) <= 2.91 (sqrt(2e) pi)^{1/4} (u/rho)^{1/4} <= 4.79 (u/rho)^{1/4},
   sup_s E log_+ 1/|s - R| <= 4 log 4.79 + 4 + log(1/rho) <= 10.3 + log(1/rho)  (<= 11.7 for c <= 1/2).
Uniform in b, c, n, laws.  This is (H1') of Thm 5.2 outright.  (It does not give alpha_1: exponent 1/4, not 1/2.)

## Entry 2. (H2): what decoupling gives, where it stops

Decay needed for (H2'): |phi| <~ |t|^{-1/2-delta} (or int_{|t|<=T}|phi| <= C T^{1/2-delta}).
 - D_2 with I-marginals <= h < 1 (q = 2h): decay 1/(2h) > 1/2.  OK.
 - D_3 with q = 2 (no marginal condition): decay 3/4.  OK.
 - D_1: at best decay 1/2 (q = 1, marginals <= 1/2): borderline, NOT enough.
Useful inequality: for the block M_IJ with rows r_i and singular values s_1 >= s_2 >= ...,
   alpha_i^{(2)} <= |r_i|^2 e_1(s^2)/e_2(s^2) <= 2 |r_i|^2 / s_2^2        (e_2/e_1 >= s_2^2/2 in both cases s_1^2 >< sum_{m>=2} s_m^2).
So small rows + s_2 bounded below => D_2.

No-hub case: if every row of O has norm <= rho (small), eigenvectors v_k of O with |mu_k| >= 1-c satisfy
|v_k(i)| <= |r_i|/|mu_k| (delocalised); a random partition gives B = V_I^T O_IJ V_J with E B = diag(mu)/4 and
fluctuations O(rho) (linear chaos part: (mu_l - mu_k) sum_i eps_i v_k(i) v_l(i)/4; quadratic part small).
Then s_2(O_IJ) >= s_2(B) >= min|mu|/8 w.p. >= 1/2.  [TO BE WRITTEN CAREFULLY - scale issue when |mu_1| >> |mu_2|.]

Hubs: a single hub h (row w, |w| ~ 1) is seen by every off-diagonal block with rank one; decoupling gives exactly
decay 1/2 from it: borderline for (H2).  Absolute-value Fourier bound for hub + general remainder R':
|phi(t)| <= int f_h(x) |Phi'(t, 2tx)| dx, Phi'(t,eta) = E e^{itR' + i eta L}; bathtub + Cauchy-Schwarz +
Plancherel in eta gives |phi| <= (sqrt 2 pi/(|t||w|))^{1/2}; any Holder p > 2 is worse; p < 2 needs the phase of R'.
So for hubs the Fourier route is stuck exactly at the (H2) borderline, and the real-variable route is needed:
 - a_hh = 0: GEOM Prop 5.3 gives alpha_2 whatever the remainder.  DONE.
 - 0 < |a_hh| < c: the open case (see Entry 3).

## Entry 3. Numerical check of Theorem 1 (NUMERICAL) - num/check_D1q2.py
E_W prod |psi_i(2t(MW)_i)|^2 / (sqrt(2e) pi/(|t| ||M||_F)) over t in {0.5,...,100}, 100k samples:
uniform laws: max ratio 0.41 (single row), 0.40 (column), 0.26 (Gaussian blocks), 0.33 (heavy row + noise),
0.41 (spread rank one), 0.40 (1x1 entry).  Spread-set laws: all <= 0.28.  The single-row value 0.41 matches the
hand prediction e^{-1/2} * 0.977/sqrt 2 = 0.42 (Gaussian-limit density of <a,W> for triangular W).  No violation.

## Entry 4. Hub with small diagonal: exact reduction to the "discriminant form" (PROVED)

Q = a X_h^2 + 2 X_h L + R',  L = <w, X'> + beta, R' ANY quadratic polynomial in X' = X_{-h}.
Given X', Lemma 1.2(ii) with critical value kappa = R' - L^2/a gives, since |a||s - kappa| = |Delta_s|,
   P(|Q - s| <= u | X') <= min{1, 2 sqrt 2 u^{1/2} |a|^{-1/2}, 4 u |Delta_s|^{-1/2}},   Delta_s := L^2 + a (s - R').
Integrate v from 1 to inf with u = v^{-2}:
   int_1^inf min(1, 2sqrt2 v^{-1}|a|^{-1/2}, 4 v^{-2}|Delta|^{-1/2}) dv
      <= C ( |Delta|^{-1/4} 1{|Delta| > a^2} + |a|^{-1/2} (1 + log(a^2/|Delta|)) 1{|Delta| <= a^2} ).
Hence  E[|s - Q|^{-1/2}; |s-Q| <= 1] <= 1 + C E(...).  If Delta_s has a uniform small-ball bound
   sup_{s'} P(|Delta_s - s'| <= r) <= K r^theta  (all r > 0) with theta > 1/4,
then the first term is <= K/(4 theta - 1) + 1 and the second is <= K |a|^{2 theta - 1/2}(1 + 1/theta) <= K(1 + 1/theta).
So: (H2') for the hub form holds as soon as the discriminant form Delta_s (matrix N = w w^T - a M', which is
-a times the Schur complement M/a) has small-ball exponent > 1/4, uniformly in its linear terms.
Checks: a = 0 gives Delta = L^2, exponent 1/2 (Prop 5.3 recovered).  Pure hub R' = 0: Delta = L^2 + as, fine
uniformly in a (matches the X_h-first computation P <~ (u/|w|) log(1/u)).
The theta > 1/4 threshold is EXACTLY what Theorem 1 (D_1, q = 2) misses: it gives theta = 1/4.  D_1 with I-marginals
<= h < 1 (q = 2h) gives decay 1/(4h) > 1/4, i.e. theta > 1/4.  So what is needed for N is a partition whose
off-diagonal block has Frobenius norm >= rho and no I-row carrying more than a fraction h < 1 of it.

Warning example (why N can be small): M = (1/a)(a,w)(a,w)^T - [0 0; 0 v v^T], v perp w spread: no pivot (for n large),
eigenvalues ~ |w|^2/a and -1, and N = a v v^T is O(|a|).  But then Q = (aX_h + L)^2/a - V^2 is a SPREAD rank-two form
(the vector (a,w) is spread; h is not a true hub) and D_2 applies to M itself.  So the hub analysis must be run only
after D_2/D_3 for M have been ruled out.

## Entry 5. Three ingredients found for (H2)

(a) ORIENTATION LEMMA (PROVED, trivial).  For a real matrix A with ||A||_F^2 = Z and max A_ij^2 <= eta Z, and
h in (1/2,1) with 2h - 1 >= eta: either every row share |row_i|^2/Z is <= h or every column share is <= h.
Proof: row i share > h and column j share > h give Z >= |row_i|^2 + |col_j|^2 - A_ij^2 > 2hZ - A_ij^2.
Consequence (D_1 at threshold h): D_1 marginals ARE row shares (1x1 volume sampling), and decoupling may be run
with either side as I.  With q = 2h, E_W F^q <= e^{1/2}(2 pi/|t|) q^{-1/2} Z^{-1/2}, so
   |phi(t)| <= [e^{1/2} 2 pi q^{-1/2} Z^{-1/2}]^{1/(2q)} |t|^{-1/(2q)},  q = 2h.  h = 3/4: decay 1/3.
So: ANY off-diagonal block with ||A_IJ||_F^2 = Z >= rho^2 and entries^2 <= Z/2 gives small-ball exponent 1/3 > 1/4.
In the no-pivot regime entries are tiny, so this is available whenever (H1)'s Frobenius block exists.

(b) THE DISCRIMINANT MATRIX IS A MATRIX OF 2x2 MINORS (identity, checked).  For a coordinate h let m_h = M e_h.
   N^(h) := m_h m_h^T - m_hh M   (its h-th row and column vanish),   N^(h)_ij = -det M_{{h,i},{h,j}}.
So N^(h)_ii = -(principal 2x2 minor on {h,i}), |N_ii| < c under no pivot; |N_ij| <= 2c + c sqrt(2c).
The hub reduction of Entry 4 (Q = a X_h^2 + 2 X_h L + R') has Delta_s with quadratic part N^(h) restricted to
X_{-h}; linear part arbitrary.  With (a): (H2') holds with C(nu) as soon as ||N^(h)_off||_F >= nu (and c <= c_0(nu)).
   HUB THEOREM: no c-pivot, some h with ||N^(h)_off||_F >= nu  =>  (H2'), C = C(nu), whatever the rest of M.

(c) EIGEN-TEST.  For any unit vector v: v^T N^(h) v = <m_h, v>^2 - m_hh v^T M v.  For an eigenpair (mu_k, v_k):
   v_k^T N^(h) v_k = mu_k^2 v_k(h)^2 - m_hh mu_k,   so ||N^(h)|| >= |mu_k| (|mu_k| v_k(h)^2 - c).
Hence the hub theorem applies at h whenever SOME eigenpair with |mu_k| >= 1 has weighted leverage
|mu_k| v_k(h)^2 >= 2c + nu.   [Pure hub: v_+ = (e_h + w)/sqrt2, mu = 1: |mu| v(h)^2 = 1/2.  Warning example of
Entry 4: h has weighted leverage a^2/(a^2+|w|^2) * |w|^2/a ~ |a| -> hub theorem correctly does NOT fire.]

DICHOTOMY for (H2) (M no c-pivot, top two eigenpairs (mu_1, v_1), (mu_2, v_2), |mu_1| >= |mu_2| >= 1):
 (L) localized: some h, k in {1,2} with |mu_k| v_k(h)^2 >= eps  ->  HUB THEOREM (needs c << eps).
 (D) delocalized: v_k(i)^2 < eps/|mu_k| for all i, k = 1,2  ->  want D_2 for a random partition.
In (D): with G_I = V_I^T V_I = I/2 + Sigma/2 (Sigma_kl = sum eps_i v_k(i) v_l(i), Rademacher), G_J = I - G_I,
   B := V_I^T M_IJ V_J = G_I Lambda G_J + V_I^T (M_3)_IJ V_J,  M_3 = sum_{k>=3} mu_k v_k v_k^T,
   4 G_I Lambda G_J = Lambda + [Sigma, Lambda] - Sigma Lambda Sigma,
and every fluctuation is small relative to Lambda EXCEPT the antisymmetric [Sigma, Lambda] (size sqrt(eps|mu_1|)),
which does not hurt: det(Lambda + [Sigma,Lambda]) = mu_1 mu_2 + sigma_12^2 (mu_1 - mu_2)^2 and sigma_12^2 <~ eps/|mu_1|.
So s_2(M_IJ) >= s_2(B) >~ 1/8 w.p. >= 1/2, UNIFORMLY in how large mu_1 is.  The remaining issue for D_2 is the
I-marginal (a sub-threshold hub inside M_3, or the huge direction, can carry a marginal near 1): see Entry 6.

## Entry 6. A complete architecture for (H2) (PARTIAL -> being audited)

Normalise: order eigenvalues |mu_1| >= |mu_2| >= ...; scaling Q -> Q/|mu_2| keeps "no c-pivot" and
(H2')(Q) <= (H2')(Q/lambda) for lambda >= 1.  So WLOG |mu_2| = 1, K := |mu_1| = ||M||.
Fix constants: nu (hub threshold), K_0 (bounded/huge split), c << nu, c << 1/K_0^3.

STEP H (hub theorem, Entry 5b): if some h has ||N^(h)_off||_F >= nu then (H2') <= 5 + 22 K_Delta,
   K_Delta = 3.26 B, B = [4 pi e^{1/2} sqrt(2/3)/nu]^{1/3} ~ 2.57 nu^{-1/3}.
   Derivation of the "5 + 22 K": I(Delta,a) := int_1^inf min{1, 2sqrt2 v^{-1}|a|^{-1/2}, 4 v^{-2}|Delta|^{-1/2}} dv
   <= min{4|Delta|^{-1/4}, 2sqrt2|a|^{-1/2}(2 + (1/2)log_+(a^2/(4|Delta|)))}; with P(|Delta| <= r) <= K r^{1/3}:
   E[4|Delta|^{-1/4}; |Delta| > a^2] <= 4 + 12 K;  E[2nd; |Delta| <= a^2] <= 2 sqrt2 K |a|^{1/6}(2 + 3/2) <= 9.9 K.

STEP A (bounded, K <= K_0).  If some row r_h >= rho: ||N^(h)|| >= |m_h|^2 - |m_hh| ||M|| >= rho^2 - c K_0, so
   ||N_off||_F >= rho^2 - c(K_0+1) >= rho^2/2 =: nu  ->  STEP H.
   Else all rows < rho: eigenvectors |v_k(i)| <= r_i/(|mu_k| - c) (from (mu_k - m_ii) v_k(i) = sum_{j!=i} m_ij v_k(j)).
   Random partition, B = V_I^T M_IJ V_J (V = [v_1 v_2]):  4B_kl = v_k^T O v_l + (mu_l - mu_k) S_kl - C_kl, where
   S_kl = sum_i eps_i v_k(i) v_l(i), C_kl = sum_{i!=j} eps_i eps_j v_k(i) O_ij v_l(j) (the m_ii terms CANCEL in the linear
   part).  E S_12^2 <= max v_1^2, E C_kl^2 <= 2 sum a_ij^2 <= 2 max_i v_k(i)^2 sum_j v_l(j)^2 r_j^2.
   4B = [[mu_1, s],[-s, mu_2]] + err, s = (mu_2 - mu_1) S_12; |det| >= |mu_1 mu_2| - s^2, s_1 <= 2K_0 + 1.
   => s_2(M_IJ) >= s_2(B) >= sigma_0 := 3/(32(2K_0+1)) w.p. > 1/2 (rho <~ 1/K_0).  Marginals:
   alpha_i <= |a_i|^2 e_1/e_2 <= 2|a_i|^2/s_2^2 <= 2 rho^2/sigma_0^2 <= 1/2.  D_2 (q = 1) gives decay |t|^{-1}: alpha_2.

STEP B (huge, K > K_0).  Eigen-test (Entry 5c) for k = 1, 2: if |mu_k|(|mu_k| v_k(h)^2 - c) >= nu + c for some h
   -> STEP H.  Else (D'): K v_1(i)^2 < c + (nu+c)/K and v_2(i)^2 < nu + 2c for all i.
   Random partition: G_I = V_I^T V_I = I/2 + Sigma/2, G_J = I/2 - Sigma/2,
     B = V_I^T M_IJ V_J = G_I Lambda G_J + V_I^T (M_3)_IJ V_J,  4 G_I Lambda G_J = Lambda + [Sigma,Lambda] - Sigma Lambda Sigma.
   M_3 part: mean -(1/4)V^T diag(M_3) V (small: diag(M_3)_ii = m_ii - mu_1 v_1(i)^2 - mu_2 v_2(i)^2), linear chaos
   VANISHES (since sum_{j!=i}(M_3)_ij V(j) = -(M_3)_ii V(i)), quadratic chaos variance <= 2 max_i v_k(i)^2 ||M_3||^2.
   Sigma Lambda Sigma = O((nu + c) lambda^2) (the mu_1 entries meet Sigma_11, Sigma_12 whose variance is <= c/K).
   [Sigma, Lambda] antisymmetric, s = Sigma_12 (mu_1 - mu_2), s^2/K = O(c lambda^2).  => s_2(4B) >= 1/8.
   So s_2(A) >= 1/32, s_1(A) >~ K/4 for A = M_IJ.
   Marginals (exact formula): alpha_i = sum_m p_m u_m(i)^2, p_m = s_m^2 e_1(s_{-m}^2)/e_2(s^2) <= s_m^2 (1/T + 1/S)
   for m >= 2 (S = s_1^2, T = ||A_res||_F^2, A_res = A - s_1 u_1 v_1'^T), so
       alpha_i <= u_1(i)^2 + share_i(A_res) + |row_i(A_res)|^2 / S.
   Davis-Kahan: sin angle(u_1, x^) <= 5/sigma_0 (sigma_0 = |mu_1||x||y|, x = v_{1I}, y = v_{1J}); so u_1(i)^2 tiny,
   |row_i(A_res)| <= |row_i(E)| + 5|x^_i| <= 2 (E = (M_{>=2})_IJ, ||E|| <= 1), entries of A_res <= sqrt(2c) + O(c + 1/K).
   ORIENTATION LEMMA on A_res (||A_res||_F >= s_2(A) >= 1/32, tiny entries): in one orientation all shares <= 0.6,
   so alpha <= 0.65 there.  D_2 with q = 1.3: decay |t|^{-1/1.3} = |t|^{-0.77} > 1/2.  Z_2 >= s_1^2 s_2^2 >= 1.

Conclusion if all steps survive audit: (H2') holds for every no-c-pivot M (c <= c_*) with >= 2 eigenvalues of
modulus >= 1, uniformly in b, c.  With (H1) this reduces the conjecture to (H3) alone.
TODO audit: (1) numerics for identity N^(h)_ij = -det M_{hi,hj} and the eigen-test; (2) random examples of
STEP B compression (huge spread square + O(1) second eigenvector + sub-threshold hub in M_3); (3) marginal
formula/bound; (4) Monte Carlo of the hub reduction on hub + small diagonal + dense remainder.

## Entry 7. Audit results (NUMERICAL) and constants

num/check_linalg2.py: 2-marginal formula alpha_i = (G_ii tr G - (G^2)_ii)/e_2(G), G = AA^T, vs brute force over all
2x2 minors: error <= 3e-15.  Identity N^(h)_ij = -det M_{hi,hj}: exact (0.0).  Eigen-test holds.
STEP B family (n = 500, K = 30..150, second eigenvalue +-1.2..1.8, sub-threshold hub 0.8-0.9, Wigner noise, zero
diagonal): over random partitions s_2(M_IJ) >= 0.59 (needed 1/32); best-orientation max 2-marginal <= 0.037;
bound alpha_i <= u_1(i)^2 + share_i(A_res) + |row_i(A_res)|^2/S never violated (max excess -2e-4 < 0);
max entry of A_res / ||A_res||_F <= 0.16.
num/check_hub_H2.py: exact conditional preimage lengths (no histogram), sup over 25 values of s, X_h uniform or on
three spread intervals, m = 60 leaves, L = <1/sqrt m, X'>:
   pure hub a = 0, 0.01, 0.1: 6.30, 6.33, 6.41 (uniform), 1.48, 1.49, 1.42 (spread);
   R' = theta L^2 with a theta = 0.25, 0.5, 0.9: 3.03, 2.40, 2.08;  dense eps W twists: 0.29 - 1.54.
No growth as a -> 0, none near the cancellation a theta -> 1.

Explicit constants (not optimised).  STEP B: c <= 1e-6, nu = 5e-5, eta = nu + 2c, K_0 = 1e4.
   Davis-Kahan in the form |lambda sin phi| = |z^T P u| <= ||P||: sin angle(u_1, x^) <= (2s0+1)/(s0^2-2s0-1) <= 3/s0.
   entries of A_res <= sqrt(2c) + 1.1 eta + 9 sqrt(eta/K) + 21/K <= 4.2e-3; ||A_res||_F >= 1/32; ratio^2 <= 0.018 <= 0.1.
   => one orientation with 2-marginals <= 0.551; D_2 at q = 1.2: |phi| <= 6.5 |t|^{-5/6}; small ball <= 84.8 u^{5/6};
   (H2') <= 128.
STEP A: K_0 = 1e4, rho = 3/(64(K_0+2)), nu_A = rho^2/2, c <= min(rho^2/(2(K_0+1)), nu_A/9) (~1e-15).  Universal.
Hub theorem: (H2') <= 5 + 21 K_Delta, K_Delta = 3.263 * (16.92/nu)^{1/3}.

## Entry 8. Push beyond the assignment: level 3 through the discriminant (PROVED, but weak)
For ANY coordinate h, given X' the conditional density of Q at s is (f_h(x_+) + f_h(x_-))/(2 sqrt Delta_s) <=
Delta_s^{-1/2} 1{Delta_s > 0}.  Hence  ||p_Q||_inf <= sup_{s'} E|Delta^(h) - s'|^{-1/2}  <= 1 + (H2')(Delta^(h)).
N^(h) has no pivot (entries <= 3c, its 2x2 minors <= 10 c^2).  So: if for SOME h the discriminant matrix
N^(h) = m_h m_h^T - m_hh M has two eigenvalues of modulus >= 1, Q has bounded density (by the (H2) theorem applied
to Delta^(h)).  But N^(h) = |m_h|^2-direction + O(|m_hh| ||M||): its second eigenvalue is >= 1 only if
|m_hh| |mu_k| >~ 1 for some eigenvalue transversal to m_h, i.e. only when M has an eigenvalue >~ 1/c.  For the
pure hub + rank one (a = 0) N = w w^T is rank one and this route gives nothing: the f_h(x_+-) factor, which it
discards, is exactly what Prop 5.4 uses.  So (H3) is NOT reduced to level 2 by this; it is a remark.

## Entry 9. Referee correction (RV Lemma 3.1 is a rearrangement bound, not pointwise) - checked
Nothing here uses a pointwise bound on |psi|.  Fourier steps use only the L^p lemma int|psi|^p <= 4 pi/sqrt p
(p >= 2) inside Brascamp-Lieb (Theorem 1 / D_1 at q in [1,2], D_2 at q = 1 and q = 1.2); real-variable steps use
Lemma 1.2(ii) and Esseen (Fejer kernel).  Ball's 1-D marginal bound appears only in sanity checks.

## Entry 10. Final constants, final status (the full report goes in the final message; the environment refuses
## REPORT.md for this folder)
num/check_Dk_q.py: D_1 at q = 3/2 (block with a row share 0.82): max ratio 0.28; D_2 at q = 1.2 (dominant rank one
+ O(1) second direction, max 2-marginal 0.48): max ratio 0.10.  No violation.
Lemma 6 re-derived with |mu_2| = 1 exactly: s_2(P) = |det P|/||P|| >= 0.99K/1.01K, so s_2(B) >= 0.225 (not 1/32);
entries of A_res <= 2.75e-3 at K = 1e4; orientation at h' = 0.51; marginals <= 0.52 (use 0.6 for margin).
Case split: c_* = 1e-15; STEP B: K > 1e4, nu = 5e-5, eta = nu + 3c (the (D') complement of the eigen-test at
threshold nu + 2c); STEP A: K <= 1e4, rho_A = 3/(64(K_0+2)), nu_A = rho_A^2/2.
STATUS: (H1') PROVED (Theorem A, only needs max|m_ii| <= 1/2 and ||M|| >= 1).  (H2') PROVED (Theorem C, no c_*-pivot).
Hence the conjecture is equivalent to (H3) for no-c-pivot matrices, for any one c > 0.
(H3) not touched beyond the discriminant remark (Entry 8).

## Entry 11. (H1) in the stronger alpha_1 form (PROVED)
Theorem A'. No c-pivot with c <= 1e-5, ||M|| >= 1  =>  alpha_1(Q) <= C (universal), uniformly in b, c.
Proof. O = off-diagonal part, F^2 = ||O||_F^2 >= (1-c)^2.  eps = 1/100.  Heavy set Hv = {i : r_i^2 > eps F^2},
|Hv| < 1/eps.  Force Hv into J; put each light coordinate in I or J by a fair coin.  Z = ||M_IJ||_F^2.
  E Z = (1/4) sum_{light-light} + (1/2) sum_{light-heavy} >= (F^2 - sum_{Hv x Hv} O_ij^2)/4 >= (F^2 - 2c/eps^2)/4.
  Efron-Stein: Z is affine in each xi_i with |dZ/dxi_i| <= r_i^2, so Var Z <= (1/4) sum_{i light} r_i^4 <= (eps/4) F^4.
  Chebyshev: P(Z < EZ/2) <= Var/(EZ/2)^2 <= 16 eps F^4/(F^2 - 2c/eps^2)^2 < 1 for c <= eps^2 F^2/8.
So some partition has Z >= F^2/9 with every I-row light: share <= eps F^2/Z <= 9 eps < 1/2.  D_1 at q = 1:
|phi| <= (2 pi e^{1/2} Z^{-1/2})^{1/2} |t|^{-1/2}; Esseen with decay exactly 1/2 has no log:
P(|Q-s| <= u) <= 1.0877 u * 2 * 2 B u^{-1/2} = 4.35 B sqrt(u),  B = (2 pi sqrt(e) * 3/F)^{1/2}.  QED.
(alpha_2 for (H2) is NOT claimed: the hub theorem gives only the half-power integrability.)

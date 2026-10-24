# NOTES - semidefinite forms (wave 2, piece 01)

## 0. Plan (written first)

Target: bounded density for PSD A with >= 3 eigenvalues >= 1, any rank, any linear terms.

Route: decision tree with 1x1 pivots only (PSD Schur complements are PSD, lose at most one
large eigenvalue, GEOM Lemma 1.5), leaves = no-pivot PSD matrices (all a_ii < c).
In the no-pivot PSD regime prove Hyp_1, Hyp_2, Hyp_3 by decoupling (Theorem D / D_k).

Key new tools (to be checked):
 (S) singular-value lemma for a random partition, via an exact identity;
 (M) volume-sampling marginal <= 2 x ridge leverage;
 (LR/HR) dichotomy: few eigenvalues >= theta (low rank at scale theta: marginals controlled
     by second moments in bounded dimension) versus many (use the marginal-free volumes
     k = 2, 4, 5 of D_k with q = 2).

## 1. Gram picture

A = B B^T, B = U Lambda^{1/2} (n x r, r = rank), B^T B = Lambda = diag(lambda_1..lambda_r) > 0.
Rows b_i in R^r, |b_i|^2 = a_ii.  PSD + no pivot  <=>  every |b_i|^2 < c.  THIS is the whole
point: rows of A can be huge ((A^2)_ii <= lambda_max a_ii), but rows of B are small.

Random partition: xi_i in {0,1} iid Bernoulli(1/2), eps_i = 2 xi_i - 1, I = {xi = 1}, J = {xi = 0}.
H_I = sum_{i in I} b_i b_i^T,  H_J = sum_{j in J} b_j b_j^T,  H_I + H_J = Lambda.
N := H_I - Lambda/2 = (1/2) sum_i eps_i b_i b_i^T,   H_J = Lambda/2 - N.
A_IJ = B_I B_J^T.

## 2. The identity (no cancellation problem)

For g in R^r put z = B_I g in R^I, x = B_J g in R^J. Then
   <z, A_IJ x> = g^T H_I H_J g = g^T (Lambda/2 + N)(Lambda/2 - N) g = |Lambda g|^2/4 - |N g|^2,
because the cross terms g^T(N Lambda - Lambda N) g vanish (commutator of symmetric matrices is
antisymmetric). Also |z|^2 |x|^2 = (g^T H_I g)(g^T H_J g) <= (g^T Lambda g / 2)^2 (AM-GM).

Courant-Fischer with F = B_J G (G a k-dim subspace of R^r):
   s_k(A_IJ) >= min_{g in G} (|Lambda g|^2/4 - |N g|^2) / (g^T Lambda g / 2).
(Injectivity of B_J on G follows: B_J g = 0 would make the left side 0 < |Lambda g|^2/8.)

Lemma S (PROVED, to be written in REPORT). Let A be PSD, max a_ii <= c, and let K be a set of
k eigen-indices with lambda_m >= theta. With probability >= 1 - 2kc/theta over the partition,
   s_k(A_IJ) >= theta/4.
Proof: G = span{e_m : m in K}. For g = sum theta_m e_m, |N g| <= |Lambda g| (sum_m |N e_m|^2/lambda_m^2)^{1/2}
(Cauchy-Schwarz). E|N e_m|^2 = (1/4) sum_i b_i(m)^2 |b_i|^2 <= (c/4) lambda_m (sum_i b_i(m)^2 = lambda_m).
So E sum_K |N e_m|^2/lambda_m^2 <= kc/(4 theta); Markov gives <= 1/8 with prob >= 1 - 2kc/theta.
Then |N g|^2 <= |Lambda g|^2/8 on G and s_k >= min |Lambda g|^2/(4 g^T Lambda g) >= theta/4.

Remark: nothing about the other eigenvalues (huge or tiny) enters. Dimension-free.

## 3. Marginal bound

k-volume sampling of M = A_IJ: alpha_i = sum_m p_m u_m(i)^2, p_m = sigma_m e_{k-1}(sigma_{-m})/e_k(sigma),
sigma_m = s_m(M)^2, u_m left singular vectors (complete basis, p = 0 on the kernel).
 (a) p_m <= 1 (e_k(sigma) = sigma_m e_{k-1}(sigma_{-m}) + e_k(sigma_{-m})).
 (b) e_k(mu) >= (mu_(k)/k) e_{k-1}(mu) for mu >= 0 (map each (k-1)-set T to T u {j}, j in top-k minus T;
     each k-set hit at most k times). Hence p_m <= k sigma_m / sigma_(k) for every m.
 (c) min(1,x) <= 2x/(1+x)  =>  p_m <= 2 sigma_m/(sigma_m + kappa) for any 0 < kappa <= sigma_(k)/k.
So  alpha_i <= 2 [G (G+kappa)^{-1}]_ii = 2 m_i^T (M^T M + kappa)^{-1} m_i   (ridge leverage of row i).
For M = B_I B_J^T: m_i^T(M^T M + kappa)^{-1} m_i = b_i^T H_J (H_I H_J + kappa)^{-1} b_i
   = b_i^T (H_I + kappa H_J^{-1})^{-1} b_i <= b_i^T (H_I + kappa Lambda^{-1})^{-1} b_i   (H_J <= Lambda).
Lemma M: alpha_i <= 2 b_i^T (H_I + kappa Lambda^{-1})^{-1} b_i for 0 < kappa <= s_k(A_IJ)^2/k.

## 4. Dichotomy at scale theta < 1

HR: >= k_* eigenvalues >= theta (k_* = 5, 4, 2 for levels 3, 2, 1). Lemma S with k_*: s_{k_*} >= theta/4,
    so Z_{k_*} >= (theta/4)^{2 k_*}; D_{k_*} with q = 2 needs NO marginal condition.
LR: at most k_* - 1 eigenvalues >= theta (K_b = those indices, |K_b| <= K_0 = k_* - 1), and >= k eigenvalues >= 1
    (k = 3, 2, 1). Lemma S with theta = 1: s_k >= 1/4; kappa := 1/(16k).
    rho := kappa/theta. H_I + kappa Lambda^{-1} >= H_I + rho P_s  (P_s = small coordinates, lambda < theta).
    Block inequality [[P,R],[R^T,S]] >= (P - 2 R S^{-1} R^T) (+) S/2  (difference is 2|S^{-1/2}R^T x + S^{1/2} y/2|^2).
    With H_bs = N_bs (Lambda diagonal):  H_I + rho P_s >= [Lambda_b/2 + N_bb - (2/rho) N_bs N_sb] (+) (rho/2) I_s.
    E1: ||Lambda_b^{-1/2} N_bb Lambda_b^{-1/2}||_F^2 <= 1/64: E = (1/4) sum_i l_i^2 <= (c/(4 theta)) K_0,
        l_i = |Lambda_b^{-1/2} b_i^b|^2 <= c/theta, sum_i l_i = |K_b|.
    E2: (2/rho) ||N_sb Lambda_b^{-1/2}||_F^2 <= 1/8: E ||..||_F^2 = (1/4) sum_i |b_i^s|^2 l_i <= c K_0/4.
    Under E1, E2: H_I + kappa Lambda^{-1} >= Lambda_b/4 (+) (rho/2) I_s, so
        alpha_i <= 8 l_i + (4/rho)|b_i^s|^2 <= max(8/theta, 4 theta/kappa) c.
    Failure prob <= 2kc + 16 c K_0/theta + 4 c K_0/rho = 2kc + 16cK_0/theta + 64 k K_0 c theta.
    Level 3 (k=3, K_0=4): theta = 1/(2 sqrt 3) = 0.2887 gives failure <= 449.4 c, alpha <= 55.4 c.

STATUS so far: Lemma S, Lemma M, LR/HR analysis written above in outline; numerics next.

## 5. Numerics round 1 (check_lemmas.py, stress_partition.py)

check_lemmas.py, 57 cases (n = 7..10, PSD with eigenvalues e^{U(-3,5)}, k = 1,2,3):
 identity error 5e-14 (relative); brute-force k-volume marginals vs sum p_m u_m(i)^2: 9e-12;
 p_m - k sigma_m/sigma_(k) <= 0 always; alpha_i - 2 ridge_i <= -1.3e-5 (never violated, nearly tight once);
 push-through identity 1e-12; ridge - b_i^T(H_I + kappa Lambda^{-1})^{-1} b_i <= -6.5e-4 (never violated).
stress_partition.py (n = 200, 600; huge + two, multiscale 2^j, flat projection, 3 + bulk, block indicators +
huge spread vector): s_3(A_IJ) always >= 0.45 lambda_3 or so; max 3-volume marginal <= 0.16. (These examples
have max a_ii up to 4, far outside the small-c regime of the theory, and are still fine.)

## 6. A proposed route and a simplification (NO dichotomy needed)

Proposed: U = top-3 eigenvectors, R = A - U Lambda U^T (PSD, <= lambda_3, R U = 0);
U^T P_I A P_J U = G_I Lambda G_J - U^T P_I R P_I U (because R P_J U = -R P_I U). Checked: correct.
The chaos U^T P_I R P_I U = U^T E R E U with E = diag(delta - 1/2) (linear terms vanish since R U = 0,
U^T R = 0); NOTE its mean is NOT zero: (1/4) sum_a u_k(a) u_l(a) R_aa, of size <= c/4 (harmless).
Their s_3 bound is equivalent to my Lemma S (mine is shorter: no split needed).
Their marginal step ("p_m ~ sigma_m^2/sigma_3^2 for m >= 4 and the R-part row norms <= lambda_3 c") has a gap:
the singular directions of A_IJ beyond the third are NOT the R-part; when lambda_1 >> lambda_3 and R has
eigenvalues ~ lambda_3 there is no spectral gap at 3 and sin-theta arguments fail. The ridge-leverage Lemma M
avoids the SVD entirely and closes it.

SIMPLIFICATION: in the LR analysis take K_b = the TOP k eigen-indices (not "all >= theta"). Every other
eigenvalue is <= lambda_k, so kappa Lambda^{-1} >= (kappa/lambda_k) P_s, rho = kappa/lambda_k. With
kappa = lambda_k^2/(16k) (allowed once s_k >= lambda_k/4): rho = lambda_k/(16k). Then
 E1: P(fail) <= 16 sum_i l_i^2 <= 16 k c/lambda_k   (l_i <= a_ii/lambda_k, sum l_i = k)
 E2: P(fail) <= 8 E[(2/rho)||N_sb Lambda_b^{-1/2}||_F^2] <= (4/rho) k c = 64 k^2 c/lambda_k
 S : P(fail) <= 2 k c/lambda_k
 marginals: alpha_i <= 8 l_i + (4/rho)|b_i^s|^2 <= 64 k a_ii/lambda_k <= 64 k c/lambda_k.
k = 3: failure <= 630 c/lambda_3, alpha <= 192 c/lambda_3. So c <= lambda_3/640 suffices. Then Theorem D:
Z_3 >= s_3^6 >= (lambda_3/4)^6 and ||p_Q|| <= 6 sqrt(e) * 4/lambda_3.
The high-rank case (D_5 without marginals) is NOT needed. Scale-invariant: condition is max a_ii <= lambda_k/640.

## 7. chain_check.py (flat Hadamard eigenvectors, n = 1024; killed at 600 s after 3 of 5 spectra)

Big block = top k. For every partition: whenever S <= 1/8 held, s_k >= lambda_k/4 held; whenever E1, E2 held,
2 ridge_i <= 8 l_i + (4/rho)|b_i^s|^2 held; alpha_i <= 2 ridge_i always. Empirical means of S, E1, E2 match the
exact expectation formulas used in the Markov steps (e.g. S 1.42e-3 vs 1.42e-3; E2 2.79e-2 vs 3.12e-2).
Examples with c/lambda_k ~ 0.003 (theory regime): conditions held 11-12/12, alpha_max <= 0.007 << chain bound.
Example 3 + 60 at 0.9 (c = 0.056, outside the theory regime): conditions failed, true alpha still <= 0.007.
(The script is slow because of per-row solves; not rerun. Enough for the deterministic chain.)

## 8. Constants (PSD, q = 1 decoupling)

Fejer kernel: P(|Z - s| <= u) <= (u/(2 sin^2 1)) int_{|t| <= 2/u} |phi| = 0.70614 u int ...
 (k(x) = (sin x/x)^2 >= sin^2 1 on [-1,1], hat k = pi (1 - |tau|/2)_+).
 |phi| <= B|t|^{-1/2}  =>  alpha_1 <= 3.995 B.   |phi| <= min(1, B/|t|), B >= 2  =>  alpha_2 <= 1.4123 B.
No-pivot PSD, thresholds: level 1 c_1 = 1/128 (failure 82c, marginal 64c), level 2 c_2 = 1/300 (292c, 128c),
level 3 c_3 = 1/640 (630c, 192c).
 H_1: |phi| <= e^{1/4}(2 pi)^{1/2} Z_1^{-1/4}|t|^{-1/2}, Z_1 >= (lambda_1/4)^2  =>  B <= 6.437, alpha_1 <= 25.71.
 H_2: |phi| <= e^{1/2}(2 pi) Z_2^{-1/4}|t|^{-1}, Z_2 >= (lambda_2/4)^4  =>  B <= 41.44, alpha_2 <= 58.52.
 H_3: Theorem D, Z_3 >= (lambda_3/4)^6  =>  ||p|| <= 6 sqrt(e) * 4 = 39.57.
Decision tree (1x1 pivots only; compositions C5, C2, C1):
 A_1 = max(4 c_1^{-1/2}, H_1) = 45.25;  A_2 = max(4 sqrt 2 c_2^{-1/2} A_1, H_2) = 4433;
 ||p_Q|| <= max(3 c_3^{-1/2} sqrt(A_2 (3 + log A_2)), H_3) = 75.9 * 224.8 = 1.71e4.
(C1 re-derived: sup_s E|s - xi|^{-1/2} <= V + K'(3 + 2 log V)/V, V = sqrt(K'(3 + log K')), total <= 3 sqrt(K'(3+log K')).)

## 9. Extension to indefinite matrices with small |M|-diagonal (to be checked)

M = B S B^T, B = U|Lambda|^{1/2}, S = sign; |b_i|^2 = |M|_ii (diagonal of (M^2)^{1/2}).
Lemma M carries over verbatim: alpha_i <= 2 b_i^T (H_I + kappa |Lambda|^{-1})^{-1} b_i (S H_J^{-1} S >= |Lambda|^{-1}).
Lemma S with mixed signs: test z = B_I S g, x = B_J g:
 <z, M_IJ x> = |Lambda g|^2/4 - (g_-^T|Lambda| N g_+ + g_+^T|Lambda| N g_-) - (S N S g)^T (N g)
 |z|^2 + |x|^2 = g^T|Lambda|g - 4 g_+^T N g_-.
 Conditions: sum_K |N e_m|^2/lambda_m^2 <= eta^2 and ||Lambda_G^{-1/2} N_GG Lambda_G^{-1/2}|| <= eta' give
 s_k >= theta (1/4 - eta - 2 eta^2)/(1/2 + eta').
So Hyp_k holds for every no-pivot M with max_i |M|_ii <= c_k' |lambda|_(k)(M): the open no-pivot configurations all
contain a coordinate with |M|_ii >= c_k' |lambda|_(k) and |m_ii| < c ("hub-like": positive and negative parts of
|M|^{1/2} both carry weight at i). A PSD row can be huge (a delocalized huge eigenvalue) without being hub-like.

## 10. mixed_sign_check.py (n = 512, flat Hadamard frames, spectra (1,1,-1), (1.3,-1,-1)+/-0.5 x20,
##     (2,1,-1)+/-0.2 x100, (1,-1,1,-1,1); 24 partitions, k = 1,2,3)
Identity <B_I S g, M_IJ B_J g> = |Lambda g|^2/4 - (g_-^T|L|N g_+ + g_+^T|L|N g_-) - (SNSg).(Ng): error 6e-16.
Identity |B_I S g|^2 + |B_J g|^2 = g^T|L|g - 4 g_+^T N g_-: error 5e-16.
Lemma S' (s_k >= theta(1/4 - eta - 2eta^2)/(1/2 + eta')): 0 violations / 72 (bound conservative: s_k/theta ~ 0.5,
bound 0.2-0.46 when the conditions are in their regime). Lemma M with |Lambda|: 0 violations / 72.

Constants for Proposition G (general signs, max_i |M|_ii <= c, k largest |lambda|, theta = |lambda|_(k)):
 eta = 1/16, eta' = 1/8  =>  s_k >= 0.2875 theta, kappa = 0.08266 theta^2/k, rho = 0.08266 theta/k,
 block beta = 2, eta_2 = 1/8, big block >= |Lambda_K|/4;
 failure <= (64k + 16k + 48.4k^2) c/theta  (k=3: 675.6 c/theta); alpha_i <= 48.4 k c/theta (k=3: 145.2 c/theta).
 => every symmetric M with max_i |M|_ii <= |lambda|_(3)(M)/680 satisfies the hypothesis of Theorem D.
 No pivot condition is needed for this; the hub-like coordinates are the only obstruction left for decoupling.

Corollary noted: rank three. Definite rank-3 forms (the "ellipsoid" side left open by Theorem C) are covered by
the PSD theorem with any linear terms. Rank three is now open only for indefinite forms on the two-sheet side.

====================================================================================================
# WRITE-UP (complete proofs). Sections W0-W8 below are the deliverable text.
====================================================================================================

## W0. Setting and results

X = (X_1..X_n) independent, X_i has density f_i <= 1 and characteristic function psi_i. For real symmetric A,
Q = X^T A X + b^T X + c, phi(t) = E exp(itQ). Eigenvalues lambda_1(A) >= lambda_2(A) >= ...; |lambda|_(k)(A) is
the k-th largest modulus. For a random variable Z: L_Z(u) = sup_s P(|Z - s| <= u),
alpha_1(Z) = sup_{u>0} L_Z(u)/sqrt(u), alpha_2(Z) = sup_{0<u<=1} L_Z(u)/(u(1 + log(1/u))), ||p_Z||_inf = sup of
its density. A_IJ = I x J block; s_1(M) >= s_2(M) >= ... singular values; e_k = k-th elementary symmetric polynomial.

THEOREM 1 (semidefinite forms). If A is positive semidefinite with lambda_3(A) >= 1, then for every b, c and every
independent X_i with densities <= 1:  ||p_Q||_inf <= C_0 := 1.71e4.  By scaling ||p_Q||_inf <= C_0/lambda_3(A) for
every PSD A with lambda_3 > 0; the same holds for negative semidefinite A (apply it to -Q). Rank, n and b arbitrary.

THEOREM 2 (lower levels). A PSD, b, c, X as above. (a) lambda_1(A) >= 1 => L_Q(u) <= 45.26 sqrt(u) for all u > 0.
(b) lambda_2(A) >= 1 => L_Q(u) <= 4435 u (1 + log(1/u)) for 0 < u <= 1.

PROPOSITION 3 (decoupling certificate). k in {1,2,3}, A PSD, lambda_k(A) > 0, and
   max_i a_ii <= lambda_k(A)/gamma_k,  gamma_1 = 128, gamma_2 = 300, gamma_3 = 640.
Then some partition [n] = I u J has s_k(A_IJ) >= lambda_k(A)/4 and all k-volume marginals of A_IJ on I at most
64 k max_i a_ii / lambda_k(A) <= 1/2. Consequently, uniformly in b, c, X:
  k=1: |phi(t)| <= 2 e^{1/4} (2pi)^{1/2} (lambda_1 |t|)^{-1/2};  k=2: |phi(t)| <= 8 pi e^{1/2} (lambda_2 |t|)^{-1};
  k=3: ||p_Q||_inf <= 24 sqrt(e)/lambda_3.

THEOREM 4 (indefinite A without hub-like coordinates). |A| = (A^2)^{1/2}, (|A|)_ii = sum_m |lambda_m| u_m(i)^2 >= |a_ii|.
If k in {1,2,3} and max_i (|A|)_ii <= |lambda|_(k)(A)/gamma'_k (gamma'_1 = 130, gamma'_2 = 360, gamma'_3 = 680), then some
partition has s_k(A_IJ) >= 0.2875 |lambda|_(k)(A) and k-volume marginals on I at most 1/2; hence
|phi(t)| <= e^{k/4}(2pi)^{k/2} (0.2875 |lambda|_(k))^{-k/2} |t|^{-k/2}, and for k = 3 ||p_Q|| <= 34.4/|lambda|_(3)(A).

COROLLARY 5 (what is left). Call i hub-like at level k for M if (|M|)_ii > |lambda|_(k)(M)/gamma'_k. The conjecture is
equivalent to the three no-pivot statements of the reduction theorem (W1.4) restricted to matrices with no c-pivot
and at least one hub-like coordinate at the relevant level. At such i, with |m_ii| < c, both the positive and the
negative part of |M|^{1/2} carry weight >= ((|M|)_ii - c)/2 at i, and the row of M has norm >= (|M|)_ii.

COROLLARY 6 (rank three). Semidefinite rank-three forms, with any linear terms (also outside the range), have
density <= C_0/lambda_3. With the one-sheet bound pi sqrt 2 for indefinite rank three, rank three is open only
for indefinite forms on the two-sheet side.

## W1. Tools (known; constants re-derived)

W1.1 Conditioning is lossless (P(Q in E) = E P(Q in E | X_K)); given X_K the form is a quadratic polynomial in the
other coordinates with quadratic part the principal block, and new linear/constant terms.
One coordinate: if a_ii = a > 0, Q = a (X_i - m(X_{-i}))^2 + R(X_{-i}), m affine, R quadratic with matrix A/a_ii.
Given X_{-i}, a(X_i - m)^2 has density (f_i(m+r) + f_i(m-r))/(2 sqrt(a w)) <= (a w)^{-1/2} at w > 0, 0 at w < 0. So
   p_Q(y) <= a^{-1/2} E|y - R(X_{-i})|^{-1/2}   (square-root profile with K = a^{-1/2} around xi = R).        (1.1)
Schur complements: A PSD, lambda_k(A) >= 1, a_ii > 0 => A/a_ii PSD with lambda_{k-1}(A/a_ii) >= 1. [PSD: y^T(A/a_ii)y =
min_x (x,y)^T A (x,y). Invertible A: (A/a_ii)^{-1} = (A^{-1})_{-i,-i}; eigenvalues nu_j of A^{-1} are <= 1 for
j >= n-k+1, interlacing gives mu_j <= nu_j <= 1 for the k-1 indices j = n-k+1..n-1, all mu_j > 0. Singular A: use
A + eps I and continuity (a_ii > 0).]

W1.2 THEOREM D_k (RESULTS.md Theorem D for k = 3; FOURIER report Section 1.2 with q = 1). I, J disjoint, M = A_IJ,
Z_k = e_k(M^T M) = sum_{|S|=|T|=k} det(M_ST)^2, w_ST = det(M_ST)^2/Z_k, alpha_i = P_w(i in S), beta_j = P_w(j in T).
If alpha_i <= 1/2 for all i in I, then |phi(t)|^2 <= e^{k/2} (2pi)^k |t|^{-k} Z_k^{-1/2} for all b, c, X; for k = 3,
||p_Q||_inf <= 6 sqrt(e) Z_3^{-1/6}.
Proof. (i) Decoupling: condition on X_K (K = complement of I u J); Cauchy-Schwarz in X_I and an independent copy X_J'
give |phi(t)|^2 <= sup E_W prod_{i in I} |psi_i(2t (MW)_i)|, W = X_J - X_J' (independent coordinates, densities
g_j = f_j * f_j(-.) <= 1); A_II, A_JJ and all linear terms drop out. (ii) Brascamp-Lieb with exponents alpha_i on
the maps w -> <m_i, w> and 1 - beta_j on w -> w_j (sum alpha + sum (1-beta) = |J|); drop rows with alpha_i = 0 and
columns with beta_j = 1. Lieb: constant = sup_{d>0} (prod d_i^{alpha_i} prod d_j^{1-beta_j} / det(D_J + M^T D_I M))^{1/2},
D_I = diag(alpha_i d_i), D_J = diag((1-beta_j) d_j). (iii) det(D_J + M^T D_I M) = sum_{S,T} det(M_ST)^2 prod_S (alpha_i d_i)
prod_{j notin T} (1-beta_j) d_j (diagonal-plus-PSD expansion and Cauchy-Binet) >= Z_k prod (alpha_i d_i)^{alpha_i}
prod ((1-beta_j) d_j)^{1-beta_j} (weighted AM-GM with weights w_ST); the d's cancel: constant <= Z_k^{-1/2}
prod alpha_i^{-alpha_i/2} prod (1-beta_j)^{-(1-beta_j)/2}. (iv) int |psi|^p <= 4 pi/sqrt(p) for p >= 2 (RESULTS
Lemma 1: Rogozin + Ball); with p = 1/alpha_i, ||h_i||_{1/alpha_i} <= ((2|t|)^{-1} 4 pi alpha_i^{1/2})^{alpha_i}, h_i = |psi_i(2t .)|;
||g_j||_{1/(1-beta_j)} <= 1; the alpha^{alpha/2} cancel; prod (1-beta)^{-(1-beta)/2} <= e^{sum beta/2} = e^{k/2}.
For k = 3, |phi| <= min(1, B|t|^{-3/2}), B = (2pi)^{3/2} e^{3/4} Z_3^{-1/4}, ||p_Q|| <= (2pi)^{-1} int |phi| = (3/pi) B^{2/3}. []

W1.3 LEMMA 1.1 (Fejer). L_Z(u) <= (u/(2 sin^2 1)) int_{|t| <= 2/u} |phi_Z| <= 0.70615 u int_{|t|<=2/u} |phi_Z|.
[k(x) = (sin x/x)^2 >= sin^2 1 on [-1,1]; int k(x) e^{i tau x} dx = pi(1 - |tau|/2)_+ (checked by quadrature);
P(|Z-s| <= u) <= E k((Z-s)/u)/sin^2 1 and Fourier inversion.] Hence |phi_Z| <= B|t|^{-1/2} => alpha_1(Z) <= 3.9946 B;
|phi_Z| <= min(1, B/|t|), B >= 2 => alpha_2(Z) <= 1.4123 B (for u < 2/B the integral is 2B(1 + log(2/(uB)))
<= 2B(1 + log(1/u)); for 2/B <= u <= 1, L <= 1 <= (B/2)u).

W1.4 LEMMA 1.2 (compositions; GEOM Section 3.1). Q has a square-root profile with constant K around xi.
 (C5) alpha_1(Q) <= 4K.  [int_{|y-s|<=u} |y-d|^{-1/2} dy <= 4 sqrt(u).]
 (C2) alpha_1(xi) <= K' => alpha_2(Q) <= 4 sqrt(2) K max(K',1).  [int_{-u}^u |y+d|^{-1/2} <= 4 sqrt(2) u max(|d|,u)^{-1/2};
      E max(|Z|,u)^{-1/2} = int_0^{u^{-1/2}} P(|Z| < v^{-2}) dv <= int_0^{u^{-1/2}} min(1, K'/v) dv <= max(K',1)(1 + log(1/u)/2).]
 (C1) alpha_2(xi) <= K', K' >= 1 => ||p_Q|| <= 3K (K'(3 + log K'))^{1/2}.  [sup_s E|s - xi|^{-1/2} <= V + K'(3 + 2 log V)/V,
      V = (K'(3 + log K'))^{1/2}; checked numerically in constants.py.]
Reduction (GEOM Theorems 5.1-5.2): the conjecture is equivalent to bounds, uniform in linear/constant terms, for
matrices with no c-pivot (|m_ii| < c, all 2x2 principal minors < c): alpha_1 <= H_1 if |lambda|_(1) >= 1, alpha_2 <= H_2
(or the integrability form) if |lambda|_(2) >= 1, ||p|| <= H_3 if |lambda|_(3) >= 1. For PSD matrices only 1x1 pivots
are needed: m_ii < c forces every 2x2 principal minor into [0, c^2).

## W2. The Gram picture and the partition identity

Let A be PSD of rank r, A = sum_{m <= r} lambda_m u_m u_m^T (lambda_m > 0), and B = U Lambda^{1/2} (n x r), so that
   A = B B^T,   B^T B = Lambda = diag(lambda_1, ..., lambda_r),   |b_i|^2 = a_ii   (b_i = i-th row of B).
Rows of A may be huge ((A^2)_ii <= lambda_1 a_ii), but the rows of B are controlled by the diagonal alone. This is the
only place where semidefiniteness is used.

Partitions. Let eps_1, ..., eps_n be independent uniform signs, I = {eps = +1}, J = {eps = -1}, and
   H_I = sum_{i in I} b_i b_i^T,  H_J = sum_{j in J} b_j b_j^T,  N = (1/2) sum_i eps_i b_i b_i^T,
so H_I = Lambda/2 + N, H_J = Lambda/2 - N, H_I + H_J = Lambda, and A_IJ = B_I B_J^T (B_I = rows of B in I).

LEMMA 2.1 (identity). For every g in R^r,  <B_I g, A_IJ B_J g> = |Lambda g|^2/4 - |N g|^2,  and
(g^T H_I g)(g^T H_J g) <= (g^T Lambda g/2)^2.
Proof. <B_I g, B_I B_J^T B_J g> = g^T H_I H_J g = g^T (Lambda/2 + N)(Lambda/2 - N) g
= |Lambda g|^2/4 - |Ng|^2 + (1/2)(g^T N Lambda g - g^T Lambda N g), and the last bracket is zero because both terms
equal the scalar (Lambda g).(N g). The second claim is AM-GM with g^T H_I g + g^T H_J g = g^T Lambda g. []

LEMMA 2.2 (singular values). Let K be a set of k indices with lambda_m >= theta for m in K, G = span{e_m : m in K}.
If  S_K := sum_{m in K} |N e_m|^2 / lambda_m^2 <= 1/8,  then s_k(A_IJ) >= theta/4. If max_i a_ii <= c, then
E S_K <= k c/(4 theta), so P(S_K > 1/8) <= 2 k c/theta.
Proof. For g = sum_{m in K} g_m e_m, Cauchy-Schwarz gives |N g| <= sum |g_m| |N e_m| <= |Lambda g| S_K^{1/2}, so
|N g|^2 <= |Lambda g|^2/8. By Lemma 2.1, <B_I g, A_IJ B_J g> >= |Lambda g|^2/8 > 0 for g != 0 in G; in particular
B_J is injective on G and F = B_J G has dimension k. For x = B_J g in F, |A_IJ x| >= <B_I g, A_IJ x>/|B_I g|, so
   |A_IJ x| / |x| >= (|Lambda g|^2/8) / (|B_I g| |B_J g|) >= (|Lambda g|^2/8)/(g^T Lambda g/2) = |Lambda g|^2/(4 g^T Lambda g) >= theta/4,
since |Lambda g|^2 = sum g_m^2 lambda_m^2 >= theta sum g_m^2 lambda_m. Courant-Fischer (s_k(M) = max over k-dimensional
F of min_{x in F} |Mx|/|x|) gives s_k(A_IJ) >= theta/4. For the expectation: N e_m = (1/2) sum_i eps_i b_i(m) b_i, so
E|N e_m|^2 = (1/4) sum_i b_i(m)^2 |b_i|^2 <= (c/4) sum_i b_i(m)^2 = (c/4) lambda_m (column m of B has squared norm
lambda_m), and E S_K <= (c/4) sum_{m in K} 1/lambda_m <= kc/(4 theta). Markov. []

Remarks. (a) The other eigenvalues of A, however large or small, enter only through |b_i|^2 <= c: there is no
cancellation between the leading part and the rest, because the test vectors B_I g, B_J g are built from all of B.
(b) The statement is dimension-free; no matrix concentration inequality with a dimensional factor is used.
(c) Applying the lemma to K = {1..j} for j = 1..k gives s_j(A_IJ) >= lambda_j/4 simultaneously with probability
>= 1 - 2c sum_{j<=k} j/lambda_j, hence Z_k >= prod_{j<=k} (lambda_j/4)^2 (the scale-invariant form).

## W3. Volume-sampling marginals are ridge leverages

Let M be p x q, sigma_1 >= sigma_2 >= ... >= 0 the eigenvalues of G = M M^T (sigma_m = s_m(M)^2), u_1, ..., u_p an
orthonormal eigenbasis, and k <= rank M. By Cauchy-Binet sum_T det(M_ST)^2 = det(G_SS), so the I-marginal of the
k-volume weight is the marginal of k-volume sampling of rows with kernel G, and
   alpha_i = sum_m p_m u_m(i)^2,    p_m = sigma_m e_{k-1}(sigma_{-m}) / e_k(sigma)                                (3.1)
(differentiate sum_{|S|=k} det(G_SS) prod_{j in S} z_j = [x^k] det(I + x D_z G) in z_i at z = 1; checked against
brute-force enumeration to 1e-11).

LEMMA 3.1. For every m, p_m <= min(1, k sigma_m/sigma_k). Hence for every 0 < kappa <= sigma_k/k,
   alpha_i <= 2 [G (G + kappa)^{-1}]_ii = 2 m_i^T (M^T M + kappa)^{-1} m_i,        m_i = i-th row of M.
Proof. p_m <= 1 because e_k(sigma) = sigma_m e_{k-1}(sigma_{-m}) + e_k(sigma_{-m}). For mu >= 0 with at least k
entries, e_k(mu) >= (mu_(k)/k) e_{k-1}(mu), mu_(k) the k-th largest entry: send each (k-1)-set T to T u {j(T)} with
j(T) a top-k index outside T (so mu_{j(T)} >= mu_(k)); each k-set is hit at most k times. If m is not among the k
largest, sigma_{-m} has k-th largest entry sigma_k, so p_m <= sigma_m e_{k-1}(sigma_{-m})/e_k(sigma_{-m})
<= k sigma_m/sigma_k; if it is, p_m <= 1 <= sigma_m/sigma_k. Next min(1, x) <= 2x/(1 + x) for x >= 0, which with
x = k sigma_m/sigma_k gives p_m <= 2 sigma_m/(sigma_m + sigma_k/k) <= 2 sigma_m/(sigma_m + kappa). Sum against u_m(i)^2.
The last equality is the push-through identity M^T (M M^T + kappa)^{-1} = (M^T M + kappa)^{-1} M^T. []

LEMMA 3.2. For M = A_IJ = B_I B_J^T and i in I, with b_i the row of B,
   m_i^T (M^T M + kappa)^{-1} m_i = b_i^T H_J (H_I H_J + kappa)^{-1} b_i <= b_i^T (H_I + kappa Lambda^{-1})^{-1} b_i.
Proof. m_i = B_J b_i and M^T M = B_J H_I B_J^T. From (B_J H_I B_J^T + kappa) B_J = B_J (H_I H_J + kappa) (and
H_I H_J + kappa is invertible: the spectrum of H_I H_J is that of H_J^{1/2} H_I H_J^{1/2}, nonnegative) we get
B_J^T (B_J H_I B_J^T + kappa)^{-1} B_J = H_J (H_I H_J + kappa)^{-1}. If H_J is invertible this equals
(H_I + kappa H_J^{-1})^{-1}, and H_J <= Lambda gives H_J^{-1} >= Lambda^{-1}, so it is <= (H_I + kappa Lambda^{-1})^{-1}.
In general replace H_J by H_J + eta I (<= Lambda + eta I) and let eta -> 0; both sides are continuous. []

COROLLARY 3.3. If s_k(A_IJ) >= theta_* > 0 then, with kappa = theta_*^2/k,
   alpha_i <= 2 b_i^T (H_I + kappa Lambda^{-1})^{-1} b_i    for every i in I.
(Checked numerically on 57 random multi-scale examples: never violated, nearly attained once.)

## W4. Proof of Proposition 3

Fix k in {1,2,3}, A PSD with lambda_k := lambda_k(A) > 0 and c := max_i a_ii <= lambda_k/gamma_k. Order the
eigenvalues decreasingly and let K_b = {1, ..., k} (the TOP k indices), K_s = {k+1, ..., r}; every m in K_s has
lambda_m <= lambda_k. Write vectors and matrices in blocks b/s accordingly: b_i = (b_i^b, b_i^s), Lambda_b, Lambda_s,
N_bb, N_bs, N_sb, N_ss. Put
   kappa = lambda_k^2/(16 k),   rho = kappa/lambda_k = lambda_k/(16 k),   l_i = |Lambda_b^{-1/2} b_i^b|^2 = sum_{m<=k} u_m(i)^2.
Then l_i <= |b_i^b|^2/lambda_k <= c/lambda_k and sum_i l_i = k.

Three events:
 (S)  S_K := sum_{m <= k} |N e_m|^2/lambda_m^2 <= 1/8;
 (E1) ||Lambda_b^{-1/2} N_bb Lambda_b^{-1/2}||_F^2 <= 1/64;
 (E2) (2/rho) ||N_sb Lambda_b^{-1/2}||_F^2 <= 1/8        (vacuous if K_s is empty).

LEMMA 4.1 (block inequality). For symmetric [[P, R], [R^T, T]] with T > 0 (positive definite),
[[P, R], [R^T, T]] >= [[P - 2 R T^{-1} R^T, 0], [0, T/2]].
Proof. The difference is [[2 R T^{-1} R^T, R], [R^T, T/2]], whose quadratic form at (x, y) is
2 |T^{-1/2} R^T x + T^{1/2} y/2|^2 >= 0. []

Step 1 (s_k). Under (S), Lemma 2.2 with K = K_b and theta = lambda_k gives s_k(A_IJ) >= lambda_k/4, so kappa <=
s_k^2/k and Corollary 3.3 applies: alpha_i <= 2 b_i^T (H_I + kappa Lambda^{-1})^{-1} b_i.

Step 2 (lower bound for H_I + kappa Lambda^{-1}). Since Lambda is diagonal, (H_I)_bs = N_bs, and
kappa Lambda^{-1} >= 0 (+) (kappa/lambda_k) I_s = 0 (+) rho I_s because lambda_m <= lambda_k on K_s. Hence, with Lemma 4.1
applied to H_I + rho P_s (T = (H_I)_ss + rho I >= rho I),
   H_I + kappa Lambda^{-1} >= [Lambda_b/2 + N_bb - 2 N_bs ((H_I)_ss + rho)^{-1} N_sb] (+) ((H_I)_ss + rho)/2
                          >= [Lambda_b/2 + N_bb - (2/rho) N_bs N_sb] (+) (rho/2) I_s.
Under (E1), Lambda_b^{-1/2} N_bb Lambda_b^{-1/2} >= -(1/8) I; under (E2), (2/rho) Lambda_b^{-1/2} N_bs N_sb Lambda_b^{-1/2} <= (1/8) I
(its operator norm is at most its trace (2/rho)||N_sb Lambda_b^{-1/2}||_F^2). So H_I + kappa Lambda^{-1} >= (Lambda_b/4) (+) (rho/2) I_s.

Step 3 (marginals). Therefore, for i in I,
   alpha_i <= 2 (4 l_i + (2/rho)|b_i^s|^2) = 8 l_i + (64 k/lambda_k)|b_i^s|^2 <= (8/lambda_k)|b_i^b|^2 + (64k/lambda_k)|b_i^s|^2
           <= 64 k a_ii/lambda_k <= 64 k/gamma_k <= 1/2.

Step 4 (probabilities). E|N e_m|^2 <= (c/4) lambda_m gives P(not S) <= 2kc/lambda_k (Lemma 2.2).
Lambda_b^{-1/2} N_bb Lambda_b^{-1/2} = (1/2) sum_i eps_i v_i v_i^T with |v_i|^2 = l_i, so its expected squared Frobenius norm is
(1/4) sum_i l_i^2 <= (1/4)(c/lambda_k) k and P(not E1) <= 16 k c/lambda_k.
N_sb Lambda_b^{-1/2} = (1/2) sum_i eps_i b_i^s (Lambda_b^{-1/2} b_i^b)^T has expected squared Frobenius norm
(1/4) sum_i |b_i^s|^2 l_i <= (c/4) k, so P(not E2) <= 8 (2/rho)(ck/4) = 4ck/rho = 64 k^2 c/lambda_k.
Total failure probability <= (18 k + 64 k^2) c/lambda_k = 82/gamma_1, 292/gamma_2, 630/gamma_3 for k = 1, 2, 3, i.e.
0.641, 0.973, 0.984 < 1. So a partition in S n E1 n E2 exists.

Step 5 (Fourier bounds). For that partition Z_k = e_k(A_IJ^T A_IJ) >= s_k(A_IJ)^{2k} >= (lambda_k/4)^{2k} and all
I-marginals are <= 1/2, so Theorem D_k applies: |phi(t)|^2 <= e^{k/2}(2pi)^k |t|^{-k} (lambda_k/4)^{-k}. This is the
displayed bound for k = 1, 2; for k = 3, ||p_Q|| <= 6 sqrt(e) (lambda_3/4)^{-1} = 24 sqrt(e)/lambda_3. []

Remark 4.2 (why the top k, and why no high-rank case is needed). The small block K_s may have huge dimension and
eigenvalues as large as lambda_k; it enters only through the ridge rho ~ lambda_k/k, and each coordinate's
contribution is |b_i^s|^2/rho <= 16 k a_ii/lambda_k. The big block has dimension k, so second moments suffice there.
In particular no separate treatment of matrices with many eigenvalues of size comparable to lambda_k is needed (the
marginal-free volumes D_5, D_4, D_2 with q = 2 would give an alternative route in that regime).

Remark 4.3 (constants are not optimized). With eta-parameters (Lemma 2.2 threshold 1/16 instead of 1/8, block
parameter beta = 2 and E1 threshold 1/8 in operator norm, E2 threshold 1/4) the level-3 threshold improves to about
gamma_3 = 190; the final constant would improve accordingly. Not pursued.

## W5. Proof of Theorems 1 and 2 (decision tree with 1x1 pivots)

Thresholds c_1 = 1/128, c_2 = 1/300, c_3 = 1/640 (= 1/gamma_k). All matrices below are PSD; by W1.1 every Schur
complement of a PSD matrix at a positive diagonal entry is PSD and loses at most one eigenvalue >= 1.

Level 1. A PSD with lambda_1(A) >= 1. If some a_ii >= c_1, (1.1) gives a square-root profile with K = a_ii^{-1/2}
<= c_1^{-1/2} and (C5) gives alpha_1(Q) <= 4 c_1^{-1/2} = 45.26. Otherwise max a_ii < c_1 <= lambda_1/128 and
Proposition 3 (k = 1) gives |phi(t)| <= B_1 |t|^{-1/2}, B_1 = 2 e^{1/4} (2pi)^{1/2} = 6.437, so alpha_1(Q) <= 3.9946 B_1
= 25.71 by Lemma 1.1. Hence alpha_1(Q) <= A_1 := 45.26 for every PSD A with lambda_1 >= 1 and every linear term.
This is Theorem 2(a).

Level 2. A PSD with lambda_2(A) >= 1. If some a_ii >= c_2, (1.1) gives a profile with K <= c_2^{-1/2} around
xi = R(X_{-i}), a quadratic polynomial whose matrix A/a_ii is PSD with lambda_1 >= 1; by level 1, alpha_1(xi) <= A_1,
and (C2) gives alpha_2(Q) <= 4 sqrt(2) c_2^{-1/2} A_1 = 4434.05. Otherwise Proposition 3 (k = 2) gives
|phi(t)| <= min(1, B_2/|t|), B_2 = 8 pi e^{1/2} = 41.44, and Lemma 1.1 gives alpha_2(Q) <= 58.52. Hence
alpha_2(Q) <= A_2 := 4434.05 < 4435. This is Theorem 2(b).

Level 3. A PSD with lambda_3(A) >= 1. If some a_ii >= c_3, (1.1) gives a profile with K <= c_3^{-1/2} = 25.30 around
xi with matrix A/a_ii (PSD, lambda_2 >= 1), so alpha_2(xi) <= A_2 by level 2 and (C1) gives
||p_Q|| <= 3 c_3^{-1/2} (A_2 (3 + log A_2))^{1/2} = 17061.1. Otherwise Proposition 3 (k = 3) gives
||p_Q|| <= 24 sqrt(e) = 39.57. Hence ||p_Q||_inf <= 1.71e4. This is Theorem 1. []

Which step uses which result:
 - square-root profiles and Schur complements: W1.1 (GEOM Lemmas 1.1, 1.2, 1.5);
 - leaves (no heavy diagonal): Proposition 3 = Lemma 2.2 (new) + Corollary 3.3 (new: Lemmas 3.1, 3.2) + Lemma 4.1
   and the second-moment events (new) + Theorem D_k with q = 1 (RESULTS Theorem D, FOURIER Section 1.2);
 - Fourier to concentration: Lemma 1.1 (Fejer kernel);
 - composition along the tree: (C5), (C2), (C1) (GEOM Section 3.1, re-derived in W1.4).
 - Nothing else: no 2x2 pivots, no hub propositions, no Fresnel linearisation.
All constants recomputed in constants.py (C = 17061.14).

Scaling. For PSD A with lambda_3 > 0 apply the theorem to A/lambda_3 and Q/lambda_3: p_Q(y) = lambda_3^{-1}
p_{Q/lambda_3}(y/lambda_3), so ||p_Q|| <= C_0/lambda_3. Negative semidefinite: -Q has matrix -A (PSD) and the same
density up to reflection.

Remark 5.1 (the case left open in the rank-three analysis). A rank-three PSD form with one coordinate of leverage
>= 1/50 and linear terms outside the range was reduced in GEOM Section 4 to "the e_2 version of the Fourier bound for
a rank-two PSD form with linear terms outside its range". That is exactly level 2 above: after the pivot the Schur
complement is PSD of rank two with lambda_2 >= 1, and either it has another heavy coordinate (pivot) or
Proposition 3 with k = 2 applies; decoupling removes the linear terms, wherever they point.

## W6. Indefinite matrices: proof of Theorem 4 and Corollary 5

Let A be symmetric of rank r, A = sum_m lambda_m u_m u_m^T, S = diag(sign lambda_m), B = U |Lambda|^{1/2}. Then
A = B S B^T, B^T B = |Lambda|, |b_i|^2 = (|A|)_ii =: d_i. With the same random partition, H_I = |Lambda|/2 + N,
H_J = |Lambda|/2 - N, N = (1/2) sum eps_i b_i b_i^T, and A_IJ = B_I S B_J^T. For g in R^r write g = g_+ + g_-, g_+
supported on {S = +1}.

LEMMA 6.1 (identities). (a) <B_I S g, A_IJ B_J g> = |Lambda g|^2/4 - (g_-^T |Lambda| N g_+ + g_+^T |Lambda| N g_-) - (SNSg).(Ng).
(b) |B_I S g|^2 + |B_J g|^2 = g^T |Lambda| g - 4 g_+^T N g_-.
Proof. (a) The left side is g^T (S H_I S) H_J g and S H_I S = |Lambda|/2 + S N S (S commutes with |Lambda|). Expanding,
g^T(|Lambda|/2 + SNS)(|Lambda|/2 - N) g = |Lambda g|^2/4 + (1/2)[g^T SNS |Lambda| g - g^T |Lambda| N g] - g^T SNSN g, and with
S g = g_+ - g_-, |Lambda| S g = Lambda g, the bracket equals -2(g_-^T|Lambda|N g_+ + g_+^T|Lambda|N g_-) (the g_+g_+ and
g_-g_- terms cancel as in Lemma 2.1). (b) (Sg)^T H_I (Sg) + g^T H_J g = g^T|Lambda|g + (Sg)^T N (Sg) - g^T N g and
(g_+ - g_-)^T N (g_+ - g_-) - (g_+ + g_-)^T N (g_+ + g_-) = -4 g_+^T N g_-. [Both checked numerically to 6e-16.] []

LEMMA 6.2 (singular values, mixed signs). Let K be a set of k indices with |lambda_m| >= theta on K, G = span{e_m: m in K},
N~ = |Lambda_K|^{-1/2} N_KK |Lambda_K|^{-1/2}. If (S1) sum_{m in K} |N e_m|^2/lambda_m^2 <= eta^2 and (S2) ||N~|| <= eta', then
s_k(A_IJ) >= theta (1/4 - eta - 2 eta^2)/(1/2 + eta'). If max_i d_i <= c, E(S1 sum) <= kc/(4 theta) and
E ||N~||_F^2 = (1/4) sum_i l_i^2 <= kc/(4 theta), l_i = sum_{m in K} b_i(m)^2/|lambda_m| <= d_i/theta, sum_i l_i = k.
Proof. For g in G, g_+ and g_- lie in G and |N g_pm| <= eta |Lambda g_pm| (Cauchy-Schwarz as in Lemma 2.2). The cross term
in 6.1(a) is at most 2 eta |Lambda g_+||Lambda g_-| <= eta |Lambda g|^2; the last term is at most |N S g||N g|
<= (sqrt 2 eta |Lambda g|)^2. So the left side of 6.1(a) is >= (1/4 - eta - 2 eta^2)|Lambda g|^2 > 0 (for eta = 1/16).
In 6.1(b), |4 g_+^T N g_-| = 4 |(|Lambda|^{1/2} g_+)^T N~ (|Lambda|^{1/2} g_-)| <= 2 eta' g^T|Lambda| g, so
|B_I S g| |B_J g| <= (1/2 + eta') g^T|Lambda|g. As in Lemma 2.2, B_J is injective on G, and Courant-Fischer with
F = B_J G and the test vector B_I S g gives s_k >= min_G (1/4 - eta - 2eta^2)|Lambda g|^2/((1/2+eta') g^T|Lambda| g),
and |Lambda g|^2 >= theta g^T|Lambda|g on G. Expectations as in Lemma 2.2 and W4 Step 4. []

Proof of Theorem 4. K = indices of the k largest |lambda_m|, theta = |lambda|_(k)(A), c = max_i d_i <= theta/gamma'_k.
eta = 1/16, eta' = 1/8: under S1, S2, s_k(A_IJ) >= tau := 0.2875 theta; P(not S1) <= 64 kc/theta, P(not S2) <=
P(||N~||_F^2 > 1/64) <= 16 kc/theta.
Marginals. With M = A_IJ, m_i = B_J S b_i and M^T M = B_J (S H_I S) B_J^T, so as in Lemma 3.2
m_i^T(M^T M + kappa)^{-1} m_i = (Sb_i)^T H_J (S H_I S H_J + kappa)^{-1} (S b_i) <= (S b_i)^T (S H_I S + kappa|Lambda|^{-1})^{-1} (S b_i)
= b_i^T (H_I + kappa |Lambda|^{-1})^{-1} b_i. With kappa = tau^2/k (allowed by Lemma 3.1) and rho = kappa/theta = 0.08266 theta/k,
every m outside K has |lambda_m| <= theta, so kappa|Lambda|^{-1} >= 0 (+) rho I_s, and W4 Step 2 (with |Lambda| in place of
Lambda; (|Lambda|/2)_Ks = 0) gives, under S2 and (E2) (2/rho)||N_sK |Lambda_K|^{-1/2}||_F^2 <= 1/8,
H_I + kappa|Lambda|^{-1} >= |Lambda_K|/4 (+) (rho/2) I_s and alpha_i <= 8 l_i + (4/rho)|b_i^s|^2 <= 48.39 k d_i/theta.
P(not E2) <= 8 (2/rho)(kc/4) = 48.39 k^2 c/theta. Failure total (80 k + 48.39 k^2) c/theta: 128.4/130, 353.6/360,
675.5/680 < 1; marginals <= 48.39 k/gamma'_k = 0.372, 0.269, 0.214. Theorem D_k with Z_k >= tau^{2k} gives the bounds. []

Proof of Corollary 5. Let M have no c-pivot and |lambda|_(k)(M) >= 1. If no coordinate is hub-like at level k,
Theorem 4 and Lemma 1.1 give, uniformly in linear terms, alpha_1(R) <= 3.9946 * 1.2840 * (2pi)^{1/2} * 0.2875^{-1/2}
= 23.98 (k = 1), alpha_2(R) <= 1.4123 * e^{1/2} * 2pi/0.2875 = 50.89 (k = 2), ||p_R|| <= 34.41 (k = 3). These are the
leaf hypotheses of the reduction theorem (GEOM 5.1; the alpha-forms imply the integrability forms of GEOM 5.2 by
the layer-cake Lemma 1.6 there). So the decision tree needs a hypothesis only at leaves with a hub-like coordinate;
conversely the conjecture implies the leaf statements for all matrices (GEOM 5.2, necessity). For the properties of
a hub-like i: d_i = |b_i^+|^2 + |b_i^-|^2 and m_ii = |b_i^+|^2 - |b_i^-|^2, and (M^2)_ii = sum lambda_m^2 u_m(i)^2 >=
(sum |lambda_m| u_m(i)^2)^2 = d_i^2 by Cauchy-Schwarz (sum_m u_m(i)^2 <= 1). []

Remarks. (a) A PSD coordinate is never hub-like when a_ii < c <= 1/gamma'_k; a PSD row can nevertheless be huge
(a delocalized eigenvector with a huge eigenvalue), so the row norm is the wrong measure of a hub: the diagonal of
|M| is the right one. (b) The star 2 X_h <w, X> (|w| = 1) has (|M|)_hh = 1: its hub is hub-like, as it must be, since
decoupling provably loses half of its decay. So Corollary 5 isolates exactly the configurations in which decoupling
is not enough; hubs coupled to general remainders (the open configurations of hubs with a dense remainder or a nonzero diagonal) are among them, and nothing else is.

## W7. Numerical checks (scripts in this folder; numpy/scipy, BelowNormal, each < 10 min)

- check_lemmas.py: identity of Lemma 2.1 to 5e-14; marginal formula (3.1) against brute-force enumeration of all
  k x k minors (k = 1, 2, 3; 7-10 dimensional multi-scale PSD matrices) to 9e-12; Lemma 3.1, the push-through identity
  and the monotonicity of Lemma 3.2 never violated in 57 cases.
- negative_controls.py and control_c_targeted.py: deliberately wrong variants fail - the identity without -|Ng|^2
  (72/72), Lemma 3.1 without the factor 2 (177/216), p_m <= sigma_m/sigma_k (60/216), Lemma 2.2 with theta/1.2 in place of
  theta/4 (84/84), Lambda/4 in the monotonicity (207/216). The variant kappa = sigma_k (instead of sigma_k/k) is never
  violated by random matrices but fails on a targeted example (three equal top singular values, a small direction
  localized on one row: alpha = 0.2126 > 0.1651), while the proved bound holds (0.4252); alpha matches 3eps^2/(1+3eps^2).
- chain_check.py (n = 1024, flat Hadamard eigenvectors, max a_ii/lambda_k about 0.003): whenever the events S, E1, E2 held,
  the conclusions of Lemma 2.2 and W4 Steps 2-3 held; empirical means of S, E1, E2 match the exact formulas used for Markov.
- mixed_sign_check.py: Lemma 6.1 identities to 6e-16; Lemma 6.2 and the |Lambda| version of Lemma 3.2 never violated (72 cases).
- density_smell.py: histogram peaks of PSD forms with lambda_3 = 1 (heavy coordinate of leverage 0.6 plus a linear term
  orthogonal to the range; eigenvalues (50,1,1) with a random linear term; X_1^2 plus a spread rank-two part plus a
  linear term outside the range; n = 12, 60; uniform and spread laws): at most 2.83 (the Gaussian value for
  |PX|^2 with uniform inputs is about 2.90), decreasing as the linear term grows; nothing near the proved 1.71e4.
- constants.py: every constant in W4-W6 recomputed; the Fejer transform checked by quadrature; the (C1) and (C2)
  layer-cake inequalities checked numerically.
Pointwise bounds on characteristic functions: none of the arguments uses one. The only inputs about psi_i are the
L^p bound int |psi|^p <= 4 pi/sqrt(p) (inside Theorem D_k) and |psi_i| <= 1. (A pointwise decay bound for |psi(s)| is
false for densities <= 1: laws concentrated near a lattice 2 pi Z/s_0 have |psi(s_0)| close to 1.)

## W8. What remains, and the most useful next step

Proved: Theorems 1, 2, 4, Proposition 3, Corollaries 5, 6. Constants are crude (1.71e4 against a numerical
supremum near 3).
Open, in the precise form Corollary 5 gives: no-pivot matrices M with a hub-like coordinate, (|M|)_ii > |lambda|_(k)/gamma'_k,
i.e. a coordinate that carries weight in both the positive and the negative spectral part while m_ii is small. The
star + rank one + eps W family is of this kind (its hub has (|M|)_hh ~ 1), and so is every configuration in open items
(a), (b); all others are closed by Theorem 4.
Next step: treat the hub-like set H_* = {i : (|M|)_ii > |lambda|_(k)/gamma'} directly. Because the weight of i in |M| is
large, conditioning on X_{H_*} is not free of eigenvalue loss, but one can try: (1) put H_* on the J side of the
decoupling (J carries no marginal constraint) and use Theorem MF/H-type integration of X_{H_*} against its densities
(each hub then gains a full |t|^{-1} instead of |t|^{-1/2}); (2) prove the analogue of Lemma 2.2 for the light
coordinates with H_* excluded, which needs the light rows b_i (i notin H_*) to carry a fixed fraction of |Lambda| on
the top-k directions - the quantity to control is lambda_min of |Lambda_K|^{-1/2} (sum_{i notin H_*} b_i^K b_i^{K T}) |Lambda_K|^{-1/2}.
When that fraction is small the hubs carry the top directions, which is the pure-hub situation of Propositions 5.3-5.5.

## STATUS (end)
Target PROVED: Theorem 1 (PSD, any rank, any linear terms, C_0 = 1.71e4), Theorem 2 (levels 1, 2), Proposition 3.
Also PROVED: Theorem 4 and Corollary 5 (indefinite matrices whose |M| has small diagonal; the open no-pivot part is
exactly the hub-like configurations), Corollary 6 (rank three open only on the indefinite two-sheet side).
Referee re-read of W0-W8 done: every step re-derived; all numerical controls have teeth (negative controls fail).

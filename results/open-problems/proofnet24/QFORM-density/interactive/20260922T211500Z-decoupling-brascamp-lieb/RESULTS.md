# Decoupling, Fresnel linearisation and Brascamp-Lieb bounds for the bounded-density problem

Programme QFORM-DENSITY-3EIG-20260922. Record 20260922T211500Z-decoupling-brascamp-lieb. Continued in
20260922T231000Z-semidefinite-and-hub-reduction (semidefinite forms, the lower levels (H1), (H2), the no-hub
theorem, rank three for definite forms, and the reduction of the conjecture to no-pivot matrices with a hub).

Status: Lemmas 1-4 and Theorems F, H, D below are proved, with the proofs given here, and were checked
numerically (Section 9). Section 7A records the real-variable results of GEOMETRIC_ROUTE_REPORT.md: the
conjecture for n = 3 (constant 20), for every fixed n (constant 250 n (8 + log n)), and its equivalence
with the restriction to matrices that have no pivot. None of this proves the unrestricted conjecture;
Sections 7 and 7A state which configurations are left open.

## 0. Setting

X = (X_1, ..., X_n) has independent coordinates with densities f_i <= 1. psi_i is the characteristic
function of X_i. Q(x) = x^T A x + b^T x + c with A real symmetric. phi(t) = E exp(i t Q(X)).
Conjecture: if A has at least three eigenvalues of modulus >= 1, then ||p_Q||_inf <= C, C universal.
Conditioning on any set K of coordinates is free: ||p_Q||_inf <= sup over x_K of ||p_{Q | X_K = x_K}||_inf,
and given X_K the form is a quadratic polynomial in the remaining variables whose quadratic part is the
principal block of A. By Madiman-Melbourne-Xu (arXiv:1705.00642, Thm 1.5) it suffices to treat laws that
are uniform on sets of measure one.

## 1. The three-dimensional coarea inequality is false

The inequality ||p_S||_inf <= K ||rho||_inf^{2/3} for S = sum lambda_i Y_i^2 (|lambda_i| >= 1), with Y
having an arbitrary density rho on R^3 (Lemma 3 of qform_density.tex, 22 September), fails. Let Y be
uniform on the shell R <= |y| <= R + delta with 4 pi R^2 delta = 1/B. Then ||rho||_inf ~ B, while |Y|^2 is
spread over an interval of length ~ 2 R delta = 1/(2 pi R B), so ||p_S||_inf ~ 2 pi R B, unbounded as
R -> infinity. The rank-three theorem and the 3x3-principal-block proposition of that note depend on this
inequality and are unproved as stated. Any argument for a three-dimensional piece has to use the product
structure of X, not only a bound on a three-dimensional density.

## 2. L^p bounds for characteristic functions

Lemma 1. Let f <= 1 be a probability density and g a complex function with |g| <= f. Then for p >= 2,
   integral |g^(hat)|^p <= 4 pi / sqrt(p).
Proof. For p = 2m, |g^|^{2m} is the Fourier transform of (g * g~)^{*m}, g~(x) = conj g(-x), which is
continuous, and |g^|^2 is integrable (Plancherel). So integral |g^|^{2m} = 2 pi (g*g~)^{*m}(0) and
|(g*g~)^{*m}| <= (f*f~)^{*m}, the density of a sum of 2m independent variables with densities <= 1. By
Rogozin (1987) and Ball's cube slicing that density is <= sqrt(2)/sqrt(2m) = 1/sqrt(m). For general p use
m = floor(p/2) and |g^| <= 1: m >= p/4 when p >= 4, and 2 pi <= 4 pi/sqrt(p) when 2 <= p < 4.

## 3. Fresnel linearisation

Lemma 2. For theta != 0 and eps > 0 put a = 1/(4(eps - i theta)); then Re a > 0 and
   exp(i theta y^2 - eps y^2) = sqrt(a/pi) integral exp(-a u^2 + i u y) du,   |a| -> 1/(4|theta|).
Applied to three squares lambda_k <v_k, x>^2 with the damping removed by dominated convergence,
   |E exp(i t (sum_k lambda_k <v_k,X>^2) + i t W(X))| <= prod_k (4 pi |t lambda_k|)^{-1/2}
        integral_{R^3} |E exp(i <V u, X> + i t W(X))| du                                   (3.1)
for any real function W; V is the n x 3 matrix with columns v_k.

## 4. Theorem F (Fresnel-Brascamp-Lieb)

Theorem F. Let A = sum_{k=1}^3 lambda_k v_k v_k^T + B with v_k in R^n, lambda_k != 0, B symmetric, and
let I be a set of coordinates with B_II diagonal. Put rho_i = ((v_1)_i, (v_2)_i, (v_3)_i),
G_I = sum_{i in I} rho_i rho_i^T, and suppose rho_i^T G_I^{-1} rho_i <= 1/2 for i in I. Then
   |phi(t)| <= (4 pi)^{3/2} |t|^{-3/2} (|lambda_1 lambda_2 lambda_3| det G_I)^{-1/2},
   ||p_Q||_inf <= 12 (|lambda_1 lambda_2 lambda_3| det G_I)^{-1/3}.
Proof. In (3.1) take W = X^T B X + b^T X. Condition on X_J, J = complement of I. Because B_II is diagonal
the X_I-expectation factorises: with g_i(x) = exp(i t B_ii x^2) f_i(x),
   |E(...)| <= E_{X_J} prod_{i in I} |g_i^(<rho_i, u> + s_i(X_J))|.
Integrate in u first. Substitute u = G_I^{-1/2} w; the vectors G_I^{-1/2} rho_i form a tight frame with
weights c_i = rho_i^T G_I^{-1} rho_i <= 1/2 summing to 3. The geometric Brascamp-Lieb inequality (Ball;
Barthe) is invariant under translating each one-dimensional argument, so the u-integral is at most
   det(G_I)^{-1/2} prod_i (c_i^{-1/2} integral |g_i^|^{1/c_i})^{c_i} <= (4 pi)^3 det(G_I)^{-1/2}
by Lemma 1. Finally integral min(1, K|t|^{-3/2}) dt = 6 K^{2/3} and ||p_Q||_inf <= (2 pi)^{-1} int |phi|.
Corollary. Rank-three A with |lambda_k| >= 1 and all leverages <= 1/2, plus any diagonal matrix:
density <= 12.

## 5. Theorem H (hub coordinates)

Theorem H. Split the coordinates as H u I u J. Suppose A_II = sum_{k=1}^r lambda_k v_k v_k^T + D with D
diagonal (r >= 0), and put rho~_i = ((v_k)_i, k <= r ; A_{ih}, h in H) in R^{r+|H|} for i in I,
G~ = sum_{i in I} rho~_i rho~_i^T, with normalised leverages rho~_i^T G~^{-1} rho~_i <= 1/2. Then
   |phi(t)| <= (2|t|)^{-|H|} prod_{k<=r} (4 pi |t lambda_k|)^{-1/2} (4 pi)^{r+|H|} det(G~)^{-1/2}.
The blocks A_HH, A_HJ, A_IJ, A_JJ are arbitrary.
Proof. Condition on X_J. For fixed x_H the form is quadratic in X_I with linear term 2 A_IH x_H + (fixed),
and the x_H-only terms are a phase. So |phi(t)| <= integral prod_h f_h(x_h) |Phi_I(t; 2 A_IH x_H)| dx_H with
Phi_I(t; h) = E exp(i t X_I^T A_II X_I + i t <h, X_I>). Use f_h <= 1 and substitute y = 2 t x_H (Jacobian
(2|t|)^{-|H|}); the linear phase becomes <A_IH y, X_I>. Apply (3.1) to the rank-r part of A_II with the
diagonal twist D and this linear tilt, then Brascamp-Lieb over (u, y) in R^{r+|H|} exactly as in
Theorem F.
The decay exponent is |H| + r/2. Theorem F is H = empty, r = 3. A star (one hub joined to many leaves by
entries c, total weight sum c^2 = 1) gives |phi| <= 2 pi/|t|; two disjoint stars, or one star plus one
delocalized square, give an integrable bound. Stars are invisible to Theorem D below: every off-diagonal
block of a star plus a rank-one term has rank at most two.

## 6. Theorem D (decoupling with volume-sampling weights)

Theorem D. Let I, J be disjoint, M = A_IJ, Z = e_3(M^T M) = sum over 3x3 minors det(M_ST)^2 (S in I,
T in J). Let w_ST = det(M_ST)^2 / Z, alpha_i = P_w(i in S), beta_j = P_w(j in T). If alpha_i <= 1/2 for
every i in I, then
   |phi(t)| <= (2 pi)^{3/2} e^{3/4} |t|^{-3/2} Z^{-1/4},     ||p_Q||_inf <= 6 sqrt(e) Z^{-1/6}.
Since Z >= s_1^2 s_2^2 s_3^2 (singular values of M), the density is <= 10 / s_3(A_IJ).
Proof. Condition on the remaining coordinates. Cauchy-Schwarz in X_I (Weyl differencing) gives
   |phi(t)|^2 <= E_W prod_{i in I} |psi_i(2 t (M W)_i)|,   W = X_J - X_J',
where W has independent coordinates with densities g_j = f_j * f~_j <= 1; the diagonal blocks and all
linear terms drop out. The right side is a Brascamp-Lieb integral over R^J: h_i = |psi_i(2t .)| along the
rows a_i of M with exponent alpha_i, and g_j along e_j with exponent 1 - beta_j (sum alpha = sum beta = 3).
By Lieb's theorem its constant is the supremum over centred Gaussians,
   sup prod_i (p_i d_i)^{alpha_i/2} prod_j (q_j e_j)^{(1-beta_j)/2} / det(D_J + M^T D_I M)^{1/2},
p_i = 1/alpha_i, q_j = 1/(1-beta_j). Now det(D_J + M^T D_I M) = det D_J det(I + N^T N) >= det D_J e_3(N^T N)
with N = D_I^{1/2} M D_J^{-1/2}; by Cauchy-Binet e_3(N^T N) = sum_{S,T} det(M_ST)^2 prod_S d_i prod_T e_j^{-1},
and weighted AM-GM with weights w_ST gives >= Z prod d_i^{alpha_i} prod e_j^{-beta_j}. All Gaussian
parameters cancel:
   BL <= prod alpha_i^{-alpha_i/2} prod (1 - beta_j)^{-(1-beta_j)/2} Z^{-1/2}.
Lemma 1 gives ||h_i||_{1/alpha_i} <= (4 pi sqrt(alpha_i) / (2|t|))^{alpha_i}; the factors alpha_i^{alpha_i/2}
cancel, sum alpha_i = 3 gives (2|t|)^{-3} (4 pi)^3, ||g_j||_{q_j} <= 1, and
prod (1-beta)^{-(1-beta)/2} <= e^{sum beta/2} = e^{3/2}.
Remarks. (i) alpha_i = sum_m p_m u_m(i)^2 with u_m the left singular vectors and p_m = s_m^2 e_2(s^2 without
m)/e_3(s^2), sum p_m = 3. (ii) Any weight w on pairs with marginals <= 1/2 may replace volume sampling; the
cost is Z replaced by exp(E_w log det^2 + H(w)). With two row-disjoint 3x3 minors of modulus >= delta
this gives density <= 6 sqrt(e) (2 delta^2)^{-1/6}. (iii) The J side carries no constraint, so coordinates
of large weight are placed in J. (iv) Z >= s_1^2 s_2^2 s_3^2 and every further singular value of A_IJ adds
to Z, so a dense perturbation that keeps three singular values of A_IJ large cannot hurt Theorem D.

## 7. Completion lemmas and what remains

Lemma 3 (one-coordinate completion). If a_11 = d != 0 then Q = d (X_1 + a(X'))^2 + R(X'), X' = (X_2..X_n),
and R has quadratic part the Schur complement A/d. For every s,
   p_Q(s) <= E k_d(s - R),   k_d(w) = (|d| |w|)^{-1/2} 1{sign(d) w > 0}.
Hence sup_s P(|Q - s| <= eps) <= 2 sqrt(2 eps/|d|) for every R; if sup_s P(|R - s| <= rho) <= H sqrt(rho)
then sup_s P(|Q - s| <= eps) <= C H |d|^{-1/2} eps (1 + log_+ (1/(H^2 eps))) (dyadic shells in |s - R|);
and if sup_s P(|R - s| <= rho) <= H' min(1, rho log(e/rho)) then ||p_Q||_inf <= C(H') |d|^{-1/2}, from
E k_d(s - R) = integral_0^inf P(0 < sign(d)(s - R) < 1/(|d| lam^2)) d lam. (The conditional density of
d(X_1 + a)^2 is <= k_d whatever a is.)
Lemma 4 (Schur complements keep large eigenvalues). If A has k eigenvalues of modulus >= 1 and a_11 != 0,
A/a_11 has at least k-1; for an invertible 2x2 principal block B, A/B has at least k-2. (For invertible A,
(A/a_11)^{-1} = (A^{-1})_{-1,-1} and Cauchy interlacing applies to the eigenvalues of A^{-1} in [-1,1];
the general case follows by perturbing the kernel of A.)
The two-coordinate analogue is the pair theorem of record 20260922T180015Z-pair-log: after completing an
invertible indefinite pair B, a remainder with sup_s P(|R-s| <= rho) <= H sqrt(rho) gives
||p_Q||_inf <= 4 sqrt(2H) (|det B| sigma_min(B))^{-1/4}.

Physical blocks. Every invertible 2x2 principal block B with |det B| >= D and sigma_min(B) >= kappa gives
a bounded density depending only on (D, kappa), whatever the rest of A (given s_3(A) >= 1): a definite B
by the 2D area lemma after conditioning on the other coordinates, an indefinite B by the pair theorem
together with the arbitrary-rank small-ball bound sup P(|Z^T S Z + ... - w| < rho) <= 5 (rho/||S||)^{1/4}
(FULL_MATRIX_PAIR_EXTENSION.md), since the logarithmic pair kernel absorbs any power-type small-ball
remainder, and A/B keeps a large eigenvalue by Lemma 4.

Further proved extensions are in FOURIER_ROUTE_REPORT.md (this folder): Theorem D with I-marginals up to
any h < 3/4 (constant 6 sqrt(e)(2h)^{-1/2}(3-4h)^{-1} Z^{-1/6}); a 5-volume version with no marginal
condition, ||p_Q||_inf <= 5 sqrt(2e) e_5(A_IJ^T A_IJ)^{-1/10}; fractional potentials
H_alpha(Z) = sup_s E|Z - s|^{-alpha} <= c_alpha int |t|^{alpha-1}|phi_Z|; the square peel
||p_Q||_inf <= |a|^{-1/2} H_{1/2}(A/a); the zero-diagonal pair peel; three independent blocks by Holder in
t (e.g. 2(X1X2 + X3X4 + X5X6) has density <= 3); the n = 3 zero-diagonal form 2(X1X2 + X2X3 + X1X3) has
density <= 4.55; and I - 2rr^T on R^3 is bounded by two square peels.

Ruled level sets (COUNTEREXAMPLE_SEARCH.md, Theorem C; identity re-derived here). For
q = y_1^2 + y_2^2 - y_3^2 and s > 0 parametrise one ruling by y = sqrt(s) e_theta + t w_theta,
e_theta = (cos, sin, 0), w_theta = (-sin, cos, 1). With a = -sqrt(s) sin - t cos, b = sqrt(s) cos - t sin, the
normal is N = d_theta y x d_t y = (b, -a, -t) and grad q = 2 (y_1, y_2, -y_3) = 2N, so
d sigma / |grad q| = (1/2) d theta dt and p(s) = (1/2) integral dtheta integral rho(y(theta,t)) dt. Each line
integral is 2^{-1/2} times a two-dimensional marginal density of the product measure, <= 2, so
p(s) <= pi sqrt(2) for s >= 0 (general eigenvalues: the displayed integral in that file). Hence every
indefinite rank-three form whose linear term lies in the range of A (so that Q = q(Y - y_0) + const with
Y = R^T X) has density <= pi sqrt(2) on the side where its level sets are one-sheet hyperboloids, in every
dimension, for every product law, with no leverage condition. A linear term with a component outside the
range makes Q = q(Y) + beta Y_4 and the ruled-surface argument does not apply. (The line-integral bound holds
for almost every line; for a fixed theta the lines used form a null family, which is handled by replacing X_i
with X_i + eps G_i, G_i Gaussian, and letting eps -> 0.) Rank three remains open only on the convex side
(two-sheet hyperboloids, ellipsoids), outside the low-leverage case of Theorem F, and for linear terms
outside the range.

This gives an induction on "levels" (level 1: small ball <= H sqrt(eps); level 2: <= H eps log(e/eps);
level 3: bounded density). A large diagonal entry lifts the level of its Schur complement by one, an
indefinite pair lifts it by two, a definite pair gives level 3 outright, and Theorems D, F, H give level k
directly from k off-diagonal, Fresnel or hub dimensions (via Esseen for k = 1, 2).
Open. A covering statement: every matrix with k large eigenvalues and ALL entries small is covered by
Theorem D or H. It fails for the exact classes as stated: a star plus a rank-one delocalized term plus a
small dense perturbation eps W (||eps W|| << 1) escapes both - Theorem H needs A_II to be exactly low rank
plus diagonal, and Theorem D only gives 6 sqrt(e) Z^{-1/6} with Z ~ eps^2 n. Robustness of the Fresnel
bound (3.1) to a small dense twist exp(i t X^T E X) is the missing estimate.

## 7A. Conditioning on coordinates: n = 3, fixed n, and the reduction to matrices without pivots

Proofs are in GEOMETRIC_ROUTE_REPORT.md; the statements below were re-derived from them.

Two-coordinate lemma. Let W = (W_1, W_2) have independent coordinates with densities <= 1 and let
q(w) = (w - w_0)^T B (w - w_0) + kappa with det B = -D < 0, eigenvalues mu_+ > 0 > mu_-,
Lambda = 1/mu_+ + 1/|mu_-|. For a.e. s,
   p_q(s) <= D^{-1/2} (5.2 + log_+ (32 / (Lambda |s - kappa|))),
   P(|q(W) - s| <= u) <= (2u / sqrt D) (6.2 + log_+ (16 sqrt D / u)).
The branches of {q = kappa + delta} are w = u e^t + v e^{-t} with |u| = |v| = sqrt(delta Lambda)/2, and the
map (delta, t) -> w has Jacobian 1/(2 sqrt D). On each tail one coordinate is monotone with |w_i'| >= |w_i|/3,
so its unit mass cuts off the t-integral (bathtub principle). The coefficient of the logarithm is sharp; for
a general density on R^2 with bounded marginals the statement is false.

Theorem (n = 3). If the 3 x 3 matrix A has all three eigenvalues of modulus >= 1, then Q = X^T A X + b^T X + c
has density <= 20, for all b, c and all independent X_i with densities <= 1. If some |a_ii| >= 0.3, condition
on the other two coordinates: the conditional density is <= |a_ii|^{-1/2} |s - R|^{-1/2}, where R is a
quadratic in two coordinates with matrix A/a_ii. Its inverse is a principal block of A^{-1}, so both of its
eigenvalues have modulus >= 1, and the lemma gives E|s - R|^{-1/2} <= 10.83. Otherwise some 2 x 2 principal
block B has |det B| > 0.365; conditioning on the third coordinate X_k leaves a logarithmic profile centred at
kappa(X_k), a quadratic in X_k with leading coefficient det A / det B = 1/(A^{-1})_kk of modulus >= 1, and
E log_+ 1/|s - kappa(X_k)| <= 2 log(2 sqrt 2) + 2. In any dimension, a principal 3 x 3 block whose eigenvalues
all have modulus >= gamma gives density <= 20/gamma.

Pivot calculus. With alpha_1(Z) = sup_{s,u} P(|Z - s| <= u)/sqrt(u) and
alpha_2(Z) = sup_{s, u <= 1} P(|Z - s| <= u)/(u (1 + log(1/u))): a matrix is c-certified of level 1 if it has
a diagonal entry or a 2 x 2 principal minor of modulus >= c; of level 2 if it has such a minor, or a diagonal
entry >= c whose Schur complement is level 1; of level 3 if it has a definite 2 x 2 block with det >= c, an
indefinite one whose Schur complement is level 1, or a diagonal entry >= c whose Schur complement is level 2.
Level 1 gives alpha_1 <= 50 c^{-1/2}, level 2 gives alpha_2 <= 283 c^{-1}, level 3 gives
||p_Q|| <= 135 c^{-1} sqrt(6.7 + log(1/c)), for every n and every linear term. A certificate uses at most four
coordinates, and certified levels of direct summands add (so 2(X_1 X_2 + X_3 X_4) and lambda X_1^2 + 2 X_2 X_3
are covered).

Every fixed n. Pivots of size >= 1/(2n) (diagonal) or >= 1/(2n^2) (2 x 2 minors) always exist along the tree,
which gives ||p_Q|| <= 250 n (8 + log n) for every n x n matrix with at least three eigenvalues of modulus >= 1.
For rank three, ||p_Q|| <= 20 / sigma_min(R_S)^2 for any invertible 3 x 3 row block of the eigenvector matrix R,
hence <= 60 (n - 2).

Reduction. Say M has no c-pivot if every |m_ii| < c and every 2 x 2 principal minor has modulus < c; then every
|m_ij| < sqrt(2c). The conjecture is equivalent, with polynomially related constants, to the following three
statements for matrices with no c-pivot, uniformly in the linear and constant terms: a bounded density when M
has three eigenvalues of modulus >= 1; sup_s E[|s - R|^{-1/2}; |s - R| <= 1] < infinity when it has two;
sup_s E log_+ 1/|s - R| < infinity when it has one. Sufficiency is a decision tree of depth three over pivots.
Necessity: adjoin one or two new uniform coordinates (R +- 4 X_0^2, and R + 4(X_0^2 - X_0'^2), whose density is
at least a constant times log(1/|z|) near 0).

In the no-pivot regime the Fourier results above supply these statements whenever an off-diagonal block has
spread volume, uniformly in the linear terms (decoupling removes them): Theorem D and its k-volume versions give
the three levels from spread k-volume with k = 1, 2, 3 and I-marginals <= 1/2, or from any k-volume with
k = 2, 4, 5 (FOURIER_ROUTE_REPORT.md, Section 1.2, with q = 2).

Hubs. A hub is a coordinate h with small diagonal whose row w has norm >= 1 and small entries. It carries two
eigenvalues near +-|w| and no pivot, and every off-diagonal block sees it with rank one, so decoupling loses
half of its decay. Proved in GEOMETRIC_ROUTE_REPORT.md: with a_hh = 0, alpha_2(Q) <= 2 + 4 sqrt(2)/|w| whatever
the rest of the matrix; one hub plus one rank-one direction, Q = a X_h^2 + 2(L + beta) X_h + F(L, V) with F a
function of L = <w, X> and V = <v, X> only, has bounded density for every hub diagonal a (at a = 0 the bound is
1/2 + 16 |lambda|^{-1/2}); two hubs with A_HH = 0 and sigma_min(A_{H, H^c}) >= sigma give density
<= 1/2 + 8 sigma^{-2} whatever the rest of the matrix.

Open after this section: the no-pivot regime in the three forms above. The configurations that no result here
covers are hubs coupled to a general dense remainder (the case star + rank one + eps W of Section 7 is one of
them), hubs with a small nonzero diagonal and a general remainder, and pairs of hubs with a nonzero hub block.
Numerically nothing grows: for star + rank one + eps W (n = 30 and 120, eps = 0, 0.02, 0.1, both signs of the
rank-one term, uniform and spread laws) the histogram peaks lie between 1.9 and 3.4 for uniform laws and fall
as eps grows (star_family.py, star_family_output.txt); at n = 3 the largest values found are about 2.55.

## 8. Relation to other records in this folder

- Theorem F with B = 0 is Lemma 3.1 of 20260922T161801Z-rank-two-fusion (Fresnel linearisation and
  geometric Brascamp-Lieb for diffuse projections with linear phases). The diagonal twist, the
  conditioning set J and Theorem H are the additions here.
- Theorem D sharpens Section 5 of 20260922T131746Z-regularized-determinant, which gives
  |phi(t)| <= det(I + 2q t^2 B B^T/(pi^2 e^2))^{-1/(4q)} under max_i (P_range(B))_ii <= q/2. At q = 1 the decay
  exponents agree (one half per singular direction), but the leverage there is that of the whole range of B,
  which equals one on every coordinate once B has full row rank, however small the extra singular values.
  In Theorem D a singular direction enters alpha_i with weight p_m = s_m^2 e_2(s_{-m}^2)/e_3(s^2), so tiny
  directions do not count: for A = A_3 + eps W with W Wigner, range(B) = R^I while max alpha_i ~ 3/|I|.
- The unit-density example E_delta = {0 <= x^2 + y^2 - z^2 <= delta, |z| <= 1/(2 pi delta)} in
  20260922T180015Z-pair-log/CORRECTIONS.md refutes the inequality of Section 1 exactly (Q uniform on
  [0, delta]); the same file shows the conditional projection moment diverges for independent inputs.
- The two-coordinate step of Section 7 is PAIR_LOG_THEOREM.md of that record; FULL_MATRIX_PAIR_EXTENSION.md
  extends it to arbitrary rank, and its random-sign argument (Section 3 there) finds a cross block of norm
  >= ||S||/4 for any zero-diagonal S.
- The heavy-coordinate obstruction of the fleet03/B10 handoff is the hub configuration of Section 5.
  Theorem H settles it when the light block is low rank plus diagonal; star + rank one + eps W is the case
  still open.

## 9. Numerical checks (scripts in this folder)

- check_fresnel_bl.py: Lemma 1 for uniform and spread-set laws (N = 1, 10, 40 intervals; p = 2, 3, 6, 20),
  all values below 4 pi/sqrt(p); and |phi(t)| for a rank-three frame plus a diagonal matrix with spread-set
  inputs at the Monte Carlo floor, far below the Theorem F bound.
- thmD_check.py: the marginal formula in Remark (i) against brute-force enumeration of all 3x3 minors of a
  5x6 matrix (exact agreement); Theorem D bound for random rank-three (1,1,-1) forms: about 20, falling to
  1.3 as eps grows in A_3 + eps W/sqrt(n) (n = 40, 120, 400).
- twist_test.py: the missing estimate of Section 7 in its one-dimensional form. For n = 60, L = <v, X>
  with v = (1,...,1)/sqrt(n) and E dense with E v = 0 and ||E|| = 1, integral |E exp(iuL + itX^T E X)| du
  falls from 8.73 at t = 0 to 8.50 (t = 0.5), 5.80 (t = 2) and the Monte Carlo floor (about 0.12) for
  t >= 8 with uniform inputs; with spread-set inputs it is at the floor from t = 0.5. The twist shrinks
  the integral (it tracks |E exp(itX^T E X)| times integral |phi_L|); it does not inflate it.
- claim_test.py: the decoupled quantity E prod |psi_i(2t (A_IJ W)_i)| (a mean of nonnegative terms, so
  Monte Carlo estimates it well) for A_3 + eps W: max_t T(t) t^3 decreases in eps and in n, uniform and
  spread-set inputs.

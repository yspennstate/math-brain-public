# NOTES - structure lemma (wave 2, folder 06)

Conventions. M real symmetric n x n. "off-diagonal minor" = det M_ST with S, T disjoint, |S| = |T|.
rho(M) := max over disjoint S,T of rank M_ST  (off-diagonal rank).
mr(M)  := min over diagonal D of rank(M - D)   (free-diagonal rank).
V_k(M) := sum over ORDERED pairs (S,T) of disjoint k-sets of det(M_ST)^2 (off-diagonal k-volume), V_0 = 1.
For a uniformly random partition (I,J) (each coordinate independently): E e_k(M_IJ^T M_IJ) = 4^{-k} V_k(M).

## Piece 1 (exact version, first results)

(a) Direct sums: rho and mr are additive over direct sums (off-diagonal blocks of a block-diagonal matrix are
block diagonal; M - D is block diagonal). A star (hub h, leaves with weights w, >= 2 nonzero) has rho = 1,
mr = 2. So r disjoint stars: rho = r, mr = 2r.  => f(r) >= 2r.   PROVED.

(b) f(1) = 2 exactly. PROVED (combinatorial). If all off-diagonal 2x2 minors vanish, look at the support graph G
of the off-diagonal entries. If G has two disjoint edges ik, jl then the tetrads force m_il, m_jk, m_ij, m_kl != 0
(K_4), and any vertex adjacent to a K_m (m >= 4) is adjacent to all of it; so either G (minus isolated vertices)
is one complete graph K_m, m >= 4, where tetrads give m_ij = sigma u_i u_j (c_i := m_ij m_ik / m_jk is independent
of j,k, c_i c_j = m_ij^2), i.e. mr <= 1; or all edges pairwise intersect: a star (mr <= 2) or a triangle (3x3,
mr <= 2). Hence mr <= 2.

(c) Upper bound f(r) <= 3r. PROVED. Let rho(M) = r, choose disjoint r-sets S,T with M_ST invertible, K = S u T,
L = rest, C = M_ST^{-1}. For l in L put y_l = M_{lS} in R^S, x_l = M_{lT} in R^T, n_l = (y_l, x_l) in R^{2r}.
 - Bordered minors (rows S+l, cols T+m, l != m in L, disjoint): det = det(M_ST) (M_lm - x_l^T C y_m) = 0, so
   off-diag(M_LL) = off-diag(P), P := X C Y^T (rank <= r).
 - Symmetry of M gives also M_lm = x_m^T C y_l, so omega(n_l, n_m) := x_l^T C y_m - x_m^T C y_l = 0 for l != m,
   and trivially for l = m. omega is a NONDEGENERATE skew form on R^{2r} (C invertible). So U := span{n_l} is
   omega-isotropic and dim U <= r, i.e. rank N <= r, N := [Y, X] (|L| x 2r).
 - P - P^T is skew with zero off-diagonal, so P is symmetric. Take D = diag(0_K, diag(M_LL) - diag(P)).
   Then the L-rows of M - D are [N, P] = N [I, B N^T] with P = N B N^T, B = [[0,0],[C,0]]: rank <= rank N <= r.
   The K-rows contribute <= 2r. So mr(M) <= 3r.
So 2r <= f(r) <= 3r, f(0) = 0, f(1) = 2.

(d) Evidence for f(r) = 2r (generic-L analysis, NOT a proof): write N = Z W^T (W a basis of U, 2r x p). Then
M - D = diag(I, Z) G diag(I, Z^T), G = [[M_KK - D_K, W],[W^T, E]], E = W^T B_sym W = W_x^T C W_y (symmetric).
If Z is "rich" (two disjoint row sets of L each of rank p), the remaining minor conditions say: every off-diagonal
block of G, where the p "bullet" indices may appear on BOTH sides, has rank <= r.
 - E invertible (p = r): then M_KK - W E^{-1} W^T is diagonal, so mr(M) = r (spread case).
 - E = 0 (p = r): for every partition of K, rank W_{K1} + rank W_{K2} = r, so the nonzero rows of W are
   independent: exactly r hubs R subset of K, and M_{K\R, K\R} is forced diagonal; then mr <= 2r.
Both extreme cases give <= 2r. Conjecture f(r) = 2r.

## Piece 2: small rows => Theorem D applies. The cancellation is controlled exactly.

Setting. M symmetric, U in R^{n x 3} orthonormal eigenvectors, MU = U Lambda, |lambda_k| >= 1, u(i) := U^T e_i,
l_i := |u(i)|^2, R := M - U Lambda U^T (so RU = 0, U^T R = 0). Random partition: eps_i = +-1 i.i.d. fair,
xi = (1+eps)/2, I = {xi = 1}, J = {xi = 0}, D := diag(eps).

KEY IDENTITY (exact, one line): since diag(xi) = (I+D)/2, diag(1-xi) = (I-D)/2 and RU = 0, U^T R = 0,
   U^T diag(xi) R diag(1-xi) U = (1/4) U^T (I+D) R (I-D) U = -(1/4) U^T D R D U.
Hence, with Delta := U^T D U = sum_i eps_i u(i)u(i)^T and Phi := U_I^T M_IJ U_J (3x3),
   4 Phi = (I + Delta) Lambda (I - Delta) - U^T D R D U,
   U^T D R D U = T0 + T1,  T0 = sum_i R_ii u(i)u(i)^T (deterministic),  T1 = sum_{i != j} eps_i eps_j R_ij u(i)u(j)^T.
So the feared cancellation (R_II U_I against U_I Lambda G_J) has MEAN T0/4 = (1/4) U^T diag(R) U,
which only sees the DIAGONAL of R, and a mean-zero Rademacher chaos T1 with
   E||T1||_F^2 <= 2 sum_{i != j} R_ij^2 l_i l_j <= 2 (max l) sum_i l_i ||R e_i||^2,
   E||Delta||_F^2 = sum_i l_i^2 <= 3 max l.
[Check of the chaos second moment: E eps_i eps_j eps_k eps_l != 0 for i != j, k != l only when (k,l) = (i,j) or (j,i);
<u(i)u(j)^T, u(j)u(i)^T>_F = (u(i).u(j))^2 <= l_i l_j.]

Row-norm facts (eta := max_i ||M e_i||):
 (F1) l_i <= ||Lambda u(i)||^2 <= ||M e_i||^2 <= eta^2   (||Me_i||^2 = sum_all lambda^2 u_k(i)^2, |lambda| >= 1 on U).
 (F2) M e_i = U Lambda u(i) + R e_i with R e_i orthogonal to range U, so ||R e_i|| <= ||M e_i|| <= eta.
 (F3) |R_ii| <= ||R e_i|| <= eta; with no c-pivot also |R_ii| <= |m_ii| + u(i)^T|Lambda|u(i) <= c + eta^2.

THEOREM S (PROVED). If M has >= 3 eigenvalues of modulus >= 1 and every row has Euclidean norm <= eta <= 1/20
(no pivot hypothesis needed: small rows force small diagonal), then with probability >= 1/2 over a uniformly random
partition: s_3(M_IJ) >= 0.26 and every volume-sampling I-marginal is <= 0.11. Hence (Theorem D)
||p_Q||_inf <= 6 sqrt(e) Z^{-1/6} <= 6 sqrt(e)/s_3 <= 38, for every linear and constant term.
Proof. Markov: P(||Delta||_F^2 >= 12 eta^2) <= 1/4, P(||T1||_F^2 >= 24 eta^4) <= 1/4 (E||T1||^2 <= 6 eta^4 by F1,F2).
On the complement: s_3(4Phi) >= (1 - 2 sqrt3 eta)^2 min|lambda| - ||T0|| - ||T1|| >= (1-0.1732)^2 - 0.05 - 0.0122 = 0.621,
using s_min(ABC) >= s_min(A)s_min(B)s_min(C) and ||T0|| <= max|R_ii| (sum u(i)u(i)^T = I). Then
s_3(M_IJ) >= s_3(Phi)/(||U_I|| ||U_J||), ||U_I||^2 = ||(I+Delta)/2|| <= 0.5866, so s_3(M_IJ) >= 0.155/0.5866 >= 0.264.
Marginal bound (Piece 3 below): alpha_i <= 3 ||M_{iJ}||^2 / s_3(M_IJ)^2 <= 3 (1/400)/0.0697 <= 0.108.
Z = e_3 >= s_1^2 s_2^2 s_3^2 >= s_3^6.  QED.
Same proof with U of 1 or 2 columns gives s_1 or s_2 >= 0.26 and marginals <= 0.11 (k-marginal bound
alpha^(k)_i <= k ||m_i||^2 / s_k^2), i.e. the level-1 and level-2 statements from Theorem D_1, D_2.

Caveat (scale). The row-norm hypothesis is not scale-invariant: 1000 * (spread rank 3) has rows ~ 1000 sqrt(3/n),
which exceed 1/20 unless n is huge, although the matrix is spread. The refined form uses (after scaling so the
third-largest |lambda| is 1, which is free: p_Q(s) = p_{Q/mu}(s/mu)/mu) the top-3 eigenvectors U, so ||R|| <= 1, and
the parameters l = max l_i, d = max|R_ii| <= c + max_i u(i)^T|Lambda|u(i), nu^2 = sum l_i ||Re_i||^2 <= 3:
s_3(4Phi) >= (1 - 2 sqrt(3l))^2 - d - 2 sqrt(2 l) nu  w.p. >= 1/2. The marginal condition then needs, in addition,
the rows of the REMAINDER R to be small (a weak hub inside R, eigenvalue < 1, is still heavy for the marginals when
s_4(M_IJ) is comparable to s_3). So the correct global notion of "heavy coordinate" has two parts:
tau_i^2 := u(i)^T |Lambda| u(i) (big part, scale-free) and r_i := ||R e_i|| (remainder row).

NUMERICAL (check_thmS.py): identity error 1.1e-15; marginal formula vs brute force 1.4e-15; bound
alpha_i <= 3||m_i||^2/T_3 holds (max ratio 0.50); random partitions for plain / dense-noise / diagonal-cancelling /
big-eigenvalue (1, 40, -3) remainders, n = 200, 800: s_3 median 0.45-0.63 (min 0.37), max marginal <= 0.19.
Row norms up to 8.8 in the big case: Theorem S's hypothesis is sufficient, far from necessary.

## Piece 3: marginal lemmas (all PROVED)

M in R^{I x J}, G = M M^T, rows m_i, s_1 >= s_2 >= ..., T_k := sum_{j >= k} s_j^2 (tail mass beyond top k-1).
(M1) 1 - alpha_i = e_3(G with row/col i deleted) / e_3(G)  [Cauchy-Binet: sum_T det(M_ST)^2 = det G_SS].
(M2) alpha_i e_3(G) = sum_{S' in C(I-i,2)} det(G_S'S') dist^2(m_i, span m_S') <= ||m_i||^2 e_2(G_{-i}) <= ||m_i||^2 e_2(G).
(M3) e_k(x) >= (1/k) T_k e_{k-1}(x). Proof: e_k = (1/k) sum_{B, |B|=k-1} prod_B x (sum_{j not in B} x_j) and
     sum_{j not in B} x_j >= sum_j x_j - (x_1+...+x_{k-1}) = T_k. Also e_k <= T_k e_{k-1} (map A -> (A - max A, max A)).
     Hence e_k >= T_k T_{k-1} ... T_1 / k! >= T_k^k / k!.
(M4) alpha^(k)_i <= k ||m_i||^2 / T_k(M).  [(M2) for k-sets + (M3)]  (sharper than k||m_i||^2/s_k^2: dense noise
     makes T_k large, so rows comparable to the noise are light.)
(M5) Heavy => hub or pivot. If alpha_i > h then ||m_i||^2 > h T_3/3 >= h s_3^2/3. For a symmetric A with M = A_IJ:
     row i of A has norm^2 > h T_3/3; so either |a_ii| is large (1x1 pivot), or some |a_ij|^2 >= 2c with small
     diagonal (2x2 minor <= -(2c - c^2): a 2x2 pivot), or all |a_ij| < sqrt(2c) and the row has more than
     h T_3/(6c) nonzero entries: a HUB (a spread row carrying a direction).
(M6) At most floor(3/h) coordinates of I have alpha_i > h (sum alpha = 3).
Quantitative answer to (iii): if NO partition has (s_3 >= 0.26 and all I-marginals <= 0.11), then (Theorem S)
some row of A has norm > 1/20: a hub or a pivot in the sense of (M5).

## Piece 4: THE DICHOTOMY (main target, PROVED) - hub rows forced into J; tail mass T_3 decides

Let A be symmetric, eta > 0, H := {i : ||A e_i|| >= eta} (hub rows), L := complement, tau_0 >= 12 eta^2.
For ANY partition (I, J) with I subset of L and H subset of J: every row i in I has ||A_{iJ}|| < eta, so by (M4)
all I-marginals are <= 3 eta^2 / T_3(A_IJ).
 (G2) If some such partition has T_3(A_IJ) >= tau_0: marginals <= 3eta^2/tau_0 <= 1/4 and
      Z = e_3 >= T_3^3/6 >= tau_0^3/6, so Theorem D: ||p_Q||_inf <= 6 sqrt(e) (6/tau_0^3)^{1/6}, any linear terms.
 (G3) Otherwise T_3 < tau_0 for ALL such partitions. Since e_3 <= e_2 T_3 pointwise, averaging over the random
      partitions of L (H kept in J):  4^{-3} V3L <= E e_3 < tau_0 E e_2 <= tau_0 2^{-2} V2L, where
      VkL := sum over (S,T) disjoint, |S|=|T|=k, S subset of L, of det(A_ST)^2  (P(S in I, T in J) = 2^{-k} 2^{-|T cap L|}).
      So V3L < 16 tau_0 V2L.
 Skeleton (volume-sampled): draw (S,T), S subset of L, |S|=|T|=2, with prob det(A_ST)^2 / V2L. For l in L\K,
 m not in K u {l} (K = S u T): det A_{S+l, T+m} = det(A_ST) (A - P)_{lm}, P := A_{.,T} A_ST^{-1} A_{S,.} (rank 2).
 E_w sum_{l,m} (A-P)_lm^2 = sum_{(S',T')} det(A_S'T')^2 * 9 / V2L = 9 V3L/V2L < 144 tau_0.
 (each (S',T') with S' subset of L arises from 3 x 3 choices of (l in S', m in T')). So SOME skeleton (S,T) has
   sum_{l in L\K, m not in K u {l}} (A - P)_{lm}^2 < 144 tau_0.
 I.e. every light row, off the diagonal and off the 4 columns K, is within Frobenius^2 144 tau_0 (in total) of the
 rank-2 matrix P - INCLUDING its entries in the hub columns. The hub block A_HH is unconstrained.
Consequence for the programme: in (G3), after conditioning on X_K, the light block is
   A_{L'L'} = D + (symmetric rank <= 2) + E,  ||E||_F <= 2 * 12 sqrt(tau_0) (zero diagonal)
[symmetrise P: P - P^T = offdiag(E^T - E); best rank-2 approx of P_sym is within ||P_sym - P||_F].
THEOREM H (RESULTS.md) ALLOWS ARBITRARY A_HH, A_HJ: its only failing hypothesis in (G3) is that A_II must be
EXACTLY low rank + diagonal. So the whole no-pivot problem is reduced to: Theorem H robust to a zero-diagonal
Frobenius-small twist E on the light block (plus conditioning bookkeeping). Canonical case: star + rank one + eps W
with eps sqrt(n) <= 12 sqrt(tau_0) is exactly (G3); eps sqrt(n) larger is (G2).
Levels 1, 2: same with T_k, e_k, D_k: VkL < 2^{k+1} tau_0 V(k-1)L, rows within k^2 2^{k+1} tau_0 of rank k-1.

NUMERICAL (check_dichotomy.py): skeleton identity E_w err = 9 V3L/V2L exact (10.77134 both, n = 8, two rows as hubs);
max e3/(e2 T3) = 1.000 (<= 1), min e3/(T3 T2 T1/6) = 1.05 (>= 1) over 2000 random spectra.
Canonical star + rank one + eps W (zero diagonal), hub forced into J: T_3 median ~ 0.06 (eps sqrt n)^2
(0.0054 at eps sqrt n = 0.3, 0.06 at 1, 0.53 at 3), max I-marginal median 0.07-0.32. So small eps sqrt n is (G3)
and large eps sqrt n is (G2), as predicted. (Note: with |w| = 1, lambda = 1 the eigenvalues sit AT 1; the eigenvalue
count printed 1-2 because zeroing the diagonal moves them just below 1. Harmless for the check; rescale in report.)

## Piece 5: hub propositions in the form the decomposition needs (PROVED)

(H4) Many hubs, zero hub block. H any set, A_HH = 0, B = A_{H,L} with sigma_1 >= sigma_2 > 0 (|L| >= 3).
Given X_L, Q = <c, X_H> + q(X_L), c = 2 B X_L + b_H; its density is <= sqrt2/|c| (Ball: 1D marginals <= sqrt 2).
|c| >= |P c|, P onto span(a_1, a_2) (top left singular vectors): Pc = (2 sigma_1 Z_1 + beta_1, 2 sigma_2 Z_2 + beta_2),
Z = (<b_1,X_L>, <b_2,X_L>) has density <= 2 (LPP k = 2), so Y = Pc has density <= K = 1/(2 sigma_1 sigma_2).
Bathtub on R^2: E 1/|Y| <= 2 sqrt(pi K). Hence ||p_Q||_inf <= sqrt2 * 2 sqrt(pi/(2 sigma_1 sigma_2))
 = 2 sqrt(pi) (sigma_1 sigma_2)^{-1/2} <= 3.55/sigma_2, whatever A_LL and the linear terms. (GEOM 5.5 for any |H|.)
(H5) One hub direction, zero hub block: P(|Q - s| <= u) <= (4u/sigma_1)(1 + log_+(sigma_1/(4u))) (same argument,
 1D projection density <= sqrt 2, bathtub on R). So alpha_2(Q) <= (4/sigma_1)(1 + log_+(sigma_1/4)). (GEOM 5.3 for a
 hub DIRECTION spread over several hub coordinates.)
Both need A_HH = 0 exactly. Theorem H needs nothing of A_HH but needs A_II exactly low rank + diagonal.
(G3) supplies A_II = D + rank <= 2 + E with ||E||_F <= 24 sqrt(tau_0). So the single missing analytic statement is
Theorem H with a small zero-diagonal Frobenius twist E on the I block.

Remark (hub along the rank-one direction): e_h w^T + w e_h^T + sigma w w^T = sigma (w + e_h/sigma)(w + e_h/sigma)^T
 - e_h e_h^T / sigma, eigenvalues (sigma +- sqrt(sigma^2+4))/2: only ONE of modulus >= 1 for sigma >= 0 near 1.
 So a hub whose coupling vector lies in the span of the spread part does not add an eigenvalue pair; in Theorem H
 this shows up as a singular G~. The eigenvalue count has to be done on the "core" span(e_h, w_h, v_k).

## Status line (end of work)
Constant correction: in (G3) the symmetrised light-block twist satisfies ||E||_F < 3 * 12 sqrt(tau_0) = 36 sqrt(tau_0)
(F = offdiag(A_L'L' - P), ||P - P_sym||_F <= ||F||_F, ||P_sym - P_2||_F <= ||F||_F), not 24. Robust lemma: rank R <= 4r
because col(P), col(P^T) lie in col(N).

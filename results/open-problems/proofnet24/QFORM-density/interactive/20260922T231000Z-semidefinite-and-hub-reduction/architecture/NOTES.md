# NOTES (15_proof_architecture)

## N1. Start (read BRIEF, RESULTS, GEOM, FOURIER, COUNTEREX). First observations.

### N1.1 The integrability forms need much less decay than the sublevel forms.
GEOM Thm 5.2: conjecture <=> for no-c-pivot M (uniform in linear terms):
 (H3) >=3 large eig => ||p_R|| <= C ; (H2') >=2 => sup_s E[|s-R|^{-1/2}; |s-R|<=1] <= C ;
 (H1') >=1 => sup_s E log_+ 1/|s-R| <= C.
From Fourier: Esseen with the triangle kernel: (sin(x/2)/(x/2))^2 = int (1-|t|)_+ e^{itx} dt, and
this kernel is >= (2 sin(1/2))^2 = 0.9194 on |x|<=1, so
   sup_s P(|Z-s|<=u) <= 1.0877 u int_{|t|<=1/u} |phi_Z(t)| dt.            (E)
If |phi_Z| <= min(1, B|t|^{-b}) with 0<b<1: phi_Z-small-ball <= 2.18 B u^b/(1-b), hence
  E log_+ 1/|Z-s| <= (1/b)(1 + log_+(2.18 B/(1-b)))           [needs only b > 0]
  E[|Z-s|^{-1/2}; |Z-s|<=1] <= 2.18 B/((1-b)(2b-1))            [needs b > 1/2]
  density: needs b > 1.
So H1' needs ANY power decay, H2' needs decay > 1/2, H3 needs decay > 1.

### N1.2 D_k with q = 2 (no marginal condition) gives decay k/4.  => H1' is PROVED.
Rederived D_1, q = 2: |phi|^2 <= E_W F <= (E_W F^2)^{1/2}; BL with row exponents alpha_i = |a_i|^2/Z_1,
column exponents 1-beta_j, beta_j = |col_j|^2/Z_1, Z_1 = ||M||_F^2; need 2/alpha_i >= 2 (always).
Gaussian constant via det(D_J + M^T D_I M) >= sum_{ij} m_ij^2 d_i prod_{j'!=j} e_j' >= Z_1 prod d^alpha prod e^{1-beta}
(AM-GM, weights m_ij^2/Z_1). Result E_W F^2 <= sqrt(e/2) (2 pi/|t|) Z_1^{-1/2}, so
   |phi(t)| <= (pi sqrt(2e))^{1/4} Z_1^{-1/8} |t|^{-1/4}.
No-pivot M with an eigenvalue >= 1: E = offdiag(M) has ||E|| >= 1-c; random partition gives
E ||M_IJ||_F^2 = ||E||_F^2/4 >= (1-c)^2/4. So some partition has Z_1 >= (1-c)^2/4 and H1' holds with
H_1 = 4(1 + log_+(2.18*... )) explicit. LEVEL 1 IS CLOSED (PROVED), uniformly in linear terms.
(The record lists H1 as open; the point is that the log form needs only b > 0.)

### N1.3 Fourier menu per level (disjoint I,J, M = A_IJ, Z_k = e_k(M^T M), alpha^(k) = k-vol marginals on I):
 decay k/(2q) available when max_I alpha^(k) <= q/2, 1 <= q <= 2.
 H1': k >= 1 with q = 2 (anything nonzero).  [DONE by N1.2]
 H2': need k/(2q) > 1/2: k >= 3 with q = 2 (no condition); k = 2 with max alpha^(2) <= q/2 < 1; k=1 impossible.
 H3 : need k/(2q) > 1: k >= 5 (q=2); k = 4 with max alpha^(4) < 1; k = 3 with max alpha^(3) < 3/4.

### N1.4 Exact overlap identity (new).  E symmetric, zero diagonal, E = U diag(mu) U^T.
C = C_k(E) (k-th compound), C_ST = det E_ST.  e_k(E^2) = ||C||_F^2 = W_k + O_k,
W_k = sum_{S cap T = empty} C_ST^2  (= 4^k E_partition Z_k),  O_k = sum_{S cap T != empty}.
O_k <= sum_i ||P_i C P_i||_F^2 (P_i = coordinate projection on {S : i in S}) and, with x_r = U_ir^2,
   ||P_i C P_i||_F^2 = sum_{|R|=k} lam_R^2 sum_{r != r' in R} x_r x_r'  +  sum_{|Q|=k-1} lam_Q^2 (sum_{r in Q} mu_r x_r)^2
(lam_R = prod_{r in R} mu_r). Proof: <P_i a_R, P_i a_R'> = delta_RR' - det((I - u u^T)_{R,R'}), u = row i of U;
= x_R if R=R', = +-U_ir U_ir' if R = Q+r, R' = Q+r', 0 if |R cap R'| <= k-2; then use sum_r mu_r x_r = E_ii = 0.
Summing over i:
   W_k >= e_k(E^2) - sum_R lam_R^2 sum_{r!=r' in R} kappa_rr' - sum_{|Q|=k-1} lam_Q^2 ||diag(E_Q)||^2,
   kappa_rr' = sum_i U_ir^2 U_ir'^2,  E_Q = sum_{r in Q} mu_r u_r u_r^T.
Hub check (k=2, E = e_h w^T + w e_h^T): both correction terms = |w|^4/2, total = e_2, W_2 >= 0. Correct (W_2 = 0).
=> spread eigenvectors (small kappa, small diagonals of spectral parts) force W_k ~ e_k: Fourier sees them.

## N2. Two clean tools that remove the gap/leverage problem (the cancellation concern).

### N2.1 Marginal bound (PROVED, to be checked numerically).
B any matrix, rows b_i, A = B^T B, e_k = e_k(spec A). k-volume marginal
  alpha_i^(k) = P(i in S) = 1 - e_k(A - b_i b_i^T)/e_k(A) = b_i^T grad e_k(A) b_i / e_k(A)
(e_k(A + t b b^T) is affine in t: char poly det(x - A - t bb^T) = det(x-A)(1 - t b^T (x-A)^{-1} b)).
grad e_k(A) = V diag(e_{k-1}(a_{-j})) V^T <= e_{k-1}(a) I. Hence
   alpha_i^(k) <= |b_i|^2 e_{k-1}(s^2)/e_k(s^2) <= k |b_i|^2 / s_k(B)^2,
using  y_(k) e_{k-1}(y) <= k e_k(y)  (each (k-1)-set T gets an index a(T) of the top k not in T;
T u a(T) is a k-set hit by at most k such T).  So SMALL ROWS => SMALL MARGINALS, no leverage needed.

### N2.2 Overlap inequality for light rows (PROVED, check numerically).
E symmetric zero diagonal; L any row set; B0 = E_{L,.} (rows L, all columns), singular values nu,
SVD B0 = sum nu_r a_r b_r^T. W_k^(L) := sum_{S subset L, T subset [n], |S|=|T|=k, S cap T = empty} det(E_ST)^2.
Then with rho_L = max_{i in L} |row_i(E)|:
   W_k^(L) >= e_k(nu^2) - 2(k-1) rho_L^2 e_{k-1}(nu^2).
Proof: overlap <= sum_{i in L} ||P_i^row C_k(B0) P_i^col||_F^2; compound of SVD; <P_i a_R, P_i a_R'> = x_R, +-A_ir A_ir', 0;
same for b with y; sum_r nu_r A_ir B_ir = E_ii = 0 kills the diagonal term; get
   Phi_i = sum_R nu_R^2 sum_{r != r' in R} x_r y_r' + sum_{|Q|=k-1} nu_Q^2 (sum_{r in Q} nu_r A_ir B_ir)^2.
First: <= sum_Q nu_Q^2 sum_i (sum_{r notin Q} nu_r^2 A_ir^2)(sum_{r' notin Q} nu_r'^2 B_ir'^2) <= rho^2 (k-1) e_{k-1}.
Second: Cauchy-Schwarz (sum_{r in Q} nu_r A_ir B_ir)^2 <= r_i^2 sum_{r in Q} B_ir^2, sum_i <= rho^2 (k-1).
(For L = [n] and symmetric E this is W_k >= e_k(E^2) - 2(k-1) rho^2 e_{k-1}(E^2).)  NO GAP, NO LEVERAGE.

### N2.3 Consequence: the no-hub Fourier theorem (PROVED modulo N2.1-2).
Light set L = {i : |row_i(E)| <= rho_0}, heavy H = complement. Partition L randomly into I, J_L; J = J_L u H.
B = E_IJ. E Z_3(B) >= 2^{-6} W_3^(L); E e_2(B) <= e_2(nu^2)/4. If e_3(B) >= (rho_0^2/h) e_2(B) then all
I-marginals <= h (N2.1, rows of B have norm <= rho_0). E[e_3(B) - (rho_0^2/h)e_2(B)] >= 2^{-6}[e_3 - (4+16/h) rho_0^2 e_2](nu^2).
h = 1/2: if e_3(nu^2) >= 72 rho_0^2 e_2(nu^2) + 128 delta then some partition has Z_3 >= delta... more precisely
some partition has Z_3 - 2 rho_0^2 e_2 >= 2^{-7} e_3(nu^2), so Z_3 >= 2^{-7} e_3(nu^2) with marginals <= 1/2:
   Theorem D: ||p_Q|| <= 6 sqrt(e) (2^7/e_3(nu^2))^{1/6} <= 22.2 (nu_1 nu_2 nu_3)^{-1/3}.
Condition e_3 >= 72 rho_0^2 e_2 holds if nu_3^2 >= 216 rho_0^2 (since e_3/e_2 >= nu_3^2/3).
So: FOURIER FAILURE AT LEVEL 3 => nu_3(E_{L,.}) < 14.7 rho_0 : the light rows have rank <= 2 up to
operator norm 14.7 rho_0.  With L = [n] (rho_0 = max row norm): no row of norm > |mu_3|/14.7 => Theorem D.
Level 2: same with k = 2: e_2 >= 20 rho_0^2 e_1... D_2 (q = 1) => alpha_2, hence H2'.

## N3. Numerics + structure consequences (and two questions answered).

### N3.1 Numerics (num/check_overlap*.py). Phi formula (with multiplicity |S cap T|) = brute force to 6e-15 on
40 random/structured 8x8 cases (k = 2, 3, random row sets L). Marginal bound alpha_i <= |b_i|^2 e_{k-1}/e_k:
max ratio 1.0000000000000009 (equality at k = 1, as it must). Overlap inequality never violated (60 structured
cases at n = 12, 3 at n = 22); it has positive right side only once rows are small against the spectrum
(k = 2 at n = 12; k = 3 needs rows <= ~0.35 |mu_3|, i.e. n ~ 60+ for random frames). The true overlap fraction
is ~0.5 at these n, the bound allows much more: the inequality is crude but it is enough.

### N3.2 Theorem LF (light-rows Fourier), exact constants.  For ANY row set L with rho_L = max_{i in L} |row_i E|,
nu = sing. values of E_{L,.}:  I = random half of L, J = (L \ I) u (all other coords).
 E Z_3(B) >= 2^{-6} W_3^(L) >= 2^{-6}(e_3 - 4 rho^2 e_2);  E e_2(B) <= e_2/4.
 => E[e_3(B) - 2 rho^2 e_2(B)] >= 2^{-6}(e_3 - 36 rho^2 e_2).
 If e_3(nu^2) >= 72 rho_L^2 e_2(nu^2): some partition has Z_3 >= 2^{-7} e_3(nu^2) and all I-marginals <= 1/2,
 so ||p_Q|| <= 6 sqrt(e) 2^{7/6} e_3(nu^2)^{-1/6} <= 22.2 (nu_1 nu_2 nu_3)^{-1/3}.
 Level 2 (k = 2, D_2 with q = 1): E[e_2(B) - 2rho^2 e_1(B)] >= 2^{-4}(e_2 - 18 rho^2 e_1); if e_2 >= 36 rho^2 e_1:
 Z_2 >= 2^{-5} e_2 with 2-marginals <= 1/2, |phi(t)| <= 2 pi sqrt(e) Z_2^{-1/4}/|t|  => alpha_2 and H2'.
 Uniform in all linear terms (decoupling kills them) and in the diagonal of M (never enters M_IJ).

### N3.3 Consequences when LF fails for every L (level 3; level 2 identical with 72 -> 36, e3/e2 -> e2/e1).
 (a) L = [n]: e_3/e_2 >= mu_3^2/3 forces max row norm > mu_3/sqrt(216) >= (1-c)/14.7.  [NO HUB => FOURIER.]
     Level 2: max row norm > (1-c)/sqrt(72) = (1-c)/8.5.
 (b) L = light rows (norm <= rho_0), K = 72 rho_0^2, y = nu^2, T = sum_{j>=3} y_j. If y_2 >= 4K (nu_2 >= 17 rho_0):
     T < 8K/3 = 192 rho_0^2. (Case T <= y_2: T - K < (5/8)T. Case T > y_2: e_3 > K e_2 by splitting
     e_3 - K e_2 = y1y2(T-K) + (y1+y2)(e_2(t) - KT) + e_3(t) - K e_2(t) and e_2(t) >= T(T-m)/2,
     e_3(t) >= T(T-m)(T-2m)/6, m = max tail <= y_2.)  So LIGHT ROWS = RANK 2 + FROBENIUS < 13.9 rho_0.
 (c) Heavy count: E^2 = B0^T B0 + E_H^T E_H, Weyl => mu_{j+|H|}^2 <= nu_j^2. So |H| = 0 impossible;
     |H| = 1 => nu_2 >= mu_3 (light rows carry two big directions) => normal form:
       E = S + R, S = [[Pi E_LL Pi, Pi E_Lh],[E_hL Pi, 0]] (rank 3, on span(p1,p2) + e_h), ||R||_F <= 2 sqrt(T) < 27.7 rho_0,
       p1, p2 spread: leverage <= rho_0^2/nu_2^2.  This is HUB + (Prop 5.4 form) + Frobenius-small twist.
     |H| >= 2 when nu_2 < 17 rho_0.
 (d) |H| <= N_0 forces ||E_HH||_F <= N_0 sqrt(2c): the hub block is NEGLIGIBLE when there are few hubs; it can
     matter only when |H| >~ rho_0^2/(2c) (many heavy rows). M_HH never enters the
     Fourier step (I is inside L); it enters only (iii) two-hub branch (Prop 5.5 needs A_HH = 0 exactly; see hub_pairs/)
     and the many-heavy-rows bookkeeping, which is where the tree still has a gap.
 (e) A proposed chain, checked: for |t| >= 1/||R||_F Theorem D gives an integrable tail ONLY IF the 3-volume
     marginals are <= 1/2, and in the failure regime the crude criterion (N2.1) is exactly what fails. Refined:
     alpha_i <~ lev_i(top-2) + |row_i(R)|^2 / T, so the tail estimate holds iff R has no row carrying > ~1/3 of
     ||R||_F^2 (R has no sub-hub). Otherwise that row is a smaller hub and must be peeled into S. So the chain
     needs: (T1) twist lemma for Prop 5.4 / Theorem H with a twist of Frobenius norm <= 1/|t|; (T2) a peeling
     step for sub-hubs of R. Neither is proved here.

## N4. The single-hub normal form is degenerate in general; level-2 hub reduction.

### N4.1 |H| = 1 normal form, written in the basis (e_h, w^, v): core S = [[a, k, 0],[k, alpha, beta],[0, beta, gamma]]
(w^ = hub row direction inside span(p1,p2)). Completing the square: S_LL = gamma v~ v~^T + sigma w^ w^T, v~ = v + (beta/gamma) w^,
sigma = alpha - beta^2/gamma. Theorem H applies iff sigma = 0 (hub column k w^ must be independent of the Fresnel
directions on I; with sigma != 0 the (u, y) map u w^ + k y w^ has a kernel and the BL integral diverges).
Absolute-value Fourier gives only |t|^{-1} here: twist inflation of e^{i t sigma L^2} along the hub tilt direction costs
|t sigma|^{1/2}, i.e. |phi| <~ |t|^{-3/2}(1 + |t sigma|)^{1/2}. Prop 5.4 covers sigma != 0 but needs the rest of the form to
be a function of (L, V): a diagonal twist sum d_i X_i^2 (always present in the no-pivot regime, |d_i| < c) breaks it.
EXPLICIT GAP (numerics num/degenerate_hub.py, n = 60): Q = 4 X_h L + 2 L^2 + 2 V^2 + sum d_i X_i^2, L = <w,X>, V = <v,X>
orthonormal spread. Core eigenvalues -1.236, 2, 3.236; EVERY off-diagonal block has rank exactly 2 (20/20 random
partitions), so D, D', D_4, D_5 are blind; Theorem F: leverage of h is 1; MF: Gamma = [[4,2,0],[2,1,0],[0,0,1]] singular;
Theorem H: G~ singular; Prop 5.4: needs d = 0; no pivot; one hub only. Density bounded numerically: 1.67 (d = 0),
1.65 (d = 0.02), 1.45 (d = 0.1), uniform laws; spread laws far smaller. So the canonical open case
(sigma = 0, dense twist) is NOT the only single-hub gap: sigma != 0 with a diagonal twist is open even with R = 0.
Conditioning on X_h turns it into 2(L + x)^2 + 2V^2 + D(X) - 2x^2: a DEFINITE spread rank-2 form plus a diagonal twist,
so it would follow from: (D2) definite spread rank 2 + small diagonal + linear terms has bounded density (open).

### N4.2 Level-2 hub reduction (PROVED). For any M, any coordinate h, a = m_hh, X' = X_{-h}:
Q = a X_h^2 + L' X_h + Q_0(X'), L' = 2<m_{h,-h}, X'> + b_h. Lemma 1.2(ii) with |a||s - kappa| = |Delta_s|/4 gives
  P(|Q - s| <= u | X') <= min(1, 8u |Delta_s(X')|^{-1/2}),  Delta_s = L'^2 + 4a(s - Q_0(X'))   (a = 0 included).
If alpha_1(Delta) = sup_{s,v} P(|Delta_s - z| <= v)/sqrt(v) <= K (Delta_s - Delta_0 is a constant 4as), then
  P(|Q - s| <= u) <= 8Ku (2 + log_+ (1/(8Ku)))  i.e.  alpha_2(Q) <= 8K(2 + log_+ 1/(8K)).
So level 2 at a hub reduces EXACTLY to a level-1 SUBLEVEL bound for the discriminant form Delta, whose matrix is
4(m m^T - a M_{-h,-h}) (one spread large direction 4|m|^2 plus a c-small multiple of the rest). a = 0 recovers Prop 5.3.

## N5. Level one in SUBLEVEL form (alpha_1), and level two for bounded norm.

### N5.1 Theorem A' (PROVED). c <= 1/500, no c-pivot, an eigenvalue >= 1  =>  alpha_1(Q) <= 28.1, all linear terms.
Rows sorted r_1 >= r_2 >= ...; S_k = sum_{j>=k} r_j^2; L_k = {k+1..n}, T_k = {1..k}.
Test(k): S_{k+1} >= 8 r_{k+1}^2. If it holds: coins on L_k, J = [n]\I, E||E_IJ||_F^2 >= S_{k+1}/4 (pair prob 1/4 or 1/2),
pick e_1(E_IJ) >= S_{k+1}/4 >= 2 r_{k+1}^2 => 1-marginals <= 1/2 => (D_1, q=1) |phi| <= e^{1/4}(2pi)^{1/2} Z_1^{-1/4}|t|^{-1/2}
=> (Esseen, int min(1,B t^{-1/2}) <= 4B u^{-1/2}) alpha_1 <= 14.0 e_1(E_IJ)^{-1/4}.
If Test fails for j < k: S_{j+2} < (7/8) S_{j+1}, so S_{k+1} < (7/8)^k S_1; always S_1 <= k(k-1) eps^2 + 2 S_{k+1}.
k = 11: S_1 <= 110 eps^2 + 0.461 S_1 => S_1 <= 204 eps^2 = 408 c < mu_0^2: impossible. So Test holds at some k <= 10 with
S_{k+1} >= (S_1 - 90 eps^2)/2 >= S_1/4, e_1 >= S_1/16, alpha_1 <= 28 S_1^{-1/4} <= 28.1.
With the pivot branch (level-1 certificate 50 c^{-1/2} = 1118): EVERY N with an eigenvalue >= Lambda has
alpha_1 <= 1118 Lambda^{-1/2}. (Stronger than H1'; H1' <= 2 log 28.1 + 2 <= 8.7.)

### N5.2 Hub reduction constant, cleaner: E min(1, 8u|Delta|^{-1/2}) = int_0^1 P(|Delta| < 64u^2/lam^2) dlam
<= int_0^1 min(1, 8Ku/lam) dlam = 8Ku(1 + log_+ 1/(8Ku)).  So alpha_2(Q) <= 8K(1 + log_+ 1/(8K)).
Matrix of Delta = 4(m m^T - a M_{-h,-h}) = -4a (M/a) (Schur complement!).
||N|| >= |m^T N m|/|m|^2 = 4| |m|^2 - a m^T M' m/|m|^2 | >= 4(|m|^2 - |a| ||M'||).
Corollary HR (PROVED): no c-pivot (c <= 1/500), 2 eigenvalues >= 1, ||M|| <= rho_0^2/(2c), rho_0 = mu_0/8.5:
either LF_2 or a row |m| > rho_0; then ||N|| >= 2 rho_0^2, K <= 1118/(sqrt 2 rho_0) <= 6.8e3, alpha_2 <= 16 K <= 1.1e5.
Gap (M-BIG2): hub absorbed by a huge eigen-direction (a m^T M' m ~ |m|^4). Example M = hub + Lambda vv^T, m || v,
a = |m|^2/Lambda: Delta's matrix collapses, but Q = Lambda W^2 + Z^2 is fine (2D projection) - route problem, not a
counterexample. Schur complements at N2 have norm up to ||A||^2/c, so the norm condition does not compose.

### N5.3 Audit notes (second derivations done).
- 6 sqrt(e) 2^{7/6} = 9.892 * 2.245 = 22.21 (LF_3 constant).  sqrt(216) = 14.70; sqrt(72) = 8.49.
- Theorem S(b) case T > y_2 rechecked in three sub-cases (T < 2m, 2m <= T < 4m, T >= 4m); each gives e_3 > K e_2.
- ||R||_F^2 <= 2T in Cor S1: E_LL - Pi E_LL Pi = (I-Pi)E_LL + Pi E_LL (I - Pi), second has the Frobenius norm of
  (I-Pi) E_LL Pi <= ||(I-Pi)E_LL||_F; plus the two hub off-diagonal blocks (I-Pi)E_Lh.
- Strongest case against LF: it could be vacuous in practice because the constant 72 needs rows <~ 0.12 |mu_3|.
  Check: that is exactly the "no hub" regime by definition, and for Wigner-like blocks only e_3/e_2 ~ n rho^2 matters,
  so LF is not vacuous there. It IS weak for moderate n (n = 22 random frames: rows 0.8 > threshold).

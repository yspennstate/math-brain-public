# NOTES - diagonal plus bounded rank (wave 2, piece 02)

Start 2026-09-23 ~02:15 local.

## 0. Reading done
BRIEF, RESULTS, GEOM, FOURIER, COUNTEREXAMPLE, LITERATURE read in full.

## 1. First structural observations (PROVED unless marked)

Notation. A = R M R^T, R n x r orthonormal columns r_k, rows rho_i in R^r, leverages l_i = |rho_i|^2,
M symmetric r x r (any rotation R -> RO, M -> O^T M O allowed). For D != 0: A = D + R M R^T.

1.1 (Closure under Schur complements.) If A = D + R M R^T then A/a_hh = D_{-h} + R_{-h} M' R_{-h}^T with
M' = M - M rho_h rho_h^T M / a_hh (r x r). So the class "diagonal + rank <= r" is closed under 1x1 and 2x2
Schur complements and under principal submatrices. If D = 0, rank drops by one per 1x1 pivot and by two per
invertible 2x2 pivot (Schur rank formula). PROVED (block elimination).

1.2 (Decision tree restricted to the class.) Theorem 5.1 of GEOM only ever passes to Schur complements and
principal blocks, so: the conjecture for the class C(r) = {D + rank <= r} follows from Hyp_1, Hyp_2, Hyp_3
restricted to C(r) intersect {no c-pivot}. For exact rank 3 (D = 0) the tree needs exactly:
  (S1) rank 1, one eigenvalue |mu| >= 1, any linear terms: alpha_1(Q) <= K.
  (S2) rank 2, no c-pivot, both |eig| >= 1: alpha_2(Q) <= K.
  (S3) rank 3, no c-pivot, all |eig| >= 1: ||p_Q|| <= K.
(Branches: definite 2x2 pivot ends; indefinite 2x2 pivot -> rank 1 level 1 (S1); 1x1 pivot -> rank 2 level 2,
which is either a 2x2 pivot (end), a 1x1 pivot -> (S1), or (S2).)

1.3 (S1) is PROVED: rank one lambda u u^T. Either some lambda u_i^2 >= c (1x1 pivot, alpha_1 <= 2 sqrt 2 c^{-1/2},
GEOM L1.2), or all u_i^2 < c/|lambda| <= 1/2 and Theorem F (r = 1) gives |phi(t)| <= (4 pi/|t lambda|)^{1/2}
uniformly in linear terms; Esseen then gives alpha_1 <= C |lambda|^{-1/2}. (Write constants later.)

1.4 (Interlacing structure lemma, the key linear algebra.) Let A = R M R^T have no c-pivot, all |eig(M)| >= 1.
Let H = {i : l_i >= delta}, m = |H| <= r/delta. Then ||A_HH|| <= ||A_HH||_F <= m sqrt(2c) =: tau.
Diagonalise G_H = R_H^T R_H = diag(g_1 <= ... <= g_r) by a rotation (then G_L = I - G_H is diagonal too).
||G_H^{1/2} M G_H^{1/2}|| = ||R_H M R_H^T|| <= tau. For k >= 2 consider the block on {k,..,r}... in particular
for the top two: the principal 2x2 block M_{r-1,r} has norm <= tau/g_{r-1}; by Cauchy interlacing
|lambda_2-from-top| ... precisely: a principal (r-1) x (r-1)... CLEAN FORM (r = 3): M_{23,23} has norm <= tau/g_2,
interlacing gives |lambda_2(M)| <= tau/g_2, so g_2 <= tau. Hence AT MOST ONE direction has H-weight > tau.
General r: the principal block on the directions with g > tau' has all eigenvalues <= tau/tau' in modulus;
a principal j x j block of M with all eigenvalues < 1 in modulus forces ... (interlacing) at most r - j eigenvalues
of M of modulus >= 1 ... for r = 3 with all three eigenvalues large: j <= 1. PROVED for r = 3; for general r:
#(directions with g > tau/1) <= r - #(large eigenvalues) + 1?? (check: interlacing for a principal j-block with
|eig| < 1: eigenvalues of M with |.| >= 1 number at most r - j + ... ) TO CHECK.

Consequence for exact rank 3, no pivot: either g_3 <= 1/2 (then G_L >= I/2, normalized leverages on L are
<= 2 delta, Theorem F on L after conditioning on X_H gives density <= 12 * 2 = 24), or g_3 > 1/2 and
  |M_33| <= tau/g_3 <= 2 tau,  g_1, g_2 <= tau:
ONE hub direction r_3 (more than half its mass on the <= 3/delta heavy coordinates, M_33 ~ 0), the other two
directions almost entirely on L. Rotating in the (1,2)-plane: M = [[p,q,kappa],[q,s,0],[kappa,0,m]],
kappa^2 + m^2 >= 1 (||M e_3|| >= 1), and at m = 0: (M^{-1})_{22} = 1/s so |s| >= 1.
Same for exact rank 2: either Theorem F (r = 2) on L, or one hub direction r_2 with g_2 > 1/2, M_22 ~ 0, g_1 <= tau.

1.5 Theorem H cannot be applied directly in exact rank r: A_Ih = R_I M R_H^T e_h lies in the column span of R_I,
so the vectors rho~_i are confined to an r-dimensional subspace of R^{r+|H|} and det G~ = 0 always.

## 2. The difficulty isolated (exact rank 3, hub case)
Y_3 = P_3 + S_3 (P_3 = <r_3^H, X_H>, weight g_3 > 1/2; S_3 = <r_3^L, X_L>, weight mu_3 = 1 - g_3 < 1/2),
Y_k = P_k + S_k (k = 1,2; weight on H <= tau). When mu_3 = 0 and P_1 = P_2 = 0 this is GEOM Prop 5.4 with the
hub variable P_3 (density <= sqrt 2, independent of X_L). The obstacles: (a) S_3 != 0 (the hub direction leaks
onto L with a small weight but NOT a small value: laws may be spread); (b) P_1, P_2 != 0; (c) linear terms
outside range(R).
Observation (Gaussian model): conditioning on X_h leaves a rank-3 form on L whose weakest eigenvalue is
~ mu_3 det M/(ps - q^2), and the critical value does NOT depend on X_h (the X_h-tilt is absorbed by a shift of S_3).
So "condition on the hub and use Theorem F" loses (1-l)^{-1/3}, and in the indefinite case the conditional density
really is ~ log(1/mu_3). The hub integration must be combined with the weak direction: for |t| << 1/(weak eig)
the tilt is NOT absorbed and the hub gives |t|^{-1}; for |t| >> 1/(weak eig) the weak square gives decay.
Gaussian computation confirms |phi| <~ |t|^{-3/2} uniformly in mu_3.

## 3. Definite rank three and the tree (PROVED, constants to be written)

3.1 Definite exact rank 3 (all lambda of one sign) is PROVED by the tree, with Theorem F at every leaf:
 - PSD with |eig| >= 1 gives a_ii = rho_i^T M rho_i >= l_i. So "no c-pivot" forces all l_i < c <= 1/2 and
   Theorem F (r = 3) gives density <= 12.
 - a 1x1 pivot gives A/a_ii PSD of rank 2 with both eigenvalues >= 1 (Lemma 1.5); again either a leverage >= c
   (pivot -> rank-1 PSD -> (S1)) or all leverages < c and Theorem F (r = 2): |phi| <= 4 pi/|t| -> alpha_2.
 - a definite 2x2 pivot ends the tree.
 Everything is uniform in the linear terms (Theorem F is; pivots are). So |P X - y_0|^2 type forms and every
 definite rank-3 form with any linear term have universal constants. (GEOM Sect. 4 thought this needed the e_1,e_2
 versions of Theorem D; Theorem F with r = 1, 2 supplies them directly.)

3.2 Indefinite: Theorem C covers the one-sheet side for every leverage profile, but only with linear terms
inside range(R). Remaining: two-sheet side, and linear terms outside the range.

## 4. The hub + L^2 obstruction (analysis; nothing proved yet)
Hub normal form (single hub coordinate h, rho_h = (0,0,sqrt l)):
  Q = 2 kappa S_1 Z + p' S_1^2 + s S_2^2 + m_0 Z^2 + (linear),  Z = sqrt(l) X_h + eps W,  eps^2 = 1 - l,
  (S_1, S_2, W) orthonormal projections of X_L.
(i) eps = 0: GEOM Prop 5.4 (real variable) - bounded.
(ii) p' = 0 (no L^2 term) and m_0 = 0: Theorem-H-type Fourier bound works and is ROBUST to the leakage:
   |phi(t)| <= int dx |E_{X_L} e^{itQ}|, inner = Fresnel on S_2 ... the hub integral over x is Lebesgue-translation
   invariant, so a shift of Z by eps W costs nothing IF the rest of the form is a product twist. It is not
   (2 kappa eps S_1 W is a bilinear cross term) -> must Fresnel it -> det loses eps. So even (ii) is not free.
(iii) p' != 0: Fourier with absolute values fails intrinsically: after the 3D Fresnel formula
   phi = C_t int e^{-i u^T M^{-1} u /(4t)} psi_h(sqrt l u_3) Psi_L(u) du, the u_3-phase has coefficient
   (M^{-1})_{33} = -p'/kappa^2 (m_0 = 0), and int e^{-i N u^2 - i y u} psi_h(u) du is a Schroedinger evolution of
   f_h, which for resonant sets is ~ |N|^{-1/2} (not bounded). Hub + L^2 is real-variable territory.
(iv) Real-variable (Prop 5.4 route) with leakage reduces to a MIXED NORM: int sup_{sigma} rho_{S_1 S_2 W}(sigma, w) dw,
   or equivalently a bound on the conditional density of S_2 given (S_1, W). For non-spread projections the mixed
   norm is unbounded (difference sets of combs: A-B of two measure-one combs has measure ~ 2N). For spread ones it
   is plausible (CLT) but I see no proof without moments.
So the precise open core of exact rank 3 is: hub + L^2 term + leakage of the hub direction onto light
coordinates, on the two-sheet side (the one-sheet side is Theorem C when b is in the range).

## 5. (03:25) Discriminant identity -> (S2) PROVED in full; the density version and why it stops

5.1 Discriminant (PROVED, checked numerically num/check_identities2.py, errors 1e-13). Coordinate j, X' = X_{-j}.
Given X', Q = a X_j^2 + 2 M' X_j + C', a = A_jj, M' = <alpha, X'> + m0 (alpha = A_{-j,j}), C' = X'^T B X' + <beta,X'> + c0.
Delta_s := M'^2 - a (C' - s) has quadratic part N = alpha alpha^T - a B = -a (A/a_jj) (= alpha alpha^T if a = 0).
 * A = R M R^T rank 2: N has rank <= 1 and its nonzero eigenvalue is  -det(M) l_j  (INDEPENDENT of a).
 * rank 3, basis with rho_j = sqrt(l_j) e_3, c = (M_13, M_23), P = M_{12,12}: N has rank <= 2,
   det = l_j a det M, trace = l_j (|c|^2 - M_33 tr P). For a hub (a ~ 0): eigenvalues ~ l kappa^2 and ~ a det M/kappa^2.
1D lemma: for g(x) = a x^2 + 2 M' x + C' and density <= 1, P(|g(X_j) - s| <= u) <= min(1, 4u/sqrt|Delta_s|), all a
(including a = 0). [Complete the square: |a y^2 - Delta/a| <= u; sqrt(A+B) - sqrt(A-B) <= 2B/sqrt A; the
cases Delta < 0 and u|a| > |Delta| checked separately.] Also the density: p_{Q|X'}(s) = sum_pm f(x_pm)/(2 sqrt Delta_s).

5.2 (S2) PROVED: rank 2, both |eig| >= 1, ANY linear terms, ANY configuration: alpha_2(Q) <= C.
 - all leverages <= 1/2: Theorem F (r = 2): |phi| <= 4 pi/(|t| sqrt|det M|), Esseen.
 - some l_j > 1/2: P(|Q - s| <= u) <= E min(1, 4u/sqrt|Delta_s|), Delta_s = mu <v,X'>^2 + (linear) + const,
   |mu| = |det M| l_j >= 1/2. alpha_1(Delta_s) <= C (rank one, any linear terms: light v -> Theorem F r = 1 + Esseen;
   heavy v_k -> 1D quadratic in X_k, Lemma 1.2(ii)). Then E min(1, 4u/sqrt|D|) = int_0^1 P(|D| < 16u^2/th^2) dth
   <= 4 a1 u (1 + log_+(1/(4 a1 u))).
 This is the same as Lemma X' of folder 03 (found independently there); it removes the hub-with-small-diagonal
 difficulty at level 2 for rank 2 (the hub diagonal a does not enter mu).
 Consequence: the exact-rank-3 tree is complete except its no-pivot leaf (S3).

5.3 Density analogue: p_Q(s) <= E[Delta_s^{-1/2}; Delta_s > 0] (f <= 1). For rank 3 Delta_s is a rank-2 form whose
small eigenvalue is ~ a det M/kappa^2, so this gives ~ (|a| |det M|)^{-1/2}: a pivot bound, useless for the hub.
At a = 0 exactly, Delta = M'^2 and E|M'|^{-1} = infinity: the hub needs the V^2 regularisation (Prop 5.4).

5.4 Leakage bookkeeping: localized leakage is removable. If the leakage vector w (r_3 = sqrt(l) e_h + eps w) is
supported on a set J_w, condition on X_{J_w}: W becomes a constant, Z = sqrt(l) X_h + const, and s_1, s_2 lose only
their J_w-parts (mass <= |J_w| delta); the new linear terms lie in span(s_1', s_2') (in range). So only SPREAD leakage
of small mass is a genuine obstruction, and spread leakage of mass eps^2 >= eps_0 is Theorem F on L (bound eps_0^{-2/3}).

5.5 Numerics (num/hub_leak.py): hub + L^2 + leakage, n = 40, eps in {0, .05, .2, .5}, uniform and comb hub laws:
peak density flat in eps (e.g. 3.31, 3.38, 4.18, 3.51 / 2.86, 2.95, 2.95, 2.93). No growth. (Test matrices were not all
normalised to |eig| >= 1; the point is only the flatness in eps.)

## 6. (03:4x) Two more findings

6.1 Hub case, D_2 decoupling gives |phi(t)| <= C/|t| uniformly in the leakage (PARTIAL, sketch):
 J = H u L_J, I = L_I (balanced random split of L). Rows 1,2 of M after the rotation are (p,q,kappa), (q,s,0);
 the 2x2 minors of the (strong rows) x (all columns) block are -kappa s, -kappa q, ps - q^2, and q^2 + s^2 = |M e_2|^2 >= 1,
 so Z_2 = e_2(A_IJ^T A_IJ) >= c kappa^2 (q^2 + s^2) >= c (1 - m^2): Theorem D_2 (k = 2, q = 1, 2-marginals <= 1/2)
 gives |phi| <= e^{1/2} (2 pi/|t|) Z_2^{-1/4}. With Theorem F on L (spread leakage of mass eps^2) for |t| > eps^{-2}:
 density <= C (1 + log(1/eps)). So the leaky hub is at worst logarithmic in the SPREAD leakage mass.
 Caveat: for leakage profiles that are never spread relative to their own mass (geometric w_i^2 = 2^{-i}), neither
 Theorem F nor Theorem D gives the high frequencies; conditioning on the top leakage coordinates only shrinks eps.

6.2 D + rank r, no pivot (PROVED linear algebra): with H = {l_i >= delta}, A_HH = D_H + R_H M R_H^T has norm <= tau, so the
 rank-r matrix R_H M R_H^T is within tau of -D_H; by Weyl at most r heavy coordinates have |D_hh| > tau (set H_1), their
 rows rho_h are M-orthogonal with rho_h^T M rho_h ~ -D_hh, and the rest H_0 is M-null. Each h in H_1 is a HUB created by
 diagonal cancellation, and B_LL contains the rank-one "L^2 term" along its coupling vector: D + rank 1 already gives
 hub + L^2 (v = (e_h + w)/sqrt 2: offdiag(lambda v v^T) = (lambda/2)(e_h w^T + w e_h^T + offdiag(w w^T))).
 So for D != 0 the Prop-5.4 configuration comes WITH a diagonal twist sum d_i X_i^2 on the light coordinates, which
 Prop 5.4 does not allow (it needs the rest to be a function of (L,V)) and Theorem H does not allow either (coupling
 direction = L^2 direction, det G~ = 0). Unifying open core: hub + L^2 term + (leakage | diagonal twist | outside
 linear term).

## 7. (03:30) The pointwise Rudelson-Vershynin correction; final checks
- RV Lemma 3.1 pointwise form: NOT used anywhere here. Everything Fourier goes through Lemma 1 (L^p), Theorem F,
  Theorem D / D_k, and the Fejer-kernel Esseen bound P(|Z-s|<=h) <= 1.0877 h int_{|t|<=1/h} |phi_Z| (K(x) = (sin(x/2)/(x/2))^2
  >= 0.9194 on |x| <= 1, K^ = 2 pi (1-|t|)_+).
- REPORT goes into the final message (subagents cannot create REPORT.md); a copy is saved as REPORT_02.md here.
- Hub normal form: |s| >= 1 PROVED: x = (0, kappa, -q), M x = (0, s kappa, -m q); |Mx| >= |x| gives
  s^2 kappa^2 + m^2 q^2 >= kappa^2 + q^2, so s^2 >= 1 when m^2 <= 1.  kappa^2 >= 1 - m^2 from |M e_3| >= 1.
- Leak-free hub via Prop 5.4: D_H = |det M|/(|s| kappa^2) (identity det M = -s(kappa^2 - m p'), p' = p - q^2/s);
  |det M| >= ||M|| >= max(kappa, |s|) makes 4 Psi(D_H)/sqrt(kappa |s|) universally bounded.
- Constants: alpha_1(rank 1) <= 15.43 |mu|^{-1/2} (light), 4 |mu|^{-1/2} (heavy); alpha_2(rank 2) <= 27.4 (light), <= 88 (heavy).

## 8. (03:4x) Log bound for the spread leaky hub - PROVED; cited results checked
Single hub h (l_h > 1/2), frame r_1 = s_1, r_2 = s_2 (vanish at h), r_3 = sqrt(l) e_h + eps w, light frame (s_1,s_2,w)
orthonormal on L = [n]\h with all leverages lambda_i <= 1/50. Random split L = I u L_J, J = {h} u L_J; with prob >= 0.87
(GEOM Prop 4.2 Chernoff) Gamma_I, Gamma_J >= I/4 where Gamma = Gram of (s_1,s_2,w) on the part.
 - G_I = D Gamma_I D (D = diag(1,1,eps)) >= Pi_12/4; G_J >= diag(1/4,1/4,l) >= I/4.
 - e_2(N^T N), N = G_I^{1/2} M G_J^{1/2}: N^T N = G_J^{1/2} M G_I M G_J^{1/2} >= (1/4) G_J^{1/2} M Pi_12 M G_J^{1/2};
   e_2 monotone; e_2(Q X^T X Q) = det(X Q^2 X^T) >= det(X X^T)/16 (X = rows 1,2 of M); det(X X^T) = kappa^2 s^2 + kappa^2 q^2
   + (ps - q^2)^2 >= kappa^2 (q^2 + s^2) >= 1 - m^2.  So Z_2 >= (1 - m^2)/256.
 - 2-marginals on I: u_m in range(R_I); leverage of i there = (s_1,s_2,w)(i) Gamma_I^{-1} (.)^T <= 4 lambda_i; alpha <= 8/50 < 1/2.
 - D_2 (k=2, q=1): |phi| <= e^{1/2} 2 pi |t|^{-1} Z_2^{-1/4} <= 41.7/|t| (m^2 <= 0.1).
 - Theorem F on L given X_h: |phi| <= (4 pi)^{3/2} |t|^{-3/2} (|det M| eps^2)^{-1/2} <= 44.6 eps^{-1} |t|^{-3/2}.
 => ||p_Q|| <= C_1 + C_2 log_+(1/eps), any linear terms. (constants recomputed in report)
Cited: 10 Thm 5.1 needs the cross block A_{IJ0} of low rank with the hub rows independent of it (Q_I full rank) -> fails
for hub + L^2 (the L^2 direction is the hub partner). 04 Cor 3.2 = Theorem H with B_KI = 0 (same obstruction).
09 Thm 2: >= 2 hubs with private leaves. 01 Thm 4: small |A|-diagonal -> Theorem D; Cor 6 (open only on two-sheet side)
tacitly assumes in-range linear terms (Theorem C needs them).
Also: in the no-pivot hub configuration at most TWO coordinates have l > 1/2 (heavy rows have r_1^2 + r_2^2 <= 2 tau,
r_3 is a unit vector), and if two, both have l <= 1/2 + 2 tau.

## 9. Report draft, part 1 (sections 0-2)
[Setting; tools T1-T6 (Lemma 1, Theorem F conditioned form, D_2 with q = 1, Fejer-Esseen 1.0877, GEOM lemmas,
Theorem H, Theorem C).]
L1.1 Schur closure: A/a = D_{-h} + R_{-h}(M - M rho rho^T M/a) R_{-h}^T; D = 0 -> rank drops by 1 (2).
L1.2 Interlacing: principal k-block of M with norm < 1 and all |eig M| >= 1 => 2k <= r, >= k eigenvalues >= 1 and <= -1.
L1.3 Heavy directions: ||A_HH|| <= tau = |H| sqrt(2c); leading k-block of M (G_H-diagonal basis) has norm <= tau/g_k;
     at most floor(r/2) directions with H-weight > tau; definite M => all l_i < c.
L1.4 Hub normal form: M = [[p,q,kappa],[q,s,0],[kappa,0,m]], |m| <= 1 => kappa^2 >= 1-m^2, q^2+s^2 >= 1, |s| >= 1
     (x = (0,kappa,-q)), det M = -s(kappa^2 - m p').
L1.5 Discriminant: N = alpha alpha^T - a B; rank 2: single eigenvalue -det(M) l_j; rank 3: det l a det M, trace
     l(|c|^2 - M_33 tr P); 1D bound min(1, 4u/sqrt|Delta|); density sum f/(2 sqrt Delta).
L1.6 Diagonal cancellation (Weyl): at most r heavy coordinates with |D_hh| > tau; they are hubs; example D + rank 1.
P2.1 alpha_1(rank 1) <= 15.5 |mu|^{-1/2}.  P2.2 alpha_2(rank 2, |det M| >= 1) <= 88, any configuration/linear terms.
T2.3 Exact rank 3 with a c-pivot: ||p_Q|| <= 176 c^{-1/2} (definite 2x2: pi c^{-1/2}; indefinite 2x2: 72 c^{-1/2};
     1x1: 176 c^{-1/2}).

## 10. REPORT DRAFT, part 2 (sections 3-6), condensed
T3.1 exact rank 3, no c-pivot (c <= 1/100): (a) max l <= 1/2 -> <= 12; (b) M definite -> (a) [definite rank 3 <= 249 overall,
 any b]; (c) h with l_h > 1/2: |a_hh| < c, basis rho_h = sqrt(l) e_3, m = a_hh/l, r_1,r_2 vanish at h,
 r_3 = sqrt(l) e_h + eps w, Q = F(S_1,S_2,Z) + <b,X>, Z = sqrt(l) X_h + eps W; light-frame leverages lambda_i.
 (c1) max lambda <= 1/2: <= 12 eps^{-2/3};  (c2) max lambda <= 1/50: <= 41 + 27 log_+(1/(6 eps)), any b;
 (c3) eps = 0, b in range: <= 278 (Prop 5.4; D_H = |det M|/(|s| kappa^2), |det M| >= max(kappa,|s|), |s| >= 1);
 (c4) eps = 0, p' = 0, max lambda <= 1/2: <= 7.6 any b (Theorem H, |phi| <= (4pi)^{3/2}(2 kappa)^{-1}|s|^{-1/2}|t|^{-3/2});
 (c5) b in range, one-sheet side: <= pi sqrt 2 (Theorem C).
OPEN (T3.2): no pivot, indefinite, null heavy h, and (O1) 0 < eps small with two-sheet side or b outside range
 [at most log growth when light frame spread]; (O2) eps = 0, p' != 0, b outside range; (O3) light frame not spread.
Missing estimate (LH): E[f(A(S_1,S_2) - eps W) 1{|S_1|<1}/|S_1|] <= C uniformly in eps, f <= 1, int f = 1, spread (S_1,S_2,W).
T4.1 definite exact rank r (all lambda >= 1): <= 304, uniform in r (1x1 pivots at threshold 1/2 + Theorem F).
T4.2 exact rank r, all |eig| >= 1: lambda_max(G_H) <= 1/2 (H = {l >= 1/4}) -> <= 8r/(r-2) <= 24; else <= floor(r/2)
 nearly isotropic hub directions. Pivot branches for r >= 4: discriminant + D_1 (sketch, PARTIAL).
R4.3 D != 0: spread regime by Theorem D (01 Thm 4, 06 Thm S); cancellation hubs carry square along partner + diagonal
 twist = same open core with the outside linear term replaced by the twist.

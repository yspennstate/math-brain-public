# NOTES - 14_real_variable_hub_dense

Target: Q = a X_h^2 + 2 X_h (L + beta) + lambda (V + gamma)^2 + X'^T E X' + b^T X',
X' = (X_i)_{i != h}, L = <w,X'>, V = <v,X'>, w ⊥ v unit, small entries, |lambda| >= 1, |a| < c,
E symmetric, no c-pivot, ||E||_op <= eps. Want ||p_Q||_inf <= C (indep. of n, eps, E, b).

## 0. Reductions and the exact formula (all elementary)

(R1) WLOG b ⊥ w, v. Write <b,X'> = b_w L + b_v V + B, B = <b_perp, X'>. b_v V is absorbed in gamma
(complete the square, constant changes). b_w L: 2X_h(L+beta) + b_w L = 2(X_h + b_w/2)(L + beta) - b_w beta;
X_h' = X_h + b_w/2 has density <= 1; a X_h^2 = a X_h'^2 - a b_w X_h' + const, so beta -> beta, and a new
linear term -a b_w X_h' in the hub coordinate appears; that is absorbed by completing the square in X_h' only
if a != 0 ... simpler: keep a general linear term c_h X_h. So the family is
  Q = a X_h^2 + 2 X_h (L + beta) + c_h X_h + lambda (V+gamma)^2 + R(X'),   R = X'^T E X' + <b_perp, X'>,
and c_h X_h can be folded into beta (2 X_h (L + beta + c_h/2)). So WLOG b ⊥ w, v, no hub linear term.

(R2) Separable remainders. Diagonal of E and b are both of the form sum_i phi_i(X_i). It is natural to allow an
arbitrary separable remainder S(X') = sum_i phi_i(X_i) (phi_i measurable). Fourier Theorem H already extends to
this (its proof only needs |g_i| <= f_i with g_i = e^{i t phi_i} f_i). So write E = E_off + diag, and the target is
  Q = a X_h^2 + 2 X_h (L+beta) + lambda (V+gamma)^2 + X'^T E_off X' + S(X').

(F) Exact formula (Fubini, conditioning on X' is lossless). With G(x,X') = a x^2 + 2(L+beta)x + F(X'),
F = lambda (V+gamma)^2 + R:
  p_Q(s) = E_{X'} sum_{x: G(x,X') = s} f_h(x) / (2 |a x + L + beta|).
Roots with |a x + L + beta| >= 1 contribute <= 1 in total (<= 2 roots, each <= 1/2) - for ANY remainder.
So only the region |a X_h + L + beta| < 1 (hub slope small) matters.

## 1. Theorem D when ||E_off||_F is large - checked

Claim: if ||E_off||_F >= eta_0, Theorem D (hub in J) bounds the density. Check:
- Random split I u J' of the non-hub coordinates, J = {h} u J'. M = A_IJ = w_I e_h^T + lambda v_I v_{J'}^T + E_{IJ'}.
  The rank-2 part N has singular values ~ |w_I| ~ 2^{-1/2} and |lambda| |v_I||v_J'| ~ |lambda|/2 (w ⊥ v; <w_I,v_I> ~ 0
  up to max-entry fluctuations). sum_{k>=3} s_k(M)^2 = dist_F(M, rank<=2)^2 >= sum_{k>=5} s_k(E_IJ')^2
  >= ||E_IJ'||_F^2 - 4 eps^2 (M - M_2 = E + (N - M_2), rank(N - M_2) <= 4). Z = e_3 >= s_1^2 s_2^2 sum_{k>=3} s_k^2.
- E ||E_{IJ}||_F^2 = (1/2) sum_{i<j} E_ij^2 = ||E_off||_F^2 / 4 over the random split. So OK for E_OFF, not E:
  the DIAGONAL of E is invisible to A_IJ (E = eps I has ||E||_F = eps sqrt n but E_IJ = 0). The diagonal part is
  separable, so it goes into S(X') of (R2); Theorem H handles hub + rank one + separable exactly.
- Marginal condition alpha_i <= 1/2: alpha_i ~ u_1(i)^2 + u_2(i)^2 + sum_{k>=3} (s_k^2 / sum_{j>=3} s_j^2) u_k(i)^2.
  Fails only if one row of E_off carries a constant fraction of ||E_off||_F^2; since each row has norm <= eps,
  that needs ||E_off||_F <~ eps. So for ||E_off||_F >= eta_0 >> eps it holds (after a Chernoff/second-moment
  choice of the split). VERDICT: lead is valid for E_off. We may assume ||E_off||_F <= eta_0 (any fixed eta_0,
  constant C(eta_0) = O(eta_0^{-1/3})).
- BUT the follow-up claim "X'^T E X' - E[..] has L^2 size <= eta_0" is FALSE in general: laws may be
  uniform on spread sets (Madiman-Melbourne-Xu), variances unbounded; Var(X'^T E_off X') ~ sum E_ij^2 s_i^2 s_j^2.
  And spread laws cannot be decomposed into mixtures of bounded-support laws with density <= 1 (a set S of measure 1
  made of N tiny intervals at mutual distance >> 1 has |S ∩ I| < 1 for every interval I of length O(1)).
  So "small in L^2" is only available after some conditioning that localizes; a real-variable argument must be
  scale-free.


## 2. Where step (1) (linear terms outside span(w,v)) really lives

Take E = 0, a = 0 first, b ⊥ w,v, B = <b,X'>. Two equivalent exact forms of the density:
 (F1) condition on X_h: p_Q(s) = int f_h(x) p_{Q_x}(s) dx, Q_x = lambda (V+gamma)^2 + <2xw + b, X'> + const.
      For fixed x this is ONE square plus a linear form Y_x orthogonal to v with coefficient
      mu_x = |2xw + b| = (4x^2 + |b|^2)^{1/2} >= 2|x|.
 (F2) condition on X': p_Q(s) = E K_s(L, F), F = lambda(V+gamma)^2 + B,
      K_s(l, phi) = f_h((s - phi)/(2(l+beta))) / (2|l+beta|); int K_s(l, .) dphi = 1, K_s <= 1/(2|l+beta|).
Both reduce the problem to one of:
 (PL)  Parabola lemma: for orthonormal v, y, the density of lambda(V+gamma)^2 + mu Y is <= C (|lambda| |mu|)^{-1/2}.
       PL => (via F1) p_Q <= C |lambda|^{-1/2} int f_h(x) (2|x|)^{-1/2} dx <= 2C |lambda|^{-1/2}. [any a: a x^2 is a constant for fixed x]
 (JPL) Joint form: sup_l sup_s int_{|phi - s| <= u} rho_{L,F}(l, phi) dphi <= C |lambda|^{-1/2} u^{1/2}.
       JPL => (via F2, hub uniform; general f_h by bathtub over sets of measure 2|t|) bounded density.
PL is proved below in three sub-cases; the SPREAD case (all |v_i| small) is exactly the mixed-norm obstacle:
density of lambda(V+c)^2 + mu Y = int dy Sum_roots rho_{VY}(v,y)/(2|lambda||v+c|) <= |lambda|^{-1/2} int m(y) |s - mu y|^{-1/2} dy,
m(y) = sup_v rho_{VY}(v,y); int m can be infinite for two coordinates with spread sets (difference sets).

PL sub-cases (PROVED, elementary):
 (a) some |v_i| >= c: condition on X_{-i}. Z is a 1D quadratic in X_i, leading coeff lambda v_i^2, critical value
     kappa = mu <y_{-i} - (y_i/v_i) v_{-i}, X_{-i}> + const; that coefficient vector has norm |mu| (v_i^2+y_i^2)^{1/2}/|v_i|
     (orthonormality: |y_{-i}|^2 = 1-y_i^2, |v_{-i}|^2 = 1-v_i^2, <y_{-i},v_{-i}> = -y_i v_i). kappa has density <= M :=
     sqrt2 |v_i| / (|mu| (v_i^2+y_i^2)^{1/2}); E|s-kappa|^{-1/2} <= 2 sqrt(2M) (bathtub). Lemma 1.2(i):
     p_Z <= (|lambda| v_i^2)^{-1/2} * 2 sqrt(2M) = 2^{7/4} (|lambda||mu|)^{-1/2} |v_i|^{-1/2} (v_i^2+y_i^2)^{-1/4}
        <= 2^{7/4} c^{-1} (|lambda||mu|)^{-1/2}.
     Loses 1/|v_i| for spread v: useless in the spread regime.
 (b) v, y with disjoint supports: V, Y independent; p_Z <= sqrt2 |lambda|^{-1/2} E|s - mu Y|^{-1/2} <= 2^{9/4} (|lambda||mu|)^{-1/2}.
 (c) group version of (a): if there is I with y_I = alpha v_I exactly, then with W = V_I (density <= sqrt2/|v_I|,
     independent of X_{I^c}) Z is a 1D quadratic in W with leading coeff lambda and critical value
     mu <y_{I^c} - alpha v_{I^c}, X_{I^c}> + const, so p_Z <= C |v_I|^{-1} |lambda|^{-1/2} (|mu| |y_{I^c} - alpha v_{I^c}|)^{-1/2}.
     Generic spread (v,y) has no exactly-parallel group; an approximate group leaves a perturbation mu <y_I - alpha v_I, X_I>
     that is linear in the same coordinates (small coefficients, NOT small values - spread laws).

## 3. Two further inputs (checked)
 - Theorem D for ||E_off||_F >= eta_0: valid (Section 1), diagonal part must be kept separable.
 - Twist lemma FALSE (04_twist_lemma N2): int |E e^{iu<v,X> + i kappa <v,X>^2}| du = infinity for bumpy laws.
   Consequence for me: the compression of E onto span(w) (a kappa L^2 term) and onto span(w,v) must stay INSIDE the
   real-variable step. GEOM Prop 5.4 already allows F(L,V) = lambda(V - v_c(L))^2 + sigma_F L^2 + affine, i.e. the exact
   compression P E P with P = proj onto span(w,v) is covered (the hub pair (X_h, L) gets matrix [[a,1],[1,sigma_F]]).
   So write E = P E P + (E - P E P); the first is absorbed into F(L,V); the second has no component in span(w,v) x span(w,v).
 - Positive tools N3 (L^2 Plancherel bound for any phase), N4 (block lemma) noted; not yet used.

## 4. The universal obstruction: one mixed-norm / curve-integral estimate

Observation A (Fourier already covers step (1)). For spread (w,v) (normalized leverages <= 1/2 on I = all non-hub
coordinates), Theorem H with H = {h}, r = 1 (the V-square), rho~_i = (v_i, w_i), G~ = I_2 gives
|phi(t)| <= (2|t|)^{-1} (4 pi |t lambda|)^{-1/2} (4 pi)^2, integrable, for ANY a, ANY linear terms and ANY separable
remainder sum phi_i(X_i) (its proof only uses |g_i| <= f_i). So "E = 0 or diagonal, b arbitrary" is PROVED by Fourier.
What Fourier cannot do: (i) dense E (twist lemma false, 04_twist_lemma N2); (ii) the milestone
Q = 4X_hL + 2L^2 + 2V^2 + D (frame (w_i, v_i, 2w_i) degenerate). Real-variable is needed exactly there.

Observation B (every real-variable route hits the same estimate). Write F = lambda(V+gamma)^2 + sigma_F L^2 + T, where T
collects everything that is not a function of (L,V) (orthogonal linear term, diagonal twist, dense part). Formula (F2):
p_Q(s) <= 1 + E[f_h(x*)/(2|t|); |t| < 1], t = L + beta (a=0; a != 0 same after Prop 5.4's substitution).
Needed: (JPL-T) sup_l sup_{|S| <= u} int_S rho_{L,F}(l, phi) dphi <= C |lambda|^{-1/2} u^{1/2}.
Conditioning on X_h instead gives, for the milestone, the definite form 2(L+x)^2 + 2V^2 + T, whose density is EXACTLY
  (1/(2 sqrt det)) int dtau int_0^{2pi} dtheta rho_{P,T}(p0 + r(s - tau) e(theta), tau),   P = (L,V),
<= (pi/2) int sup_p rho_{P,T}(p, tau) dtau  (mixed norm L^1_tau L^inf_p).
And PL (one square + orthogonal linear) is bounded by |lambda|^{-1/2} int sup_v rho_{V,Y}(v,y) |s - mu y|^{-1/2} dy.
All three are controlled by mixed norms of the joint law of (projection, remainder). The mixed norm itself is FALSE as a
bound for two coordinates with spread sets (difference sets), although PL is true there (Section 2(a)); so mixed norms
are too lossy and the real estimate is a curve/parabolic-strip estimate for sums of independent vectors.

Observation C (Darmois-Skitovich). For non-Gaussian product laws, <a,X> and <c,X> are independent iff a, c have disjoint
supports. So no linear re-coordinatization decouples V from (L, B) when all three vectors are spread: an argument must
handle genuinely dependent projections. Freezing works only for perturbations supported off a block that carries the frame:

Lemma (block freezing, PROVED, elementary). Split the non-hub coordinates as K u I. Suppose the remainder R satisfies
R(X') = R_0(X_K) + <c(X_K), (L_I, V_I)> + F_I(L_I, V_I), i.e. every term of R that involves X_I is a function of the two
projections L_I = <w_I, X_I>, V_I = <v_I, X_I> (plus terms linear in them with X_K-dependent coefficients), and F_I is of
Prop 5.4 form. Then conditionally on X_K the form is exactly Prop 5.4 on I with the frame (w_I, v_I) (non-orthonormal:
rescale; rho_{L_I V_I} <= 2 / sqrt(det Gram_I)), so ||p_Q|| <= C(Gram_I, D_H). Conditioning on X_K is lossless.
[Real-variable analogue of 04's N4 block lemma. Covers: E supported on K x K plus rank-<=2 couplings of K to span(w_I,v_I);
b_I in span(w_I, v_I); any b_K, any twist on K.]

## 5. KEY IDEA: a hybrid. Real variable for the pair (X_h, L), Fourier only at FIXED L.

The two tools fail on complementary parts:
 - Fourier (Theorem H) cannot linearize the hub-direction compression kappa L^2 (N12 of 04), nor an LV cross term
   (aligned twists, N2/N7).
 - Real variable (Prop 5.4) cannot handle the V-square's dependence on T (orthogonal linear terms, diagonal twist).
Resolution: condition on X' (lossless) and keep L as a REAL variable. At fixed L = l every function of L is a constant
and every L*V term is linear in V; only then use Fourier, in the single variable g = value of the remainder.

(R*) Exact formula (any remainder). Q = a X_h^2 + 2 X_h (L+beta) + F(X'), F arbitrary measurable.
   p_Q(s) = E_{X'} k_L(F),  k_l(phi) = sum_{x: a x^2 + 2(l+beta)x = s - phi} f_h(x)/(2|a x + l + beta|).
   Roots with |ax+t| >= 1 give <= 1. So p_Q(s) <= 1 + I(s), I(s) = int dl  int nu_l(dphi) k_l^{<1}(phi),
   nu_l = joint law of (L, F) disintegrated along L (mass rho_L(l) <= sqrt2).
   If F = F_1(L, V) + T with F_1(l, v) = lambda v^2 + (m_1 l + m_0) v + (k_2 l^2 + k_1 l + k_0)  [i.e. ANY quadratic in (L,V)
   with V^2-coefficient lambda, e.g. the full compression P E P], then at fixed l: F = lambda (V + gamma_l)^2 + c_l + T.

(CSP) Conditional square-root profile: for a.e. l, all gamma, all intervals S,
   int_S nu_l^{G}(dg) <= K |lambda|^{-1/2} |S|^{1/2},  G = lambda (V+gamma)^2 + T,  nu_l^G = law of (L, G) at L = l.
   (CSP_gen = same for all measurable S, i.e. a uniform weak-L^2 bound; needed for general hub laws.)

Lemma H1 (CSP from a twist bound, PROVED). Let m_tau(l) := d/dl E[e^{i tau G}; L <= l]. If xi -> E e^{i xi L + i tau G}
is integrable, m_tau(l) = (1/2pi) int e^{-i xi l} E e^{i xi L + i tau G} d xi, so
   |m_tau(l)| <= (1/2pi) int |E e^{i xi L + i tau G}| d xi <= (1/2pi) (4 pi |tau lambda|)^{-1/2} J(tau),
   J(tau) := int int |E exp(i xi L + i u V + i tau T)| d xi du      [Fresnel (3.1) on the V-square, centre gamma is a phase].
Interval S of length u: 1_S <= C Phi_u(. - c) with Phi_u >= 0, supp Phi_u^ in [-2/u, 2/u], |Phi_u^| <= C u (Fejer kernel).
Then int_S nu_l <= C (1/2pi) int_{|tau| <= 2/u} C u min(sqrt2, (1/2pi)(4 pi|tau lambda|)^{-1/2} J) d tau <= C' J |lambda|^{-1/2} u^{1/2}.
 * T separable (T = sum phi_i(X_i): diagonal matrix + ANY linear term): J(tau) <= (4 pi)^2 det(G)^{-1/2} by Theorem F's BL
   computation with g_i = f_i e^{i tau phi_i}, frame (w_i, v_i), leverages w_i^2 + v_i^2 <= 1/2. So CSP (intervals) PROVED.
 * T dense (zero-compression E'): J(tau) is exactly the twist-lemma quantity for zero-compression twists (TL0) - OPEN (04 N9/N10).

Theorem H2 (hybrid, a = 0, interval hub law, PROVED given CSP for intervals). X_h uniform on an interval of length 1.
   k_l = 1_{s - 2 t J}/(2|t|) is an interval indicator; bathtub not needed:
   I(s) <= int_{|t|<1} (2|t|)^{-1} K|lambda|^{-1/2} (2|t|)^{1/2} dt = 2 sqrt2 K |lambda|^{-1/2}.
   So ||p_Q|| <= 1 + 2sqrt2 K|lambda|^{-1/2}.  With T separable: covers
   Q = 2 X_h (L+beta) + k_2 L^2 + m_1 L V + lambda (V+gamma)^2 + sum_i d_i X_i^2 + <b, X'>   (ANY b, ANY diagonal, ANY k_2, m_1),
   in particular the 15_architecture milestone 4 X_h L + 2 L^2 + 2 V^2 + D + linear, which neither Theorem H (degenerate frame)
   nor Prop 5.4 (twist) covers.
General hub law: k_l <= 1/(2|t|), mass 1, support s - 2t supp(f_h). With CSP for intervals only and supp f_h covered by
M unit intervals: I(s) <= int_0^1 min(sqrt2/(2t), M K'(2t)^{-1/2}) dt ~ C(1 + log M). With CSP_gen: bounded, no M.
So for general hub laws the missing estimate is CSP_gen (weak-L^2 of the conditional law), not the interval form.

a != 0 (sketch, to be checked): recentre the hub interval at 0 (moves a linear-in-L term into F). Then
k_l(phi) <= |a|^{-1/2} |phi - phi_c(l)|^{-1/2}, phi_c(l) = s' + t^2/a, level sets = <= 4 intervals, |{k>lam}| <= min(2|t|+|a|,
2/lam, 4/(|a| lam^2)), sup k <= 1/(2 max(0, |t| - |a|/2)). Region |t| >= |a|/2: layer cake with CSP(intervals) gives an
integrable bound (log only near |t| = |a|/2, integrable). Region |t| < |a|/2 (measure |a|, the hub's own critical point inside
its support): CSP is useless (two square-root singularities may coincide); use instead
   contribution <= |a|^{-1/2} E[ |R_a - s|^{-1/2} ; |t| < |a|/2 ],  R_a = F - (L+beta)^2/a + const,
a RANK-TWO form in (L,V) with matrix [[k_2 - 1/a, m_1/2],[m_1/2, lambda]] (det ~ -lambda D_H / a, D_H = |1 - a k_2| as in
Prop 5.4) plus T. Theorem F (r = 2, separable T) gives alpha_2(R_a) <~ |a|^{1/2}|lambda|^{-1/2}; with P(|t|<|a|/2) <= sqrt2 |a|
and the layer cake: contribution <~ |a|^{-1/2} |a|^{3/4} log^{1/2}(1/|a|) -> bounded. So a != 0 also closes for separable T.

## 6. Hybrid, clean version (no disintegration needed) - PROVED for separable T

Lemma H1' (Fourier at frozen L). F(l; X') := lambda (V + gamma(l))^2 + c(l) + T(l; X'), where gamma, c are ANY measurable functions
of l and T(l; X') = sum_i phi_i(X_i; l) + <b(l), X'> is separable for each l. Then for every Psi in L^1(dl) (bounded, continuous):
   |E[ Psi(L) exp(-i tau F(L; X')) ]| <= ||Psi||_1 * min( sqrt2 , 4 sqrt(pi) |tau lambda|^{-1/2} ).
Proof: approximate identity eta_d in l: E[Psi(L) e^{-i tau F(L;X')}] = lim_d int dl0 Psi(l0) E[eta_d(L - l0) e^{-i tau F(l0; X')}]
(dominated convergence, continuity in l0). For FIXED l0 write eta_d(L - l0) = (1/2pi) int eta_d^(xi) e^{i xi (L - l0)} d xi, |eta^| <= 1,
so |E[eta_d(L-l0) e^{-i tau F(l0;X')}]| <= (1/2pi) int d xi |E e^{i xi L - i tau F(l0; X')}|. Fresnel (3.1) on the single V-square
(centre gamma(l0) = a phase): <= (1/2pi)(4 pi |tau lambda|)^{-1/2} int int |prod_i g_i^(xi w_i + u v_i)| d xi du, g_i = f_i e^{-i tau phi_i}
(|g_i| = f_i). Geometric BL with frame rho_i = (w_i, v_i), c_i = |rho_i|^2 <= 1/2, Lemma 1 (int |g^|^p <= 4 pi/sqrt p): <= (4pi)^2.
Total (1/2pi)(4 pi|tau lambda|)^{-1/2} 16 pi^2 = 4 sqrt(pi) |tau lambda|^{-1/2}. Trivial bound: E|Psi(L)| <= sqrt2 ||Psi||_1. []
KEY POINT: kappa L^2, L V, L*<r,X'> terms are functions of l or linear in V / in X' at frozen l, so they never enter the xi-integral;
this is exactly what N12 of 04 says Theorem H cannot do.

Theorem H2 (a = 0; hub density f_h <= 1_J, J an interval of length D; t = sigma L + beta). PROVED.
   p_Q(s) <= 1/2 + I,  I = E[ (2|t|)^{-1} 1{|t|<1} f_h((s - F)/(2t)) ] <= 1.088 E[ H(L) Phi_{u(L)}(F - c_*(L)) ],
   H = (2|t|)^{-1} 1{d0 <= |t| < 1} (d0 -> 0 by monotone convergence), u = 2|t| D, Fejer Phi_u(y) = (sin(y/u)/(y/u))^2 >= 0.919 on
   |y| <= u/2, Phi_u^(tau) = pi u (1 - u|tau|/2)_+. Fubini (legal for d0 > 0) + Lemma H1' with Psi_tau(l) = H(l) Phi_{u(l)}^(tau) e^{...}:
   ||Psi_tau||_1 = (1/sigma) int_{|t|<1} pi D (1 - |t| D |tau|)_+ dt <= (1/sigma) min(2 pi D, pi/|tau|).
   I <= (1.088/(2 pi sigma)) int d tau min(2 pi D, pi/|tau|) min(sqrt2, 4 sqrt(pi)|tau lambda|^{-1/2})
     <= (1/sigma) [ 1.54 + 21.8 D^{1/2} |lambda|^{-1/2} ].
   (Checked twice: int_{|tau|<=1/(2D)} 2D sqrt2 = 2 sqrt2; int_{|tau|>1/(2D)} 4 sqrt(pi)|lambda|^{-1/2}|tau|^{-3/2} = 16 sqrt(2 pi) D^{1/2}|lambda|^{-1/2}.)
   Milestone 4X_hL + 2L^2 + 2V^2 + D(X) + <b,X> (sigma = 2, lambda = 2, X_h uniform on an interval, D = 1): p <= 0.5 + 8.5 = 9.0.
   General f_h: cover supp f_h by M unit intervals; I <= C(1 + log M). The loss is the interval-vs-arbitrary-set gap (CSP vs CSP_gen).

a != 0: same machinery; the kernel is a sum of <= 4 interval indicators on dyadic level sets (layer cake), good set |t| >= |a|/2
fine; bad set |t| < |a|/2 (hub critical point inside J) handled by alpha_2 of the RANK-TWO form R_a = F - (L+beta)^2/a (Theorem F,
r = 2, separable T): contribution <= |a|^{-1/2} E[|R_a - s|^{-1/2}; bad] <~ |a|^{1/4} log^{1/2}(1/|a|). Needs D_H = |1 - a k_2| >= c
(det of R_a's (L,V) matrix ~ -lambda D_H/a), exactly Prop 5.4's condition. PROVED modulo writing constants.

## 7. Dense E: reduction to a NON-ALIGNED twist lemma (TL_perp)
Write X'^T E X' with L frozen: decompose relative to w: E = k ww^T + (w r^T + r w^T) + E_w, r ⊥ w, E_w w = 0. At L = l:
k l^2 (constant) + 2 l <r, X'> (linear) + X'^T E_w X'. Then R := lambda v v^T + E_w annihilates w; let v~ be its top eigenvector
(v~ ⊥ w, |v~ - v| <~ eps/lambda, eigenvalue lambda~ >= lambda - eps) and R = lambda~ v~ v~^T + R_perp with R_perp w = R_perp v~ = 0.
Lemma H1' goes through verbatim with frame (w, v~) PROVIDED
 (TL_perp)  int int |E exp(i xi <w,X'> + i u <v~,X'> + i tau X'^T R_perp X' + i sum_i phi_i(X_i))| d xi du <= C_perp
for all tau, all separable phases, all R_perp that annihilate span(w, v~) with ||R_perp|| <= 2 eps.
Then Theorem H2 holds for the full canonical family (a = 0, dense E, any b, interval hub) with 4 sqrt(pi) replaced by C_perp/(4 sqrt(pi)).
TL_perp excludes by hypothesis every counterexample in 04 (N2, N7 need an aligned twist R p != 0, p in the frame span).
For Gaussian X it is trivial (the twist is independent of the frame). It is the precise form of 04's "small non-aligned coupling".
Caveat: the diagonal of E should be kept separable (BL handles it) - decompose only E_off; then R_perp = P~^perp E_off P~^perp is
not diagonal, and TL_perp must allow separable phases + R_perp simultaneously (as stated).

## 8. Numerics (NUMERICAL; fibre_density.py = exact partition-of-unity fibre estimator, validated in t0_validate.py
against the hub-conditional estimator: 0.559/1.169/1.411/1.006 vs 0.552/1.183/1.420/1.010)
 t1_milestone_output.txt: milestone 4X_hL + 2L^2 + 2V^2 + D + <b,X'> (48 leaves): interval hub, uniform leaves: 1.64 (D=0),
   1.46 (|d_i| ~ 0.1), 0.85 (orthogonal linear term |b_perp| = 1). Spread hub laws (M = 4/16/64 pieces) and bumpy laws: <= 0.07
   (the density spreads out; spread laws only lower it). Proven bound (Theorem H2, sigma = 2, lambda = 2): 8.97.
 t2_profile_dense_output.txt: (a) g(x) = p_{Q_x}(0) for the milestone is UNIMODAL, peak ~1.5 at x = 0, ~1/|x| decay
   (0.34 at |x| = 1, 0.17 at 2, 0.11 at 3); so the bathtub-worst hub law is the interval around 0 and the log M loss of the
   interval-CSP method is a loss of the method. (b) dense family 2X_h(L+0.2) + V^2 + eps W + b_perp U (||W|| = 1, zero diag):
   uniform laws 3.45 / 2.19 / 1.43 for eps = 0 / 0.2 / 0.5 (b_perp = 0), 1.15 / 1.12 / 0.98 (b_perp = 1); comb laws (3 teeth)
   0.85 / 0.39 / 0.21. Nothing grows; the dense twist and orthogonal linear terms lower the density, as the hybrid predicts
   (they only enter through the Fourier factor, which they can only shrink when not aligned).

## 9. Final audit of the constants (wrap-up)
- Fejer: min of (sin x/x)^2 on |x| <= 1/2 is 0.91940 (1/min = 1.08767); the FT of (sin x/x)^2 at omega = 0.7 is 2.042035 (numeric)
  against pi(1 - omega/2) = 2.042035. Lemma 2 constant (1/2pi)(4pi)^{-1/2} 16 pi^2 = 7.08982 = 4 sqrt(pi). CHECKED.
- Theorem A integral (sigma = 1, D = 1, |lambda| = 1): the exact integral of min(2D, 1/|tau|) min(sqrt2, 4 sqrt(pi)|tau|^{-1/2}) is 19.56
  (log-spaced trapezoid; inner part 2.828 = 2 sqrt2 exactly, outer part 16.74), so the true bound is 0.544 * 19.56 = 10.64.
  The stated 1.54 + 21.8 = 23.34 is a VALID but loose upper bound (the analytic outer estimate 16 sqrt(2 pi) = 40.1 drops the min
  with sqrt2). A first scipy quad run returned a wrong 2.82 (divergence warning) and was discarded.
- REPORT.md could not be written (the environment refuses report files for this worker); the full report is in the final message.
- STATUS at stop: Theorem A (a = 0, hub density supported in an interval, T separable) PROVED with constants; Theorem B (dense E ->
  TL_perp) PROVED as a reduction; Proposition C (general hub law, C(1 + log M)) PROVED; Proposition D (a != 0) PARTIAL.
  Open: TL_perp (non-aligned twist lemma) for dense E; CSP_gen (weak-L^2 conditional square-root profile) for general hub laws.

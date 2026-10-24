# NOTES - decoupling without loss at hubs

## 1. Where the square-root loss of Theorem D actually sits (first observations)

Setting: Q = X^T A X + b^T X + c, phi(t) = E e^{itQ}. Split coordinates I, J. Put
Phi_J(t; x_I) = E_J exp(i t Q(x_I, X_J)). Weyl differencing (Cauchy-Schwarz in x_I):

  |phi(t)|^2 = |E_I Phi_J(t; X_I)|^2 <= E_I |Phi_J(t; X_I)|^2 = phi_D(t),          (1.1)

where D = Q(X_I, X_J) - Q(X_I, X'_J) with X'_J an independent copy. This is an IDENTITY for the
right side: E_I|Phi_J|^2 is the characteristic function of the quadratic form D in the doubled
variables (X_I, X_J, X'_J). Explicitly (W = X_J - X'_J)

  D = 2 X_I^T A_IJ W + q_J(X_J) - q_J(X'_J),    q_J(x) = x^T A_JJ x + b_J^T x,

so the I-I block of D is zero and b_I drops out. Conditioning on (X_J, X'_J):

  phi_D(t) = E_{J,J'} [ exp(i t (q_J(X_J) - q_J(X'_J))) prod_{i in I} psi_i(2 t (A_IJ W)_i) ].   (1.2)

Theorem D bounds (1.2) by E_{J,J'} prod |psi_i(...)|, i.e. it THROWS AWAY THE J-SIDE PHASE
exp(i t (q_J(X_J) - q_J(X'_J))). 

Claim (heuristic, checked on examples below): for a hub the loss is in this second step, not in
the Cauchy-Schwarz step (1.1).

Example 1 (pure hub, h in J). Q = 2 X_h L, L = L_I + L_J (L_S = <w_S, X_S>). Then
q_J(X_J) = 2 X_h L_J and (1.2) reads
  phi_D(t) = E_{X_h, X'_h} [ phi_{L_I}(2t(X_h - X'_h)) phi_{L_J}(2t X_h) conj(phi_{L_J}(2t X'_h)) ].
The factors phi_{L_J}(2tX_h), phi_{L_J}(2tX'_h) localise BOTH hub copies to |X_h|, |X'_h| <~ 1/|t|,
so phi_D = O(t^{-2}) (up to the log of a non-integrable psi), which is |phi|^2 ~ t^{-2}: no loss.
Dropping the phase leaves E|phi_{L_I}(2t(X_h - X'_h))| ~ 1/|t|: the loss.

Example 2 (hub + rank one, h in J). Q = 2 X_h L + lam V^2. Then
  D = [2 X_h L + lam V^2] - [2 X'_h L' + lam V'^2],  L' = L_I + L'_J, V' = V_I + V'_J,
a form with two hubs (X_h, X'_h) and a rank-two part lam(V^2 - V'^2): "6 units" of decay, t^{-3},
matching |phi|^2 ~ t^{-3}. Theorem D sees only the rank-two cross block (X_h - X'_h) w_I,
lam (V_J - V'_J) v_I: t^{-2}, hence |phi| <~ 1/|t|, not integrable.

So "decoupling without loss" = bound phi_D itself (the characteristic function of the doubled
form D), keeping the J-J block of D. This is the Fourier-side counterpart of Kwan-Sauermann's
"do not forget Z^(1)": in their discrete scheme P(Q = z) <= P(xi_J in Z^(1))^{1/2}, with
Z^(1) = Z_{xi_I} cap Z_{xi'_I} defined by one linear and one quadratic equation; the classical
loss comes from replacing Z^(1) by the hyperplane W^(1) (forgetting the quadratic equation).
Density form of the same step: p_Q(z) = E_I p_{Q|X_I}(z) <= (E_I p_{Q|X_I}(z)^2)^{1/2}, and
E_I p_{Q|X_I}(z)^2 = density at (z,z) of the pair (Q(X_I,X_J), Q(X_I,X'_J)).

## 2. Naive iteration of "decouple then forget" does not help hubs

Two rounds of Weyl differencing (|phi|^4 <= |phi_D|^2 <= phi_{D_2}) followed by dropping the last
J-side phase: whichever side the hub copies are placed on in round two, the surviving cross block
sees the hubs with rank 2 (two hub DIFFERENCES), giving phi_{D_2} <~ t^{-2}, |phi| <~ t^{-1/2} from
the hub: no gain over Theorem D. Reason: a hub is one coordinate times one linear form; whichever
side the hub coordinate sits on, the linear form has coordinates on both sides, and the forgotten
block always contains the coupling of the hub to its own side. So the Kwan-Sauermann "iterate
log log n times" mechanism (which reduces the relative weight of the forgotten quadratic
equation) does not by itself remove a hub loss: the hub loss is proportional to the number of
hubs, not a bounded additive loss. What removes it is keeping the hub coupling on BOTH sides,
i.e. integrating the hub coordinates exactly (Theorem H style) inside phi_D.

## 3. Numbers to keep in mind

Open regime for star + rank one + eps W: Theorem D already gives a bounded density once
||eps W_IJ||_F^2 >~ 1 for a partition (Z ~ lam^2 eps^2 n); so the open case has
||eps W||_F = eps sqrt(n) << 1: the twist is SMALL IN HILBERT-SCHMIDT NORM (and in operator norm).

## 4. The Kwan-Sauermann mechanism, read from the source (2312.13826, Sec. 3, Thm 3.4)

Setting: X = sum xi_i a_i in R^r (r fixed, t disjoint bases among the a_i), Z a quadric on a
(d+1)-dimensional affine subspace W. Claim P(X in Z) <= 2^{dr+1} t^{-(r-d)/2} (same rate as a
d-dimensional affine subspace). Proof by induction on d:
 - reducible Z (two d-planes): Halasz. Cylinder Z (Z + Rv = Z): project along v, lower d.
 - otherwise (Lemma 3.2) for x != y the intersection (Z - x) cap (Z - y) is a quadric on a
   d-DIMENSIONAL affine subspace W_{x,y}. Split X = X_I + X_J (t/2 bases each). Decoupling:
     P(X in Z)^2 <= P(X_J in (Z - X_I) cap (Z - X'_I), X_I != X'_I) + P(X in Z) P(X'_I = X_I).
 - MAIN TERM: nonempty only if X_I - X'_I in W~ (the linear space parallel to W): probability
   (t/2)^{-(r-d-1)/2} by Halasz; conditionally, X_J lies in a quadric on a d-dim subspace:
   (t/2)^{-(r-d+1)/2} by induction. Product t^{-(r-d)} = (t^{-(r-d)/2})^2: NO LOSS.
 - error term: P(X'_I = X_I) <= t^{-r/2}, then a^2 <= ab + c gives a <= b + sqrt c.

What makes it lossless: the quadratic condition is NEVER dropped. Each decoupling converts it
into (one linear condition on the DIFFERENCE X_I - X'_I, counted with full Halasz weight)
+ (a quadric of one dimension less on the J side, handled by the SAME theorem one level down).
The induction runs on the dimension of the quadric until it is a pair of points (d = 0), where
nothing quadratic is left. The general (unbounded rank) case needs: (T,U)-perturbations
(A and A + L M + M^T R define the same quadric on {M x = w}), i.e. the quadratic part is only
defined MODULO the linear constraints, and a robust-rank inheritance lemma (witness counting).

Translation to our continuous problem:
 - "quadric on a d-dim affine subspace" <-> the density of Q restricted to an affine slice,
   i.e. the joint density of (Q, M X) at (z, w), M a k x n matrix: p_{(Q, MX)}(z, w).
 - decoupling identity: E_I [p_{(Q, MX) | X_I}(z, w)^2] = density of the quadruple
   (Q(X_I,X_J), M X, Q(X_I,X'_J), M X') at (z, w, z, w) = density of
   (Q, MX, D, M(X_J - X'_J)) with D = Q(X_I,X_J) - Q(X_I,X'_J) LINEAR in X_I given J, J'.
 - the (T,U)-perturbation fact = "twist relative to the integrated directions": only the part of
   the quadratic form that is NOT of the form L M + M^T R matters on the slice {MX = w}.
So the faithful continuous analogue is an induction over joint densities of (quadratic, linear
map) pairs, where every decoupling step adds the new linear map x_I -> 2 A_IJ (x_J - x'_J) to
the constraint set instead of dropping the quadratic equation.

## 5. K-S recursion (Sec. 4, Thm 4.3) and what "loss-free" means there

f(k,s) = sup P(Q = 0, M xi = w) over M robustly of rank k and Q nondegenerate modulo (M,M)-
perturbations. Recursion: f(k,s) <= max{ s_*^{-(k+1)/2}, s_*^{-(k+2)/2} + s_*^{-k/4} f(k+1,s_*)^{1/2} }.
i.e. f(k)^2 <~ s^{-k/2} f(k+1): the factor s^{-k/2} is P(M_I (xi_I - xi'_I) = 0) (the old
constraints must hold for the DIFFERENCE), f(k+1) is the new quadric-on-codim-(k+1) problem.
Iterating m times and then FORGETTING the quadric (f(m) <= s^{-m/2}) loses s^{1/2} at level m,
which propagates to f(0) as s^{1/2^{m+1}}. So the loss is not avoided: it is pushed to the end
and diluted by repeated squaring; m ~ log log s makes it O(1). The "+2" in s^{-(k+2)/2}
(robust rank inheritance) is what makes the degenerate branch affordable.

Continuous analogue of the dilution: forgetting a quadratic constraint in a DENSITY costs one
full unit (P(|Y-z|<=e, |rest|<=e) <= P(|rest|<=e) loses a factor 1/e). After m Weyl steps,
|phi|^{2^m} <= phi_{D_m} and a final forgetting costing one unit (|t|) costs |t|^{2^{-m}} in
|phi|: O(1) for m ~ log log |t|. BUT this needs every intermediate step to be lossless, and at a
hub it is not: every Weyl step duplicates the hub, the duplicated copies coincide on the shared
block, and a final forgetting loses HALF OF ALL 2^m hub copies (not one unit). So the K-S
dilution does not apply to hubs; the hub loss is multiplicative in the copies. (Sec. 2 above.)

## 6. NEW: the hub-integrated decoupling formula (exact)

Hub h with a_hh = 0, row w; J = {h} u J0 duplicated, I shared. sigma = X_h - X'_h,
mu = (X_h + X'_h)/2, W0 = X_J0 - X'_J0, Delta = <w_J0, W0>, Sigma = <w_J0, X_J0 + X'_J0>,
M = A_{I J0}. Then (checked term by term)
  D = 2 sigma L_I + 2 mu Delta + sigma Sigma + b_h sigma + 2 X_I^T M W0 + q0(X_J0) - q0(X'_J0),
mu enters ONLY through 2 mu Delta, and with F_sigma(mu) = f_h(mu + sigma/2) f_h(mu - sigma/2),
F^_sigma(s) = int F_sigma(mu) e^{i s mu} d mu:

  phi_D(t) = E_{J0,J0'} [ e^{it(q0(X_J0)-q0(X'_J0))} int dsigma e^{it sigma(Sigma + b_h)}
                          Psi_I(2t(sigma w_I + M W0)) F^_sigma(2t Delta) ],

  |phi_Q(t)|^2 <= phi_D(t) <= int dsigma E_{W0} [ |Psi_I(2t(sigma w_I + M W0))| |F^_sigma(2t<w_J0,W0>)| ].  (6.1)

(6.1) contains NO J0-J0 block and NO I-I block of A: the twist inside J0 and inside I is gone
entirely; the twist cross block E_{I J0} only enters the argument of Psi_I (like Theorem D).
The hub is seen TWICE: the difference sigma through the density of sigma (f_h * f~_h <= 1, the
Theorem-H mechanism, robust to rough hub laws) and the sum through F^_sigma(2t Delta).
Facts: |F^_sigma| <= g_h(sigma) := (f_h * f~_h)(sigma) <= 1; ||F^_sigma||_2^2 = 2 pi ||F_sigma||_2^2
<= 2 pi g_h(sigma); int g_h = 1. F^_sigma is NOT in L^1 in general (uniform law: interval
indicator, |F^| ~ 1/|s|), so the sum copy can be counted with L^2 weight only: t^{-1/2}, not t^{-1}.
Expected count for hub + one spread direction lam V^2: t^{-1} (difference) * t^{-1} (lam cross
column) * t^{-1/2} (sum, L^2) = t^{-5/2} for |phi|^2, i.e. |phi| <~ t^{-5/4}: INTEGRABLE, against
Theorem D's t^{-1}. To do: a Brascamp-Lieb evaluation of (6.1) with the 2D factor F^_sigma.

## 7. Evaluating (6.1): what works, what does not

(a) Full Brascamp-Lieb with the 2D factor b(sigma,x) = |F^_sigma(2t x)| in L^2(R^2) (rho = 1/2)
    CANNOT give t^{-5/2}: BCCT dimension count on V0 = common kernel of the psi-rows
    ({sigma = 0, Delta_V = 0} when the twist vanishes, dim m-1) needs
    m - 1 <= sum_j (1-beta_j) + rho = m - 3/2 when sum alpha_i = 2: FALSE. So the L^2(R^2) norm
    double counts sigma (already covered by the w_I-direction of Psi_I). The right norm for b is
    the MIXED norm sup_sigma ||b(sigma, .)||_{L^2_x} <= (pi/|t|)^{1/2}; the dimension count with the
    mixed norm is exactly balanced on V0 (m-1 <= m-1). Mixed-norm BL is not standard.
    (Gaussian computation done: sup_K det(K)^{rho/2} det(G0 + P^T K P)^{-1/2} <=
    det G0^{-1/2} det(P G0^{-1} P^T)^{-rho/2}, via det(I+KH) = 1 + tr KH + det K det H >= (1+y)^2.)

(b) SEQUENTIAL proof works when the psi-factors do not depend on the hub-sum variable:
    split J0 = J_V u J_L with A_{I J_L} = 0. Then for fixed (sigma, W_V),
      E_{W_L} |F^_sigma(2t(x_V + <w_JL, W_L>))| <= ||p_{x_L}||_2 (2|t|)^{-1/2} ||F^_sigma||_2
                                                <= ||p_{x_L}||_2 (pi/|t|)^{1/2},
    and what is left is int dsigma E_{W_V} |Psi_I(2t(sigma w_I + A_{I J_V} W_V))|, a Theorem-D
    type BL integral over (sigma, W_V) in which sigma carries LEBESGUE measure (so volume sampling
    must always contain the hub column): <= (4 pi)^2 (2|t|)^{-2} e^{1/2} Z_h^{-1/2},
    Z_h = sum of squared 2x2 minors of [w_I | A_{I J_V}] containing the w column
        = |w_I|^2 ||P_{w_I perp} A_{I J_V}||_F^2, marginals = leverages of the 2-frame (need <= 1/2).
    => |phi(t)| <= K |t|^{-5/4}, K^2 = 4 pi^{5/2} e^{1/2} ||p_{x_L}||_2 Z_h^{-1/2}; INTEGRABLE.
    This is THEOREM D_H (to be written with full proof). Everything else (A_II, all J-J blocks,
    A_{I J_V}) is arbitrary: a dense twist is allowed everywhere except in the I-J_L block.

(c) Coupled case (twist in the I - J_L block). The rank-one part of the coupling along the hub
    partner, 2 theta L_I L_J0, shifts sigma -> sigma + theta Delta_L; after substitution the sum
    factor is the hub law's AMBIGUITY FUNCTION A_f(sigma,s) = int f(mu+sigma/2) f(mu-sigma/2) e^{is mu}
    along a TILTED line (sigma' - kappa s, s), kappa = theta/(2t). Metaplectic covariance:
    A_f(sigma - kappa s, s) = A_{U f}(sigma, s), U = free Schrodinger/Fresnel propagator at time kappa
    (checked: chirp e^{-i kappa xi^2/2} on f^ multiplies f^(xi+s/2) conj f^(xi-s/2) by e^{-i kappa xi s}).
    So int |A_f(tilted)|^2 ds <= 2 pi ||U_kappa f||_4^4, NOT uniformly bounded for densities <= 1
    (zone-plate sets focus: ||U_kappa f||_inf ~ kappa^{-1/2}). Uniform law: harmless (<= 8).
    But 1D Strichartz L^8_kappa L^4_x controls it on average over t: with kappa = theta/2t,
    int t^{-5/4} ||U_{theta/2t} f||_4 dt < infinity by Holder (8, 8/7). PARTIAL (sketch).
    The rest of a dense coupling correlates with Delta_L through non-Gaussian dependence of
    orthogonal linear forms of a product vector: NOT handled. This is where the method stops.

## 8. LOSS-FREE decoupling at a hub: Young + Plancherel (keeps the J-side phase)   [PROVED, see REPORT Thm 5.1]

Physical integration of BOTH hub copies (f_h <= 1, y = 2t x, y' = 2t x') inside phi_D = E_I|Phi_J|^2:
  |phi_Q|^2 <= phi_D <= (2|t|)^{-2} int int |F(y,y')| dy dy',
  F(y,y') = E_{X_I}[ e^{i(y-y')L_I} A(y w_J0 + tau(X_I)) conj A(y' w_J0 + tau(X_I)) ],
  A(eta) = E_{J0} exp(i<eta, X_J0> + i t X_J0^T A_{J0J0} X_J0)  (twisted CF of the duplicated block),
  tau(X_I) = 2t A_{J0 I} X_I + t b_J0.   Hub diagonal and linear terms disappear in |.|.
If A_{I J0} = sum_{k<=r} lam_k a_k b_k^T (low-rank CROSS block), with Z = (<a_k, X_I>):
  F(y,y') = int dz p^_z(y - y') B(y, 2t Lam z) conj B(y', 2t Lam z),  p^_z = FT in l of the joint
  density of (L_I, Z), B(y, zeta) = A(y w_J0 + sum zeta_k b_k + t b_J0).
Young (int int k(y-y') g(y) g(y') <= ||k||_1 ||g||_2^2):
  int int |F| <= sup_z ||p^_z||_1 * (2|t|)^{-r} |det Lam|^{-1} ||B||_{L^2(R^{1+r})}^2.
 - shared block I: twist KILLED by decoupling, so p^_z is a plain projection object:
   ||p^_z||_1 <= (2pi)^{-r} int |Psi_I(Q_I v)| dv <= (2pi)^{-r} (4pi)^{1+r} det G_I^{-1/2} (BL, leverages <= 1/2)
 - duplicated block J0: ARBITRARY twist, only L^2 needed: Plancherel ||B||_2^2 <= (2pi)^{1+r} 2^{(1+r)/2} det G_J0^{-1/2}.
  => |phi_Q(t)| <= (2|t|)^{-1-r/2} [2pi (4pi)^{1+r} 2^{(1+r)/2}]^{1/2} (|det Lam| sqrt(det G_I det G_J0))^{-1/2}.
r = 0: t^{-1} (hub, full weight); r = 1: t^{-3/2} (hub + one cross direction, full weight = truth).
A_II and A_J0J0 arbitrary (dense twists allowed), hub diagonal arbitrary, linear terms arbitrary.
Same scope as the twist record's hub block lemma (N8) by an independent route (N8 needs no leverage
condition; this needs leverages <= 1/2 on the shared block, but the shared block may carry ANY twist
because decoupling removes it). Mechanism = K-S "keep the quadratic equation": the duplicated side is
kept as a phase inside A and paid for in L^2, which is twist-blind; the shared side supplies L^1.
Open: coupling A_{I J0} = structured + small dense E. Aligned part (theta L_I L_J0) shifts y by
2t theta L_I inside B: fatal type (bumpy laws). Non-aligned part: needs
  Omega = int d tau sup_z || FT_l p(l, z, tau) ||_1 < inf   for (L_I, V_I, tau = 2tE X_I),
a slice-Fourier bound for product measures: the mixed-norm problem again.

## 9. Checks done before writing REPORT
- Re-derived every factor of Thm 5.1: Fubini in phi_D; E[e^{isL_I} G(Z)] = int G(z) p^_z(s) dz;
  p^_z(s) = (2pi)^{-r} int phi_{(L_I,Z)}(s,u) e^{-i<u,z>} du; Young <g, k*g> <= ||k||_1 ||g||_2^2;
  change of variables zeta = 2t Lam z; Plancherel for the twisted CF (|m| <= p); Ball/LPP 2^{k/2};
  geometric BL with c_i <= 1/2 and Lemma 1 giving (4pi)^{1+r}. Density constant for r = 1:
  ||p_Q|| <= 6 (|lam| sqrt(det G_I det G_J0))^{-1/3}  (int min(1, C|t|^{-3/2}) = 6 C^{2/3}).
- NUMERICAL (check_thm51.py, output check_thm51_output.txt): hub + rank-one cross block + dense
  twists of operator norm 0, 1, 3 INSIDE each block, uniform laws, m = 8 + 8: |phi(t)| below the
  bound at t = 2..64; from t ~ 8 on the MC values are at the floor (5e-4), so the test only has room
  to fail for t <= 8, where it passes with a factor >= 3. Weak check, consistent.

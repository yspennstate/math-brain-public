# NOTES - rank three by real-variable geometry (folder 03_rank3_geometric)

Started 2026-09-23 02:10 (local). Read BRIEF, RESULTS, GEOM report, COUNTEREXAMPLE_SEARCH.

## N1. Setting and normal form

A = R Lambda R^T, R n x 3 with orthonormal columns, rows r^(i) in R^3, leverages l_i = |r^(i)|^2, sum l_i = 3.
Y = R^T X in R^3. Every rank-3 quadratic polynomial is
   Q = (Y - y0)^T Lambda (Y - y0) + beta Z + c,   Z = <u, X>, u unit, u orthogonal to the columns of R.
Call beta Z the OUTSIDE linear term (the in-range part of b is absorbed into y0).

Tools available and checked:
- Theorem F (RESULTS s.4) with B = 0, I = [n]: G_I = R^T R = I_3, so if max_i l_i <= 1/2 then
  ||p_Q|| <= 12 (|l1 l2 l3|)^{-1/3} <= 12, ANY signature, ANY linear term b (the linear phases are
  translations inside Brascamp-Lieb). I re-derived the Fresnel constant (4 pi |t lambda|)^{-1/2}, the BL
  substitution u = G^{-1/2} w, Lemma 1 exponents and int min(1,K|t|^{-3/2}) = 6 K^{2/3}. OK.
- Lemma 1.3 (ellipse coarea, ANY density rho <= K on R^2): p_q <= pi K / sqrt(det B).
- 2D orthonormal projections of the product measure have density <= 2 (Ball / LPP).

## N2. PROVED: definite rank three with in-range linear part, density <= 12

Claim. Lambda >= I (or <= -I), beta = 0. Then ||p_Q||_inf <= 12 for every n, y0, c and every product law.
Equivalently: spherical means of rho_Y (Y an orthonormal 3D projection) satisfy M_{y0}(r) <= 6/(pi r).

Proof. If max l_i <= 1/2: Theorem F. Otherwise pick h with l_h > 1/2 and write r = r^(h),
Y = r X_h + Y', Y' = R_{-h}^T X_{-h}, D = Y' - y0. Then
   Q = a (X_h - m)^2 + D^T S D,  a = r^T Lambda r >= l_h > 1/2,  S = Lambda - Lambda r r^T Lambda / a.
S r = 0 and S is symmetric, so S = Pi S Pi (Pi = projection onto r^perp). Hence D^T S D depends only on
W = V^T Y' where V (3x2) has orthonormal columns spanning r^perp:  D^T S D = (W - w0)^T S' (W - w0),
S' = V^T S V. W = V^T R_{-h}^T X_{-h} has Gram V^T (I - r r^T) V = I_2: an ORTHONORMAL 2D projection of
X_{-h}, density <= 2. The (n-1)x(n-1) Schur complement A/a_hh equals M^T S' M with M M^T = I_2, so the
eigenvalues of S' are its nonzero eigenvalues, >= 1 by Lemma 1.5 (and S' >= 0 by Cauchy-Schwarz).
Lemma 1.3: p_{q(W)} <= 2 pi / sqrt(det S') <= 2 pi. Conditional density of a(X_h - m)^2 at s - R is
<= a^{-1/2} |s - R|^{-1/2} (Lemma 1.2(i)), so p_Q(s) <= a^{-1/2} E|s - R|^{-1/2}
<= a^{-1/2} sup_{p <= 2 pi} int p(x)|s-x|^{-1/2} dx = a^{-1/2} 2 sqrt(2 * 2 pi) = 4 sqrt(pi) a^{-1/2}
<= 4 sqrt(2 pi) = 10.03.  QED.  Status: PROVED (second check below still to do numerically).

Remark. The GEOM report (s.4) left this open because it wanted arbitrary linear terms; with the linear part
in the range the Schur complement has NO linear term outside its range (computed above), so the rank-2 step
is the elementary ellipse bound. The genuinely open rank-3 cases are therefore:
 (T) two-sheet side of signature (2,1), heavy coordinate present;
 (O) outside linear term beta Z != 0, heavy coordinate present (any signature, one-sheet side included:
     Theorem C's ruling argument also needs beta = 0).

## N3. Case split for the two-sheet side (T), heavy h (l_h > 1/2), a = a_hh = r^T Lambda r
- a <= -c (timelike heavy row): Schur complement S' positive definite (signature count), same proof as N2:
  p <= 4 sqrt(pi)/sqrt(c).  PROVED.
- a >= c (spacelike heavy row): S' has signature (1,1); need
     Lemma X: sup_s E|s - q(W)|^{-1/2} <= C for q indefinite 2x2 (|eig| >= 1) of an orthonormal 2D projection W.
- |a| < c (nearly null heavy row): hub-like. Normal form in the frame (rhat, V):
     Y = (sqrt(l) X_h + sqrt(1-l) Z0) rhat + V W, (Z0, W) orthonormal 3D projection of X_{-h}.
  Pure case l = 1: Q = 2 X_h V + W^2 type = GEOM Prop 5.4 (bounded). l < 1 adds the small twist 2 sqrt(1-l) Z0 V.

Useful identity (conditioning on the heavy coordinate, in the r-hat frame): with tau = <rhat,y0> - sqrt(l) x,
   p_Q(s) = l^{-1/2} int f_h(x(tau)) g(tau) d tau,  g(tau) = density at s of the form in (sqrt(1-l) Z0 - tau, W).
Using f_h <= 1 only gives l^{-1/2} int g = the pivot bound a^{-1/2} E|s - q'(W)|^{-1/2}; the unit mass of f_h
(bathtub: only a tau-set of measure sqrt(l) counts) is what must rescue the hub case.

## N4. Lemma X (rank-2 form of a 2D projection, level 2) - PROVED  [written 02:41]

Lemma X. W = M X, M 2 x n with orthonormal rows, q(w) = (w - w0)^T S (w - w0) + kappa, S symmetric with
|det S| >= 1 (any signature). Then for 0 < u <= 1:
   sup_s P(|q(W) - s| <= u) <= C u (1 + log(1/u)),   hence sup_s E|s - q(W)|^{-1/2} <= C'.
Proof. Rows w^(i) of M^T, sum |w^(i)|^2 = 2.
(a) Light: all |w^(i)|^2 <= 1/2. Rank-2 Fresnel + geometric BL (as Theorem F):
    |phi(t)| <= (4 pi |t|)^{-1} |det S|^{-1/2} (4 pi)^2 = 4 pi/(|t| sqrt|det S|), ANY linear terms.
    Esseen (proved: F(x) = (sin(x/2)/(x/2))^2 >= 0.9194 on |x|<=1, F^ = 2 pi (1-|t|)_+):
    P(|Z - s| <= h) <= 1.0877 h int_{|t|<=1/h} |phi_Z(t)| dt. With |phi| <= min(1, 4pi/|t|):
    P <= 27.4 h (1 + log_+(1/(4 pi h))).
(b) Heavy: some j with |w^(j)|^2 >= 1/2. Frame (what, e'), what = w^(j)/|w^(j)|: T = <what,W> =
    |w^(j)| X_j + (function of X_{-j}), Z2 = <e',W> (function of X_{-j} only, unit 1D projection of X_{-j},
    density <= sqrt 2). Given X_{-j}, q is a 1D quadratic g(X_j), leading coeff a = S_tt |w|^2, and
    DISCRIMINANT IDENTITY:  a (s - kappa_crit) = |w|^2 [ |det S| (Z2 - z0)^2 + S_tt (s - kappa) ]  =: D(Z2)
    (complete the square in T; the critical value is (det S/S_tt)(Z2-z0)^2 + kappa). It depends on Z2 ONLY.
    Lemma 1.2(ii): P(|g(X_j) - s| <= u | X_{-j}) <= 4u/sqrt(|a| max(|s - kappa_crit|, u)) <= 4u/sqrt|D(Z2)|
    (also correct in the limit a = 0: slope 2 S_tz |w| (Z2 - z0), |S_tz| = sqrt|det S|).
    So P(|q - s| <= u) <= E min(1, 4u/sqrt|D(Z2)|), D(z) = A((z - z0)^2 + B'), A = |w|^2 |det S| >= 1/2.
    Bathtub for the density of Z2 (<= sqrt 2, mass 1): split E into {|z^2 + B'| >= z^2/2} (weight
    <= sqrt2 c/|z|, gives c(C + log 1/c)) and the part near +-sqrt(-B') (weight <= c|B'|^{-1/4}|z -+ sqrt|B'||^{-1/2},
    gives <= 4c). c = 4u A^{-1/2}.  Uniform in B', a, S_tt.  QED.
Remark: (b) uses in-range linear terms only (absorbed in w0, kappa). An outside linear term breaks the
identity (D then depends on a 3D projection). (a) allows all linear terms.

## N5. Consequences for rank three, two-sheet side (T)  - PROVED except the nearly-null regime
(2,1) signature, Q = (Y-y0)^T Lambda (Y-y0), s on the two-sheet side.
- max l <= 1/2: Theorem F, <= 12.
- heavy h, a_hh <= -c: pivot, Schur complement definite, <= 4 sqrt(pi)/sqrt(c).
- heavy h, a_hh >= c: pivot, Schur complement q'(W) indefinite 2x2 of the orthonormal 2D projection W
  (no outside linear term: N2 computation), p_Q(s) <= a^{-1/2} E|s - q'(W)|^{-1/2} <= C/sqrt(c) by Lemma X.
- REMAINING: every heavy row nearly null (|a_hh| < c). Pure case l_h = 1 is GEOM Prop 5.4 (any a_hh).
  So open: l_h in (1/2, 1), |a_hh| small.

## N6. The nearly-null regime: normal form and where it stands
Frame (rhat, e_V, e_U), b = Lambda-tilde_{perp,1} = |b| e_V (|b| = |Lambda rhat| >= 1 when a_hh = 0).
After a unimodular triangular change (keeps density bounds): Q = 2 T V + U^2 (normalised), with
   T = sqrt(l) X_h + eps Z0, eps = sqrt(1-l), (Z0, V, U) orthonormal-ish 3D projection of X_{-h}.
Facts: T | (V,U) has density <= 1/sqrt(l) (mixture of translates of f_h). Region where |V| >= kappa |Y|
(the T-derivative is a fixed fraction of the gradient) contributes <= (sqrt2/(2 kappa)) E[1/|W|] <= C/kappa:
PROVED. The rest of the level set is a thin cone around the heavy null direction (T-axis), where the level
set is nearly the plane {V = 0}, which CONTAINS the heavy direction. There the bound needs the joint law of
(Z0, V, U) near V = 0: the danger is 2 eps Z0 V + U^2 ~ s on {|V| ~ 2^-k} with probability ~2^-k/k.
Heavy coordinates of V (2x2 pivot {h,j}), of U (1x1 pivot, then Lemma X), of Z0 (condition on it, reduces
eps) are removable. Left: LIGHT (Z0, V, U). Fourier route (Theorem H + Fresnel on U^2 + Theorem F for
|t| > eps^-2) reduces it to the twist estimate
   J(tau) = int int |E exp(i(yV + uU + tau Z0 V))| dy du <= C (1 + |tau|),  tau = 2 t eps,
and ANY growth up to linear in tau is affordable (int_1^{eps^-2} eps t^{-1/2} dt <= 2). Gaussian case: J(tau)
is constant in tau (no inflation, the twist involves the NEW direction Z0, not an integrated one).

## N7. Lemma X' : outside linear terms allowed  (PROVED, written 02:55)

Lemma A1 (alpha_1 of a square plus an arbitrary linear form). Z2 = unit 1D projection of X, Xi = ANY linear
form in X, A >= 1/2 (say). Then alpha_1(A (Z2 - z)^2 + lambda Xi) <= 22 uniformly in lambda, z.
 - Z2 light (all coefficients^2 <= 1/2): Fresnel on the square, the Xi-frequency t*lambda*xi_i is a SHIFT in each
   factor; 1D BL (Hoelder, sum c_i = 1, c_i <= 1/2) + Lemma 1:  |phi(t)| <= (4 pi |t| A)^{-1/2} 4 pi.
   Esseen (1.0877 h int_{|t|<1/h}|phi|): P(|. - s| <= v) <= 15.4 sqrt(v/A).
 - Z2 heavy (a coordinate k with z_k^2 > 1/2): given X_{-k} it is a 1D quadratic in X_k with leading coefficient
   A z_k^2 >= A/2; Lemma 1.2(ii): P <= 2 sqrt(2v/(A/2)) = 4 sqrt(v/A).
Lemma X' (level 2 for a rank-2 form of a 2D projection plus ANY linear term). W orthonormal 2D projection,
q(w) = (w-w0)^T S (w-w0) + kappa with |det S| >= 1, any signature, beta' Z'' any linear form. Then
alpha_2(q(W) + beta' Z'') <= C uniformly in beta', w0, kappa.
 - W light: rank-2 Fresnel, linear term is a shift in BL: |phi| <= 4 pi/|t|; Esseen.
 - W heavy (j, |w^(j)|^2 >= 1/2): given X_{-j} the form is a X_j^2 + 2 M' X_j + C', and
     D' := M'^2 - a (C' - s) = A (Z2 - z0')^2 + lambda Xi + B,   A = |w|^2 |det S|, lambda = S_tt |w| beta',
   Xi = u''_j (c - t0) - |w| Z'''' orthogonal to Z2 (the tau^2 and tau Z2 terms cancel: same identity as N4).
   P(|. - s| <= u | X_{-j}) <= min(1, 4u/sqrt|D'|); so
     P(|q + beta'Z'' - s| <= u) <= int_0^1 P(|D'| < 16 u^2/theta^2) d theta <= 4 u a1 (1 + log_+ 1/(4 u a1)),
   a1 = alpha_1(D') <= 22 by Lemma A1.  QED.

## N8. THEOREM: every DEFINITE rank-3 form, with ARBITRARY linear terms b, has density <= C (C ~ 300 crude).
Proof. max l <= 1/2: Theorem F (any b). Else l_h > 1/2 and a_hh >= l_h > 1/2 (definite). Pivot on h:
Q = a (X_h - m)^2 + R_h with R_h = q'(W) + (linear form in X_{-h}) (N2 computation plus the outside term;
the part of the linear form along W is absorbed in w0 because q' is invertible). p_Q(s) <= a^{-1/2} E|s-R_h|^{-1/2}
and Lemma X' + Lemma 1.6 bound E|s - R_h|^{-1/2}.  QED. (Status PROVED; constants to be recomputed.)
Also: the same pivot works for ANY signature whenever a heavy row has |a_hh| >= c:  p <= C c^{-1/2}.

## N9. Updated open core for rank three
Open only: Lambda indefinite, EVERY row with l_i > 1/2 nearly null (|a_ii| < c), and either the two-sheet side
(s < 0 for signature (2,1)) or an outside linear term. Normal form Q = 2TV + U^2 (+ Lambda11 T^2 + beta Z_out),
T = sqrt(l) X_h + eps Z0. Reductions: heavy coordinate of V -> indefinite 2x2 pivot {h,j} (det ~ -l nu_j^2), the
type-2 centre is a 1D square of a unit 1D projection plus a linear form, alpha_1 <= 22 by Lemma A1 -> (C3);
heavy coordinate of U -> 1x1 pivot (a_kk ~ mu_k^2) -> Lemma X'; heavy coordinate of Z0 -> condition on it.
Light (Z0,V,U) -> Theorem H + twist estimate J(tau) <= C(1+|tau|) (outside linear terms are shifts there).
Numerics (hub_two_sheet_output.txt): Q = 2TV + U^2, n = 41, l from 0.5 to 1: two-sheet sup flat in eps
(uniform laws 3.55 -> 3.19; one-sheet 4.10 -> 3.61); spread laws only lower it.

## N10. Checks done (second, independent ways)
- check_identities.py (sympy): (i) the Lemma X' discriminant identity with the outside term; (ii) the rank-3
  discriminant D = l (L11 s - W^T N W), Z0 cancels; (iii) det N = L11 det(Lambda-tilde). All True.
- check_pivot_outside.py: exact heavy-coordinate estimator vs direct histograms (2e6 samples, bin 0.02) for
  definite and (2,1) forms, heavy row spacelike or timelike, outside term beta in {0,1,5}: agreement to ~1-2%.
  sup_s p decreases in beta (definite l_h=0.9: 1.60, 1.48, 1.00, 0.43, 0.20 for beta = 0, .3, 1, 3, 10).
- twist_J.py: J(tau) for a light random orthonormal (Z0,V,U), m = 60 uniform coordinates: 71.9 (tau=0,1,3),
  71.4 (10), 64.9 (30), 28.7 (100). [SUPERSEDED by N15: the decrease at large tau was a fixed-grid artifact; with a tau-adaptive grid J is flat: 72.1 / 71.9 / 71.5 / 68.9 at tau = 0/3/10/30.]

## N11. The nearly-null core: why marginal information cannot close it (worth keeping)
Danger sum: p_B <= sum_k 2^k P(|V| ~ 2^-k, x* in supp f_h), x* = ((s-U^2)/(2V) - eps Z0)/sqrt(l).
Constraints I can use: rho_{Z0,V,U} <= 2^{3/2}, rho_V <= sqrt2, rho_{Z0,V} <= 2, Z0 unit mass. They allow
P(...) ~ 2^-k at every scale k >= log(1/eps) (a density concentrated in the regions |v|~2^-k, |z|~2^k/eps,
|zv + c/eps| < 2^-k/eps satisfies all of them), so the sum can diverge. Lemma X (bounded density of Z0 V)
does not forbid it either (P(|Z0 V - a| <= eta) ~ eta there). So the core genuinely needs the product
structure beyond densities of projections: Fourier (twist estimate) or a finer real-variable induction.
Also: T | (V,U) having bounded conditional density is NOT enough (T = t*(W) + unif[0,1/K] is a counterexample
to that weaker hypothesis: density E[K/(2|V|)] = infinity). The linear dependence T - sqrt(l) X_h = eps Z0 must
enter.

## N12. Two-sheet analogue of the ruled identity (answer to the assignment's question)
Hub normal form q = 2tv + u^2. For EVERY beta in R and every s:
   p(s) = (1/2) int d alpha int dv rho_Y( (s - beta^2)/(2v) - alpha beta - alpha^2 v/2 , v , beta + alpha v ),
(substitute u = beta + alpha v at fixed v, du = |v| d alpha; the coarea weight is dv du/(2|v|)). The curves
alpha -> fixed are planar (plane u = beta + alpha v) and are LINES iff beta^2 = s: that is Theorem C (one-sheet),
arc length factor 1 + alpha^2/2 gives (1/2) int 2/(1+alpha^2/2) = pi sqrt 2. For s < 0 no real beta makes them
lines; beta = 0 gives hyperbolas in the pencil of planes through the null T-axis. With T|(V,U) bounded the
hyperbola integral is <= sqrt2/(sqrt(l) sqrt(1+alpha^2)): only 1/|alpha| decay, log divergent - exactly the hub
log. So: a two-sheet fibration exists (pencil of hyperbolas), but its fibre integrals are not 2D marginals.
The "condition on one coordinate" idea IS the pivot: it converts the two-sheet 3D problem into the 2D
hyperbolic Lemma X, and fails exactly when the conditioned row is null.

## N13. The Rudelson-Vershynin pointwise form is false - check of the arguments above
Nothing here uses the pointwise bound |psi(s)| <= 1 - c s^2 / sqrt(2 pi/|s|). Fourier steps used: Lemma 1 of RESULTS
(int |g^|^p <= 4 pi/sqrt p, p >= 2) inside geometric Brascamp-Lieb (Theorem F, Lemma X' light case, Lemma A1 light
case via 1D Hoelder), the Fresnel linearisation, and the Esseen inequality (proved from the Fejer kernel). Real-
variable steps: Lemma 1.2-1.6 of GEOM, Ball/LPP marginal bounds, bathtub. OK.
Stress test (core_adversarial.py, big-jump pairs entering Z0 as a(X+X') and V as a(X-X'), R = 10,100,1000,
c scanned on [-120,120]): two-sheet sup 1.73 / 1.74 / 1.75 / 1.78 for eps = 0.1 / 0.032 / 0.01 / 0, peak at
c = 0, s -> 0-. No trace of the danger mechanism.

## N14. Constants (constants.py) and last attempts on the core
Esseen 1/F(1) = 1.08767. Lemma A1: alpha_1 <= 15.43 A^{-1/2}. Lemma X': alpha_2 <= 27.34 (light), 87.24 (heavy).
sup_s E|Z-s|^{-1/2} <= 57.93 when alpha_2 <= 87.24.  => definite rank three, ANY linear term: <= sqrt2 * 57.93 = 82
(Theorem F gives 12 when all l <= 1/2); indefinite with a heavy row |a_hh| >= c: <= 57.93 / sqrt(c).
In-range definite: 12; spherical means M <= 6/(pi r) = 1.91/r.

Core attempts that did not close:
- Sufficient condition: if (Phi, V') (Phi = light form, V' = hub partner) has joint density <= K on |V'| < 1 then
  p <= 1/c + 2K (substitute phi = s - c v x). But that joint density involves the conditional density of Z at
  ~ s/(2 v eps) and is unbounded for spread laws.
- Big jumps: finitely many coordinates carrying the tail of Z can be conditioned on (lossless) -> shifted core,
  so they cannot create the divergence; a counterexample would need the danger spread over ever more coordinates,
  where Z is sum-like. For supports of diameter <= M this gives p <= C (1 + log_+(eps M/|s|)) (Hoeffding tail of Z),
  not uniform. Uniformity in the spread of the laws is exactly what the twist estimate would supply.

## N15. CORRECTION to the J(tau) numerics (N10)
The first run (twist_J.py) used a fixed grid |y| <= 16. The twist moves the effective V-frequency to y + tau Z, so
the support of |E ...| in y grows like tau sd(Z); the fixed grid undercounts, and the "decrease" to 28.7 at tau=100
was an artifact. twist_J2.py (y-window 14 + 4 tau sd(Z)): corrected J = 72.1 / 71.9 / 71.5 / 68.9 at tau = 0/3/10/30
(m = 60 random), 71.5 / 71.5 / 71.0 / 68.9 (shared block), 68.3 / 68.1 / 67.7 / 66.6 (m = 12). Flat in tau, as the
Gaussian computation predicts exactly: for i.i.d. N(0, s^2) coordinates J(tau) = 2 pi / s^2 = 24 pi = 75.4 for all
tau. Claim to keep: no twist inflation observed, J(tau) ~ J(0).
Side remark worth keeping: Lemma X' is (H2) for EVERY rank-two symmetric matrix (both nonzero |eig| >= 1) with
arbitrary linear terms, and Lemma A1 is alpha_1 for every rank-one matrix plus any linear term; the GEOM report
listed exactly these as the missing ingredient for PSD rank three with a heavy coordinate.

## N16. Final state (for the report)
PROVED: pivot identity (Lemma 1.1); Lemma A1 (alpha_1 <= 15.43 A^{-1/2}); Lemma X' (alpha_2 <= 87.3, any
signature, any linear term; = (H2) for all rank-two matrices); definite rank three <= 82 for all linear terms
(<= 12 in-range; spherical means <= 6/(pi r)); indefinite rank three <= 57.93 c^{-1/2} when a heavy row has
|a_hh| >= c; reduction of rank three to the nearly-null core; localisation lemma; Proposition (twist estimate
J(tau) <= K(1+|tau|) => core bounded, outside terms included); explicit density showing marginal bounds cannot
close the core; fibration identity p(s) = (1/2) int d alpha int dv rho(gamma_{alpha,beta}(v)).
NUMERICAL: core densities flat in eps (1.7-3.6), J(tau) flat.
OPEN: the twist estimate for light frames (or any other proof of the core); the heavy-Z0 conditioning step
(frame no longer orthonormal) is sketched, not written.
Scripts: hub_two_sheet.py, check_identities.py, check_pivot_outside.py, twist_J.py (superseded), twist_J2.py,
core_adversarial.py, constants.py; outputs *_output.txt.

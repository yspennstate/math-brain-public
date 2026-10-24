# NOTES - 11_extremal_laws (reduction of the class of laws / interval laws)

## Entry 1 (setup, structural facts, plan)

Notation. X_i independent, densities f_i <= 1. For a fixed symmetric A put
  D(f_1,...,f_n) := sup_{b,c} || p_{X^T A X + b^T X + c} ||_inf .
The conjecture is sup D <= C over laws with f_i <= 1 when A has 3 eigenvalues of modulus >= 1.

### 1.1 Route 2 is the i.i.d. centred-uniform problem with arbitrary linear terms (PROVED, trivial)
If X_i ~ U[a_i, a_i+1], write X_i = c_i + U_i, c_i = a_i + 1/2, U_i ~ U[-1/2,1/2] i.i.d. Then
  Q(X) = U^T A U + (2Ac + b)^T U + Q(c),
so "the conjecture for unit-interval laws in arbitrary positions" = "the conjecture for i.i.d. U[-1/2,1/2]
coordinates, uniformly over all linear and constant terms". Conditioning on coordinates keeps this class
(the remaining coordinates are still i.i.d. uniform), so the pivot calculus and the reduction GEOM 5.1-5.2
stay inside it: Route 2 is equivalent to (H1)-(H3) for i.i.d. uniform coordinates.

### 1.2 Properties of D (PROVED)
(a) Translation invariance in each coordinate: f_i(. - y) changes b only.
(b) Coordinate convexity: for fixed (b,c,s) the value p(s) is linear in f_i; D is a sup of such, so convex in
    each f_i. Hence D(mixture) <= max over the components (with the other coordinates fixed).
(c) Monotone under convolution: D(f_1 * nu_1, f_2, ...) <= D(f_1, f_2, ...) for every probability nu_1.
    Proof: X_1 + Z_1 with Z_1 ~ nu_1 independent; condition on Z_1: Q(X + Z_1 e_1) is a quadratic form in X with
    the same A and a new linear term; its density is <= D; average over Z_1. Also D(f*nu) <= D(nu*...) is NOT
    available in general because nu may have unbounded density. Note f*nu <= 1 whenever f <= 1, so the class
    is closed under convolution.
(d) Scaling: if X_i = r_i U_i with r_i >= 1 then the matrix becomes R A R (R = diag r) whose eigenvalues are
    theta_k lambda_k(A) with theta_k in [min r^2, max r^2] (Ostrowski), so the count of eigenvalues of modulus >= 1
    is preserved; linear terms are arbitrary anyway.

Consequence (transfer). If the conjecture holds for unit-interval laws (with constant C), it holds with the same C
for every law in the closed convex hull of { U[a, a + r] * nu : a in R, r >= 1, nu a probability }.
[(d) gives widths r >= 1, (c) the convolutions, (b) the mixtures.] This class contains every density of the form
f(x) = G(x + 1/2) - G(x - 1/2) (G a distribution function), every symmetric unimodal density that is flat on the
unit interval around its mode, all triangular/trapezoidal laws with plateau >= ... ; it does NOT contain uniform
laws on spread sets (these are extreme points: 1_E = 1_F * nu with |F| = 1 forces nu = delta).
So Route 2 alone reaches every law except the "spread" ones; the gap between Route 2 and the conjecture is
exactly the extreme points that are not intervals.

### 1.3 Exact hub formula for an interval hub law (PROVED)
Q = 2 X_h Lt + R(X'), Lt = <w, X'> + beta, X_h ~ U[c - 1/2, c + 1/2] independent of X'. Write X_h = c + U:
2 X_h Lt = 2 U Lt + 2 c Lt and absorb 2 c Lt into R (a linear term). Given X', Q is uniform on the interval
R + [-|Lt|, |Lt|], so for a.e. s
   p_Q(s) = (1/2) E[ |Lt|^{-1} 1{ |s - R| <= |Lt| } ].                                   (H)
Dyadic decomposition in |Lt|:  p_Q(s) <= 1/2 + sum_{k>=0} 2^k P(|Lt| <= 2^{-k}, |R - s| <= 2^{-k}).
So: a PAIR small-ball bound P(|Lt| <= d, |R - s| <= d) <= K d^{1+theta} (theta > 0, uniform in s, beta and in the
linear terms of R) gives ||p_Q|| <= 1/2 + K 2^{1+theta}/(1 - 2^{-theta}).
For a general hub law f_h = 1_{E_h}, E_h = union of intervals of lengths w_j, the same computation gives a sum over
the pieces of K' w_j^theta (each piece is a wedge with its own slope, absorbed into its own linear term), which is
bounded only if theta = 1 (bounded joint density of (Lt, R)); for a comb with N teeth the bound grows like
N^{1-theta}. So the interval law of the hub coordinate lowers the requirement from theta = 1 to any theta > 0.
In the canonical untwisted case R = lambda V^2 + (independent) the pair bound holds with theta = 1/2.

### Plan
(i) Numerics for Route 1: exact (fibre / conditional) estimators; best interval configuration; best-response
    functions g_i(x) = density of Q at s* given X_i = x; is the top measure-one superlevel set an interval?
(ii) Look for an explicit form in the class where a non-interval set strictly beats every interval configuration.
(iii) Theory for Route 2: what the exact hub formula gives (zero and small nonzero hub diagonal); rank-three
     convex side via log-concavity of projections of the cube (Archimedes + John).

## Entry 2 (numerics n = 3: best responses from intervals) - NUMERICAL

Tools: q3tools.py (exact partial densities g_i(t) by quadrature with the partition of unity
(d_u q)^2 + (d_w q)^2 = |grad q|^2 over the two free coordinates; integrand capped at 1/eta, which moves the
integral by O(eta) - needed because a node next to a critical point gives a 1/r spike that fooled Nelder-Mead
once, value 2702). Validated: sphere density 2 pi sqrt(s) and 3 pi - 4 pi sqrt(s) (errors < 3e-3), and a random
matrix with linear terms and two-piece laws against 4e6-sample Monte Carlo (0.1119 vs 0.1119; 0.1364 vs 0.137).
altbr3.py: for invertible A the linear term can be removed by translating the sets, so b = 0 and alternate
exact best responses over sets (top measure-one set of g_i on a grid of cell 1/100 over [-6,6]), s re-optimised.

Results (value p after 4 sweeps; start = centred intervals / random 2-4 piece sets spread over [-3,3]):
  I - 2ee^T        2.57 / -       intervals are a fixed point
  example (a)      2.57 / 2.55    both end in single intervals (random start: shifted intervals)
  2I - J           1.53 / 1.49    single intervals
  -(J - I)         2.09 / 2.09    single intervals
  diag(1,1,-1)     3.15 / 3.13    single intervals (= pi, the separable bound)
  diag(4,1,-1)     1.59 / 1.58    coordinate 0: only |x_0| <= 0.26 is useful (g_0 = 0 outside), the spare
                                  mass lands anywhere -> the optimal set is not unique, intervals included
  diag(9,1,1)      1.05 / 0.84    same non-uniqueness; the random start ends in a GENUINE non-interval local
                                  optimum (coordinate 1 = symmetric pair [-0.69,-0.19] u [0.19,0.69], s = 0.47)
                                  with a lower value (0.84 < pi/3 = 1.047)
  rand0..rand5     0.46,1.07,1.46,0.64,2.04,0.94  (random matrices scaled to min|eig| = 1): single intervals
                                  except rand3, see below.
rand3 (negative definite, eig -11.41, -2.55, -1): best responses at s = -0.39 have holes ([-0.56,0.56] minus two
gaps of width 0.06 near +-0.35). Explanation (PROVED, elementary): for a definite 2x2 principal block B_jk,
conditioning on the third coordinate gives g_i(t) <= pi / sqrt(det B_jk), with EQUALITY for every t whose slice
ellipse lies inside the box of the other two coordinates (the density of a 2D definite quadratic under Lebesgue
measure is the constant pi/sqrt(det B), Lemma 1.3). So g_i is FLAT-TOPPED and dips exactly where the slice
ellipse leaves the box - the partial densities of definite forms are not unimodal, and at a suboptimal s the best
response has holes. But p <= min_{j<k} pi/sqrt(det B_jk) = 0.6475 for EVERY product law, and centred intervals
already give 0.647 (s = -0.45): no gain is possible and the holes are an artefact of the suboptimal s.

Conclusion (NUMERICAL): at n = 3 no set configuration beat the best interval configuration beyond quadrature
error (+-0.005). Two mechanisms that make the extremal set non-interval were seen, neither of which increases
the supremum: (1) large diagonal entry -> only a short window of that coordinate is useful -> non-uniqueness;
(2) flat-topped partial densities of definite blocks -> holes at suboptimal s. The one genuine non-interval local
optimum (symmetric pair for a coordinate entering through x^2) is worse than the interval optimum.

## Entry 3 (Route 2: the 3D coarea inequality holds for quasi-concave densities -> rank 3 + k for interval laws)

Correction: RV Lemma 3.1 bounds the decreasing rearrangement of |psi| only; the pointwise form
is false for spread sets. NOTHING here uses it. (The only pointwise decay mentioned anywhere in these notes is the
exact sinc of an INTERVAL law, which is a different, true statement; it is not used in any proof below either.)

### 3.1 Ball lemma (to be checked numerically)
X uniform on the unit ball B of R^3, P(x) = sum_k m_k (x_k - c_k)^2 + const (every nondegenerate quadratic polynomial
has this form after a rotation, which preserves B). Then ||p_{P(X)}||_inf <= C_ball |m_1 m_2 m_3|^{-1/3}.
Proof. Pivot on coordinate 1: given (X_2,X_3), X_1 is uniform on a chord of half-length h = sqrt(1 - x_2^2 - x_3^2),
the density of m_1(X_1 - c_1)^2 at y is <= 1/(2 h sqrt(|m_1| |y|)), and (X_2,X_3) has density 3h/(2 pi) on the unit
disc; the chord factor cancels: p_P(s) <= (3/(4 pi)) |m_1|^{-1/2} int_disc |s - R|^{-1/2}, R = m_2(.)^2 + m_3(.)^2.
Definite R: area{|R - s| < u} <= 2 pi u / sqrt(D), D = |m_2 m_3|, and area <= pi, so int <= 2 pi sqrt2 D^{-1/4}.
Indefinite R: Lebesgue on [-1,1]^2 = 4 x (product of U[-1,1], densities 1/2 <= 1); GEOM Lemma 1.4 gives
area <= (8u/sqrt D)(6.2 + log_+(16 sqrt D/u)), and substituting lambda = D^{-1/4} mu in the layer cake,
int <= C_ind D^{-1/4} with C_ind = int_0^inf min(pi, 8 mu^{-2}(6.2 + log_+ 16 mu^2)) d mu  (NO log of D survives).
Choice of pivot (|m_1| >= |m_2| >= |m_3| up to relabelling): all signs equal -> pivot on the largest; signature with
minority coordinate j: if m_j^2 >= product of the other two, pivot on j (remaining block definite), else pivot on the
largest of the other two (remaining block indefinite). In each case |m_pivot|^{-1/2} D^{-1/4} <= |m_1 m_2 m_3|^{-1/3}
(the condition is D <= m_pivot^2, checked in each case).
### 3.2 Convex bodies (CG)
mu_r(C) := int_C delta(q(z) - r) dz <= C_CG |det M_0|^{-1/3} vol(C)^{1/3} for every convex body C in R^3, every
quadratic polynomial q with nondegenerate quadratic part M_0 and a.e. r.
Ellipsoid E = c + T B: mu_r(E) = |det T| vol(B) p_{q(c+TX)}(r), quadratic part T^T M_0 T, det = det(T)^2 det M_0,
so mu_r(E) <= (4 pi/3)^{2/3} C_ball |det M_0|^{-1/3} vol(E)^{1/3}; John: E_J <= C <= 3 E_J, mu_r monotone in the set
-> C_CG = 3 (4 pi/3)^{2/3} C_ball.
### 3.3 Theorem (3D coarea for quasi-concave densities)
Z in R^3 with density g <= K whose superlevel sets are convex (e.g. log-concave): p_{q(Z)} <= C_CG |det M_0|^{-1/3} K^{2/3}.
Layer cake g = int_0^K 1_{C_t} dt, int vol(C_t) dt = 1, Hoelder int_0^K vol(C_t)^{1/3} dt <= K^{2/3}.
[This is the inequality that RESULTS section 1 shows FALSE for general densities (thin shells are not convex).]
### 3.4 Theorem (bounded rank, interval laws)
X uniform on an axis-parallel unit cube (any position). A = R Lambda R^T + R' Lambda' R'^T (orthonormal columns,
Lambda 3x3 with |lambda_k| >= 1, R' of width k, Lambda' arbitrary). Any b, c. Let Y' = (R'^T X, <u, X>) in R^{k'}
(u = unit vector along the part of b orthogonal to range(A); k' = k or k+1). The (3+k')-marginal (Y, Y') is
log-concave with density <= 2^{(3+k')/2} (LPP); given Y' = y', Y is log-concave with sup <= 2^{(3+k')/2}/rho_{Y'}(y');
Q = q(Y) + (function of y'). Hence p_Q <= C_CG |det Lambda|^{-1/3} 2^{1 + k'/3} int_{R^{k'}} rho_{Y'}^{1/3}.
Y' is log-concave with covariance I/12 (orthonormal frame, Var X_i = 1/12) and sub-Gaussian; Hoelder with the weight
(1 + |y|/sigma)^{3k'+1}... gives int rho^{1/3} <= C^{k'}. For k' = 1: int rho_U^{1/3} <= (E(1+|U-m|/s)^3)^{1/3}(4 s)^{2/3}
<= 2.6 with s = 1/sqrt 12.  => RANK THREE (all signatures, all linear terms, any dimension) is BOUNDED for interval
laws; rank 3 + k with constant C^{k+1}. For general laws rank three is open on the convex side (only 60(n-2)).
TO DO: numbers for C_ind, C_ball; numerical check of the ball lemma and of 3.4 on a heavy-leverage example.

## Entry 4 (constants, checks, the fixed-s counterexample)
Constants (ball_check.py): C_ind = int_0^inf min(pi, 8 mu^{-2}(6.2 + log_+ 16 mu^2)) d mu = 38.19; definite 2 pi sqrt2 = 8.886;
C_ball = (3/(4 pi)) max = 9.117; C_CG = 3 (4 pi/3)^{2/3} C_ball = 71.07.
Ball lemma checked on 3e6 uniform points of the ball, 56 shapes (log|m| up to +-4, both signatures, centres up to
~3.7 away): max_s p * |m1 m2 m3|^{1/3} <= 1.72 (the centred sphere, true value 1.5; histogram noise), bound 9.12. NUMERICAL.
Integral of rho^{1/3} (clean version): Y' in R^{k'} orthogonal projection of a uniform unit cube: E e^{<theta, Y'-m>}
<= e^{|theta|^2/8} (Hoeffding, each coordinate in an interval of length one), so E e^{|Y'-m|^2} <= 2^{k'/2}
(Gaussian trick, E_G e^{sqrt2 <G,V>}), and Hoelder with w = e^{|y-m|^2}:
  int rho^{1/3} <= (E w(Y'))^{1/3} (int w^{-1/2})^{2/3} = 2^{k'/6} (2 pi)^{k'/3} <= 2.07^{k'}.
So Theorem 3.4 holds with ||p_Q|| <= C_CG 2^{(3+k')/3} 2.07^{k'} |det Lambda|^{-1/3} = 142.1 * 2.61^{k'} |det Lambda|^{-1/3}.
Rank-3 check on cubes (rank3_cube_check.py; n = 10, 40; leverage of coordinate 0 = 0.09, 0.90; signatures (+++),
(++-), (+--); outside linear term gamma = 0, 0.3, 3; cube in random position): all maxima between 0.39 and 3.55. NUMERICAL.
Fixed-s rearrangement is FALSE (exact, sphere_fixed_s.py): Q = X1^2 + X2^2 + X3^2, X2, X3 ~ U[-1/2,1/2], s = 0.3. The
partial density g_1(t) = p_{|W|^2}(0.3 - t^2) equals pi for 0.2236 <= |t| <= 0.5477 and dips to 1.4595 at t = 0 (the
circle leaves the square). Every unit interval gives <= 2.5419; the set [-0.5477,-0.0477] u [0.0477,0.5477] gives 2.7014.
But sup_s over all laws is pi (2D definite lemma), attained by centred intervals at s = 1/4. So any rearrangement
statement must be about the supremum over s (and linear terms), not about fixed s.

## Entry 5 (simplifications and audit before the report)
- Ball lemma: pivot simply on the eigenvalue of LARGEST modulus. Then D = |m_j m_k| <= m_p^2 automatically and
  |m_p|^{-1/2} D^{-1/4} = |m1 m2 m3|^{-1/3} (D/m_p^2)^{1/12} <= |m1 m2 m3|^{-1/3}; the indefinite 2D layer cake has NO
  log D (substitution lambda = D^{-1/4} mu), so no case analysis on the signature is needed.
- Analytic check of Theorem 3.3 on the worst shape for the cone: q = 2ab + z_2^2 (a normal to the tangent plane along a
  ruling), Z uniform on |a| <= d/2, 0 <= b <= L, |z_2| <= sqrt(dL): p_{q(Z)}(0) = 1/(dL), K^{2/3} = 2^{-2/3}(dL)^{-1},
  ratio 2^{2/3} for every d, L. Bounded, as claimed.
- Scale invariance of Theorem 3.3 checked (Z -> lambda Z: K -> lambda^{-3} K, |det M0|^{-1/3} -> lambda^2 |det M0|^{-1/3}).
- Hub remark calibration: R = lambda V^2 + G, G independent of (L,V): rectangle bound K = 8 sqrt(2/|lambda|), theta = 1/2,
  uniform in the tilt c (for fixed l the v-set has measure <= 2 sqrt(2 rho/|lambda|)).
- Nothing uses the pointwise form of RV Lemma 3.1.
Status: Route 1 PARTIAL (structural reduction + fixed-s FALSE + numerics); Route 2 PARTIAL (bounded rank PROVED,
hubs reduced to a pair small-ball estimate; dense twist open).

## Entry 6 (answer to the hub-law question: when is the interval the worst hub law?)
Q = 2 X_h T + S(X'), zero hub diagonal. p_Q(s) = int f_h g, g(x) = p_{S + 2xT}(s) = int rho(tau, s - 2 x tau) d tau:
g is the X-RAY TRANSFORM of the joint density of (T, S) along the lines through the single point (0, s), x = minus half
the slope. So sup over hub laws = bathtub value int_0^inf min(1, |{g > l}|) dl <= 2 ||g||_{L^{2,inf}}.
(a) Singular directions of g = tangent directions at (0, s) of the singular curves of rho (for S = lambda V^2 + ...:
    the critical-value curve sigma = kappa(tau) of S on the slices {T = tau}); one curve -> one singularity of g ->
    interval within a constant. A spread hub set gains only by collecting several singular directions.
(b) Sufficient condition for ALL hub laws (PROVED, same dyadic argument as (H)): if for every measurable family of
    sets Gamma(tau) with |Gamma(tau)| <= 2|tau|, P(|T| <= d, S in Gamma(T)) <= K d^{1+theta} (d <= 1), then
    ||p_Q|| <= 1/2 + K/(1 - 2^{-theta}) for every hub law (take Gamma(tau) = s - 2 tau E_h). This "set-uniform" pair
    bound follows from weak-L^{1/(1-theta)} control of the conditional density of S given T (theta = 1/2: weak L^2);
    the rectangle pair bound is not enough for combs (sum_j w_j^theta).
(c) Their degenerate hub Q = 4 X_h L + 2L^2 + 2V^2 + D, D = sum d_i X_i^2: completing the square in L,
       S + 2xT = 2(L + x)^2 - 2x^2 + 2V^2 + D,   so g(x) = p_{F_x}(s + 2x^2),  F_x = 2(L + x)^2 + 2V^2 + D,
    and sup over ALL hub laws <= sup_beta || p_{2(L+beta)^2 + 2V^2 + D} ||_inf. For D = 0 this is <= pi for every law of
    every coordinate ((L,V) has density <= 2, definite binary form of determinant 4, Lemma 1.3): the hub law is
    irrelevant. With D != 0 the question becomes a bounded density for "two eigenvalues 2, 2 of the same sign + small
    diagonal", uniformly in the shift along w - no rearrangement needed. Numerics (hub_all_laws_check.py, n = 40,
    hub laws interval / 5-tooth / 40-tooth combs over [-6,6], leaves interval / 3-tooth combs, D = 0 or random 0.05):
    max density 1.71 (interval hub, interval leaves); every spread hub law gave <= 0.30. NUMERICAL.

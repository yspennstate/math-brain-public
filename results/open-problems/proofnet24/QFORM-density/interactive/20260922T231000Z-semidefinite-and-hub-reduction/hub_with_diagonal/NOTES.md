# 08 - one hub with small nonzero diagonal, general remainder. Working notes.

Start 02:10 (clock of the machine), notes begun 02:32.

Setting. Q = a X_h^2 + 2 X_h t + R(X'), t = L + beta, L = <w, X'>, X_h independent of X' = (X_i)_{i != h},
f_h <= 1 the density of X_h. Full matrix A = [[a, w^T],[w, M]].

## Piece 1 (02:32). Exact identities. Status: PROVED (elementary; checked twice below).

(1.1) Conditioning on X'. Given X', Q = g(X_h), g(x) = a x^2 + 2 x t + R. With u = a x + t,
   a x^2 + 2 x t = (u^2 - t^2)/a, so the roots of g = s are u_pm = pm sqrt(Delta), Delta = t^2 + a (s - R),
   x_pm = (u_pm - t)/a, and |g'(x_pm)| = 2|u_pm|. Hence
      p_Q(s) = E[ sum_{pm} f_h(x_pm) / (2 sqrt(Delta)) ; Delta > 0 ].
   Delta = a (s - kappa), kappa = R - t^2/a is the random centre of the square-root singularity.
   Delta is a quadratic polynomial in X' with matrix w w^T - a M.

(1.2) Conditioning on X_h. Given X_h = x, Q = a x^2 + Y_x with Y_x = R + 2 x t (matrix M, linear part b + 2 x w):
      p_Q(s) = int f_h(x) p_{Y_x}(s - a x^2) dx.
   Note Y_x + a x^2 = R + 2 x (L + beta + a x / 2): the nonzero diagonal is the SAME as the zero-diagonal hub with an
   x-dependent offset beta(x) = beta + a x/2. So any zero-diagonal bound that is uniform in beta INSIDE the x-integral
   (i.e. controls int f_h(x) sup_sigma p_{R + 2xL}(sigma) dx) transfers to every a. This "sup over centres" statement
   fails in the Prop 5.4 configuration (see piece 3), so the transfer is not free in the real-variable route.

(1.3) Split. Roots with |a x + t| >= 1 contribute <= E[2 * 1/2] = 1. So p_Q(s) <= 1 + T(s),
      T(s) = E[ sum_{roots, |u| < 1} f_h(x)/(2|u|) ] = int int rho_{t,R}(t, r) K_s(t, r) dt dr,
      K_s(t, r) = sum_{x : a x^2 + 2 x t + r = s, |a x + t| < 1} f_h(x) / (2 |a x + t|)
   (rho_{t,R} is the joint law of (t, R); where it has no density read the integrals against the measure).

(1.4) Tangent-line representation. Parametrize the (t, r)-plane by (u, x), t = u - a x, r = s + a x^2 - 2 x u.
   Jacobian: d(t,r)/d(u,x) = det [[1, -a], [-2x, 2 a x - 2 u]] = -2u, so dt dr = 2|u| du dx and
      T(s) = int f_h(x) [ int_{-1}^{1} rho_{t,R}(u - a x, s + a x^2 - 2 x u) du ] dx.
   For fixed x the inner integral runs over the segment {(t, r) = (-a x, s + a x^2) + u (1, -2x)}, which is the
   TANGENT line to the parabola Gamma_s = {r = s + t^2/a} at its point with t = -a x (slope of Gamma_s there is
   2 t/a = -2x). Full line = {r = s - a x^2 - 2 x t}; its X-ray (dt measure) of rho_{t,R} is p_{Y_x}(s - a x^2).
   At a = 0 the lines {r = s - 2 x t} form the PENCIL through (0, s); for a != 0 they form the tangent family of
   Gamma_s, whose vertex is (0, s). In the coordinates (t, kappa), kappa = r - t^2/a, the tangent line at x becomes the
   curve kappa = s - (t + a x)^2/a: horizontal translates of one parabola.
   Check (second way): the (u,x) formula gives back (1.3) because at a point (t,r) of the segment the kernel weight is
   f_h(x)/(2|u|) and dt dr = 2|u| du dx; and it gives back (1.2) because the full-line integral is the density of
   R + 2 x t at s - a x^2 (coarea along a line with dt measure).

(1.5) Kernel masses (f_h <= 1, int f_h = 1):
   (i)   int int K_s dt dr = int f_h(x) int_{-1}^1 du dx = 2.
   (ii)  for fixed t: int K_s(t, r) dr = int f_h(x) 1{|a x + t| < 1} dx <= min(1, 2/|a|).
   (iii) for fixed r, sigma = s - r: int K_s(t, r) dt = G_a(sigma) := int f_h(x) 1{|a x^2 + sigma| < 2|x|} dx/(2|x|).
         Proof: at fixed r the root relation is t = (sigma - a x^2)/(2x), |dt/dx| = |sigma + a x^2|/(2x^2), and
         a x + t = (a x^2 + sigma)/(2x); the product of the weight and |dt/dx| is f_h(x)/(2|x|).
         On the support |sigma| < 2|x| + |a| x^2, i.e. |x| > x_*(sigma) = |sigma|/(1 + sqrt(1 + |a sigma|)). Bathtub:
            G_a(sigma) <= log(1 + 1/(2 x_*)) = log(1 + (1 + sqrt(1 + |a sigma|))/(2|sigma|)).
         For |a sigma| <= 1 this is <= log(1 + 1.21/|sigma|): the SAME log profile as at a = 0.

Consequences (PROVED from (1.5)):
 (C2) Bounded joint density: T(s) <= 2 ||rho_{L,R}||_inf, so p_Q <= 1 + 2 ||rho_{L,R}||_inf for EVERY a, beta.
 (C1) Bounded conditional density of L given R, rho_{L,R}(l, r) <= kappa_0 rho_R(r): by (iii),
      T(s) <= kappa_0 E G_a(s - R) <= kappa_0 E log(1 + (1 + sqrt(1 + |a||s - R|))/(2|s - R|)).
      So the hub has a type-2 (logarithmic) profile around the centre R with constant kappa_0, uniformly in a, and
      by Lemma 1.6 of GEOM, p_Q <= 1 + kappa_0 (2 log_+ alpha_1(R) + C). The diagonal a costs nothing here.
 Neither hypothesis holds in the Prop 5.4 model (R = lambda (V - v_c(L))^2 + F_c(L)), where rho_{L,R} has a square-root
 singularity along the curve r = F_c(l); that is the case where a enters (through D_H = |1 - a sigma_F|).

Next: (a) the square-root/centre composition (generalizing Prop 5.4), (b) the Fourier transfer, (c) numerics.

## Piece 2 (about 02:55). Square-root profile around a centre: the composition that tracks the random centre.

(SQ) Hypothesis on (L, R): there are K and a random variable C (jointly distributed with L) with
     E phi(L, R) <= K E[ int phi(L, r) |r - C|^{-1/2} dr ]   for all phi >= 0
   ("R has a square-root profile around C, along L"). Typical source: R = lambda (V - D)^2 + C where V has conditional
   density <= kappa_V given (L, D, C): then K = kappa_V |lambda|^{-1/2}.
   Lebesgue variant (SQ_leb): rho_{L,R}(l, r) <= K' E_Xi |r - C(l, Xi)|^{-1/2} with Xi independent of L, Lebesgue in l;
   typical source: (L, V) with joint density <= K_2, R = lambda (V - D(L, Xi))^2 + C(L, Xi): K' = K_2 |lambda|^{-1/2}.

Lemma 2.1 (reduction to the centre). Under (SQ), T(s) <= K N_a(s),
      N_a(s) = E[ 1{|a X_h + t| < 1} |s - a X_h^2 - 2 X_h t - C|^{-1/2} ],  X_h independent of (L, C).
   Proof: int K_s(t, r) phi(r) dr = int f_h(x) 1{|ax+t|<1} phi(s - a x^2 - 2 x t) dx (substitute r = s - a x^2 - 2xt
   at fixed t, dr = 2|ax + t| dx), applied with phi = |. - C|^{-1/2}. PROVED.
   So the question becomes a LOWER-LEVEL one: the negative half-moment of the hub with remainder C, on the slab.

Lemma 2.2 (the one-dimensional kernel). For fixed (t, sigma) put
      J_a(t, sigma) = E[1{|a X_h + t| < 1} |sigma - a X_h^2 - 2 X_h t|^{-1/2}],  Delta = t^2 + a sigma.
   Then  J_a <= 8 max(|Delta|, a^2/16)^{-1/4} + sqrt(2) |a|^{-1/2} log_+(a^2/(16 |Delta|)),
   and at a = 0, J_0 <= 2 |t|^{-1/2}.
   Proof. phi(x) = sigma - a x^2 - 2xt = -a(x + t/a)^2 + Delta/a. Lebesgue measure of {|phi| < eps} is
   <= min(2 sqrt(2 eps/|a|), 4 eps / sqrt(max(|Delta|, |a| eps))) (Lemma 1.2(ii) of GEOM with f = 1; |a| * |critical
   value| = |Delta|). Bathtub: J_a <= int_0^inf min(1, m(lam)) dlam with m(lam) = |{|phi|^{-1/2} > lam}|, i.e. eps = lam^{-2}.
   If |Delta| >= a^2/16: for lam >= lam_1 = 2|Delta|^{-1/4} one has |a| lam^{-2} <= |Delta| and m <= 4 lam^{-2} |Delta|^{-1/2},
   so J <= lam_1 + 4|Delta|^{-1/2}/lam_1 = 4 |Delta|^{-1/4}.
   If |Delta| < a^2/16: with lam_0 = sqrt(|a|/|Delta|), lam_2 = 2 sqrt 2/sqrt|a| < lam_0, use m <= 2 sqrt 2/(lam sqrt|a|) on
   [lam_2, lam_0] and m <= 4 lam^{-2}|Delta|^{-1/2} beyond: J <= |a|^{-1/2}(4 + 2 sqrt 2 + sqrt 2 log(a^2/(8|Delta|))).
   Both are <= the displayed bound. At a = 0, 2 X_h t has density <= 1/(2|t|) and sup_c E|c - Z|^{-1/2} <= 2 sqrt 2 D^{1/2}
   for density <= D. PROVED (constants re-derived twice; see numerics check in piece 4).

Theorem 2.3 (composition under SQ). Under (SQ),
      p_Q(s) <= 1 + K E[ 8 max(|Delta_C|, a^2/16)^{-1/4} + sqrt 2 |a|^{-1/2} log_+(a^2/(16 |Delta_C|)) ],
      Delta_C = (L + beta)^2 + a (s - C).
   At a = 0 the right side is 1 + 8 K E|L + beta|^{-1/2} <= 1 + 8 K 2^{7/4} |w|^{-1/2} FOR EVERY CENTRE C.
   For a != 0 what is needed of the centre is exactly a negative quarter moment of the quadratic Delta_C = t^2 - a (C - s).
   It is large only if (t, C) concentrates near the parabola C = s + t^2/a = Gamma_s: the centre curve of R aligned with
   the tangent family. This is the precise sense in which the proof "tracks the random centre".
   Special cases (PROVED):
   (i) C = sigma L^2 + C1 L + C0 with (C1, C0) random but sigma deterministic and L having density <= D_L given (C1, C0):
       Delta_C = (1 - a sigma) (t - m)^2 + k, and by Cauchy-Schwarz on the two linear factors
       E|Delta_C|^{-1/4} <= |1 - a sigma|^{-1/4} sup_c E|t - c|^{-1/2} <= |1 - a sigma|^{-1/4} 2 sqrt 2 D_L^{1/2}
       (for k >= 0 bound by E|t - m|^{-1/2}; for k < 0 factor (t - m - r)(t - m + r) and use Cauchy-Schwarz).
       The log term is harmless (it lives on |Delta_C| < a^2/16 and contributes O(|a|^{1/2}) there... to be written out).
       D_H = |1 - a sigma| is Prop 5.4's determinant; here it appears to the power -1/4 (the elliptic Psi of Prop 5.4).
   (ii) C independent of L: Delta_C = t^2 + (independent shift) and E|Delta_C|^{-1/4} <= sup_k E|t^2 + k|^{-1/4}, uniform in a.

Remark 2.4 (generalized Prop 5.4 by conditioning). If R is any quadratic polynomial in (L, V, Xi), with Xi a vector of
   coordinates disjoint from supp(w) u supp(v), and the V^2-coefficient lambda != 0, then completing the square in V gives
   R = lambda (V - D(L, Xi))^2 + sigma_F L^2 + c1(Xi) L + c0(Xi), sigma_F = sigma - gamma^2/lambda deterministic. Given Xi this
   is Prop 5.4's F(L, V) with changed affine parts, and Prop 5.4 is uniform in those, so the bound of Prop 5.4 holds as it
   stands. So Prop 5.4 already covers: hub + rank one on the support of (w, v) + ARBITRARY remainder elsewhere + arbitrary
   bilinear coupling of (L, V) with the rest. What it does not cover is a remainder that depends on the coordinates of
   supp(w) other than through L and V (the dense twist).

Remark 2.5 (a one-parameter family of completions). For any sigma with a sigma != 1 put R_sigma = R - sigma t^2 and
   q_sigma(x, t) = a x^2 + 2 x t + sigma t^2 (det a sigma - 1). If the conditional density of t given R_sigma is <= kappa_0 then,
   given R_sigma, (X_h, kappa_0 t) is a product pair with densities <= 1 and Q = q_sigma + R_sigma, so Lemma 1.3/1.4 give
      p_Q(s) <= kappa_0 |1 - a sigma|^{-1/2} (5.2 + E log_+(16 sqrt|1 - a sigma| /(kappa_0 |s - R_sigma|)))   (a sigma < 1),
      p_Q(s) <= pi kappa_0 / sqrt(a sigma - 1)                                                     (a sigma > 1).
   sigma = 0 is (C1). As sigma -> 1/a the constant blows up, but that is an artifact of Lemma 1.4's constant term for very
   unequal eigenvalues; at sigma = 1/a exactly (q = Z^2/a, Z = a X_h + t, rank one) the type-1 route gives instead:
   (C5) if t has conditional density <= kappa_0 given kappa = R - t^2/a, then
      p_Q(s) <= 1 + kappa_0 |a|^{1/2} E[|s - kappa|^{-1/2}; |s - kappa| < 1/|a|]
   (E_t f_h((Z - t)/a) <= kappa_0 |a| given kappa, two roots, |Z_pm| = sqrt(|a||s - kappa|)). PROVED.
   So the degenerate end (hub block of rank one: really a spread square with eigenvalue ~|w|^2/a) needs level 2 (H2) of
   the centre kappa and pays only |a|^{1/2}; the genuine-hub end needs level 1 of R. Which end applies is decided by
   D_H, see piece 3.

## Piece 3 (about 03:05). Kernel constant, Fourier transfer, eigenvalue dichotomy, examples.

Kernel constant simplified (PROVED). log x <= (4/e) x^{1/4} for x >= 1 turns the log term of Lemma 2.2 into
   sqrt 2 |a|^{-1/2} (4/e)(a^2/16)^{1/4} |Delta|^{-1/4} = 1.04 |Delta|^{-1/4}, so   J_a(t, sigma) <= 9.05 |t^2 + a sigma|^{-1/4}
   for all a (the a-dependence is only through Delta). Numerics (num/k1b_kernel_exact.py, exact level-set measure,
   3000 random (a, Delta), a in 10^[-4,0], |Delta| in 10^[-9,2]): worst ratio J/(9.05|Delta|^{-1/4}) = 0.32;
   J/(two-regime bound) <= 0.74. Note J_a can exceed J_0 by sqrt 2 as a -> 0 (the second root x = -2t/a, inside the
   slab, can carry mass of an adversarial f_h): the tangent family has two tangents from each point outside Gamma_s.
   The kernel-mass bound G_a of (1.5)(iii) is attained (ratio 1.00): sharp.
   So Theorem 2.3 reads:  p_Q(s) <= 1 + 9.05 K E|(L + beta)^2 + a (s - C)|^{-1/4}.

Proposition F (Fourier transfer; PROVED, one line). phi_Q(tau) = int f_h(x) e^{i tau (a x^2 + 2 x beta)} E e^{i tau (R + 2xL)} dx,
   so |phi_Q(tau)| <= B(tau) := int f_h(x) |E e^{i tau (R + 2 x L)}| dx, which does not depend on a or beta. Hence
      ||p_Q||_inf <= (1/2pi) int min{1, B(tau)} dtau   for every hub diagonal a.
   B(tau) <= (1/(2|tau|)) int |E e^{i(theta L + tau R)}| dtheta. Every zero-diagonal hub bound proved through B (Theorem H's
   first step is exactly this inequality; that is why A_HH is arbitrary there) holds verbatim for every a.
   Limitation: B is not integrable when R has curvature along w. For R = lam V^2 + mu L^2 with L, V independent
   Gaussian-like, int|E e^{i tau(mu L^2 + y L)}| dy ~ sqrt(4 pi |mu|) |tau|^{-1/2} (twist inflation), so
   B(tau) ~ sqrt(pi|mu|/(2|lam|)) |tau|^{-1}: log-divergent for EVERY a, including a = 0, although the density is bounded
   (Prop 5.4). So the Fourier route is blind to a but not to the curvature mu of R along w; the real-variable route
   (Prop 5.4, Theorem 2.3) is blind to mu at a = 0 and sees only the product a*mu through D_H = |1 - a mu|.

Lemma E (hub block dichotomy; PROVED). Let B = [[a, W],[W, m]], W >= 1, |a| < c <= 1/8, sigma = m/W^2. If both eigenvalues
   of B have modulus >= 1 then |sigma| < 4 and D_H = |1 - a sigma| >= 1 - 4c >= 1/2.
   Proof: if |sigma| >= 4, the eigenvalues have |mu_1 + mu_2| >= |sigma| W^2 - c and |mu_1 mu_2| = W^2 |1 - a sigma|
   <= W^2 (1 + c|sigma|), so the smaller one has modulus <= 2(1 + c|sigma|)/(|sigma| - c) <= 2(1.5)/3.875 < 1 (the bound
   decreases in |sigma|). Conversely D_H <= 1/2 forces |sigma| >= 1/(2|a|) and then the small eigenvalue has modulus
   <= 2|a| W^2/(W^2 - 2a^2) ~ 2|a|: the block is a rank-one piece (a, w)(a, w)^T/a, i.e. a delocalized square with
   eigenvalue ~W^2/a, not a hub.
   In the Prop 5.4 model (R = lam V^2 + sigma L^2, V decoupled) three eigenvalues of modulus >= 1 in the core with the hub
   block carrying two of them therefore give D_H >= 1/2 automatically: the nonzero diagonal is harmless there.
   Degenerate end (D_H small): the third large eigenvalue must come from outside the core, so R' = R - sigma t^2 then has
   two large eigenvalues and the type-1 route (C5) applies with the small constant |a|^{1/2}.

Examples showing what the composition must look like (PROVED by direct computation):
 (E1) Marginal hypotheses on R are never enough, even at a = 0. R = 2 Y L + c with Y an extra coordinate independent of
      (X_h, L): R has alpha_2(R) bounded (it is itself a hub) and L is spread, yet at beta = 0
      Q = a X_h^2 + 2(X_h + Y) L + c and at a = 0 Q = 2 Z L + c with Z = X_h + Y of density <= 1: log-divergent density at c.
      (A has only two nonzero eigenvalues ±sqrt 2 W: the two hub rows are parallel.) Any composition lemma must be joint
      in (L, R); the joint quantity here is the conditioning of the pair of hub rows (Prop 5.5's sigma_min).
 (E2) The zero-diagonal bound does not transfer to a != 0 without D_H. R = t^2/a0 + lam V^2 with V independent of
      (X_h, L), lam a0 < 0. At a = 0: p_Q <= E[(2|t|)^{-1} min(1, C sqrt(|t|/|lam|))] < inf (Prop 5.4 at a = 0, uniform in
      sigma_F). At a = a0: Q = Z^2/a0 + lam V^2, Z = a0 X_h + t, a hyperbolic form in the product pair (Z, V):
      p_Q(s) ~ sqrt(|a0|/|lam|) rho_Z(0) rho_V(0) 2 log(1/|s|) near s = 0: unbounded. For a near a0 the singularity is
      cut off at the scale set by D_H = |1 - a/a0|: growth log(1/D_H) with the small factor |a0|^{1/2} (elliptic case
      lam a0 > 0: bounded). A here has eigenvalues ~W^2/a0, lam and one of modulus ~|a0| D_H: two large eigenvalues only,
      so this is consistent with the conjecture; it shows the transfer genuinely needs the nondegeneracy that Lemma E
      extracts from the third eigenvalue.

## Piece 4 (about 03:12). Numerics so far; the degenerate end needs a second square in the centre.

NUMERICAL (num/f1_star_twist.py, output f1_star_twist_uniform_output.txt): star + rank one + eps W, n = 60 leaves,
   w random-sign unit, v orthonormal to w, W dense ||W|| = 1, uniform laws, exact conditional estimator (sum over roots),
   2e5-6e5 samples per point. max_s p_Q for a in {0, .02, .1, .3, -.1, -.3}:
     lam=+1 eps=0 beta=0:  3.55 3.59 3.51 3.47 3.62 3.62      lam=+1 eps=.2 beta=0:  2.16 2.18 2.16 2.14 2.18 2.16
     lam=+1 eps=0 beta=.4: 2.05 2.05 2.06 2.06 2.05 2.04      lam=+1 eps=.2 beta=.4: 1.49 1.51 1.50 1.50 1.56 1.51
     lam=-1 eps=0 beta=0:  3.58 3.60 3.59 3.65 3.57 3.44      lam=-1 eps=.2 beta=0:  2.18 2.18 2.19 2.61 2.18 2.15
     lam=-1 eps=0 beta=.4: 2.06 2.07 2.06 2.05 2.05 2.07      lam=-1 eps=.2 beta=.4: 1.51 1.52 1.50 1.50 1.51 1.50
   Flat in a to Monte Carlo accuracy (the single 2.61 is a heavy-tail spike of the estimator; see piece 5 for a
   repeat). Spread laws on every coordinate (f1b) only lower the density (~0.014) and are uninformative.

NUMERICAL (num/f2_aligned_curvature.py): Q = a Xh^2 + 2 Xh t + sigma t^2 + lam V^2 + lam2 U^2, a = 0.2, lam = -1,
   L, V, U independent sums of 30 uniforms (unit norm), sigma = (1 - D_H)/a:
     D_H:            1.000  0.300  0.100  0.030  0.010  0.003
     lam2 = 0:       3.67   4.62   5.35   6.22   6.98   7.93     (two large eigenvalues: grows like log(1/D_H))
     lam2 = +1:      2.69   2.34   2.20   2.13   2.08   2.13     (three large eigenvalues: bounded, decreasing)
     lam2 = -1:      2.32   2.52   2.43   2.34   2.33   2.36     (bounded)
   lam2 = 0 slope: about 1.7 per decade = 0.72 per unit of log(1/D_H); prediction from the D_H = 0 limit
   Q = Z^2/a - V^2 (product pair (Z, V), Lemma 1.4): rho_Z(0) rho_V(0)/sqrt(D) = 1.37*1.38/sqrt 5 = 0.85. Consistent.
   This confirms (E2) quantitatively and shows the conjecture's third eigenvalue removes the growth.

What the degenerate end needs (PROVED, by choosing the square-root source): in the lam2 != 0 family apply Theorem 2.3
   with the square-root profile taken from lam2 U^2 (K = |lam2|^{-1/2} rho_U) and centre C = sigma t^2 + lam V^2. Then
   Delta_C = D_H t^2 - a lam V^2 + a s, a quadratic in the independent pair (t, V) with coefficients (D_H, -a lam), and
   E|Delta_C|^{-1/4} <= C (max(D_H, |a lam|))^{-1/4} (condition on t, use the V-square; or condition on V, use t).
   So the bound is uniform in D_H for fixed a. As a -> 0 with D_H -> 0 this route loses |a|^{-1/4}; the right route there
   is the type-1 one from the hub's own square: Q = Z^2/a + kappa, kappa = -(D_H/a) t^2 + lam V^2 + lam2 U^2, and
   (1.5)-type kernel mass in (t, kappa) coordinates: for fixed k, int F(t, k) dt = |a|^{1/2} |s - k|^{-1/2} 1{0 < (s-k)/a < a^{-2}}
   where F is the conditional density contribution; so T <= |a|^{1/2} int sup_t rho_{t,kappa}(t, k) |s - k|^{-1/2} dk, which
   here is <= C |a|^{1/2} (the 2D form lam V^2 + lam2 U^2 has a log-bounded density). The two routes together cover the
   whole family uniformly in (a, D_H). General statement: piece 5.

## Piece 5 (03:27). The sharp centre condition; an unconditional class; bipartite leaves; referee points.

Theorem 2.5 (integrate t first; PROVED). Under (SQ) with centre C = sigma_c t^2 + phi_1 t + phi_0 + C', where the
   conditional density of t = L + beta given C' is <= D (sigma_c, phi_1, phi_0 deterministic, sigma_c != 0),
   write D_H = 1 - a sigma_c. Then N_a(s) <= D E_{X_h, C'} I(X_h, C'), I(x, c') = int_{|a x + tau| < 1} |h(tau)|^{-1/2} dtau,
   h(tau) = s - a x^2 - 2 x tau - sigma_c tau^2 - phi_1 tau - phi_0 - c' (quadratic in tau, leading coeff -sigma_c).
   (I1) curvature: I <= |sigma_c|^{-1/2}(5.66 + 1.42 log_+(|sigma_c|/|h_c|)), h_c = critical value of h in tau
        = s - c' - q_c(x), q_c(x) = -(D_H/sigma_c) x^2 + (lin) + const.
        [m(lam) <= min(2, A/lam, B/lam^2), A = 2 sqrt2 |sigma_c|^{-1/2}, B = 4(|sigma_c||h_c|)^{-1/2}; int = A(2 + log(2B/A^2))
        with 2B/A^2 = sqrt(|sigma_c|/|h_c|); the case |h_c| > |sigma_c| gives <= 5.66|sigma_c|^{-1/2}.]
   (I2) slope: on the slab h' = -2 x D_H - phi_1 +- 2|sigma_c|; if |h'| >= g0 > 0 there, I <= 4 g0^{-1/2}.
   Off E0 = {|2 x D_H + phi_1| <= 4|sigma_c|}: g0 >= 2|sigma_c|, so I <= 2.83 |sigma_c|^{-1/2}. On E0 use (I1) and
   E log_+(1/|h_c|) <= 2 + 2 log_+ alpha_1(h_c), alpha_1(h_c) <= min(alpha_1(C'), alpha_1(q_c(X_h))) (independent sum),
   alpha_1(q_c(X_h)) <= 2 sqrt2 (|sigma_c|/|D_H|)^{1/2} (Lemma 1.2(ii)). Result:
      N_a(s) <= D |sigma_c|^{-1/2} (11.4 + 1.42 log_+|sigma_c| + 1.42 min{2 log_+ alpha_1(C'), log_+(8|sigma_c|/|D_H|)}).
   Combined with Theorem 2.3 (i) (N_a <= 9.05 E|Delta_C|^{-1/4} <= 25.6 D^{1/2} |D_H|^{-1/4}, Cauchy-Schwarz on the two
   linear factors of the quadratic Delta_C in t):
      p_Q <= 1 + K min{ 25.6 D^{1/2} |D_H|^{-1/4},  D |sigma_c|^{-1/2}(11.4 + 1.42 log_+|sigma_c| + 1.42 min{...}) }.
   Genuine hub (|D_H| >= 1/2, Lemma E): first term, a harmless. Degenerate end (sigma_c ~ 1/a, D_H -> 0): second term,
   ~ D |a|^{1/2} (C + 1.42 log(1/|a|) + 1.42 min{2 log alpha_1(C'), log(8/(|a| D_H))}). The random centre only has to
   carry level-1 randomness (alpha_1(C') finite) to kill the degeneracy; without it the growth is log(1/D_H), and that
   is attained (E2).
   NUMERICAL confirmation (num/f4_centre_randomness.py): Q = a Xh^2 + 2 Xh t + sigma t^2 - V^2 + eps Y (Y an extra
   uniform coordinate, alpha_1(eps Y) = sqrt(2/eps)), a = 0.2:
      eps:             0      1e-3   1e-2   1e-1   1
      D_H = 0.1:      5.29   5.05   4.37   2.52   0.82
      D_H = 0.003:    8.06   6.23   4.32   2.41   0.81
   The curves merge once eps exceeds the D_H scale: max density ~ const + c min(log(1/D_H), log(1/eps)), as predicted.

Theorem U (unconditional class: transverse square on its own coordinates; PROVED). Leaves split into disjoint S, T;
   V = <v, X_S>, L = <w, X_T>; Q = a X_h^2 + 2 X_h (L + beta) + lam (V - D)^2 + C with D any function of X_T and C any
   quadratic polynomial in X_T (matrix M_C; ANY dense twist on the hub's leaves allowed). Then, conditioning on
   (X_T, X_h) (lossless) and using the square in V (density of V <= sqrt2/|v|):
      p_Q(s) <= (sqrt2/|v|) |lam|^{-1/2} E|s - a X_h^2 - 2 X_h t - C|^{-1/2} <= 9.05 (sqrt2/|v|)|lam|^{-1/2} E|Delta_C|^{-1/4}
      <= 25.6 |lam|^{-1/2} |v|^{-1} alpha_1(Delta_C)^{1/2},   Delta_C = (L + beta)^2 + a (s - C)  (matrix w w^T - a M_C).
   (a) a = 0: directly E|s - 2 X_h t - C|^{-1/2} <= E 2|t|^{-1/2} <= 6.73 |w|^{-1/2}, so ||p_Q|| <= 9.5 |lam|^{-1/2}|v|^{-1}|w|^{-1/2}
       for EVERY quadratic C on T: the zero-diagonal hub + rank one + dense twist, when the twist avoids supp(v).
   (b) a != 0: level 1 of Delta_C is all that is needed. By Theorem D with k = 1, q = 1 (FOURIER report 1.2:
       |phi| <= e^{1/4} sqrt(2 pi) Z_1^{-1/4} |t|^{-1/2} when row marginals <= 1/2) and the referee's Esseen constant
       (alpha_1 <= 4.36 B): if |w| = 1, max|w_i| <= 1/16 and |a| ||M_C|| <= 1/16, a balanced split I, J of T gives
       ||N_IJ||_F >= |w_I||w_J| - |a| ||M_C|| >= 0.437, row norms <= 0.107, marginals <= 0.06, alpha_1(Delta_C) <= 14.0 Z_1^{-1/4}
       <= 21.2, hence ||p_Q|| <= 118 |lam|^{-1/2}/|v|, uniformly in a, beta, s and the linear terms on T.
   SCOPE (same as the referee's flag on Prop 5.4): linear terms on S must be along v (a term <b_perp, X_S> with b_perp
   orthogonal to v breaks the independence of V from the centre). The twist touching supp(v) is not covered.

Proposition B (bipartite leaves; PROVED). If a leaf set G carries no quadratic terms of R (M_GG = 0), condition on
   X_c (c = the other leaves) and then on X_h = x: Q is linear in X_G with coefficient 2 x w_G + eta, eta = 2 M_{Gc} X_c + b_G,
   density <= sqrt2/|2 x w_G + eta| (Ball). Bathtub in x: p_Q <= (sqrt2/|w_G|) E arcsinh(|w_G|/|eta_perp|), eta_perp = the part of
   eta orthogonal to w_G. With e a unit vector of R^G orthogonal to w_G, <e, eta> is a linear form in X_c with coefficient
   2 M_{cG} e, so E log_+(1/|eta_perp|) <= 1 + log_+(sqrt2/|M_{cG} e|). Hence
      ||p_Q|| <= (sqrt2/|w_G|)(1 + log(1 + 2|w_G|) + log_+(sqrt2/sigma_G)),  sigma_G = max_{e perp w_G} |M_{cG} e|,
   for EVERY a, beta, every M_cc, every w_c. (The density-level version of the referee's alpha_2 replacement for GEOM's
   remark: the leaves may be coupled to the rest, and the coupling transverse to w_G supplies the third direction.)

Referee points. (1) Nothing here uses the pointwise Rudelson-Vershynin bound; the only characteristic-function inputs are
   the triangle inequality (Prop F) and Theorem D's k = 1 case (L^p lemma + Brascamp-Lieb). (2) GEOM's sqrt(|a| u) remark:
   agreed with finding 3; in the present language the square-root term appears exactly when the centre curve is aligned
   with Gamma_s (C ~ s + t^2/a), e.g. A = (1/a)(a, w)(a, w)^T, and example (E2) quantifies the log version.

## Piece 6 (03:45). Last numerics.

NUMERICAL (num/f5_theoremU.py): leaves S (30, carry V) and T (30, carry L and the twist), uniform laws.
   twist on T only (Theorem U applies):   lam=+1: eps .3: 2.13 2.14 2.14 (a = 0, .05, -.05); eps 1: 1.08 1.07 1.06
                                          lam=-1: eps .3: 2.13 2.13 2.14;                      eps 1: 1.06 1.07 1.07
   twist on all leaves (not covered):     lam=+1: eps .3: 1.83 1.85 1.82;                      eps 1: 0.79 0.76 0.80
                                          lam=-1: eps .3: 1.85 1.87 1.83;                      eps 1: 0.80 0.80 0.79
   Flat in a; far below the proven 9.5 (a = 0) and 118 (a != 0).
NUMERICAL (num/f6_bound_vs_truth.py): model with (SQ) exact (V on own coordinates), C = sigma_c t^2 + mu U:
   (a, sigma_c, D_H, lam, mu) = (.1, 0, 1, -1, 0): true 3.63, Thm 3.3 bound 41.3
                                (.1, 3, .7, -1, 0): true 3.93, Thm 3.3 45.1, Thm 3.4 21.3
                                (.2, 4.95, .01, -1, 0): true 7.07, Thm 3.3 128.8, Thm 3.4 23.4
                                (.2, 4.95, .01, -1, .3): true 1.70, Thm 3.3 43.8, Thm 3.4 17.1
                                (-.3, 1, 1.3, 1, .5): true 1.71, Thm 3.3 29.2, Thm 3.4 28.4
   All bounds valid; crude by factors 5-20; Thm 3.4 tracks the degenerate end much better than Thm 3.3.
NUMERICAL (num/k2_curvature_kernel.py): the curvature bound (I1) of Theorem 2.5, exact level-set measure, 600 random
   (sigma, h_c): worst ratio 0.76.
Also (num/f3_adversarial.py): curvature mu along w with the dense twist, D_H from 0.4 to 1.6: max density 3.00-3.56
   (eps = 0) and 2.00-2.18 (eps = .2), mild dependence on D_H; spread hub law with the slab placed on the hub mass:
   densities 0.03-0.09, decreasing in a.
REPORT.md: the environment refuses the file ("return findings as text"); the full report goes into the final message.

## Piece 7 (03:55). REPORT DRAFT, part 1 of 3 (the final message carries the same text)

# One hub with a small nonzero diagonal and a general remainder

Setting. X_h and X' = (X_i)_{i != h} are independent, every coordinate has a density bounded by 1, f_h is the density of
X_h, and
    Q = a X_h^2 + 2 X_h t + R(X'),   t = L + beta,   L = <w, X'>,   R(X') = X'^T M X' + b^T X' + const,
with full matrix A = [[a, w^T], [w, M]]. Standard inputs: a linear form <theta, X> has density <= sqrt 2/|theta| (Ball);
k-dimensional marginals have density <= 2^{k/2} (Livshyts-Paouris-Pivovarov); Lemmas 1.2(ii), 1.3, 1.4, 1.6 of the
geometric report (one-dimensional quadratics, definite and hyperbolic two-dimensional forms, layer cake). No pointwise
bound on characteristic functions is used. alpha_1(Z) = sup_{s,u} P(|Z - s| <= u)/sqrt(u).

Answer in one paragraph. The needed property of R, jointly with L, is a square-root profile of R around a random centre
C, uniformly along L (hypothesis SQ of Section 3), together with a negative quarter moment of the single quadratic
Delta_C = (L + beta)^2 - a (C - s). At a = 0 the second condition is automatic. For a != 0 it can fail only if the centre
is aligned with the parabola C = s + t^2/a. That happens only when the hub block of A is nearly of rank one. There the
hub's own square Z^2/a (Z = a X_h + t) takes over with constant |a|^{1/2}, and any level-1 randomness of the independent
part of the centre removes the remaining logarithm. No hypothesis on the marginal law of R suffices, even at a = 0.

## 1. Exact identities

1.1. Given X', Q = g(X_h), g(x) = a x^2 + 2xt + R. With u = ax + t, a x^2 + 2xt = (u^2 - t^2)/a; the roots of g = s are
u = +-sqrt(Delta), Delta = t^2 + a(s - R), x_pm = (u_pm - t)/a, and |g'(x_pm)| = 2|u_pm|. Hence
    p_Q(s) = E[ sum_pm f_h(x_pm) / (2 sqrt Delta) ; Delta > 0 ].
Delta = a(s - kappa), kappa = R - t^2/a (the random centre of the square-root singularity); Delta is a quadratic in X' with
matrix w w^T - a M. Given X_h = x instead, Q = a x^2 + Y_x, Y_x = R + 2xt, and p_Q(s) = int f_h(x) p_{Y_x}(s - a x^2) dx.
Because Y_x + a x^2 = R + 2x(L + beta + ax/2), a nonzero diagonal is a zero diagonal with the x-dependent offset
beta + ax/2: zero-diagonal bounds that are uniform in the offset inside the x-integral transfer at once.

1.2. Roots with |ax + t| >= 1 contribute at most 1. So p_Q <= 1 + T(s),
    T(s) = int K_s(t, r) dmu_{t,R},   K_s(t, r) = sum_{x: a x^2 + 2xt + r = s, |ax + t| < 1} f_h(x)/(2|ax + t|).

1.3 (tangent lines). The map (u, x) -> (t, r) = (u - ax, s + a x^2 - 2xu) has Jacobian determinant -2u, every image point
has x as a root with ax + t = u, and so, when (t, R) has a density rho,
    T(s) = int f_h(x) [ int_{-1}^{1} rho(u - ax, s + a x^2 - 2xu) du ] dx.
The segment for fixed x passes through (-ax, s + a x^2), a point of Gamma_s = {r = s + t^2/a}, with slope -2x = 2t/a: it is
TANGENT to Gamma_s. The full line {r = s - a x^2 - 2xt} carries the X-ray p_{Y_x}(s - a x^2). At a = 0 these lines form the
pencil through (0, s); for a != 0 they form the tangent family of Gamma_s. In coordinates (t, kappa), kappa = r - t^2/a,
the tangent lines become the translates kappa = s - (t + ax)^2/a of one parabola.

Lemma 1.4 (kernel masses). For 0 <= f_h <= 1, int f_h = 1:
 (i) int int K_s dt dr = 2;
 (ii) for fixed t and phi >= 0, int K_s(t, r) phi(r) dr = int f_h(x) 1{|ax + t| < 1} phi(s - a x^2 - 2xt) dx;
 (iii) for fixed r, sigma = s - r: int K_s(t, r) dt = int f_h(x) 1{|a x^2 + sigma| < 2|x|} dx/(2|x|)
       <= log(1 + (1 + sqrt(1 + |a sigma|))/(2|sigma|)) <= log 2.5 + log_+(1/|sigma|)   (|a| <= 1).
Proof. (i) from 1.3. (ii): at fixed t substitute r = s - a x^2 - 2xt, |dr/dx| = 2|ax + t|. (iii): at fixed r,
t = (sigma - a x^2)/(2x), |dt/dx| = |sigma + a x^2|/(2x^2) and ax + t = (a x^2 + sigma)/(2x), so weight times Jacobian is
f_h(x)/(2|x|); the support lies in |x| > x_* = |sigma|/(1 + sqrt(1 + |a sigma|)); the bathtub principle (f_h = 1 on
x_* < |x| < x_* + 1/2) gives log(1 + 1/(2x_*)). The last inequality uses (1 + sqrt(1 + |a sigma|))/(2|sigma|)
<= 1/|sigma| + sqrt|a|/(2 sqrt|sigma|). []
The bound (iii) is attained (numerically, ratio 1.00): the logarithmic profile of the hub does not depend on a.

## 2. Regularity routes, uniform in a

Proposition 2.1. If (L, R) has a bounded joint density, p_Q <= 1 + 2 ||rho_{L,R}||_inf for all a, beta. (Lemma 1.4(i).)

Proposition 2.2. If the conditional density of L given R is at most kappa_0, then for |a| <= 1
    p_Q(s) <= 1 + kappa_0 E[log 2.5 + log_+ 1/|s - R|] <= 1 + kappa_0 (log 2.5 + 2 + 2 log_+ alpha_1(R)).
Proof. Integrate K_s in t at fixed r (Lemma 1.4(iii)) and use Lemma 1.6. [] The hub then has a type-2 profile around the
centre R, with a constant that does not depend on a.

Neither hypothesis holds in the configuration of Prop. 5.4 (R = lambda (V - v_c(L))^2 + F_c(L)), where the joint density
has a square-root singularity along r = F_c(l).

## Piece 8 (04:05). REPORT DRAFT, part 2 of 3

## 3. Square-root profiles and the random centre

(SQ) There are K > 0 and a random variable C, defined jointly with L, such that for every measurable phi >= 0
    E phi(L, R) <= K E[ int phi(L, r) |r - C|^{-1/2} dr ].
Typical source: R = lambda (V - D)^2 + C with V having conditional density <= kappa_V given (L, D, C); then
K = kappa_V |lambda|^{-1/2} (two roots v, |dR/dv| = 2 sqrt(|lambda||r - C|)). Lebesgue variant (SQ_leb):
rho_{L,R | Xi}(l, r) <= K' |r - C(l, Xi)|^{-1/2} with Xi independent of L; source: (L, V) with joint density <= K_2,
R = lambda (V - D(L, Xi))^2 + C(L, Xi), K' = K_2 |lambda|^{-1/2}.

Lemma 3.1 (reduction to the centre). Under (SQ), T(s) <= K N_a(s),
    N_a(s) = E[ 1{|a X_h + t| < 1} |s - a X_h^2 - 2 X_h t - C|^{-1/2} ]   (X_h independent of (L, C)).
Proof. Apply (SQ) to phi(l, r) = K_s(l + beta, r) and Lemma 1.4(ii) with phi = |. - C|^{-1/2}. []
So a level-3 question for Q becomes a level-2 question: the negative half-moment of the hub with remainder C.

Lemma 3.2 (one-dimensional kernel). For fixed t, sigma, with Delta = t^2 + a sigma,
    J_a(t, sigma) := sup_{0 <= f <= 1, int f = 1} int f(x) |sigma - a x^2 - 2xt|^{-1/2} dx <= 9.05 |Delta|^{-1/4},
and J_0(t, sigma) <= 2|t|^{-1/2}.
Proof. phi(x) = sigma - a x^2 - 2xt = -a(x + t/a)^2 + Delta/a. By Lemma 1.2(ii) (Lebesgue measure),
|{|phi| < eps}| <= m(eps) := min(2 sqrt(2 eps/|a|), 4 eps / sqrt(max(|Delta|, |a| eps))). The bathtub principle gives
J_a <= int_0^inf min(1, m(lam^{-2})) dlam. If |Delta| >= a^2/16, then for lam >= lam_1 = 2|Delta|^{-1/4} one has
|a| lam^{-2} <= |Delta|, so J_a <= lam_1 + int_{lam_1}^inf 4 lam^{-2} |Delta|^{-1/2} dlam = 4 |Delta|^{-1/4}. If |Delta| < a^2/16, split
at lam_2 = 2 sqrt2/sqrt|a| and lam_0 = sqrt(|a|/|Delta|) > lam_2: J_a <= |a|^{-1/2}(4 + 2 sqrt 2 + sqrt 2 log(a^2/(8|Delta|))).
Since log y <= (4/e) y^{1/4} for y >= 1, the second case is <= (8 + 1.04)|Delta|^{-1/4}. At a = 0, 2 X_h t has density
<= 1/(2|t|), and sup_c E|c - Z|^{-1/2} <= 2 sqrt2 D^{1/2} for a density <= D. []
Numerically (exact level-set measure, 3000 random (a, Delta)): worst ratio to 9.05|Delta|^{-1/4} is 0.32. The
supremum can exceed J_0 by a factor sqrt 2 as a -> 0: the second root x = -2t/a is a second tangent point.

Theorem 3.3 (composition under SQ). Under (SQ),
    p_Q(s) <= 1 + 9.05 K E|Delta_C|^{-1/4},   Delta_C = (L + beta)^2 + a (s - C).
In particular, if C = sigma_c t^2 + phi_1 t + phi_0 + C' with constants sigma_c, phi_1, phi_0 and the conditional density of
t given C' at most D, then with D_H = 1 - a sigma_c
    p_Q <= 1 + 25.6 K D^{1/2} |D_H|^{-1/4}.
Proof. Lemma 3.1 and Lemma 3.2 give the first line. Given C', Delta_C is a quadratic in t with leading coefficient D_H;
if it is (t - m)^2 + k up to that factor with k >= 0, bound by |t - m|^{-1/2}; if k = -r^2 < 0, factor it and use
Cauchy-Schwarz: E|t - m - r|^{-1/4}|t - m + r|^{-1/4} <= sup_c E|t - c|^{-1/2} <= 2 sqrt2 D^{1/2}. []
At a = 0 the right side is 1 + 9.05 K E|t|^{-1/2}, finite for every centre C whatsoever. For a != 0 the only obstruction is
concentration of (t, C) near C = s + t^2/a.

Theorem 3.4 (integrating t first; the degenerate end). Under the hypotheses of the second part of Theorem 3.3,
    p_Q(s) <= 1 + K D |sigma_c|^{-1/2} (11.4 + 1.42 log_+|sigma_c| + 1.42 min{ 2 log_+ alpha_1(C'), log_+(8|sigma_c|/|D_H|) }).
Proof. By Lemma 3.1, N_a <= D E_{X_h, C'} I(X_h, C') with I(x, c') = int_{|ax + tau| < 1} |h(tau)|^{-1/2} dtau and
h(tau) = s - a x^2 - 2x tau - sigma_c tau^2 - phi_1 tau - phi_0 - c' (condition on (X_h, C'); t has density <= D and is
independent of X_h). h is quadratic with leading coefficient -sigma_c and critical value h_c = s - c' - q_c(x),
q_c(x) = (a - 1/sigma_c) x^2 - (phi_1/sigma_c) x + phi_0 - phi_1^2/(4 sigma_c), whose leading coefficient is -D_H/sigma_c.
(I1) With m(lam) <= min(2, A/lam, B/lam^2), A = 2 sqrt2 |sigma_c|^{-1/2}, B = 4 (|sigma_c||h_c|)^{-1/2} (Lemma 1.2(ii)):
     I <= A (2 + log(2B/A^2)) = |sigma_c|^{-1/2} (5.66 + 1.42 log(|sigma_c|/|h_c|)) when |h_c| <= |sigma_c|, and
     I <= 2 sqrt(2B) <= 5.66 |sigma_c|^{-1/2} otherwise.
(I2) On the slab h' = -(2x D_H + phi_1) + O(2|sigma_c|); if |h'| >= g0 > 0 there then I <= 4 g0^{-1/2}. Off
     E0 = {x : |2x D_H + phi_1| <= 4|sigma_c|} one has g0 >= 2|sigma_c|, so I <= 2.83 |sigma_c|^{-1/2}.
Hence E I <= |sigma_c|^{-1/2}(2.83 + 5.66 + 1.42 E log_+(|sigma_c|/|h_c|)). Finally
E log_+ 1/|h_c| <= 2 + 2 log_+ alpha_1(h_c) (Lemma 1.6), alpha_1 of the independent sum C' + q_c(X_h) is at most the
smaller of alpha_1(C') and alpha_1(q_c(X_h)) <= 2 sqrt2 (|sigma_c|/|D_H|)^{1/2} (Lemma 1.2(ii)). []
(I1) was checked numerically with the exact level-set measure (600 random (sigma_c, h_c)): worst ratio 0.76.

Reading of 3.3-3.4. Genuine hub (|D_H| >= 1/2, see 4.1): p_Q <= 1 + 36.2 K D^{1/2}; the diagonal is harmless. Degenerate
end (sigma_c ~ 1/a, D_H -> 0): p_Q <= 1 + K D |a|^{1/2}(C + 1.42 log(1/|a|) + 1.42 min{2 log alpha_1(C'), log(8/(|a| D_H))}):
the small factor |a|^{1/2} comes from the hub's own square Z^2/a, and the only thing needed of the random centre is
level-1 randomness of its independent part C'. Without it the growth is log(1/D_H), and Example 4.3 shows this is
attained.

Corollary 3.5 (Prop. 5.4 with an arbitrary coupling to further coordinates). Let (L, V) be linear forms in the coordinates
P = supp(w) u supp(v) with joint density <= K_2, Xi = X_{P^c}, and let R be any quadratic polynomial in (L, V, Xi) whose
V^2-coefficient lambda is nonzero. Completing the square in V, R = lambda (V - D(L, Xi))^2 + sigma_c L^2 + c_1(Xi) L + c_0(Xi)
with sigma_c deterministic. Given Xi this is the configuration of Prop. 5.4 with modified affine parts, and Prop. 5.4 is
uniform in them; so its bound holds with D_H = |1 - a sigma_c|. The t-first argument of Theorem 3.4 (Lebesgue variant,
D replaced by 1, K by K_2 |lambda|^{-1/2}) gives in addition
    T <= K_2 |lambda|^{-1/2} |sigma_c|^{-1/2} (11.4 + 1.42 log_+|sigma_c| + 1.42 min{2 sup_x log_+ alpha_1(S_x), log_+(8|sigma_c|/|D_H|)}),
where S_x(Xi) = c_0(Xi) - (x + c_1(Xi)/2)^2/sigma_c is the value at Xi of the minimum over (L, V) of R + 2xL: the Schur
complement form in the coordinates Xi. So in the degenerate regime the bound is uniform in D_H as soon as the Schur
complement form has a level-1 small-ball bound, which is the level-1 statement of the reduction theorem applied to a
quadratic form in independent coordinates. (Scope: linear terms of R on the coordinates of P must lie in span(w, v).)

## Piece 9 (03:55). REPORT DRAFT, part 3a

## 4. The hub block, and why the hypotheses must be joint

Lemma 4.1 (dichotomy). B = [[a, W], [W, m]], W >= 1, |a| < c <= 1/8, sigma = m/W^2. If both eigenvalues of B have modulus
>= 1 then |sigma| < 4 and D_H = |1 - a sigma| >= 1 - 4c >= 1/2. If D_H <= 1/2 then |sigma| >= 1/(2|a|) and the smaller
eigenvalue has modulus <= 2|a| W^2/(W^2 - 2a^2): B is a rank-one piece (a, w)(a, w)^T/a up to O(a), a delocalized square
with eigenvalue about W^2/a rather than a hub.
Proof: if |sigma| >= 4 then |mu_1 + mu_2| >= |sigma| W^2 - c and |mu_1 mu_2| <= W^2 (1 + c|sigma|); the smaller eigenvalue
has modulus <= 2(1 + c|sigma|)/(|sigma| - c), decreasing in |sigma|, equal to 0.77 at |sigma| = 4.

Example 4.2 (marginal hypotheses never suffice, even at a = 0). Y a further coordinate independent of (X_h, L),
R = 2 Y L + c: R is itself a hub (bounded alpha_1 and level-2 quantity), L is spread, yet at a = 0, beta = 0,
Q = 2 (X_h + Y) L + c is a product of two independent variables with densities positive at 0: unbounded density.
A has only the eigenvalues +-sqrt2 W besides 0 (parallel hub rows).

Example 4.3 (no transfer without D_H; the logarithm is sharp). V independent of (X_h, L), lambda a0 < 0,
R = t^2/a0 + lambda V^2. At a = 0, averaging over V first gives p_Q <= C |lambda|^{-1/2} E|t|^{-1/2}. At a = a0,
Q = Z^2/a0 + lambda V^2, Z = a0 X_h + t: hyperbolic in the independent pair (Z, V), density ~ rho_Z(0) rho_V(0)
(|a0|/|lambda|)^{1/2} log(1/|s|). For a near a0 the log is cut at the scale of D_H = |1 - a/a0|. A has two large eigenvalues
only. Numerics (a = .2, lambda = -1; sums of 30 uniforms), max_s p_Q for sigma t^2 + lambda V^2 + lambda2 U^2:
   D_H 1, .3, .1, .03, .01, .003:  lambda2 = 0: 3.67 4.62 5.35 6.22 6.98 7.93;  lambda2 = +1: 2.69 2.34 2.20 2.13 2.08 2.13;
   lambda2 = -1: 2.32 2.52 2.43 2.34 2.33 2.36.  Slope 0.72 per unit log(1/D_H) (predicted 0.85).
   With eps Y added (lambda2 = 0), eps = 0, 1e-3, 1e-2, 1e-1, 1: D_H = .1: 5.29 5.05 4.37 2.52 0.82;
   D_H = .003: 8.06 6.23 4.32 2.41 0.81.

## 5. Unconditional class (Theorem 5.1) - statement and proof as in piece 5 (Theorem U), constants 9.51 (a = 0),
   25.6 |lambda|^{-1/2}|v|^{-1} alpha_1(Delta_C)^{1/2} (all a), 118 |lambda|^{-1/2}|v|^{-1} under |w| = 1, max|w_i| <= 1/16,
   |a| ||M_C|| <= 1/16. Row norms of N_IJ <= 1/16 + 1/16 = 0.125, marginals <= 0.125^2/0.191 = 0.082.

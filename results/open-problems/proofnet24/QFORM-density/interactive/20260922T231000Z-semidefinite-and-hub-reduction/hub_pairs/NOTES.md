# NOTES - several hubs with a nonzero hub block

## 0. Setting and notation (fixed for the whole folder)

H = hub set, k = |H| >= 2, X' = X_{H^c}. A_{H,H^c} =: A (k x m), singular values s_1 >= ... >= s_k >= sigma.
B := A_HH (k x k symmetric, small). Linear term beta_H on the hubs, R(X') the whole remainder (quadratic + linear + const).

   Q = X_H^T B X_H + 2 X_H^T (A X' + beta_H) + R(X').

Put L = A X' + beta_H (k-dim), c = 2L, r = R(X'). Given X': Q = q_c(X_H) + r, q_c(x) = x^T B x + c^T x.
Density facts: L has density <= 2^{k/2}/prod s_j  (k-dim projections of a product measure have density <= 2^{k/2};
then the linear map U Sigma). So c has density <= K := 2^{k/2}/(2^k prod s_j).

If B invertible: q_c(x) = (x - x0)^T B (x - x0) + kappa(c), x0 = -B^{-1}c/2 = -B^{-1}L, kappa = -c^T B^{-1} c/4 = -L^T B^{-1} L.
So Q = Y^T B Y + xi, where Y = X_H + Z, Z = B^{-1} L, and
   xi = R(X') - L^T B^{-1} L      (the "Schur centre": a quadratic in X' whose matrix is the Schur complement A/B on H^c).
Z has density <= |det B| 2^{k/2}/prod s_j.  Given X', Y has independent coordinates with densities <= 1 (translates of X_H).

## 1. The key structural observation: the obstruction is sup over the level INSIDE the expectation

p_Q(s) = E_{X'} [ p_{q_c}(s - r) ]. Because r is an arbitrary function of X' correlated with c, the only general bound is
   p_Q(s) <= E_c [ sup_t p_{q_c}(t) ].
For A_HH = 0 (GEOM Prop 5.5) sup_t p_{q_c}(t) <= 1/|c|_inf, integrable in dim >= 2.  For B != 0 the conditional density has
critical behaviour at the critical point x0(c):
 - B indefinite (k = 2): p_{q_c}(t) has a LOG singularity at t = kappa(c) whenever f is positive near x0 -> sup_t = infinity.
 - B definite (k = 2): a step of height pi/sqrt(det B) * f(x0) at t = kappa (bounded, but large).
The adversary is R = L^T B^{-1} L + (anything), which makes xi independent of... in the extreme xi = const.

## 2. FALSE: two hubs with an indefinite hub block need not give a bounded density (counterexample)

Take k = 2, B = diag(b, -b), b > 0, and R(X') = L^T B^{-1} L = (L_1^2 - L_2^2)/b. Then xi = 0 and
   Q = b (X_{h1} + L_1/b)^2 - b (X_{h2} - L_2/b)^2 = b (U^2 - V^2),  U = X_{h1} + Z_1, V = X_{h2} + Z_2, Z = (L_1/b, -L_2/b).
(U,V) has the continuous density rho_UV = (f_1 x f_2) * law(-Z)... (convolution of an L^1 function with a bounded density),
and rho_UV(0) > 0 for suitable data. Then P(|Q| <= eps) >= c0 (eps/b) log(b/eps) -> the density of Q is infinite at 0.
Full matrix: M = b u u^T - b v v^T with u = e_{h1} + A_1^T / b, v = e_{h2} - A_2^T / b: RANK TWO, eigenvalues about
+-(b + |A_i|^2/b). Entries: hub block +-b, hub rows = rows of A (small), remainder entries (A_1i A_1j - A_2i A_2j)/b,
small when the rows are spread (entries ~ sigma/sqrt m) and m >> sigma^2/(b c). So it is a no-pivot matrix with
exactly two large eigenvalues and an unbounded density. It does not contradict the conjecture (needs three), but it
shows: Prop 5.5 does NOT extend to A_HH != 0 in the form "bounded density whatever the remainder".
Note the log coefficient: rho_UV(0) <= ||rho_Z||_inf <= 2 b^2/(s1 s2), so p_Q(s) ~ (2b/(s1 s2)) log(b/|s|): SMALL weight.
So the natural statement for a pair with indefinite block is a log profile with small weight around the centre xi.

## 3. Where a bounded density can still be expected

 - k = 2, det B >= 0 (semidefinite hub block).  Checked by hand for the adversary R = L^T B^{-1} L (perfect square):
   B = bI gives p <= 2 pi b/(s1 s2) (average over Z first: rho_Y <= ||rho_Z||).  Rank one B = b e1 e1^T:
   sup_t p_{q_c}(t) <= inf_M [ 1/M + m_{M/b}(x1*)/|c2| ],  x1* = -c1/(2b), m_w(x) = f1-mass of [x-w, x+w];
   E over c1 of m_{M/b}(x1*) is <= (density of c) * 4M (the critical line moves at speed 1/(2b) in c1): bounded, uniformly in b.
 - k = 2, det B < 0, and the full matrix has >= 3 eigenvalues of modulus >= 1: then A/B keeps >= 1 large eigenvalue
   (Lemma 1.5) and the centre xi has a power small-ball law; a log profile with small weight composes to a bounded density.
 - k >= 3: expected bounded whatever the remainder (the saddle of a nondegenerate 3-variable quadratic is not singular).

## 4. The technical core (status: being worked out)

Everything reduces to bounding E_c[ sup_t (local conic integral near x0(c)) ], a maximal-function-type quantity.
Fixed-level versions are easy: E_c[ p_{q_c}(s) ] at a FIXED s is <= int f(x) rho_{c.x}(s - x^T B x) dx
<= (sqrt2/(2 sigma)) int f(x)/|x| dx <= sqrt(2 pi)/sigma  (bathtub in R^2).  So R = 0 (or R independent of c) is easy.
The difficulty is exactly the correlation between r and c.

## 5. Theorem A (PROVED, draft proof): private leaves, ANY hub block, any k >= 2

Split coordinates H u J u K, |H| = k >= 2. Suppose the matrix of Q vanishes on J x J and on J x K (the leaves J are
coupled only to the hubs; linear terms on J arbitrary). Everything on H u K is arbitrary (hub block, hub diagonals,
hub-K couplings, anything on K). If s_k(A_{HJ}) >= sigma then
    ||p_Q||_inf <= C_k / sigma,   C_k = (sqrt2/2) * int_{|x| <= r_k} dx/|x|,  V_k r_k^k = 1;
    C_2 = sqrt(2 pi) = 2.5066,  C_3 = (sqrt2/2) * 2 pi (3/(4 pi))^{2/3} = 1.7096.
Proof. Condition on X_K. Then Q = <v(X_H), X_J> + g(X_H), v(x) = 2 A_{HJ}^T x + b_J, g arbitrary.
Condition further on X_H = x: <v, X_J> has density <= sqrt2/|v| (Ball, 1D marginals of products with densities <= 1).
Fubini: p_Q(s) <= int f_H(x) sqrt2/|v(x)| dx. Let P = projection onto range(A_{HJ}^T); |v(x)| >= |P v(x)| =
|2 A_{HJ}^T (x - x_b)| >= 2 sigma |x - x_b| for x_b = -(A A^T)^{-1} A b_J / 2 (A = A_{HJ}). Bathtub (weight radially
decreasing about x_b, f_H <= 1, int f_H = 1): int f_H(x)/|x - x_b| dx <= int_{|x| <= r_k} dx/|x|. QED.
No smallness, no leverage condition, no eigenvalue condition. Fails for k = 1 (int dx/|x| diverges in 1D) - the single
hub is genuinely different.
Relation to RESULTS Theorem H (r = 0): H allows A_II DIAGONAL on the leaves and leaf-to-rest couplings A_IJ arbitrary,
but needs normalised leverages <= 1/2; Theorem A needs pure leaves but no leverage condition, constant explicit and small.
The counterexample of Section 2 is exactly Theorem H with r = 2 and a DEGENERATE frame: the remainder's rank-two part
L^T B^{-1} L lives in the span of the hub rows, so G~ (4 x 4) has rank 2 and det G~ = 0.

## 6. Theorem B (PROVED, draft): two hubs, one hub diagonal nonzero, zero hub-hub coupling, ANY remainder

B = diag(a, 0) (a != 0 arbitrary), rows of A with s_2(A) >= sigma, R arbitrary. Then
    ||p_Q||_inf <= 1 + 4/(s1 s2) + 4 sqrt2 / s2   (to be re-optimised).
Proof. Given X': q = a x1^2 + c1 x1 + c2 x2. Graph over x1: p(t) = (1/|c2|) int f1(x1) f2((t - g(x1))/c2) dx1,
g(x1) = a x1^2 + c1 x1, g'(x1) = 2a (x1 - x1*), x1* = -c1/(2a). For omega > 0, off the window |x1 - x1*| <= omega
substitute x2 = (t - g(x1))/c2 on each of the two monotone branches: dx1 = |c2| dx2/|g'| <= |c2| dx2/(2|a| omega).
So  sup_t p(t) <= 1/(|a| omega) + m1(x1*, omega)/|c2|,   m1(x, w) = int_{|y - x| <= w} f1.   (also <= 1/|c2|)
Put lambda = 2|a| omega (gradient scale): sup_t p <= 2/lambda + m1(x1*, lambda/(2|a|))/|c2|.
The critical line x1 = x1* moves with speed 1/(2|a|) in c1:  int m1(-c1/(2a), lambda/(2|a|)) dc1 = 2 lambda * int f1 = 2 lambda.
With lambda = |c2|^{1/2} on |c2| <= 1 and the trivial bound on |c2| > 1:
  E sup_t p <= P(|c2|>1) + K int_{|c2|<=1} 2|c2|^{-1/2} dc2 + E[2|c2|^{-1/2}; |c2| <= 1]
            <= 1 + 8 K + 8 K_2,   K = density of c <= 1/(2 s1 s2),  K_2 = density of c2 <= 1/(sqrt2 s2).
Uniform in a. Same proof for k >= 3 hubs with B = diag(a, 0, ..., 0) (replace c2 by the (k-1)-vector c_{>=2}).
Why it works: the critical set is a coordinate line x1 = x1*(c1), so the window is independent of the level t and its
f1-mass is LINEAR in f1; averaging over c1 costs nothing. For a rotated rank-one block (critical line not a coordinate
line) or a definite block (critical point), the window moves with t and a maximal function appears (Section 7).

## 7. The obstruction for general B: a maximal function (status: not proved; precise statement)

For det B > 0, sup_t p_{q_c}(t) = sup_delta (1/(2 sqrt D)) int_theta f(x0 + y_delta(theta)) d theta  (ellipse means
around the moving centre x0 = -B^{-1} c/2, density of x0 <= 4 D K). A bound E_c sup_t p <= C(K) uniformly in B would
follow from a weak-L^2 inequality |{x0 : M_B f(x0) > h}| <= C/(D h^2) for the elliptic maximal function of PRODUCT
densities f = f1 x f2 (f_i <= 1, int f_i = 1). Heuristics and the grid examples satisfy it with constant ~pi; every
one-coordinate reduction I tried (graph pieces + 1D Hardy-Littlewood) loses exactly a factor log(1/D): the 1D maximal
function averaged against a density of height ~|b| gives |b| log(1/|b|). Circular maximal functions are not bounded on
L^2 for general functions (Bourgain's theorem needs p > 2), so the product structure must be used in two dimensions.

## 8. NUMERICAL (n1_counterexample.py, n1_output.txt): the counterexample is real

Exact conditional sublevel estimator (given X' and X_{h1}, the event is a union of <= 2 intervals in X_{h2}),
m = 80 leaves, orthonormal spread hub rows (sigma = 1, max entry 0.31), uniform laws, R = L^T B^{-1} L, N = 1.2M samples.
Prediction: P(|Q| <= eps)/(2 eps) ~ (rho_Y(0)/sqrt|det B|) log(1/eps) + O(1).
  B = diag(0.2,-0.2):   1.20, 2.02, 2.86, 3.69, 4.50, 5.31, 6.18 at eps = 1e-1..1e-7; fitted slope 0.359, predicted 0.362.
  B = [[0,.2],[.2,0]] (zero hub diagonals, hub-hub coupling only): same growth, 2.03 -> 2.83 -> 3.63 (eps 1e-2..1e-4);
      estimator noisy below 1e-4 (linear in X_{h2} with slope c2 + 2e X1 near 0).
  B = diag(0.05,-0.05): slope 0.089, predicted 0.092: the weight of the log is small, ~ b, as predicted.
  CONTROL B = 0.2 I (same Schur-matching remainder): flat at 0.565 = (pi/b) rho_Y(0)/2 (the step at the minimum, halved
      by the symmetric window).  Bounded, as predicted.
So even an arbitrarily small hub-hub coupling (zero hub diagonals) destroys the conclusion of Prop 5.5: the correct
dichotomy for |H| = 2 "whatever the remainder" is the sign of det A_HH.

## 9. NUMERICAL (n2_output.txt, n3_output.txt)

n2 (m = 60, sigma = 1, sup over an s-grid then refined; spread hub laws = 5 and 7 intervals over +-8, +-12):
  Thm A, R = 0 on leaves: 2.375 (B = diag(.3,-.3), uniform hubs), 2.398 (B = .3 I), spread hubs 0.18-0.21.
     Bound sqrt(2pi) = 2.507: NEARLY SHARP (uniform hubs: int_{cube} dx/|x| = 3.526 vs disk 3.545, and the Gaussian limit
     of the leaf form has density 1.382 vs Ball's 1.414).
  Thm B, B = diag(a,0), R = L1^2/a: 2.65 (a = 1), 1.79 (a = .2), 0.60 (a = .02) uniform; spread 0.19-0.32. Bound 10.5.
  Definite B = b I, R = t L^T B^{-1} L, spread hubs: b = .2: 0.22, 0.25, 0.22, 0.15, 0.13 (t = 0,.5,1,1.5,2);
     b = .05: 0.28, 0.22, 0.18, 0.12, 0.09; b = .01: 0.29 (t = 0).  No growth as b -> 0.
n3 (B = diag(.2,-.2), uniform), P(|Q-s|<=eps)/(2eps) at eps = 1e-2..1e-6, worst s:
  t = 1   : 2.03 2.87 3.77 4.52 5.30  (log divergence)
  t = .99 : 2.04 2.89 3.33 3.37 3.35  (saturates ~ log(1/|1-t|))
  t = .9  : 2.18 2.64 2.65 2.67 2.66;  t = .5: 2.62;  t = 0: 2.41
  t = 1 plus lam V3^2 (third direction on the leaves, v3 orthogonal to the hub rows): lam = .25: 1.88; 1: 1.37; 4: 0.89 (flat)
  t = 1 plus 4 X_k^2 (independent coordinate): 0.73 flat;  plus 4X_k^2 - 4X_k'^2: 0.61 flat.

## 10. Theorem C (PROVED, draft): Schur-matched leaves - the log has weight ~ sqrt(det B); a third direction closes it

Q = (X_H + Z)^T B (X_H + Z) + W, Z = B^{-1}(A_{HJ} X_J + g(X_K)), W = W(X_K), g affine, W quadratic, arbitrary.
Given X_K the level is fixed, so average over X_J AT A FIXED LEVEL (no sup needed). kappa_Z := ||rho_Z|| <= 2D/(s1 s2).
 (a) B definite: p <= (1/(2 sqrt D)) 2 pi kappa_Z <= 2 pi sqrt(D)/(s1 s2).  [numerics: 1.139 measured vs 1.257 bound]
 (b) B indefinite: Lemma 1.4's tail bound 3 log(1+1/m) is uniform in the centre; split each branch at |t| = T2,
     average the middle over Z (<= 2 T2 kappa_Z), choose e^{T2} with m >= M = 1/kappa_Z:
       p_{Y^T B Y}(delta) <= (kappa_Z/sqrt D) [7.04 + 2 log_+(4 sqrt2/kappa_Z) + log_+(1/(Lambda |delta|))].
     Hence p_Q(s) <= (2 sqrt D/(s1 s2)) [7.04 + 2 log_+(2 sqrt2 s1 s2/D) + E log_+ 1/|s - W|]   (D <= 4).
 (c) small-ball lemma (re-derived, decoupling): any quadratic zeta with quadratic part S: P(|zeta - s| <= rho)
     <= 4 (rho/||S||)^{1/4}; so ||S_W|| >= 1 gives E log_+ 1/|s - W| <= 9.55 and ||p_Q|| <= (2 sqrt D/(s1s2))(16.6 +
     2 log_+(2 sqrt2 s1 s2/D)). S_W = Schur complement of B in the (H u K) block; >= 1 whenever that block has three
     eigenvalues of modulus >= 1 (Lemma 1.5).

====================================================================================================================
# CLEAN WRITE-UP: groups of hubs with a nonzero hub block (complete proofs)
====================================================================================================================

## W0. Summary

Let H be a set of k = |H| >= 2 coordinates, B = A_HH the hub block, A = A_{H,H^c} the hub rows with singular values
s_1 >= ... >= s_k > 0, X' = X_{H^c}, L = A X' + beta_H and R(X') everything not involving X_H:
      Q = X_H^T B X_H + 2 X_H^T L + R(X').
GEOM Prop 5.5 gives ||p_Q|| <= 1/2 + 8/(s1 s2) for k = 2, B = 0 and every R.

 Thm 1  k = 2 and ANY hub block with det B < 0 (in particular zero hub diagonals with an arbitrarily small hub-hub
        coupling): the remainder R = L^T B^{-1} L gives P(|Q| <= eps) >= c eps log(1/eps); no bounded density. The full
        matrix has rank two, no pivot, small entries.  Prop 5.5 does not extend to B != 0 "whatever the remainder".
        PROVED (i.e. the naive extension is FALSE).
 Thm 2  Private leaves (the leaves J coupled only to the hubs): ||p_Q|| <= C_k / s_k(A_{HJ}) for EVERY hub block and
        everything else arbitrary; C_2 = sqrt(2 pi) = 2.507, C_3 = 1.710. Nearly attained (2.40). PROVED.
 Thm 3  k = 2, B = diag(a, 0) (any a), every remainder: ||p_Q|| <= 1 + 9.52 s_1^{-1/2} s_2^{-1}. PROVED.
 Thm 4  Schur-matched leaves + independent part W: the log of Thm 1 has weight <= 2 sqrt|det B|/(s1 s2); density
        <= 2 pi sqrt(det B)/(s1 s2) for definite B; for indefinite B <= (2 sqrt D/(s1 s2)) (16.6 + 2 log_+(2 sqrt2 s1 s2/D))
        once the Schur complement of B in the H u K block has norm >= 1. PROVED.
 Lem 5  Any quadratic zeta with quadratic part S: P(|zeta - s| <= rho) <= 4 (rho/||S||)^{1/4}. PROVED (re-derived).
 Conj 6 k = 2: bounded whatever the remainder iff det B >= 0; for det B < 0 a log profile of weight O(sqrt|det B|)
        around the random centre xi = R - L^T B^{-1} L.  k >= 3 (rank B != 2): bounded whatever the remainder.
        CONJECTURAL, numerical support.
 Prop 7 det B > 0 case of Conj 6 <= a maximal inequality for elliptic means of product densities; one-coordinate
        reductions lose exactly log(1/det B). Reduction PROVED, inequality OPEN.

Structural point. Given X', Q = q_c(X_H) + r, q_c(x) = x^T B x + c^T x, c = 2L, r = R(X'); r may be any function of X'
correlated with c, so the general bound is p_Q(s) <= E_c sup_t p_{q_c}(t). For B = 0 the sup is 1/|c|_inf (integrable
in dim 2). For B != 0 there is a critical point x0(c) = -B^{-1}c/2: if det B < 0, sup_t p_{q_c}(t) = infinity whenever
the product density is positive near x0(c), and Thm 1 shows a quadratic remainder can place all these log singularities
at one level; if det B > 0 the sup is finite but its expectation is a maximal function. What is proved avoids the sup:
the level is independent of the centre (Thms 2, 4), the critical set is a coordinate line (Thm 3), or the singularities
are made to coincide (Thm 1).

## W1. Tools

(F1) Ball + Rogozin: <v, X_J> has density <= sqrt2/|v|.
(F2) M X' (M k x m of rank k, singular values s_j) has density <= 2^{k/2}/prod s_j. So for k = 2: L has density
     <= 2/(s1 s2), c = 2L has density <= K := 1/(2 s1 s2), c_2 = 2 L_2 has density <= K_2 := 1/(sqrt2 s2)
     (the second hub row has norm >= s_2).
(F3) Bathtub: 0 <= g <= 1, int g <= 1, w radially decreasing about a point: int g w <= int over the ball of volume 1.
(F4) GEOM Lemma 1.4 and its proof: Y = (Y1,Y2) independent with densities g_i <= 1, B indefinite, det B = -D,
     eigenvalues mu_+ > 0 > mu_-, Lambda = 1/mu_+ + 1/|mu_-|. For delta != 0,
       p_{Y^T B Y}(delta) = (1/(2 sqrt D)) sum_{eps=+-1} int_R g(y_eps(t)) dt,  y_eps(t) = u_eps e^t + v_eps e^{-t},
       |u_eps| = |v_eps| = rho_0 = (1/2) sqrt(|delta| Lambda);  u, v depend only on (B, delta).
     For T >= T_1 = (3/4) log 2: int_T^inf g(y_eps(t)) dt <= 3 log(1 + 1/m), m = |u_{eps,i}| e^T/2 >= rho_0 e^T/(2 sqrt2),
     and likewise for t <= -T. This holds for all densities g_i <= 1, hence uniformly in translations of Y.
(F5) GEOM Lemma 1.3: Y in R^2 with ANY density <= kappa, B definite: p_{Y^T B Y} <= pi kappa/sqrt(det B).

Completing the square (B invertible):
   Q = Y^T B Y + xi,   Y = X_H + Z,   Z = B^{-1} L,   xi = R(X') - L^T B^{-1} L.                          (1.1)
Given X', Y has independent coordinates with densities f_h(. - Z_h) <= 1. The centre xi is a quadratic in X' with
matrix A/B (Schur complement, restricted to H^c). By (F2), Z has density <= |det B| 2^{k/2}/prod s_j.

## W2. Theorem 1 (counterexample)

Theorem 1. k = 2, B symmetric with det B = -D < 0, A of rank two, R(X') = L^T B^{-1} L. Then Q = Y^T B Y, and if the
density rho_Y of Y is positive at 0 (e.g. uniform laws on [-1/2,1/2], beta_H = 0) there are c_0, r_1 > 0 with
      P(|Q| <= eps) >= (2 c_0/sqrt D) eps (1 + log(r_1^2/eps))    (0 < eps <= r_1^2).
In particular Q has no bounded density.
Proof. xi = 0 in (1.1). rho_Y = f_H * mu (mu = law of Z) is the convolution of an L^1 function with an L^inf function
(Z has a bounded density), hence uniformly continuous. For uniform laws and beta_H = 0: AX' has a log-concave density,
positive on the interior of its support A[-1/2,1/2]^m, which contains a neighbourhood of 0 (A is onto R^2); so Z has
positive density near 0 and rho_Y(0) = int f_H(-z) dmu(z) > 0. Let rho_Y >= c_0 on |y| <= r_0. In the eigenbasis of B,
y^T B y = mu_+ u^2 - |mu_-| v^2; put a = sqrt(mu_+) u - sqrt|mu_-| v, b = sqrt(mu_+) u + sqrt|mu_-| v: y^T B y = ab,
da db = 2 sqrt D du dv; |a|, |b| <= r_1 := r_0/sqrt(Lambda) implies u^2 + v^2 <= r_0^2. Hence
   P(|Q| <= eps) >= (c_0/(2 sqrt D)) |{|ab| <= eps, |a|,|b| <= r_1}| = (c_0/(2 sqrt D)) 4 eps (1 + log(r_1^2/eps)).  QED
The matrix: M = G^T B G, G = [I_2, B^{-1} A], rank two; nonzero eigenvalues = those of B + A A^T B^{-1}
(= +-(b + sigma^2/b) for B = diag(b,-b), A A^T = sigma^2 I). Entries: B; the hub rows; a_j^T B^{-1} a_l (a_j = j-th
column of A). With |a_j| <= eta: remainder diagonal <= eta^2 ||B^{-1}||, remainder 2x2 minors det(B^{-1}) det[a_j a_l]^2,
mixed minors b_hh a_j^T B^{-1} a_j - A_hj^2. So ||B|| < c and eta^2 ||B^{-1}|| < c/4 give no c-pivot (spread rows,
m >~ sigma^2 ||B^{-1}||/c leaves). A no-pivot matrix with exactly two large eigenvalues and an unbounded density:
consistent with the conjecture (three are needed); it rules out any bounded-density statement for a pair of hubs that
holds whatever the remainder.
Remarks. (i) det B < 0 includes [[0,e],[e,0]] for every e != 0: Prop 5.5 is sharp in requiring A_HH = 0 exactly.
(ii) The weight is small: rho_Y(0) <= ||rho_Z|| <= 2D/(s1 s2), and Theorem 4(b) gives the matching upper bound
p_Q(s) <= (2 sqrt D/(s1 s2)) (log(1/|s|) + O(log(s1 s2/D))).  (iii) In RESULTS Theorem H this remainder is a rank-two
A_JJ = A^T B^{-1} A whose eigenvectors lie in the span of the hub rows; the frame rho~_i in R^4 has rank two and
det G~ = 0.  (iv) The same remainder with det B > 0 gives ||p_Q|| <= pi ||rho_Y||/sqrt D <= 2 pi sqrt D/(s1 s2) (F5).
Numerics: Section 8 of these notes (fitted log-slopes 0.359 and 0.089 against predicted 0.362 and 0.092).

## W3. Theorem 2 (private leaves; any hub block, any k >= 2)

Theorem 2. Split the coordinates as H u J u K, |H| = k >= 2, and suppose the matrix of Q vanishes on J x J and J x K
(linear terms on J arbitrary; the blocks H x H, H x K, K x K and all other linear terms arbitrary). If
s_k(A_{HJ}) >= sigma > 0, then
      ||p_Q||_inf <= C_k/sigma,  C_k = (sqrt2/2) int_{|x| <= r_k} dx/|x|, V_k r_k^k = 1,
      C_k = (sqrt2/2) |S^{k-1}|^{1/k} k^{(k-1)/k}/(k-1);  C_2 = sqrt(2 pi) = 2.5066, C_3 = 1.7096.
Proof. Condition on X_K; then Q = <v(X_H), X_J> + g(X_H) with v(x) = 2 A_{HJ}^T x + b_J and g a function of X_H.
Condition further on X_H = x: by (F1) the density of Q at s is <= sqrt2/|v(x)|. By Fubini
p_Q(s) <= int f_H(x) sqrt2/|v(x)| dx. Let P be the orthogonal projection onto range(A_{HJ}^T) and
w_b = (A A^T)^{-1} A b_J (A = A_{HJ}), so P b_J = A^T w_b and P v(x) = 2 A^T (x - x_b), x_b = -w_b/2. Then
|v(x)| >= |P v(x)| >= 2 sigma |x - x_b|, and (F3) gives int f_H(x)/|x - x_b| dx <= int_{|x| <= r_k} dx/|x|.  QED
Remarks. No smallness, leverage or eigenvalue condition. The hypothesis k >= 2 is essential (in 1D the last integral
diverges). Compared with RESULTS Theorem H (r = 0): Theorem H allows a diagonal A_II on the leaves and arbitrary
leaf-to-rest couplings but needs normalised leverages <= 1/2; Theorem 2 needs pure leaves and no leverage condition,
with an explicit constant. Sharpness: uniform hub laws on [-1/2,1/2]^2, R = 0 on the leaves, m = 60 spread leaves:
sup_s p_Q = 2.375 (B = diag(.3,-.3)) and 2.398 (B = .3 I) against 2.507; the gap is int_{cube} dx/|x| = 3.526 versus
the disk 3.545, and the Gaussian leaf density 1.382 versus 1.414.

## W4. Theorem 3 (one hub diagonal, no hub-hub coupling, every remainder)

Theorem 3. k = 2, B = diag(a, 0) with a != 0 arbitrary, A of rank two, R arbitrary. Then
      ||p_Q||_inf <= 1 + 16 sqrt(K K_2) = 1 + 9.514 s_1^{-1/2} s_2^{-1}.
Proof. Given X, q(x) = a x1^2 + c1 x1 + c2 x2 + r. The density of c2 X2 at t - g(x1) (g(x1) = a x1^2 + c1 x1) is
f2((t - g(x1))/c2)/|c2|, so
      p(t) = (1/|c2|) int f1(x1) f2((t - g(x1))/c2) dx1.
Let x1* = -c1/(2a) and omega > 0. On each of the two half-lines x1 >= x1* + omega, x1 <= x1* - omega the map
x1 -> x2 = (t - g(x1))/c2 is monotone with |dx2/dx1| = 2|a||x1 - x1*|/|c2| >= 2|a| omega/|c2|, so bounding f1 <= 1
there, the contribution of both is <= (1/|c2|) * 2 * |c2|/(2|a| omega) = 1/(|a| omega). On the window bound f2 <= 1:
      sup_t p(t) <= 2/lambda + m1(x1*, lambda/(2|a|))/|c2|,   lambda = 2|a| omega,  m1(x, w) = int_{|y-x|<=w} f1,
and also sup_t p(t) <= 1/|c2|. Now average over c = (c1, c2) (density <= K) with lambda = theta |c2|^{1/2} on |c2| <= 1:
  E[2/lambda; |c2| <= 1] <= (2/theta) K_2 int_{-1}^{1} |y|^{-1/2} dy = 8 K_2/theta;
  E[m1/|c2|; |c2| <= 1] <= K int_{|c2|<=1} (1/|c2|) [int m1(-c1/(2a), lambda/(2|a|)) dc1] dc2,
and the inner integral is int f1(x) |{c1 : |2a x + c1| <= lambda}| dx = 2 lambda: the critical line x1 = x1*(c1) moves
at speed 1/(2|a|) in c1, so the window meets the mass of f1 with probability proportional to lambda, whatever a is.
This term is <= 2 theta K int_{-1}^{1} |y|^{-1/2} dy = 8 theta K. On |c2| > 1, sup_t p <= 1. With theta = sqrt(K_2/K):
E sup_t p <= 1 + 16 sqrt(K K_2), and p_Q(s) <= E sup_t p_{q_c}(t).  QED
Remarks. Uniform in a (no smallness needed). The same bound holds for k >= 3 hubs with B = diag(a, 0, ..., 0): condition
on the other hubs. Numerics with the adversarial remainder R = L_1^2/a (Schur matching in the first hub): sup density
2.65 (a = 1), 1.79 (a = .2), 0.60 (a = .02) for uniform laws, 0.19-0.32 for spread laws; bound 10.5.
What makes this case provable is that the critical set {x1 = x1*} is a coordinate line: the window is independent of
the level t and its mass is linear in f1. Any 2 x 2 block with b_12 != 0 and b_22 = 0 has det < 0 and falls under Thm 1.
(In the first line of the proof, "Given X" means given X_{H^c}.)

## W5. Lemma 5 (small ball for any quadratic polynomial)

Lemma 5. zeta = Z^T S Z + b^T Z + c_0, Z with independent coordinates with densities <= 1, lambda = ||S|| > 0. Then
P(|zeta - s| <= rho) <= 4 (rho/lambda)^{1/4} for all s, rho > 0. Consequently E log_+ 1/|zeta - s| <= 9.55 if lambda >= 1.
Proof. If rho > lambda the bound exceeds 4. Case 1, some |s_ii| >= lambda/2: condition on the other coordinates; zeta is
a 1D quadratic with leading coefficient s_ii and GEOM Lemma 1.2(ii) gives <= 2 sqrt(2 rho/|s_ii|) <= 4 sqrt(rho/lambda)
<= 4 (rho/lambda)^{1/4}. Case 2, all |s_ii| < lambda/2: S_off = S - diag S has ||S_off|| > lambda/2. Take a unit u with
|u^T S_off u| = ||S_off||; for a uniformly random subset I (J = complement), E[2 u_I^T S_IJ u_J] = (1/2) u^T S_off u,
so some I has |2 u_I^T S_IJ u_J| >= ||S_off||/2, and since |u_I||u_J| <= 1/2, ||S_IJ|| >= ||S_off||/2 > lambda/4.
Decouple: with Z_J2 an independent copy of Z_J, Cauchy-Schwarz in Z_I gives
P(|zeta - s| <= rho) <= P(|zeta(Z_I, Z_J) - zeta(Z_I, Z_J2)| <= 2 rho)^{1/2}. The difference is 2 Z_I^T S_IJ W + h(Z_J, Z_J2),
W = Z_J - Z_J2 (independent coordinates with densities <= 1); the Z_I^T S_II Z_I and linear Z_I terms cancel.
By (F1), P(. | W) <= min(1, 2 sqrt2 rho/|S_IJ W|), and P(|S_IJ W| <= t) <= 2 sqrt2 t/||S_IJ|| (project on the top left
singular vector). With t = sqrt(rho ||S_IJ||): P <= (4 sqrt2)^{1/2} (rho/||S_IJ||)^{1/4} <= 2.378 (4 rho/lambda)^{1/4}
= 3.37 (rho/lambda)^{1/4}. For the logarithm: E log_+ 1/|zeta - s| = int_0^inf P(|zeta - s| <= e^{-tau}) dtau
<= int_0^inf min(1, 4 lambda^{-1/4} e^{-tau/4}) dtau = 4 log 4 - log lambda + 4 <= 9.55 for lambda >= 1.  QED

## W6. Theorem 4 (Schur-matched leaves: the logarithm has small weight; a third direction closes it)

Setting. H = {h1, h2}, J, K disjoint, B = A_HH invertible, D = |det B|, s_1 >= s_2 the singular values of A_{HJ}, and
      Q = (X_H + Z)^T B (X_H + Z) + W,   Z = B^{-1}(A_{HJ} X_J + g(X_K)),   W = W(X_K),
with g affine and W quadratic, both arbitrary. This allows arbitrary hub-K couplings and anything on K; the J-block is
the Schur-matching block A_{JH} B^{-1} A_{HJ} and the J x K block is A_{JH} B^{-1} G, G the linear part of g.
Theorem 4. (a) If B is definite, ||p_Q|| <= 2 pi sqrt(D)/(s1 s2).
(b) If B is indefinite and D <= 4, then for every s
      p_Q(s) <= (2 sqrt D/(s1 s2)) [ 7.04 + 2 log_+(2 sqrt2 s1 s2/D) + E log_+ 1/|s - W| ].
(c) If moreover the Schur complement S_W = A_KK - A_KH B^{-1} A_HK (the quadratic part of W) has ||S_W|| >= 1 - which
holds whenever the principal block of the matrix of Q on H u K has at least three eigenvalues of modulus >= 1 (GEOM
Lemma 1.5) - then ||p_Q|| <= (2 sqrt D/(s1 s2)) (16.6 + 2 log_+(2 sqrt2 s1 s2/D)).
Proof. Condition on X_K; then W is a constant w and the level of Y^T B Y is fixed. Z = B^{-1}(A_{HJ} X_J + g) has
density <= kappa_Z := 2D/(s1 s2) by (F2), and Y = X_H + Z has density rho_Y = E f_H(. - Z) <= kappa_Z.
(a) (F5): p <= pi kappa_Z/sqrt D = 2 pi sqrt D/(s1 s2); average over X_K.
(b) Given Z = z, Y has independent coordinates with densities f_h(. - z_h) <= 1, so (F4) applies for each z with
the same curves y_eps(t) (they depend only on B and the level delta). Fix T_2 >= T_1 and split each branch integral at
|t| = T_2. The tails are <= 3 log(1 + 1/m) each for every z, with m >= rho_0 e^{T_2}/(2 sqrt2). The middle part,
averaged over X_J at the fixed level, is int_{|t|<=T_2} E f_H(y_eps(t) - Z) dt <= 2 T_2 kappa_Z (Tonelli). Choose
e^{T_2} = max(e^{T_1}, 2 sqrt2 M/rho_0) so that m >= M; then T_2 <= 0.52 + log_+(4 sqrt2 M/sqrt(|delta| Lambda)) and
      p_{Y^T B Y}(delta) <= (1/sqrt D) [2 kappa_Z T_2 + 6/M].
With M = 1/kappa_Z:  p_{Y^T B Y}(delta) <= (kappa_Z/sqrt D) [7.04 + 2 log_+(4 sqrt2/kappa_Z) + log_+ 1/(Lambda |delta|)].
F(kappa) = kappa (a + 2 log_+(4 sqrt2/kappa)) is increasing for a >= 2, so kappa_Z may be replaced by 2D/(s1 s2); and
Lambda >= 2/sqrt D >= 1 for D <= 4. Average over X_K at delta = s - W.
(c) Lemma 5 gives E log_+ 1/|s - W| <= 9.55.  QED
Meaning. Theorem 1 is the case W = const of (b): the logarithm is real and its weight 2 sqrt(D)/(s1 s2) tends to zero
with the hub block. The unbounded density needs the remainder to align EVERY singularity exactly; an independent
structure with one large eigenvalue off the leaves removes it. Numerics: adding 4 X_k^2 to the Theorem 1 example gives
a flat 0.73, adding 4 X_k^2 - 4 Y_k^2 (two new coordinates) gives 0.61.

## W7. The general hub block: conjectures and the missing maximal inequality

Conjecture 6. (i) k = 2, det B >= 0: ||p_Q|| <= C(s_1, s_2) for every remainder, uniformly in B.
(ii) k = 2, det B < 0: p_Q(s) <= C + C sqrt|det B| E log_+ 1/|s - xi| with xi = R - L^T B^{-1} L (the Schur centre, a
quadratic with matrix A/B); in particular P(|Q - s| <= u) <= C u (1 + log 1/u) for every remainder, and ||p_Q|| <= C
whenever the whole matrix has three eigenvalues of modulus >= 1 (then ||A/B|| >= 1 by GEOM Lemma 1.5 and Lemma 5 applies).
(iii) k >= 3 with rank B != 2: ||p_Q|| <= C(s_1, ..., s_k) for every remainder.
Evidence: Theorems 1-4; numerics below (no growth as b -> 0 for definite b I under five remainders; for indefinite B the
density is bounded for every remainder tried except exact Schur matching).

Proposition 7 (reduction). For definite B put M_B f(x) := sup_t p_{(X_H - x)^T B (X_H - x)}(t)
= sup_{delta > 0} (1/(2 sqrt D)) int_0^{2 pi} f_H(x + y_delta(theta)) dtheta (ellipse means, GEOM Lemma 1.3). Since
q_c(x) = (x - x0)^T B (x - x0) + kappa(c) with x0 = -B^{-1} c/2, for every remainder
      p_Q(s) <= E_c sup_t p_{q_c}(t) = E M_B f_H(x0),   x0 having density <= 4 D K = 2D/(s1 s2).
Hence Conjecture 6(i) for definite B follows from the ELLIPTIC MAXIMAL INEQUALITY FOR PRODUCTS:
      int rho(x) M_B f(x) dx <= Phi(||rho||_inf/det B)  for all f = f1 x f2 (f_i <= 1, int f_i = 1), all B > 0 and all
      probability densities rho,
with ||p_Q|| <= Phi(2/(s1 s2)). In every example (unit square, spread grids of n^2 squares, isotropic B) the left side
is <= C sqrt(||rho||/det B) (a weak-L^2 bound |{M_B f > h}| <~ 1/(h^2 det B)). The circular maximal function is not
bounded on L^2 for general functions, so the product structure has to be used in both coordinates at once: bounding
f1 f2 <= f_i on the arcs where x_i moves fast gives M_B f(x0) <= (C/sqrt D)(M f1(x0_1) + M f2(x0_2)) (1D Hardy-
Littlewood maximal functions), and E M f1(x0_1) against a one-dimensional density of height ~|b| K_1 is ~ |b| K_1
log(1/|b|), sharp for f1 = 1_[0,1]. So every one-coordinate reduction loses exactly log(1/det B). The rank-one case
(Theorem 3) escapes because its critical set is a coordinate line and the window is independent of the level.
For indefinite B the analogous statement is a bound for the regular part sup_delta [p_{q_c}(delta) - w(c) log_+ 1/|delta
- kappa(c)|] with E w = O(sqrt D); combined with Lemma 5 for the centre xi it would give Conjecture 6(ii).

## W8. The requested generalisations

Rows not orthogonal: nothing above uses orthogonality; only singular values of the hub rows enter (s_k(A_{HJ}) in
Theorem 2, s_1, s_2 and |A_2| >= s_2 in Theorem 3, the singular values of A_{HJ} in Theorem 4).
Hubs overlapping the remainder's large eigenvectors: the overlap is the whole story. No remainder on the leaves:
Theorem 2 (bounded). Remainder whose eigenvectors lie in the span of the hub rows and match B^{-1} exactly: Theorem 1
(unbounded if det B < 0), Theorem 4 (bounded with weight sqrt D once a third structure is present off the leaves).
Partial overlap: RESULTS Theorem H, with the bound proportional to det(G~)^{-1/2}, which degenerates exactly at full
overlap. Numerically (B = diag(.2,-.2), R = t L^T B^{-1} L): bounded for t != 1 with a level ~ log(1/|1 - t|)
(t = .99: 3.35; t = .9: 2.66; t = 0: 2.41), divergent only at t = 1; a third direction on the leaves themselves
(R = L^T B^{-1} L + lam V3^2, v3 orthogonal to the hub rows) is bounded (lam = .25, 1, 4: 1.88, 1.37, 0.89).
One hub plus a hub-like structure inside the remainder: a coordinate of the remainder with a spread row coupled to the
hub is a second hub, and the pair has block [[a_hh, a_hk], [a_hk, a_kk]]; the dichotomy is the sign of
a_hh a_kk - a_hk^2. Zero diagonals with a_hk != 0: Theorem 1 (a Schur-matching remainder makes it unbounded; a third
large eigenvalue is needed, Theorem 4 / Conjecture 6(ii)). a_hk = 0 and one zero diagonal: Theorem 3 (bounded whatever
the remainder). A hub plus a delocalised rank-one direction (GEOM Prop 5.4) is not a hub pair and is not affected.

## W9. Numerics (exact conditional estimators)

Estimator. Given X' and X_{h1}, Q is a one-dimensional quadratic in X_{h2}; P(|Q - s| <= eps | X', X_{h1}) is the
f_{h2}-measure of at most two explicit intervals, computed exactly for laws uniform on unions of intervals. Averaging
over samples of (X', X_{h1}) gives an unbiased estimate of P(|Q - s| <= eps) with values in [0, 1]; P/(2 eps) is
reported. Scripts: hubpair_lib.py (estimator), n1_counterexample.py, n2_positive_cases.py, n3_indefinite_third.py;
outputs n1_output.txt, n2_output.txt, n3_output.txt. m = 60-80 leaves with spread orthonormal hub rows (sigma = 1,
entries <= 0.31), leaf laws uniform, hub laws uniform or spread (5 and 7 intervals over +-8 and +-12), 1.5e5-1.2e6
samples, all runs BelowNormal and under 10 minutes.
  Theorem 1: slopes 0.359 / 0.089 against 0.362 / 0.092 (table in Section 8); definite control flat at 0.57.
  Theorem 2: 2.375, 2.398 (uniform hubs), 0.18-0.21 (spread hubs); bound 2.507.
  Theorem 3: 2.65, 1.79, 0.60 (a = 1, .2, .02; uniform), 0.19-0.32 (spread); bound 10.5.
  Theorem 4(a): 1.139 = (pi/b) rho_Y(0), bound 1.257.  Theorem 4(b)-(c): 0.73 and 0.61 flat in eps.
  Open definite case, B = b I, spread hubs, R = t L^T B^{-1} L with t = 0, .5, 1, 1.5, 2:
     b = .2: 0.22 0.25 0.22 0.15 0.13;  b = .05: 0.28 0.22 0.18 0.12 0.09;  b = .01 (t = 0): 0.29.
  Open indefinite case: see W8.

## W10. Audit

 - Theorem 1: the lower bound is proved; the numerical log-slopes agree with the predicted rho_Y(0)/sqrt D to 1-3%,
   and the weight scales like b (0.359 at b = .2, 0.089 at b = .05). The no-pivot claim was checked entry by entry.
 - Theorem 2: constant recomputed from |S^{k-1}| r^{k-1}/(k-1); the numerical value 2.40 sits below 2.507 by exactly the
   two explained losses (cube versus disk, Gaussian versus Ball density).
 - Theorem 3: the inequality p_Q(s) <= E_c sup_t p_{q_c}(t) holds for every remainder, so the adversarial choice is
   covered; the window integral int m1 dc1 = 2 lambda was recomputed from |{c1 : |2ax + c1| <= lambda}|.
 - Theorem 4: F4's tail bound is uniform in the translation because it only uses g_i <= 1 and int g_i <= 1; the middle
   average uses Tonelli at a FIXED level, which is legitimate because W depends only on X_K.
 - Lemma 5: (4 sqrt2)^{1/2} = 2.378, times 4^{1/4} = 3.364 <= 4; int_0^inf min(1, 4 e^{-tau/4}) = 4 log 4 + 4 = 9.55.
 - Strongest case against Conjecture 6(i): the elliptic maximal inequality could fail for some product set built like
   a Besicovitch-Rado-Kinney set in each coordinate. Check: search for product sets maximising int rho M_B f with rho of
   height h over a disk of area 1/h, for h -> 0; growth faster than h^{1/2} would falsify the weak-L^2 form.

Next step. Prove the elliptic maximal inequality for product densities (equivalently E_c sup_t p_{q_c}(t) <= C for
definite 2 x 2 hub blocks), then its hyperbolic analogue with the logarithm removed; with Lemma 5 this would show that a
pair of hubs with any hub block inside a matrix with three large eigenvalues has a bounded density.

## W11. Adversarial check of Conjecture 6(i) (n4_adversarial_definite.py, n4_output.txt)

Sup density, R = 0 / half Schur match / full Schur match (L^T B^+ L), uniform | spread hub laws:
  diag(.2,.2)       2.397 1.950 1.083 | 0.098 0.099 0.098
  diag(.2,.02)      2.463 0.709 0.316 | 0.118 0.109 0.084
  diag(.2,.002)     2.452 0.259 0.075 | 0.119 0.045 0.030
  diag(.2,.0002)    2.406 0.064 0.024 | 0.120 0.016 0.009
  .2 u u^T (rotated rank one, u = (1,1)/sqrt2)       2.408 2.359 2.051 | 0.109 0.114 0.117
  .2 u u^T + .002 n n^T (near rank one)             2.444 0.203 0.064 | 0.108 0.058 0.032
No growth under anisotropy or near-degeneracy; R = 0 values sit just under the Theorem 2 bound 2.507 (as they must).
Check: nothing here uses the pointwise Rudelson-Vershynin bound; no Fourier input anywhere.
The referee's two-hub bound sqrt(2 pi)/sigma_min for any hub block under A_SS = A_SK = 0 is Theorem 2 with k = 2.

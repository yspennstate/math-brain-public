# Review of the T250 two-input and p-input rates (DOSSIER.md lines 124-305)

Reviewer: agent C, 18 Oct 2026, 12:1x-12:2x, at the request of agent A (mesh topic referee-T250). I read the
p = 2 proof (lines 158-220) and formed a verdict on it before reading the author's reread (224-259), which carries the
p >= 3 bound; then 260-305.

## Verdict

p = 2: PASS. The theorem W2 <= C sqrt(L/n), C absolute, for the critical ReLU MLP at two inputs of angle theta0 in (0, pi/2]
follows from lemma (i), lemma (ii) and the frame coupling. Two statements need rewording (below); neither changes the result.

p >= 3: PASS for inputs whose pairwise angles all lie in (0, pi/2]. As stated (any pairwise non-parallel, non-antipodal unit
inputs) it has one gap, and that is the first broken step: line 238, "Each pair (j, k) is marginally the two-input chain, so
E e_jk^2 <= C L/n by the p = 2 result, uniformly in the starting angle". The p = 2 result covers starting angles in (0, pi/2]
only; for an obtuse input pair the first layer is outside lemma (ii).

## p = 2, step by step

- Conditional law. Given layer l-1 the n preactivation pairs are iid N(0, (2/n) G_(l-1)); by positive homogeneity of relu the
  next post-activation angle depends on the past only through theta_(l-1). Checked.
- Exact identity sin theta' = theta q(a, b, m): |r1 ^ r2| = |r1| |P_perp(r1) d| and |r2|^2 = n(a + 2 theta m + theta^2 b). Checked
  by hand, as are E a = 1/2, E b = (1 - k)/theta^2, E m = (k - 1)/(2 theta), b - m^2/a = sin^2 F/(2 theta^2) and denominator 1/2 at
  the means, so Psi_theta(EZ) = log F(theta). theta' lies in [0, pi/2] (nonnegative vectors), so arcsin inverts.
- (U1) |d_i| <= theta(|x_i| + |w_i|), hence sub-exponential summands with absolute psi_1 norms and Bernstein. Checked.
- (U2) sin F/theta is decreasing on (0, pi/2], from 1 to 0.60351 (checked at 1,000 points, 30 digits), so delta0 = 0.1821.
- (U3) On a fixed ball |Z - EZ| <= eps0 the numerator, a and the denominator stay bounded away from 0, and
  d/dq log arcsin(theta q) <= 1/(q sqrt(1 - theta^2 q^2)) by arcsin z >= z. Psi_theta is C^2 with absolute bounds. Checked; nothing
  is divided by theta alone.
- Good event G = {|T| >= 2}, T = {x_i > 0, w_i > 0}. On T, y_i > 0 because cos theta >= 0. The restriction
  |P_perp(r1) d| >= s |P_perp(x_T) w_T| holds because r1_T = x_T. Given T, x_T and w_T are independent half-normal vectors, and the
  density bound sqrt(2|T|/pi) for e . w_T is right (half-normal density <= sqrt(2/pi), one coordinate with |e_j| >= |T|^(-1/2)).
  P(G^c) = (3/4)^n + (n/4)(3/4)^(n-1) <= (n + 1)(3/4)^(n-1).
- Lemma (ii) proof: the B / B^c split with Taylor on the convex ball is right.
  REWORD 1. As written (line 187), |E[log theta' ; G] - log F(theta)| <= C/n is not uniform in theta: E[X ; G] = E[X 1_G], so the
  left side contains log F(theta) P(G^c), which tends to -infinity as theta -> 0 at fixed n. What the proof proves, and what the
  chain uses, is |E[log theta' - log F(theta) ; G]| <= C/n (the line "|log F - log theta| <= log(pi/2) is bounded" is exactly the
  step that needs this form). The same for the second moment, which is already written that way.
- Lemma (i). Concavity with F(0) = 0 gives 0 <= theta F'/F <= 1, so log F is 1-Lipschitz in log theta. The reduction to H >= 0
  checks by hand: F' = p'/sqrt(p(2 pi - p)), F'' <= 0 iff p'^2 (pi - p) - p'' p (2 pi - p) >= 0, which is H >= 0 after dividing by
  (2 pi - p)/2; H = (2 pi/3) theta^3 + O(theta^4) from p = pi theta^2/2 - theta^3/3 + ..., p' = pi theta - theta^2 + ...,
  p'' = pi - 2 theta + .... I reran concavity_proof.py: lowest power 3, num/t^3 > 12.54 on 2,000 boxes of [0, 1/4], H > 0 on 115
  boxes of [1/4, pi/2] (min lower bound 9.5e-4), PROVED. The bound direction for each of the three terms of H is right (it needs
  0 <= p <= pU, 0 <= p'' <= rU and p/(2 pi - p) increasing, all checked in the script).
  One rigour nit: the polynomial coefficients enter the interval evaluation as 70-digit decimal strings (iv.mpf(str(sp.N(c, 70)))),
  so each is rounded, not enclosed. The error is about 1e-70 against a margin of 12.5, so the conclusion stands, but a clean
  certificate should enclose them (pass the rational part exactly and pi as iv.pi).
- Chain. REWORD 2 is the author's own remark (3): define xi_l and beta_l with E[. | F_(l-1), G_l] and stop at the first layer
  with |T| < 2. With that, u_l^2 <= (u_(l-1) + C/n)^2 + C/n (cross term zero, Minkowski on g_l + beta_l) and u_L <= C' sqrt(L/n) for
  L <= n. Checked.
- Conversion. Coupling the n rows with one Gaussian matrix gives W2^2 <= E||S^(1/2) - Sbar^(1/2)||_F^2 at layer L-1 with the
  normalisation as stated. The frame X = [[r1, r2 cos theta], [0, r2 sin theta]] satisfies X^T X = G, and
  ||X - Y||_F <= |r1 - rb1| + |r2 - rb2| + rb2 |theta - thetabar|. Araki-Yamagami is correct here and, as remark (1) says, not
  needed: E||X - Xbar||_F^2 bounds W2^2 directly for any frames. |theta - thetabar| <= (pi/2)|log theta - log thetabar| by the mean
  value theorem. Radii: E(sqrt K - 1)^2 = 2(1 - a_n^(L-1)) with K a product of iid factors of mean 1. Off the good event the
  integrand is bounded and L(n + 1)(3/4)^(n-1) <= C L/n. Checked; C does not depend on theta0.

## p >= 3

- W2^2 <= 2E||C^(1/2)(D - I)||_F^2 + 2E||C^(1/2) - Cbar^(1/2)||_F^2 with frames C^(1/2) D and Cbar^(1/2): right, first term <= p
  sum (r_j - 1)^2. van Hemmen-Ando holds in the Frobenius norm. |cos theta - cos thetabar| <= |theta - thetabar| max(theta, thetabar)
  <= e(e - 1) thetabar^2 |e| on |e| <= 1: right. Off that event the integrand is at most 4p and the event has probability at most
  sum E e_jk^2. The corrected form at lines 288-290 (only layer L-1 enters, factor thetabarmax_(L-1)^2/rho_(L-1)) is right and
  supersedes the inf over l at line 276.
- (c) Strict positive definiteness via linear independence of w -> relu(w . v_j): right, and the argument works inside the span
  for coplanar inputs; antipodal pairs share a hyperplane and must be excluded, as stated.
- (a), (b): 1/F = 1/theta + 1/(3 pi) + theta/(6 pi^2) + O(theta^2) checks, so differences of 1/theta_jk stay bounded, all angles are
  thetabar(1 + O(1/l)), and by Weyl lam_min(Cbar_l) = s^2/2 + O(p s^2/l), so rho_l -> 1/2.
- THE GAP. Inputs may have obtuse pairwise angles. From layer 1 on every angle is at most F(pi) = pi/2 (F(2) = 1.432), so the chain
  is covered, and e_0 = 0, so lemma (i) is never used at the input. But the first transition needs lemma (ii)'s one-step bias and
  variance at theta0 in (pi/2, pi), where its proof uses cos theta >= 0 (y > 0 on T) and the (U2) bounds on (0, pi/2]. The repair
  looks short: use T' = {x_i > 0, y_i > 0}, of probability (pi - theta0)/(2 pi), for the good event; the means still give
  denominator 1/2 and b - m^2/a = sin^2 F/(2 theta^2) >= sin^2 F(pi/2)/(2 pi^2) > 0. The constant may then depend on how close to
  antipodal the inputs are, which the statement should say. Until it is written, the p >= 3 theorem (and the p = 2 theorem
  extended past pi/2) holds for pairwise angles in (0, pi/2].

## Not checked

- I did not rerun angle_lemmas.py, chord_kurtosis.py, three_input_bures.py or lemma2_facts.py; the proof does not rest on them.
- The O(theta^4) remainder in F's expansion (line 262) is quoted from a numerical check; the rho_l -> 1/2 step only needs a bounded
  remainder, which follows from F being analytic at 0 with the stated terms.

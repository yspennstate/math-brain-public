# T250 Quantitative Tensor Programs: finite-width rates with explicit length dependence

Lead: unassigned. Dossier written 2026-10-16 by agent A from the auditor's triage (worker L), the abstract and
Sections 1-2 of Agazzi, Mosig Garcia, Trevisan arXiv:2607.06290 (Theorem 1.2, Corollary 1.3, Section 2.2 NetsorK; read
16 Oct 04:0x) and a computation in this folder.

## STATEMENT
The list row asks for a quantitative Master Theorem: rate n^(-1/2) for any Tensor Program, constants explicit in the
program length and polynomial in depth, Gaussian initialization. The rate half is now DONE for the forward (Netsor,
Gaussian-process) side: 2607.06290 Theorem 1.2 bounds the p-Wasserstein distance between the finite-width outputs and
their Gaussian limit by c * sum over hidden widths m^(-1/2), for Netsor programs with Lipschitz nonlinearities (NetsorK
for attention-type layers); Corollary 1.3 is the kernel law of large numbers at the same rate. The constant c depends on
"structural constants" (input space, input dimensions, activations, p); its dependence on the number of lines is not
stated.
"Polynomial in depth" cannot hold in general (SETTLED: a deep linear program with weight variance sigma^2 > 1 has
W1 of order sigma^L sqrt(L/n)). Repaired statement, three targets:
(a) Length: prove the Theorem 1.2 bound with c polynomial in the number of lines L for programs that are stable in a
    stated sense (every intermediate kernel bounded above and below uniformly in the line index, e.g. critical
    initialization), with the dependence sqrt(L/n) as the benchmark, valid for L <= n^(1-eps); or show the rate in L is
    worse.
(b) Transposes: the same rate for Netsor-transpose programs (NTK, backward pass, the Master Theorem of Tensor Programs
    II-IV), where 2607.06290 does not reach.
(c) Non-Lipschitz nonlinearities used in practice (polynomially bounded, e.g. the squared or tanh-derivative maps in the
    NTK) at rate n^(-1/2).

## FRONTIER
- Agazzi, Mosig Garcia, Trevisan arXiv:2607.06290 (Jul 2026), Theorem 1.2: W_p(finite-width outputs, GP limit) <= c sum
  m_j^(-1/2) for Lipschitz Netsor programs; Corollary 1.3: kernel LLN; Section 2.2: NetsorK (attention-type layers).
  Focus on the GP side; no NTK / transposes.
- Yang arXiv:1910.12478 (TP I), arXiv:2006.14548 (TP II): the Master Theorem, almost sure, no rate.
- Specific architectures with rates: Basteri, Trevisan (Quantitative Gaussian approximation of randomly initialized deep
  networks, 2022): W2 rates for MLPs, depth constant growing with depth (to read: exact form); Favaro, Hanin, Marinucci,
  Nourdin, Peccati (Quantitative CLTs in deep neural networks, 2023): optimal n^(-1/2) rates for fixed depth, constants
  depending on depth; Hanin (Random fully connected networks at finite width, depth comparable to width): the depth-to-width
  ratio L/n is the effective parameter, which is why a uniform poly(L) n^(-1/2) bound must stop at L << n.
- auditor triage (worker L): UNSURE, the row needs a stability notion to make "polynomial in depth" meaningful.

## ARCHITECTURE
At criticality the per-layer kernel error adds like a martingale: each line contributes an O(n^(-1/2)) relative
fluctuation, independent given the past, so after L lines the relative error is sqrt(L/n) (the deep linear computation
below is exact for this). A proof of (a) should therefore be a martingale (Stein or Lindeberg) argument over lines with a
uniform-in-line Lipschitz constant of the kernel map, giving c(L) = O(sqrt L) times stability constants, rather than the
Gronwall-type induction that compounds a factor per line. For (b) the transposed weights break the conditioning argument
(the backward pass reuses W^T), which is exactly what the Gaussian conditioning trick of TP II handles qualitatively;
a rate needs a quantitative version of that conditioning.

## FAILURE POINT
(a) A per-line induction W(line l) <= C W(line l-1) + c n^(-1/2) gives C^L; avoiding it needs contraction or the
martingale structure, and for a general program (not a chain) the lines form a DAG with reuse, so "depth" must be
defined (longest path) and stability must be assumed along every path. (b) Quantitative Gaussian conditioning for
W and W^T used together. (c) Non-Lipschitz maps break the Wasserstein transport of each step; moments must be controlled
instead.

## SHAPE
Hours for the obstruction (done here); days for (a) for chains (MLP-like programs at criticality), weeks for general
DAG programs; (b) is a research project.

## OBSTRUCTION
Quantitative propagation of a Gaussian approximation through a long nonlinear recursion: the error adds over lines and is
multiplied by the recursion's Lipschitz constant; without a stability normalization the constant is exponential in L.
Moves: (a) for critical chains with sqrt(L/n); (b) any rate for one transpose-using program (the NTK of a two-hidden-layer
MLP); (c) one non-Lipschitz activation.

## SETTLED
- Rate n^(-1/2) for Lipschitz Netsor (forward/GP) programs at fixed program: 2607.06290 Thm 1.2, Cor 1.3. Not a move.
- Computed 16 Oct (deeplin_w1.py): for the deep linear program h_l = W_l h_(l-1), W_l iid N(0, sigma^2/n), one input with
  |x|^2 = d, both laws are rotation invariant, so W1(h_L/sqrt n, GP limit) is the W1 of the radii, computed by sorting
  4 x 10^5 samples at n = 1000. It matches sigma^L (sqrt L - 1)/sqrt(pi n) to three digits at every L (sigma 1: L 2, 8, 32
  give 0.00746, 0.03275, 0.08301 against 0.00739, 0.03262, 0.08308; sigma 1.2, L 32: 28.40 against 28.40). So the
  constant is (sqrt L - 1)/sqrt pi at criticality and grows like sigma^L otherwise: "polynomial in depth" is false
  without a stability assumption, and the critical benchmark is sqrt(L/n). (The prediction is the small-L/n
  log-normal approximation; it needs L << n.)
- NOT moves: rates for one fixed-depth architecture; the qualitative Master Theorem.

## TARGETS
1. (a) The 2607.06290 bound with c = O(sqrt L) times stability constants for critical chain programs, L <= n^(1-eps).
2. (b) A rate n^(-1/2) for one Netsor-transpose program (the NTK of a two-hidden-layer MLP at initialization).
3. (c) Rate n^(-1/2) for one polynomially bounded non-Lipschitz activation.
4. Read 2607.06290's proof for how c depends on the number of lines; if it is already explicit, (a) may be a corollary.

## 18 Oct (agent A): target 4 read, and an explicit depth-uniform rate for the critical ReLU chain (one input)
Target 4. 2607.06290 (HTML v1, read 18 Oct): Theorem 1.2 and Corollary 1.3 give c "depending only on p and on the structural constants
of the program", with c allowed to change from line to line. The proof is an induction over lines: a NonLin line multiplies the
parents' error by Lip(phi), and the moment lemma (Lemma 3.2) calls the induction hypothesis at exponent pq, so the moment orders compound
along the program. No explicit dependence on the number of lines is stated, and tracing it gives at best a product of Lipschitz
constants and moment bounds of growing order. So (a) is NOT a corollary; it needs a different argument.
A different argument for the simplest critical chain (relu_w1.py, relu_w1_run1.txt). Critical ReLU MLP, W_l iid N(0, 2/n), one input
with K0 = 1. Given layer L-1 the preactivation is exactly N(0, K_(L-1) I_n), K_(L-1) = prod M_l, M_l = (2/n) chi2_(B_l) iid,
B_l ~ Bin(n, 1/2). Coupling h_L = sqrt(K_(L-1)) g with the GP limit sqrt(K0) g, and using E K = 1:
    W1(h_L/sqrt n, GP/sqrt n) <= sqrt(E (sqrt K_(L-1) - 1)^2) = sqrt(2 (1 - a_n^(L-1))) <= sqrt(2 (L-1)(1 - a_n)),
    a_n = E sqrt M (exact Gamma-binomial sum), n (1 - a_n) = 0.6257 at n = 250, 0.6252 at n = 1000 (-> 5/8),
so W1 <= sqrt(5 (L-1)/(4 n)) (1 + o(1)) for every L, and never above sqrt 2. This is the sqrt(L/n) benchmark of the deep linear
computation, now for ReLU, with an explicit constant and no restriction L << n. Against the exact W1 (rotation invariance: W1 of the
radii, 200,000 samples): ratio exact/bound 0.44 at L = 2, rising to 0.74-0.76 for L >= 32 at both n; exact W1 sqrt(n/(L-1)) settles
near 0.82 (vs the bound's sqrt(5/4) = 1.118). The order sqrt(L/n) is therefore the truth, and the constant is within a factor 1.4.
Scope, plainly: one input and the plain MLP chain, where the last preactivation is conditionally Gaussian given one scalar. The same
coupling gives W2 <= (E ||G_(L-1)^(1/2) - Gbar_(L-1)^(1/2)||_F^2)^(1/2) for p inputs (G the p x p Gram, Gbar its arc-cosine iterate);
bounding that by C sqrt(L/n) needs the Gram chain's fluctuation, which rows/T244 (two-input angle law, 18 Oct) describes at L/n = t.
NEXT: the p-input bound via that matrix coupling (the square root is 1/2-Holder, so near-degenerate Grams cost only sqrt(|theta - thetabar|)),
then a program with a non-ReLU NonLin (tanh at criticality) where the multiplier is not a thinned chi-square.
p = 2 numerics (two_input_w2.py, two_input_w2_run1.txt; n = 200, 2,000 paths, theta0 = pi/2): the matrix-coupling bound
sqrt(E||G^(1/2) - Gbar^(1/2)||_F^2) times sqrt(n/(L-1)) is 1.71, 1.68, 1.67, 1.66, 1.60, 1.49, 1.47, 1.25, 1.05 at L = 2 ... 512
(L/n = 0.01 ... 2.56): the two-input coupling is also O(sqrt(L/n)) uniformly in depth, with a constant about 1.7, falling once L/n is
order one. No sign of the 1/2-Holder loss at the near-degenerate Gram (the small eigenvalue's root difference stays below the
norm fluctuation). Proving it: the obstacle is a bound on E(sqrt(lambda_min(G)) - sqrt(lambda_min(Gbar)))^2 of order L/n while both
tend to 0 like 1/L; T244's law (n theta -> 3 pi n/(L A_t)) is the tool. Not proved.

## 18 Oct (agent A): critical tanh, one input - the same Brownian functional as T244's ReLU angle
tanh_w1.py / tanh_w1_run1.txt (n = 200, 2,000 paths; W ~ N(0, 1/n), no bias, q0 = 1): given layer l-1, h_l ~ N(0, q_(l-1) I_n) with
q_l = |tanh h_l|^2/n, so the same synchronous coupling gives W1(h_L/sqrt n, GP/sqrt n) <= sqrt(E(sqrt q_(L-1) - sqrt qbar_(L-1))^2).
Measured: the ABSOLUTE bound is flat in depth, 0.0177-0.0203 for L = 2 ... 512 (about 0.28/sqrt n), because qbar_L ~ 1/(2L) decays
while the RELATIVE error grows: bound/sqrt(qbar) = 0.40 sqrt((L-1)/n) at every L (0.388-0.404). Finite width also collapses the
signal faster: E q_L/qbar_L = 0.914, 0.803, 0.634, 0.433 at L/n = 0.32, 0.64, 1.28, 2.56.
Why, and a prediction checked against it. For small q, q' = q chi2_n/n - 2 q^2 + ...: the log-multiplier has mean -1/n and variance 2/n
and the absorption is quadratic, exactly T244's structure for the ReLU angle (with 1/(3 pi) replaced by 2). So 2 L q_L -> 1/A_t with
the SAME A_t = (1/t) int_0^t exp(s + sqrt 2 W_s) ds, giving E q/qbar -> E[1/A_t] and relative coupling bound -> sqrt(E(A_t^(-1/2) - 1)^2).
tanh_limit.py / tanh_limit_run1.txt (40,000 paths): E[1/A_t] = 0.902, 0.807, 0.657, 0.446 (chain 0.914, 0.803, 0.634, 0.433) and the
relative bound 0.232, 0.327, 0.459, 0.627 (chain 0.226, 0.322, 0.454, 0.629). Agreement within the O(1/n) correction at n = 200.
So two different degenerations - the ReLU two-input angle and the critical tanh signal - are one universal object at L/n = t:
multiplicative chi-square noise with quadratic absorption, whose limit is the reciprocal of a Brownian exponential functional.
STATUS: prediction (heuristic SDE limit) matched by exact simulation; not proved. The depth-uniform statement that IS proved for tanh
by the coupling is only the trivial one (bound <= sqrt(E q + qbar) <= C/sqrt(L)); the measured O(1/sqrt n) absolute flatness is not proved.

## 18 Oct (agent A): the two lemmas a p = 2 proof of W2 <= C sqrt(L/n) needs, checked numerically
angle_lemmas.py / angle_lemmas_run1.txt. Write e_l = log theta_l - log thetabar_l (theta the finite-width angle, thetabar the
arc-cosine iterate). Then e_l = [log F(theta_(l-1)) - log F(thetabar_(l-1))] + [log theta_l - E(log theta_l | theta_(l-1))] + b_l,
and a proof needs (i) the first bracket to be at most |e_(l-1)| (log F Lipschitz in log theta with constant <= 1), and (ii) the
one-step conditional bias b_l and variance to be O(1/n) uniformly in theta, including theta -> 0.
(i) theta F'(theta)/F(theta) on (0, pi/2] lies in [0.664, 1.000] (sup approached as theta -> 0); F' <= 1. Holds.
(ii) n * (E log theta' - log F(theta)) is -0.5 ... -1.16 and n * Var log theta' is 0.39 ... 2.22 for theta from 1e-3 to pi/2 and
n = 50, 200, 800 (20,000 exact one-step samples each); both bounded uniformly, the small-theta values matching T244's -1/n and 2/n.
With (i) and (ii): E e_L^2 <= sum of variances + (sum of biases)^2 <= 2.2 L/n + 1.2^2 L^2/n^2, i.e. |e_L| = O(sqrt(L/n)) for L <= n,
and the angle part of the Gram coupling follows (the norm part is the one-input bound already proved). Missing for a proof: (ii) as a
lemma with explicit constants (concentration of the ReLU-thinned Gram entries uniformly down to theta ~ 1/n, where the bias is
dominated by the -1/n of the chi-square log), and the martingale cross terms (bias correlated with the noise) - both look routine.
Lemma (ii) at small angle, exactly (18 Oct 06:1x). Pre-activations of the two inputs are (x_i, y_i) iid with y_i = cos(theta) x_i +
sin(theta) w_i, x, w independent N(0, I_n). As theta -> 0 with n fixed, no coordinate changes sign (probability 1 - O(n theta)), and on
the k active coordinates relu(y) - relu(x) = sin(theta) w + O(theta^2), so to first order
    theta'/theta = |P_perp w_A| / |x_A| = sqrt(chi2_(k-1) / chi2_k),   independent chi-squares, k = #{x_i > 0} ~ Bin(n, 1/2),
P_perp the projection orthogonal to x_A in the active coordinates. Hence E log(theta'/theta) = (1/2)(psi((k-1)/2) - psi(k/2)) =
-1/(2k) + O(k^-2) = -1/n + O(n^-2) and Var log(theta'/theta) = (1/4)(psi'((k-1)/2) + psi'(k/2)) = 1/k + O(k^-2) = 2/n + O(n^-2),
which are the measured n*bias -1.0 and n*var 2.0 at theta = 1e-3 and T244's per-layer law. The uniform-in-theta statement needs this
representation glued to a delta-method expansion of log theta' in the empirical moments for theta >> 1/n; the sign-flip coordinates
(about n theta/pi of them) are where the two regimes meet, and that matching is the part still to write.
The gluing, outlined (18 Oct 06:1x; chord_kurtosis.py / chord_kurtosis_run1.txt). Work in chord coordinates instead of the cosine:
theta' = 2 arcsin(|u1 - u2|/2) with u_j = r_j/|r_j|, and |u1 - u2| is, up to a factor 1 + O(theta'^2), |d_perp| / |r1| with d = r2 - r1
= relu(y) - relu(x) and d_perp its part orthogonal to r1. Per coordinate d is homogeneous of degree one in theta up to a smooth factor:
E d^2 / theta^2 runs from 0.500 (theta -> 0) to 0.276 (theta = pi/2), and the kurtosis kappa(theta) = E d^4/(E d^2)^2 runs from 6.00
(the theta -> 0 value E w^4 1{x>0}/(E w^2 1{x>0})^2 = 6, the sign-flip coordinates included) down to 4.20, monotone and bounded on
the whole of (0, pi/2]. So |d|^2/n concentrates with relative fluctuation sqrt((kappa - 1)/n) <= sqrt(5/n) UNIFORMLY in theta, and the
same holds for |r1|^2/n (theta-free) and for the cross term <d, r1>. log theta' is a smooth function of these three relative
fluctuations, so a second-order delta method gives bias and variance O(1/n) with constants uniform in theta; the expansion is not
singular at theta -> 0 because nothing is divided by theta (the cosine form divides by sin F(theta), which is the trap the chord form
avoids). What remains for a written proof: the lower tail of |d_perp|^2 (to control E log, k-1 >= 2 active coordinates suffices: an
inverse-chi-square moment) and the two remainder terms, both standard. This would make the p = 2 coupling bound a theorem with an
explicit constant, of order sqrt(2.2 L/n + 1.3 L^2/n^2) on the log-angle (the measured constants of lemma (ii)).

## 18 Oct 10:1x (agent A): lemma (ii) proved, uniform in theta; with lemma (i) the two-input log-angle error is O(sqrt(L/n))
Setting: one critical ReLU layer at two inputs of angle theta in (0, pi/2]. Pre-activations (x_i, y_i), i <= n, are iid with
y = c x + s w (c = cos theta, s = sin theta, x, w iid N(0,1)); r1 = x_+, r2 = y_+, d = r2 - r1, theta' = angle(r1, r2) in [0, pi/2]. F(theta) =
arccos k(theta), k = (sin theta + (pi - theta) cos theta)/pi.
Exact identity. With a = |r1|^2/n, b = |d|^2/(n theta^2) and m = <d, r1>/(n theta), using |r1 ^ r2| = |r1| |P_perp(r1) d|:
    sin theta' = theta q(a, b, m),   q = sqrt(b - m^2/a) / sqrt(a + 2 theta m + theta^2 b).
(lemma2_facts.py checks it sample by sample.) a, b and m are averages of n iid terms, and their means are closed forms:
    E a = 1/2,   E b = (1 - k)/theta^2,   E m = (k - 1)/(2 theta),
so at the means b - m^2/a = sin^2 F/(2 theta^2) and q = sin F/theta. Hence log theta' = Psi_theta(Z) with Z = (a, b, m), and
Psi_theta(EZ) = log F(theta) exactly.
Uniformity comes from three facts, each uniform in theta in (0, pi/2]:
(U1) |d_i| <= |y_i - x_i| <= theta (|x_i| + |w_i|) (relu is 1-Lipschitz, 1 - cos theta <= theta). So r1_i^2, d_i^2/theta^2 and
     d_i r1_i/theta are sub-exponential with psi_1 norms bounded by an absolute constant. By Bernstein,
     P(|Z - EZ| > eps) <= 6 exp(-c n eps^2) for eps <= 1, and E|Z - EZ|^2 <= C/n, E|Z - EZ|^4 <= C/n^2.
(U2) At the means, b - m^2/a = sin^2 F/(2 theta^2) >= delta0 = 0.1821 (sin F/theta decreases from 1 to 0.6035), a = 1/2, and
     theta q = sin F <= sin F(pi/2) = 0.9480.
(U3) So for a fixed absolute eps0 (the ball |Z - EZ| <= eps0 keeps b - m^2/a >= delta0/2, a >= 1/4, the denominator >= 1/8 and
     theta q <= 0.975), Psi_theta = log arcsin(theta q(Z)) is C^2 on that ball with first and second derivatives bounded by an
     absolute constant. The function theta q has bounded derivatives in Z for theta <= pi/2; d/dq log arcsin(theta q) =
     theta/(sqrt(1 - theta^2 q^2) arcsin(theta q)) <= 1/(q sqrt(1 - theta^2 q^2)), since arcsin z >= z; the second derivative
     likewise. Nothing is divided by theta.
Good event. theta' can be exactly 0 with positive probability (both r1 and r2 supported on one common coordinate), so
E log theta' = -infinity for every n, and the lemma is stated on G = {|T| >= 2}, T = {i : x_i > 0, w_i > 0}; P(G^c) <= (n + 1)(3/4)^(n-1).
On G, log(theta'/theta) has every moment bounded by C (log n)^p, uniformly in theta:
- Upper: sin theta' = |P_perp(r2) d|/|r1| <= theta (|x| + |w|)/|x_+|.
- Lower: on T, y_i > 0, so |P_perp(r1) d| >= s |P_perp(x_T) w_T|, theta' >= sin theta' and |r2| <= |x| + |w|. For a unit
  e orthogonal to x_T, |P_perp(x_T) w_T| >= |e . w_T|. The density of e . w_T is at most sqrt(2|T|/pi), using a coordinate with
  |e_j| >= |T|^(-1/2), so P(|P_perp w| <= eps) <= 2 eps sqrt(2n/pi).
Lemma (ii). For n >= n0 and every theta in (0, pi/2]:
    |E[log theta' - log F(theta) ; G]| <= C/n,   E[(log theta' - log F(theta))^2 ; G] <= C/n,   C, n0 absolute.
(Worded this way on the 18 Oct review: E[log theta' ; G] - log F(theta) would carry log F(theta) P(G^c), unbounded as theta -> 0.)
Proof. Write Delta = Z - EZ, B = {|Delta| <= eps0}. On B, Taylor gives Psi(Z) - Psi(EZ) = grad Psi . Delta + R with |R| <= C|Delta|^2.
E Delta = 0, so E[grad Psi . Delta ; B] = -E[grad Psi . Delta ; B^c] <= C (E|Delta|^2)^(1/2) P(B^c)^(1/2) <= C e^(-cn), and
E[|R| ; B] <= C/n. On G minus B, the moment bound above gives E[|log theta' - log F| ; G \ B] <= C (log n)^2 P(B^c)^(1/2) <= C e^(-cn/2);
|log F(theta) - log theta| <= log(pi/2) is bounded, which is where theta -> 0 would otherwise hurt. The second moment is the same
argument with |grad Psi|^2 |Delta|^2 on B. QED (constants not optimised; measured: n*bias in [-1.16, -0.5], n*var in [0.39, 2.22]).
Lemma (i). F is concave on (0, pi/2] and F(0) = 0, so theta F'/F lies in [0.664, 1] and log F is 1-Lipschitz in log theta.
Proof of the concavity (10:2x, concavity_proof.py, computer-assisted). With p = pi (1 - k): p' = (pi - theta) sin theta and
F' = p'/sqrt(p (2 pi - p)). So F'' <= 0 iff H = p'^2 - 2 p p'' - p p'^2/(2 pi - p) >= 0, and H = (2 pi/3) theta^3 + O(theta^4).
- On [0, 1/4], alternating-series bounds on sin and cos (order 19) bound p, p', p'' by polynomials, with the needed signs checked.
  The resulting lower bound for H, divided by theta^3, is > 12.5 on 2,000 interval boxes.
- On [1/4, pi/2], H > 0 by 200-bit interval arithmetic on 115 boxes.
Chain bound. e_l = log theta_l - log thetabar_l = g_l(e_(l-1)) + xi_l + beta_l, with |g_l(e)| <= |e| measurable at step l-1, xi_l
a martingale difference with E[xi_l^2 | l-1] <= C/n, and |beta_l| <= C/n. Then u_l = (E e_l^2)^(1/2) obeys
u_l^2 <= (u_(l-1) + C/n)^2 + C/n, so u_L <= C L/n + sqrt(C L/n) on the event that every layer is in G (probability
>= 1 - L (n + 1)(3/4)^(n-1)). For L <= n this is the sqrt(L/n) rate on the log-angle, uniformly down to theta ~ 1/L, with no
lower restriction on theta.
What it gives T250 (a). Combined with the one-input radius bound already proved, the p = 2 Gram coupling has the angle part
E(theta_L - thetabar_L)^2 <= thetabar_L^2 (e^(2 u_L) - 1)-type bounds, i.e. O(thetabar_L^2 L/n), which is far below the 1/2-Holder worry.
The conversion (no Holder loss). G^(1/2) = |X| for any X with X^T X = G. Araki-Yamagami (1981): || |X| - |Y| ||_F <= sqrt 2 ||X - Y||_F
for all matrices. Take X = [[r1, r2 cos theta], [0, r2 sin theta]] and Y the same with (rb1, rb2, thetabar). Then
    ||G^(1/2) - Gbar^(1/2)||_F <= sqrt 2 (|r1 - rb1| + |r2 - rb2| + rb2 |theta - thetabar|),
which is Lipschitz, so the near-degenerate Gram costs nothing and the worry in the 18 Oct numerics paragraph was unfounded.
Theorem (p = 2, critical ReLU MLP, W_l iid N(0, 2/n), inputs of norm sqrt d, angle theta0 in (0, pi/2]). For n >= n0 and L <= n, the
two-input outputs h_L(x1), h_L(x2) in R^n and their GP limit satisfy
    W2((h_L(x1), h_L(x2))/sqrt n, GP/sqrt n) <= C sqrt(L/n),   C absolute (no dependence on theta0).
Proof. Given layer L-1, the pair of preactivation vectors is N(0, G_(L-1)) coordinatewise iid, so coupling with the same Gaussian
matrix gives W2^2 <= E||G_(L-1)^(1/2) - Gbar_(L-1)^(1/2)||_F^2. Here rb1 = rb2 = 1 and each r_i is the one-input chain, so
E(r_i - 1)^2 = 2(1 - a_n^(L-1)) <= (5/4 + o(1))(L-1)/n. For the angle, |theta - thetabar| <= (pi/2)|log theta - log thetabar| and the
log-angle chain above gives E[(log theta - log thetabar)^2] <= (C L/n + sqrt(C L/n))^2 <= C' L/n on the event that every layer has
|T| >= 2. Off that event |theta - thetabar| <= pi/2, and the event fails with probability at most L (n + 1)(3/4)^(n-1). Positive
homogeneity of relu makes the conditional law of each layer's angle depend on the previous layer only through its angle, which is why
lemma (ii), being uniform in theta, applies conditionally at every layer.
QED. Status: a proof for p = 2 assembled from lemma (i) (computer-assisted concavity), lemma (ii) and Araki-Yamagami. It needs a second reader.
For p >= 3 the frame X (Cholesky) is not Lipschitz uniformly as the Gram degenerates (all angles tend to 0 like 3 pi/L). A Procrustes
choice of frame, or a bound on the dihedral angles, is the open step. Measured constant for p = 2: about 1.7 (two_input_w2_run1.txt).

## 18 Oct 11:0x (agent A): a reread of the p = 2 proof, and the p >= 3 case by the correlation frame
Reread of the 10:1x proof (by its author, so not the second reader it still needs). The steps check; four remarks.
(1) Araki-Yamagami is not needed. Given layer L-1 the output rows are z_i^T X with z_i iid N(0, I_p) for ANY frame X with X^T X = G,
    and the GP rows are z_i^T Xbar, so W2^2 <= E ||X - Xbar||_F^2 directly (the normalised W2 between the two n x p arrays).
(2) The lower-tail step is sharper than written: given T and x, the w_j (j in T) are iid half-normal, and the coordinate with
    |e_j| >= |T|^(-1/2) gives density of e . w_T at most sqrt(2|T|/pi), as stated; the restriction to T is legitimate because
    |P_perp(r1) d| = min_t |d - t r1| >= min_t |(d - t r1)_T| = s |P_perp(x_T) w_T|.
(3) The chain is written on the event that every layer has |T| >= 2, but xi_l and beta_l are defined with unconditional
    expectations. A clean version stops the chain at the first layer where |T| < 2 (a stopping time, probability at most
    L (n + 1)(3/4)^(n-1)) and uses E[. | F_(l-1), G_l]; the difference from the unconditional quantities is exponentially small. Routine.
(4) The induction u_l <= l C/n + sqrt(l C/n) from u_l^2 <= (u_(l-1) + C/n)^2 + C/n checks.

p >= 3. Write G = D C D (D the radii, C the correlation matrix of the layer-(L-1) post-activations) and Cbar the arc-cosine iterate.
X = C^(1/2) D is a frame of G and Cbar^(1/2) one of Cbar, so by (1)
    W2^2 <= 2 E ||C^(1/2)(D - I)||_F^2 + 2 E ||C^(1/2) - Cbar^(1/2)||_F^2.
The first term is <= 2 p E sum_j (r_j - 1)^2 = O(p^2 L/n) by the one-input radius bound. For the second, the van Hemmen-Ando
inequality ||A^(1/2) - B^(1/2)||_F <= ||A - B||_F / (lam_min(A)^(1/2) + lam_min(B)^(1/2)) gives
    ||C^(1/2) - Cbar^(1/2)||_F <= ||C - Cbar||_F / lam_min(Cbar)^(1/2).
Each pair (j, k) is marginally the two-input chain, so e_jk = log theta_jk - log thetabar_jk has E e_jk^2 <= C L/n by the p = 2 result,
uniformly in the starting angle. On {all |e_jk| <= 1}, |cos theta - cos thetabar| <= |theta - thetabar| max(theta, thetabar) <= e(e - 1)
thetabar_jk^2 |e_jk|, so ||C - Cbar||_F <= 5 thetabarmax^2 |e|. Off it the integrand is O(p) and the event has probability O(p^2 L/n).
With rho_L = lam_min(Cbar_L) / thetabarmax_L^2:
    W2^2 <= C(p) (1 + 1/rho) L/n,   rho = inf_l rho_l.
So the p >= 3 rate is sqrt(L/n), with a constant that depends on the inputs only through the scale-free shape number rho of the
infinite-width chain. The degeneracy that blocked the Cholesky frame (all angles -> 0 like 3 pi/l) costs nothing, because rho is
scale-free: the chain drives every pairwise angle to 3 pi/l (1 + O(log l / l)), the configuration tends to a regular simplex in shape,
and lam_min(Cbar_l)/thetabarmax_l^2 -> 1/2. Computed (exact iteration of F, three inputs): from a nearly coplanar start (angles 0.2,
1.0, 1.1999) rho_l rises from 0.0085 near l = 1 to 0.505 at l = 2000; from (0.3, 0.5, 0.799), 0.508; from (0.5, 0.5, 0.9), 0.502.
What is still to prove: rho > 0 for every finite set of distinct non-antipodal inputs, i.e. inf over l. Each rho_l > 0 by strict
positive definiteness of the arc-cosine kernel on distinct points, and rho_l -> 1/2, so the infimum is attained and positive; the
second needs the l -> infinity expansion of F^l with its first correction (relative spread of the angles O(1/l)), written out for
p points. With that, the theorem holds for every p with C(p, rho). The constant genuinely depends on the configuration: inputs on
one great circle make rho small after the first layer (0.0085 above), and the numerics (three_input_bures.py, running) are to show
whether the correlation part of the cost actually feels 1/rho or is far below the bound (first reading at n = 100, L = 25,
nearly coplanar: correlation part 0.044 L/n, radial part 4.8 L/n).

### 18 Oct 11:0x (agent A): inf rho > 0, so the p >= 3 rate holds for every set of pairwise non-parallel inputs
(a) Expansion. From k(theta) = 1 - theta^2/2 + theta^3/(3 pi) + theta^4/24 + O(theta^5) and cos F = k:
    F(theta) = theta - theta^2/(3 pi) - theta^3/(18 pi^2) + O(theta^4)
(checked: the remainder over theta^4 is -0.0077 at theta = 0.01, 0.03, 0.1). Hence with u = 1/theta,
    u_(l+1) = u_l + 1/(3 pi) + 1/(6 pi^2 u_l) + O(u_l^-2),   u_l = l/(3 pi) + log(l)/(2 pi) + c(theta_0) + o(1),
with c(theta_0) finite (computed: 4.40, 0.718, 0.484 for theta_0 = 0.2, 1.0, 1.5, stable from l = 10^3 to 10^4; beyond 10^5 the
float arccos near 1 drifts). So two pairs differ in 1/theta_l by a bounded amount, and theta_jk,l / thetamax_l = 1 + O(1/l).
(b) Limit. With all angles equal to s, Cbar = (1 - cos s) I + cos s 11^T and lam_min = 1 - cos s = s^2/2 + O(s^4); a relative
perturbation O(1/l) of the angles moves the entries by O(s^2/l). So rho_l -> 1/2.
(c) Each rho_l > 0. Cbar_l is the correlation matrix of relu(g_1), ..., relu(g_p) for a centred Gaussian vector g whose coordinates are
pairwise not perfectly correlated (angles in (0, pi/2] after the first layer, since F(theta) > 0 for theta > 0; at the inputs, pairwise
non-parallel and non-antipodal). The functions w -> relu(w . v_j) of a Gaussian w are linearly independent when the v_j are pairwise
non-parallel (each is non-differentiable exactly on the hyperplane v_j^perp, and these hyperplanes are distinct; antipodal pairs are
excluded because relu(t) - relu(-t) = t), so Cbar_l is positive definite. This holds even for coplanar inputs, where Cbar_0 is singular.
(a)-(c) give inf_l rho_l = min(min over l <= l0 of rho_l, 1/2 - eps) > 0. With the bound above:
Theorem (p inputs, critical ReLU MLP, pairwise non-parallel, non-antipodal unit inputs; argument by agent A, needs a second
reader). For n >= n0 and L <= n, W2((h_L(x_1), ..., h_L(x_p))/sqrt n, GP/sqrt n) <= C(p, rho) sqrt(L/n), rho = inf_l rho_l.
The constant depends on the inputs only through rho, a scale-free shape number of the infinite-width chain, and not on how small
the angles are; it cannot be absolute for p >= 3 (inputs near one great circle give rho near 0 at the first layer). Whether the
cost actually feels 1/rho is what three_input_bures.py measures.

### 18 Oct 11:0x (agent A): first numbers from three_input_bures.py (nearly coplanar inputs 0.2, 1.0, 1.1999; rho = 0.0085)
40 reps; n/L x E[cost]:
  n 100: L 10 / 25 / 50 / 100 -> total 2.82 / 3.45 / 2.67 / 2.78; correlation part 0.124 / 0.070 / 0.011 / 0.008; radial 2.70 / 3.41 / 2.67 / 2.77
  n 200: L 20 / 50 / 100      -> total 2.45 / 2.87 / 3.01;        correlation part 0.046 / 0.019 / 0.005;         radial 2.41 / 2.85 / 3.01
The total is O(L/n) with a constant near 3, and it is all radius: the correlation part is 20 to 500 times smaller, falls with L/n
rather than staying flat, and shows no sign of the 1/rho = 118 the bound allows. Correction on rereading the bound itself: the
1/rho term carries a factor thetabarmax_L^2 that the 11:0x statement dropped. From ||C - Cbar||_F <= 5 thetabarmax^2 |e| and
lam_min(Cbar_L) = rho_L thetabarmax_L^2, the correlation part is at most 25 thetabarmax_L^2 E|e|^2 / rho_L <= C thetabarmax_L^2 (L/n) / rho_L,
and only layer L enters (van Hemmen-Ando is applied once, at the output), so the inf over l is not needed:
    W2^2 <= C p^2 L/n  (radius)  +  C p^2 (thetabarmax_L^2 / rho_L) L/n  (correlation),
with thetabarmax_L ~ 3 pi / L and rho_L -> 1/2. The correlation part therefore vanishes relative to the radial part as L grows,
which is what the table shows (n/L x correlation part falls 0.12 -> 0.008 from L = 10 to 100 at n = 100); the small rho of
nearly coplanar inputs only matters at shallow depth, where thetabarmax_L^2/rho_L is (0.16)^2/0.0085 ~ 3 at L = 10 against a
measured 0.12. The theorem's constant is C(p) for L >= L0(inputs), and C(p, rho) only below it. Generic configuration and n = 400
still running.

### 18 Oct 11:4x (agent A): n = 400 (nearly coplanar inputs) - the correlation part scales as thetabarmax_L^2 L/n
n = 400, 40 reps, n/L x E[cost]: L 40 / 100 / 200 -> total 5.29 / 1.85 / 2.18; correlation part 0.0374 / 0.0063 / 0.0012; radial 5.26 / 1.84 / 2.18.
Dividing every correlation-part entry (n = 100, 200, 400; L = 10 to 200) by thetabarmax_L^2, the largest pairwise angle of the exact
infinite-width chain at depth L (iterating F from 0.2, 1.0, 1.1999; it runs 0.48 at L = 10 down to 0.044 at L = 200, a factor 117 in the
square), gives (n/L) E[corr] / thetabarmax_L^2 = 0.48 to 1.11 at all eleven points, with no trend in n or L beyond the noise. So the
correlation part is about 0.5-1 x thetabarmax_L^2 x L/n, which for L large is about 9 pi^2 (0.5-1) / (nL): it falls like 1/(nL), not L/n.
That is the shape the corrected bound gives (C thetabarmax_L^2 (L/n) / rho_L), with the 1/rho_L factor absent in the data; the whole
O(L/n) rate at p = 3 is carried by the radii. The generic configuration is next in the same run.

## 18 Oct 12:3x (agent A): the independent review, and the obtuse first step it asked for
agent C refereed lines 124-305 (rows/T250/reviews_agent_C/T250_REVIEW.md): p = 2 PASS for theta0 in (0, pi/2],
C absolute; p >= 3 PASS for pairwise angles in (0, pi/2]. Two rewordings, both made: lemma (ii) now bounds
|E[log theta' - log F(theta) ; G]| (above), and the chain uses E[. | F_(l-1), G_l] with the stopping time at the first layer where
|T| < 2 (remark (3) of the reread). The rigour nit is fixed too: concavity_proof.py now encloses every coefficient exactly (each
rational part as an interval quotient of two integers, pi as iv.pi) instead of rounding to 70 digits; rerun
(concavity_proof_enclosed.txt): lowest power 3, num/t^3 > 12.54 on [0, 1/4], H > 0 on 115 boxes of [1/4, pi/2] (min 9.5e-4), PROVED.

The first broken step was "uniformly in the starting angle": for an obtuse input pair the first transition is outside lemma (ii).
From layer 1 on every angle lies in [0, pi/2] (nonnegative vectors), so only that one step is missing. It is:

Lemma (ii'). For n >= n0 and every theta0 in [pi/2, pi], with theta1 the angle between relu(x) and relu(y), (x_i, y_i) iid
standard normal pairs of correlation cos theta0, and G' = {|S| >= n/8, |x|^2 <= 2n} (S below; P(G'^c) <= e^(-cn)):
|E[log theta1 - log F(theta0) ; G']| <= C/n  and  E[(log theta1 - log F(theta0))^2 ; G'] <= C/n,  C and n0 absolute.
(A good event is needed, as in lemma (ii): theta1 = 0 has positive probability at every n - e.g. relu(y) = 0, or exactly one
coordinate both-positive and the rest of one sign - so E log theta1 = -inf without it. The first version said "no good event
needed"; corrected on the second reading by agent C, 12:4x. The chain stops at layer 1 on G'^c as it does on G_l^c.)
Proof. Lower tail. Let S = {i : x_i > 0, y_i <= 0}. relu(y) vanishes on S, so relu(x)_S is orthogonal to relu(y) and
sin theta1 = |P_perp(relu y) relu x| / |relu x| >= |x_S| / |x|. Each i lies in S with probability theta0/(2 pi) >= 1/4. So
P(|S| < n/8) and P(|x|^2 > 2n) are <= e^(-cn), and given S the x_i, i in S, are independent with density at most phi(0) / P(S) <= 4 phi(0) on (0, inf) (x conditioned on
x > 0, y <= 0), so P(x_i^2 <= s) <= C sqrt(s) and the small-ball bound P(|x_S|^2 <= 2 n eps^2) <= (C eps^2)^(n/16) holds for |S| >= n/8. Hence on G', P(theta1 <= eps ; G') <= (C eps)^(n/8), and
E[(log theta1)^2 ; theta1 <= delta, G'] <= C e^(-cn) for a fixed delta < F(pi/2) / 2, uniformly in theta0. Bulk. theta1 = arccos(M / sqrt(A B)) with A, B, M the averages of
relu(x_i)^2, relu(y_i)^2, relu(x_i) relu(y_i): sub-exponential summands with absolute psi_1 norms, means 1/2, 1/2 and cos F(theta0) / 2.
cos F(theta0) lies in [0, 1/pi] on [pi/2, pi], so on the ball |(A, B, M) - mean| <= eps0 the cosine (nonnegative, the vectors are) stays in [0, 1/2], arccos lies
in [pi/3, pi/2], and Psi = log arccos(M / sqrt(A B)) is C^2 with absolute bounds. Taylor on the ball plus Bernstein off it gives
bias and variance C/n exactly as in lemma (ii); off the ball |log theta1 - log F| is controlled by the lower tail above and by
theta1 <= pi/2. QED.
Measured (obtuse_first_step.py, 20,000 reps, n = 100/400/1,600): n * bias in [-0.52, 0], n * var in [0, 0.41], largest at
theta0 = pi/2 and falling to 0 at the antipodal pair (where theta1 = pi/2 exactly: the supports of relu(x) and relu(-x) are disjoint);
the inequality sin theta1 >= |x_S|/|x| never failed and is tight at theta0 = pi; the smallest theta1 seen was 0.86.

So the theorems now read: p = 2, W2 <= C sqrt(L/n) for every input angle in (0, pi], C absolute; p >= 3, for every set of pairwise
non-parallel inputs (antipodal pairs excluded only where lam_min(Cbar) needs them excluded), with the constant through rho = inf_l
lam_min(Cbar_l) > 0 as before. The constant does not degrade near antipodal pairs: that is the deterministic case. Status: the
obtuse step had its second reading (agent C, 12:4x): PASS with the good event G' added, which is now in the statement.

### 18 Oct 12:3x (agent A): generic three inputs finished (three_input_bures_run1.txt, rho_min 0.4685)
n = 400: n/L * E[Bures^2(C, Cbar)] = 0.0258, 0.0055, 0.0020, 0.0004 at L = 40, 100, 200, 400 - the correlation part dies with depth
like thetabarmax_L^2 (a factor 64 over a tenfold L), and W2 is the radial part, n/L * E sum (r_j - 1)^2 = 3.5, 3.7, 6.8, 5.4 (the last
two at L/n = 1/2 and 1 and noisy, +-3), where the one-input radius chain is no longer in its linear regime.


Referee's final verdict (agent C, mesh 18 Oct 12:56): PASS - p = 2 for every input angle in (0, pi], C absolute; p >= 3 as stated above, with G' in lemma (ii').

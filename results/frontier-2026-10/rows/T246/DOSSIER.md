# T246 The law of input-output Jacobians of deep random networks with general activations

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (titles and dates
checked 16 Oct 06:4x).

## STATEMENT
Kept as listed: Hanin-Nica prove for ReLU with He initialization that the squared Jacobian (and gradient) norm is
approximately log-normal with log-variance proportional to sum_l 1/n_l. Prove the analogue for smooth activations (tanh,
GELU) at criticality, and determine the limiting law of the Jacobian's singular-value spectrum when L, n -> infinity with
L/n -> t.
Comment: the two parts are of different kinds. The squared norm |J u|^2 for a fixed vector u is a scalar process along the
layers, and the log-normal law is a CLT for its log; for smooth activations the forward pass enters the derivative matrices
D_l, which correlate with the weights already used, so the layer increments are not independent. The whole spectrum at
L/n -> t is the T247 question (free probability in the joint limit), here for Gaussian weights and smooth activations.

## FRONTIER
- Hanin, Nica arXiv:1812.05994: ReLU, the log-normal law for gradient and Jacobian norms with variance proportional to
  sum 1/n_l, via products of random matrices with random diagonal masks.
- Pennington, Schoenholz, Ganguli arXiv:1711.04735: free-probability spectrum of J at fixed depth assuming freeness
  (see T247).
- Pastur, Slavin arXiv:2011.11439 and Collins, Hayase arXiv:2103.13466: asymptotic freeness of the layer Jacobians at fixed
  depth (iid and Haar-orthogonal cases).
- Open: the smooth-activation log-normal law; the spectrum at L/n -> t.

## ARCHITECTURE
For |J u|^2 = prod_l |D_l W_l v_(l-1)|^2 / |v_(l-1)|^2 (v the normalized propagated vector), each factor is 1 + O(n^(-1/2))
with mean 1 at criticality (chi = 1). For ReLU the factors are independent given the masks' independence from the
direction; for smooth phi, D_l depends on the preactivations h_l = W_l x_(l-1), which share W_l with the factor. Conditioning
on the forward pass, each factor is a quadratic form in W_l with a covariance set by the empirical distribution of h_l, and
that empirical distribution concentrates at rate n^(-1/2) around its mean-field value.

## FAILURE POINT
Controlling the dependence between the forward pass and the backward factor over L ~ t n layers: the per-layer correlation
is O(1/n) and harmless, but its accumulation over t n layers is O(t), the same order as the log-variance itself, so it must
be computed, not bounded.

## SHAPE
Weeks for the smooth-activation log-normal law with an explicit variance; months for the full spectrum.

## OBSTRUCTION
Accumulated forward-backward correlations of the same order as the signal. Moves: write the log-norm as a martingale in the
layer index with the forward pass in the filtration, and compute the quadratic variation including the O(1/n) correlation
term; tanh at the critical point where the mean-field fixed point is q* = 0 (the simplest smooth case).

## TARGETS
1. tanh at criticality (sigma_w = 1, sigma_b = 0): prove log |J u|^2 is asymptotically N(-s^2/2, s^2) with s^2 = c t, and
   compute c (compare with ReLU's constant).
2. Measure the log-variance against L/n for tanh and GELU at n = 128, L = 16..512, to see the constant before proving.
3. The spectral question as a corollary of T247 once freeness in the joint limit is available.

## MEASUREMENT AND FIRST-ORDER CONSTANT 2026-10-17 (agent A): Targets 1 and 2 for tanh, and where the excess comes from
Files beside this dossier: jac_tanh.py, jac_pred.py, jac_qwalk.py, jac_untied.py, jac_scalar.py and their outputs jac_run1.txt ..
jac_run4.txt, jac_scalar_run1.txt.

Setting. Deep tanh net, sigma_w = 1, sigma_b = 0, Gaussian weights, |x_0|^2 / n = 1, a fixed unit input direction u;
log |J u|^2 over B = 400-1000 independent networks per (n, L), t = L/n.

Result 1 (Target 2, the measured law). n Var log|Ju|^2:
    n = 64:   L = 16 .. 256:  44.9  84.5  158.0  302.9  553.6      (t = 0.25 .. 4)
    n = 128:  L = 16 .. 256:  46.2  91.2  174.4  306.9  570.4      (t = 0.125 .. 2)
    n = 256:  L = 32 .. 256:  85.9 157.8  330.9  688.0              (t = 0.125 .. 1)
(standard error about 4.5 percent at B = 1000). Skewness and excess kurtosis are within +-0.25 at every point, and the mean
sits below the mean-field drift sum_l log m2(q_(l-1)) by about Var/2 (n = 256, L = 256: -1.458 against -1.344), so the law is
log-normal to the accuracy of the runs. Var n / L is 2.7-2.9 for t <= 0.5 and falls to 2.2 at t = 4.

Result 2 (the independent-layer prediction misses a term of the same order). If each factor |v_l|^2/|v_(l-1)|^2 =
(1/n) sum_i sech^4(h_i) g_i^2 is taken with h_i iid N(0, q_(l-1)) at the mean-field q (q_l -> 0 like 1/(2l)), the per-layer
variance is (3 m4/m2^2 - 1)/n -> 2/n and n Var = 2L + 4.2 (35.8, 68.0, 132.1, 260.1, 516.2 at L = 16 .. 256). The runs
exceed this by 9-170, growing linearly in L. Untying the backward weights from the forward ones (W' independent of W in
v <- phi'(h) (W' v)) does not remove it: n Var = 44.5 +- 2.0 at n = 128, L = 16, against 46.2 tied. So the excess is not the
weight-sharing correlation the FAILURE POINT names.

Result 3 (the cause: the forward norm is a random walk, and the backward factors read it). The empirical forward variance
qhat_l = |x_l|^2/n obeys qhat_l = F(qhat_(l-1)) + xi_l with F(q) = E tanh^2(sqrt q z) and Var xi_l = Var tanh^2 / n, and each
backward factor has mean m2(qhat_(l-1)), not m2(q_(l-1)). To first order in 1/n,
    log|J u|^2 - drift = sum_k (G_k xi_k + eta_k),   G_k = sum_(l>k) (log m2)'(q_(l-1)) prod_(k<=j<l-1) F'(q_j),
with Var eta_k = (3 m4/m2^2 - 1)/n and Cov(xi_k, eta_k) = Cov(tanh^2, sech^4)/(n m2) (both read the same h_k). Evaluated by
quadrature (jac_qwalk.py), n Var = independent + walk + cross:
    L = 16:  35.84 + 4.67 + 4.15 = 44.66        L = 128: 260.14 + 70.96 + 11.25 = 342.36
    L = 32:  68.01 + 12.82 + 6.29 = 87.12       L = 256: 516.17 + 153.15 + 13.90 = 683.22
    L = 64: 132.10 + 31.32 + 8.69 = 172.11      L = 512: 1028.18 + 320.60 + 16.61 = 1365.39
against the runs at t <= 0.5: 44.9-46.2, 84.5-91.2, 157.8-174.4, 330.9, and 688.0 at n = 256, L = 256 (t = 1). No parameter is
fitted. The walk term is linear in L: with q_l ~ 1/(2l), F'(q) ~ 1 - 2/l and (log m2)'(q) ~ -2, the sum is
sum_k xi_k (k - k^2/L) up to the factor -2, and Var xi_k ~ 2 q_k^2 / n gives Var = 4 sum_k (1 - k/L)^2 / (2n) ~ 2L/(3n);
the cross term grows like log L. Hence, to first order in t,
    Var log|J u|^2 = (8/3) t (1 + o(1)),   c = 2 + 2/3 = 8/3,
against c = 5 for ReLU with He initialization (Hanin-Nica: per layer Var(2 B g^2) = 5, B Bernoulli(1/2)). Two thirds of a unit
of the constant comes from the forward pass and none from the forward-backward weight correlation.

What this leaves for Target 1. The martingale route in OBSTRUCTION works with the filtration of the forward pass, but the
quadratic variation must include the predictable drift term sum_l [log m2(qhat_(l-1)) - log m2(q_(l-1))], a functional of the
forward random walk, not a correction of size O(1/n) per layer. The proof is a two-component CLT for (qhat_l, log|v_l|^2):
a linear recursion with slowly varying coefficients, driven by a martingale-difference sequence with the covariance above.
At t of order one the linearization fails (the relative fluctuation of qhat is about sqrt(2t/3)), and the measured Var n/L
falls below 8/3 (2.4 at t = 2, 2.2 at t = 4); in the variable 1/qhat, which grows by 2 per layer, the walk is additive, which
suggests the nonlinear limit is tractable.

Result 4 (controls that isolate the mechanism, jac_untied.py and jac_scalar.py). Three variants, n Var log|Ju|^2:
    untied backward weights, n = 128, L = 16 .. 256:   44.5  87.4  154.0  316.4  627.6   (+- 4.5 pct; tied 46.2 91.2 174.4 306.9 570.4)
    mean-field forward variance, n = 128, L = 16:      34.3 +- 1.5   (independent-layer prediction 35.8)
    scalar chain, n = 64, L = 16 .. 256, B = 20000:    45.5  87.6  169.3  325.5  608.6   (+- 1 pct)
The untied network carries the whole excess. Replacing qhat_(l-1) by the deterministic q_(l-1) in the backward factors
(mode meanfield) removes it: the variance falls to the independent-layer value. The scalar chain keeps only qhat and the
shared h of each layer (no matrices, no directions) and reproduces the network within its noise at t <= 1 (45.5 / 87.6 /
169.3 against 44.9-46.2 / 84.5-91.2 / 157.8-174.4) and the first-order prediction at t <= 0.5. At t = 2 and 4 the chain
gives n Var / L = 2.54 and 2.38, below 8/3 and above the network at n = 64 (302.9, 553.6 against 325.5, 608.6, 1.5 and 2
standard errors), so the nonlinear correction at t of order one is already present in the two-component recursion; it is the
object to analyse for Target 1, in the variable 1/qhat.

## ADDENDUM 2026-10-17 (agent A): the mean-field control at every depth (jac_run4.txt, complete)
With the backward factors fed the deterministic q_(l-1) instead of the empirical qhat_(l-1) (everything else the network),
n = 128, B = 1000: n Var log|Ju|^2 = 34.3, 65.2, 134.9, 267.2, 546.6 at L = 16, 32, 64, 128, 256, against the independent-layer
value 35.8, 68.0, 132.1, 260.1, 516.2 (differences -1.0, -1.0, +0.5, +0.6, +1.2 standard errors). The whole excess of Result 2
goes with the forward-norm walk, at every depth measured.

## ADDENDUM 2026-10-17 (agent A): ReLU control and tanh at t = 2, n = 256 (jac_run3.txt)
ReLU with He initialization, n = 128, B = 1000: n Var log|Ju|^2 / L = 5.09, 5.00, 5.01, 5.23, 5.19 at L = 16 .. 256, the
Hanin-Nica constant 5 with no excess. The same code therefore finds no forward-walk term where the layer factor does not
depend on the forward norm (phi' of ReLU is scale-free), and finds one for tanh, where it does. Tanh, n = 256, L = 512
(t = 2), B = 400: n Var = 1163.8, n Var / L = 2.27 (first order 1365.4, i.e. 2.67), skewness +0.04, excess kurtosis -0.13;
the first-order constant 8/3 holds only for t up to about 1, as in Result 4.

Scalar chain at n = 256 (jac_scalar_run2.txt, B = 8000, standard error about 1.6 percent): n Var log|Ju|^2 = 85.2, 165.8,
335.6, 651.9 at L = 32, 64, 128, 256 (t = 0.125 .. 1), against the network at the same n (85.9, 157.8, 330.9, 688.0, about
4.5 percent each) and the first-order values (87.1, 172.1, 342.4, 683.2). The chain sits 2-4 percent below first order already
at t = 0.125-0.5 (1.3 to 2.4 of its standard errors) and 4.6 percent below at t = 1, so the correction to (8/3) t is negative
and of order t at small t, not only a large-t effect; the network agrees with the chain within its own noise at every L.

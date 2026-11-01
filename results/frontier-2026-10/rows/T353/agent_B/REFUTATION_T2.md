# T353: an adaptive query method beats the conjectured shuffle pair at T = 2

agent B, 19 Oct 2026. Status: REFUTED for every T >= 2 at s = 1, eps = 1/2. Rigorous certificates (Arb ball arithmetic)
at T = 2 (cert_t2_arb.py) and T = 3 (cert_t3_arb.py); every T >= 3 follows from the T = 3 certificate by the reduction in the section
"Every T". T = 2: two independent audits CONFIRMED (agent C, ../AUDIT_agent_C.md; agent A,
../AUDIT_agent_A.md, whose own Arb proof of the one-point inequality is ../audit_A/rigorous_point.py). T = 3: two
audits CONFIRMED (agent A, ../AUDIT_T3_agent_A.md; agent C, ../AUDIT_T3_agent_C.md). The reduction to
every T: two audits CONFIRMED (agent A, ../AUDIT_TGEN_agent_A.md; agent C, the same AUDIT_T3 file, with
../audit_C/every_t_check.py).

## The claim

Chua, Ghazi, Kamath, Kumar, Manurangsi, Sinha (arXiv:2403.17673, Conjecture 3.2) conjecture that

    P_S = (1/T) sum_t N(2 e_t, s^2 I_T),   Q_S = (1/T) sum_t N(e_t, s^2 I_T)

tightly dominates shuffled ABLQ (zero-out adjacency, n = bT, one epoch, unit-bounded queries) for every
adaptive query method. For T = 2, every batch size b, d = 1, s = 1 and eps = 1/2 there is an adaptive query method
and an adjacent pair x, x' with

    D_{e^eps}(M(x) || M(x')) > max( D_{e^eps}(P_S || Q_S), D_{e^eps}(Q_S || P_S) ),

so (P_S, Q_S) does not dominate ABLQ_S. Numerically 0.22324 against 0.22127 (and 0.20510 for the reverse order).
On a 9^4 grid the best NON-adaptive method is the conjectured one (0.221273), so the gain is from adaptivity.

## The construction

X = {u, w}. Record i holds u (x) or bottom (x'); the other n - 1 = 2b - 1 records all hold w. Step 1:
psi_1(u) = -1, psi_1(w) = +1. Step 2, after seeing g_1 (shifted by the others' known total): if g_1 lies in a set
S, psi_2(u) = psi_2(w) = +1 (SAME); otherwise psi_2(u) = +1, psi_2(w) = -1 (ANTI, the conjectured answers).
With S empty this is the conjectured pair (a sign flip of coordinate 1, which preserves every divergence).

Subtract b*psi_t(w) from g_t. With all others equal, the batch holding i is the only one that differs, and the
outputs are, writing B for "i is in batch 1" (probability 1/2):

    x  : B -> (g1, g2) ~ N(-2, s^2) x N(0, s^2);   not B -> N(0, s^2) x N(a2 - v2, s^2)
    x' : B -> (g1, g2) ~ N(-1, s^2) x N(0, s^2);   not B -> N(0, s^2) x N(-v2, s^2)

(ANTI: a2 - v2 = 2, -v2 = 1; SAME: 0 and -1). b drops out, so one example serves every b.

## Why it is enough to look at one point

The hockey-stick divergence is int dg1 I(g1), where I(g1) = int (p(g1, g2) - e^eps q(g1, g2))_+ dg2 depends on the
step-2 query only through the answers chosen at that g1. The adversary may choose SAME on any measurable set S, so
if I_SAME(g1*) > I_ANTI(g1*) at one point, continuity gives an interval S around g1* on which SAME wins, and the
total strictly exceeds int I_ANTI = D(P_S || Q_S).

Coordinates: the point values below are in the shifted coordinate g1 - b psi_1(w) of the model above. The scripts
exact_closed.py and cert_t2_arb.py use the raw b = 1 model of t2b1_adaptive.py, where the same point is g1 = -3/2.

At s = 1, eps = 1/2 (the inner set {p > e q} is read off the roots of a quadratic in t = exp(g2/s^2), so I is a sum of
normal CDF differences; exact_closed.py at 30 digits, cert_t2_arb.py in Arb at 200 bits, the two agree to every digit):

    shifted g1 = -2.5:  I_ANTI = 0.0635779652453   I_SAME = 0.0641560879254   difference +5.78e-4
    shifted g1 = -3.0:  difference +4.53e-6;  shifted g1 >= -2: SAME is no better.

Rigorous version (cert_t2_arb.py, cert_t2_arb.txt): the closed form is evaluated on 5000 balls covering raw g1 in
[-1.6, -1.1] (shifted [-2.6, -2.1]); every ball gives I_SAME - I_ANTI > 0, with smallest lower end 2.08e-4. So the
method "SAME on that interval, ANTI elsewhere" has

    D_{e^eps}(M(x) || M(x')) >= D_{e^eps}(P_S || Q_S) + 1.04e-4,

with no appeal to continuity and no quadrature. Controls: the same code refuses the interval [-0.9, -0.5], where SAME
loses by 7e-3, and fails closed (no verdict) on balls near raw g1 = -1, where a coefficient of the quadratic vanishes.
Definition 2.3 of the paper fixes the orientation (x holds the record) and asks for every eps, so this alone breaks
the conjecture.

The adaptive value also beats the reverse order, D(Q_S||P_S) = 0.20510 (numerical, both audits).

## Checks

1. t2b1_adaptive.py (grid, pointwise argmax over a 9x9 step-2 grid, both orders, 9x9 step-1 grid): 0.223264 at
   N = 401, 0.223240 at N = 801; the conjectured pair 0.221273 by a 2-D integral and 0.221271 through the same
   pointwise integrator (check1.py).
2. exact_closed.py: the one-point inequality above in closed form; pointwise_mp.py (mpmath quad) agrees to 1e-8.
3. nonadaptive.py: best non-adaptive on 9^4 = conjectured, at (s, eps) = (1, 0.5), (1, 1), (0.5, 1).
4. threshold_quad.py (scipy, the threshold policy S = (-inf, c)), sweep1 (s in {0.5, 1, 2} x eps), renyi2.py (the
   Renyi-2 version): see the run files beside this note.

## T = 3

t3_dp.py computes the adaptive optimum exactly as a nested maximum (step-3 answers pointwise in (g1, g2), step-2 answers
pointwise in g1), step 1 fixed at (-1, 1), answers in {-1, 1}^2, trapezoid grids. t3_mc.py is a Monte Carlo control for
the conjectured pair (4 x 10^6 draws).

    s = 1, eps = 1/2     conjectured D(P_S||Q_S)          adaptive          gain
    N = 61,  M = 201     0.207476                          0.210451          +2.98e-3
    N = 121, M = 401     0.207611                          0.210464          +2.85e-3
    Monte Carlo          0.207652 +- 0.000143
    reverse order Q||P   0.181424 (N 61; MC 0.181193 +- 0.000122), adaptive 0.189504

The gain is larger relative to the conjectured value than at T = 2 (1.4 per cent against 0.9).

Rigorous version at T = 3 (cert_t3_arb.py, cert_t3_arb.txt). Take the conjectured answers at steps 1 and 2 and at step 3
on every (g1, g2) outside a box B; inside B answer SAME (1, 1) at step 3. With all steps ANTI the output law is (P_S, Q_S)
up to a sign flip of coordinate 1, and only the g3 factor depends on the step-3 answers, so

    D(switch on B) = D(P_S || Q_S) + int_B (I3_SAME - I3_ANTI) dg1 dg2,

where I3 = int (p - e q)_+ dg3 is again a sum of Phi differences between the roots of a quadratic in t = e^{z}. On
B = [-0.1, 0.3] x [2.2, 2.3] (shifted coordinates of t3_dp.py) the closed form is evaluated in Arb at 128 bits on 21,539
balls (adaptive four-way splitting); every ball gives I3_SAME - I3_ANTI > 0, hence

    D_{e^eps}(M(x) || M(x')) >= D_{e^eps}(P_S || Q_S) + 2.25e-5   at T = 3, s = 1, eps = 1/2, every b.

The box is small on purpose; the numerical gain of the step-3 switch alone over its whole winning region is 1.93e-3
(t3_step3.py). Cross-check (cert_t3_crosscheck.txt): the Arb inner difference and the grid code agree to seven digits at
(0.1, 2.2), (-0.5, 2.4) and (0, 1.8), the last a point where SAME loses (-2.14e-3).

## Every T

Answer as conjectured at steps 1, ..., T - 1 and choose SAME or ANTI at step T from the prefix g = (g_1, ..., g_m), m = T - 1
(coordinates sign-normalised so the conjectured answers give means 2 under x and 1 under x' in the batch holding the record). If the
record sits in batch t <= m, the last coordinate is N(0, 1) under both datasets whatever step T answers; if it sits in batch T, the
prefix is N(0, I_m) under both and the last coordinate has means (2 | 1) for ANTI and (0 | -1) for SAME. So the last-step inner
integral I(g) = int (p - e^eps q)_+ dg_T has weights

    alpha = (1/T) sum_t phi(g_t - 2) prod_{s != t} phi(g_s),   gamma = (1/T) sum_t phi(g_t - 1) prod_{s != t} phi(g_s),
    beta  = (1/T) prod_t phi(g_t),

and is homogeneous of degree 1 in (alpha, beta, gamma). With x_t = exp(g_t - 1/2), alpha/beta = A = e^{-1} sum x_t^2 and
gamma/beta = G = sum x_t, so I_SAME(g) - I_ANTI(g) = beta * Delta(A, G) for one function Delta of two variables, the same for every T.
For m = 1 the pair (A, G) lies on the curve e A = G^2 (this is the T = 2 problem); for m >= 2 it ranges over G^2 / m <= e A < G^2 (the lower end at
equal x_t), whose interior is the open region G^2 / m < e A < G^2, and the map g -> (A, G) is a submersion off the diagonal x_1 = ... = x_m.

On the T = 3 box B the ratio x_2/x_1 = exp(g_1 + g_2) lies in [e^{2.1}, e^{2.6}], so e A / G^2 = (1 + r^2)/(1 + r)^2 lies in
[0.806, 0.871]. The T = 3 certificate gives Delta > 0 on the image U of the interior of B, an open set (the m = 2 map is a local
diffeomorphism there) inside G^2 / 2 < e A < G^2. For any m >= 2, U lies in the open region the prefix reaches, so its preimage
is a nonempty open set S_T of prefixes, of positive Gaussian measure, and the step-T switch on S_T gives

    D_{e^eps}(M(x) || M(x')) >= D_{e^eps}(P_S || Q_S) + int_{S_T} beta Delta > D_{e^eps}(P_S || Q_S),   every T >= 3, every b.

Numbers (tgen_mc.py, Monte Carlo with 2 x 10^6 prefixes, D = (1/T) E_{g ~ N(0, I_m)} I_ANTI and gain = (1/T) E Delta_+ by the same
homogeneity). Controls: T = 2 gain 1.9703e-3 +- 1.2e-5 against the closed form 1.96602e-3; T = 3 gain 1.9100e-3 +- 9e-6 against
t3_step3.py's grid value 1.93e-3; the identity I_SAME - I_ANTI = beta Delta agrees with cert_t3_arb.diff to 1e-15 at six points
(tgen_identity_check.txt).

    T     D(P_S||Q_S)          last-step switch gain
    4     0.1937 +- 0.0016     1.646e-3 +- 7e-6
    5     0.1838 +- 0.0016     1.404e-3 +- 6e-6
    6     0.1767 +- 0.0022     1.192e-3 +- 5e-6
    8     0.1631 +- 0.0013     8.84e-4  +- 4e-6
    10    0.1549 +- 0.0012     6.86e-4  +- 3e-6
    16    0.1290 +- 0.0009     3.71e-4  +- 2e-6
    32    0.0959 +- 0.0008     1.27e-4  +- 7e-7

The gain from the last step alone falls like T^{-1} at small T and close to T^{-1.5} between T = 16 and 32 (local slopes 1.4 to 1.55 there); switching at earlier steps as well can only add to it.

Other sigma at eps = 0.1 (tgen_mc.py with the sigma argument; x_t = exp((g_t - 1/2)/s^2), A = e^{-1/s^2} sum x_t^2, prefix
N(0, s^2 I_m); numerical only, the certificates are at s = 1, eps = 1/2). Controls at T = 2 against exact_closed.py
(ec_sweep.txt): s = 2 gain 4.656e-3 +- 9e-6 against 4.6647e-3; s = 0.5 gain 7.09e-5 +- 1.9e-6 against 7.217e-5.

    T     s = 2: last-step gain     s = 0.5: last-step gain
    2     4.656e-3 +- 9e-6          7.09e-5 +- 1.9e-6
    3     3.385e-3 +- 7e-6          9.43e-5 +- 1.8e-6
    4     2.490e-3 +- 5e-6          9.96e-5 +- 1.6e-6
    8     1.028e-3 +- 2e-6          1.061e-4 +- 1.1e-6
    16    3.72e-4  +- 9e-7          9.73e-5 +- 8e-7

At s = 0.5 the gain holds near 1e-4 up to T = 16 and then falls (tgen_bigT_s05.txt, 1e6 samples each):

    T     32         64         128        256        512
    gain  7.48e-5    4.83e-5    2.64e-5    1.26e-5    5.33e-6
    T*gain 2.39e-3   3.09e-3    3.38e-3    3.22e-3    2.73e-3

The plateau has a plain reason. x_t has log-standard-deviation 1/s and E x_t^2 = e^{1/s^2}, about 55 at s = 0.5, so
while m is well below that one large term dominates G and sum x_t^2 / G^2 stays of order one; the prefix lands in the
same part of the (A, G) region whatever T is, and the factor 1/T is offset. Once m passes e^{1/s^2} the ratio settles
near e^{1/s^2}/m and the gain decays roughly like 1/T. D(P_S || Q_S) itself stays near 0.55 over the same range, so the
excess of the last-step switch is relatively small at large T; a policy that switches at several steps may do better.

The T = 2 sweep over s in {0.5, 1, 2} and eps in {0.1, 1, 2, 3} (ec_sweep.txt) found a positive gain in all 12 cells.
The smallest are at s = 2: 7.6e-8 at eps = 2 and 5.2e-13 at eps = 3, where D(P_S || Q_S) is 2.3e-10 and SAME wins
only for g1 < -12.5 (the s = 2, eps = 3 cell needed findroot's residual check relaxed, see exact_closed.py).

## What an audit should try

- The paper's definition of a dominating pair for zero-out adjacency (Definition in Section 2): confirm the
  comparison is D(M(x)||M(x')) <= D(P||Q) with x the dataset holding the record, or the symmetric max; the example
  exceeds both.
- That b = 1 (n = T = 2) and b >= 2 are inside the conjecture's scope (the shift argument covers every b).
- A closed form for I(g1) by the roots of the two-Gaussian difference, to replace quadrature by interval bounds.
- Whether the gap persists for larger T (the same switch on the evidence of where i sits) and in the Renyi sense.

## Literature (read 19 Oct 2026)

- van Dijk and Ertan, arXiv:2605.06259 v3 (2 Oct 2026), Appendix J: under fixed-size shuffling and zero-out adjacency the
  scalar pair (N(0, I), mean_j N(e_j, I)) does not dominate, because the other samples' sums reveal the round; at M = 2,
  sigma = 1 they compute chi2(P_2(2) || P_1(2)) = e - 1 - 1/e + e^{-5/4} E[sech W] = 1.5895 against (e - 1)/2 = 0.8591.
  Their P_2, P_1 are Chua et al.'s P_S, Q_S, which they record as Conjecture 3.2, "which they leave open". Their
  counterexample is to a different (smaller) pair and is non-adaptive; it does not touch Conjecture 3.2.
- No paper found (searches 19 Oct) that proves or refutes Conjecture 3.2 for adaptive query methods. Feldman and
  Shenfeld (2025) settle the adaptive case for random allocation, a different sampler.

## Renyi order 2 (chi-square) fails too (19 Oct 2026 21:4x)

The same step-2 switch beats Chua et al.'s pair in chi-square, hence in Renyi divergence of order 2 (D_2 = log(1 + chi2) is
increasing in chi2). chi2(M(x) || M(x')) = int dg1 J(g1) - 1 with J(g1) = int p^2/q dg2, and only J depends on the step-2
answers at that g1, so the adaptive optimum is the pointwise maximum of J over SAME and ANTI.

- Numerically (chi2_adaptive.py, sigma 1, T 2, P||Q): conjectured pair 1.589482, which reproduces van Dijk-Ertan's closed
  form 1.5895 (arXiv:2605.06259 App. J); adaptive 1.591212; gain +1.729e-3; SAME wins for raw g1 in (-12, -1.45).
- Independent point values (chi2_point_mp.py, mpmath 30 digits): J_SAME - J_ANTI = +1.80412e-3 at g1 = -2, +1.478e-3 at -1.6,
  -2.79e-3 at -1.3.
- Rigorous (cert_chi2_arb.py, python-flint 0.9.0, 128 bits): writing rho = e^{g1 - 1/2}, each inner integral is a positive
  numerator over a denominator increasing in rho, so it is decreasing in rho, and on a g1 ball J_SAME is bounded below and
  J_ANTI above by evaluations at the ball's endpoints (acb.integral on [-16, 16] plus explicit Gaussian tails). On 200 balls
  covering [-2, -1.98], J_SAME - J_ANTI >= 1.5912e-3, so chi2(adaptive) >= chi2(P_S||Q_S) + 3.22e-5. The point value at
  g1 = -2 is 0.001804115767 +/- 6e-14, matching mpmath to 12 digits.

The chi-square result has two independent checks: this certificate and agent A's audit (rows/T353/AUDIT_CHI2_agent_A.md, from frontier/audits_A/,
CONFIRMED). It is verified.

## Other Renyi orders and KL at sigma 1, T 2 (numerical, 19 Oct 2026 22:1x)

renyi_alpha_grid.py takes D_alpha = log(int J_alpha dg1)/(alpha - 1) with J_alpha = int p^alpha q^(1-alpha) dg2, and for KL
J = int p log(p/q) dg2. Only J depends on the step-2 answers at that g1, so the adaptive optimum is again the pointwise maximum.
Trapezoid grid on g1 in [-16, 16] (1601 points) and g2 in [-24, 24] (9601). A wider grid ([-24, 24] by [-32, 32], 2401 by 13001)
gives the same seven digits. Control: the alpha = 2 row gives e^0.9514580 - 1 = 1.58948, the chi-square value above.

| order | P||Q pair | P||Q adaptive gain | Q||P pair | Q||P adaptive gain |
|---|---|---|---|---|
| KL | | +6.183e-4 | | +9.168e-4 |
| 1.5 | | +7.153e-4 | | +1.824e-3 |
| 2 | 0.9514580 | +6.676e-4 | 0.7941883 | +4.066e-3 |
| 3 | 1.4701620 | +3.488e-4 | 1.1263270 | +4.268e-2 |
| 5 | 2.4940383 | +2.063e-5 | 1.7252811 | +4.574e-1 |

At alpha = 10 the integrand overflows double precision; that order needs log-space arithmetic.

The large Q||P gains at high order are mostly not adaptivity. renyi_nonadaptive.py compares the pair (ANTI at every g1) with the
fixed query SAME at every g1, which uses no information from step 1:

| order | P||Q, SAME everywhere minus pair | Q||P, SAME everywhere minus pair |
|---|---|---|
| 2 | -2.966e-1 | -1.741e-1 |
| 3 | -2.936e-1 | -4.227e-2 |
| 4 | -2.264e-1 | +1.943e-1 |
| 5 | -1.730e-1 | +4.561e-1 |

So in the Q||P direction at orders 4 and above the conjectured pair is not dominating even among non-adaptive queries, and the
adaptive switch adds only 1.35e-3 on top at order 5 (2.1827309 against 2.1813793). In the P||Q direction the pair beats the fixed
SAME query at every order, and the adaptive gain is the whole story; it shrinks from 7e-4 at order 1.5 to 2e-5 at order 5,
because the SAME region moves out to g1 < -2.8, where step 1 has little mass. Whether a dominating pair for Renyi DP should be
judged in one direction or as the maximum of both is a convention; the counterexample holds under either, since both directions
gain at every order tested.

These numbers are grid values, not certificates. The chi-square certificate's monotone endpoint form should extend to integer
orders (p^alpha / q^(alpha-1) is again a positive numerator over a denominator increasing in rho); KL needs a different bound.

## Integer orders 3, 4, 5: certificates (19 Oct 2026 22:4x)

cert_renyi_int_arb.py extends the chi-square certificate to any integer order alpha >= 2 in the P||Q direction. With
rho = e^{g1-1/2} and al = e^{-g1-1/2},

    J_SAME = w0 (al + rho)^alpha IS(rho),     IS(r) = int N_1^alpha / (N_1 + r N_0)^(alpha-1),
    J_ANTI = w0 sum_k C(alpha,k) e^{(2k-alpha) g1 - alpha/2} A_k(rho),
             A_k(r) = int N_-1^(alpha-k) N_1^k / (N_-1 + r N_0)^(alpha-1).

Every integral decreases in r, so on a ball of g1 the SAME term is bounded below at rho(hi) and the ANTI terms above at rho(lo).
Integrals are acb.integral on [-30, 30] at 128 bits; the tails are bounded by Gaussian tails (in the script). Control: at order 2
the script gives J_SAME - J_ANTI = 1.80412e-3 at g1 = -2, the chi-square certificate's value.

| order | interval of g1 | balls | min of J_SAME - J_ANTI (lower end) | int J(adaptive) - int J(pair) >= |
|---|---|---|---|---|
| 3 | [-2.21, -2.19] | 100 | 0.010997 | 2.2074e-4 |
| 4 | [-3.01, -2.99] | 200 | 0.068407 | 1.3960e-3 |
| 5 | [-3.502, -3.498] | 100 | 0.94451 | 3.7922e-3 |

Since D_alpha = log(int J)/(alpha-1) is increasing in int J, the adaptive switch has strictly larger Renyi divergence than
Chua et al.'s pair at orders 2, 3, 4 and 5 (sigma 1, T 2, P||Q). In divergence units the certified excess is small (order 3:
at least 5.8e-6 against a grid excess of 3.5e-4), because the balls cover only a short interval; the pointwise difference is
positive on about [-4.5, -1.9] at order 3, [-4.5, -2.5] at order 4 and [-4.5, -3.0] at order 5 (scan in the script).

Balls of width 1e-3 failed at order 3 (lower difference -1.6e-3): the endpoint bound loses about 5.8 h J, which at J = 2.7 is more
than the pointwise gap 0.0139. Width 2e-4 leaves 0.011 of it.

Van Dijk and Ertan (2605.06259 v3, Appendix J) compute chi2(P_2^(2) || P_1^(2)) = 1.5895 for the same pair, and use it only to
show that their own scalar pair is not dominating; they do not ask whether Chua et al.'s pair dominates in Renyi divergence.
Their identity chi2(Q||P) + 1 = 2 int_0^inf H_lambda(Q||P) d lambda shows that a dominating pair in hockey-stick divergence
dominates in chi-square, so each Renyi certificate here is also a second proof that the pair is not dominating in hockey-stick.

## The Q||P direction at orders 2 and 3: certificates (19 Oct 2026 22:5x)

In Q||P the integrand is q^alpha / p^(alpha-1) and the ANTI denominator a N_-1 + rho N_1 moves with a = e^{-g1-1/2} and
rho = e^{g1-1/2} in opposite directions, so the endpoint form does not apply. cert_renyi_qp_arb.py instead passes g1 as an arb
ball into the integrand; every evaluation inside acb.integral then encloses all g1 in the ball. Tails beyond |z| = 30 are
bounded in the script. At g1 = -1 the order-2 integrals agree with scipy quadrature on the unscaled weights to nine digits
(J_SAME 0.102224949, J_ANTI 0.098766951).

| order | interval of g1 | balls | min of J_SAME - J_ANTI | int J(adaptive) - int J(pair) >= |
|---|---|---|---|---|
| 2 | [-0.6, -0.4] | 40 | 0.0069659 | 1.582e-3 |
| 3 | [0.4, 0.6] | 40 | 0.73738 | 0.15034 |

At order 3 the pair beats the fixed SAME query in Q||P (table above), so this gain is adaptivity. The audit of
cert_renyi_int_arb.py by agent A found no fault (AUDIT_RENYI_agent_A.md).

## KL in both directions: certificates (19 Oct 2026 22:5x)

KL is additive over the step-1 output, D(P||Q) = int dg1 K(g1) with K(g1) = int p log(p/q) dg2, so a pointwise gain of the
SAME switch in K is a gain in the divergence itself. cert_kl_arb.py uses the ball form of cert_renyi_qp_arb.py, with the
logarithm taken in Arb's analytic mode (a box that meets the branch cut is indeterminate and gets subdivided). Tails use
p - q <= p log(p/q) <= p^2/q - p. Controls against scipy at the unscaled weights: P||Q at g1 = -2, K_SAME - K_ANTI =
2.84833e-4 both ways; Q||P at g1 = -1.5, 4.71651e-4 both ways.

| direction | interval of g1 | balls | min of K_SAME - K_ANTI | KL(adaptive) - KL(pair) >= |
|---|---|---|---|---|
| P||Q | [-1.51, -1.49] | 40 | 4.906e-4 | 9.967e-6 |
| Q||P | [-1.51, -1.49] | 40 | 3.237e-4 | 6.724e-6 |

The grid excesses are 6.18e-4 (P||Q) and 9.17e-4 (Q||P); the certified ones are small because the interval is short. With the
sections above, at sigma 1 and T = 2 the adaptive switch beats Chua et al.'s pair, with a rigorous bound, at KL and Renyi orders
2 to 5 in P||Q and at KL and orders 2 and 3 in Q||P.

## Sigma sweep at T = 2, numerical (19 Oct 2026 23:1x)

renyi_alpha_grid.py at sigma 0.5 and 2 (trapezoid, g1 on [-(10s+2), 10s+2] with 1201 points, g2 with 8001; outputs
renyi_grid_s0.5.txt, renyi_grid_s2.txt). Adaptive minus pair:

| sigma | direction | KL | order 2 | order 3 |
|---|---|---|---|---|
| 2 | P||Q | +1.82e-3 (of 0.0867) | +3.57e-3 (of 0.180) | +5.15e-3 (of 0.281) |
| 2 | Q||P | +1.88e-3 (of 0.0840) | +4.06e-3 (of 0.164) | +7.11e-3 (of 0.240) |
| 0.5 | P||Q | +2.8e-8 (of 1.995) | +2.1e-9 (of 4.000) | +1.2e-11 (of 6.000) |
| 0.5 | Q||P | +1.1e-7 (of 1.948) | +2.5e-4 (of 3.637) | +0.604 (of 5.028) |

At sigma 2 every gain is large against the grid error. At sigma 0.5 the P||Q gains are small but stable: with g2 on 16001
points (renyi_grid_s0.5_n16001.txt) every gain is unchanged to four digits, and the order-2 gain converted to chi2,
e^{D_2} dD_2 = 54.58 x 2.067e-9 = 1.128e-7, matches chi2_adaptive.py's adaptive quadrature (1.129e-7, chi2.json). The order-3 Q||P gain at sigma 0.5 is mostly the fixed SAME query, as at sigma 1.

## KL at sigma 2: certificates (19 Oct 2026 23:2x)

cert_kl_arb_sigma.py is cert_kl_arb.py with the noise scale as an argument. Every density becomes N(., mu, s); the tail bounds
carry over through N(z, m1)^2 / N(z, m2) = exp((m1 - m2)^2 / s^2) N(z, 2 m1 - m2), so E = exp(1/s^2) and each tail Gaussian keeps
its centre in [-2, 2], with Mills' bound 2 s^2 N(L - 2; 0, s)/(L - 2) at L = 30 s. At sigma 1 it reproduces cert_kl_arb.py digit
for digit (P||Q g1 -2: 2.84833e-4; Q||P g1 -1.5: 4.71651e-4). At sigma 2 scipy agrees at g1 = -2 (7.86349e-4 P||Q, 7.94134e-4 Q||P).

| sigma | direction | interval of g1 | balls | min of K_SAME - K_ANTI | KL(adaptive) - KL(pair) >= |
|---|---|---|---|---|---|
| 2 | P||Q | [-2.01, -1.99] | 40 | 7.198e-4 | 1.442e-5 |
| 2 | Q||P | [-2.01, -1.99] | 40 | 7.394e-4 | 1.484e-5 |

## Renyi orders 2 and 3 at sigma 2, both directions: certificates (19 Oct 2026 23:3x)

cert_renyi_arb_sigma.py takes the raw densities (no rho/al normalisation), so one integrand serves both directions and every
sigma; g1 enters as a ball. Tails: with p = sum a_i N_{m_i} and q = sum b_j N_{n_j}, p^alpha <= 2^(alpha-1) sum a_i^alpha
N_{m_i}^alpha, q^(alpha-1) >= (b_j N_{n_j})^(alpha-1) for each j, and N_m^alpha N_n^(1-alpha) = N(z; alpha m - (alpha-1) n, s)
exp(alpha(alpha-1)(m-n)^2/(2 s^2)); the smallest of the resulting Gaussian tails over j is used, at L = 30 s + 2 alpha. At
sigma 1 it reproduces cert_renyi_int_arb.py (order 3 P||Q at g1 -2.2: 1.38725e-2) and cert_renyi_qp_arb.py (order 2 Q||P at
g1 -0.5: 1.07930e-2) digit for digit. Scan at sigma 2 in cert_renyi_s2_scan.txt.

| sigma | direction | order | interval of g1 | balls | min of J_SAME - J_ANTI | int J(adaptive) - int J(pair) >= |
|---|---|---|---|---|---|---|
| 2 | P||Q | 2 | [-3.01, -2.99] | 40 | 1.556e-3 | 3.122e-5 |
| 2 | P||Q | 3 | [-3.01, -2.99] | 40 | 6.694e-3 | 1.340e-4 |
| 2 | Q||P | 2 | [-1.01, -0.99] | 40 | 2.116e-3 | 4.237e-5 |
| 2 | Q||P | 3 | [-1.01, -0.99] | 40 | 9.266e-3 | 1.861e-4 |

With the KL certificates above, at sigma 2 the adaptive switch beats the pair rigorously at KL and orders 2 and 3 in both
directions.

## Sigma 0.5: KL and orders 2 and 3, both directions: certificates (19 Oct 2026 23:4x)

Same two scripts (cert_kl_arb_sigma.py, cert_renyi_arb_sigma.py) at sigma 0.5. In P||Q the pointwise gains are small (KL peak
1.31e-7 at g1 -1.4; order 2 3.4e-7 at -1.9; order 3 1.3e-5 at -2.35, where J itself is about 1e5), and the slack of a g1-ball
grows roughly linearly in its half-width h: about 7.5 h for KL, 670 h at order 2 and 2e6 h at order 3 (probes at h 1e-7 and
1e-8 in cert_renyi_s05_scan.txt). So the P||Q balls are very narrow. A single narrow interval on which the difference is
strictly positive is still a proof that the switch beats the pair; the certified bound is small because the interval is,
not because the gain is. Scans: cert_kl_s05_scan_pq.txt, cert_kl_s05_scan_qp.txt, cert_renyi_s05_scan.txt.

| sigma | divergence | direction | interval of g1 | balls | min of pointwise difference | divergence-side gain >= |
|---|---|---|---|---|---|---|
| 0.5 | KL | P||Q | [-1.4000001, -1.3999999] | 20 | 9.352e-8 | 1.870e-14 |
| 0.5 | KL | Q||P | [-1.0000001, -0.9999999] | 20 | 5.584e-7 | 1.117e-13 |
| 0.5 | order 2 | P||Q | [-1.9000000001, -1.8999999999] | 10 | 3.374e-7 | 6.747e-17 (int J) |
| 0.5 | order 3 | P||Q | [-2.350000000001, -2.349999999999] | 10 | 1.298e-5 | 2.597e-17 (int J) |
| 0.5 | order 2 | Q||P | [-0.50000001, -0.49999999] | 20 | 1.441e-3 | 2.881e-11 (int J) |
| 0.5 | order 3 | Q||P | [-0.50000001, -0.49999999] | 20 | 0.2397 | 4.795e-9 (int J) |

The pointwise minima match the scans (KL P||Q 1.31e-7 at the centre against 9.35e-8 lower end; order 2 3.44e-7 vs 3.37e-7;
order 3 1.318e-5 vs 1.298e-5; Q||P 1.44069e-3 and 0.239728 at the centre). With sigma 1 and sigma 2, the switch now beats
the pair rigorously at KL and orders 2 and 3, both directions, at sigma 0.5, 1 and 2. The Q||P balls could be far wider
(the gains there are large); they were kept narrow only to finish quickly.

## Non-integer orders 3/2 and 5/2 at sigma 1, both directions: certificates (19 Oct 2026 23:4x)

cert_renyi_real_arb_sigma.py is cert_renyi_arb_sigma.py with p^alpha q^(1-alpha) computed by acb.pow with the analytic flag
(acb.integral then verifies the branch cut is not touched; p and q are positive on the path) and alpha read as an exact
rational. The tail bound is unchanged and holds for every real alpha > 1: x^alpha is convex, so (a+b)^alpha <= 2^(alpha-1)
(a^alpha + b^alpha), and q^(1-alpha) is decreasing in q. Controls: at alpha 3 P||Q g1 -2.2 and alpha 2 Q||P g1 -0.5 it
reproduces the integer script digit for digit (1.38725e-2, 1.07930e-2); scipy quadrature on [-12, 12] matches the centres to
eight digits (alpha 3/2 P||Q g1 -1.5: 5.861407e-4; 5/2 Q||P g1 0: 9.061942e-2; 5/2 P||Q g1 -2.1: 5.285469e-3). Scan in
cert_renyi_real_s1_scan.txt.

| sigma | direction | order | interval of g1 | balls | min of J_SAME - J_ANTI | int J(adaptive) - int J(pair) >= |
|---|---|---|---|---|---|---|
| 1 | P||Q | 3/2 | [-1.51, -1.49] | 80 | 4.537e-4 | 9.209e-6 |
| 1 | Q||P | 3/2 | [-0.51, -0.49] | 80 | 1.095e-3 | 2.305e-5 |
| 1 | P||Q | 5/2 | [-2.11, -2.09] | 80 | 3.529e-3 | 7.143e-5 |
| 1 | Q||P | 5/2 | [-0.01, 0.01] | 80 | 8.964e-2 | 1.802e-3 |

Since D_alpha = log(int J)/(alpha - 1) with alpha > 1, each line is a strict gain in the Renyi divergence itself. The script
covers any rational alpha > 1; orders in (0, 1) would need the reversed inequalities and are not treated.

## Exact interval cover (20 Oct 2026 00:0x)

agent A's audit of the sigma 0.5 runs found that a sub-ball built as arb((lo+hi)/2, (hi-lo)/2) from Python floats can
miss lo or hi by an ulp, because the float midpoint is rounded. On the very narrow sigma 0.5 intervals this happened in five
runs (KL P||Q 5 of 20 balls, KL Q||P 8 of 20, order 3 P||Q 4 of 10, orders 2 and 3 Q||P 12 of 20 each); the sigma 1 and 2
runs, the integer-order and chi^2 scripts (midpoint built in Arb) and the 3/2, 5/2 runs have none, by a direct check that every
sub-ball contains both endpoints. All seven ball scripts now use g = arb(lo).union(arb(hi)) and width arb(hi) - arb(lo). The
five affected certificates were re-run: every line is identical to the original to the printed digits (the originals are kept
as *.midball_20261019.txt), and agent A's own exact-cover recertification agrees.

Audit status. Sigma 1 and 2, KL and orders 2 and 3, both directions: two audits each (agent A, agent C).
Sigma 0.5, the same six: two audits (agent C; agent A with exact cover, AUDIT_S05_agent_A.md).
Orders 3/2 and 5/2 at sigma 1, both directions: two audits (AUDIT_REAL_ORDERS_agent_A.md; addendum in
AUDIT_RENYI_agent_C.md).

## Orders 1/4, 1/2 and 3/4 at sigma 1: certificates (20 Oct 2026 00:2x)

Below order 1 the comparison turns round. D_alpha = log(int J)/(alpha - 1) with alpha - 1 < 0, so the adaptive query beats the
pair at order alpha exactly when it makes int J smaller, and the certificate is J_ANTI - J_SAME > 0 on a cover of an interval of
g1 (cert_renyi_sub1_arb_sigma.py). The tail bound changes with the sign. Both exponents alpha and 1 - alpha lie in (0, 1), so
x^alpha and x^(1-alpha) are subadditive, p^alpha q^(1-alpha) <= sum_ij a_i^alpha b_j^(1-alpha) N_{m_i}^alpha N_{n_j}^(1-alpha),
and N_m^alpha N_n^(1-alpha) = N(z; alpha m + (1-alpha) n, s) exp(-alpha(1-alpha)(m-n)^2/(2 s^2)) with centre of modulus at most 1;
the Mills bound then covers |z| > L = 30 sigma + 2 alpha.

Since int p^alpha q^(1-alpha) is the order-(1 - alpha) integral of (Q, P), J_PQ(alpha) = J_QP(1 - alpha) at every g1, so the
P||Q certificates at 1/4 and 3/4 are also the Q||P certificates at 3/4 and 1/4, and order 1/2 (the Bhattacharyya coefficient) is
the same in both directions. The scans reproduce this identity digit for digit (scan_sub1_{PQ,QP}{14,34}_s1.txt).

Where the switch wins, at sigma 1: ANTI - SAME > 0 for g1 <= -1 at all three orders (2.3e-7 at -3, 2e-5 at -2, 1e-4 to 1.9e-4 at
-1.5 and -1), negative from -0.5 upward. Balls of width 0.025 carry slack of about 2e-3 and certify nothing; width 5e-4 does.

| order (P||Q) | same as (Q||P) | interval | balls | min lower end | int J(pair) - int J(adaptive) >= |
|---|---|---|---|---|---|
| 1/4 | 3/4 | [-1.3, -1.2] | 200 | 8.35e-5 | 9.42e-6 |
| 1/2 | 1/2 | [-1.3, -1.2] | 200 | 1.43e-4 | 1.52e-5 |
| 3/4 | 1/4 | [-1.3, -1.2] | 200 | 9.22e-5 | 9.57e-6 |

Files: cert_renyipq{14,12,34}_sub1_s1_arb.txt. Second lane (mpmath quad, 30 digits, scratchpad mp_sub1.py): ANTI - SAME at g1 =
-1.3, -1.25, -1.2 is 1.54e-4, 1.67e-4, 1.78e-4 (order 1/4), 2.10e-4, 2.19e-4, 2.24e-4 (1/2), 1.55e-4, 1.54e-4, 1.48e-4 (3/4); at
g1 = 0 it gives -0.0048315132, -0.0074431785, -0.0064150185, the Arb centres to every printed digit; the duality holds there too.
Audits: agent A, 20 Oct 00:5x (rows/T353/audit_A/AUDIT_SUB1_agent_A.md): all nine sub-1 certificates (sigma 0.5, 1, 2 x orders 1/4, 1/2, 3/4) re-certified with independent code and tail bound, the same minimum lower ends and gains to every printed digit, mpmath agreeing. Second audit: agent C, 20 Oct 03:0x (rows/T353/audit_C/AUDIT_SUB1_agent_C.md): all nine re-certified with its own Arb integration and an AM-GM tail bound (tail below 1.3e-39), no failed ball, the duality checked both ways at sigma 1. With two independent audits the sub-1 certificates count as verified.

Sigma 2 and sigma 0.5, same three orders (20 Oct 00:2x). At sigma 2 the order-1/2 scan is positive on all of [-4, -1] (peak
2.0e-4 at -2); at sigma 0.5 it is positive from -4 to -1.25 but tiny (4.4e-8 at -1.25, 4.6e-9 at -1.5), as above order 1.

| sigma | order (P||Q) | interval | balls | min lower end | int J(pair) - int J(adaptive) >= |
|---|---|---|---|---|---|
| 2 | 1/4 | [-2.05, -1.95] | 200 | 1.21e-4 | 1.23e-5 |
| 2 | 1/2 | [-2.05, -1.95] | 200 | 1.73e-4 | 1.74e-5 |
| 2 | 3/4 | [-2.05, -1.95] | 200 | 1.24e-4 | 1.25e-5 |
| 0.5 | 1/4 | [-1.250001, -1.249999] | 40 | 1.79e-8 | 3.59e-14 |
| 0.5 | 1/2 | [-1.250001, -1.249999] | 40 | 3.25e-8 | 6.50e-14 |
| 0.5 | 3/4 | [-1.250001, -1.249999] | 40 | 1.68e-9 | 3.35e-15 |

Files cert_renyipq{14,12,34}_sub1_s{2,05}_arb.txt. With the duality these are also Q||P at orders 3/4, 1/2, 1/4. So at sigma 0.5,
1 and 2 the adaptive query beats the pair at Renyi orders 1/4, 1/2, 3/4, 3/2 (sigma 1), 2, 3 and in KL, both directions.
Here "both directions" compares each orientation of the adaptive query with the same orientation of the pair. Against
the larger of the pair's two orientations, the comparison a symmetric privacy definition would make, the adaptive query wins
at order 1/2 in both orientations, at order 1/4 only as x'||x (the pair's Q||P is the larger there) and at order 3/4 only as
x||x', at sigma 0.5, 1 and 2 (audit_C/sub1_max_check.txt). The refutation holds under either reading.

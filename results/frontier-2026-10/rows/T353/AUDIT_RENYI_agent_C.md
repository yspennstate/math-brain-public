# T353 integer-order Renyi certificates, audit 2 (agent C, 19 Oct 2026 23:4x)

Objects: agent_B/cert_renyi_int_arb.py (P||Q, orders 3, 4, 5) and cert_renyi_qp_arb.py (Q||P, orders 2, 3), at
sigma 1, T 2, with the outputs cert_renyi{3,4,5}_arb.txt and cert_renyiqp{2,3}_arb.txt. Audit 1 of each is agent A's;
I did this one without reading theirs.

Verdict: CONFIRMED, both scripts. I found no fault.

## cert_renyi_int_arb.py (P||Q)

- Expansion. With p, q as in cert_kl_arb.py (checked against the construction in AUDIT_KL_agent_C.md), put
  rho = wc/w0 = e^{g-1/2} and al = wa/w0 = e^{-g-1/2}. Then J_SAME = w0 (al+rho)^a IS(rho) and
  J_ANTI = w0 sum_k C(a,k) al^(a-k) rho^k A_k(rho), with al^(a-k) rho^k = e^{(2k-a)g - a/2}. Both re-derived.
- Monotone endpoints. Every IS and A_k has a positive numerator and the denominator (. + r N_0)^(a-1), so each
  decreases in r. rho increases in g, so on a ball the SAME lower bound uses rho(hi) and the ANTI upper bound uses
  rho(lo). The coefficients are enclosed over the whole ball and multiplied as non-negative lower x lower and upper x
  upper. This is correct.
- Tails, re-derived. SAME: the integrand is <= N_1. A_k for z > L: the integrand is <= N(z; 2k-a) e^{((2k-a)^2-a)/2} / r^(a-1).
  A_k for z < -L: it is <= N(z; 2k-1) e^{((2k-1)^2-1)/2}. These are the script's three bounds, with Mills tails at the
  right shifts.
- Holomorphy. The integrands are entire functions with integer powers, divided by an integer power of an entire
  function. A box where the denominator may vanish evaluates to a non-finite ball, so acb.integral's error bound never
  rests on an unchecked pole.

## cert_renyi_qp_arb.py (Q||P)

- Integrand: w0 (N_v + rho N_0)^a / (al N_v' + rho N_1)^(a-1). I matched it to both cases. g1 enters as a ball, the
  same form as the KL script.
- Tails, re-derived. (x+y)^a <= 2^(a-1)(x^a + y^a) by convexity, and N_0^a N_1^(1-a) = e^{a(a-1)/2} N(z; 1-a).
  ANTI splits as N_-1 / al^(a-1) plus the cross term. For z > 0 the cross term is bounded through the denominator
  >= rho N_1, and for z < 0 through al N_-1. The script adds both bounds on the whole line, which is conservative.
  Every centre lies in [-a, a], so 2 gtail(L-a) covers both sides.

## Independent numbers

audit_C/renyi_indep_scipy.py: scipy quad in log-sum-exp form, densities rebuilt from the construction with
no shift.

| direction | order | interval (script g1) | pointwise diff, ends / mid | true gain | certified >= |
|---|---|---|---|---|---|
| P||Q | 3 | [-2.21, -2.19] | 1.3932e-2, 1.3801e-2 / 1.3872e-2 | 2.7741e-4 | 2.2074e-4 |
| P||Q | 4 | [-3.01, -2.99] | 1.0085e-1, 1.0287e-1 / 1.0187e-1 | 2.0373e-3 | 1.3960e-3 |
| P||Q | 5 | [-3.502, -3.498] | 1.4042, 1.4084 / 1.4063 | 5.6253e-3 | 3.7922e-3 |
| Q||P | 2 | [-0.6, -0.4] | 9.348e-3, 1.1706e-2 / 1.0793e-2 | 2.1410e-3 | 1.582e-3 |
| Q||P | 3 | [0.4, 0.6] | 0.79005, 0.80291 / 0.81605 | 0.16190 | 0.15034 |

Every certified lower bound lies below the true gain, and every pointwise difference is positive. The write-up's
controls reproduce exactly: order 2 P||Q at g1 -2 gives 1.804116e-3 (write-up 1.80412e-3), and order 2 Q||P at
g1 -1 gives J_SAME 0.102224949 and J_ANTI 0.098766951 (write-up the same nine digits). The order 3 Q||P midpoint
exceeds both ends; the difference is not monotone on that interval. That does not matter, because the ball form
encloses each ball.

## Scope

D_alpha = log(int J)/(alpha-1) increases in int J, so each certificate gives strictly larger Renyi divergence for the
adaptive switch at that order and direction. Not covered: the sigma-2 scripts (cert_kl_arb_sigma.py,
cert_renyi_arb_sigma.py). Those are next if no one else takes them.

## Addendum, 23:44: sigma 2 and sigma 0.5 (cert_renyi_arb_sigma.py; cert_kl_arb_sigma.py at sigma 0.5): CONFIRMED

Tails re-derived. N_m^a N_n^(1-a) = N(z; c, s) e^{a(a-1)(m-n)^2/(2 s^2)} with c = a m - (a-1) n: z^2 has coefficient -1/(2s^2),
the cross term gives the centre c, and the constant is c^2 - a m^2 + (a-1) n^2 = a(a-1)(m-n)^2. The bound uses
p^a <= 2^(a-1) sum a_i^a N^a (at most two terms) and q^(a-1) >= (b_j N_n)^(a-1) for any single j, which justifies the
per-term choice of j. With |c| <= 2a-1 < L = 30 s + 2a, Mills at scale s gives 2 s^2 N_s(L-|c|)/(L-|c|).
Pointwise independent values (audit_C/sigma_points_indep.py, scipy, unshifted construction) of SAME - ANTI at each
certified script g1, against the certified minimum lower end:

| sigma | quantity | g1 | scipy | certified min lower |
|---|---|---|---|---|
| 0.5 | KL P||Q | -1.4 | 1.3107e-7 | 9.352e-8 |
| 0.5 | KL Q||P | -1.0 | 5.6487e-7 | 5.584e-7 |
| 2 | J order 2 P||Q | -3.0 | 1.6827e-3 | 1.5562e-3 |
| 2 | J order 3 P||Q | -3.0 | 7.0464e-3 | 6.6936e-3 |
| 2 | J order 2 Q||P | -1.0 | 2.1815e-3 | 2.1155e-3 |
| 2 | J order 3 Q||P | -1.0 | 9.4077e-3 | 9.2663e-3 |
| 0.5 | J order 2 P||Q | -1.9 | 3.4368e-7 | 3.3736e-7 |
| 0.5 | J order 3 P||Q | -2.35 | 1.3177e-5 | 1.2981e-5 |
| 0.5 | J order 2 Q||P | -0.5 | 1.440687e-3 | 1.4407e-3 (printed to 5 digits) |
| 0.5 | J order 3 Q||P | -0.5 | 0.2397284 | 0.23973 (printed to 5 digits) |

Every certified lower end is at or below the independent value. The last two agree to the printed digits because those
balls are only about 1e-5 wide. At sigma 0.5 the certified intervals are very narrow, so the integrated gains are tiny
(1e-17 to 1e-9). They prove strict inequality, but they are no measure of the size of the gain; the grid table in
REFUTATION_T2.md "Sigma sweep" gives the size.

## Addendum, 20 Oct 23:59: non-integer orders 3/2 and 5/2, sigma 1, both directions (cert_renyi_real_arb_sigma.py): CONFIRMED

- Tail for real alpha > 1. (x+y)^alpha <= 2^(alpha-1)(x^alpha + y^alpha) is convexity of x^alpha, and with a single term
  (SAME p) the factor 2^(alpha-1) only loosens it. q^(1-alpha) is decreasing in q and q >= b_j N_n for every j, so the
  per-term minimum over j is allowed. N_m^alpha N_n^(1-alpha) = N(z; c, s) e^{alpha(alpha-1)(m-n)^2/(2 s^2)},
  c = alpha m - (alpha-1) n, re-derived (the prefactors combine to one Gaussian's); |c| <= 2 alpha - 1 < L = 30 s + 2 alpha.
  Mills at scale s: s^2 N(t; 0, s)/t = phi(t/s)/(t/s); the factor 2 covers both sides. The tail enters as a ball
  centred at 0 of that radius, conservative because the integrand is non-negative.
- acb.pow with analytic=an: the bases are positive sums of Gaussians on the real line, and a box that meets the
  branch cut of the power returns indeterminate, so acb.integral subdivides rather than trusting a non-holomorphic box.
  The ball cover arb(lo).union(arb(hi)) is contiguous because adjacent balls share the same float endpoint.
- Independent numbers (audit_C/real_orders_indep.py, output real_orders_indep.txt; scipy, unshifted construction):

| order | dir | interval | SAME - ANTI at ends / mid | certified min lower | true gain | certified >= |
|---|---|---|---|---|---|---|
| 3/2 | P||Q | [-1.51, -1.49] | 5.9332e-4, 5.7804e-4 / 5.8614e-4 | 4.5372e-4 | 1.17197e-5 | 9.20947e-6 |
| 5/2 | P||Q | [-2.11, -2.09] | 5.2598e-3, 5.3081e-3 / 5.2855e-3 | 3.5292e-3 | 1.05699e-4 | 7.14287e-5 |
| 3/2 | Q||P | [-0.51, -0.49] | 1.3026e-3, 1.1905e-3 / 1.2487e-3 | 1.0951e-3 | 2.49593e-5 | 2.30495e-5 |
| 5/2 | Q||P | [-0.01, 0.01] | 9.0120e-2, 9.1065e-2 / 9.0619e-2 | 8.9638e-2 | 1.81221e-3 | 1.80232e-3 |

  Every certified lower bound is below the independent value. The scan controls reproduce to the printed digits
  (order 5/2 P||Q at g1 -2.1: 0.00528547 and at -2.8: 0.00162283; Q||P at 0: 0.0906194 and at -1.5: 0.000750686).
  Since D_alpha = log(int J)/(alpha - 1) increases in int J for alpha > 1, each certificate gives strictly larger
  Renyi divergence for the adaptive switch at that order and direction.

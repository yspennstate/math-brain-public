# T238 target 2: the lazy-to-rich window for a quadratic student is matrix sensing's initialization scale

Reduction. The student is alpha m^-1 sum_j a_j (w_j . x)^2, with +- pairs that share w_j(0) ~ N(0, I/d), trained by
gradient flow on the empirical square loss with m -> infinity. Each w_j moves by a linear ODE w' = -/+ G w with
G = (1/n) sum_i r_i x_i x_i^T, which depends only on the current residuals. So the predictor is x^T M x with
M = P - Q, where

  P' = -(G P + P G),   Q' = +(G Q + Q G),   P(0) = Q(0) = c I,

and c is proportional to alpha / d (time rescaled by alpha). This is matrix sensing with a difference of two PSD
factors grown multiplicatively from a scaled identity. When the G(t) commute, P = c exp(-2 int G) and
Q = c exp(2 int G), so M = -2c sinh(2 int G). The implicit regularizer is then the spectral hypentropy at scale c, the
matrix version of Woodworth et al. (2002.09277). As c -> infinity the flow is M' = -4c G, which converges to the
minimum-Frobenius interpolant; as c -> 0 it is nuclear-norm-like.

Numerics (window.py). Teacher y = (v . x)^2 with abs(v) = 1, n = d^2/4, flow run to train MSE below 1e-10 (or 4e5
steps at the smallest c), 2000 test points. The table gives the distance to the lazy predictor,
abs(f - f_lin)^2 / Var y, as a fraction of its c -> 0 value.

| c | d = 8 | d = 12 (s1) | d = 12 (s2) | d = 16 |
|---|---|---|---|---|
| 1e-4 | 0.99 | 0.99 | 0.93 | 0.89 |
| 1e-3 | 0.92 | 0.95 | 0.78 | 0.71 |
| 1e-2 | 0.54 | 0.75 | 0.44 | 0.37 |
| 0.1 | 0.05 | 0.20 | 0.05 | 0.03 |
| 0.3 | 0.003 | 0.03 | 0.003 | 0.002 |
| 1 | 0.00 | 0.001 | 0.00 | 0.00 |

Test error goes from about 0 at c <= 1e-4 (the rank-one teacher is recovered) to the minimum-Frobenius value at
c >= 1. That value is 0.44, 0.10, 0.45 and 0.50 for the four runs.

Reading.

- The lazy edge sits at c of about 0.3 for every d tried, which is alpha of order d in the student's units.
- A second pass (win2_*.txt: a second seed at d = 8 and 16, two seeds at d = 24, one at d = 32, c in 1e-3, 1e-2, 0.1) does
  not support a moving rich end. Remaining share of the gap, by seed, with the lazy test error as the c -> 0 value:

| c | d = 8 | d = 12 | d = 16 | d = 24 | d = 32 |
|---|---|---|---|---|---|
| 1e-3 | 0.92, 0.54 | 0.95, 0.78 | 0.71, 0.84 | 0.88, 0.86 | 0.91 |
| 1e-2 | 0.54, 0.22 | 0.75, 0.44 | 0.37, 0.46 | 0.52, 0.48 | 0.58 |
| 0.1 | 0.05, 0.015 | 0.20, 0.05 | 0.03, 0.03 | 0.04, 0.03 | 0.05 |

  Seed spread is as large as any trend. Over d = 8 to 32 at n = d^2/4 the window is fixed in c: centre near 1e-2,
  lazy by 0.1-0.3, rich by 1e-3. The first pass's reading (rich end moving down with d) came from one seed per d.
- The rich side gets better with d: test error at c = 1e-3 is 0.044 (d = 8, seed 2), 0.006, 0.002-0.003 and 0.001
  (d = 16, 24, 32).
- The bulk eigenvalues of the lazy interpolant stay at 0.06-0.12 (median and rms) from d = 8 to 32, so the window is
  not set by a bulk scale that shrinks with d.
- The window is a curve in c = alpha/d against the teacher's scale. This answers target 1's request for a curve at
  T = convergence, for this family.

Open. Whether the rich edge moves at larger d, as the hypentropy picture suggests for fixed precision (Woodworth et al.
2002.09277; the d-threshold is still to be read from the paper body), a proof of the hypentropy bias when the G(t) do
not commute, finite m, and other n/d^2.

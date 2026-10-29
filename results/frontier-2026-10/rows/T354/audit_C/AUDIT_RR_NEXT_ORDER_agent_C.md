# T354 next-order term under random reshuffling, beta1 >= 0, eps = 0, audit 2 (agent C, 20 Oct 2026 04:3x)

Object: the two NOTE sections "The next-order term, random reshuffling, beta1 = 0, eps = 0" and "... with momentum, eps = 0",

    x*/x0 = 1 + d (K - (3/4) T H/(K B2 B3)) + O(d^2),   T = E[b Z^2],   H = (1/n) sum_p (1 - beta1^(p+1)) h(p),
    h(p) = 1 - 3p/(n-1) + 2p(p-1)/((n-1)(n-2)),

with beta1 = 0 giving H = 1/6 and the limit 1/2 - T/(4 B2 B3). Audit 1 is agent A's (push cf490b48).

Verdict: CONFIRMED. The coefficient is re-derived by hand below. It is also checked against exact roots on a model the note did not
use: b = (6, 2, -1 x 8), on which an S = Var(b^2) term would show if there were one. The check uses my own exact solver, a different
code from the Laplace route the note checked against.

## Re-derived by hand

- With x = 0 and g = b, and using sum_b Z_b = 0:
  - M0l = E[b_a Z_a Z_b] = -T/(n-1).
  - Mjj = E[b_a Z_b^2] = -T/(n-1), since sum_a b_a = 0.
  - Mjl = E[b_a Z_b Z_c] over distinct a, b, c. Replace Z_c by its average over the other n-2 positions, which is -(Z_a + Z_b)/(n-2).
    This gives 2T/((n-1)(n-2)).
- Full earlier epoch: M00 + 2(n-1) M0l + (n-1) Mjj + (n-1)(n-2) Mjl = T(1 - 2 - 1 + 2) = 0.
- Current epoch at beta2 = 1: the Z lags are the p + 1 positions 0..p, one of which is g's own sample. The bracket is
  T(1 - 2p/(n-1) - p/(n-1) + 2p(p-1)/((n-1)(n-2))) = T h(p).
  - It depends only on the count of current-epoch positions, so it is the same for every momentum lag i <= p.
  - Those lags carry total weight 1 - beta1^(p+1). So Q = (d/B2)^2 T H.
- First order at beta2 = 1: a current-epoch lag contributes 1 - p/(n-1), and an earlier epoch contributes 1 - (n-1)/(n-1) = 0.
  So K0 = (1/n) sum_p (1 - beta1^(p+1))(1 - p/(n-1)).
- Solve: C/V = B3/B2 + 2x + O(d^2), so x(1 - dK) = dK B3/(2 B2) - (3/8) Q + O(d^3). Divide by x0 = dK B3/(2B2) to get the formula.

## Exact roots on b = (6, 2, -1 x 8) (rr_exact_two_special.py, rr2_runs.txt; predictions rr2_pred.py)

- The model: B2 = 4.8, B3 = 21.6, T = 572.64, n = 10.
- The solver extends rr_exact_mom_eps.py to two special values. In each epoch their positions are a uniform ordered pair of distinct
  positions, independent across epochs, and 1/sqrt(v) is (2/sqrt pi) times the integral over t of e^(-t^2 v), which factorizes
  over epochs.
- Controls on the test model reproduce the note's own exact values: -1.274532 at (beta1 0, beta2 0.999) and -0.809838 at
  (beta1 0.5, beta2 0.999). The first is also matched by my one-special solver.
- Raising the nodes from 160 to 240 changes nothing in the printed digits.

| beta1 | limit (formula) | exact (x*/x0-1)/d at beta2 0.9995 / 0.999 / 0.998 | gap to the K-form, over d | linear extrapolation to d = 0 |
|---|---|---|---|---|
| 0   | -0.880787 | -0.880114 / -0.879445 / -0.878116 | -5.53 / -5.52 / -5.50 | -0.880783 |
| 0.5 | -0.541022 | -0.539657 / -0.538296 / -0.535586 | -1.97 / -1.96 / -1.94 | -0.541018 |
| 0.9 | -0.087858 | -0.085557 / -0.083252 / -0.078634 | 3.40 / 3.41 / 3.44    | -0.087862 |

- The gap is flat in d in every family, so what remains is O(d^2).
- Extrapolating from beta2 0.9995 and 0.999 lands within 4e-6 of the formula's limit at all three beta1.
- On this model an iid-style S term would move the beta1 = 0 limit by (3/4) S/B2^2 = (3/4)(108.96/23.04) = 3.55 at this order,
  with S = E[Z^2]. The data rule that out, which confirms the note's claim that reshuffling has no S term at first correction.

## Not covered

eps > 0 under reshuffling, a rigorous remainder for the next order, the regime where n d is not small, and vector b.

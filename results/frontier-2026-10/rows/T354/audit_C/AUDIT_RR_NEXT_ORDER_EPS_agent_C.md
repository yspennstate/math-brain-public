# T354 next-order term under random reshuffling, beta1 >= 0, eps > 0, audit 2 (agent C, 20 Oct 2026 05:1x)

Object: the NOTE section "The next-order term, random reshuffling with momentum and eps > 0" (20 Oct 04:2x),

    x*/x0 = 1 + d (r K - p2 T H/(r K B2 B3)) + O(d^2),   x0 = r d K B3/(2 B2),
    s = sqrt(B2),  r = s/(s + eps),  p2 = s(eps + 3s)/(4(eps + s)^2),

with T, H, K as in the eps = 0 sections. Audit 1 is agent A's (push 8cbf6228).

Verdict: CONFIRMED. The coefficient is re-derived by hand below, and exact roots at eps 1 and eps 10 on a model the note did not use
(b = (6, 2, -1 x 8)) extrapolate to the formula's limit within 2e-6 in all six families. An S = Var(b^2) term is ruled out at both eps.

## Re-derived by hand

- psi(y) = (s + eps)/(s sqrt(y) + eps). psi'(y) = -(s + eps) s/(2 sqrt(y) (s sqrt(y) + eps)^2), so psi'(1) = -s/(2(s + eps)) = -r/2.
- psi''(1) = ((s + eps) s/2)((s + eps) + 2s)/(2(s + eps)^3) = s(eps + 3s)/(4(s + eps)^2) = p2.
- Solve: with y = v/V the ratio of the moment to its frozen value, the drift is
  0 = x - (r/2) d K C/V + (p2/2) Q + O(d^3), where Q = (d/B2)^2 T H is the same quadratic term as at eps = 0.
  - r and p2 depend on x only through V = x^2 + B2, which moves at O(d^2), so they are constants at this order.
  - C/V = B3/B2 + 2x + O(d^2), which gives x(1 - r d K) = r d K B3/(2 B2) - (p2/2) Q + O(d^3).
  - Dividing by x0 = r d K B3/(2 B2) gives 1 + d r K - (p2/2) Q/x0 = 1 + d (r K - p2 T H/(r K B2 B3)).
- At eps = 0, r = 1 and p2 = 3/4, which is the eps = 0 formula already audited twice.
- The S = Var(b^2) terms. Under iid sampling they come from E[(y - 1)^2] = O(d). Under reshuffling every earlier epoch sums
  Z to zero, so E[(y - 1)^2] = O(d^2) and they leave this order. I take this from audit 2 at eps = 0 (rr2_runs.txt), where an S
  term was ruled out on this same model; the runs below test it again with eps > 0.

## Exact roots on b = (6, 2, -1 x 8) (rr_exact_two_special_eps.py, rr2e_runs.txt; predictions rr2e_pred.py)

The solver is rr_exact_two_special.py (audit 2 at eps = 0) with one change. It uses
1/(sqrt(v) + eps) = int_0^inf (2/sqrt pi)(1 - eps sqrt(pi) t erfcx(eps t)) e^(-t^2 v) dt, which still factorizes over epochs
because the extra weight depends on t only. kernel_t_check.txt compares this kernel with direct evaluation at 160 and 240 nodes: the
largest relative error is 4e-13 and 1.4e-13.

Control: on the note's test model (9, -1, -1 x 8) at beta1 0, beta2 0.999, eps 1, x* = 0.00150382594436 and (x*/x0 - 1)/d =
-1.104672. agent A's different solver gives 0.001503825946, and the note gives -1.10467.

| eps | beta1 | limit (formula) | exact (x*/x0-1)/d at beta2 0.9995 / 0.999 / 0.998 | gap to the K-form, over d | linear extrapolation to d = 0 (minus the limit) |
|---|---|---|---|---|---|
| 1 | 0 | -0.748998 | -0.748858 / -0.748718 / -0.748439 | -4.97 / -4.96 / -4.93 | -0.748998 (+0.0e+00) |
| 1 | 0.5 | -0.470931 | -0.470265 / -0.469600 / -0.468274 | -2.24 / -2.23 / -2.21 | -0.470930 (+1.0e-06) |
| 1 | 0.9 | -0.085310 | -0.083940 / -0.082568 / -0.079817 | 1.84 / 1.85 / 1.87 | -0.085312 (-2.0e-06) |
| 10 | 0 | -0.535837 | -0.536068 / -0.536298 / -0.536751 | -3.08 / -3.07 / -3.05 | -0.535838 (-1.0e-06) |
| 10 | 0.5 | -0.357564 | -0.357497 / -0.357428 / -0.357289 | -1.61 / -1.60 / -1.59 | -0.357566 (-2.0e-06) |
| 10 | 0.9 | -0.081188 | -0.080696 / -0.080202 / -0.079208 | 0.57 / 0.57 / 0.58 | -0.081190 (-2.0e-06) |

- The K-form is the formula with the exact K at that beta2 (rr2e_pred.txt). The gap over d is flat in every family, so what remains is O(d^2).
- Extrapolating from beta2 0.9995 and 0.999 lands within 2e-6 of the limit in all six families.
- The S = Var(b^2) term of the iid formula at this eps (rr2e_pred.txt, S = 108.96) would move the beta1 = 0 limit by -2.4588 at eps 1 and -1.1905 at
  eps 10. The data rule both out, as audit 2 did at eps = 0.
- Node count: the eps 10, beta1 0, beta2 0.999 root at 240 nodes equals the 160-node root in all twelve printed digits of x*.
- At eps 10 the beta1 = 0 values approach the limit from below and at eps 1 from above; the sign of the O(d^2) term changes with eps,
  which is why both eps were run rather than one.

## Not covered

A rigorous remainder, the regime where n d is not small, vector b, and a_i other than 1.

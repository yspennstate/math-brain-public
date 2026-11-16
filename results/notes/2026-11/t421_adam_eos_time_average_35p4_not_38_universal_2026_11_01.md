---
name: t421_adam_eos_time_average_35p4_not_38_universal_2026_11_01
description: T421 Adam on quadratics: as eps->0 eta*C time-averages 35.40 (not 38), range [31,39.8], universal in eta/p/h; 38 two-cycle only near threshold
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T17:41:00+04:00
  status: provisional
  evidence: "frontier/rows/T421 m421a moves 262c66bf, adam_run1/2.txt"
---

T421 (Adam at the edge of stability, preconditioned sharpness vs the 38/eta threshold for beta1 = 0.9). Move m421a, moves 262c66bf, 1 Nov.

Full-batch bias-corrected Adam (0.9, 0.999) on a diagonal quadratic is coordinate-wise. As eps -> 0 the dynamics of eta C_i = eta h_i/(sqrt(vhat) + eps) depend only on r = eta h/eps.
- For r >= 1e3, eta C does not settle at 38. It wanders in [31, 39.8] with time average 35.40, universal to 0.2 pct over eta 1e-3..1e-1, p 1.5..3, h 1..100 and up to 1e6 steps.
- The sign alternates 85 pct of the time. |x| bursts to 0.25 eta while the mean loss is only 1.16x the 2-cycle floor h(eta/38)^2/2: a relaxation oscillation.
- At r = 100 the mean is 36.17. Coordinates with r < 38 converge.
- The exact 38 two-cycle (an agent, 20 Oct) is stable only for r in (38, 38.107).

So "within o(1/eta) of the threshold" fails pointwise; the time-average constant is 0.93 x 38.

Pre-registered "38 within 2 pct, period 2" failed. The universality bar passed.

Open: 35.40 as a function of (beta1, beta2), from a slow-fast reduction.


ADDENDUM (1 Nov, m421b, moves 8a8779c1): the constant is set by beta1, hardly by beta2. Long-run mean eta C over the threshold
2(1 + beta1)/(1 - beta1), at r = 1e4: 1.000 at beta1 = 0 (RMSprop sits on the exact 2-cycle), 0.98 at 0.5, 0.93 at 0.9, for beta2
from 0.99 to 0.9999 (under 1 pct change). Pre-registered band [0.85, 0.97] everywhere: FAIL, 3 of 9 cells.
Trap: in float64, Adam with beta2 >= 0.999 and small eps falsely converges near the edge. |x| falls by up to 840 decades between bursts,
hits exactly 0 and stays there. A common rescaling of (x, m, v) does not fix it; separate exponents for (x, m) and for v do
(rows/T421/adam_beta3.py). Also corrected: the eps -> 0 symmetry is (x, eta, eps) -> c(x, eta, eps), not x -> c x.

ADDENDUM 2 (1 Nov, m421c, moves e63c0e59): the beta1 dependence is not a power law (0.084 beta1^2 failed 0 of 5). At beta2 0.999, for
beta1 <= 0.145 Adam locks exactly onto the 2-cycle at the threshold. Above beta1* in (0.145, 0.15) it oscillates with the time average
ABOVE threshold (up to 1.058 near 0.18), crosses 1 near 0.4, bottoms at 0.926 near 0.8 and returns to 0.988 at 0.99. r-independent.
beta1* moves with beta2 (below 0.14 at beta2 0.99), so "beta2 barely matters" holds for the mean, not for the lock edge.

ADDENDUM 3 (1 Nov, m421d, moves d20b71b7): the lock edge is a subcritical Neimark-Sacker bifurcation of the exact eps = 0 2-cycle,
at beta1* = 0.172 for every beta2 from 0.99 to 0.9999 (3 x 3 Jacobian). Below it the cycle and the relaxation oscillation coexist:
started on the cycle Adam stays locked up to 0.16 (pre-registered, 6 of 6), but from x = 1 it lands on the oscillation from beta1 0.14-0.15.
So addendum 2's "beta1* moves with beta2" is the basin edge, not the bifurcation. At beta1 0.9 the cycle is unstable (rho 1.10).

"""Front and tail diagnostics for the layer recursion of arXiv:2608.04303 (Theorem 2).

s_0 = 1,  s_i(y) = 1 - exp(-int_0^y s_{i-1}),  lbar_k = int_0^inf s_k(y) e^{-y} dy.

Claim: s_k(y) = P(M_k <= y) where M_k is the minimum at generation k of the branching random walk
whose children sit at the points of a rate-one Poisson process on (0, inf) (the Poisson-weighted
infinite tree), so lbar_k = E[e^{-M_k}].

Addario-Berry and Ford, Ann. Appl. Probab. 23 (2013), Theorem 1.1: median(M_n) = n/e + (3/(2e)) log n
+ O(1); Theorem 1.2: P(M_n <= median - x) << e^{-c x} for every c < e.

This script measures the median of M_k and the left-tail slope directly, and reports lbar_k against
the candidate exponents.  The window is kept 40 units BELOW the front, where s_k < e^{-100}, so the
mass to the left of the window is exactly negligible and no bookkeeping is carried across shifts.
"""
import numpy as np, sys
from math import e, log, exp

K = int(sys.argv[1]) if len(sys.argv) > 1 else 200
H = float(sys.argv[2]) if len(sys.argv) > 2 else 0.002
BELOW, ABOVE = 45.0, 45.0
W = BELOW + ABOVE
n = int(W / H) + 1
y = np.arange(n) * H
off = 0.0
s = np.ones(n)
rows = []
for k in range(1, K + 1):
    S = np.concatenate(([0.0], np.cumsum((s[1:] + s[:-1]) * 0.5 * H)))   # = int_0^y s_{k-1}, left mass < e^{-100}
    s = -np.expm1(-S)          # 1 - exp(-S) without the cancellation at tiny S
    yy = off + y
    lbar = np.trapezoid(s * np.exp(-yy), dx=H) + exp(-(off + W))
    i = int(np.searchsorted(s, 0.5))
    med = float('nan')
    if 0 < i < n:
        med = yy[i - 1] + (0.5 - s[i - 1]) * H / (s[i] - s[i - 1])
    tail = []
    for x in (5.0, 15.0):
        j = int(round((med - x - off) / H)) if med == med else -1
        tail.append(-log(s[j]) / x if 0 <= j < n and s[j] > 0 else float('nan'))
    rows.append((k, lbar, med, tail[0], tail[1]))
    # slide so the window's left edge stays ~BELOW under the front
    target = max(0.0, (k + 1) / e - BELOW)
    m = int(round((target - off) / H))
    if m > 0:
        s2 = np.empty(n); s2[:n - m] = s[m:]; s2[n - m:] = 1.0
        s = s2; off = off + m * H
print(f"h={H} window={W} (front sits {BELOW} above the left edge)")
print(f"{'k':>6} {'lbar_k':>13} {'median':>10} {'med-k/e-(3/2e)ln k':>19} {'med-k/e-.5 ln k':>16} {'tail@5':>7} {'tail@15':>7} {'b_k':>8}")
for k, lb, med, t5, t15 in rows:
    if not (k % max(1, K // 15) == 0 or k in (1, 2, 5, 10, 20, 50, 100)): continue
    b = lb * exp(k / e) * k ** (3 / (2 * e))
    print(f"{k:>6} {lb:>13.5e} {med:>10.5f} {med - k/e - (3/(2*e))*log(k):>19.5f} {med - k/e - 0.5*log(k):>16.5f} {t5:>7.4f} {t15:>7.4f} {b:>8.5f}")
print("lambda* = e = %.5f ;  3/(2e) = %.5f" % (e, 3 / (2 * e)))

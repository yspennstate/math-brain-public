"""H0019 / Conjecture 1 of arXiv:2608.04303 (layer distribution of the random recursive tree).

Their Theorem 2:  lbar_k = int_0^inf s_k(y) e^{-y} dy,  s_0 = 1,  s_i(y) = 1 - exp(-int_0^y s_{i-1}).

Claim under test: with u_i := 1 - s_i,  u_i(y) = exp(-int_0^y (1 - u_{i-1})) is exactly the
recursion for u_i(y) = P(M_i > y), M_i = minimal position at generation i of the branching random
walk whose children sit at the points of a rate-one Poisson process on (0, inf) (the PWIT).
Hence lbar_k = E[e^{-M_k}] and, by the branching-random-walk front
m_k = k/e + (3/(2e)) log k + O(1),  lbar_k = exp(-k/e - (3/(2e)) log k + O(1)).

This script (a) integrates the recursion on a fine grid to high k and tests whether
lbar_k * exp(k/e) * k^{3/(2e)} is bounded and converging, against the two rival hypotheses
(no log correction, and a log correction with a different coefficient); (b) checks the identity
lbar_k = E[e^{-M_k}] by direct simulation of the Poisson branching random walk.
"""
import numpy as np, sys
from math import e, log, exp

K = int(sys.argv[1]) if len(sys.argv) > 1 else 60
YMAX = K / e + 40.0
H = float(sys.argv[2]) if len(sys.argv) > 2 else 0.002
n = int(YMAX / H) + 1
y = np.arange(n) * H
s = np.ones(n)                      # s_0 = 1
rows = []
for k in range(1, K + 1):
    # S(y) = int_0^y s  by the trapezoid rule (s is smooth and increasing in y)
    S = np.concatenate(([0.0], np.cumsum((s[1:] + s[:-1]) * 0.5 * H)))
    s = 1.0 - np.exp(-S)
    # lbar_k = int_0^inf s_k(y) e^{-y} dy ; the tail beyond YMAX contributes < e^{-YMAX}
    w = np.exp(-y)
    lbar = np.trapezoid(s * w, dx=H) if hasattr(np, 'trapezoid') else np.trapz(s * w, dx=H)
    rows.append((k, lbar))
print(f"grid h={H} ymax={YMAX:.1f} points={n}")
print(f"{'k':>4} {'lbar_k':>14} {'*exp(k/e)':>14} {'*k^(3/2e)':>12} {'ratio':>9} {'no-log':>12} {'coef 3/2':>12}")
prev = None
for k, lb in rows:
    a = lb * exp(k / e)
    b = a * k ** (3 / (2 * e))
    c = a                      # hypothesis: no log correction
    d = a * k ** 1.5           # hypothesis: coefficient 3/2 instead of 3/(2e)
    r = (b / prev) if prev else float('nan')
    prev = b
    if k <= 6 or k % 5 == 0 or k == rows[-1][0]:
        print(f"{k:>4} {lb:>14.6e} {a:>14.6e} {b:>12.6f} {r:>9.5f} {c:>12.6f} {d:>12.4f}")
# the exact small-k values from their Corollary 2.1 / text
print("\ncheck against the paper: lbar_1 = 1/2, lbar_2 = 3 - e = %.6f" % (3 - e))
print("computed:                lbar_1 = %.6f, lbar_2 = %.6f" % (rows[0][1], rows[1][1]))

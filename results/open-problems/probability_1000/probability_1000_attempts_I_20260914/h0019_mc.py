"""Independent test of the dictionary  s_k(y) = P(M_k <= y),  lbar_k = E[e^{-M_k}].

The recursion of arXiv:2608.04303 Theorem 2 is integrated nowhere here.  Instead the Poisson-weighted
infinite tree is simulated directly: root at 0, children of a particle at x are the points of a
rate-one Poisson process on (x, infinity).  Only particles below a cutoff Y are kept - legitimate,
because displacements are positive, so a particle above Y has no descendant below Y - and the
minimum at generation k is read off.  The estimates are then compared with the recursion values
(hard-coded from the exact run, and recomputed here on a coarse grid only for the comparison table).
"""
import numpy as np, sys
from math import e, exp

Y = float(sys.argv[1]) if len(sys.argv) > 1 else 10.0
R = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
KMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 12
rng = np.random.default_rng(20260914)

mins = np.full((R, KMAX + 1), np.inf)
for r in range(R):
    pos = np.zeros(1)
    for k in range(1, KMAX + 1):
        if pos.size == 0:
            break
        cnt = rng.poisson(Y - pos)
        tot = int(cnt.sum())
        if tot == 0:
            pos = np.empty(0); break
        par = np.repeat(pos, cnt)
        pos = par + (Y - par) * rng.random(tot)
        mins[r, k] = pos.min()

# the recursion, on its own grid, for the comparison
H = 0.001
n = int((Y + 25) / H) + 1
yg = np.arange(n) * H
s = np.ones(n)
rec = {}
for k in range(1, KMAX + 1):
    S = np.concatenate(([0.0], np.cumsum((s[1:] + s[:-1]) * 0.5 * H)))
    s = -np.expm1(-S)
    rec[k] = (s.copy(), np.trapezoid(s * np.exp(-yg), dx=H))

print(f"Poisson-weighted infinite tree, cutoff Y={Y}, {R} replicates")
print(f"{'k':>3} {'y':>5} {'MC P(M_k<=y)':>13} {'recursion s_k(y)':>17} {'MC E[e^-M_k]':>13} {'recursion lbar_k':>17}")
for k in (1, 2, 3, 5, 8, 10, 12):
    if k > KMAX: continue
    sk, lb = rec[k]
    m = mins[:, k]
    emc = np.mean(np.exp(-np.minimum(m, 1e9)))     # M_k > Y contributes < e^{-Y}
    for yv in (1.0, 3.0, 6.0):
        p = float(np.mean(m <= yv))
        se = (p * (1 - p) / R) ** 0.5
        print(f"{k:>3} {yv:>5.1f} {p:>8.4f}+-{se:.4f} {sk[int(yv/H)]:>17.4f}"
              + (f" {emc:>13.6f} {lb:>17.6f}" if yv == 1.0 else ""))

"""Does the explicit V_[3,2] model agree with the closed formula for Gval?  (n = 5)

For the top eigenvector x the gap-weighted state is D = Dt / tr Dt, Dt = sum_k g_k a_k a_k^t.  If the formula for Gval
in gval_n5_check_lib.py (through canon_spectral.build) is right, then on every graph

    Gval = c * ((n-2) tr(Dt L32) - ((n-1) lam - 2W) tr Dt)

with one constant c.  The two sides come from different code: the left from the matrix M of canon_spectral, the right
from the model of V_[3,2] by symmetric matrices in state_mix_n5.py.
"""
import sys
import numpy as np

sys.path.insert(0, "~/brain-repo/06_math_research/t104_alon_agent_2026_11_11")
from gval_n5_check_lib import gval          # noqa: E402
from state_mix_n5 import n, pairs, lap, L32, comp32   # noqa: E402

rng = np.random.default_rng(3)
ratios, gaps = [], []
for trial in range(300):
    w = rng.random(len(pairs)) ** rng.integers(1, 4)
    if trial % 3 == 0:
        w[rng.random(len(pairs)) < 0.3] = 0.0
    if w.sum() < 1e-6:
        continue
    w = w / w.sum()
    L = lap(w)
    ev, U = np.linalg.eigh(L)
    if ev[-1] - ev[-2] < 1e-3:
        continue
    x = U[:, -1]
    Pi = np.eye(n) - 1.0 / n
    Q = Pi - np.outer(x, x)
    g, Y = np.linalg.eigh(Q @ (ev[-1] * Pi - L) @ Q)
    Dt = sum(gk * np.outer(comp32(x, Y[:, k]), comp32(x, Y[:, k])) for k, gk in enumerate(g) if gk > 1e-13)
    rhs = (n - 2) * float(np.trace(Dt @ L32(w))) - ((n - 1) * ev[-1] - 2.0) * float(np.trace(Dt))
    G = gval(w)[0]
    if abs(rhs) > 1e-9:
        ratios.append(G / rhs); gaps.append(ev[-1] - ev[-2])
r = np.array(ratios)
print("graphs used: %d   Gval / model value: min %.12f  max %.12f  spread %.2e" % (len(r), r.min(), r.max(), r.max() - r.min()))

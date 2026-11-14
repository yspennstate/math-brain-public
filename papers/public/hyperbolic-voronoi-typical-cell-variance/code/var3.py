"""lam^2 Var(V) = int_0^inf (p(t) - e^{-t}) dt in H^2 (formula and p(t) in var.py), the values of Table 1.
Two points at area-distance t share a cell when a nucleus sits near their midpoint, at cost about 2 sqrt(pi lam t), so
p(t) has a tail out to t ~ 1/lam, and p falls from 1 on the scale t ~ lam (distance ~ 1). Every grid is geometric
(ratio 2) over these scales, with 12 and 18 Gauss-Legendre nodes per piece. Usage: python var3.py 100 10 1 0.1 ..."""
import math, sys, time
import numpy as np
from var import gl_pieces, p_of

def geo(lo, hi, ratio=2.0):
    cuts = [0.0, lo]
    while cuts[-1] * ratio < hi:
        cuts.append(cuts[-1] * ratio)
    return cuts + [hi]

def lam2var(lam, n=12):
    tmax = max(80.0, 400.0 / lam)
    T = gl_pieces(geo(min(1e-4, 1e-4 * lam), tmax), n)
    S = gl_pieces(geo(min(1e-4, 1e-4 * lam), 80.0), n)
    TH = gl_pieces(geo(1e-4 * min(1.0, math.sqrt(lam)), math.pi), n)
    p = np.array([p_of(t, lam, S, TH) for t in T[0]])
    return float((T[1] * (p - np.exp(-T[0]))).sum()), p, T

if __name__ == '__main__':
    for lam in [float(x) for x in sys.argv[1:]]:
        t0 = time.time()
        v1, p, T = lam2var(lam, 12)
        v2, _, _ = lam2var(lam, 18)
        tail = float((T[1] * p)[T[0] > 80].sum())
        print(f'lam={lam:<8g} lam^2 Var={v1:.10f} (finer {v2:.10f}, diff {v2 - v1:+.1e})  lam*Var={v2 / lam:.8f}  '
              f'mass of p beyond t=80: {tail:.3e}  p(t_min)={p[0]:.6f}  ({time.time() - t0:.0f}s)', flush=True)

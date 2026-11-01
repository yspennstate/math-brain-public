"""Selector coordinate of the X003 family: Delta_y U / Inf_y and Delta_y H / Inf_y as k grows (EVIDENCE)."""
import numpy as np, time
from feilib import spectrum, entropy, influences, restrict
from upward import Uprime

def x003_table(k, r):
    n = 1 + k + r; N = 1 << n
    xs = np.arange(N)
    y = (xs & 1)  # bit0 = y (1 means y=-1)
    xbits = (xs >> 1) & ((1 << k) - 1)
    zbits = (xs >> (1 + k)) & ((1 << r) - 1)
    # bent b(x) = (-1)^{x1x2 + x3x4 + ...} on bits
    b = np.ones(N, dtype=np.int64)
    for j in range(k // 2):
        b *= np.where(((xbits >> (2 * j)) & 1) & ((xbits >> (2 * j + 1)) & 1), -1, 1)
    flip = (y == 1) & (xbits == 0)
    b = np.where(flip, -b, b)
    return np.where(zbits == 0, b, 1), n

for k in [4, 6, 8, 10]:
    t0 = time.time(); r = k
    t, n = x003_table(k, r)
    p = spectrum(t); inf = influences(p, n); U = float(Uprime(p, n)); H = float(entropy(p))
    tp = restrict(t, n, 0, 0); tm = restrict(t, n, 0, 1)
    pp = spectrum(tp); pm = spectrum(tm)
    dU = U - 0.5 * (float(Uprime(pp, n - 1)) + float(Uprime(pm, n - 1)))
    dH = H - 0.5 * (float(entropy(pp)) + float(entropy(pm)))
    print(f"k={k} n={n} Inf_y={inf[0]:.3e} dU/Inf={dU/inf[0]:.3f} dH/Inf={dH/inf[0]:.3f} U/I={U/inf.sum():.3f} H/I={H/inf.sum():.3f} ({time.time()-t0:.1f}s)", flush=True)

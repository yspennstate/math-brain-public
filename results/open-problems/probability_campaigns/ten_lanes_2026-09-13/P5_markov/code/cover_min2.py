"""Minimise E_pi[cover time] over reversible n-state chains, numerically robust."""
import os, sys, numpy as np
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from covertime import cover_float, target
rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 20260913)
NMAX = 12.0

def unpack(x, n, loops):
    W = np.zeros((n, n)); k = 0
    for i in range(n):
        for j in range(i, n):
            if i == j and not loops: continue
            W[i, j] = W[j, i] = np.exp(NMAX * np.tanh(x[k] / NMAX)); k += 1
    return W

def nparams(n, loops):
    return n * (n + 1) // 2 if loops else n * (n - 1) // 2

def obj(x, n, loops):
    W = unpack(x, n, loops)
    w = W.sum(1)
    if not np.all(np.isfinite(W)) or w.min() <= 0: return 1e9
    if np.linalg.matrix_rank(np.sign(W) + np.eye(n)) < 1: return 1e9
    try: v = cover_float(W)
    except Exception: return 1e9
    if not np.isfinite(v) or v < n - 1 - 1e-9: return 1e9   # E_pi C >= n-1 trivially
    return v

n = int(sys.argv[1])
for loops in (True, False):
    best = (np.inf, None); m = nparams(n, loops)
    starts = {3: 200, 4: 200, 5: 120, 6: 60, 7: 25}.get(n, 20)
    for t in range(starts):
        x0 = rng.normal(0, 2.0, m)
        r1 = minimize(obj, x0, args=(n, loops), method="Nelder-Mead",
                      options=dict(maxiter=8000, maxfev=8000, xatol=1e-11, fatol=1e-13))
        r2 = minimize(obj, r1.x, args=(n, loops), method="Nelder-Mead",
                      options=dict(maxiter=8000, maxfev=8000, xatol=1e-12, fatol=1e-14))
        if r2.fun < best[0]: best = (r2.fun, r2.x)
    W = unpack(best[1], n, loops); W = W / W.max()
    tgt = float(target(n))
    print(f"n={n} loops={loops}: min E_pi C = {best[0]:.12f}  target {tgt:.12f}  ratio {best[0]/tgt:.10f}")
    np.set_printoptions(precision=5, suppress=True)
    print(W)
    sys.stdout.flush()

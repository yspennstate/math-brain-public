"""Minimise E_pi[cover time] over reversible n-state chains (weighted graphs
with self-loops allowed).  Target of Aldous-Fill Open Problem 6.30:
E_pi C >= (n-1)H_{n-1}, conjectured extremal = non-lazy complete graph."""
import os, sys, numpy as np
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from covertime import cover_float, target
rng = np.random.default_rng(20260913)

def unpack(x, n, loops=True):
    W = np.zeros((n, n))
    k = 0
    for i in range(n):
        for j in range(i, n):
            if i == j and not loops:
                continue
            W[i, j] = W[j, i] = np.exp(x[k]); k += 1
    return W

def nparams(n, loops=True):
    return n * (n + 1) // 2 if loops else n * (n - 1) // 2

def obj(x, n, loops):
    W = unpack(x, n, loops)
    if (W.sum(1) <= 1e-14).any(): return 1e9
    try:
        v = cover_float(W)
    except Exception:
        return 1e9
    return v if np.isfinite(v) else 1e9

for n in range(3, 7):
    for loops in (True, False):
        best = (np.inf, None)
        m = nparams(n, loops)
        starts = 120 if n <= 5 else 40
        for t in range(starts):
            x0 = rng.normal(0, 1.5, m)
            res = minimize(obj, x0, args=(n, loops), method="Nelder-Mead",
                           options=dict(maxiter=6000, maxfev=6000, xatol=1e-10, fatol=1e-12))
            if res.fun < best[0]:
                best = (res.fun, res.x)
        W = unpack(best[1], n, loops)
        W = W / W.max()
        tgt = float(target(n))
        print(f"n={n} loops={loops}: min E_pi C found = {best[0]:.10f}   target = {tgt:.10f}   "
              f"ratio = {best[0]/tgt:.8f}")
        np.set_printoptions(precision=4, suppress=True)
        print("   argmin weights (scaled):\n", W)
        sys.stdout.flush()

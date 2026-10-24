"""Test the normalization credit and alpha*TC/I for weighted threshold events (float evidence)."""
import numpy as np, math, json, time, sys
from scipy.optimize import minimize
from biased import ltf_table, credit_terms
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
TLIM = float(sys.argv[2]) if len(sys.argv) > 2 else 300
def rand_weights(n):
    kind = rng.integers(0, 4)
    if kind == 0: w = rng.integers(1, 4, n).astype(float)
    elif kind == 1: w = rng.integers(1, 12, n).astype(float)
    elif kind == 2: w = np.exp(rng.normal(0, 1.5, n))
    else: w = np.where(rng.random(n) < 0.3, rng.integers(2, 6), 1).astype(float)
    return np.sort(w)[::-1]
def objs(T, q):
    c = credit_terms(T, q)
    if c['I'] < 1e-12: return 0, 0, c
    return c['aTC'] / c['I'], c['excess'] / c['I'], c
def neg(x, T, which):
    q = 1 / (1 + np.exp(-np.clip(x, -11, 11)))
    a, b, c = objs(T, q)
    return -(a if which == 0 else b)
t0 = time.time(); best = [(0, None), (0, None)]; cnt = 0
while time.time() - t0 < TLIM:
    n = int(rng.integers(3, 11)); w = rand_weights(n)
    th = rng.random() * w.sum(); T = ltf_table(w, th)
    if T.min() == T.max(): continue
    x = rng.normal(0, 3, n); q = 1 / (1 + np.exp(-x))
    a, b, c = objs(T, q); cnt += 1
    for which, val in ((0, a), (1, b)):
        if val > 0.5 * best[which][0] and val > 0:
            r = minimize(neg, x, args=(T, which), method='Nelder-Mead', options=dict(maxiter=200 * n))
            v = -r.fun
            if v > best[which][0]:
                qq = 1 / (1 + np.exp(-np.clip(r.x, -11, 11)))
                best[which] = (v, (n, w.tolist(), th, qq.tolist()))
print('configs', cnt)
print('max alpha*TC/I =', best[0][0], best[0][1])
print('max (VlnV - credit)/I =', best[1][0], best[1][1])

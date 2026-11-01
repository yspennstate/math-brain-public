import numpy as np, math, sys, time, warnings
from scipy.optimize import minimize
from biased import ltf_table
from gibbs_bound import gibbs
warnings.filterwarnings('ignore')
rng = np.random.default_rng(int(sys.argv[1])); TLIM = float(sys.argv[2])
def rw(n):
    k = rng.integers(0, 4)
    if k == 0: w = rng.integers(1, 4, n)
    elif k == 1: w = rng.integers(1, 12, n)
    elif k == 2: w = np.exp(rng.normal(0, 1.5, n))
    else: w = np.where(rng.random(n) < 0.3, rng.integers(2, 7), 1)
    return np.sort(np.asarray(w, float))[::-1]
def neg(x, T, w, key):
    q = 1 / (1 + np.exp(-np.clip(x, -11, 11)))
    r = gibbs(T, q, w)
    return 0.0 if r is None else -r[key]
t0 = time.time(); best = {'B_over_I': (0, None), 'Bloose_over_I': (0, None)}; cnt = 0
while time.time() - t0 < TLIM:
    n = int(rng.integers(3, 10)); w = rw(n); th = rng.random() * w.sum()
    T = ltf_table(w, th)
    if T.min() == T.max(): continue
    x = rng.normal(0, 3, n); q = 1 / (1 + np.exp(-x))
    r = gibbs(T, q, w); cnt += 1
    if r is None: continue
    for key in best:
        if r[key] > 0.7 * best[key][0]:
            res = minimize(neg, x, args=(T, w, key), method='Nelder-Mead', options=dict(maxiter=150 * n))
            v = -res.fun
            if v > best[key][0]:
                best[key] = (v, (n, w.round(3).tolist(), round(th, 3), (1 / (1 + np.exp(-np.clip(res.x, -11, 11)))).round(5).tolist()))
print('configs', cnt)
for k, v in best.items(): print(k, v)

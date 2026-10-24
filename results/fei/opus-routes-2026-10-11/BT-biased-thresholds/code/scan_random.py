"""Random weighted thresholds n=5..13 with random/extreme biases; local bias optimization of good hits.
Float evidence; candidates with ratio > 7.6 are re-checked exactly elsewhere."""
import numpy as np, math, json, time, sys
from scipy.optimize import minimize
from biased import ltf_table, metrics
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
TLIM = float(sys.argv[2]) if len(sys.argv) > 2 else 400
def rand_weights(n):
    kind = rng.integers(0, 5)
    if kind == 0: w = rng.integers(1, 4, n).astype(float)
    elif kind == 1: w = rng.integers(1, 10, n).astype(float)
    elif kind == 2: w = np.exp(rng.normal(0, 1.5, n))
    elif kind == 3:
        w = np.where(rng.random(n) < 0.3, rng.integers(2, 6), 1).astype(float)
    else: w = rng.random(n) + 0.5
    return np.sort(w)[::-1]
def rand_bias(n):
    kind = rng.integers(0, 4)
    if kind == 0: return rng.random(n) * 0.98 + 0.01
    x = rng.normal(0, 4, n)
    if kind == 2: x = np.where(rng.random(n) < 0.5, x, rng.normal(0, 0.5, n))
    return 1 / (1 + np.exp(-x))
def ratio(T, q):
    m = metrics(T, q, with_rho=False)
    if m['Delta'] < 1e-9: return 0.0, m
    return m['Hplus'] / m['Delta'], m
def negr(x, T):
    q = 1 / (1 + np.exp(-np.clip(x, -12, 12)))
    r, m = ratio(T, q)
    return -r
t0 = time.time(); top = []; cnt = 0
while time.time() - t0 < TLIM:
    n = int(rng.integers(5, 12))
    w = rand_weights(n)
    tot = w.sum(); th = rng.random() * tot
    T = ltf_table(w, th)
    if T.min() == T.max(): continue
    q = rand_bias(n)
    r, m = ratio(T, q); cnt += 1
    if r > 5.0:
        x0 = np.log(q / (1 - q))
        res = minimize(negr, x0, args=(T,), method='Nelder-Mead', options=dict(maxiter=300 * n))
        if -res.fun > r:
            r = -res.fun; q = 1 / (1 + np.exp(-np.clip(res.x, -12, 12)))
    top.append((r, n, w.tolist(), th, q.tolist()))
    top.sort(key=lambda z: -z[0]); top = top[:25]
print('evaluated', cnt, 'configs in', round(time.time() - t0), 's')
for z in top[:12]:
    print(round(z[0], 4), z[1], [round(v, 3) for v in z[2]], round(z[3], 3), [round(v, 5) for v in z[4]])
json.dump(top, open(f'../data/scan_random_seed{sys.argv[1] if len(sys.argv)>1 else 7}.json', 'w', encoding='utf-8'))

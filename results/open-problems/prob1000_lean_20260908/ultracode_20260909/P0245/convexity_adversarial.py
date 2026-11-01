# Try hard to break convexity of f(W) = E_pi C on the slice sum(W)=1 (symmetric nonneg W with loops).
import numpy as np, time, sys
from scipy.optimize import minimize
from cover_exact import *
rng = np.random.default_rng(7)
f = lambda W: E_pi_cover(rw_on_graph(W))

def unpack(theta, n):
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    W = np.zeros((n, n))
    for t, (i, j) in zip(theta, pairs):
        W[i, j] = W[j, i] = np.exp(np.clip(t, -12, 12))
    return W / W.sum()

def violation(theta, n):
    m = len(theta) // 2
    W1 = unpack(theta[:m], n); W2 = unpack(theta[m:], n)
    try:
        f1, f2, fm = f(W1), f(W2), f((W1 + W2) / 2)
    except np.linalg.LinAlgError:
        return 0.0
    return fm - (f1 + f2) / 2   # >0 means convexity violated

t0 = time.time()
for n in [3, 4, 5]:
    m = n * (n + 1) // 2
    best = -np.inf
    for s in range(8 if n < 5 else 5):
        th0 = rng.normal(0, 3, 2 * m)
        res = minimize(lambda th: -violation(th, n), th0, method="Nelder-Mead", options={"maxiter": 1500 if n < 5 else 600, "xatol": 1e-4, "fatol": 1e-9})
        v = -res.fun
        best = max(best, v)
        print("n=%d start %d: max violation found %.3e (best %.3e) t=%.0fs" % (n, s, v, best, time.time() - t0)); sys.stdout.flush()
# extreme random segments
for n in [4, 5, 6, 7]:
    worst = -np.inf; cnt = 0
    for trial in range(400 if n < 7 else 60):
        spread = rng.uniform(1, 6)
        W1 = unpack(rng.normal(0, spread, n * (n + 1) // 2), n); W2 = unpack(rng.normal(0, spread, n * (n + 1) // 2), n)
        if rng.random() < 0.5: np.fill_diagonal(W1, 0); W1 /= W1.sum()
        if rng.random() < 0.5: np.fill_diagonal(W2, 0); W2 /= W2.sum()
        try:
            f1, f2 = f(W1), f(W2)
            for lam in [0.1, 0.3, 0.5, 0.7, 0.9]:
                fm = f(lam * W1 + (1 - lam) * W2)
                worst = max(worst, fm - lam * f1 - (1 - lam) * f2); cnt += 1
        except np.linalg.LinAlgError:
            pass
    print("n=%d extreme segments tested %d, worst (f_mid - chord) = %.3e" % (n, cnt, worst))

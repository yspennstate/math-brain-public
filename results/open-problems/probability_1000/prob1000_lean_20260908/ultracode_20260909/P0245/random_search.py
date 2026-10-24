# Random reversible chains (symmetric weights incl. self loops), minimize E_pi C by scipy over log-weights.
import numpy as np, time, sys
from scipy.optimize import minimize
from cover_exact import *
rng = np.random.default_rng(20260909)

def chain_from_theta(theta, n, pairs):
    W = np.zeros((n, n))
    for t, (i, j) in zip(theta, pairs):
        W[i, j] = np.exp(t); W[j, i] = np.exp(t)
    return rw_on_graph(W)

def run(n, starts, budget_s):
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    m = len(pairs); T = target(n)
    best = np.inf; t0 = time.time(); bestP = None
    for s in range(starts):
        if time.time() - t0 > budget_s: break
        theta0 = rng.normal(0, 2.0, m)
        # sometimes kill self-loops entirely
        if rng.random() < 0.7:
            for k, (i, j) in enumerate(pairs):
                if i == j: theta0[k] = -30
        def f(th):
            th = np.clip(th, -14, 14)
            try:
                return E_pi_cover(chain_from_theta(th, n, pairs))
            except np.linalg.LinAlgError:
                return 1e6
        res = minimize(f, theta0, method="L-BFGS-B", bounds=[(-14, 14)] * m, options={"maxiter": 60, "eps": 1e-6})
        v = res.fun
        if v < best: best = v; bestP = chain_from_theta(np.clip(res.x, -14, 14), n, pairs)
        print("n=%d start %d: initial %.4f -> %.6f  (best %.6f, target %.6f)" % (n, s, f(theta0), v, best, T)); sys.stdout.flush()
    print("n=%d BEST %.6f target %.6f diff %.2e" % (n, best, T, best - T))
    np.set_printoptions(precision=3, suppress=True)
    print(bestP)

run(6, 12, 200)
run(7, 8, 250)

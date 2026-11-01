"""Auxiliary inputs only (core at 1/2): E F = (sum_j mu_j)/256 exactly (every Walsh coefficient of g on two or more
auxiliary coordinates is zero), so sum_j mu_j = 0 is exact balance.  Minimise s - C over mu_9..mu_16 with
mu_17 = -(mu_9 + ... + mu_16), inputs priced by the saved fixed point V.  Also scans symmetric patterns
(k auxiliaries at +m, k at -m).
Usage: python opt_aux.py <vig npz> <nstarts> <seed>
"""
import sys, time, itertools
import numpy as np
try:
    import psutil
    _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass
from scipy.optimize import minimize
from opt18 import Pricer, evaluate, N

pr = Pricer(sys.argv[1]); C = pr.C
nst = int(sys.argv[2]); seed = int(sys.argv[3])
AUX = list(range(9, 18))


def full(z):
    mu = np.zeros(N)
    mu[9:17] = z; mu[17] = -z.sum()
    return mu


def f(z):
    mu = full(z)
    if abs(mu[17]) >= 0.999:
        return 1.0 + (abs(mu[17]) - 0.999), np.zeros(8)
    s, EF, It, Ht, g, dEF = evaluate(mu, pr)
    assert abs(EF - mu[9:].sum() / 256) < 1e-12
    return s - C, g[9:17] - g[17]


print("symmetric patterns: k aux at +m, k aux at -m (others 1/2)", flush=True)
for k in (1, 2, 3, 4):
    for up in [tuple(range(9, 9 + k))]:
        dn = tuple(range(9 + k, 9 + 2 * k))
        for m in (0.1, 0.3, 0.5, 0.7, 0.9, 0.99):
            mu = np.zeros(N); mu[list(up)] = m; mu[list(dn)] = -m
            s, EF = evaluate(mu, pr, grad=False)[:2]
            print("  k=%d up=%s dn=%s m=%.2f: s - C = %+.5e (E F = %.1e)" % (k, up, dn, m, s - C, EF), flush=True)
rng = np.random.default_rng(seed)
best = None; t0 = time.time()
for st in range(nst):
    z0 = rng.uniform(-0.9, 0.9, 8) * rng.choice([0.3, 0.7, 1.0])
    if abs(z0.sum()) > 0.95:
        z0 *= 0.9 / abs(z0.sum())
    res = minimize(f, z0, jac=True, method="L-BFGS-B", bounds=[(-0.995, 0.995)] * 8, options={"maxiter": 300})
    mu = full(res.x)
    print("start %2d: s - C = %+.6e  nit %3d  mu_aux=%s  (%.0f s)" % (st, res.fun, res.nit, np.array2string(mu[9:], precision=3, max_line_width=300), time.time() - t0), flush=True)
    if best is None or res.fun < best[0]:
        best = (res.fun, mu)
print("BEST aux-only balanced s - C = %+.6e at mu_aux=%s" % (best[0], np.array2string(best[1][9:], precision=4, max_line_width=300)))

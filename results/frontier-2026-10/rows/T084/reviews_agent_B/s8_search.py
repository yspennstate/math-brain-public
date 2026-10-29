# T084, agent B: numeric search for N < 0 at S8 pairs (0,1), (4,5) (and (3,7) as positive control), from the exact
# monomial expansion: min over log-weights in [-8, 8] and q in (0,1) of N / sum |terms|, Nelder-Mead from random starts.
import numpy as np, json
from scipy.optimize import minimize
exec(open('amgm_cert.py').read().split("if __name__")[0])
A = [0b0111, 0b1011, 0b1101, 0b1111]
cols = [1, 2, 4, 8] + [sum(((A[r] >> (3 - c)) & 1) << r for r in range(4)) for c in range(4)]
rng = np.random.default_rng(0)
for e, f in [(0, 1), (4, 5), (3, 7)]:
    C = Npoly(cols, e, f); M = np.array(list(C.keys()), float)
    P = [np.array([float(x) for x in sp.Poly(c, q).all_coeffs()]) for c in C.values()]
    def obj(z):
        qv = 1 / (1 + np.exp(-z[0])); x = np.clip(z[1:], -8, 8)
        cv = np.array([np.polyval(p, qv) for p in P]); w = np.exp(M @ x); t = cv * w
        return t.sum() / np.abs(t).sum()
    best = (1, None)
    for s in range(60):
        z0 = np.concatenate([[rng.uniform(-6, 3)], rng.uniform(-6, 6, M.shape[1])])
        r = minimize(obj, z0, method='Nelder-Mead', options=dict(maxiter=4000, xatol=1e-8, fatol=1e-12))
        if r.fun < best[0]: best = (r.fun, r.x)
    print(json.dumps(dict(pair=(e, f), min_ratio=float(best[0]), q=float(1 / (1 + np.exp(-best[1][0]))), logy=[round(float(v), 2) for v in best[1][1:]])), flush=True)

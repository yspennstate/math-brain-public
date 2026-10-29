"""Refine the minimum of K/(AB(A+B)) and K/(AB) (Prop 6.2) by Nelder-Mead from the worst random samples.
Messages a = rho(4 softmax(u) - 1) * r with r in (0, 1] (sigmoid), so the whole region is covered."""
import sys, json
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, '.')
import kernel_indep as KI   # reuses only K() written from the paper text

def sm(u): e = np.exp(u - u.max()); return e / e.sum()
def unpack(x):
    a = KI.msg(sm(x[0:4])) / (1 + np.exp(-x[8])); b = KI.msg(sm(x[4:8])) / (1 + np.exp(-x[9])); return a, b
def ratio(x, m, which):
    a, b = unpack(x); k, d = KI.K(a[None], b[None], m)
    A, B = (a * a).sum(), (b * b).sum()
    return float(k[0] / (d[0] if which == 'cubic' else A * B))

rng = np.random.default_rng(int(sys.argv[1])); n = int(sys.argv[2]); out = []
for m in (0.0, KI.M):
    for which in ('cubic', 'quad'):
        X = np.concatenate([rng.normal(0, 2.5, (n, 8)), rng.normal(0, 3, (n, 2))], 1)
        ab = [unpack(x) for x in X]; a = np.array([t[0] for t in ab]); b = np.array([t[1] for t in ab])
        k, d = KI.K(a, b, m); den = d if which == 'cubic' else (a * a).sum(1) * (b * b).sum(1)
        r = k / den; best = np.argsort(r)[:12]; res = []
        for i in best:
            o = minimize(ratio, X[i], args=(m, which), method='Nelder-Mead', options={'maxiter': 4000, 'xatol': 1e-9, 'fatol': 1e-12})
            res.append((o.fun, unpack(o.x)))
        f, (a0, b0) = min(res, key=lambda t: t[0])
        out.append({"m": m, "ratio": which, "sample_min": float(r.min()), "refined_min": f, "a": a0.round(6).tolist(), "b": b0.round(6).tolist(),
                    "K_at": float(KI.K(a0[None], b0[None], m)[0][0])})
for o in out: print(json.dumps(o))

# Renyi-2 at T=2 (any b, identical others), d=1: exact sup over adaptive (a2,v2)(g1) on a 9x9 grid, both orders,
# against the conjectured pair. D_2(P||Q) = log int p^2/q; the inner integral depends only on (a2,v2)(g1).
import sys, json, numpy as np
from t2b1_adaptive import phi
res = {}
for s in [float(x) for x in sys.argv[1].split(",")]:
    g = np.linspace(-2 - 9 * s, 4 + 9 * s, 501); dg = g[1] - g[0]
    G1, G2 = np.meshgrid(g, g, indexing="ij")
    P = .5 * (phi(G1 - 2, s) * phi(G2, s) + phi(G1, s) * phi(G2 - 2, s))
    Q = .5 * (phi(G1 - 1, s) * phi(G2, s) + phi(G1, s) * phi(G2 - 1, s))
    conj = max(np.log((P * P / Q).sum() * dg * dg), np.log((Q * Q / P).sum() * dg * dg))
    grid = np.linspace(-1, 1, 9)
    A2, V2 = np.meshgrid(grid, grid, indexing="ij"); A2 = A2.ravel()[:, None]; V2 = V2.ravel()[:, None]
    fv = phi(g[None] - V2, s); fa = phi(g[None] - A2, s); f0 = phi(g[None], s)
    best = (-1e9, None)
    for rev in (False, True):
        for a1 in grid:
            for v1 in grid:
                tot = 0.0
                for x1 in g:
                    wa = .5 * phi(x1 - a1, s); w0 = .5 * phi(x1, s); wc = .5 * phi(x1 - v1, s)
                    p = wa * fv + wc * fa; q = w0 * fv + wc * f0
                    r = (q * q / p) if rev else (p * p / q)
                    tot += (r.sum(1) * dg).max() * dg
                if np.log(tot) > best[0]: best = (np.log(tot), (float(a1), float(v1), rev))
    print("sigma %.2f D2 conj %.6f adaptive %.6f at %s gain %+.3f%%" % (s, conj, best[0], best[1], 100 * (best[0] / conj - 1)), flush=True)
    res[str(s)] = {"conj": conj, "adaptive": best[0], "at": best[1]}
json.dump(res, open(sys.argv[2], "w"), indent=1)

"""Numerical triage of STRAT11's 13,368 OPEN leaves: per box, sample points, keep those passing the float version of
cover_face.necessary (without the scale ceiling), evaluate the N=6 numerator. NUMERICAL only - classifies, proves nothing.
usage: python open_box_diag.py <STRAT10 dir> <remaining_open_boxes.json> <out.json> [nsamp] [limit]"""
import sys, json, numpy as np
from fractions import Fraction as F
src, boxf, outf = [__import__("os").path.abspath(p) for p in sys.argv[1:4]]; ns = int(sys.argv[4]) if len(sys.argv) > 4 else 4000; lim = int(sys.argv[5]) if len(sys.argv) > 5 else None
sys.path.insert(0, src); import os; os.chdir(src)
from cover_face import polynomials
P = polynomials()[0]
E = np.array(list(P.keys()), dtype=np.int64); C = np.array([float(c) for c in P.values()])
rng = np.random.default_rng(7)

def num(X):  # X: (n,6)
    lx = np.log(np.abs(X) + 1e-300); sg = np.sign(X)
    out = np.zeros(len(X))
    for k in range(0, len(C), 400):
        e = E[k:k+400]; mag = np.exp(lx @ e.T); s = np.prod(np.where(e[None] % 2 == 1, sg[:, None, :], 1.0), axis=2)
        out += (mag * s) @ C[k:k+400]
    return out

def feas(X):
    t, v1, z1, v2, z2, z = X.T
    xs = [v1, v2, 1 - t - v1 - v2, t, -np.ones_like(t)]; ys = [z1, z2, -z - z1 - z2, np.zeros_like(t), z]
    ok = (t * t - 1 - z * z >= 0) & (v2 - v1 >= 0) & (xs[2] - v2 >= 0) & (xs[2] + 1 >= 0)
    for i in range(5): ok &= 4 * t - xs[i] ** 2 - ys[i] ** 2 >= 0
    for i in range(5):
        for j in range(i + 1, 5):
            if (i, j) != (3, 4): ok &= t + xs[i] * xs[j] + ys[i] * ys[j] >= 0
    M00 = sum(x * x for x in xs); M11 = sum(y * y for y in ys); M01 = sum(x * y for x, y in zip(xs, ys))
    dl = M00 * M11 - M01 ** 2; tau = M00 + M11
    ok &= (5 * t - M00 >= 0) & (5 * t - M11 >= 0) & ((5 * t - M00) * (5 * t - M11) - M01 ** 2 > 0) & (dl > 0) & (529 * dl - 60 * tau ** 2 > 0)
    return ok, dl, tau, t

boxes = json.load(open(boxf))['boxes'][:lim]
res = []
for b in boxes:
    lo = np.array([float(F(p[0])) for p in b['box']]); hi = np.array([float(F(p[1])) for p in b['box']])
    X = lo + (hi - lo) * rng.random((ns, 6))
    ok, dl, tau, t = feas(X)
    r = dict(node=b['node'], nfeas=int(ok.sum()))
    if ok.any():
        v = num(X[ok]); scale = (dl[ok] * t[ok] ** 3)  # crude normaliser
        i = np.argmin(v / scale); r.update(minv=float(v[i]), minrel=float((v / scale)[i]), neg=int((v < 0).sum()), pt=X[ok][i].tolist())
    res.append(r)
json.dump(res, open(outf, 'w'))
fe = [r for r in res if r['nfeas']]
print("boxes", len(res), "with feasible samples", len(fe), "with a negative sample", sum(1 for r in fe if r['neg']))
if fe:
    m = sorted(fe, key=lambda r: r['minrel'])[:5]
    for r in m: print(r['node'], r['nfeas'], "%.3e %.3e" % (r['minv'], r['minrel']), np.round(r['pt'], 4).tolist())
    qs = np.quantile([r['minrel'] for r in fe], [0, .01, .1, .5, .9]); print("minrel quantiles 0/1/10/50/90%:", qs)

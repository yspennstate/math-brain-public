"""Maximize c_G(p) over interior product biases for every distinct restriction class of Numaro's g (logs/restr_gates.pkl).
Multi-start pattern search in logit coordinates.  usage: restr_opt.py <npz> <kmin> <kmax> <starts> <tag>"""
import sys, os, time, json, pickle
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
F.lowprio()

npz, kmin, kmax, starts, tag = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
pot = F.Pot(npz, 0.0)
gates = pickle.load(open(os.path.join(HERE, "..", "logs", "restr_gates.pkl"), "rb"))
rng = np.random.default_rng(11)
res = []
t0 = time.time()
for k in range(kmin, kmax + 1):
    best_k = (-1e9, None)
    for ci, (v, free, assign) in enumerate(gates.get(k, [])):
        vals = v.astype(float)
        cu = float(F.cG(vals, np.full((1, k), 0.5), pot)[0][0])
        cands = [np.full(k, 0.5)]
        for s in range(starts):
            cands.append(1.0 / (1.0 + 2.0 ** (-rng.normal(0, 1.5, k))))
        best = (-1e9, None)
        for p0 in cands:
            c, p = F.maximize_c(vals, pot, p0, tol=1e-6)
            if c > best[0]:
                best = (c, p)
        c, p = best
        D, W, po, It = F.stats(vals, p[None, :], pot)
        row = dict(k=k, cls=ci, free=[int(x) for x in free], assign=[str(a) for a in assign], c_uniform=cu, c_best=c,
                   p=[float(x) for x in p], p_out=float(po[0]), W=float(W[0]), D=float(D[0]),
                   It=[float(x) for x in It[0]], ones=int((vals < 0).sum()))
        res.append(row)
        if c > best_k[0]:
            best_k = (c, row)
    if best_k[1] is not None:
        r = best_k[1]
        print("k=%2d  classes %3d  best c = %+.6e  (uniform %+.4e)  p_out=%.5f W=%.3e  p=%s  (%.0f s)"
              % (k, len(gates.get(k, [])), r["c_best"], r["c_uniform"], r["p_out"], r["W"],
                 ["%.4g" % x for x in r["p"]], time.time() - t0), flush=True)
json.dump(res, open(os.path.join(HERE, "..", "logs", "restr_opt_%s.json" % tag), "w"), indent=0)
res.sort(key=lambda r: -r["c_best"])
print("top 15 overall:")
for r in res[:15]:
    print("  k=%2d cls=%3d c=%+.6e c_unif=%+.4e p_out=%.5f W=%.3e min It=%.2e p=%s" %
          (r["k"], r["cls"], r["c_best"], r["c_uniform"], r["p_out"], r["W"], min(r["It"]), ["%.4g" % x for x in r["p"]]))

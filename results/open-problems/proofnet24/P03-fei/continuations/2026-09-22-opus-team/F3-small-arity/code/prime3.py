"""The composition-prime three-input NPN classes, and max over biases of c_G for each, for a given potential.
A 3-input gate is decomposable iff some pair block {i,j} has at most two distinct cofactors (functions of the third
input); prime = every pair block has at least three.  Search: 97^3 logit grid, the three coordinate lines solved onto the
shoulders of the dips of Gamma at 1/4, 1/2, 3/4, then pattern search from the best 40 points.
usage: prime3.py <npz> <c_margin> <tag>"""
import sys, os, time, json, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "2026-09-22-gate-reformulation"))
import fgate as F
F.lowprio()

npz, cm, tag = sys.argv[1], float(sys.argv[2]), sys.argv[3]
pot = F.Pot(npz, cm)
reps = np.load(os.path.join(HERE, "..", "..", "..", "2026-09-22-gate-reformulation", "npn_reps_k3.npy"))
k = 3; n = 8


def rows(tt, A):
    B = [i for i in range(k) if i not in A]
    rs = set()
    for a in range(1 << len(A)):
        r = []
        for b in range(1 << len(B)):
            x = 0
            for l, i in enumerate(A):
                x |= ((a >> l) & 1) << i
            for l, i in enumerate(B):
                x |= ((b >> l) & 1) << i
            r.append((int(tt) >> x) & 1)
        rs.add(tuple(r))
    return len(rs)


def depends(tt, i):
    return any(((int(tt) >> x) & 1) != ((int(tt) >> (x ^ (1 << i))) & 1) for x in range(n))


out = []
t0 = time.time()
for tt in reps:
    tt = int(tt)
    ess = [i for i in range(k) if depends(tt, i)]
    prime = len(ess) == 3 and all(rows(tt, A) >= 3 for A in itertools.combinations(range(k), 2))
    trues = [x for x in range(n) if (tt >> x) & 1]
    desc = "true points " + ",".join(format(x, "03b")[::-1] for x in trues)
    if not prime:
        out.append(dict(tt=tt, prime=False, ess=len(ess), desc=desc)); continue
    vals = F.pm_from_int(tt, k)
    u = np.linspace(-9, 9, 97)
    U = np.array(np.meshgrid(u, u, u, indexing="ij")).reshape(3, -1).T
    P = 1 / (1 + 2.0 ** (-U))
    c = np.concatenate([F.cG(vals, P[i:i + 200000], pot, 1e-10)[0] for i in range(0, len(P), 200000)])
    order = list(np.argsort(-c)[:30])
    starts = [P[j] for j in order]
    # dips: solve one coordinate so that p_out hits a shoulder target, the others on a coarse grid
    targets = [b + s * d for b in (0.25, 0.5, 0.75) for d in (0.0012, 0.0026, 0.004) for s in (-1, 1)]
    ug = 1 / (1 + 2.0 ** (-np.linspace(-6, 6, 25)))
    cand = []
    for i in range(k):
        for a in ug:
            for b in ug:
                for tgt in targets:
                    # p_out is affine in p_i: p_out = e0 + (e1 - e0) p_i
                    pv = np.array([a, b]); PP = np.zeros((2, 3)); o = [j for j in range(k) if j != i]
                    PP[:, o] = pv; PP[0, i] = 0.0; PP[1, i] = 1.0
                    e = []
                    for r in range(2):
                        pr = np.prod(np.where(((np.arange(n)[:, None] >> np.arange(k)) & 1) == 1, PP[r], 1 - PP[r]), 1)
                        e.append(float(((vals < 0) * pr).sum()))
                    if abs(e[1] - e[0]) < 1e-12:
                        continue
                    pi = (tgt - e[0]) / (e[1] - e[0])
                    if 1e-6 < pi < 1 - 1e-6:
                        q = PP[0].copy(); q[i] = pi; cand.append(q)
    cand = np.array(cand)
    cc = F.cG(vals, cand, pot, 1e-10)[0]
    for j in np.argsort(-cc)[:10]:
        starts.append(cand[j])
    best = (-1e9, None)
    for p0 in starts:
        cv, p = F.maximize_c(vals, pot, np.clip(p0, 1e-6, 1 - 1e-6), tol=1e-8)
        if cv > best[0]:
            best = (cv, p)
    D, W, po, It = F.stats(vals, best[1][None, :], pot)
    out.append(dict(tt=tt, prime=True, desc=desc, c_max=best[0], p=[float(x) for x in best[1]], p_out=float(po[0]),
                    W=float(W[0]), It=[float(x) for x in It[0]], grid_max=float(c.max()), dip_max=float(cc.max())))
    print("tt=%3d %-40s c_max=%+.6e (grid %+.3e, dip starts %+.3e)  p=%s p_out=%.5f min It=%.2e (%.0f s)"
          % (tt, desc, best[0], c.max(), cc.max(), ["%.5g" % x for x in best[1]], po[0], It[0].min(), time.time() - t0), flush=True)
print("classes: %d; composition-prime: %d" % (len(out), sum(1 for r in out if r["prime"])))
for r in out:
    if not r["prime"]:
        print("  not prime: tt=%3d essential inputs %d  %s" % (r["tt"], r["ess"], r["desc"]))
json.dump(out, open(os.path.join(HERE, "..", "logs", "prime3_%s.json" % tag), "w"), indent=0)

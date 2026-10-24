"""Hill climbing over ALL k-input truth tables (not only monotone) with the bias optimized jointly: at the current bias,
evaluate every single-entry flip in one batch and take the best (with a small annealing temperature); every few steps
re-optimize the bias by pattern search.  Reports the best c with every input carrying influence >= 1e-3.
usage: hill.py <k> <npz> <restarts> <seed> <tag> [steps]"""
import sys, os, time, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
F.lowprio()

k = int(sys.argv[1]); npz = sys.argv[2]; restarts = int(sys.argv[3]); seed = int(sys.argv[4]); tag = sys.argv[5]
steps = int(sys.argv[6]) if len(sys.argv) > 6 else 300
pot = F.Pot(npz, 0.0)
n = 1 << k
rng = np.random.default_rng(seed)
FL = np.ones((n, n)) - 2 * np.eye(n)          # row j flips entry j


def score(vals, p):
    c, D, W = F.cG(vals, p[None, :], pot, 1e-9)
    return float(c[0])


def genuine_c(vals, p):
    D, W, po, It = F.stats(vals, p[None, :], pot)
    if W[0] <= 1e-9:
        return -1e9, It[0]
    return float(-D[0] / W[0]), It[0]


def init_table():
    r = rng.random()
    if r < 0.4:                                  # random monotone DNF
        terms = [rng.choice(k, size=rng.integers(1, min(4, k) + 1), replace=False) for _ in range(rng.integers(2, 2 + k))]
        x = np.arange(n)
        tr = np.zeros(n, bool)
        for t in terms:
            m = sum(1 << int(i) for i in t)
            tr |= (x & m) == m
        return np.where(tr, -1.0, 1.0)
    if r < 0.6:                                  # random threshold
        w = rng.normal(0, 1, k); th = rng.normal(0, 1)
        x = ((np.arange(n)[:, None] >> np.arange(k)[None, :]) & 1) * 2 - 1
        return np.where(x @ w > th, -1.0, 1.0)
    d = rng.uniform(0.2, 0.8)
    return np.where(rng.random(n) < d, -1.0, 1.0)


t0 = time.time()
glob = []
for rs in range(restarts):
    vals = init_table()
    U = rng.normal(0, 1.2, k); U[rng.random(k) < 0.4] = 0.0
    p = 1.0 / (1.0 + 2.0 ** (-U))
    cur = score(vals, p)
    best = (-1e9, None, None)
    T = 2e-3
    for st in range(steps):
        cand = vals[None, :] * FL
        c = F.cG(cand, np.broadcast_to(p, (n, k)), pot, 1e-9)[0]
        j = int(np.argmax(c))
        if c[j] > cur or rng.random() < np.exp((c[j] - cur) / T):
            vals = cand[j]; cur = float(c[j])
        T *= 0.985
        if st % 20 == 19 or st == steps - 1:
            cur, p = F.maximize_c(vals, pot, p, tol=1e-4)
            gc, It = genuine_c(vals, p)
            if It.min() >= 1e-3 and gc > best[0]:
                best = (gc, vals.copy(), p.copy())
    if best[1] is not None:
        c, p = F.maximize_c(best[1], pot, best[2], tol=1e-7)
        gc, It = genuine_c(best[1], p)
        if It.min() >= 1e-3:
            tt = int(sum(1 << x for x in range(n) if best[1][x] < 0))
            glob.append(dict(c=gc, tt=hex(tt), p=[float(v) for v in p], minIt=float(It.min()), ones=int((best[1] < 0).sum())))
    if rs % 10 == 9 or rs == restarts - 1:
        glob.sort(key=lambda r: -r["c"])
        b = glob[0] if glob else None
        print("restart %d/%d  best genuine c = %s  (%.0f s)" % (rs + 1, restarts, ("%+.5e tt=%s p=%s" % (b["c"], b["tt"], ["%.3g" % v for v in b["p"]])) if b else "none", time.time() - t0), flush=True)
glob.sort(key=lambda r: -r["c"])
json.dump(glob[:50], open(os.path.join(HERE, "..", "logs", "hill_%s.json" % tag), "w"), indent=0)
print("top 10:")
for r in glob[:10]:
    print("  c=%+.6e  tt=%s  ones=%d  minIt=%.2e  p=%s" % (r["c"], r["tt"], r["ones"], r["minIt"], ["%.4g" % v for v in r["p"]]))

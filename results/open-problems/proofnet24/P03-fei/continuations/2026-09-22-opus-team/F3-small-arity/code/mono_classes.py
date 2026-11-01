"""Monotone gates on n inputs: reduce to one representative per permutation-invariant key (number of true points,
sorted edge-boundary counts, sorted |Walsh| multiset), screen each representative at R random bias vectors (logit
normal) plus all-1/2, then bias-optimize the best ones.  usage: mono_classes.py <n> <npz> <R> <nopt> <tag>"""
import sys, os, time, json, hashlib
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
F.lowprio()

n = int(sys.argv[1]); npz = sys.argv[2]; R = int(sys.argv[3]); nopt = int(sys.argv[4]); tag = sys.argv[5]
pot = F.Pot(npz, 0.0)
N2 = 1 << n


def monotone(n):
    if n == 0:
        return np.array([0, 1], dtype=np.uint64)
    prev = monotone(n - 1)
    half = np.uint64(1 << (n - 1))
    return np.concatenate([prev[(prev & ~f1) == 0] | (f1 << half) for f1 in prev])


t0 = time.time()
M = monotone(n)
full = np.uint64(0xFFFFFFFFFFFFFFFF) if n == 6 else np.uint64((1 << N2) - 1)
M = M[(M != 0) & (M != full)]
print("n=%d: %d nonconstant monotone functions (%.1f s)" % (n, len(M), time.time() - t0), flush=True)
bits = np.arange(N2, dtype=np.uint64)
keys = {}
CH = 200000
for i0 in range(0, len(M), CH):
    blk = M[i0:i0 + CH]
    v = (1 - 2 * ((blk[:, None] >> bits[None, :]) & np.uint64(1)).astype(np.int32))
    w = v.copy(); h = 1
    while h < N2:
        w = w.reshape(len(blk), -1, 2 * h); a = w[:, :, :h].copy(); b = w[:, :, h:].copy()
        w[:, :, :h] = a + b; w[:, :, h:] = a - b; w = w.reshape(len(blk), N2); h *= 2
    sq = (w * w).astype(np.int64)
    inf = np.stack([sq[:, (np.arange(N2) >> i) & 1 == 1].sum(1) for i in range(n)], 1)
    inf.sort(axis=1)
    aw = np.sort(np.abs(w), axis=1)
    ones = (v < 0).sum(1)
    K = np.concatenate([ones[:, None], inf, aw], 1).astype(np.int64)
    for j in range(len(blk)):
        kk = K[j].tobytes()
        if kk not in keys:
            keys[kk] = int(blk[j])
print("distinct invariant keys: %d (%.0f s)" % (len(keys), time.time() - t0), flush=True)
reps = np.array(list(keys.values()), dtype=np.uint64)
V = 1.0 - 2.0 * ((reps[:, None] >> bits[None, :]) & np.uint64(1)).astype(float)
rng = np.random.default_rng(3)
best = np.full(len(reps), -1e9); bestp = np.zeros((len(reps), n))
cu = F.cG(V, np.full((len(reps), n), 0.5), pot, 1e-9)[0]
best = cu.copy(); bestp[:] = 0.5
for r in range(R):
    U = rng.normal(0, 1.6, (len(reps), n))
    U[rng.random(U.shape) < 0.35] = 0.0
    P = 1.0 / (1.0 + 2.0 ** (-U))
    c = F.cG(V, P, pot, 1e-9)[0]
    upd = c > best
    best[upd] = c[upd]; bestp[upd] = P[upd]
    if r % 64 == 0:
        print("  screen round %d/%d  max c = %+.5e  (%.0f s)" % (r, R, best.max(), time.time() - t0), flush=True)
order = np.argsort(-best)
out = []
for j in order[:nopt]:
    c, p = F.maximize_c(V[j], pot, bestp[j], tol=1e-7)
    c2, p2 = F.maximize_c(V[j], pot, np.full(n, 0.5), tol=1e-7)
    if c2 > c:
        c, p = c2, p2
    D, W, po, It = F.stats(V[j], p[None, :], pot)
    out.append(dict(tt=hex(int(reps[j])), c_uniform=float(cu[j]), c_screen=float(best[j]), c_opt=float(c),
                    p=[float(x) for x in p], p_out=float(po[0]), W=float(W[0]), It=[float(x) for x in It[0]]))
out.sort(key=lambda r: -r["c_opt"])
print("optimized %d representatives (%.0f s); best 25:" % (len(out), time.time() - t0))
for r in out[:25]:
    print("  tt=%s  c_opt=%+.6e  (screen %+.3e, uniform %+.3e)  p_out=%.5f  min It=%.2e  p=%s" %
          (r["tt"], r["c_opt"], r["c_screen"], r["c_uniform"], r["p_out"], min(r["It"]), ["%.4g" % x for x in r["p"]]))
json.dump(out, open(os.path.join(HERE, "..", "logs", "mono_classes_%s.json" % tag), "w"), indent=0)

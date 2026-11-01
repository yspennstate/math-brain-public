"""Every nonconstant monotone gate on n inputs, no deduplication: each function (all input permutations are present in
the list) is screened at the all-1/2 vector and R random bias vectors (logit-normal, 35 per cent of coordinates at 1/2);
the best distinct screened functions are then bias-optimized.  usage: mono_full.py <n> <npz> <R> <nopt> <tag>"""
import sys, os, time, json
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
print("n=%d: %d nonconstant monotone functions" % (n, len(M)), flush=True)
bits = np.arange(N2, dtype=np.uint64)


def Vof(lo, hi):
    return 1.0 - 2.0 * ((M[lo:hi][:, None] >> bits[None, :]) & np.uint64(1)).astype(float)


CH = 100000
best = np.full(len(M), -1e9); bestp = np.full((len(M), n), 0.5, dtype=np.float32)
rng = np.random.default_rng(13)
for r in range(R + 1):
    for i in range(0, len(M), CH):
        j = min(i + CH, len(M))
        if r == 0:
            P = np.full((j - i, n), 0.5)
        else:
            U = rng.normal(0, 1.6, (j - i, n)); U[rng.random(U.shape) < 0.35] = 0.0
            P = 1.0 / (1.0 + 2.0 ** (-U))
        c = F.cG(Vof(i, j), P, pot, 1e-9)[0]
        upd = c > best[i:j]
        best[i:j][upd] = c[upd]; bestp[i:j][upd] = P[upd]
    print("  round %d/%d  max c = %+.5e  (%.0f s)" % (r, R, best.max(), time.time() - t0), flush=True)
order = np.argsort(-best)
out = []; seen = set()
for j in order:
    if len(out) >= nopt:
        break
    key = (round(float(best[j]), 8))
    if key in seen:
        continue
    seen.add(key)
    Vj = Vof(j, j + 1)[0]
    c, p = F.maximize_c(Vj, pot, bestp[j].astype(float), tol=1e-7)
    D, W, po, It = F.stats(Vj, p[None, :], pot)
    out.append(dict(tt=hex(int(M[j])), c_screen=float(best[j]), c_opt=float(c), p=[float(x) for x in p],
                    p_out=float(po[0]), W=float(W[0]), It=[float(x) for x in It[0]]))
out.sort(key=lambda r: -r["c_opt"])
print("optimized %d (%.0f s); best 20:" % (len(out), time.time() - t0))
for r in out[:20]:
    print("  tt=%s  c_opt=%+.6e  (screen %+.3e)  p_out=%.5f  min It=%.2e  p=%s" %
          (r["tt"], r["c_opt"], r["c_screen"], r["p_out"], min(r["It"]), ["%.4g" % x for x in r["p"]]))
json.dump(out, open(os.path.join(HERE, "..", "logs", "mono_full_%s.json" % tag), "w"), indent=0)

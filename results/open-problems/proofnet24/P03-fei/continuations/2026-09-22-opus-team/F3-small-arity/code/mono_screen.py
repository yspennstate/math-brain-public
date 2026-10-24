"""Every monotone Boolean function on n = 5 or 6 inputs (7,581 / 7,828,354 of them), screened for c_G at a family of bias
multisets.  Because the list is closed under input permutation, one bias vector per multiset covers every assignment of
those biases to inputs.  The top candidates are then bias-optimized by multi-start pattern search.
usage: mono_screen.py <n> <npz> <ntop> <tag>"""
import sys, os, time, json, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
F.lowprio()

n = int(sys.argv[1]); npz = sys.argv[2]; ntop = int(sys.argv[3]); tag = sys.argv[4]
pot = F.Pot(npz, 0.0)


def monotone(n):
    if n == 0:
        return np.array([0, 1], dtype=np.uint64)          # constant false, constant true (bit 0 = the empty point)
    prev = monotone(n - 1)
    half = np.uint64(1 << (n - 1))
    out = []
    for f1 in prev:
        f0s = prev[(prev & ~f1) == 0]
        out.append(f0s | (f1 << half))
    return np.concatenate(out)


t0 = time.time()
M = monotone(n)
N2 = 1 << n
M = M[(M != 0) & (M != np.uint64((1 << N2) - 1))] if n < 6 else M[(M != 0) & (M != np.uint64(0xFFFFFFFFFFFFFFFF))]
print("n=%d: %d nonconstant monotone functions (%.1f s)" % (n, len(M), time.time() - t0), flush=True)

levels = [0.5, 0.42, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.58, 0.65, 0.7, 0.8, 0.9]
multis = set()
for a in levels:
    for b in levels:
        for m in range(0, n + 1):
            multis.add(tuple(sorted([a] * m + [b] * (n - m))))
rng = np.random.default_rng(7)
for _ in range(40):
    multis.add(tuple(sorted(rng.choice(levels, n))))
multis = sorted(multis)
print("%d bias multisets" % len(multis), flush=True)

bits = np.arange(N2, dtype=np.uint64)
CH = 60000
best = np.full(len(M), -1e9); barg = np.zeros(len(M), dtype=np.int32)
for mi, ms in enumerate(multis):
    P1 = np.array(ms, float)
    for i0 in range(0, len(M), CH):
        blk = M[i0:i0 + CH]
        vals = 1.0 - 2.0 * ((blk[:, None] >> bits[None, :]) & np.uint64(1)).astype(float)
        P = np.broadcast_to(P1, (len(blk), n))
        c, D, W = F.cG(vals, P, pot, wmin=1e-9)
        upd = c > best[i0:i0 + CH]
        best[i0:i0 + CH][upd] = c[upd]; barg[i0:i0 + CH][upd] = mi
    if mi % 50 == 0:
        print("  multiset %d/%d  running max c = %+.4e  (%.0f s)" % (mi, len(multis), best.max(), time.time() - t0), flush=True)
order = np.argsort(-best)
print("screen done: max screened c = %+.6e (%.0f s); top screened:" % (best[order[0]], time.time() - t0), flush=True)
for j in order[:10]:
    print("   tt=%#x  c=%+.4e  at multiset %s" % (int(M[j]), best[j], multis[barg[j]]))
# de-duplicate the top list up to permutation (canonical = min over permutations) and optimize
def canon(tt):
    """permutation-invariant key: number of true points, sorted influences, sorted |Walsh| (integers)"""
    v = 1 - 2 * np.array([(int(tt) >> x) & 1 for x in range(N2)], dtype=np.int64)
    w = v.copy(); h = 1
    while h < N2:
        w = w.reshape(-1, 2 * h); a = w[:, :h].copy(); b = w[:, h:].copy()
        w[:, :h] = a + b; w[:, h:] = a - b; w = w.ravel(); h *= 2
    sq = w * w
    inf = [int(sq[[S for S in range(N2) if (S >> i) & 1]].sum()) for i in range(n)]
    return (int((v < 0).sum()), tuple(sorted(inf)), tuple(sorted(np.abs(w).tolist())))
done = set(); out = []
for j in order:
    if len(out) >= ntop:
        break
    cn = canon(M[j])
    if cn in done:
        continue
    done.add(cn)
    vals = 1.0 - 2.0 * np.array([(int(M[j]) >> x) & 1 for x in range(N2)], float)
    p0s = [np.array(multis[barg[j]])]
    # the multiset is sorted; the function's own orientation may need a permutation: try every distinct permutation
    cand = set(itertools.permutations(multis[barg[j]]))
    scored = []
    for pp in cand:
        cc = float(F.cG(vals, np.array(pp)[None, :], pot, 1e-9)[0][0]); scored.append((cc, pp))
    scored.sort(reverse=True)
    bestc, bestp = -1e9, None
    for cc, pp in scored[:3]:
        c, p = F.maximize_c(vals, pot, np.array(pp), tol=1e-7)
        if c > bestc:
            bestc, bestp = c, p
    D, W, po, It = F.stats(vals, bestp[None, :], pot)
    out.append(dict(tt=hex(int(M[j])), canon=str(cn[:2]), c_screen=float(best[j]), c_opt=bestc, p=[float(x) for x in bestp],
                    p_out=float(po[0]), W=float(W[0]), It=[float(x) for x in It[0]]))
    print("  opt %3d  tt=%s  screen %+.4e  -> optimized c = %+.6e  p_out=%.4f  min It=%.2e  p=%s"
          % (len(out), hex(int(M[j])), best[j], bestc, po[0], It[0].min(), ["%.4g" % x for x in bestp]), flush=True)
json.dump(out, open(os.path.join(HERE, "..", "logs", "mono_screen_%s.json" % tag), "w"), indent=0)
print("done (%.0f s)" % (time.time() - t0))

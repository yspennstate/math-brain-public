"""Screen aimed at the dips of the read-once potential.  Gamma_RO has narrow V-shaped minima at dyadic measures (slope
+-30 at 1/2, a bump of +0.047 at 1/2 +- 0.0026), so a gate asks the most when its output measure sits on a dip's
shoulder.  For a monotone gate G, every nonempty input subset S and every target t on a shoulder, the common bias q of the
inputs in S (the others at 1/2) is solved by bisection so that p_out = t; c_G is evaluated there, and the best starts are
then bias-optimized.  Input lists: 'mono5' / 'mono6' (one representative per permutation class of monotone gates, found by
a fine spectral invariant), or 'numaro7' (the arity-7 restriction classes of Numaro's g: the positive control).
usage: cusp_screen.py <list> <npz> <nopt> <tag>"""
import sys, os, time, json, itertools, pickle
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
F.lowprio()

which, npz, nopt, tag = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
pot = F.Pot(npz, 0.0)
t0 = time.time()


def monotone(n):
    if n == 0:
        return np.array([0, 1], dtype=np.uint64)
    prev = monotone(n - 1)
    half = np.uint64(1 << (n - 1))
    return np.concatenate([prev[(prev & ~f1) == 0] | (f1 << half) for f1 in prev])


def mono_reps(n):
    N2 = 1 << n
    M = monotone(n)
    full = np.uint64(0xFFFFFFFFFFFFFFFF) if n == 6 else np.uint64((1 << N2) - 1)
    M = M[(M != 0) & (M != full)]
    bits = np.arange(N2, dtype=np.uint64)
    Ssz = np.array([bin(S).count("1") for S in range(N2)])
    memb = ((np.arange(N2)[:, None] >> np.arange(n)[None, :]) & 1).astype(bool)
    keys = {}
    CH = 100000
    for i0 in range(0, len(M), CH):
        blk = M[i0:i0 + CH]
        v = (1 - 2 * ((blk[:, None] >> bits[None, :]) & np.uint64(1)).astype(np.int64))
        w = v.copy(); h = 1
        while h < N2:
            w = w.reshape(len(blk), -1, 2 * h); a = w[:, :, :h].copy(); b = w[:, :, h:].copy()
            w[:, :, :h] = a + b; w[:, :, h:] = a - b; w = w.reshape(len(blk), N2); h *= 2
        w2 = w * w; w4 = w2 * w2; w3 = np.abs(w) * w2
        prof = np.stack([np.stack([w2[:, memb[:, i]].sum(1), w4[:, memb[:, i]].sum(1), w3[:, memb[:, i]].sum(1),
                                   (w2 * Ssz)[:, memb[:, i]].sum(1)], 1) for i in range(n)], 1)   # (B, n, 4)
        # pairwise second-order: sum over S containing both i and j of w^2, sorted per row -> order-free summary
        pair = np.stack([np.stack([w2[:, memb[:, i] & memb[:, j]].sum(1) for j in range(n)], 1) for i in range(n)], 1)
        order = np.lexsort(prof.transpose(2, 0, 1)[::-1].reshape(4, -1)).reshape(-1)   # not used for exactness
        for r in range(len(blk)):
            pr = [tuple(prof[r, i].tolist()) + tuple(sorted(pair[r, i].tolist())) for i in range(n)]
            kk = (int((v[r] < 0).sum()), tuple(sorted(pr)))
            if kk not in keys:
                keys[kk] = int(blk[r])
    reps = np.array(list(keys.values()), dtype=np.uint64)
    V = 1.0 - 2.0 * ((reps[:, None] >> bits[None, :]) & np.uint64(1)).astype(float)
    return V, [hex(int(x)) for x in reps]


if which == "mono5":
    V, names = mono_reps(5); k = 5
elif which == "mono6":
    V, names = mono_reps(6); k = 6
elif which == "numaro7":
    gates = pickle.load(open(os.path.join(HERE, "..", "logs", "restr_gates.pkl"), "rb"))
    V = np.array([g[0].astype(float) for g in gates[7]]); names = ["numaro7_cls%d" % i for i in range(len(V))]; k = 7
else:
    raise SystemExit("unknown list")
G = len(V); n = 1 << k
print("%s: %d gates of arity %d (%.0f s)" % (which, G, k, time.time() - t0), flush=True)

targets = []
for base in (0.5, 0.25, 0.75):
    for d in (0.0012, 0.0026, 0.004, 0.007):
        targets += [base - d, base + d]
targets = np.array(sorted(set(targets)))
subsets = [S for S in range(1, 1 << k)]
xbits = ((np.arange(n)[:, None] >> np.arange(k)[None, :]) & 1)
tru = (V < 0).astype(float)                                                        # (G, n)

best = np.full(G, -1e9); bestp = np.full((G, k), 0.5)
for S in subsets:
    m = np.array([(S >> i) & 1 for i in range(k)], bool)
    # p_out(q) = sum_j a_j q^j (1-q)^(s-j), a_j = 2^-(k-s) #{true x : |x cap S| = j}; increasing in q (monotone G)
    s = int(m.sum())
    cnt = (xbits[:, m].sum(1))                                    # |x cap S| for each point x
    OH = (cnt[:, None] == np.arange(s + 1)[None, :]).astype(float)
    A = (tru @ OH) * 0.5 ** (k - s)                               # (G, s+1)
    lo = np.full((G, len(targets)), 1e-7); hi = np.full((G, len(targets)), 1 - 1e-7)
    jj = np.arange(s + 1)
    for it in range(40):
        mid = 0.5 * (lo + hi)
        terms = mid[:, :, None] ** jj[None, None, :] * (1 - mid[:, :, None]) ** (s - jj)[None, None, :]
        po = np.einsum("gtj,gj->gt", terms, A)
        up = po < targets[None, :]
        lo = np.where(up, mid, lo); hi = np.where(up, hi, mid)
    q = 0.5 * (lo + hi)
    for tj in range(len(targets)):
        P = np.full((G, k), 0.5); P[:, m] = q[:, tj][:, None]
        c = F.cG(V, P, pot, 1e-9)[0]
        upd = c > best
        best[upd] = c[upd]; bestp[upd] = P[upd]
    if S % 8 == 0 or S == subsets[-1]:
        print("  subset %d/%d  max screened c = %+.5e  (%.0f s)" % (S, len(subsets), best.max(), time.time() - t0), flush=True)
order = np.argsort(-best)
out = []
for j in order[:nopt]:
    c, p = F.maximize_c(V[j], pot, bestp[j], tol=1e-7)
    D, W, po, It = F.stats(V[j], p[None, :], pot)
    out.append(dict(name=names[j], c_screen=float(best[j]), c_opt=float(c), p=[float(x) for x in p], p_out=float(po[0]),
                    W=float(W[0]), It=[float(x) for x in It[0]]))
out.sort(key=lambda r: -r["c_opt"])
print("optimized %d of %d (%.0f s); best 15:" % (len(out), G, time.time() - t0))
for r in out[:15]:
    print("  %s  c_opt=%+.6e  (screen %+.3e)  p_out=%.5f  min It=%.2e  p=%s" %
          (r["name"], r["c_opt"], r["c_screen"], r["p_out"], min(r["It"]), ["%.4g" % x for x in r["p"]]))
print("max screened c over all %d gates: %+.6e" % (G, best.max()))
json.dump(dict(screen_max=float(best.max()), top=out), open(os.path.join(HERE, "..", "logs", "cusp_%s.json" % tag), "w"), indent=0)

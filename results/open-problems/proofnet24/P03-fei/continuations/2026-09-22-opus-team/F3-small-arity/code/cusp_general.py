"""Dip-targeted screen without monotonicity assumptions.  For every gate in the list, every nonempty input subset S (common
bias q on S, the others at 1/2, and also the others at 1/4 and 3/4) and every target t on a shoulder of the potential's dips
at 1/4, 1/2, 3/4, all roots q of p_out(q) = t are found (p_out is a polynomial in q: sign changes on a 400-point logit grid,
then bisection); c_G is evaluated at every root and the best points are bias-optimized.
Lists: npn3, npn4 (all NPN classes, gate-reformulation/npn_reps_k*.npy), mono5all (all 7,581 monotone 5-input functions).
usage: cusp_general.py <list> <npz> <nopt> <tag>"""
import sys, os, time, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
F.lowprio()

which, npz, nopt, tag = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
pot = F.Pot(npz, 0.0)
t0 = time.time()
GR = os.path.join(HERE, "..", "..", "..", "2026-09-22-gate-reformulation")


def monotone(n):
    if n == 0:
        return np.array([0, 1], dtype=np.uint64)
    prev = monotone(n - 1)
    half = np.uint64(1 << (n - 1))
    return np.concatenate([prev[(prev & ~f1) == 0] | (f1 << half) for f1 in prev])


if which in ("npn3", "npn4"):
    k = int(which[-1]); reps = np.load(os.path.join(GR, "npn_reps_k%d.npy" % k))
    tts = [int(t) for t in reps]
elif which == "mono5all":
    k = 5; M = monotone(5); tts = [int(t) for t in M if t != 0 and t != (1 << 32) - 1]
else:
    raise SystemExit("unknown list")
n = 1 << k
V = np.array([[1.0 - 2.0 * ((t >> x) & 1) for x in range(n)] for t in tts])
depends = np.array([[np.any(V[g] != V[g][np.arange(n) ^ (1 << i)]) for i in range(k)] for g in range(len(V))])
keep = depends.all(1)
V = V[keep]; tts = [t for t, kp in zip(tts, keep) if kp]
G = len(V)
print("%s: %d gates depending on all %d inputs (%.0f s)" % (which, G, k, time.time() - t0), flush=True)
tru = (V < 0).astype(float)
xbits = ((np.arange(n)[:, None] >> np.arange(k)[None, :]) & 1)
targets = np.array(sorted(set(b + s * d for b in (0.25, 0.5, 0.75) for d in (0.0012, 0.0026, 0.004, 0.007) for s in (-1, 1))))
qg = 1 / (1 + 2.0 ** (-np.linspace(-12, 12, 400)))
best = np.full(G, -1e9); bestp = np.full((G, k), 0.5)
for rest in (0.5, 0.25, 0.75):
    for S in range(1, 1 << k):
        m = np.array([(S >> i) & 1 for i in range(k)], bool)
        s = int(m.sum())
        # p_out(q) = sum_x tru(x) prod: coefficient per |x cap S| = j, times the product over the others at bias `rest`
        cnt = xbits[:, m].sum(1); cnto = xbits[:, ~m].sum(1)
        w_rest = rest ** cnto * (1 - rest) ** ((k - s) - cnto)
        OH = (cnt[:, None] == np.arange(s + 1)[None, :]).astype(float) * w_rest[:, None]
        A = tru @ OH                                     # (G, s+1)
        jj = np.arange(s + 1)
        basis = qg[:, None] ** jj[None, :] * (1 - qg[:, None]) ** (s - jj)[None, :]   # (Q, s+1)
        PO = A @ basis.T                                 # (G, Q)
        for t in targets:
            f = PO - t
            sc = np.nonzero(np.sign(f[:, :-1]) * np.sign(f[:, 1:]) < 0)
            if len(sc[0]) == 0:
                continue
            gi, qi = sc
            lo = qg[qi].copy(); hi = qg[qi + 1].copy()
            flo = f[gi, qi]
            for it in range(45):
                mid = 0.5 * (lo + hi)
                bm = mid[:, None] ** jj[None, :] * (1 - mid[:, None]) ** (s - jj)[None, :]
                fm = (A[gi] * bm).sum(1) - t
                same = np.sign(fm) == np.sign(flo)
                lo = np.where(same, mid, lo); flo = np.where(same, fm, flo); hi = np.where(same, hi, mid)
            q = 0.5 * (lo + hi)
            P = np.full((len(gi), k), rest); P[:, m] = q[:, None]
            c = F.cG(V[gi], P, pot, 1e-9)[0]
            for r in np.nonzero(c > best[gi])[0]:
                g = gi[r]
                if c[r] > best[g]:
                    best[g] = c[r]; bestp[g] = P[r]
    print("  rest=%.2f done: max screened c = %+.5e  (%.0f s)" % (rest, best.max(), time.time() - t0), flush=True)
order = np.argsort(-best)
out = []
for j in order[:nopt]:
    c, p = F.maximize_c(V[j], pot, bestp[j], tol=1e-7)
    D, W, po, It = F.stats(V[j], p[None, :], pot)
    out.append(dict(tt=hex(tts[j]), c_screen=float(best[j]), c_opt=float(c), p=[float(x) for x in p], p_out=float(po[0]),
                    W=float(W[0]), It=[float(x) for x in It[0]]))
out.sort(key=lambda r: -r["c_opt"])
print("optimized %d of %d (%.0f s); best 10:" % (len(out), G, time.time() - t0))
for r in out[:10]:
    print("  tt=%s  c_opt=%+.6e  (screen %+.3e)  p_out=%.5f  min It=%.2e  p=%s" %
          (r["tt"], r["c_opt"], r["c_screen"], r["p_out"], min(r["It"]), ["%.4g" % x for x in r["p"]]))
print("max screened c over all %d gates: %+.6e" % (G, best.max()))
json.dump(dict(screen_max=float(best.max()), top=out), open(os.path.join(HERE, "..", "logs", "cusp_%s.json" % tag), "w"), indent=0)

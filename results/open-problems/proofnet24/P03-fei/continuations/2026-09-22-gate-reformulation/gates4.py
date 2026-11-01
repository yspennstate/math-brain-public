"""The gate inequality over NPN class representatives, batched over bias vectors.

D_G(p) = sum_i It_i(G;p) (Gamma(p_i)+h(V_i))/V_i - Ht_G(p) - Gamma(p_out) >= 0 is the condition for the
induction over read-once formulas built from G to close.  D_G is NPN-invariant once the bias grid is symmetric
under p -> 1-p and closed under permutation, so one representative per class suffices: 4 classes at arity 2,
14 at arity 3, 222 at arity 4.  Gates are split DEGENERATE / READONCE / GENUINE; only GENUINE gates can ask for
a constant that arity two does not already give.
usage: gates4.py <k> <npz> <c> <tag> <nx> [batch]"""
import sys, os, math, time, json
import numpy as np
import gam, decomp

def grid_values(nx):
    xs = np.unique(np.concatenate([np.linspace(1.0, 6.0, nx), np.array([7., 8., 9., 10., 12., 14., 17., 20., 25., 30.])]))
    p = 2.0 ** -xs
    return np.unique(np.concatenate([p, 1 - p]))

def combos(vals, k):
    out = []
    def rec(start, cur):
        if len(cur) == k:
            out.append(tuple(cur)); return
        for i in range(start, len(vals)):
            cur.append(vals[i]); rec(i, cur); cur.pop()
    rec(0, [])
    return np.array(out)

if __name__ == "__main__":
    k = int(sys.argv[1]); npz = sys.argv[2]; c = float(sys.argv[3]); tag = sys.argv[4]
    nx = int(sys.argv[5]); BATCH = int(sys.argv[6]) if len(sys.argv) > 6 else 512
    n = 1 << k
    reps = np.load("npn_reps_k%d.npy" % k)
    TT = 1.0 - 2.0 * ((reps[:, None] >> np.arange(n)[None, :]) & 1).astype(np.float64)
    RO, degenerate = decomp.classify(k)
    lab = np.array(["DEGENERATE" if degenerate(int(t)) else ("READONCE" if int(t) in RO else "GENUINE") for t in reps])
    cls = {nm: np.flatnonzero(lab == nm) for nm in ("DEGENERATE", "READONCE", "GENUINE") if (lab == nm).any()}
    names = list(cls.keys())
    SEL = np.array([[(S >> i) & 1 for i in range(k)] for S in range(n)], float)
    Gm = gam.Gam(npz, c)
    vals = grid_values(nx); B = combos(list(vals), k)
    print("arity %d: %d NPN classes (%s); %d bias vectors from %d grid values; c=%.5g Gamma(1/2)=%.7f"
          % (k, len(reps), ", ".join("%s %d" % (nm, len(cls[nm])) for nm in names), len(B), len(vals), c, Gm.cap), flush=True)
    best = {nm: (1e9, -1, None) for nm in names}
    t0 = time.perf_counter()
    for i0 in range(0, len(B), BATCH):
        P = B[i0:i0 + BATCH]; b = len(P)
        A = np.ones((b, 1, 1))
        for i in range(k):
            p = P[:, i]; s2 = np.sqrt(p * (1 - p))
            M = np.empty((b, 2, 2)); M[:, 0, 0] = 1 - p; M[:, 0, 1] = p; M[:, 1, 0] = s2; M[:, 1, 1] = -s2
            m = A.shape[1]
            A = np.einsum("bsi,bSx->bsSix", M, A).reshape(b, 2 * m, 2 * m)
        C = np.einsum("bSx,tx->btS", A, TT)
        pS = C * C
        lg = np.log2(np.maximum(pS, 1e-300))
        Ht = -np.einsum("btS,btS->bt", pS, lg)
        It = np.einsum("btS,Si->bti", pS, SEL)
        p_out = np.clip((1.0 - C[:, :, 0]) * 0.5, 0.0, 1.0)
        V = 4 * P * (1 - P)
        base = (Gm(P) + gam.h2(V)) / V                       # (b,k)
        D = np.einsum("bti,bi->bt", It, base) - Ht - Gm(p_out)
        for nm in names:
            idx = cls[nm]
            sub = D[:, idx]
            j = int(np.argmin(sub)); r, cc = divmod(j, sub.shape[1])
            if sub[r, cc] < best[nm][0]:
                best[nm] = (float(sub[r, cc]), int(reps[idx[cc]]), tuple(float(v) for v in P[r]))
        if (i0 // BATCH + 1) % 200 == 0:
            el = time.perf_counter() - t0
            print("  %d/%d  %.0f s (eta %.0f s)  " % (i0 + b, len(B), el, el / (i0 + b) * (len(B) - i0 - b))
                  + "  ".join("%s %.9f" % (nm, best[nm][0]) for nm in names), flush=True)
    print("RESULTS arity %d  c=%.5g  Gamma(1/2)=%.7f  (%.0f s)" % (k, c, Gm.cap, time.perf_counter() - t0))
    for nm in names:
        D, tt, ps = best[nm]
        print("  %-11s min D = %+.9f   tt=%-8d p=%s" % (nm, D, tt, ["%.6f" % v for v in (ps or ())]))
    json.dump({nm: [best[nm][0], best[nm][1], list(best[nm][2] or ())] for nm in names}, open("gates4_%s.json" % tag, "w"))

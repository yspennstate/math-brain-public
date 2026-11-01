"""Margin needed per gate class, guarded against near-constant configurations.

c_G(p) = -D_G(p) / ( I(G;p)/4 - p_out(1-p_out) ).  For the AND gate the denominator is exactly p q (1-p)(1-q)
and c_G reduces to the certificate's own -Phi/((1-p)(1-q)), so arity 2 IS the certificate margin and the
comparison across arities is like for like.  Where the gate is nearly constant at the given biases both D and
the denominator vanish and the ratio is numerical noise, so points with a denominator below DEN_MIN are skipped
and counted.
usage: gates6.py <k> <npz> <tag> <nx> [batch] [den_min]"""
import sys, time, json
import numpy as np
import gam, decomp
from gates4 import grid_values, combos

if __name__ == "__main__":
    k = int(sys.argv[1]); npz = sys.argv[2]; tag = sys.argv[3]; nx = int(sys.argv[4])
    BATCH = int(sys.argv[5]) if len(sys.argv) > 5 else 256
    DEN_MIN = float(sys.argv[6]) if len(sys.argv) > 6 else 1e-8
    n = 1 << k
    reps = np.load("npn_reps_k%d.npy" % k)
    TT = 1.0 - 2.0 * ((reps[:, None] >> np.arange(n)[None, :]) & 1).astype(np.float64)
    RO, degenerate = decomp.classify(k)
    lab = np.array(["DEGENERATE" if degenerate(int(t)) else ("READONCE" if int(t) in RO else "GENUINE") for t in reps])
    cls = {nm: np.flatnonzero(lab == nm) for nm in ("DEGENERATE", "READONCE", "GENUINE") if (lab == nm).any()}
    names = list(cls.keys())
    SEL = np.array([[(S >> i) & 1 for i in range(k)] for S in range(n)], float)
    Gm = gam.Gam(npz, 0.0)
    vals = grid_values(nx); B = combos(list(vals), k)
    print("arity %d: %d NPN classes (%s); %d bias vectors from %d grid values; Gamma(1/2)=%.7f; den_min=%.0e"
          % (k, len(reps), ", ".join("%s %d" % (nm, len(cls[nm])) for nm in names), len(B), len(vals), Gm.cap, DEN_MIN), flush=True)
    best = {nm: (-1e9, -1, None) for nm in names}
    skipped = 0; total = 0
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
        Ht = -np.einsum("btS,btS->bt", pS, np.log2(np.maximum(pS, 1e-300)))
        It = np.einsum("btS,Si->bti", pS, SEL)
        p_out = np.clip((1.0 - C[:, :, 0]) * 0.5, 0.0, 1.0)
        V = 4 * P * (1 - P)
        base = (Gm(P) + gam.h2(V)) / V
        D = np.einsum("bti,bi->bt", It, base) - Ht - Gm(p_out)
        den = It.sum(axis=2) / 4.0 - p_out * (1 - p_out)
        ok = den > DEN_MIN
        total += ok.size; skipped += int((~ok).sum())
        need = np.where(ok, -D / np.where(ok, den, 1.0), -1e9)
        for nm in names:
            idx = cls[nm]; sub = need[:, idx]
            j = int(np.argmax(sub)); r, cc = divmod(j, sub.shape[1])
            if sub[r, cc] > best[nm][0]:
                best[nm] = (float(sub[r, cc]), int(reps[idx[cc]]), tuple(float(v) for v in P[r]))
        if (i0 // BATCH + 1) % 400 == 0:
            el = time.perf_counter() - t0
            print("  %d/%d  %.0f s (eta %.0f s)  " % (i0 + b, len(B), el, el / (i0 + b) * (len(B) - i0 - b))
                  + "  ".join("%s %.4e" % (nm, best[nm][0]) for nm in names), flush=True)
    print("RESULTS arity %d  (%.0f s)  %d of %d gate-bias pairs skipped as near-constant" % (k, time.perf_counter() - t0, skipped, total))
    for nm in names:
        c, tt, ps = best[nm]
        print("  %-11s max margin c = %+.6e  -> constant %.7f   tt=%-6d p=%s"
              % (nm, c, Gm.cap + max(c, 0.0) / 4, tt, ["%.6f" % v for v in (ps or ())]))
    json.dump({nm: [best[nm][0], best[nm][1], list(best[nm][2] or ())] for nm in names}, open("gates6_%s.json" % tag, "w"))

"""Slack value iteration on a dyadic-aligned grid: uniform step 2^-11 on [2^-5, 1/2] and a geometric tail with M points
per octave from 2^-5 down to 2^-K (every 2^-k, k <= K, is a grid point), mirrored about 1/2. Same operator as
fei_readonce_gamma_geo.py. Reports the tail wobble G(p) - 2(C-4) log2(1/p), G = Gamma/p, per octave.
Usage: python -u fei_readonce_gamma_dyadic.py <M> <K> <C or 'bisect'> <tag>
"""
import sys, math, time, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fei_readonce_gamma_geo import iterate
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

def make_grid(M, K):
    tail = 2.0 ** (-(5 + np.arange(0, (K - 5) * M + 1) / M))     # 2^-5 down to 2^-K
    mid = np.arange(64, 1024 + 1) / 2048.0                        # 2^-5 .. 1/2 step 2^-11
    pts = np.concatenate([tail, mid, 1 - tail, 1 - mid, [0.5]])
    return np.unique(pts)

if __name__ == "__main__":
    M, K, mode, tag = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
    ps = make_grid(M, K); here = os.path.dirname(os.path.abspath(__file__))
    print("grid: %d points, smallest %.3e (2^-%d), M=%d per octave" % (len(ps), ps.min(), K, M), flush=True)
    if mode == "bisect":
        lo, hi = 6.40, 6.60
        for _ in range(16):
            mid = (lo + hi) / 2; t0 = time.time(); ok, G = iterate(mid, ps)
            print("  C=%.7f %s (%.0f s)" % (mid, "feasible" if ok else "infeasible", time.time() - t0), flush=True)
            if ok: hi = mid
            else: lo = mid
        print("smallest feasible C (M %d, K %d): %.7f  [Hod 6.4547837]" % (M, K, hi), flush=True)
        C = hi
    else:
        C = float(mode)
    t0 = time.time(); ok, G = iterate(C, ps)
    np.save(os.path.join(here, f"gamma_dyadic_{tag}.npy"), np.stack([ps, G]))
    print("C=%.7f feasible=%s min Gamma %.3e at p=%.3e (%.0f s)" % (C, ok, G.min(), ps[np.argmin(G)], time.time() - t0), flush=True)
    alpha = 2 * (C - 4); bstar = 8 - 4 / math.log(2)
    m = ps <= 0.5
    w = G[m] / ps[m] - alpha * np.log2(1 / ps[m])
    print("wobble w(p) = G/p - 2(C-4)log2(1/p), b* = %.5f; per octave [min, max] and the value at 2^-k:" % bstar)
    for k in range(1, K + 1):
        sel = (ps[m] <= 2.0 ** -(k - 1)) & (ps[m] >= 2.0 ** -k)
        j = int(np.argmin(np.abs(ps[m] - 2.0 ** -k)))
        print("  k=%2d  [%.5f, %.5f]  at 2^-k: %.5f  (grid p=%.3e)" % (k, w[sel].min(), w[sel].max(), w[j], ps[m][j]), flush=True)
    print("global wobble min %.6f max %.6f" % (w.min(), w.max()))

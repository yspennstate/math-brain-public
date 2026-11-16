"""The n = 4 failure of the gap-weighted state, carried to larger n (see canon_gap.py).

At n = 4 the gap-weighted state is negative near two disjoint heavy edges joined by light edges, where the top two
Laplacian eigenvalues nearly coincide.  This script starts local searches for n >= 5 from that configuration
(remaining vertices isolated, or lightly attached) and prints the smallest Gval / W^2 found.
usage: canon_gap_target.py n starts seed
"""
import sys
import numpy as np
from scipy.optimize import minimize
from canon_gap import gval


def main():
    n, starts, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    m = len(pairs)
    base = np.zeros(m)
    for k, p in enumerate(pairs):
        if p == (0, 1):
            base[k] = 0.4150
        elif p == (2, 3):
            base[k] = 0.4235
        elif p in ((0, 2), (0, 3)):
            base[k] = 0.0807
    v0, g0 = gval(base, n, pairs)
    print("n=%d at the padded n = 4 minimiser: Gval/W^2 = %+.4e (top gap %.1e)" % (n, v0, g0))

    def f(z):
        return gval(z * z, n, pairs)[0]

    found = []
    for s in range(starts):
        w = base * rng.uniform(0.8, 1.2, m) + (0.02 * rng.uniform(0, 1, m) ** 2 if s % 2 else 0)
        res = minimize(f, np.sqrt(w), method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-13, "maxiter": 300 * m})
        res = minimize(f, res.x, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-14, "maxiter": 300 * m})
        w = res.x ** 2
        w = w / w.sum()
        v, gap = gval(w, n, pairs)
        found.append((v, gap, w))
    found.sort(key=lambda t: t[0])
    print("n=%d, %d local searches from there; smallest %.3e; number below -1e-7: %d"
          % (n, len(found), found[0][0], sum(1 for t in found if t[0] < -1e-7)))
    for v, gap, w in found[:3]:
        print("  %+.3e  gap %.2e  %s" % (v, gap, " ".join("%d%d:%.4f" % (p[0] + 1, p[1] + 1, a)
                                                              for p, a in zip(pairs, w) if a > 2e-3)))


if __name__ == "__main__":
    main()

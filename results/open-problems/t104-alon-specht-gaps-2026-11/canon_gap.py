"""Directed search against the gap-weighted state (HOOKS_AND_TWO_ROWS.md section 5).

Candidate: for a weighted graph with top Laplacian eigenvector x (eigenvalue lam), take the covariance
    C = (lam Pi - L_G) / ((n-1) lam - 2W)      (Pi the projection onto sum-zero vectors; C x = 0, tr C = 1).
Then Conjecture F for G follows from   Gval(w) := tr( M (lam Pi - L_G) ) >= 0,   M as in canon_spectral.py.
Gval is homogeneous of degree 2 in w.  The script minimises Gval / W^2 over weights by local search from many
starts (random, sparse, near a star, near a path, near a double star) and prints the smallest values found.
usage: canon_gap.py n starts seed
"""
import sys
import numpy as np
from scipy.optimize import minimize
from canon_spectral import build


def gval(w, n, pairs):
    W = w.sum()
    if W <= 1e-14:
        return 0.0, 0.0
    w = w / W
    L, ev, U, x, M = build(w, n, pairs)
    Pi = np.eye(n) - 1.0 / n
    lam = ev[-1]
    return float(np.trace(M @ (lam * Pi - L))), float(ev[-1] - ev[-2])


def closed(w, n, pairs):
    """The same number from the expanded formula in degrees and squared weights (W = 1)."""
    w = w / w.sum()
    L, ev, U, x, M = build(w, n, pairs)
    lam = ev[-1]
    deg = np.zeros(n); deg2 = np.zeros(n)
    sw2 = 0.0; sw2xx = 0.0; sw2d2 = 0.0
    for (i, j), v in zip(pairs, w):
        d2 = (x[i] - x[j]) ** 2
        deg[i] += v; deg[j] += v
        deg2[i] += v * d2; deg2[j] += v * d2
        sw2 += v * v; sw2xx += v * v * x[i] * x[j]; sw2d2 += v * v * d2
    W = 1.0
    A = (deg * x * x).sum()
    t1 = (2 * W - lam) * ((n - 1) * lam - 2 * W)
    t2 = (2 * n / (n - 2.0)) * ((n - 1) * lam - 2 * W) * (lam * (n - 1.0) / n - A)
    t3 = -2 * n * (lam * A - lam * lam / n - (deg * deg * x * x).sum() - 2 * sw2xx)
    t4 = -(n - 2) * (lam * (4 * lam - 2 * W) - 2 * (deg2 * deg).sum() - 4 * sw2d2 + (deg * deg).sum() + 2 * sw2)
    return t1 + t2 + t3 + t4


def main():
    n, starts, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    m = len(pairs)
    dev = 0.0
    for _ in range(40):
        w = rng.uniform(0, 1, m)
        dev = max(dev, abs(closed(w, n, pairs) - gval(w, n, pairs)[0]))
    print("n=%d expanded formula against the trace: largest deviation %.1e" % (n, dev))

    def f(z):
        return gval(z * z, n, pairs)[0]

    found = []
    for s in range(starts):
        kind = s % 6
        if kind == 0:
            w = rng.uniform(0, 1, m)
        elif kind == 1:
            w = rng.uniform(0, 1, m) * (rng.uniform(0, 1, m) < 0.4)
        elif kind == 2:
            w = np.array([1.0 if i == 0 else 0.0 for (i, j) in pairs]) + 0.3 * rng.uniform(0, 1, m) ** 2
        elif kind == 3:
            w = np.array([1.0 if j == i + 1 else 0.0 for (i, j) in pairs]) * rng.uniform(0.2, 1, m) + 0.05 * rng.uniform(0, 1, m) ** 3
        elif kind == 4:
            w = np.array([1.0 if (i == 0 or i == 1) else 0.0 for (i, j) in pairs]) * rng.uniform(0, 1, m)
        else:
            w = np.exp(rng.normal(0, 2.5, m))
        if w.sum() <= 0:
            continue
        res = minimize(f, np.sqrt(w), method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-13, "maxiter": 300 * m})
        res = minimize(f, res.x, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-14, "maxiter": 300 * m})
        w = res.x ** 2
        w = w / w.sum()
        v, gap = gval(w, n, pairs)
        found.append((v, gap, w))
    found.sort(key=lambda t: t[0])
    print("n=%d, %d local searches; smallest Gval/W^2: %.3e; number below -1e-7: %d"
          % (n, len(found), found[0][0], sum(1 for t in found if t[0] < -1e-7)))
    for v, gap, w in found[:6]:
        print("  %+.3e  gap %.2e  %s" % (v, gap, " ".join("%d%d:%.4f" % (p[0] + 1, p[1] + 1, a)
                                                              for p, a in zip(pairs, w) if a > 2e-3)))


if __name__ == "__main__":
    main()

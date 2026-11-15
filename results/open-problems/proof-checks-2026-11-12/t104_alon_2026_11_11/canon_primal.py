"""Primal test of the uniform state of HOOKS_AND_TWO_ROWS.md section 5.

The per-edge inequality fails for some x, but a proof of Conjecture F needs only
    S(w) = sum_ij w_ij [ (2 - d_ij^2) N(x) - c A_ij(x) ] >= 0,   c = (n-2)/(n-1),
at x = a top eigenvector of the Laplacian of w: then
    2W - lambda_max(L_G) >= c tr(rho(x) L(G, sigma)) >= c lambda_min(G, sigma).
This script minimises S over weights (W = 1), using the closed form of canon_state.py.
usage: canon_primal.py n samples seed
"""
import sys
import numpy as np
from scipy.optimize import minimize
from canon_state import closed


def setup(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def S_of(w, n, pairs):
    L = np.zeros((n, n))
    for (i, j), v in zip(pairs, w):
        L[i, i] += v
        L[j, j] += v
        L[i, j] -= v
        L[j, i] -= v
    ev, U = np.linalg.eigh(L)
    x = U[:, -1]
    c = (n - 2.0) / (n - 1.0)
    N, A = closed(x)
    tot = 0.0
    for (i, j), v in zip(pairs, w):
        tot += v * ((2 - (x[i] - x[j]) ** 2) * N - c * A[i, j])
    return tot, ev[-1] - ev[-2]


def main():
    n, samples, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    pairs = setup(n)
    m = len(pairs)
    worst, arg, gap_at = float("inf"), None, 0.0
    for k in range(samples):
        kind = k % 4
        if kind == 0:
            w = rng.uniform(0, 1, m)
        elif kind == 1:
            w = np.exp(rng.normal(0, 2.5, m))
        elif kind == 2:
            w = rng.uniform(0, 1, m) * (rng.uniform(0, 1, m) < 0.4) + 1e-9
        else:
            w = np.array([1.0 if i == 0 else 0.0 for (i, j) in pairs]) + 0.2 * rng.uniform(0, 1, m) ** 3
        w = w / w.sum()
        v, g = S_of(w, n, pairs)
        if v < worst:
            worst, arg, gap_at = v, w, g
    print("n=%d random: smallest S %.6e over %d weights (top eigenvalue gap there %.3e)" % (n, worst, samples, gap_at))

    def f(z):
        w = z * z
        s = w.sum()
        if s < 1e-14:
            return 1e3
        return S_of(w / s, n, pairs)[0]

    for r in range(10):
        z0 = np.sqrt(arg) + (0.15 * rng.normal(0, 1, m) if r else 0)
        res = minimize(f, z0, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-14, "maxiter": 500 * m})
        if res.fun < worst:
            w = res.x ** 2
            worst, arg = res.fun, w / w.sum()
    v, g = S_of(arg, n, pairs)
    print("  after local search: smallest S %.6e, top eigenvalue gap %.3e, weights: %s"
          % (worst, g, " ".join("%d%d:%.3f" % (p[0] + 1, p[1] + 1, a) for p, a in zip(pairs, arg) if a > 2e-3)))


if __name__ == "__main__":
    main()

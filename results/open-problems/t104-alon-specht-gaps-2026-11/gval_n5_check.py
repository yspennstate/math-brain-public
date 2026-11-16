"""Is Gval < 0 at n = 5 for a graph with a SIMPLE top eigenvalue?  (an agent, 11 Nov 2026)

The search on Mac mini 1 (gap_n5.out) printed Gval/W^2 = -2.010e-03 and -3.947e-04 at two weightings whose top
Laplacian eigenvalue is double to 1e-11.  At a double eigenvalue the top eigenvector is not unique and Gval depends
on the choice.  This script starts from the printed (rounded) weights, and
  1. evaluates Gval for every unit x in the (near) top eigenspace (a circle), at the degenerate point;
  2. moves off the degenerate set in random directions by small steps and evaluates Gval with the unique top x;
  3. minimises Gval locally subject to a spectral gap >= 1e-3 (penalty), to see whether a negative value survives
     with a clearly simple top eigenvalue.
"""
import sys
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, "~/brain-repo/06_math_research/t104_alon_agent_2026_11_11")
from canon_spectral import build  # noqa: E402

n = 5
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
idx = {p: k for k, p in enumerate(pairs)}


def from_text(s):
    w = np.zeros(len(pairs))
    for tok in s.split():
        a, v = tok.split(":")
        w[idx[(int(a[0]) - 1, int(a[1]) - 1)]] = float(v)
    return w


def lap(w):
    L = np.zeros((n, n))
    for (i, j), v in zip(pairs, w):
        L[i, i] += v; L[j, j] += v; L[i, j] -= v; L[j, i] -= v
    return L


def gval_x(w, x):
    """Gval with a prescribed unit top vector x (eigenvalue lam = x^t L x)."""
    w = w / w.sum()
    L = lap(w)
    lam = float(x @ L @ x)
    W = 1.0
    D = np.diag(x)
    L2 = np.zeros((n, n))
    for (i, j), v in zip(pairs, w):
        c = v * (x[i] - x[j]) ** 2
        L2[i, i] += c; L2[j, j] += c; L2[i, j] -= c; L2[j, i] -= c
    M = (2 * W - lam) * np.eye(n) + (2 * n / (n - 2.0)) * ((n - 1) * lam - 2 * W) * D @ D - 2 * n * D @ L @ D - (n - 2) * (2 * L2 - L)
    Pi = np.eye(n) - 1.0 / n
    return float(np.trace(M @ (lam * Pi - L)))


def gval(w):
    w = w / w.sum()
    L, ev, U, x, M = build(w, n, pairs)
    Pi = np.eye(n) - 1.0 / n
    return float(np.trace(M @ (ev[-1] * Pi - L))), float(ev[-1] - ev[-2])


cases = [
    "12:0.0031 13:0.0259 14:0.2021 15:0.2067 23:0.2972 24:0.0078 34:0.0297 35:0.0235 45:0.2038",
    "12:0.2143 13:0.2116 14:0.0134 23:0.2115 24:0.0134 34:0.0172 35:0.0043 45:0.3142",
]
rng = np.random.default_rng(7)
for s in cases:
    w0 = from_text(s)
    w0 = w0 / w0.sum()
    g, gap = gval(w0)
    # consistency of gval_x with build
    L, ev, U, x, M = build(w0, n, pairs)
    print("case:", s)
    print("  rounded weights: Gval %.4e, gap %.3e, check gval_x %.4e" % (g, gap, gval_x(w0, x)))
    ev, U = np.linalg.eigh(lap(w0))
    u1, u2 = U[:, -1], U[:, -2]
    vals = [gval_x(w0, np.cos(t) * u1 + np.sin(t) * u2) for t in np.linspace(0, np.pi, 181)]
    print("  over the top two-plane (treating it as degenerate): min %.4e, max %.4e" % (min(vals), max(vals)))
    # random small moves
    worst = (1e9, 0.0)
    for scale in (1e-3, 3e-3, 1e-2, 3e-2):
        best = (1e9, 0.0)
        for _ in range(4000):
            w = np.abs(w0 + scale * rng.normal(0, 1, len(pairs)) * (w0 > 0))
            g, gap = gval(w)
            if g < best[0]:
                best = (g, gap)
        print("  moves of size %.0e (support kept): smallest Gval %.4e at gap %.3e" % (scale, best[0], best[1]))

    # constrained local minimisation: gap >= gmin
    for gmin in (1e-3, 1e-2, 3e-2):
        def f(z):
            g, gap = gval(z * z)
            return g + 50.0 * max(0.0, gmin - gap) ** 2 / gmin
        best = None
        for trial in range(12):
            z0 = np.sqrt(np.abs(w0 + 0.01 * rng.normal(0, 1, len(pairs))))
            res = minimize(f, z0, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-14, "maxiter": 6000})
            g, gap = gval(res.x ** 2)
            if gap >= 0.9 * gmin and (best is None or g < best[0]):
                best = (g, gap, res.x ** 2 / (res.x ** 2).sum())
        if best:
            print("  gap >= %.0e: smallest Gval %.6e at gap %.4e" % (gmin, best[0], best[1]))
            print("     weights " + " ".join("%d%d:%.6f" % (i + 1, j + 1, v) for (i, j), v in zip(pairs, best[2]) if v > 1e-9))

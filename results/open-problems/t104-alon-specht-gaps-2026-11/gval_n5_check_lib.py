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



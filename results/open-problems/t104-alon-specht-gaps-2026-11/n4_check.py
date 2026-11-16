"""Numerical check of the n = 4 case of the 2/3 conjecture (N4_PROOF.md).

(1) The closed forms: lambda_min(G, 211) = 2W - lambda_max(L_G) and
    lambda_min(G, 22) = W - sqrt(a^2 + b^2 + c^2 - ab - bc - ca), with a = w12 + w34, b = w13 + w24, c = w14 + w23,
    against the Specht-module matrices of alon_search.py.
(2) The inequality lambda_max(L_G) <= (4/3) W + (2/3) D on random weights of several shapes.
(3) The certificate: for random unit x orthogonal to 1, the vector u of the proof satisfies sum u = 0, |u| <= 1 and
    (x_i - x_j)^2 <= 4/3 + sqrt(2/3) u_m for the two edges ij of each perfect matching m.
usage: n4_check.py trials seed
"""
import sys, math
import numpy as np
from alon_search import edge_ops, lam

EDGES = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
MATCH = {(1, 2): 0, (3, 4): 0, (1, 3): 1, (2, 4): 1, (1, 4): 2, (2, 3): 2}


def lap(w):
    L = np.zeros((4, 4))
    for (i, j), v in zip(EDGES, w):
        L[i - 1, i - 1] += v
        L[j - 1, j - 1] += v
        L[i - 1, j - 1] -= v
        L[j - 1, i - 1] -= v
    return L


def abc(w):
    v = np.zeros(3)
    for e, x in zip(EDGES, w):
        v[MATCH[e]] += x
    return v


def D(v):
    a, b, c = v
    return math.sqrt(max(a * a + b * b + c * c - a * b - b * c - c * a, 0.0))


def certificate(x):
    """The vector u of the proof for a unit x orthogonal to 1, indexed by the matchings 12|34, 13|24, 14|23."""
    ea = np.array([1, 1, -1, -1]) / 2.0
    eb = np.array([1, -1, 1, -1]) / 2.0
    ec = np.array([1, -1, -1, 1]) / 2.0
    p, q, r = abs(x @ ea), abs(x @ eb), abs(x @ ec)
    t = np.array([(q + r) ** 2, (p + r) ** 2, (p + q) ** 2]) - 4.0 / 3.0
    order = np.argsort(t)                 # t[order[0]] <= t[order[1]] <= t[order[2]]
    lo, mid, hi = order
    u = np.zeros(3)
    if t[hi] <= 0:
        return u, t
    if t[mid] <= -t[hi] / 2:
        u[hi] = t[hi]
        u[mid] = u[lo] = -t[hi] / 2
    else:
        u[hi], u[mid] = t[hi], t[mid]
        u[lo] = -t[hi] - t[mid]
    return math.sqrt(1.5) * u, t


def main():
    trials = int(sys.argv[1])
    rng = np.random.default_rng(int(sys.argv[2]))
    A211, e211, _, _ = edge_ops((2, 1, 1))
    A22, e22, _, _ = edge_ops((2, 2))
    assert e211 == EDGES and e22 == EDGES
    worst_form = 0.0
    worst_gap = float("inf")
    worst_ratio = float("inf")
    for k in range(trials):
        kind = k % 4
        if kind == 0:
            w = rng.uniform(0, 1, 6)
        elif kind == 1:
            w = np.exp(rng.normal(0, 3, 6))
        elif kind == 2:
            w = rng.uniform(0, 1, 6) * (rng.uniform(0, 1, 6) < 0.5)
        else:
            w = np.array([1.0, 1.0, 1.0, 0, 0, 0]) + 0.05 * rng.normal(0, 1, 6) ** 2    # near the star at vertex 1
        w = w / max(w.sum(), 1e-300)
        W = w.sum()
        lmax = np.linalg.eigvalsh(lap(w))[-1]
        d = D(abc(w))
        l211 = lam(A211, w)[0]
        l22 = lam(A22, w)[0]
        worst_form = max(worst_form, abs(l211 - (2 * W - lmax)), abs(l22 - (W - d)))
        worst_gap = min(worst_gap, (4.0 / 3.0) * W + (2.0 / 3.0) * d - lmax)
        if l22 > 1e-9:
            worst_ratio = min(worst_ratio, l211 / l22)
    print("closed forms: largest deviation %.2e over %d weights" % (worst_form, trials))
    print("inequality: smallest value of (4/3)W + (2/3)D - lambda_max = %.3e (must be >= 0)" % worst_gap)
    print("smallest ratio lambda_min(211)/lambda_min(22) seen: %.9f" % worst_ratio)
    bad = 0
    worst_norm = 0.0
    worst_slack = float("inf")
    worst_sum = 0.0
    for k in range(trials):
        x = rng.normal(0, 1, 4)
        if k % 3 == 1:
            x = np.array([3.0, -1, -1, -1]) + 0.1 * rng.normal(0, 1, 4)
        if k % 3 == 2:
            x = np.array([1.0, -1, 0, 0]) + 0.1 * rng.normal(0, 1, 4)
        x = x - x.mean()
        x = x / np.linalg.norm(x)
        u, t = certificate(x)
        worst_norm = max(worst_norm, np.linalg.norm(u))
        worst_sum = max(worst_sum, abs(u.sum()))
        for (i, j) in EDGES:
            s = 4.0 / 3.0 + math.sqrt(2.0 / 3.0) * u[MATCH[(i, j)]] - (x[i - 1] - x[j - 1]) ** 2
            worst_slack = min(worst_slack, s)
        if np.linalg.norm(u) > 1 + 1e-12 or worst_slack < -1e-12:
            bad += 1
    print("certificate: largest |u| = %.12f (must be <= 1), largest |sum u| = %.1e, smallest edge slack = %.3e "
          "(must be >= 0), failures %d of %d" % (worst_norm, worst_sum, worst_slack, bad, trials))


if __name__ == "__main__":
    main()

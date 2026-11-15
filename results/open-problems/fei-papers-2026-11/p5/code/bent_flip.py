"""Inner product on 2k variables with one value flipped: min over orders of L/Inf at each coordinate.
Same conventions as check_witness.py (functions repeated so that this script runs on its own)."""
import math
import numpy as np


def wht(v):
    a = np.asarray(v, float).copy()
    h = 1
    while h < len(a):
        a = a.reshape(-1, 2 * h)
        x, y = a[:, :h].copy(), a[:, h:].copy()
        a[:, :h], a[:, h:] = x + y, x - y
        a = a.reshape(-1)
        h *= 2
    return a / len(a)


def eta(x):
    x = np.asarray(x, float)
    out = np.zeros_like(x)
    m = x > 1e-300
    out[m] = -x[m] * np.log2(x[m])
    return out


def Phi(p, q):
    return eta(p) + eta(q) - eta(np.asarray(p) + np.asarray(q))


def pq(mu, n, i):
    others = [j for j in range(n) if j != i]
    m = n - 1
    t = np.arange(1 << m)
    full = np.zeros(1 << m, dtype=np.int64)
    for b in range(m):
        full |= ((t >> b) & 1) << others[b]
    return mu[full], mu[full | (1 << i)]


def zeta(v, m):
    a = v.copy()
    idx = np.arange(1 << m)
    for b in range(m):
        hi = idx[(idx >> b) & 1 == 1]
        a[hi] += a[hi ^ (1 << b)]
    return a


def best_order(p, q):
    m = int(round(math.log2(len(p))))
    a, b = zeta(p, m), zeta(q, m)
    best = np.full(1 << m, np.inf)
    best[0] = float(Phi(a[0], b[0]))
    for R in sorted(range(1, 1 << m), key=lambda t: bin(t).count("1")):
        S = np.array([R ^ (1 << j) for j in range(m) if (R >> j) & 1])
        best[R] = float((best[S] + Phi(a[R] - a[S], b[R] - b[S])).min())
    return best[(1 << m) - 1]


rng = np.random.default_rng(5)
for k in range(2, 6):
    n = 2 * k
    idx = np.arange(1 << n)
    ip = np.array([(-1) ** bin((j & ((1 << k) - 1)) & (j >> k)).count("1") for j in idx])
    for label, pt in (("origin", 0), ("random", int(rng.integers(1 << n)))):
        f = ip.copy()
        f[pt] *= -1
        mu = wht(f) ** 2
        F, E = [], []
        for i in range(n):
            p, q = pq(mu, n, i)
            d = float(q.sum())
            F.append(best_order(p, q) / d)
            E.append(float(Phi(p, q).sum()) / d)
        print(f"n={n:2d} flip at {label:6s}: F_i min {min(F):.4f} max {max(F):.4f};  "
              f"E_i/Inf_i min {min(E):.4f} max {max(E):.4f}", flush=True)

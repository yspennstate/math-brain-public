"""Circulant graphs: the stratum target in Fourier form, checked against a direct computation.

Vertices Z_n (n odd), weight w_s = a_s / n on the n edges {i, i+s}, s = 1..m = (n-1)/2, sum a_s = 1.
theta_j = (2/n) sum_s a_s (1 - C_j(s)), C_j(s) = cos(2 pi j s / n); top frequency k, lambda = theta_k (double).
Closed forms (sums over the cos/sin pair of each low frequency j != 0, +-k):
  sum g Q = 16 sum_s (a_s/n)(1 - C_k(s))(lambda - 2/n - a_s/n)
  P_j     = 4 theta_j + 8 lambda/(n-2) - 16 (1 - sum_s a_s C_k(s) C_j(s)) / (n(n-2)) + 4 (1 - lambda)(n-4)/(n-2)^2
  sum g P = sum_{j=1..m, j != k} (lambda - theta_j) P_j
usage: python t104_circ_fourier.py n trials seed
"""
import sys
import numpy as np

n, TR, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
m = (n - 1) // 2
S = np.arange(1, m + 1)
C = np.cos(2 * np.pi * np.outer(np.arange(n), S) / n)   # C[j, s-1]


def fourier(a):
    th = (2.0 / n) * ((1 - C) @ a)
    k = 1 + int(np.argmax(th[1:m + 1]))
    lam = th[k]
    gQ = 16 * np.sum((a / n) * (1 - C[k]) * (lam - 2.0 / n - a / n))
    gP = 0.0
    for j in range(1, m + 1):
        if j == k:
            continue
        Pj = (4 * th[j] + 8 * lam / (n - 2) - 16 * (1 - np.sum(a * C[k] * C[j])) / (n * (n - 2))
              + 4 * (1 - lam) * (n - 4) / (n - 2) ** 2)
        gP += (lam - th[j]) * Pj
    second = np.sort(th[1:m + 1])[-2] if m > 1 else -1
    return gQ, gP, lam, k, (lam - second) / lam


def direct(a):
    pairs = [(i, (i + s) % n, a[s - 1] / n) for s in S for i in range(n)]
    L = np.zeros((n, n))
    for i, j, w in pairs:
        L[i, i] += w; L[j, j] += w; L[i, j] -= w; L[j, i] -= w
    ev, U = np.linalg.eigh(L)
    lam = ev[-1]
    top = [t for t in range(1, n) if ev[t] > lam - 1e-9]
    low = [t for t in range(1, n) if ev[t] <= lam - 1e-9]
    c = 2.0 * n / (n - 2)
    gP = gQ = 0.0
    for l in low:
        v, mu = U[:, l], ev[l]
        P = Q = 0.0
        for t in top:
            u = U[:, t]; p = u * v
            P += mu + c * (lam * p @ p - p @ L @ p) + (1 - lam) * (1 - c * p @ p) / (n - 2)
            Q += 2 * sum(w * ((u[i] - u[j]) * (v[i] - v[j])) ** 2 for i, j, w in pairs)
        gP += (lam - mu) * P; gQ += (lam - mu) * Q
    return gQ, gP, len(top)


rng = np.random.default_rng(SEED)
tests = [np.eye(m)[0]] + [rng.dirichlet(np.ones(m) * 0.5) for _ in range(TR)]
err = 0.0; worst = 0.0
for a in tests:
    gQ, gP, lam, k, rg = fourier(a)
    if rg < 1e-6:
        continue
    dQ, dP, D = direct(a)
    if D != 2:
        continue
    err = max(err, abs(gQ - dQ), abs(gP - dP))
    worst = max(worst, gQ / gP)
print("n %d  checked %d circulants  largest |fourier - direct| %.1e  largest ratio %.6f  (C_n ratio %.6f)"
      % (n, len(tests), err, worst, fourier(np.eye(m)[0])[0] / fourier(np.eye(m)[0])[1]))

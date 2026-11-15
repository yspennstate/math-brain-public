"""Independent check of P7 Theorem 3 (BIAS), written from the outline's statement only:
   H/I <= 2[n/r + 1 + log2(e)/r],  r = log2(1/min(P[f=1], P[f=-1])),  any Boolean f on n variables.
H = sum_S fhat(S)^2 log2(1/fhat(S)^2) (all S incl. empty), I = sum_S |S| fhat(S)^2. Constants excluded (I = 0).
Exhaustive for n <= 4, random (uniform and sparse) for n = 5..10, plus AND/OR/tribes-like examples."""
import itertools, math, random
import numpy as np
LOG2E = 1 / math.log(2)

def wht_rows(F):  # F: (m, 2^n) of +-1
    a = F.astype(float).copy(); m, N = a.shape; h = 1
    while h < N:
        a = a.reshape(m, -1, 2, h)
        a = np.concatenate([a[:, :, 0:1] + a[:, :, 1:2], a[:, :, 0:1] - a[:, :, 1:2]], axis=2).reshape(m, N)
        h *= 2
    return a / N

def check(F, n):
    N = 1 << n
    size = np.array([bin(s).count("1") for s in range(N)])
    w = wht_rows(F) ** 2
    with np.errstate(divide="ignore", invalid="ignore"):
        H = np.where(w > 0, -w * np.log2(np.where(w > 0, w, 1)), 0).sum(1)
    I = (w * size).sum(1)
    p1 = (F == 1).mean(1); mu = np.minimum(p1, 1 - p1)
    ok = (I > 0) & (mu > 0)
    r = np.log2(1 / mu[ok])
    bound = 2 * (n / r + 1 + LOG2E / r)
    ratio = H[ok] / I[ok]
    frac = ratio / bound
    return int(ok.sum()), int((ratio > bound + 1e-9).sum()), float(frac.max()) if ok.any() else 0.0

rng = np.random.default_rng(7)
print("n  functions  violations  max (H/I)/bound")
for n in range(1, 5):
    N = 1 << n
    idx = np.arange(1 << N)[:, None]
    F = 1 - 2 * ((idx >> np.arange(N)) & 1)
    print(n, *check(F, n), "exhaustive")
for n in range(5, 11):
    N = 1 << n
    tot = [0, 0, 0.0]
    for p in (0.5, 0.2, 0.05, 0.01, 2.0 ** -n * 3):
        F = np.where(rng.random((2000, N)) < p, -1, 1)
        c = check(F, n); tot[0] += c[0]; tot[1] += c[1]; tot[2] = max(tot[2], c[2])
    # structured: AND of k variables, OR of k, disjoint ANDs (tribes-like)
    S = []
    x = np.arange(N)
    for k in range(1, n + 1):
        S.append(np.where((x & ((1 << k) - 1)) == (1 << k) - 1, -1, 1))
        S.append(np.where((x & ((1 << k) - 1)) != 0, -1, 1))
    for w in range(2, n + 1):
        t = n // w
        if t >= 1:
            v = np.zeros(N, bool)
            for j in range(t):
                m = ((1 << w) - 1) << (j * w); v |= (x & m) == m
            S.append(np.where(v, -1, 1))
    c = check(np.array(S), n); tot[0] += c[0]; tot[1] += c[1]; tot[2] = max(tot[2], c[2])
    print(n, *tot, "random + structured")

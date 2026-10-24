# Attempt to break J_i <= B_i and D_i <= lambda_i + 3 d_i/ln2 beyond n=4: random functions, random sparse
# (small-support) functions, majority, tribes, address, and point functions, n = 5..12. float64.
import json, math, sys
import numpy as np

OUT = sys.argv[1]
rng = np.random.default_rng(20261011)
LN2 = math.log(2.0)


def fwht(v):
    v = v.astype(float).copy()
    N = v.shape[0]
    h = 1
    while h < N:
        v = v.reshape(N // (2 * h), 2, h)
        a = v[:, 0, :].copy(); b = v[:, 1, :].copy()
        v[:, 0, :] = a + b; v[:, 1, :] = a - b
        v = v.reshape(N)
        h *= 2
    return v / N


def xl(p):
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def worst(f, m):
    c = fwht(f)
    S = np.arange(1 << m)
    H = xl(c * c)
    wJB, wD = -1e9, -1e9
    for j in range(m):
        T0 = S[((S >> j) & 1) == 0]
        a, b = c[T0], c[T0 | (1 << j)]
        d = float((b * b).sum())
        if d < 1e-15:
            continue
        q = a * a + b * b
        B = H - xl(q)
        J = xl(q) - 0.5 * (xl((a + b) ** 2) + xl((a - b) ** 2))
        mk = b * b > 0
        lam = float((b[mk] ** 2 * np.log2(q[mk] / b[mk] ** 2)).sum())
        wJB = max(wJB, (J - B) / d)
        wD = max(wD, (B + J - lam - 3 * d / LN2) / d)
    return wJB, wD


fams = {}
for m in range(5, 13):
    N = 1 << m
    x = np.arange(N)
    bits = (x[:, None] >> np.arange(m)) & 1
    cands = {
        "random": [1 - 2 * rng.integers(0, 2, N) for _ in range(20)],
        "sparse": [np.where(np.isin(x, rng.choice(N, size=int(rng.integers(1, 6)), replace=False)), -1, 1) for _ in range(20)],
        "biased": [np.where(rng.random(N) < rng.choice([0.02, 0.1, 0.3]), -1, 1) for _ in range(20)],
        "majority": [np.where(bits.sum(1) * 2 > m, -1, 1)],
        "point": [np.where(x == 0, -1, 1)],
        "tribes": [np.where(np.any(bits[:, : (m // 2) * 2].reshape(N, -1, 2).all(axis=2), axis=1), -1, 1)],
    }
    for fam, fs in cands.items():
        for f in fs:
            if np.all(f == f[0]):
                continue
            a, b = worst(f, m)
            r = fams.setdefault(fam, {"max (J-B)/d": -1e9, "max (D-lam-3d/ln2)/d": -1e9, "count": 0})
            r["max (J-B)/d"] = max(r["max (J-B)/d"], a)
            r["max (D-lam-3d/ln2)/d"] = max(r["max (D-lam-3d/ln2)/d"], b)
            r["count"] += 1
print(json.dumps(fams, indent=1))
with open(OUT + "/break_JB.json", "w", encoding="utf-8") as fh:
    json.dump(fams, fh, indent=1)

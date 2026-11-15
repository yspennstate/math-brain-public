"""Q_b(f) = sum_i g(Inf_i) E_i / sum_i g(Inf_i) Inf_i with g(t) = (1 + log2(1/t))^-b.
b = 0 is the A* quotient sum E_i / I. Scan: all functions on 4 variables, random monotone up to n = 10.
Question: is sup Q_1 much larger than sup Q_0 on small f (weights helping or hurting)?"""
import numpy as np, itertools, sys


def wht_rows(T):
    T = T.astype(float).copy(); N = T.shape[1]; h = 1
    while h < N:
        T = T.reshape(T.shape[0], -1, 2 * h)
        a = T[:, :, :h].copy(); b = T[:, :, h:].copy()
        T[:, :, :h] = a + b; T[:, :, h:] = a - b
        T = T.reshape(T.shape[0], N); h *= 2
    return T / N


def EI(F, n):
    w2 = F ** 2; idx = np.arange(1 << n); E = []; I = []
    for i in range(n):
        bit = 1 << i; T = idx[(idx & bit) == 0]
        a = w2[:, T]; c = w2[:, T | bit]; s = a + c
        t = np.divide(c, s, out=np.zeros_like(s), where=s > 1e-300)
        with np.errstate(divide="ignore", invalid="ignore"):
            H = -(t * np.log2(np.where(t > 0, t, 1)) + (1 - t) * np.log2(np.where(t < 1, 1 - t, 1)))
        E.append((s * H).sum(1)); I.append(c.sum(1))
    return np.array(E).T, np.array(I).T


def Q(E, I, b):
    with np.errstate(divide="ignore", invalid="ignore"):
        g = np.where(I > 1e-15, (1 + np.log2(1 / np.where(I > 1e-15, I, 1))) ** (-b), 0.0)
    num = (g * E).sum(1); den = (g * I).sum(1)
    return np.where(den > 1e-12, num / np.where(den > 1e-12, den, 1), 0.0)


def report(tag, E, I):
    q0 = Q(E, I, 0); q1 = Q(E, I, 1); q2 = Q(E, I, 2)
    print(f"{tag}: max Q0={q0.max():.4f} max Q1={q1.max():.4f} max Q2={q2.max():.4f} "
          f"max Q1/Q0={np.nanmax(np.where(q0 > 0.05, q1 / np.where(q0 > 0, q0, 1), 0)):.4f}")
    sys.stdout.flush()


n = 4
tabs = np.array([[1.0 if (m >> x) & 1 else -1.0 for x in range(16)] for m in range(1 << 16)])
E, I = EI(wht_rows(tabs), n); report("all n=4", E, I)

rng = np.random.default_rng(7)
for n in (6, 8, 10):
    N = 1 << n; rows = []
    pts = np.array([[(m >> i) & 1 for i in range(n)] for m in range(N)])
    for _ in range(3000 if n < 10 else 600):
        k = rng.integers(1, 6)
        gens = pts[rng.choice(N, size=k, replace=False)]
        up = np.zeros(N, bool)
        for gvec in gens:
            up |= (pts >= gvec).all(1)
        rows.append(np.where(up, 1.0, -1.0))
    E, I = EI(wht_rows(np.array(rows)), n); report(f"random monotone n={n}", E, I)

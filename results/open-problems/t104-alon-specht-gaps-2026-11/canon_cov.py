"""Is the family of states { P(x.y) : y orthogonal to 1 and x } enough for tau = [2,1^(n-2)], sigma = [2,2,1^(n-4)]?

For a unit x with sum 0 and a covariance C >= 0 on {1, x}^perp, rho(x, C) is the normalised mixture of the vectors
P((x y^t + y x^t)/sqrt 2) with y ~ C.  slack_ij(C) = (2 - d_ij^2) tr(C G) - c tr(C H_ij), c = (n-2)/(n-1), is linear
in C.  For each x we maximise min_ij slack_ij over C (trace 1) and report the smallest maximum over the x tried.
A value >= 0 for every x would say the family is enough; a negative value at some x says it is not.
usage: canon_cov.py n vectors seed
"""
import sys
import numpy as np
from scipy.optimize import minimize


def forms(x):
    n = len(x)
    one = np.ones(n) / np.sqrt(n)
    Pi = np.eye(n) - np.outer(one, one)
    B = np.linalg.svd(np.vstack([one, x]))[2][2:]
    m = n - 2
    PT = []
    for y in B:
        T = (np.outer(x, y) + np.outer(y, x)) / np.sqrt(2.0)
        PT.append(T - (n / (n - 2.0)) * Pi @ np.diag(np.diag(T)) @ Pi)
    G = np.array([[(PT[a] * PT[b]).sum() for b in range(m)] for a in range(m)])
    pairs, H, w = [], [], []
    for i in range(n):
        for j in range(i + 1, n):
            p = np.arange(n)
            p[i], p[j] = j, i
            S = [t[np.ix_(p, p)] for t in PT]
            H.append(G + np.array([[(PT[a] * S[b]).sum() for b in range(m)] for a in range(m)]))
            w.append(2 - (x[i] - x[j]) ** 2)
            pairs.append((i, j))
    return G, np.array(H), np.array(w)


def best_C(x, rng, starts=5):
    n = len(x)
    m = n - 2
    c = (n - 2.0) / (n - 1.0)
    G, H, w = forms(x)
    Mats = w[:, None, None] * G[None] - c * H               # slack_ij(C) = tr(C Mats_ij)
    tril = np.tril_indices(m)

    def neg(z):
        L = np.zeros((m, m))
        L[tril] = z
        C = L @ L.T
        tr = np.trace(C)
        if tr < 1e-14:
            return 1e3
        return -np.min(np.tensordot(Mats, C / tr, axes=2))

    best = float("inf")
    for s in range(starts):
        z0 = np.eye(m)[tril] if s == 0 else rng.normal(0, 1, len(tril[0]))
        res = minimize(neg, z0, method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 400 * len(z0)})
        res = minimize(neg, res.x, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 400 * len(z0)})
        best = min(best, res.fun)
    return -best


def unit(z):
    z = z - z.mean()
    return z / np.linalg.norm(z)


def main():
    n, vectors, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    star = unit(np.array([n - 1.0] + [-1.0] * (n - 1)))
    edge = unit(np.array([1.0, -1.0] + [0.0] * (n - 2)))
    worst, arg = float("inf"), None
    hist = []
    for k in range(vectors):
        kind = k % 4
        if kind == 0:
            x = rng.normal(0, 1, n)
        elif kind == 1:
            t = rng.uniform(0, 1)
            x = t * star + (1 - t) * edge + 0.05 * rng.normal(0, 1, n)
        elif kind == 2:
            x = star + 0.3 * rng.normal(0, 1, n)
        else:
            x = rng.normal(0, 1, n) * (rng.uniform(0, 1, n) < 0.6)
        if np.linalg.norm(x - np.mean(x)) < 1e-6:
            continue
        x = unit(x)
        v = best_C(x, rng)
        hist.append(v)
        if v < worst:
            worst, arg = v, x
    hist = np.array(hist)
    print("n=%d: %d vectors; best min-slack over C: smallest %.6e, median %.4f, share below -1e-7: %.3f"
          % (n, len(hist), worst, np.median(hist), (hist < -1e-7).mean()))
    print("  worst x = %s" % " ".join("%.5f" % v for v in np.sort(arg)))


if __name__ == "__main__":
    main()

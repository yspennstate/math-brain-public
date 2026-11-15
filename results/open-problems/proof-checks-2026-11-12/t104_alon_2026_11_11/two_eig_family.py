"""The gap-weighted inequality on the two-eigenvalue family (GAP_STATE_FORM.md, section "Two-eigenvalue family").

Family: x a unit sum-zero vector, N = g Q with Q the projection onto {1, x}^perp, i.e. the weighted graph
    w_ij = (lam - g)/n - g x_i x_j,      L = lam x x^t + (lam - g)(Pi - x x^t).
The smallest admissible lam is g (1 + n m), m = max_{i != j} x_i x_j.  With q = sum x_i^4, p3 = sum x_i^3 the claim is
    Gval = 2 g^2 Psi,   Psi = (n-4)(2q - 1) - 2(n-3) p3^2 + (n-1)(n^2 - 6n + 6 + 2nq) m.
The script (1) compares the formula with gval of canon_gap.py, (2) minimises Psi over x by random starts and
Nelder-Mead and prints the smallest value found for each n.
usage: two_eig_family.py starts seed nmin nmax
"""
import sys
import numpy as np
from scipy.optimize import minimize
from canon_gap import gval


def unit0(z):
    z = z - z.mean()
    s = np.linalg.norm(z)
    return z / s if s > 1e-12 else None


def psi(x):
    n = len(x)
    q = float((x ** 4).sum())
    p3 = float((x ** 3).sum())
    P = np.outer(x, x)
    np.fill_diagonal(P, -np.inf)
    m = float(P.max())
    return (n - 4) * (2 * q - 1) - 2 * (n - 3) * p3 ** 2 + (n - 1) * (n * n - 6 * n + 6 + 2 * n * q) * m, q, p3, m


def formula_check(rng):
    worst = 0.0
    for _ in range(300):
        n = int(rng.integers(4, 10))
        x = unit0(rng.normal(size=n) * rng.uniform(0, 1, n) ** 2)
        if x is None:
            continue
        ps, q, p3, m = psi(x)
        if m < 1e-6:
            continue
        g = 2.0 / (1 + n * (n - 1) * m)          # makes the total weight 1
        lam = g * (1 + n * m)
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        w = np.array([(lam - g) / n - g * x[i] * x[j] for (i, j) in pairs])
        if w.min() < -1e-12 or abs(w.sum() - 1) > 1e-9:
            worst = max(worst, 1.0)
            continue
        w = np.maximum(w, 0)
        worst = max(worst, abs(gval(w, n, pairs)[0] - 2 * g * g * ps))
    return worst


def main():
    starts, seed, nmin, nmax = (int(a) for a in sys.argv[1:5])
    rng = np.random.default_rng(seed)
    print("formula against gval: largest deviation %.2e (300 vectors, n = 4..9)" % formula_check(rng))
    for n in range(nmin, nmax + 1):
        best = (float("inf"), None)
        f = lambda z: (psi(unit0(z))[0] if unit0(z) is not None else 1e9)
        for s in range(starts):
            kind = s % 4
            if kind == 0:
                z = rng.normal(size=n)
            elif kind == 1:
                z = rng.normal(size=n) * (rng.uniform(size=n) < 0.5)
            elif kind == 2:                       # near a star vector
                z = -np.ones(n); z[0] = n - 1; z = z + 0.3 * rng.normal(size=n)
            else:                                 # near an edge vector
                z = np.zeros(n); z[0], z[1] = 1, -1; z = z + 0.2 * rng.normal(size=n)
            if unit0(z) is None:
                continue
            r = minimize(f, z, method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 4000})
            if r.fun < best[0]:
                best = (float(r.fun), unit0(r.x))
        x = np.sort(best[1])[::-1]
        ps, q, p3, m = psi(x)
        print("n=%d: smallest Psi %+.3e  (q %.4f, p3^2 %.4f, m %.5f)  x = %s"
              % (n, ps, q, p3 * p3, m, " ".join("%+.4f" % v for v in x)))


if __name__ == "__main__":
    main()

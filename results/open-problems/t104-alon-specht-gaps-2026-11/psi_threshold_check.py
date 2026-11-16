"""Psi with m replaced by the best average of x_i x_j over the k smallest or the k largest coordinates
(k = 2..n-1; 2(n-2) sets instead of all subsets).  Same split as psi_split_check.py:
    Psi_A(x) = K ((n-1) mu_A - 1/n) + 2 (n-3) D,   mu_A = ((sum_A x)^2 - sum_A x^2) / (k (k-1)).
Minimised over unit sum-zero x.  usage: psi_threshold_check.py starts seed nmin nmax
"""
import sys
import numpy as np
from scipy.optimize import minimize
from two_eig_family import psi, unit0


def psi_thr(x, side="both"):
    n = len(x)
    ps, q, p3, m = psi(x)
    K = n * n - 6 * n + 6 + 2 * n * q
    D = q - 1.0 / n - p3 * p3
    s = np.sort(x)
    best = -np.inf
    for k in range(2, n):
        lo, hi = s[:k], s[n - k:]
        cands = []
        if side in ("both", "low"):
            cands.append(lo)
        if side in ("both", "high"):
            cands.append(hi)
        for a in cands:
            best = max(best, (a.sum() ** 2 - (a * a).sum()) / (k * (k - 1)))
    return K * ((n - 1) * best - 1.0 / n) + 2 * (n - 3) * D, best, m


def main():
    starts, seed, nmin, nmax = (int(a) for a in sys.argv[1:5])
    rng = np.random.default_rng(seed)
    for n in range(nmin, nmax + 1):
        f = lambda z: (psi_thr(unit0(z))[0] if unit0(z) is not None else 1e9)
        best = (float("inf"), None)
        for s in range(starts):
            kind = s % 4
            if kind == 0:
                z = rng.normal(size=n)
            elif kind == 1:
                z = rng.normal(size=n) * (rng.uniform(size=n) < 0.5)
            elif kind == 2:
                z = -np.ones(n); z[0] = n - 1; z = z + 0.3 * rng.normal(size=n)
            else:
                z = -np.ones(n) * (rng.uniform(size=n) < 0.6); z[0] = -z.sum() + 0.2 * rng.normal(); z = z + 0.05 * rng.normal(size=n)
            if unit0(z) is None:
                continue
            r = minimize(f, z, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 6000})
            if r.fun < best[0]:
                best = (float(r.fun), unit0(r.x))
        x = np.sort(best[1])[::-1]
        val, mu, m = psi_thr(x)
        print("n=%d smallest %+.4e  (mu %.5f, m %.5f, Psi %+.4e)  x = %s"
              % (n, val, mu, m, psi(x)[0], " ".join("%+.4f" % v for v in x)), flush=True)


if __name__ == "__main__":
    main()

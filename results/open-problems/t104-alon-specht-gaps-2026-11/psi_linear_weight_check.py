"""Psi with m replaced by the weighted-pair bound with weights c_i = |alpha - x_i|, alpha = max x or alpha = min x:
    m ((sum c)^2 - sum c^2) >= (sum c_i x_i)^2 - sum c_i^2 x_i^2
gives, for alpha outside the open interval (min x, max x),
    m >= M(alpha) = (1 - q + 2 alpha p3 - alpha^2) / (n (n-1) alpha^2 - 1),
a bound in q, p3 and one extreme coordinate only.  Phi(x) = K ((n-1) max(M(max x), M(min x)) - 1/n) + 2 (n-3) D
is minimised over unit sum-zero x.  mode "ext": alpha in {max x, min x}; mode "one": alpha = the extreme
coordinate of larger modulus only.  usage: psi_linear_weight_check.py starts seed nmin nmax
"""
import sys
import numpy as np
from scipy.optimize import minimize
from two_eig_family import psi, unit0


def phi(x, mode="ext"):
    n = len(x)
    ps, q, p3, m = psi(x)
    K = n * n - 6 * n + 6 + 2 * n * q
    D = q - 1.0 / n - p3 * p3
    hi, lo = x.max(), x.min()
    al = [hi, lo] if mode == "ext" else [hi if abs(hi) >= abs(lo) else lo]
    best = -np.inf
    for a in al:
        den = n * (n - 1) * a * a - 1
        if den > 1e-12:
            best = max(best, (1 - q + 2 * a * p3 - a * a) / den)
    return K * ((n - 1) * best - 1.0 / n) + 2 * (n - 3) * D, best, m


def main():
    starts, seed, nmin, nmax = (int(a) for a in sys.argv[1:5])
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(4000):
        n = int(rng.integers(4, 12))
        x = unit0(rng.normal(size=n) * rng.uniform(0, 1, n) ** 2)
        v, M, m = phi(x)
        worst = max(worst, M - m)
    print("bound check: largest M - m over 4000 vectors %.2e (must be <= 0)" % worst)
    for mode in ("ext", "one"):
        for n in range(nmin, nmax + 1):
            f = lambda z: (phi(unit0(z), mode)[0] if unit0(z) is not None else 1e9)
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
                r = minimize(f, z, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 4000})
                if r.fun < best[0]:
                    best = (float(r.fun), unit0(r.x))
            x = np.sort(best[1])[::-1]
            val, M, m = phi(x, mode)
            print("%s n=%d smallest %+.4e  (M %.5f, m %.5f, Psi %+.4e)  x = %s"
                  % (mode, n, val, M, m, psi(x)[0], " ".join("%+.4f" % v for v in x)), flush=True)


if __name__ == "__main__":
    main()

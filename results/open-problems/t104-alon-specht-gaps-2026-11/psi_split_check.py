"""Two checks on Psi of the two-eigenvalue family (GAP_STATE_FORM.md).

(1) The split   Psi = K ((n-1) m - 1/n) + 2 (n-3) D,   K = n^2 - 6n + 6 + 2nq,   D = q - 1/n - p3^2 >= 0
    (D is the Cauchy-Schwarz defect of p3 = <x, x^2 - 1/n>).  So Psi >= 0 whenever m >= 1/(n(n-1)).
(2) Replace m by the averaged lower bound
        mu_U = ((sum_U x)^2 + sum_U x^2 - 1) / ((n-|U|)(n-|U|-1)),
    the mean of x_i x_j over ordered pairs outside U (U a set of at most n-2 indices), and minimise
        Psi_U(x) = K ((n-1) max_U mu_U - 1/n) + 2 (n-3) D
    over unit sum-zero x: once with |U| <= 2, once with all U.  A nonnegative minimum would reduce Psi >= 0 to
    polynomial inequalities without a maximum over pairs.
usage: psi_split_check.py starts seed nmin nmax
"""
import sys
import itertools
import numpy as np
from scipy.optimize import minimize
from two_eig_family import psi, unit0


def parts(x):
    n = len(x)
    ps, q, p3, m = psi(x)
    K = n * n - 6 * n + 6 + 2 * n * q
    D = q - 1.0 / n - p3 * p3
    return ps, K, D, m


def masks(n, kmax):
    out = []
    for k in range(1, kmax + 1):
        for U in itertools.combinations(range(n), k):
            v = np.zeros(n)
            v[list(U)] = 1
            out.append(v)
    return np.array(out)


def psi_avg(x, Mk):
    n = len(x)
    ps, K, D, m = parts(x)
    k = Mk.sum(axis=1)
    mu = ((Mk @ x) ** 2 + Mk @ (x * x) - 1) / ((n - k) * (n - k - 1))
    return K * ((n - 1) * mu.max() - 1.0 / n) + 2 * (n - 3) * D, mu.max(), m


def main():
    starts, seed, nmin, nmax = (int(a) for a in sys.argv[1:5])
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(2000):
        n = int(rng.integers(4, 10))
        x = unit0(rng.normal(size=n) * rng.uniform(0, 1, n) ** 2)
        if x is None:
            continue
        ps, K, D, m = parts(x)
        worst = max(worst, abs(ps - (K * ((n - 1) * m - 1.0 / n) + 2 * (n - 3) * D)))
        if D < -1e-12:
            worst = 9.0
    print("split identity: largest deviation %.2e (2000 vectors, n = 4..9), D >= 0 throughout" % worst)
    for n in range(nmin, nmax + 1):
        for label, kmax in (("|U|<=2", 2), ("all U", n - 2)):
            Mk = masks(n, kmax)
            f = lambda z: (psi_avg(unit0(z), Mk)[0] if unit0(z) is not None else 1e9)
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
                    z = np.zeros(n); z[0], z[1] = 1, -1; z = z + 0.2 * rng.normal(size=n)
                if unit0(z) is None:
                    continue
                r = minimize(f, z, method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 3000})
                if r.fun < best[0]:
                    best = (float(r.fun), unit0(r.x))
            x = np.sort(best[1])[::-1]
            val, mu, m = psi_avg(x, Mk)
            print("n=%d %-7s smallest %+.4e  (mu %.5f, m %.5f, Psi %+.4e)  x = %s"
                  % (n, label, val, mu, m, psi(x)[0], " ".join("%+.4f" % v for v in x)))


if __name__ == "__main__":
    main()

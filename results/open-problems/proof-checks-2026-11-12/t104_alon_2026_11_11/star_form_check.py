"""Check the compact form (*) of HOOKS_AND_TWO_ROWS.md section 5 against the matrices of canon_cov.py.

For a unit x with sum 0 and a covariance C (trace 1) on {1, x}^perp, with y ~ C:
    kappa = E sum_k x_k^2 y_k^2,   g_ij = E (x_i y_i - x_j y_j)^2,   c_ij = E (y_i - y_j)^2,   d = x_i - x_j,
    (n-1) * slack_ij(C) = (2 - d^2) + (2 n kappa/(n-2)) ((n-1) d^2 - 2) - 2 n g_ij - (n-2) (2 d^2 - 1) c_ij.
usage: star_form_check.py trials seed
"""
import sys
import numpy as np
from canon_cov import forms, unit


def main():
    trials, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(seed)
    worst = 0.0
    for t in range(trials):
        n = int(rng.integers(4, 9))
        x = unit(rng.normal(0, 1, n))
        one = np.ones(n) / np.sqrt(n)
        B = np.linalg.svd(np.vstack([one, x]))[2][2:]           # same basis as forms()
        m = n - 2
        R = rng.normal(0, 1, (m, m))
        C = R @ R.T
        C /= np.trace(C)
        G, H, w = forms(x)
        c = (n - 2.0) / (n - 1.0)
        Cn = B.T @ C @ B                                         # covariance of y in R^n
        kappa = float((x ** 2 * np.diag(Cn)).sum())
        k = 0
        for i in range(n):
            for j in range(i + 1, n):
                lhs = (n - 1.0) * (w[k] * np.tensordot(C, G) - c * np.tensordot(C, H[k]))
                d2 = (x[i] - x[j]) ** 2
                e = np.zeros(n); e[i], e[j] = 1, -1
                cij = e @ Cn @ e
                f = np.zeros(n); f[i], f[j] = x[i], -x[j]
                gij = f @ Cn @ f
                rhs = (2 - d2) + (2 * n * kappa / (n - 2.0)) * ((n - 1) * d2 - 2) - 2 * n * gij - (n - 2) * (2 * d2 - 1) * cij
                worst = max(worst, abs(lhs - rhs))
                k += 1
    print("compact form against matrices: largest deviation %.2e over %d random (n, x, C), n = 4..8" % (worst, trials))


if __name__ == "__main__":
    main()

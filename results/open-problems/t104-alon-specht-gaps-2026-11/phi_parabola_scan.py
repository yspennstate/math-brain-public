"""Phi' of GAP_STATE_FORM.md on the relaxed extreme set.

x = (S, y), y_i = -a + z_i, a = S/(n-1), N = n-1, sum z = 0, sum z^2 = rho^2 = 1 - n S^2/(n-1),
Z3 = sum z^3 = w rho^3, |w| <= wmax = (N-2)/sqrt(N(N-1)), and Z4 >= rho^4 (w^2 + 1/N) with equality iff z is
two-valued.  For fixed S, Phi' is concave in (Z3, Z4) (n >= 5), and the attainable (Z3, Z4) lie in the convex hull
of the arc Z4 = rho^4 (w^2 + 1/N), |w| <= wmax.  So Phi' >= 0 on the arc for all S^2 in [1/n, (n-1)/n] implies
Phi' >= 0 everywhere.  The script scans the arc and prints the minimum for each n.
usage: phi_parabola_scan.py nmin nmax grid
"""
import sys
import numpy as np


def phi_arc(n, u, w):
    """u = S^2, w = Z3 / rho^3; returns Phi' / (n Den) (i.e. the lower bound for Psi) and Phi'."""
    N = n - 1
    S = np.sqrt(u)
    a = S / N
    r2 = 1 - n * u / N
    r2 = np.maximum(r2, 0.0)
    rho = np.sqrt(r2)
    Z3 = w * rho ** 3
    Z4 = r2 ** 2 * (w * w + 1.0 / N)
    p3 = S ** 3 - N * a ** 3 - 3 * a * r2 + Z3
    q = u * u + N * a ** 4 + 6 * a * a * r2 - 4 * a * Z3 + Z4
    K = n * n - 6 * n + 6 + 2 * n * q
    D = q - 1.0 / n - p3 * p3
    den = n * (n - 1) * u - 1
    Nn = n * (n - 1) * (1 - q + 2 * S * p3 - 2 * u) + 1
    return K * Nn + 2 * n * (n - 3) * den * D, den


def main():
    nmin, nmax, g = (int(a) for a in sys.argv[1:4])
    for n in range(nmin, nmax + 1):
        N = n - 1
        wmax = (N - 2) / np.sqrt(N * (N - 1))
        u = np.linspace(1.0 / n, (n - 1.0) / n, g)[:, None]
        w = np.linspace(-wmax, wmax, g)[None, :]
        F, den = phi_arc(n, u, w)
        i, j = np.unravel_index(np.argmin(F), F.shape)
        # value at the edge corner and at the star
        fe, _ = phi_arc(n, np.array(0.5), np.array(-wmax))
        fs, _ = phi_arc(n, np.array((n - 1.0) / n), np.array(0.0))
        neg = int((F < -1e-9).sum())
        print("n=%d min Phi' %+.4e at u=%.4f w/wmax=%+.4f | edge %+.2e star %+.2e | grid points below -1e-9: %d of %d"
              % (n, F[i, j], u[i, 0], w[0, j] / wmax, float(fe), float(fs), neg, F.size), flush=True)


if __name__ == "__main__":
    main()

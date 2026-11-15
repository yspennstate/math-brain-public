"""Phi' (GAP_STATE_FORM.md) on the boundary of the moment section.

x = (S, y), S the coordinate of largest modulus, y the other N = n-1 coordinates.  Replace the empirical measure of
y by any probability measure on [-S, S] with mean -S/N and second moment (1 - S^2)/N.  For fixed S the pairs
(third moment, fourth moment) form a convex set and Phi' is concave on it (n >= 5), so its minimum is on the boundary:
  L: two atoms s > t inside [-S, S], weights theta, 1 - theta;
  U: atoms -S, t, S with weights alpha, beta, gamma.
The script scans both families and prints the minimum of Phi' for each n.
usage: phi_boundary_scan.py nmin nmax grid
"""
import sys
import numpy as np


def phi_from_moments(n, u, m3, m4):
    N = n - 1
    S = np.sqrt(u)
    p3 = S ** 3 + N * m3
    q = u * u + N * m4
    K = n * n - 6 * n + 6 + 2 * n * q
    D = q - 1.0 / n - p3 * p3
    den = n * (n - 1) * u - 1
    Nn = n * (n - 1) * (1 - q + 2 * S * p3 - 2 * u) + 1
    return K * Nn + 2 * n * (n - 3) * den * D


def scan_L(n, g):
    N = n - 1
    u = np.linspace(1.0 / n, (n - 1.0) / n, g)[:, None]
    th = np.linspace(1e-4, 1 - 1e-4, g)[None, :]
    S = np.sqrt(u)
    a = S / N
    v = np.maximum((1 - u) / N - a * a, 0.0)
    s = -a + np.sqrt(v * (1 - th) / th)
    t = -a - np.sqrt(v * th / (1 - th))
    ok = (s <= S + 1e-12) & (t >= -S - 1e-12)
    m3 = th * s ** 3 + (1 - th) * t ** 3
    m4 = th * s ** 4 + (1 - th) * t ** 4
    F = np.where(ok, phi_from_moments(n, u, m3, m4), np.inf)
    i, j = np.unravel_index(np.argmin(F), F.shape)
    return F[i, j], u[i, 0], th[0, j], int((F < -1e-8).sum()), int(ok.sum())


def scan_U(n, g):
    N = n - 1
    u = np.linspace(1.0 / n, (n - 1.0) / n, g)[:, None]
    S = np.sqrt(u)
    a = S / N
    mu2 = (1 - u) / N
    r = np.linspace(-1 + 1e-6, 1 - 1e-6, g)[None, :]
    t = r * S
    beta = (u - mu2) / (u - t * t)
    dif = (-a - beta * t) / S
    tot = 1 - beta
    gam = 0.5 * (tot + dif)
    alp = 0.5 * (tot - dif)
    ok = (beta >= -1e-12) & (beta <= 1 + 1e-12) & (gam >= -1e-12) & (alp >= -1e-12)
    m3 = (gam - alp) * S ** 3 + beta * t ** 3
    m4 = (gam + alp) * u * u + beta * t ** 4
    F = np.where(ok, phi_from_moments(n, u, m3, m4), np.inf)
    i, j = np.unravel_index(np.argmin(F), F.shape)
    return F[i, j], u[i, 0], r[0, j], int((F < -1e-8).sum()), int(ok.sum())


def main():
    nmin, nmax, g = (int(a) for a in sys.argv[1:4])
    for n in range(nmin, nmax + 1):
        fl, ul, tl, nl, okl = scan_L(n, g)
        fu, uu, tu, nu, oku = scan_U(n, g)
        print("n=%d  L: min %+.4e at u=%.4f theta=%.4f, below -1e-8: %d of %d   U: min %+.4e at u=%.4f t/S=%+.4f, below -1e-8: %d of %d"
              % (n, fl, ul, tl, nl, okl, fu, uu, tu, nu, oku), flush=True)


if __name__ == "__main__":
    main()

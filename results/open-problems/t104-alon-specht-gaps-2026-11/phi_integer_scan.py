"""Phi' on genuine vectors x = (S, s x k, t x (N-k)), s > t, N = n-1, 1 <= k <= N-1, with |s|, |t| <= S
(S the coordinate of largest modulus).  For each n the script scans u = S^2 and prints the minimum of Phi', and
the minimum of the true Psi on the same vectors.  usage: phi_integer_scan.py nmin nmax grid
"""
import sys
import numpy as np
from two_eig_family import psi


def main():
    nmin, nmax, g = (int(a) for a in sys.argv[1:4])
    for n in range(nmin, nmax + 1):
        N = n - 1
        best = (np.inf, None)
        bestpsi = (np.inf, None)
        neg = 0
        tot = 0
        for k in range(1, N):
            th = k / N
            for u in np.linspace(1.0 / n, (n - 1.0) / n, g):
                S = np.sqrt(u)
                a = S / N
                v = (1 - u) / N - a * a
                if v < 0:
                    continue
                s = -a + np.sqrt(v * (1 - th) / th)
                t = -a - np.sqrt(v * th / (1 - th))
                if s > S + 1e-12 or t < -S - 1e-12:
                    continue
                x = np.array([S] + [s] * k + [t] * (N - k))
                ps, q, p3, m = psi(x)
                K = n * n - 6 * n + 6 + 2 * n * q
                D = q - 1.0 / n - p3 * p3
                den = n * (n - 1) * u - 1
                F = K * (n * (n - 1) * (1 - q + 2 * S * p3 - 2 * u) + 1) + 2 * n * (n - 3) * den * D
                tot += 1
                if F < -1e-9:
                    neg += 1
                if F < best[0]:
                    best = (F, (k, u, s, t, ps))
                if ps < bestpsi[0]:
                    bestpsi = (ps, (k, u))
        k, u, s, t, ps = best[1]
        print("n=%d min Phi' %+.4e at k=%d u=%.4f s=%+.4f t=%+.4f (Psi there %+.4e); points below -1e-9: %d of %d; min Psi %+.3e at k=%d u=%.4f"
              % (n, best[0], k, u, s, t, ps, neg, tot, bestpsi[0], bestpsi[1][0], bestpsi[1][1]), flush=True)


if __name__ == "__main__":
    main()

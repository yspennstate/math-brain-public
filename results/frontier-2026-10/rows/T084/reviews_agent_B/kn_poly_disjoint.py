"""Exact covariance numerator N = Z_e^2 - Z Z_ef for the DISJOINT pair e = ab, f = cd on K_n, a polynomial in (lam, u), q = 1 - u,
by the recursion of kn_gibbs_disjoint.py."""
from math import comb
from sympy import Poly
from kn_poly_adjacent import lam, u


def numerator(n):
    P = lambda e: Poly(e, lam, u, domain="ZZ")
    one, L, O = P(1), P(lam), P(0)
    G = [P((1 + lam) ** (s * (s - 1) // 2)) for s in range(n + 1)]
    C = [O] * (n + 1); F = [O] * (n + 1); D4 = [O] * (n + 1)
    for s in range(1, n + 1):
        C[s] = G[s] - sum((comb(s - 1, k - 1) * C[k] * G[s - k] for k in range(1, s)), O)
    for s in range(2, n + 1):
        F[s] = L * P((1 + lam) ** (s * (s - 1) // 2 - 1)) - sum((comb(s - 2, k - 2) * F[k] * G[s - k] for k in range(2, s)), O)
    for s in range(4, n + 1):
        sep = sum((comb(s - 4, k1 - 2) * comb(s - 2 - k1, k2 - 2) * F[k1] * F[k2] * G[s - k1 - k2]
                   for k1 in range(2, s - 1) for k2 in range(2, s - k1 + 1)), O)
        D4[s] = L * L * P((1 + lam) ** (s * (s - 1) // 2 - 2)) - sum((comb(s - 4, k - 4) * D4[k] * G[s - k] for k in range(4, s)), O) - sep
    q = P(1 - u)
    Z = [one] + [O] * n
    for m in range(1, n + 1):
        Z[m] = sum((comb(m - 1, k - 1) * q * C[k] * Z[m - k] for k in range(1, m + 1)), O)
    Zef = sum((comb(n - 4, s - 4) * q * D4[s] * Z[n - s] for s in range(4, n + 1)), O) + \
        sum((comb(n - 4, k1 - 2) * comb(n - 2 - k1, k2 - 2) * q * q * F[k1] * F[k2] * Z[n - k1 - k2]
             for k1 in range(2, n - 1) for k2 in range(2, n - k1 + 1)), O)
    Ze = sum((comb(n - 2, s - 2) * q * F[s] * Z[n - s] for s in range(2, n + 1)), O)
    return Ze ** 2 - Z[n] * Zef

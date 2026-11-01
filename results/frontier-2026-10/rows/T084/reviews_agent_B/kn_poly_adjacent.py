"""Exact covariance numerator for the adjacent pair on K_n as a polynomial in (lam, u), q = 1 - u, via the cluster recursion of
kn_gibbs.py. N = Z_e^2 - Z Z_ef (Z_e = Z_f by symmetry). Negative correlation for all q < 1, lam > 0 follows on that K_n if N/u^r has
only nonnegative coefficients (r = the order of vanishing at u = 0). Prints r and the negative coefficients."""
import sys, json
from math import comb
from sympy import symbols, Poly
lam, u = symbols("lam u")


def numerator(n):
    P = lambda e: Poly(e, lam, u, domain="ZZ")
    one, L = P(1), P(lam)
    G = [P((1 + lam) ** (s * (s - 1) // 2)) for s in range(n + 1)]
    C = [P(0)] * (n + 1); F = [P(0)] * (n + 1); D = [P(0)] * (n + 1)
    for s in range(1, n + 1):
        C[s] = G[s] - sum((comb(s - 1, k - 1) * C[k] * G[s - k] for k in range(1, s)), P(0))
    for s in range(2, n + 1):
        F[s] = L * P((1 + lam) ** (s * (s - 1) // 2 - 1)) - sum((comb(s - 2, k - 2) * F[k] * G[s - k] for k in range(2, s)), P(0))
    for s in range(3, n + 1):
        D[s] = L * L * P((1 + lam) ** (s * (s - 1) // 2 - 2)) - sum((comb(s - 3, k - 3) * D[k] * G[s - k] for k in range(3, s)), P(0))
    q = P(1 - u)
    Z = [one] + [P(0)] * n
    for m in range(1, n + 1):
        Z[m] = sum((comb(m - 1, k - 1) * q * C[k] * Z[m - k] for k in range(1, m + 1)), P(0))
    glob = lambda X, r: sum((comb(n - r, s - r) * q * X[s] * Z[n - s] for s in range(r, n + 1)), P(0))
    return glob(F, 2) ** 2 - Z[n] * glob(D, 3)


if __name__ == "__main__":
    for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        N = numerator(n)
        terms = N.terms()
        r = min(m[1] for m, c in terms)
        neg = [(m, int(c)) for m, c in terms if c < 0]
        print(json.dumps({"n": n, "u_order": r, "min_lam_order": min(m[0] for m, c in terms), "n_terms": len(terms), "n_negative": len(neg),
                          "negatives_sample": neg[:6]}), flush=True)

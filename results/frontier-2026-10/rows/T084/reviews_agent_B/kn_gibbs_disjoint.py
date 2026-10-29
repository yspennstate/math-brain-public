"""Disjoint pair e = ab, f = cd on K_n: Cov(X_e, X_f) <= 0 iff Z Z_ef <= Z_e^2, exactly by cluster decomposition (mpmath).
D4_s: connected on s vertices containing both fixed disjoint edges:
  lam^2 (1+lam)^(C(s,2)-2) = sum_k C(s-4,k-4) D4_k G_{s-k} + sum_{k1,k2} C(s-4,k1-2) C(s-2-k1,k2-2) F_k1 F_k2 G_{s-k1-k2}.
Z_ef = sum_s C(n-4,s-4) q D4_s Z_{n-s} + sum_{k1,k2} C(n-4,k1-2) C(n-2-k1,k2-2) q^2 F_k1 F_k2 Z_{n-k1-k2}."""
import sys, json
from mpmath import mp, mpf, nstr, binomial as Bn
mp.dps = 400


def run(n, q, lam):
    q = mpf(q); lam = mpf(lam)
    G = [(1 + lam) ** (s * (s - 1) // 2) for s in range(n + 1)]
    C = [mpf(0)] * (n + 1); F = [mpf(0)] * (n + 1); D4 = [mpf(0)] * (n + 1)
    for s in range(1, n + 1):
        C[s] = G[s] - sum(Bn(s - 1, k - 1) * C[k] * G[s - k] for k in range(1, s))
    for s in range(2, n + 1):
        F[s] = lam * (1 + lam) ** (s * (s - 1) // 2 - 1) - sum(Bn(s - 2, k - 2) * F[k] * G[s - k] for k in range(2, s))
    for s in range(4, n + 1):
        sep = sum(Bn(s - 4, k1 - 2) * Bn(s - 2 - k1, k2 - 2) * F[k1] * F[k2] * G[s - k1 - k2]
                  for k1 in range(2, s - 1) for k2 in range(2, s - k1 + 1))
        D4[s] = lam ** 2 * (1 + lam) ** (s * (s - 1) // 2 - 2) - sum(Bn(s - 4, k - 4) * D4[k] * G[s - k] for k in range(4, s)) - sep
    Z = [mpf(1)] + [mpf(0)] * n
    for m in range(1, n + 1):
        Z[m] = sum(Bn(m - 1, k - 1) * q * C[k] * Z[m - k] for k in range(1, m + 1))
    Zef = sum(Bn(n - 4, s - 4) * q * D4[s] * Z[n - s] for s in range(4, n + 1)) + \
        sum(Bn(n - 4, k1 - 2) * Bn(n - 2 - k1, k2 - 2) * q ** 2 * F[k1] * F[k2] * Z[n - k1 - k2]
            for k1 in range(2, n - 1) for k2 in range(2, n - k1 + 1))
    Ze = sum(Bn(n - 2, s - 2) * q * F[s] * Z[n - s] for s in range(2, n + 1))
    r = Z[n] * Zef / Ze ** 2
    return {"n": n, "q": float(q), "n_lambda": float(n * lam), "pair": "disjoint", "cov_sign_ratio": float(r),
            "one_minus_ratio": nstr(1 - r, 8)}


if __name__ == "__main__":
    n, q, nl = int(sys.argv[1]), sys.argv[2], sys.argv[3]
    print(json.dumps(run(n, q, mpf(nl) / n)))

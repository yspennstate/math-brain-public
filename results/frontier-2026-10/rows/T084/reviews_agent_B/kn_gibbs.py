"""Random-cluster model on K_n, adjacent pair e = ab, f = bc, computed exactly through the cluster (Gibbs-partition)
decomposition, high-precision mpmath. Weights lambda^|A| q^k(A).
  G_s = (1+lam)^C(s,2); C_s connected spanning subgraphs of K_s;
  F_s connected on s vertices containing a fixed edge; D_s connected containing two fixed adjacent edges;
  Bc_s (both bridges), Jc_s ({e,f} a 2-edge cut, neither alone a bridge: b's side and the a,c side), UV_s = sum_B |U||V|;
  Z_m = sum_k C(m-1,k-1) q C_k Z_{m-k}.
Global: Z_ef = sum_s C(n-3,s-3) q D_s Z_{n-s}, Z_e = sum_s C(n-2,s-2) q F_s Z_{n-s};  Cov <= 0  iff  Z Z_ef <= Z_e^2.
B, J, sum_B w|U||V| likewise with Bc, Jc, UV.  E_J[N] = lam sum_B w|U||V| / J (identity in all_edge_injection.py)."""
import sys, json
from mpmath import mp, mpf, nstr, binomial as Bn
mp.dps = 400


def run(n, q, lam):
    q = mpf(q); lam = mpf(lam)
    G = [(1 + lam) ** (s * (s - 1) // 2) for s in range(n + 1)]
    C = [mpf(0)] * (n + 1); F = [mpf(0)] * (n + 1); D = [mpf(0)] * (n + 1)
    for s in range(1, n + 1):
        C[s] = G[s] - sum(Bn(s - 1, k - 1) * C[k] * G[s - k] for k in range(1, s))
    for s in range(2, n + 1):
        F[s] = lam * (1 + lam) ** (s * (s - 1) // 2 - 1) - sum(Bn(s - 2, k - 2) * F[k] * G[s - k] for k in range(2, s))
    for s in range(3, n + 1):
        D[s] = lam ** 2 * (1 + lam) ** (s * (s - 1) // 2 - 2) - sum(Bn(s - 3, k - 3) * D[k] * G[s - k] for k in range(3, s))
    Bc = [mpf(0)] * (n + 1); UV = [mpf(0)] * (n + 1)
    for s in range(3, n + 1):
        for u in range(1, s - 1):
            for v in range(1, s - u):
                m = s - u - v
                w = lam ** 2 * Bn(s - 3, u - 1) * Bn(s - 2 - u, v - 1) * C[u] * C[m] * C[v]
                Bc[s] += w; UV[s] += w * u * v
    # J: e and f each a non-bridge, {e, f} a cut: b's side (size p) and the a,c side, both connected
    Jc = [lam ** 2 * sum(Bn(s - 3, p - 1) * C[p] * C[s - p] for p in range(1, s - 1)) if s >= 3 else mpf(0) for s in range(n + 1)]
    Z = [mpf(1)] + [mpf(0)] * n
    for m in range(1, n + 1):
        Z[m] = sum(Bn(m - 1, k - 1) * q * C[k] * Z[m - k] for k in range(1, m + 1))
    glob = lambda X, r: sum(Bn(n - r, s - r) * q * X[s] * Z[n - s] for s in range(r, n + 1))
    Zef, Ze, Bt, Jt, UVt = glob(D, 3), glob(F, 2), glob(Bc, 3), glob(Jc, 3), glob(UV, 3)
    Zn = Z[n]
    return {"n": n, "q": float(q), "n_lambda": float(n * lam), "cov_sign_ratio": float(Zn * Zef / Ze ** 2), "one_minus_ratio": nstr(1 - Zn * Zef / Ze ** 2, 8),
            "E_B_UV": float(UVt / Bt), "E_J_N": float(lam * UVt / Jt), "J_over_B": float(Jt / Bt)}


if __name__ == "__main__":
    n, q, nl = int(sys.argv[1]), sys.argv[2], sys.argv[3]
    print(json.dumps(run(n, q, mpf(nl) / n)))

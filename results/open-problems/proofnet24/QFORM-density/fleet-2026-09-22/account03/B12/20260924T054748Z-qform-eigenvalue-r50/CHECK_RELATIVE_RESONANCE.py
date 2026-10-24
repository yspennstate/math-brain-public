import numpy as np

SEED = 202609240550
TRIALS = 10000
rng = np.random.default_rng(SEED)

def sv(M):
    return np.linalg.svd(M, compute_uv=False)

full_violations = 0
rank_tail_violations = 0
minimum_all_j_margin = float("inf")
minimum_rank_tail_s5_margin = float("inf")

for _ in range(TRIALS):
    n = int(rng.integers(12, 23))
    m = int(rng.integers(5, min(12, n) + 1))

    M = rng.normal(size=(n, m))
    M[:m, :] += 2.0 * np.eye(m)
    g = sv(M)[-1]

    # Full theorem: arbitrary local action N.
    N = rng.normal(size=(n, m)) * np.exp(rng.uniform(-2.0, 2.0))
    G = M.T @ M
    K = np.linalg.solve(G, M.T @ N)
    L = np.eye(m) + K
    lhs = sv(M + N)
    rhs = g * sv(L)
    margin = float(np.min(lhs - rhs))
    minimum_all_j_margin = min(minimum_all_j_margin, margin)
    if margin < -1.0e-9:
        full_violations += 1

    # Rank-tail corollary: q <= m-5 arbitrary relative directions,
    # a small full-rank relative tail, and arbitrary transverse action.
    q = int(rng.integers(0, m - 4))
    if q:
        K0 = (
            rng.normal(size=(m, q))
            @ rng.normal(size=(q, m))
            * np.exp(rng.uniform(-2.0, 4.0))
        )
    else:
        K0 = np.zeros((m, m))

    eps = float(rng.uniform(0.0, 0.3))
    F = rng.normal(size=(m, m))
    fop = sv(F)[0]
    F *= eps / fop

    # Orthogonal codomain term of unrestricted size.
    Q, _ = np.linalg.qr(M)
    Z0 = rng.normal(size=(n, m)) * np.exp(rng.uniform(-2.0, 4.0))
    Z = Z0 - Q @ (Q.T @ Z0)

    N2 = M @ (K0 + F) + Z
    lhs5 = float(sv(M + N2)[4])
    rhs5 = float(g * (1.0 - eps))
    margin5 = lhs5 - rhs5
    minimum_rank_tail_s5_margin = min(minimum_rank_tail_s5_margin, margin5)
    if margin5 < -1.0e-8:
        rank_tail_violations += 1

print({
    "seed": SEED,
    "trials": TRIALS,
    "full_theorem_violations": full_violations,
    "minimum_all_j_margin": minimum_all_j_margin,
    "rank_tail_violations": rank_tail_violations,
    "minimum_rank_tail_s5_margin": minimum_rank_tail_s5_margin,
})

import json
import math
import numpy as np

SEED = 20260924074439
TRIALS = 10000
rng = np.random.default_rng(SEED)

spectrum_violations = 0
tail_violations = 0
minimum_spectrum_margin = float("inf")
minimum_tail_margin = float("inf")

for _ in range(TRIALS):
    n = int(rng.integers(8, 17))
    m = int(rng.integers(5, min(10, n + 1)))

    Z = rng.normal(size=(n, n))
    A0 = (Z + Z.T) / 2
    A0[:m, :m] += 3 * np.eye(m)
    M = A0[:, :m]
    g = np.linalg.svd(M, compute_uv=False)[-1]

    Z = rng.normal(size=(n, n))
    G = (Z + Z.T) / 2
    G *= float(np.exp(rng.uniform(-3, 3)))
    N = G[:, :m]

    U_M = np.linalg.qr(M, mode="reduced")[0]
    U_N, s_N, _ = np.linalg.svd(N, full_matrices=False)
    r_N = int(np.sum(s_N > 1e-10))
    if r_N:
        U_S = U_N[:, :r_N]
        c = np.linalg.svd(U_S.T @ U_M, compute_uv=False)
        c = np.r_[c, np.zeros(m - len(c))]
        c = np.sort(c)[::-1]
    else:
        c = np.zeros(m)

    sv = np.linalg.svd(M + N, compute_uv=False)
    for q in range(m):
        lhs = sv[m - q - 1]
        rhs = g * math.sqrt(max(0.0, 1.0 - c[q] ** 2))
        margin = lhs - rhs
        minimum_spectrum_margin = min(minimum_spectrum_margin, margin)
        if margin < -1e-9:
            spectrum_violations += 1

    Z = rng.normal(size=(n, n))
    T = (Z + Z.T) / 2
    T *= float(np.exp(rng.uniform(-4, -1)))
    eps = np.linalg.svd(T[:, :m], compute_uv=False)[0]
    sv_tail = np.linalg.svd(M + N + T[:, :m], compute_uv=False)
    for q in range(m):
        lhs = sv_tail[m - q - 1]
        rhs = max(g * math.sqrt(max(0.0, 1.0 - c[q] ** 2)) - eps, 0.0)
        margin = lhs - rhs
        minimum_tail_margin = min(minimum_tail_margin, margin)
        if margin < -1e-9:
            tail_violations += 1

results = {
    "seed": SEED,
    "trials": TRIALS,
    "spectrum_violations": spectrum_violations,
    "minimum_spectrum_margin": minimum_spectrum_margin,
    "tail_violations": tail_violations,
    "minimum_tail_margin": minimum_tail_margin,
    "status": "sanity_check_only_not_part_of_proof",
}
print(json.dumps(results, indent=2))

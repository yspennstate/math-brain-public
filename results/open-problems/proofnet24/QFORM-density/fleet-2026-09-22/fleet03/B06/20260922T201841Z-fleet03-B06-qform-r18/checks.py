import itertools
import json
import math
import numpy as np

RNG = np.random.default_rng(20260922)


def e2_singular(M):
    s = np.linalg.svd(M, compute_uv=False)
    lam = s * s
    return 0.5 * (lam.sum() ** 2 - (lam * lam).sum())


def e2_minors(M):
    total = 0.0
    for rows in itertools.combinations(range(M.shape[0]), 2):
        for cols in itertools.combinations(range(M.shape[1]), 2):
            total += np.linalg.det(M[np.ix_(rows, cols)]) ** 2
    return total


max_e2_rel = 0.0
min_transfer_ratio = float("inf")
transfer_count = 0

for _ in range(500):
    m = int(RNG.integers(3, 8))
    n = int(RNG.integers(3, 8))
    H = RNG.normal(size=(m, n))
    j = int(RNG.integers(0, m))
    H0 = np.delete(H, j, axis=0)

    E = e2_singular(H0)
    E_cb = e2_minors(H0)
    max_e2_rel = max(max_e2_rel, abs(E - E_cb) / max(E, E_cb, 1e-12))

    g = 10 ** RNG.uniform(-1, 1)
    M = g * g * np.eye(n) + H.T @ H
    vals, vecs = np.linalg.eigh(M)
    M_inv_half = vecs @ np.diag(vals ** -0.5) @ vecs.T
    Z = H @ M_inv_half
    Z0 = np.delete(Z, j, axis=0)
    Ez = e2_singular(Z0)
    if Ez > 1e-10:
        ratio = E / (g ** 4 * Ez)
        min_transfer_ratio = min(min_transfer_ratio, ratio)
        transfer_count += 1
        assert ratio >= 1 - 1e-8

q = 0.99
eta = 1 / 64
B = (
    math.e * eta ** (-1 / 4)
    + 2 ** (27 / 8) * math.e ** (13 / 16)
      * q ** (-3 / 16) * eta ** (-5 / 32)
)
C_A = 8 * 3 ** (-3 / 4)
C_near = 2 * math.sqrt(2) * C_A * math.sqrt(B)
s_min = 127 / 129
rank1_tail = 2 * eta / s_min

assert max_e2_rel < 1e-10
assert C_near < 72
assert rank1_tail == 129 / 4064

result = {
    "random_instances": 500,
    "max_e2_cauchy_binet_relative_error": max_e2_rel,
    "transfer_checks_with_positive_e2": transfer_count,
    "min_E_over_g4_Ez": min_transfer_ratio,
    "eta": eta,
    "q": q,
    "B_eta_q": B,
    "optimized_L3_to_Linf_Abel_constant": C_A,
    "near_coloop_branch_constant": C_near,
    "s_min": s_min,
    "rank1_tail_bound": rank1_tail,
    "rank1_tail_exact_fraction": "129/4064",
    "terminator": "QFORM_B06_R18_HYBRID_CHECK_PASS",
}

print(json.dumps(result, indent=2, sort_keys=True))

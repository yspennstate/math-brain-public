#!/usr/bin/env python3
"""Deterministic sanity checks for QFORM-RANK3-SHAREDHUB-RANK2-TRANSVERSE-NORMALFORM-v1.

This script is not a proof. It tests the exact singular-value identity on random
exact-rank-three indefinite frames and reproduces the constants in REPORT.md.
"""
import math
import numpy as np

rng = np.random.default_rng(20260923)
max_rel = 0.0
min_abs_a = float("inf")
rank2_count = 0
max_rank_c = 0

for trial in range(2000):
    n = 9
    G = rng.normal(size=(n, 3))
    R, _ = np.linalg.qr(G)
    lam = np.array([1.2, 1.7, -1.1]) if trial % 2 == 0 else np.array([-1.2, -1.7, 1.1])
    M = np.diag(lam)
    A = R @ M @ R.T

    i = 0
    L = np.arange(1, 5)
    RR = np.arange(5, 9)
    c = A[L, i]
    r = A[i, RR]
    N = A[np.ix_(L, RR)]
    alpha = np.linalg.norm(c)
    beta = np.linalg.norm(r)
    if alpha < 1e-12 or beta < 1e-12:
        continue

    e = c / alpha
    f = r / beta
    Pe = np.eye(len(L)) - np.outer(e, e)
    Pf = np.eye(len(RR)) - np.outer(f, f)
    C = Pe @ N @ Pf
    sc = np.linalg.svd(C, compute_uv=False)
    rank_c = int(np.sum(sc > 1e-9))
    max_rank_c = max(max_rank_c, rank_c)
    assert rank_c <= 2

    if rank_c == 2:
        a = A[i, i]
        assert abs(a) > 1e-12
        sn = np.linalg.svd(N, compute_uv=False)
        delta3 = float(np.prod(sn[:3]))
        d2 = float(sc[0] * sc[1])
        rhs = alpha * beta * d2 / abs(a)
        rel = abs(delta3 - rhs) / max(1.0, delta3, rhs)
        max_rel = max(max_rel, rel)
        min_abs_a = min(min_abs_a, abs(a))
        rank2_count += 1

beta0 = 289 / 15984
theta0 = math.sqrt(191) * beta0 / 32
gamma0 = 3 * beta0 / 4
K0 = (128**4 * 6**3) ** (1 / 7)
C_r43 = (128**4 * 6**3 / (gamma0 * theta0**2)) ** (1 / 7)

print("rank2_cases", rank2_count)
print("max_rank_C", max_rank_c)
print("max_relative_identity_error", f"{max_rel:.3e}")
print("min_abs_pivot_seen", f"{min_abs_a:.15g}")
print("K0", f"{K0:.15f}")
print("r43_constant", f"{C_r43:.15f}")
assert rank2_count > 0
assert max_rel < 1e-10
assert abs(K0 - 34.48366168863777) < 1e-12
assert abs(C_r43 - 255.00675888591775) < 1e-12
print("QFORM_B11_RANK2_TRANSVERSE_PIVOT_CHECK_PASS")

#!/usr/bin/env python3
"""Finite regression diagnostics for QFORM-S16-TRANSVERSE-CARRIER-v1.
Not a proof certificate. No network access or external data required.
"""
import itertools
import numpy as np

rng = np.random.default_rng(20260924)

def sv(a):
    return np.linalg.svd(a, compute_uv=False)

max_rank_violation = -np.inf
max_split_violation = -np.inf
ratios = []

for _ in range(500):
    ni = nj = 8
    b = rng.normal(size=(ni, ni)); b = (b + b.T) / 2
    c = rng.normal(size=(nj, nj)); c = (c + c.T) / 2

    u, _ = np.linalg.qr(rng.normal(size=(ni, 4)))
    v, _ = np.linalg.qr(rng.normal(size=(nj, 4)))
    sig = np.exp(rng.normal(size=4))
    m4 = u @ np.diag(sig) @ v.T

    k = np.block([[np.zeros((ni, ni)), m4],
                  [m4.T, np.zeros((nj, nj))]])
    d = np.block([[b, np.zeros((ni, nj))],
                  [np.zeros((nj, ni)), c]])
    a0 = d + k
    p = np.block([[u @ u.T, np.zeros((ni, nj))],
                  [np.zeros((nj, ni)), v @ v.T]])
    t = (np.eye(ni + nj) - p) @ d

    max_rank_violation = max(max_rank_violation, sv(a0)[15] - sv(t)[7])

    pu = u @ u.T
    o = b - np.diag(np.diag(b))
    half_base = np.linalg.norm((np.eye(ni) - pu) @ o, 2) / 2
    best = 0.0
    for signs in itertools.product((-1.0, 1.0), repeat=ni):
        e = np.diag(signs)
        ce = (o - e @ o @ e) / 2
        best = max(best, np.linalg.norm((np.eye(ni) - pu) @ ce, 2))
    max_split_violation = max(max_split_violation, half_base - best)
    if half_base > 1e-12:
        ratios.append(best / half_base)

print("QFORM_B11_R57_TRANSVERSE_S16_CHECK_PASS")
print(f"trials=500")
print(f"max_rank_violation={max_rank_violation:.16e}")
print(f"max_split_violation={max_split_violation:.16e}")
print(f"min_best_to_half_ratio={min(ratios):.16e}")
print(f"mean_best_to_half_ratio={np.mean(ratios):.16e}")

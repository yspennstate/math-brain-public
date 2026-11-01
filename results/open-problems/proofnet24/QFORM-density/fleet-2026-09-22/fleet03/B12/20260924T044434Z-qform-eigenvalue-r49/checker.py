#!/usr/bin/env python3
"""Deterministic consistency checks for QFORM-DYNAMIC-DESTRUCTIVE-BUDGET-v1."""
import json
import math
import numpy as np

SEED = 20260924
TRIALS = 10000

def svals(M):
    return np.linalg.svd(M, compute_uv=False)

def proj_range(M, tol=1e-12):
    U, s, _ = np.linalg.svd(M, full_matrices=False)
    r = int(np.sum(s > tol))
    if r == 0:
        return np.zeros((M.shape[0], M.shape[0]))
    U = U[:, :r]
    return U @ U.T

rng = np.random.default_rng(SEED)
violations = 0
minimum_full_margin = float("inf")
minimum_simple_margin = float("inf")

for _ in range(TRIALS):
    n, m = 12, 6
    M = rng.normal(size=(n, m))
    M[:m, :] += 2 * np.eye(m)
    Pi = proj_range(M)

    scale = float(np.exp(rng.uniform(-4, 4)))
    N = scale * rng.normal(size=(n, m))

    D = Pi @ N
    T = (np.eye(n) - Pi) @ N

    g = svals(M)[-1]
    delta = svals(D)[0]
    tau = svals(T)[-1]
    lhs = svals(M + N)[-1]

    rhs = math.sqrt(max(g - delta, 0.0) ** 2 + tau ** 2)
    simple_rhs = max(g - delta, 0.0)

    minimum_full_margin = min(minimum_full_margin, lhs - rhs)
    minimum_simple_margin = min(minimum_simple_margin, lhs - simple_rhs)

    if lhs + 1e-10 < rhs:
        violations += 1

# Partner-family carrier after the exact resonance:
# M_* e1=-2e1 and M_* ej=2e_(6+j), j=2,...,6.
n, m = 12, 6
M0 = np.zeros((n, m))
M0[0, 0] = -2
for j in range(1, 6):
    M0[6 + j, j] = 2
Pi0 = proj_range(M0)

packet = np.array([0.0, 1e6, -3e5, 7e4, -2e6, 9e5])
S = np.zeros((n, n))
for j in range(1, 6):
    S[j, j] = packet[j]

N = S[:, :m]
partner_destructive_norm = svals(Pi0 @ N)[0]
partner_smin = svals(M0 + N)[-1]

result = {
    "seed": SEED,
    "trials": TRIALS,
    "violations": violations,
    "minimum_full_pythagorean_margin": minimum_full_margin,
    "minimum_simple_destructive_budget_margin": minimum_simple_margin,
    "explicit_partner_family": {
        "destructive_projection_norm": partner_destructive_norm,
        "minimum_singular_value_after_huge_signed_packet": partner_smin,
        "packet_eigenvalues_on_e2_to_e6": packet[1:].tolist(),
    },
}

print(json.dumps(result, indent=2))

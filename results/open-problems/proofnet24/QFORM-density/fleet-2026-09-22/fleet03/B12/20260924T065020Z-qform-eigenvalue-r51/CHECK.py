#!/usr/bin/env python3
import json
import math
import numpy as np

SEED = 202609240651
TRIALS = 10000
rng = np.random.default_rng(SEED)


def orth(a):
    q, _ = np.linalg.qr(a)
    return q


violations = 0
min_angle_margin = float("inf")
min_rank_tail_margin = float("inf")
max_coherence_error = 0.0

for _ in range(TRIALS):
    n, m = 30, 11
    U = orth(rng.normal(size=(n, m)))[:, :m]
    V = orth(rng.normal(size=(m, m)))
    singulars = np.exp(rng.uniform(math.log(0.7), math.log(3.0), size=m))
    M = U @ np.diag(singulars) @ V.T
    g = np.linalg.svd(M, compute_uv=False)[-1]

    z = rng.normal(size=(n, 8))
    z = z - U @ (U.T @ z)
    S0 = orth(z)[:, :5]

    c = float(rng.uniform(0.0, 0.8))
    S = c * U[:, :5] + math.sqrt(1.0 - c * c) * S0
    c_actual = np.linalg.svd(U.T @ S, compute_uv=False)[0]
    max_coherence_error = max(max_coherence_error, abs(c_actual - c))

    N_good = S @ (rng.normal(size=(5, m)) * math.exp(rng.uniform(-2.0, 3.0)))
    smin_good = np.linalg.svd(M + N_good, compute_uv=False)[-1]
    rhs_good = g * math.sqrt(1.0 - c_actual * c_actual)
    min_angle_margin = min(min_angle_margin, smin_good - rhs_good)

    q = int(rng.integers(0, 7))
    if q:
        left = rng.normal(size=(n, q))
        right = rng.normal(size=(q, m)) * math.exp(rng.uniform(-2.0, 2.0))
        N_bad = left @ right
    else:
        N_bad = np.zeros((n, m))

    tail = rng.normal(size=(n, m))
    tail_norm = np.linalg.svd(tail, compute_uv=False)[0]
    epsilon = float(rng.uniform(0.0, 0.08))
    tail *= epsilon / tail_norm

    final = M + N_good + N_bad + tail
    s5 = np.linalg.svd(final, compute_uv=False)[4]
    rhs = max(rhs_good - epsilon, 0.0)
    margin = s5 - rhs
    min_rank_tail_margin = min(min_rank_tail_margin, margin)
    if margin < -1e-9:
        violations += 1

# Exact sharpness instance for the sine factor.
c = 0.6
g = 2.0
s = math.sqrt(1.0 - c * c)
M = np.array([[g], [0.0]])
w = np.array([[c], [s]])
N = -g * c * w
sharp_lhs = float(np.linalg.norm(M + N))
sharp_rhs = g * s

out = {
    "seed": SEED,
    "trials": TRIALS,
    "violations": violations,
    "minimum_angle_only_margin": float(min_angle_margin),
    "minimum_rank_tail_margin": float(min_rank_tail_margin),
    "max_constructed_coherence_error": float(max_coherence_error),
    "sharp_example": {
        "c": c,
        "g": g,
        "lhs": sharp_lhs,
        "rhs": sharp_rhs,
        "difference": sharp_lhs - sharp_rhs,
    },
    "note": "Finite floating-point checks only; analytic proof is in REPORT.md."
}
print(json.dumps(out, indent=2, sort_keys=True))

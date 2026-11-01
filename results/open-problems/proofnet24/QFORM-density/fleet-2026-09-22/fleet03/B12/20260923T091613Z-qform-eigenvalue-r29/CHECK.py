#!/usr/bin/env python3
"""Finite matrix sanity checks for QFORM spectral-window Schur shielding.

These checks verify only deterministic inequalities/constants appearing in REPORT.md.
They are not evidence for the full conjecture and do not replace the proof.
"""

import json
import math
import numpy as np

SEED = 20260923
TRIALS = 5000
rng = np.random.default_rng(SEED)


def ell(rho: float) -> float:
    return (math.sqrt(rho * rho + 4.0) - rho) / 2.0


violations = 0
min_margin = float("inf")
min_ratio = float("inf")
max_leakage_norm_error = 0.0

for _ in range(TRIALS):
    s = int(rng.integers(1, 5))
    p = int(rng.integers(3, 7))
    q = int(rng.integers(1, 6))

    mu = float(rng.uniform(0.5, 3.0))
    vals = mu + rng.uniform(0.0, 4.0, size=p)
    signs = rng.choice([-1.0, 1.0], size=p)
    Dp = np.diag(signs * vals)

    X = rng.normal(size=(q, q))
    Dq = (X + X.T) / 2.0
    Dq *= 10.0 ** float(rng.uniform(-2.0, 3.0))

    X = rng.normal(size=(s, s))
    C = (X + X.T) / 2.0
    C *= 10.0 ** float(rng.uniform(-2.0, 3.0))

    Bp = rng.normal(size=(s, p))
    Bq = rng.normal(size=(s, q))
    epsilon = float(rng.uniform(0.0, 0.4))
    nBq = np.linalg.norm(Bq, 2)
    if nBq > 0.0:
        Bq *= epsilon / nBq

    rho = float(np.linalg.norm(Bp @ np.linalg.inv(Dp), 2))
    protected_gap = ell(rho) ** 2 * mu

    H0 = np.block([
        [C, Bp, np.zeros((s, q))],
        [Bp.T, Dp, np.zeros((p, q))],
        [np.zeros((q, s)), np.zeros((q, p)), Dq],
    ])
    E = np.block([
        [np.zeros((s, s)), np.zeros((s, p)), Bq],
        [np.zeros((p, s)), np.zeros((p, p)), np.zeros((p, q))],
        [Bq.T, np.zeros((q, p)), np.zeros((q, q))],
    ])
    H = H0 + E

    leakage_norm = float(np.linalg.norm(E, 2))
    max_leakage_norm_error = max(max_leakage_norm_error, abs(leakage_norm - epsilon))

    svals = np.linalg.svd(H, compute_uv=False)
    s3 = float(svals[2])
    bound = protected_gap - epsilon
    margin = s3 - bound
    min_margin = min(min_margin, margin)
    if bound > 1e-12:
        min_ratio = min(min_ratio, s3 / bound)
    if margin < -2e-10:
        violations += 1

example_mu = 2.0
example_rho = 0.5
example_epsilon = 0.1
example_delta = 0.1
example_m = 7
example_gamma = example_mu * ell(example_rho) ** 2 - example_epsilon - example_delta
example_density_constant = 2.0 * math.sqrt(6.0 * math.pi * example_m) / example_gamma

result = {
    "seed": SEED,
    "trials": TRIALS,
    "violations": violations,
    "minimum_margin_s3_minus_bound": min_margin,
    "minimum_ratio_when_bound_positive": min_ratio,
    "max_abs_error_norm_symmetric_leakage_minus_Bq_norm": max_leakage_norm_error,
    "example_constants": {
        "mu": example_mu,
        "rho": example_rho,
        "ell_squared": ell(example_rho) ** 2,
        "leakage_epsilon": example_epsilon,
        "local_dense_delta": example_delta,
        "gamma": example_gamma,
        "m": example_m,
        "density_constant": example_density_constant,
    },
    "interpretation": "finite deterministic sanity check only; analytic theorem proved separately",
}

print(json.dumps(result, indent=2, sort_keys=True))
if violations:
    raise SystemExit(1)

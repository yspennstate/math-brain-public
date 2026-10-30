#!/usr/bin/env python3
"""Deterministic sanity checks for fleet03/B12 r46.

These checks are not proof evidence.  The report proves the inequalities
analytically by singular-value Weyl/interlacing.
"""
import math
import numpy as np


def svals(x):
    return np.linalg.svd(x, compute_uv=False)


def overlap_check(trials=10000, seed=2026092401):
    rng = np.random.default_rng(seed)
    m, n, q, k = 8, 16, 2, 6
    violations = 0
    margins = []
    for _ in range(trials):
        U, _ = np.linalg.qr(rng.normal(size=(m, m)))
        V, _ = np.linalg.qr(rng.normal(size=(n, m)))
        sig = np.sort(rng.uniform(1.0, 4.0, size=m))[::-1]
        M = (U * sig) @ V.T

        W, _ = np.linalg.qr(rng.normal(size=(m, q)))
        L = np.zeros((m, n))
        packet_count = int(rng.integers(2, 8))
        for _ in range(packet_count):
            L += W @ rng.normal(scale=50.0, size=(q, n))

        R = rng.normal(size=(m, n))
        eps = float(rng.uniform(0.0, 0.2))
        R *= eps / svals(R)[0]

        lhs = svals(M + L + R)[k - 1]
        rhs = max(0.0, svals(M)[k + q - 1] - svals(R)[0])
        margin = float(lhs - rhs)
        margins.append(margin)
        if margin < -1e-9:
            violations += 1
    return {
        "seed": seed,
        "trials": trials,
        "violations": violations,
        "minimum_margin": min(margins),
        "median_margin": float(np.median(margins)),
    }


def variational_check(trials=10000, seed=2026092402):
    rng = np.random.default_rng(seed)
    violations = 0
    minimum_margin = math.inf
    for _ in range(trials):
        m, n = 8, 14
        M = rng.normal(size=(m, n))
        N = rng.normal(size=(m, n))
        sm, sn, ss = svals(M), svals(N), svals(M + N)
        k = int(rng.integers(1, 7))
        q = int(rng.integers(0, m - k + 1))
        rhs = max(0.0, sm[k + q - 1] - sn[q])
        margin = float(ss[k - 1] - rhs)
        minimum_margin = min(minimum_margin, margin)
        if margin < -1e-9:
            violations += 1
    return {
        "seed": seed,
        "trials": trials,
        "violations": violations,
        "minimum_margin": minimum_margin,
    }


if __name__ == "__main__":
    print(overlap_check())
    print(variational_check())

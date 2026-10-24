#!/usr/bin/env python3
"""Finite consistency checks for QFORM-LOCAL-SHADOW-PROFILE-EXPORT-v1.

These tests are NOT proof of the universal QFORM conjecture. The analytic proof
is in REPORT.md. No simulation of output densities is performed.
"""

import json
import math
import statistics
import numpy as np

SEED = 20260923
TRIALS = 10_000
rng = np.random.default_rng(SEED)


def sym(n, scale=1.0):
    x = rng.normal(size=(n, n)) * scale
    return (x + x.T) / 2.0


def opnorm(a):
    return float(np.linalg.norm(a, 2))


def main():
    margins = []
    violations = 0
    n, m, k = 13, 9, 5

    for _ in range(TRIALS):
        a0 = sym(n, 0.4)
        r = int(rng.integers(1, 3))
        u, _ = np.linalg.qr(rng.normal(size=(n, r)))
        theta = rng.uniform(-100.0, 100.0, size=r)
        s = (u * theta) @ u.T

        local_shadow = np.concatenate([u, a0 @ u], axis=1)[:m, :]
        q = int(np.linalg.matrix_rank(local_shadow, tol=1e-10))
        assert k + q <= m

        e = sym(n, 1.0)
        epsilon = float(rng.uniform(0.0, 0.35))
        e *= epsilon / max(opnorm(e), 1e-12)
        a = a0 + s + e

        a0sq_h = (a0 @ a0)[:m, :m]
        eig = np.linalg.eigvalsh(a0sq_h)[::-1]
        g = max(math.sqrt(max(float(eig[k + q - 1]), 0.0)) - epsilon, 0.0)

        c = a[:m, :m]
        cross = a[:m, m:]
        sc = np.linalg.svd(c, compute_uv=False)
        sm = np.linalg.svd(cross, compute_uv=False)

        lhs = float(sc[2] ** 2 + sm[2] ** 2)
        rhs = g * g
        margin = lhs - rhs
        margins.append(margin)
        if margin < -1e-8:
            violations += 1

    k3 = 3.0 * 2.0 ** (4.0 / 3.0) * math.exp(1.0 / 3.0)
    partner_g = 7.0 / 4.0
    out = {
        "schema_version": 1,
        "seed": SEED,
        "trials": TRIALS,
        "violations": violations,
        "minimum_margin": min(margins),
        "median_margin": statistics.median(margins),
        "K3": k3,
        "partner_g": partner_g,
        "partner_E3_bound": math.sqrt(2.0) * k3 / partner_g,
        "partner_exact_rank8_crossing_bound": 16.0 / 21.0,
        "interpretation": "finite deterministic consistency checks only; analytic proof is in REPORT.md",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

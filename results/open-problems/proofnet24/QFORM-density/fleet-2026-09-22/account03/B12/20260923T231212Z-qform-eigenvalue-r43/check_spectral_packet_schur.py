#!/usr/bin/env python3
"""Finite consistency checks for QFORM-SPECTRAL-PACKET-SCHUR-BUDGET-v1.

These checks are not proof evidence. The theorem is proved analytically in REPORT.md.
"""
import json
import numpy as np


def schur(A, r):
    B = A[:r, :r]
    C = A[:r, r:]
    D = A[r:, r:]
    return D - C.T @ np.linalg.inv(B) @ C


def threshold_counts(M, t):
    w = np.linalg.eigvalsh(M)
    return int(np.sum(w >= t)), int(np.sum(w <= -t))


def main():
    rng = np.random.default_rng(43122026)
    violations = 0
    margins = []
    used = 0

    for _ in range(10000):
        n = int(rng.integers(7, 17))
        r = int(rng.integers(1, min(4, n - 2) + 1))
        q = int(rng.integers(0, min(4, n - r - 1) + 1))
        k = int(rng.integers(1, n - r - q + 1))

        X = rng.normal(size=(n, n))
        A0 = (X + X.T) / 2

        U, _ = np.linalg.qr(rng.normal(size=(n, n)))
        vals = rng.uniform(-0.5, 0.5, size=n)
        for h in range(q):
            vals[h] = rng.choice([-1.0, 1.0]) * 10 ** rng.uniform(0, 4)
        E = U @ np.diag(vals) @ U.T
        A = A0 + E

        B = A[:r, :r]
        if np.min(np.abs(np.linalg.eigvalsh(B))) < 1e-8:
            continue

        S = schur(A, r)
        delta = np.linalg.svd(E, compute_uv=False)[q]
        lhs = np.linalg.svd(S, compute_uv=False)[k - 1]
        rhs = np.linalg.svd(A0, compute_uv=False)[q + r + k - 1] - delta
        margin = float(lhs - rhs)
        margins.append(margin)
        used += 1
        if lhs + 1e-8 < rhs:
            violations += 1

    rng = np.random.default_rng(43122027)
    sign_violations = 0
    sign_used = 0
    min_sign_slack = 10**9

    for _ in range(5000):
        n = int(rng.integers(7, 16))
        r = int(rng.integers(1, min(4, n - 2) + 1))
        q = int(rng.integers(0, min(4, n - r - 1) + 1))

        X = rng.normal(size=(n, n))
        A0 = (X + X.T) / 2

        U, _ = np.linalg.qr(rng.normal(size=(n, n)))
        vals = rng.uniform(-0.3, 0.3, size=n)
        for h in range(q):
            vals[h] = rng.choice([-1.0, 1.0]) * 10 ** rng.uniform(0, 3)
        E = U @ np.diag(vals) @ U.T
        A = A0 + E

        B = A[:r, :r]
        if np.min(np.abs(np.linalg.eigvalsh(B))) < 1e-8:
            continue

        S = schur(A, r)
        delta = np.linalg.svd(E, compute_uv=False)[q]
        tau = float(delta + rng.uniform(0.05, 1.5))

        p0, n0 = threshold_counts(A0, tau)
        ps, ns = threshold_counts(S, tau - delta)
        reqp = max(0, p0 - q - r)
        reqn = max(0, n0 - q - r)
        slack = min(ps - reqp, ns - reqn)
        min_sign_slack = min(min_sign_slack, slack)
        sign_used += 1
        if ps < reqp or ns < reqn:
            sign_violations += 1

    result = {
        "seed_profile": 43122026,
        "profile_tests": used,
        "profile_violations": violations,
        "minimum_profile_margin": min(margins),
        "median_profile_margin": float(np.median(margins)),
        "seed_sign": 43122027,
        "sign_tests": sign_used,
        "sign_violations": sign_violations,
        "minimum_sign_integer_slack": int(min_sign_slack),
        "status": "finite consistency check only; analytic proof is in REPORT.md",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

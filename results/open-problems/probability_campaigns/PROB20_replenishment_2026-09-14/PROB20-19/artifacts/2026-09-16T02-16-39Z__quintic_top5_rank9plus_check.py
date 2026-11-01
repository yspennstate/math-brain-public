#!/usr/bin/env python3
"""Reproducible self-checks for PROB20-19 quintic top-five rank>=9 proof.

This checks algebraic identities and runs a deterministic randomized sanity bank.
It is not independent verification and does not replace the analytic proof in
runs/2026-09-16/2026-09-16T02-13-54Z__report.md.
"""

import math
import numpy as np
import sympy as sp


def symbolic_checks():
    r = sp.symbols("r", positive=True, integer=True)
    S2, S3, S4, S5, A, B, L, M = sp.symbols("S2 S3 S4 S5 A B L M")
    T5 = r * (r + 2) * (r + 4) * (r + 6) * (r + 8)

    # Exact occupancy numerator from the spherical power-sum expansion.
    N = sp.expand(
        T5
        - 135 * (r + 8) * S2**2
        + 1350 * S2 * S3
        - 150 * (r + 6) * (r + 8) * S3
        + 1710 * (r + 8) * S4
        - 7020 * S5
        - 2160 * (r + 8) * A
        - 720 * (r + 8) * B
        + 16200 * L
        + 10800 * M
    )
    Ncoord = sp.factor(N.subs({S2: r, S3: r, S4: r, S5: r, A: 0, B: 0, L: 0, M: 0}))
    assert sp.expand(Ncoord - r * (r - 1) * (r - 2) * (r - 3) * (r + 26)) == 0

    # Lower bound after B<=A<= (S2-S3)/2 and dropping positive L,M.
    Nlb = sp.expand(
        T5
        - 135 * (r + 8) * S2**2
        - 1440 * (r + 8) * (S2 - S3)
        + 1350 * S2 * S3
        - 150 * (r + 6) * (r + 8) * S3
        + 1710 * (r + 8) * S4
        - 7020 * S5
    )

    D2, D3, D4, D5 = sp.symbols("D2 D3 D4 D5")
    gap = sp.expand(
        (Nlb - Ncoord).subs({S2: r - D2, S3: r - D3, S4: r - D4, S5: r - D5}) / 15
    )
    G_expected = sp.expand(
        -9 * (r + 8) * D2**2
        + 90 * D2 * D3
        + (18 * r**2 + 150 * r + 768) * D2
        + (10 * r**2 - 46 * r - 288) * D3
        - (114 * r + 912) * D4
        + 468 * D5
    )
    assert sp.expand(gap - G_expected) == 0

    W, mu, nu, xi = sp.symbols("W mu nu xi")
    normalized = sp.expand(
        G_expected.subs(
            {
                D2: W,
                D3: W * (1 + mu),
                D4: W * (1 + mu + nu),
                D5: W * (1 + mu + nu + xi),
            }
        )
        / W
    )
    normalized_expected = sp.expand(
        28 * r**2
        - 10 * r
        + 36
        + W * (90 * mu - 9 * r + 18)
        + mu * (10 * r**2 - 160 * r - 732)
        - (114 * r + 444) * nu
        + 468 * xi
    )
    assert sp.expand(normalized - normalized_expected) == 0

    # Integer-hypersimplex cumulant pair-merging factorization.
    a, b, R = sp.symbols("a b R", nonnegative=True)
    w = lambda z: z * (1 - z)
    k = lambda z: z * (1 - z) * (1 - 2 * z)
    F_before = k(a) + k(b) + (R + w(a) + w(b)) ** 2
    F_after = k(a + b) + (R + w(a + b)) ** 2
    merge_expected = 2 * a * b * (
        2 * R + 3 - (a + b) - 2 * (a + b) ** 2 + 2 * a * b
    )
    assert sp.expand(F_before - F_after - merge_expected) == 0

    # Pointwise weighted-moment lower bound used for r>=5.
    x = sp.symbols("x")
    pointwise = sp.factor(
        468 * x**3 - (114 * r + 444) * x**2 - (24 - 114 * r) * x
    )
    assert sp.expand(pointwise - 6 * x * (1 - x) * (19 * r - 78 * x - 4)) == 0

    # Borderline r=9 polynomial.
    J9 = sp.expand(2214 - 2364 * mu + (90 * mu - 63) * (2 * mu - 1))
    assert sp.expand(J9 - 3 * (60 * mu**2 - 860 * mu + 759)) == 0
    assert sp.simplify(J9.subs(mu, sp.Rational(10, 11)) - sp.Rational(9717, 121)) == 0

    return {
        "coordinate_numerator": str(Ncoord),
        "r9_endpoint": str(sp.Rational(9717, 121)),
    }


def projection_invariants(P):
    d = np.diag(P).copy()
    p = len(d)
    S = {k: float(np.sum(d**k)) for k in range(2, 6)}
    A = B = L = M = 0.0
    for i in range(p):
        for j in range(i + 1, p):
            q = float(P[i, j] ** 2)
            A += d[i] * d[j] * q
            B += q * q
            L += d[i] * d[j] * (d[i] + d[j]) * q
            M += (d[i] + d[j]) * q * q
    return d, S, A, B, L, M


def numerator(r, S, A, B, L, M):
    T5 = r * (r + 2) * (r + 4) * (r + 6) * (r + 8)
    return (
        T5
        - 135 * (r + 8) * S[2] ** 2
        + 1350 * S[2] * S[3]
        - 150 * (r + 6) * (r + 8) * S[3]
        + 1710 * (r + 8) * S[4]
        - 7020 * S[5]
        - 2160 * (r + 8) * A
        - 720 * (r + 8) * B
        + 16200 * L
        + 10800 * M
    )


def coordinate_numerator(r):
    return r * (r - 1) * (r - 2) * (r - 3) * (r + 26)


def diagonal_G(r, d):
    S = {k: float(np.sum(d**k)) for k in range(2, 6)}
    D = {k: r - S[k] for k in range(2, 6)}
    return (
        -9 * (r + 8) * D[2] ** 2
        + 90 * D[2] * D[3]
        + (18 * r**2 + 150 * r + 768) * D[2]
        + (10 * r**2 - 46 * r - 288) * D[3]
        - (114 * r + 912) * D[4]
        + 468 * D[5]
    )


def sample_capped(integer_sum, n, rng, steps=50):
    x = np.zeros(n, dtype=float)
    x[:integer_sum] = 1.0
    for _ in range(steps):
        i, j = rng.choice(n, size=2, replace=False)
        s = x[i] + x[j]
        lo = max(0.0, s - 1.0)
        hi = min(1.0, s)
        t = rng.uniform(lo, hi)
        x[i] = t
        x[j] = s - t
    return x


def randomized_checks():
    rng = np.random.default_rng(20260916)

    # Check the new cumulant inequality on an arbitrary capped-simplex bank.
    min_cumulant_slack = math.inf
    capped_cases = 0
    for r in range(1, 13):
        for n in range(r + 1, r + 7):
            for _ in range(80):
                x = sample_capped(r, n, rng)
                W = float(np.sum(x * (1 - x)))
                K = float(np.sum(x * (1 - x) * (1 - 2 * x)))
                min_cumulant_slack = min(min_cumulant_slack, K + W * W)
                assert K + W * W >= -2e-10
                capped_cases += 1

    # Projection bank. Ranks 4..8 are included deliberately to document that
    # the exact facet remains positive in this bank even when the diagonal
    # relaxation G can be negative; this is evidence, not proof for those ranks.
    min_exact_gap = {}
    min_diagonal_G = {}
    projection_cases = 0
    for r in range(4, 13):
        exact_min = math.inf
        g_min = math.inf
        for p in range(r + 1, r + 7):
            for _ in range(80):
                X = rng.normal(size=(p, r))
                Q, _ = np.linalg.qr(X, mode="reduced")
                P = Q @ Q.T
                d, S, A, B, L, M = projection_invariants(P)

                # Projection identities and elementary bounds used analytically.
                row_resid = np.max(np.abs(np.sum(P * P, axis=1) - d))
                assert row_resid < 2e-10
                assert B <= A + 2e-10
                assert A <= 0.5 * (S[2] - S[3]) + 2e-10

                exact_gap = numerator(r, S, A, B, L, M) - coordinate_numerator(r)
                g = diagonal_G(r, d)
                exact_min = min(exact_min, exact_gap)
                g_min = min(g_min, g)

                # The theorem proved in the report.
                if r >= 9:
                    assert g > -2e-8
                    assert exact_gap > -2e-8

                projection_cases += 1

        min_exact_gap[r] = exact_min
        min_diagonal_G[r] = g_min

    return {
        "capped_cases": capped_cases,
        "min_cumulant_slack": min_cumulant_slack,
        "projection_cases": projection_cases,
        "min_exact_gap_by_rank": min_exact_gap,
        "min_diagonal_G_by_rank": min_diagonal_G,
    }


if __name__ == "__main__":
    sym = symbolic_checks()
    rnd = randomized_checks()
    print("symbolic checks: PASS")
    print("coordinate numerator:", sym["coordinate_numerator"])
    print("r=9 endpoint lower bound:", sym["r9_endpoint"])
    print("capped-simplex cases:", rnd["capped_cases"])
    print("minimum cumulant slack K+W^2:", f"{rnd['min_cumulant_slack']:.12g}")
    print("projection cases:", rnd["projection_cases"])
    print("minimum exact K5>=4 numerator gap by rank:")
    for r, value in rnd["min_exact_gap_by_rank"].items():
        print(f"  r={r}: {value:.12g}")
    print("minimum diagonal relaxation G_r by rank:")
    for r, value in rnd["min_diagonal_G_by_rank"].items():
        print(f"  r={r}: {value:.12g}")

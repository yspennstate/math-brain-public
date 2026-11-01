"""PROB20-19 quartic projection-moment checker.

Reproduces the algebra in runs/2026-09-15/2026-09-15T14-32-40Z__report.md.

Checks:
  1. the exact quartic weight formulas W_4,W_31,W_22,W_211,W_1111;
  2. the exact positive-contrast gap decomposition;
  3. brute-force ordered-index enumeration on random projections;
  4. the elementary large-r coefficient lower bounds used for r>=9.

This is a reproducible algebra/numerics check, not an independent proof review.
Requires numpy and sympy.
"""
from __future__ import annotations

import collections
import itertools
import numpy as np
import sympy as sp


def symbolic_check() -> None:
    r, S2, S3, S4, U, T4 = sp.symbols("r S2 S3 S4 U T4")

    W4 = S4
    W31 = 4 * (r + 6) * S3 - 28 * S4
    W22 = 3 * (S2**2 - S4) + 48 * U + 16 * T4
    W211 = (
        -18 * S2**2
        + 6 * r**2 * S2
        + 60 * r * S2
        + 144 * S2
        - 60 * r * S3
        - 360 * S3
        + 228 * S4
        - 288 * U
        - 96 * T4
    )
    W1111 = (
        r**4
        + 12 * r**3
        + 44 * r**2
        + 48 * r
        - 18 * r**2 * S2
        - 180 * r * S2
        - 432 * S2
        + 27 * S2**2
        + 120 * r * S3
        + 720 * S3
        - 342 * S4
        + 432 * U
        + 144 * T4
    )

    # Coordinate projection weights for exponent partitions of 4.
    coord = sp.Matrix(
        [
            r,
            4 * r * (r - 1),
            3 * r * (r - 1),
            6 * r * (r - 1) * (r - 2),
            r * (r - 1) * (r - 2) * (r - 3),
        ]
    )
    weights = sp.Matrix([W4, W31, W22, W211, W1111])
    gap = sp.expand(coord - weights)

    # Moment-contrast basis:
    # I1=D-3E, I2=C-3D, I3=B-5D, I4=A-4B-5C.
    I1 = sp.Matrix([0, 0, 0, 1, -3])
    I2 = sp.Matrix([0, 0, 1, -3, 0])
    I3 = sp.Matrix([0, 1, 0, -5, 0])
    I4 = sp.Matrix([1, -4, -5, 0, 0])

    D2 = r - S2
    D3 = r - S3
    D4 = r - S4
    V = T4 + 3 * U
    lam4 = D4
    lam3 = 4 * (r**2 - (r + 6) * S3 + 6 * S4)
    lam2 = 3 * (r**2 - S2**2) + 2 * D4 - 16 * V
    lam1 = (
        6 * (r + 4) * (r + 6) * D2
        - 40 * (r + 6) * D3
        + 114 * D4
        - 9 * (r**2 - S2**2)
        + 48 * V
    )

    reconstructed = sp.expand(lam1 * I1 + lam2 * I2 + lam3 * I3 + lam4 * I4)
    assert all(sp.simplify(gap[i] - reconstructed[i]) == 0 for i in range(5))

    # Wick/constant-objective vector must annihilate the orientation gap.
    gaussian_ratios = sp.Matrix([105, 15, 9, 3, 1])
    assert sp.simplify(gap.dot(gaussian_ratios)) == 0

    # Exact factorization used for lambda_3.
    x = sp.symbols("x")
    assert sp.factor(r * x - (r + 6) * x**3 + 6 * x**4) == x * (1 - x) * (
        r * (1 + x) - 6 * x**2
    )

    # Large-r lambda_1 lower-bound polynomial is positive from r=9 onward.
    lower_poly = 6 * r**2 - 38 * r - 108
    assert int(lower_poly.subs(r, 8)) < 0
    assert int(lower_poly.subs(r, 9)) > 0

    print("symbolic quartic gap/decomposition checks: PASS")


def random_projection(p: int, r: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    q, _ = np.linalg.qr(rng.normal(size=(p, r)))
    return q @ q.T


def brute_quartic_weights(P: np.ndarray) -> dict[tuple[int, ...], float]:
    """Enumerate all ordered products in (theta^T P theta)^4 and sign-average.

    Intended only for small p (4 or 5) as a verification routine.
    """
    p = P.shape[0]
    pairs = [(i, j, P[i, j]) for i in range(p) for j in range(p)]
    out: dict[tuple[int, ...], float] = collections.defaultdict(float)
    for terms in itertools.product(pairs, repeat=4):
        coeff = 1.0
        degree = [0] * p
        for i, j, value in terms:
            coeff *= value
            degree[i] += 1
            degree[j] += 1
        if any(k % 2 for k in degree):
            continue
        partition = tuple(sorted((k // 2 for k in degree if k), reverse=True))
        out[partition] += coeff
    return out


def formula_quartic_weights(P: np.ndarray) -> dict[tuple[int, ...], float]:
    r = int(round(np.trace(P)))
    d = np.diag(P)
    S2 = float(np.sum(d**2))
    S3 = float(np.sum(d**3))
    S4 = float(np.sum(d**4))
    U = sum(
        d[i] * d[j] * P[i, j] ** 2
        for i in range(len(d))
        for j in range(i + 1, len(d))
    )
    T4 = sum(
        P[i, j] ** 4
        for i in range(len(d))
        for j in range(i + 1, len(d))
    )
    return {
        (4,): S4,
        (3, 1): 4 * (r + 6) * S3 - 28 * S4,
        (2, 2): 3 * (S2**2 - S4) + 48 * U + 16 * T4,
        (2, 1, 1): (
            -18 * S2**2
            + 6 * r**2 * S2
            + 60 * r * S2
            + 144 * S2
            - 60 * r * S3
            - 360 * S3
            + 228 * S4
            - 288 * U
            - 96 * T4
        ),
        (1, 1, 1, 1): (
            r**4
            + 12 * r**3
            + 44 * r**2
            + 48 * r
            - 18 * r**2 * S2
            - 180 * r * S2
            - 432 * S2
            + 27 * S2**2
            + 120 * r * S3
            + 720 * S3
            - 342 * S4
            + 432 * U
            + 144 * T4
        ),
    }


def numeric_check() -> None:
    for p, r, seed in [(4, 2, 4202), (5, 2, 5202), (5, 3, 5303)]:
        P = random_projection(p, r, seed)
        brute = brute_quartic_weights(P)
        formula = formula_quartic_weights(P)
        errors = {part: abs(brute[part] - value) for part, value in formula.items()}
        worst = max(errors.values())
        print(f"(p,r)=({p},{r}) worst brute/formula error: {worst:.3e}")
        assert worst < 1e-9
    print("brute-force quartic weight checks: PASS")


if __name__ == "__main__":
    symbolic_check()
    numeric_check()

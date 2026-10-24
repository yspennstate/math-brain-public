"""PROB20-19 checker for the strengthened quartic projection bounds.

Checks performed:
1. symbolic identities in the rank-two lambda_3 merging proof;
2. random orthogonal projections for the sharpened U and V bounds;
3. the W,mu,nu lower bounds proving lambda_2>=0 for r>=3;
4. the compression-trace lower bound used for lambda_1;
5. the explicit lambda_1 lower bound for r>=5.

This is reproducible self-checking, not independent verification of the
Mallat-Zeitouni conjecture.

Requires numpy and sympy.
"""
from __future__ import annotations

import numpy as np
import sympy as sp


def random_projection(p: int, r: int, rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(p, r)))
    return q @ q.T


def invariants(P: np.ndarray) -> dict[str, float | np.ndarray]:
    r = int(round(float(np.trace(P))))
    d = np.diag(P)
    s2 = float(np.sum(d**2))
    s3 = float(np.sum(d**3))
    s4 = float(np.sum(d**4))
    u = sum(
        d[i] * d[j] * P[i, j] ** 2
        for i in range(len(d))
        for j in range(i + 1, len(d))
    )
    t4 = sum(
        P[i, j] ** 4
        for i in range(len(d))
        for j in range(i + 1, len(d))
    )
    v = t4 + 3.0 * u
    W = r - s2
    mu = (s2 - s3) / W if W > 1e-13 else 0.0
    nu = (s3 - s4) / W if W > 1e-13 else 0.0

    lam4 = r - s4
    lam3 = 4.0 * ((r + 6) * (r - s3) - 6 * (r - s4))
    lam2 = 3.0 * (r * r - s2 * s2) + 2.0 * (r - s4) - 16.0 * v
    lam1 = (
        6.0 * (r + 4) * (r + 6) * (r - s2)
        - 40.0 * (r + 6) * (r - s3)
        + 114.0 * (r - s4)
        - 9.0 * (r * r - s2 * s2)
        + 48.0 * v
    )
    return {
        "r": r,
        "d": d,
        "S2": s2,
        "S3": s3,
        "S4": s4,
        "U": u,
        "T4": t4,
        "V": v,
        "W": W,
        "mu": mu,
        "nu": nu,
        "lambda1": lam1,
        "lambda2": lam2,
        "lambda3": lam3,
        "lambda4": lam4,
    }


def symbolic_rank_two_check() -> None:
    a, b, x, y, z = sp.symbols("a b x y z", nonnegative=True)

    def h(t):
        return t - 4 * t**3 + 3 * t**4

    # Merge identity used when a+b <= 1.
    lhs = sp.factor(h(a) + h(b) - h(a + b))
    rhs = -6 * a * b * (2 * (a + b) ** 2 - a * b - 2 * (a + b))
    assert sp.expand(lhs - rhs) == 0

    # Terminal three-coordinate identity after a=1-x, b=1-y, c=1-z,
    # x+y+z=1.
    terminal = sp.expand((h(1 - x) + h(1 - y) + h(1 - z)).subs(z, 1 - x - y))
    zsub = 1 - x - y
    e2 = x * y + y * zsub + zsub * x
    e3 = x * y * zsub
    assert sp.expand(terminal - 6 * (e2**2 - 2 * e3)) == 0
    print("rank-two symbolic identities: PASS")


def randomized_projection_checks(seed: int = 2019) -> None:
    rng = np.random.default_rng(seed)
    tol = 2e-9

    for r in range(2, 9):
        for p in range(r + 1, r + 6):
            for _ in range(300):
                P = random_projection(p, r, rng)
                I = invariants(P)
                d = I["d"]
                s2, s3, s4 = I["S2"], I["S3"], I["S4"]
                W, mu, nu = I["W"], I["mu"], I["nu"]

                # Projection row identity.
                for i in range(p):
                    row_off = sum(P[i, j] ** 2 for j in range(p) if j != i)
                    assert abs(row_off - d[i] * (1 - d[i])) < 2e-8

                # Improved upper bound U <= (S3-S4)/2.
                assert I["U"] <= 0.5 * (s3 - s4) + tol

                # Two-branch V bound.
                H = (r - s2) / 2.0 - (s2 - s3)
                v_upper = 2.0 * (s3 - s4) + min(0.0, H)
                assert I["V"] <= v_upper + 2e-8

                # Compression-trace lower bound.
                u_lower = 0.5 * (s2 * s2 / r - s4)
                assert I["U"] + 2e-8 >= u_lower

                if W > 1e-12:
                    # Weighted Cauchy constraints.
                    assert 0.0 <= nu <= mu + 2e-8
                    assert W <= r * (1.0 - mu) + 2e-8
                    assert nu + 2e-8 >= mu * mu

                if r >= 3 and W > 1e-12:
                    if mu <= 0.5:
                        lower2 = W * (-3 * W + 2 * mu - 30 * nu + 6 * r + 2)
                    else:
                        lower2 = 3 * W * (-W + 6 * mu - 10 * nu + 2 * r - 2)
                    assert I["lambda2"] + 2e-8 >= lower2
                    assert lower2 >= -2e-8

                if r >= 5 and W > 1e-12:
                    lower1 = W * (
                        6 * r * r + 2 * r - 54
                        + (9 + 72 / r) * W
                        - (40 * r + 54) * mu
                        + 186 * nu
                    )
                    assert I["lambda1"] + 2e-8 >= lower1
                    assert lower1 >= -2e-8

                if r == 2:
                    assert I["lambda3"] >= -2e-8
                if r >= 5:
                    assert min(
                        I["lambda1"], I["lambda2"], I["lambda3"], I["lambda4"]
                    ) >= -2e-8

    print("randomized projection inequalities: PASS")


def threshold_check() -> None:
    r = sp.symbols("r", real=True)
    numerator = 716 * r**2 - 708 * r - 10773
    assert numerator.subs(r, 5) == 3587
    # Derivative is positive for every r>=5.
    assert sp.diff(numerator, r).subs(r, 5) > 0
    print("lambda1 r>=5 threshold algebra: PASS")


if __name__ == "__main__":
    symbolic_rank_two_check()
    threshold_check()
    randomized_projection_checks()

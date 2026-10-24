"""Reproducible algebraic checks for the rank-three M4 closure in PROB20-19.

This checker verifies:
  1. the exact edge representation of lambda_1 at rank 3;
  2. the two scalar minima used in the high/low mixing bounds;
  3. randomized projection checks of the exact identity and both lower bounds.

It is a self-checking algebra/numerics artifact, not independent verification of the
Gaussian-PCA conjecture.

Requires: numpy, sympy.
"""
from __future__ import annotations

import numpy as np
import sympy as sp


def symbolic_checks() -> None:
    a, b, W = sp.symbols("a b W", real=True)
    s = a + b
    t = a * b
    wp = a * (1 - a) + b * (1 - b)

    c = 156 - 246 * s + 114 * (a**2 + b**2) + 144 * t

    # Global minimum of c: positive-definite Hessian, unique critical point.
    sol = sp.solve([sp.diff(c, a), sp.diff(c, b)], [a, b], dict=True)
    assert sol == [{a: sp.Rational(41, 62), b: sp.Rational(41, 62)}]
    assert sp.simplify(c.subs(sol[0]) + sp.Rational(207, 31)) == 0

    # Pair-variance rewrite.
    rewritten = 156 - 204 * s + 72 * s**2 - 42 * wp
    assert sp.expand(c - rewritten) == 0

    # Scalar quadratic minimum is 23/2 at s=17/12.
    ss = sp.symbols("ss", real=True)
    quad = 156 - 204 * ss + 72 * ss**2
    critical_s = sp.solve(sp.diff(quad, ss), ss)
    assert critical_s == [sp.Rational(17, 12)]
    assert sp.simplify(quad.subs(ss, critical_s[0]) - sp.Rational(23, 2)) == 0

    # Thresholds overlap.
    assert sp.Rational(23, 62) < sp.Rational(23, 48)

    # High-mixing lower bound from Q=W/2.
    Q = W / 2
    high = -sp.Rational(207, 31) * Q + 36 * Q**2
    assert sp.factor(high - W * (9 * W - sp.Rational(207, 62))) == 0

    # Low-mixing lower bound after R <= W^2/2.
    low = sp.Rational(23, 4) * W - 42 * (W**2 / 2) + 9 * W**2
    assert sp.factor(low - W * (sp.Rational(23, 4) - 12 * W)) == 0

    print("symbolic checks: PASS")


def random_projection(p: int, r: int, rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(p, r)))
    return q @ q.T


def lambda1_original(P: np.ndarray) -> float:
    d = np.diag(P)
    r = 3.0
    S2 = np.sum(d**2)
    S3 = np.sum(d**3)
    S4 = np.sum(d**4)
    D2 = r - S2
    D3 = r - S3
    D4 = r - S4
    E = 0.0
    U = 0.0
    p = len(d)
    for i in range(p):
        for j in range(i + 1, p):
            qij = P[i, j] ** 2
            E += qij**2
            U += d[i] * d[j] * qij
    V = E + 3 * U
    return 378 * D2 - 360 * D3 + 114 * D4 - 9 * (9 - S2**2) + 48 * V


def lambda1_edge(P: np.ndarray) -> tuple[float, float, float]:
    d = np.diag(P)
    p = len(d)
    Q = 0.0
    E = 0.0
    edge_sum = 0.0
    for i in range(p):
        for j in range(i + 1, p):
            qij = P[i, j] ** 2
            a, b = d[i], d[j]
            c = 156 - 246 * (a + b) + 114 * (a * a + b * b) + 144 * a * b
            edge_sum += qij * c
            Q += qij
            E += qij**2
    return edge_sum + 36 * Q**2 + 48 * E, Q, E


def randomized_checks(seed: int = 20260915, trials: int = 2000) -> None:
    rng = np.random.default_rng(seed)
    min_lambda = float("inf")
    for p in range(4, 13):
        for _ in range(trials):
            P = random_projection(p, 3, rng)
            lam = lambda1_original(P)
            edge, Q, E = lambda1_edge(P)
            assert np.allclose(P @ P, P, atol=1e-10)
            assert abs(lam - edge) < 1e-8

            d = np.diag(P)
            w = d * (1 - d)
            W = np.sum(w)
            R = np.sum(w**2)
            assert abs(W - 2 * Q) < 1e-9
            assert R <= W**2 / 2 + 1e-9

            high = W * (9 * W - 207 / 62)
            low = W * (23 / 4 - 12 * W) + 48 * E

            if W >= 23 / 62 - 1e-12:
                assert lam + 1e-8 >= high
            if W <= 23 / 48 + 1e-12:
                assert lam + 1e-8 >= low

            # The two validity intervals cover every positive W.
            assert (W <= 23 / 48 + 1e-12) or (W >= 23 / 62 - 1e-12)
            min_lambda = min(min_lambda, lam)

    print(f"randomized rank-three checks: PASS; smallest sampled lambda_1={min_lambda:.12g}")


if __name__ == "__main__":
    symbolic_checks()
    randomized_checks()

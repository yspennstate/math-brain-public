"""Diagnostics for PROB20-19 report 2026-09-15T16-42-26Z.

Checks the algebra used to close rank-four lambda_1:
  * nu = mu - Q/W;
  * the small-W third-cumulant bound |K| <= W^2 on random integer-sum
    hypersimplex samples in the regime W < 1/2;
  * max_i w_i <= W/2 and Q <= W^2/2;
  * the two rank-four lower-bound regimes;
  * direct lambda_1 >= 0 on random rank-four projections.

These are reproducible diagnostics, not a formal or independent proof.
Requires numpy and sympy.
"""
from __future__ import annotations

from fractions import Fraction
import numpy as np
import sympy as sp


def symbolic_checks() -> None:
    W, mu, q = sp.symbols("W mu q", positive=True, real=True)
    nu = mu - q
    rank4 = sp.expand(50 + 27 * W - 214 * mu + 186 * nu)
    assert sp.expand(rank4 - (50 + 27 * W - 28 * mu - 186 * q)) == 0

    x = sp.symbols("x", real=True)
    c = 28 * x + 186 * x * (1 - x)
    xc = sp.Rational(107, 186)
    assert sp.diff(c, x).subs(x, xc) == 0
    assert sp.simplify(c.subs(x, xc) - sp.Rational(11449, 186)) == 0

    margin = sp.Rational(50) + 27 * sp.Rational(9, 20) - sp.Rational(11449, 186)
    assert margin == sp.Rational(1109, 1860)

    A, qb, qa = sp.symbols("A qb qa", positive=True, real=True)
    upper_K = 3 * qb - 2 * qb**2 / A - (3 - 2 * A) * qa
    D = sp.expand((2 * A - qb - qa) ** 2 - upper_K)
    dD_dqa = sp.diff(D, qa)
    assert sp.expand(dD_dqa - (2 * qa + 3 + 2 * qb - 6 * A)) == 0

    t = sp.symbols("t", nonnegative=True, real=True)
    D0 = sp.factor(D.subs({qa: 0, qb: A**2 * t}) / A**2)
    expected = 4 - (3 + 4 * A) * t + (A**2 + 2 * A) * t**2
    assert sp.expand(D0 - expected) == 0
    assert sp.expand(expected.subs(t, 1) - (1 - A) ** 2) == 0

    print("symbolic identities: PASS")
    print("large-W overlap margin:", margin)


def project_to_capped_simplex(v: np.ndarray, total: int, steps: int = 80) -> np.ndarray:
    """Euclidean projection form clip(v-lambda,0,1) with specified sum."""
    lo = float(np.min(v) - 2.0)
    hi = float(np.max(v) + 2.0)
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        s = np.clip(v - mid, 0.0, 1.0).sum()
        if s > total:
            lo = mid
        else:
            hi = mid
    return np.clip(v - 0.5 * (lo + hi), 0.0, 1.0)


def diagonal_stats(d: np.ndarray) -> tuple[float, float, float, float, float, float]:
    w = d * (1.0 - d)
    W = float(w.sum())
    if W == 0.0:
        return W, 0.5, 0.0, 0.0, 0.0, 0.0
    mu = float(np.dot(w, d) / W)
    nu = float(np.dot(w, d * d) / W)
    Q = float(np.dot(w, w))
    q = Q / W
    K = float(np.dot(w, 1.0 - 2.0 * d))
    return W, mu, nu, Q, q, K


def random_hypersimplex_checks(seed: int = 19019, trials: int = 30000) -> None:
    rng = np.random.default_rng(seed)
    smallest_rank4_bracket = float("inf")
    checked_small = 0
    for _ in range(trials):
        p = int(rng.integers(5, 14))
        d = project_to_capped_simplex(rng.normal(size=p), 4)
        W, mu, nu, Q, q, K = diagonal_stats(d)
        if W <= 1e-12:
            continue

        assert abs((mu - nu) - q) < 2e-10
        assert np.max(d * (1.0 - d)) <= W / 2.0 + 2e-10
        assert Q <= W * W / 2.0 + 2e-10

        if W < 0.5 - 1e-10:
            checked_small += 1
            assert abs(K) <= W * W + 5e-9

        bracket = 50.0 + 27.0 * W - 28.0 * mu - 186.0 * q
        smallest_rank4_bracket = min(smallest_rank4_bracket, bracket)
        if W <= 9.0 / 20.0 + 1e-12:
            assert bracket >= 36.0 - 80.0 * W - 2e-8
        else:
            assert bracket >= 50.0 + 27.0 * W - 11449.0 / 186.0 - 2e-8
        assert bracket >= -2e-8

    print("random hypersimplex checks: PASS")
    print("small-W samples checked:", checked_small)
    print("smallest sampled rank-four bracket:", smallest_rank4_bracket)


def random_projection(p: int, r: int, rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(p, r)))
    return q @ q.T


def lambda1_exact(P: np.ndarray) -> float:
    d = np.diag(P)
    r = int(round(float(np.trace(P))))
    S2 = float(np.sum(d**2))
    S3 = float(np.sum(d**3))
    S4 = float(np.sum(d**4))
    U = 0.0
    T4 = 0.0
    p = len(d)
    for i in range(p):
        for j in range(i + 1, p):
            qij = float(P[i, j] ** 2)
            U += float(d[i] * d[j] * qij)
            T4 += qij * qij
    V = T4 + 3.0 * U
    return (
        6.0 * (r + 4) * (r + 6) * (r - S2)
        - 40.0 * (r + 6) * (r - S3)
        + 114.0 * (r - S4)
        - 9.0 * (r * r - S2 * S2)
        + 48.0 * V
    )


def random_projection_checks(seed: int = 22019, trials: int = 10000) -> None:
    rng = np.random.default_rng(seed)
    min_lam = float("inf")
    for _ in range(trials):
        p = int(rng.integers(5, 13))
        P = random_projection(p, 4, rng)
        lam = lambda1_exact(P)
        min_lam = min(min_lam, lam)
        assert lam >= -2e-8
    print("random rank-four projection lambda1 checks: PASS")
    print("smallest sampled exact lambda1:", min_lam)


if __name__ == "__main__":
    symbolic_checks()
    random_hypersimplex_checks()
    random_projection_checks()

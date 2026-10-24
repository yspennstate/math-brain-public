"""PROB20-19 rank-two all-distinct coefficient checker.

Checks the new theorem archived in
runs/2026-09-15/2026-09-15T21-11-50Z__report.md:

1. For k=4, symbolic extraction of [x1^2 x2^2 x3^2 x4^2]
   from |sum z_i x_i|^8 agrees with the explicit phase formula

      72 prod(d_i) * (1 + |S|^2 + |E2|^2/2).

2. For general small k, direct multinomial enumeration agrees with the
   Laurent constant-term / circle-average formula.

3. For random rank-two projections, the quartic coefficient lambda_1
   agrees with W_1111/3 and with the sum of the positive local terms.

This is reproducible algebra/numerical self-checking, not independent
formal verification.
"""
from __future__ import annotations

import itertools
import math
from math import factorial
import numpy as np
import sympy as sp


def symbolic_k4_check() -> None:
    x = sp.symbols("x0:4", real=True)
    r = sp.symbols("r0:4", positive=True)
    th = sp.symbols("th0:4", real=True)

    # Use formal complex phase variables u_i and their inverses.
    u = sp.symbols("u0:4", nonzero=True)

    # Direct multinomial phase sum for beta_i in {0,1,2}, sum beta_i=4.
    phase_sum = 0
    for beta in itertools.product(range(3), repeat=4):
        if sum(beta) != 4:
            continue
        term = sp.Integer(factorial(4) ** 2)
        for i, b in enumerate(beta):
            term *= u[i] ** (b - 1) / (factorial(b) * factorial(2 - b))
        phase_sum += term

    # Explicit phase identity after dividing by prod(d_i):
    # 72 * (1 + |S|^2 + |E2|^2/2).
    # For unit u_i, conjugation means u_i -> u_i^{-1}.
    S = sum(u)
    Sbar = sum(1 / ui for ui in u)
    E2 = sum(u[i] * u[j] for i in range(4) for j in range(i + 1, 4))
    E2bar = sum(1 / (u[i] * u[j]) for i in range(4) for j in range(i + 1, 4))
    explicit = 72 * (1 + S * Sbar + sp.Rational(1, 2) * E2 * E2bar)

    diff = sp.factor(sp.together(phase_sum - explicit))
    assert diff == 0, diff
    print("symbolic k=4 phase identity: PASS")


def direct_phase_factor(u: np.ndarray) -> float:
    k = len(u)
    total = 0.0 + 0.0j
    for beta in itertools.product(range(3), repeat=k):
        if sum(beta) != k:
            continue
        coeff = float(factorial(k) ** 2)
        term = 1.0 + 0.0j
        for i, b in enumerate(beta):
            coeff /= factorial(b) * factorial(2 - b)
            term *= u[i] ** (b - 1)
        total += coeff * term
    return float(total.real)


def constant_term_factor(u: np.ndarray) -> float:
    """Exact finite Laurent enumeration of (k!)^2 [t^0] product factors."""
    k = len(u)
    total = 0.0 + 0.0j
    for gamma in itertools.product((-1, 0, 1), repeat=k):
        if sum(gamma) != 0:
            continue
        coeff = 1.0
        term = 1.0 + 0.0j
        for i, g in enumerate(gamma):
            if g:
                coeff *= 0.5
                term *= u[i] ** g
        total += coeff * term
    return float((factorial(k) ** 2 * total).real)


def circle_average_factor(u: np.ndarray, ngrid: int = 200_000) -> float:
    k = len(u)
    psi = 2 * np.pi * np.arange(ngrid) / ngrid
    prod = np.ones(ngrid)
    for ui in u:
        phi = np.angle(ui)
        prod *= 1.0 + np.cos(psi + phi)
    return float(factorial(k) ** 2 * np.mean(prod))


def all_orders_numeric_check() -> None:
    rng = np.random.default_rng(2019)
    for k in range(1, 8):
        for _ in range(20):
            phi = rng.uniform(-np.pi, np.pi, size=k)
            u = np.exp(1j * phi)
            a = direct_phase_factor(u)
            b = constant_term_factor(u)
            c = circle_average_factor(u, ngrid=20_000)
            assert a >= -1e-9
            assert b >= -1e-9
            assert abs(a - b) <= 1e-8 * (1 + abs(a))
            assert abs(a - c) <= 5e-8 * (1 + abs(a))
    print("all-orders multinomial/constant-term/circle checks: PASS")


def random_projection(p: int, r: int, rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(p, r)))
    return q @ q.T


def quartic_lambda1(P: np.ndarray) -> float:
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
    V = T4 + 3 * U
    return (
        6 * (r + 4) * (r + 6) * (r - S2)
        - 40 * (r + 6) * (r - S3)
        + 114 * (r - S4)
        - 9 * (r**2 - S2**2)
        + 48 * V
    )


def local_k4_from_rows(rows: np.ndarray) -> float:
    z = rows[:, 0] + 1j * rows[:, 1]
    d = np.abs(z) ** 2
    if np.any(d <= 1e-15):
        return 0.0
    u = z**2 / d
    S = np.sum(u)
    E2 = sum(u[i] * u[j] for i in range(4) for j in range(i + 1, 4))
    return float(72 * np.prod(d) * (1 + abs(S) ** 2 + 0.5 * abs(E2) ** 2))


def projection_quartic_check() -> None:
    rng = np.random.default_rng(20260915)
    for p in range(4, 10):
        for _ in range(100):
            q, _ = np.linalg.qr(rng.normal(size=(p, 2)))
            P = q @ q.T
            lam1 = quartic_lambda1(P)
            w1111 = 0.0
            for I in itertools.combinations(range(p), 4):
                w1111 += local_k4_from_rows(q[list(I), :])
            assert w1111 >= -1e-10
            assert abs(lam1 - w1111 / 3.0) <= 2e-9 * (1 + abs(lam1))
    print("rank-two lambda1 = W1111/3 local-sum checks: PASS")


if __name__ == "__main__":
    symbolic_k4_check()
    all_orders_numeric_check()
    projection_quartic_check()

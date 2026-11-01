"""PROB20-19 rank-two quartic lambda2 checker.

Reproduces exact symbolic identities from the 2026-09-15T19-46-00Z report
and performs randomized numerical checks on rank-two projections.

This is a self-checking aid, not an independent/formal proof.
Requires numpy and sympy.
"""
from __future__ import annotations
import numpy as np
import sympy as sp


def symbolic_checks() -> None:
    # One-coordinate boundary: x=(1,y), sum y=1.
    e2, e3, e4 = sp.symbols("e2 e3 e4")
    s2 = 1 - 2 * e2
    s3 = 1 - 3 * e2 + 3 * e3
    s4 = 1 - 4 * e2 + 2 * e2**2 + 4 * e3 - 4 * e4
    F = sp.expand(11 - 6 * s2 - 3 * s2**2 - 32 * s3 + 30 * s4)
    assert sp.factor(F - 24 * (2 * e2**2 + e3 - 5 * e4)) == 0

    # Uniform support N.
    N = sp.symbols("N", positive=True)
    x = sp.Rational(2, 1) / N
    Fu = sp.factor(16 - 3 * (N * x**2) ** 2 - 32 * N * x**3 + 30 * N * x**4)
    assert sp.factor(Fu - 16 * (N - 3) * (N - 2) * (N + 5) / N**3) == 0

    # One-plus-n family.
    n, a = sp.symbols("n a", positive=True)
    b = (2 - a) / n
    S2 = a**2 + n * b**2
    S3 = a**3 + n * b**3
    S4 = a**4 + n * b**4
    Fn = sp.factor(16 - 3 * S2**2 - 32 * S3 + 30 * S4)
    assert sp.factor(Fn.subs(n, 2) - 3 * a**2 * (3 * a - 2) ** 2) == 0
    assert sp.factor(
        Fn.subs(n, 3)
        - sp.Rational(8, 9) * a * (29 * a**3 - 30 * a**2 - 12 * a + 20)
    ) == 0

    xvar = sp.symbols("xvar", positive=True)
    finf = 16 - 32 * a**3 + 27 * a**4
    H = (
        6 * a**2 * xvar
        + (3 * a**2 - 44 * a + 76) * xvar**2
        - 30 * (2 - a) ** 2 * xvar**3
    )
    assert sp.factor(Fn - (finf - (2 - a) ** 2 * H.subs(xvar, 1 / n))) == 0

    F4 = sp.factor(Fn.subs(n, 4))
    target = sp.Rational(3, 32) * (
        275 * a**4 - 280 * a**3 - 120 * a**2 + 160 * a + 48
    )
    assert sp.factor(F4 - target) == 0
    assert sp.factor(
        sp.diff(F4, a)
        - sp.Rational(15, 8) * (5 * a - 2) * (11 * a**2 - 4 * a - 4)
    ) == 0
    print("symbolic identities: PASS")


def random_projection(p: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    X = rng.normal(size=(p, 2))
    Q, _ = np.linalg.qr(X)
    return Q @ Q.T, Q


def frame_quantities(P: np.ndarray, Qframe: np.ndarray):
    d = np.diag(P)
    z = Qframe[:, 0] + 1j * Qframe[:, 1]
    w = z * z
    A = np.sum(d * w)
    B = np.sum(w * w)
    S2 = np.sum(d**2)
    S3 = np.sum(d**3)
    S4 = np.sum(d**4)
    T = sum(P[i, j] ** 4 for i in range(len(d)) for j in range(i + 1, len(d)))
    U = sum(
        d[i] * d[j] * P[i, j] ** 2
        for i in range(len(d))
        for j in range(i + 1, len(d))
    )
    lam2_general = 3 * (4 - S2**2) + 2 * (2 - S4) - 16 * (T + 3 * U)
    lam2_complex = 16 - 18 * S2**2 + 30 * S4 - 16 * abs(A) ** 2 - abs(B) ** 2
    F = 16 - 3 * S2**2 - 32 * S3 + 30 * S4

    lam1_general = (
        288 * (2 - S2)
        - 320 * (2 - S3)
        + 114 * (2 - S4)
        - 9 * (4 - S2**2)
        + 48 * (T + 3 * U)
    )
    qsum = 0.0
    E = 0.0
    edge = 0.0
    for i in range(len(d)):
        for j in range(i + 1, len(d)):
            q = P[i, j] ** 2
            c = (
                92
                - 206 * (d[i] + d[j])
                + 114 * (d[i] ** 2 + d[j] ** 2)
                + 144 * d[i] * d[j]
            )
            edge += q * c
            qsum += q
            E += q * q
    lam1_edge = edge + 36 * qsum * qsum + 48 * E
    return d, w, A, B, S2, S3, S4, lam2_general, lam2_complex, F, lam1_general, lam1_edge


def random_checks(seed: int = 2019, trials: int = 500) -> None:
    rng = np.random.default_rng(seed)
    min_lam2 = float("inf")
    min_F = float("inf")
    for p in range(3, 13):
        for _ in range(trials):
            P, Q = random_projection(p, rng)
            d, w, A, B, S2, S3, S4, l2g, l2c, F, l1g, l1e = frame_quantities(P, Q)
            assert np.allclose(P @ P, P, atol=2e-10)
            assert abs(np.sum(d) - 2) < 2e-10
            assert abs(np.sum(w)) < 2e-10
            assert abs(l2g - l2c) < 2e-9
            assert abs(l1g - l1e) < 2e-9

            # Lemma 4.1 and Lemma 4.2.
            assert abs(A) ** 2 <= 2 * S3 - S2**2 + 2e-10
            assert abs(B) ** 2 <= 2 * S3 - abs(A) ** 2 + 2e-10
            assert l2c >= F - 2e-9
            assert F >= -2e-9
            min_lam2 = min(min_lam2, l2c)
            min_F = min(min_F, F)
    print(f"random projection checks: PASS; min lambda2={min_lam2:.6g}, min F={min_F:.6g}")


def equality_checks() -> None:
    # Coordinate rank-two projection.
    P = np.diag([1.0, 1.0, 0.0, 0.0])
    Q = np.array([[1.0, 0.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0]])
    vals = frame_quantities(P, Q)
    assert abs(vals[8]) < 1e-12

    # Equilateral tight frame: P=I-(1/3)11^T in R^3.
    P = np.eye(3) - np.ones((3, 3)) / 3
    _, vecs = np.linalg.eigh(P)
    Q = vecs[:, -2:]
    vals = frame_quantities(P, Q)
    assert abs(vals[9]) < 1e-10   # scalar F = 0
    assert abs(vals[8] - 16 / 9) < 1e-9
    print("equality cases: PASS")


if __name__ == "__main__":
    symbolic_checks()
    equality_checks()
    random_checks()

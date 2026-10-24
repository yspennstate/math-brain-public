"""Symbolic / numerical checker for PROB20-19 run 2026-09-15T17-35-56Z.

Checks:
  1. degree-2 and degree-3 analytic contrasts as positive combinations of
     quartic contrasts I1,...,I4;
  2. complement-transfer formulas for rank-three projections;
  3. exact rank-three / p=4 codimension-one reduction
         lambda1 = 24*(e2 - 5*e3 + 35*e4);
  4. random numerical sanity checks of the complement identities and the
     lower bound lambda1 >= 4*e2.

This is a reproducible algebra checker, not an independent proof verifier.
Requires numpy and sympy.
"""
from __future__ import annotations

import numpy as np
import sympy as sp


def analytic_contrast_check() -> None:
    p = sp.symbols("p", integer=True, positive=True)
    A, B, C, D, E = sp.symbols("A B C D E")
    I1, I2, I3, I4 = sp.symbols("I1 I2 I3 I4")

    sol = sp.solve(
        [
            sp.Eq(I1, D - 3 * E),
            sp.Eq(I2, C - 3 * D),
            sp.Eq(I3, B - 5 * D),
            sp.Eq(I4, A - 4 * B - 5 * C),
        ],
        [A, B, C, D],
        dict=True,
    )[0]

    A3 = A + (p - 1) * B
    B3 = B + C + (p - 2) * D
    C3 = 3 * D + (p - 3) * E
    D1 = sp.expand(B3 - 3 * C3).subs(sol)
    D2 = sp.expand(A3 - 5 * B3).subs(sol)

    A2 = A3 + (p - 1) * B3
    B2 = 2 * B3 + (p - 2) * C3
    J2 = sp.expand(A2 - 3 * B2).subs(sol)

    assert sp.simplify(D1 - ((p - 3) * I1 + I2 + I3)) == 0
    assert sp.simplify(D2 - ((p - 2) * I3 + I4)) == 0
    assert sp.simplify(
        J2
        - (
            (p - 2) * (p - 3) * I1
            + (p - 2) * I2
            + 2 * (p - 2) * I3
            + I4
        )
    ) == 0
    print("analytic contrast identities: PASS")


def geom(P: np.ndarray) -> dict[str, float]:
    r = int(round(np.trace(P)))
    d = np.diag(P)
    S2 = float(np.sum(d**2))
    S3 = float(np.sum(d**3))
    S4 = float(np.sum(d**4))
    D2 = r - S2
    D3 = r - S3
    D4 = r - S4
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
    l4 = D4
    l3 = 4 * ((r + 6) * D3 - 6 * D4)
    l2 = 3 * (r * r - S2 * S2) + 2 * D4 - 16 * V
    l1 = (
        6 * (r + 4) * (r + 6) * D2
        - 40 * (r + 6) * D3
        + 114 * D4
        - 9 * (r * r - S2 * S2)
        + 48 * V
    )
    return {
        "r": r,
        "W": D2,
        "D3": D3,
        "l1": l1,
        "l2": l2,
        "l3": l3,
        "l4": l4,
    }


def random_projection(p: int, r: int, rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(p, r)))
    return q @ q.T


def complement_transfer_check(seed: int = 190319) -> None:
    rng = np.random.default_rng(seed)
    for p in (5, 6, 7, 9):
        for _ in range(50):
            P = random_projection(p, 3, rng)
            Q = np.eye(p) - P
            gp = geom(P)
            gq = geom(Q)
            s = p - 3
            H = 40 * gq["D3"] - 6 * (s + 7) * gq["W"]
            pred = np.array(
                [
                    gq["l1"] + s * H,
                    gq["l2"] + H,
                    gq["l3"] + 4 * ((9 - s) * gq["D3"] - 9 * gq["W"]),
                    gq["l4"] + 6 * gq["W"] - 4 * gq["D3"],
                ]
            )
            got = np.array([gp["l1"], gp["l2"], gp["l3"], gp["l4"]])
            assert np.allclose(got, pred, atol=2e-10, rtol=2e-10)
            assert np.isclose(
                gp["l1"] - s * gp["l2"],
                gq["l1"] - s * gq["l2"],
                atol=2e-10,
                rtol=2e-10,
            )
    print("complement-transfer identities: PASS")


def codim1_symbolic_check() -> None:
    e = sp.symbols("e0:4", nonnegative=True)
    d = [1 - x for x in e]
    S2 = sum(x**2 for x in d)
    S3 = sum(x**3 for x in d)
    S4 = sum(x**4 for x in d)
    U = sum(
        d[i] * d[j] * e[i] * e[j]
        for i in range(4)
        for j in range(i + 1, 4)
    )
    T4 = sum(
        (e[i] * e[j]) ** 2
        for i in range(4)
        for j in range(i + 1, 4)
    )
    V = T4 + 3 * U
    lam1 = sp.expand(
        378 * (3 - S2)
        - 360 * (3 - S3)
        + 114 * (3 - S4)
        - 9 * (9 - S2**2)
        + 48 * V
    )

    sym, rem, mapping = sp.symmetrize(lam1, e, formal=True)
    assert rem == 0
    s1, s2, s3, s4 = [item[0] for item in mapping]
    reduced = sp.expand(sym.subs(s1, 1))
    target = 24 * (s2 - 5 * s3 + 35 * s4)
    assert sp.simplify(reduced - target) == 0
    print("codimension-one symbolic reduction: PASS")


def codim1_random_check(seed: int = 4043) -> None:
    rng = np.random.default_rng(seed)
    for _ in range(1000):
        e = rng.dirichlet(np.ones(4))
        z = np.sqrt(e)
        P = np.eye(4) - np.outer(z, z)
        l1 = geom(P)["l1"]
        e2 = sum(e[i] * e[j] for i in range(4) for j in range(i + 1, 4))
        e3 = sum(
            e[i] * e[j] * e[k]
            for i in range(4)
            for j in range(i + 1, 4)
            for k in range(j + 1, 4)
        )
        e4 = float(np.prod(e))
        exact = 24 * (e2 - 5 * e3 + 35 * e4)
        assert np.isclose(l1, exact, atol=2e-10, rtol=2e-10)
        assert l1 + 2e-10 >= 4 * e2
    print("codimension-one random lower-bound checks: PASS")


if __name__ == "__main__":
    analytic_contrast_check()
    complement_transfer_check()
    codim1_symbolic_check()
    codim1_random_check()

"""Reproducible self-checks for the PROB20-19 2026-09-15T22-48-54Z report.

This script checks the exact scalar factorization used for the universal
quintic top-four occupancy facet and randomized projection instances of both
that facet and the all-orders expected-support inequality.  It is supporting
self-review, not an independent formal proof.
"""

import math
import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------
# Exact symbolic checks for the quintic U_4 facet.
# ---------------------------------------------------------------------------
x, r = sp.symbols("x r", real=True)

Phi = (
    10 * (r + 6) * (r + 8) * x**3
    - 105 * (r + 8) * x**4
    + 378 * x**5
)
Phi1 = sp.expand(Phi.subs(x, 1))
Q = (
    10 * r**2 * (1 + x)
    + r * (35 + 35 * x - 105 * x**2)
    + 18 + 18 * x - 462 * x**2 + 378 * x**3
)

assert sp.expand(Phi1 - (10 * r**2 + 35 * r + 18)) == 0
assert sp.expand(x * Phi1 - Phi - x * (1 - x) * Q) == 0
assert sp.expand(
    (Q.subs(r, 3) - 27)
    - 3 * (x - 1) * (126 * x**2 - 133 * x - 62)
) == 0

# The coordinate numerator C_4 is 15 r Phi_r(1).
C4_COORD = sp.expand(15 * r * Phi1)
assert C4_COORD == 15 * r * (10 * r**2 + 35 * r + 18)


# ---------------------------------------------------------------------------
# Numerical projection sanity checks.
# ---------------------------------------------------------------------------
def odd_double_factorial(odd_n: int) -> int:
    if odd_n <= 0:
        return 1
    out = 1
    for j in range(1, odd_n + 1, 2):
        out *= j
    return out


def T(rank: int, m: int) -> float:
    out = 1.0
    for j in range(m):
        out *= rank + 2 * j
    return out


def c4_numerator(diag: np.ndarray, rank: int) -> float:
    s3 = np.sum(diag**3)
    s4 = np.sum(diag**4)
    s5 = np.sum(diag**5)
    return (
        150 * (rank + 6) * (rank + 8) * s3
        - 1575 * (rank + 8) * s4
        + 5670 * s5
    )


def c4_coordinate(rank: int) -> float:
    return 15 * rank * (10 * rank**2 + 35 * rank + 18)


def support_marginal(rank: int, k: int, d: float) -> float:
    """g_{r,k}(d)=1-E(1-d U_1^2)^k, evaluated by exact moments."""
    out = 0.0
    for m in range(1, k + 1):
        moment = odd_double_factorial(2 * m - 1) / T(rank, m)
        out += ((-1) ** (m + 1)) * math.comb(k, m) * d**m * moment
    return out


rng = np.random.default_rng(20260915)

for rank in range(3, 11):
    for extra in (1, 3, 7):
        p = rank + extra
        for _ in range(50):
            G = rng.normal(size=(p, rank))
            Qmat, _ = np.linalg.qr(G, mode="reduced")
            P = Qmat @ Qmat.T
            d = np.diag(P)

            # Report theorem (7.2), before dividing by T_{r,5}:
            # C4(coord)-C4(P) >= 405(r-S2).
            W = rank - np.sum(d * d)
            gap = c4_coordinate(rank) - c4_numerator(d, rank)
            assert gap + 1e-8 >= 405 * W

            # Report theorem (8.5): expected occupied categories are at least
            # the coordinate/projective value.  Check several orders.
            for k in (2, 3, 5, 8):
                lhs = sum(support_marginal(rank, k, float(di)) for di in d)
                rhs = rank * support_marginal(rank, k, 1.0)
                assert lhs + 1e-10 >= rhs

print("PROB20-19 quintic top-four/support checks passed")

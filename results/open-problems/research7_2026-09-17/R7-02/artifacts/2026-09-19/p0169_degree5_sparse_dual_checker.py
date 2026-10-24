#!/usr/bin/env python3
"""Exact rational checker for the d=5 sparse layer-dual identities in P0169.

No floating-point arithmetic is used.  The checker verifies the coefficient
identities on the full normalized-Newton basis for symmetrized degree-5
Boolean functions, the resulting 11- and 12-variable bounds, and the dyadic
granularity gap around sqrt(5).
"""

from fractions import Fraction
from math import comb


def row(n: int, k: int, d: int = 5):
    """Coefficients of b_k in the integer Newton coordinates u_0,...,u_d.

    If r(k)=sum_j u_j binom(k,j)/binom(n,j), then
    b_k=binom(n,k)r(k)=sum_j u_j binom(n-j,k-j).
    """
    return [
        Fraction(comb(n - j, k - j)) if 0 <= j <= min(d, k) else Fraction(0)
        for j in range(d + 1)
    ]


def combine(n: int, terms, d: int = 5):
    out = [Fraction(0) for _ in range(d + 1)]
    for k, lam in terms:
        r = row(n, k, d)
        for j in range(d + 1):
            out[j] += lam * r[j]
    return out


# For degree <=5 the signed level-one mass is
# L=-u_1-u_2-(3/4)u_3-(1/2)u_4-(5/16)u_5.
objective = [
    Fraction(0),
    Fraction(-1),
    Fraction(-1),
    Fraction(-3, 4),
    Fraction(-1, 2),
    Fraction(-5, 16),
]

id11 = combine(
    11,
    [
        (0, Fraction(1, 16)),
        (11, Fraction(-1, 16)),
        (3, Fraction(1, 80)),
        (8, Fraction(-1, 80)),
    ],
)

id12 = combine(
    12,
    [
        (0, Fraction(13, 288)),
        (12, Fraction(-13, 288)),
        (3, Fraction(1, 180)),
        (9, Fraction(-1, 180)),
        (4, Fraction(1, 480)),
        (8, Fraction(-1, 480)),
    ],
)

assert id11 == objective
assert id12 == objective

bound11 = Fraction(1, 16) + Fraction(comb(11, 3), 80)
bound12 = (
    Fraction(13, 288)
    + Fraction(comb(12, 3), 180)
    + Fraction(comb(12, 4), 480)
)

assert bound11 == Fraction(17, 8)
assert bound11 * bound11 < 5
assert bound12 == Fraction(331, 144)
assert bound12 < Fraction(37, 16)
assert Fraction(35, 16) ** 2 < 5 < Fraction(36, 16) ** 2
assert Fraction(36, 16) - bound11 == Fraction(1, 8)

print("P0169 d=5 exact sparse-dual checker")
print("arithmetic=fractions.Fraction; floating_point=False")
print("objective_newton_coeffs", objective)
print("n=11_dual_coeffs", id11)
print("n=11_bound", bound11, "square", bound11 * bound11, "<5")
print("n=12_dual_coeffs", id12)
print("n=12_continuous_bound", bound12)
print(
    "dyadic_gap: (35/16)^2 =",
    Fraction(35, 16) ** 2,
    "< 5 < (36/16)^2 =",
    Fraction(36, 16) ** 2,
)
print("n=12_granular_bound <= 36/16 =", Fraction(36, 16))
print(
    "if n=12 has L=9/4, each singleton >= 9/4-17/8 =",
    Fraction(36, 16) - bound11,
)
print("ASSERTIONS_PASS")

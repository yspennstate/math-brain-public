#!/usr/bin/env python3
"""Exact/rational arithmetic support for P17-M43.

This artifact does NOT diagonalize a magnetic Bloch matrix and does NOT by itself
prove a spectral gap.  It records the rational-fiber dimensions, exact Fermi-rank
targets of the four already-classified historical classes, the corresponding
singular-value counts in the doubled chiral cell, and the refined phase-grid
Lipschitz constant proved in the M43 report.
"""

from fractions import Fraction
from math import exp, pi, sin

r = 0.4
Q1 = P1 = 153
Q2 = P2 = 148
N = P1 * P2

theta1 = Fraction(97, 153)
theta2 = Fraction(87, 148)
b = Fraction(1, 153)

# Coordinates are (c_empty, c_13, c_24, c_34, c_1234).
classes = {
    "x1": (1, -1, -1, 0, 1),
    "x2": (-1, 2, 2, 0, -3),
    "x3": (2, -2, -2, 0, 3),
    "x4": (0, 1, 1, 0, -1),
}


def trace_of(c):
    c0, c13, c24, c34, c1234 = c
    return (
        Fraction(c0)
        + c13 * theta1
        + c24 * theta2
        + c34 * b
        + c1234 * theta1 * theta2
    )


ranks = {}
for name, c in classes.items():
    tr = trace_of(c)
    rk = tr * N
    assert rk.denominator == 1
    ranks[name] = int(rk)
    print(f"{name}: trace={tr}, rank={int(rk)}")

assert ranks["x1"] + ranks["x4"] == N
assert ranks["x2"] + ranks["x3"] == N

# In the doubled 2P1 x P2 chiral cell, a positive full gap at energy E has
# rank 2r_E.  If B is the N x N off-diagonal block, then
#   #{singular values of B below E} = 2 r_E - N.
inner_positive_singular_count = 2 * ranks["x3"] - N
outer_positive_singular_count = 2 * ranks["x4"] - N
print(f"N={N}, doubled_dimension={2*N}")
print(f"inner_positive_singular_count={inner_positive_singular_count}")
print(f"outer_positive_singular_count={outer_positive_singular_count}")

# Refined coefficient bounds for the rational source hopping.
s1 = sin(pi * 97 / 153)
s2 = sin(pi * 87 / 148)
A1 = exp(-1 + 2 * r * s1)
A2 = exp(-1 + 2 * r * s2)

# Equal M-point grid on alpha1, alpha2, doubled beta1, beta2, each with
# covering radius pi/M.  The proved M43 modulus is
# 4 r s1 A1/Q1 * |d alpha1|
# +4 r s2 A2/Q2 * |d alpha2|
# +A1/P1 * |d beta1_tilde|
# +2 A2/P2 * |d beta2|.
equal_grid_numerator = pi * (
    4 * r * (s1 * A1 / Q1 + s2 * A2 / Q2)
    + A1 / P1
    + 2 * A2 / P2
)
print(f"s1={s1:.17g}, s2={s2:.17g}")
print(f"A1={A1:.17g}, A2={A2:.17g}")
print(f"equal_grid_numerator={equal_grid_numerator:.17g}")
for M in (4, 6, 8, 10, 12, 16):
    print(f"M={M}: epsilon={equal_grid_numerator/M:.17g}")

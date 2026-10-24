#!/usr/bin/env python3
"""Exact/numerical sanity checks for NM13-12 radial-margin universality.

The theorem itself is proved analytically in the run report.  This script checks
only the finite arithmetic used in the application: the inherited T03 bracket,
the explicit chi-radius union-bound rate delta_N=sqrt(12 log N/N), and the
Rademacher kappa=-1 localized-witness obstruction to unrestricted entrywise
universality.
"""

from fractions import Fraction
import math

alpha_L = Fraction(630297437506, 10**11)
alpha_U = Fraction(1278437096216, 10**11)
width = alpha_U - alpha_L
assert width == Fraction(64813965871, 10**10)

print("INHERITED_T03_BRACKET")
print("alpha_L_exact", alpha_L)
print("alpha_L_decimal", f"{float(alpha_L):.11f}")
print("alpha_U_exact", alpha_U)
print("alpha_U_decimal", f"{float(alpha_U):.11f}")
print("width_exact", width)
print("width_decimal", f"{float(width):.11f}")

# Laurent--Massart consequence used in the report:
# P(| ||g||/sqrt(N)-1 |>delta) <= 2 exp(-N delta^2/4), 0<delta<=1.
# With delta_N=sqrt(12 log N/N), the one-row RHS is 2 N^{-3}; for
# M<=ceil(alpha_U N) the union bound is O(N^{-2}).
print("\nCHI_RADIUS_RATE")
for N in (10_000, 100_000, 1_000_000):
    delta = math.sqrt(12.0 * math.log(N) / N)
    assert delta < 1.0
    one_row_bound = 2.0 * math.exp(-N * delta * delta / 4.0)
    target = 2.0 / (N**3)
    assert abs(one_row_bound - target) <= 1e-24 + 1e-12 * target
    M = math.ceil(float(alpha_U) * N)
    union_bound = M * one_row_bound
    print(
        "N", N,
        "delta_N", f"{delta:.15g}",
        "harder_margin", f"{-1.0 + delta:.15g}",
        "easier_margin", f"{-1.0 - delta:.15g}",
        "union_bound", f"{union_bound:.15g}",
    )

# Exact obstruction to any blanket iid-entry Lindeberg universality at kappa=-1:
# for a Rademacher matrix and x=e_j, every row inner product is +/-1 >= -1.
assert min((-1, 1)) >= -1
print("\nRADEMACHER_KAPPA_MINUS1_COORDINATE_WITNESS_PASS")
print("For every M,N and every column j, x=e_j is feasible deterministically.")
print("ALL_CHECKS_PASS")

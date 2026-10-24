#!/usr/bin/env python3
"""Exact rational checks for the finite arithmetic anchor in the P0083 alpha>6 proof.

This does NOT certify the analytic Hessian/Laplacian argument.  That proof is written
on the immutable run report page.  This script only checks the rational endpoint
identities/inequalities used after the analytic monotonicity reduction.
"""

from fractions import Fraction


def g(w: Fraction) -> Fraction:
    return w - 2 + Fraction(2, 1) / w


a = 6
h6 = Fraction(a - 1, a)
c6 = Fraction(a + 2, a)
g_three_halves = g(Fraction(3, 2))
g_c6 = g(c6)

# F(alpha) = 2 (alpha-1)^2/(alpha+2) * (alpha/(alpha+2))^alpha.
F6 = Fraction(2 * (a - 1) ** 2, a + 2) * Fraction(a, a + 2) ** a
F6_gap = F6 - 1

assert h6 == Fraction(5, 6)
assert c6 == Fraction(4, 3)
assert g_three_halves == Fraction(5, 6)
assert g_c6 == Fraction(5, 6)
assert F6 == Fraction(18225, 16384)
assert F6_gap == Fraction(1841, 16384)
assert F6 > 1

# The report proves symbolically:
#   g(1+2/a) - (1-1/a) = (6-a)/(a(a+2)),
# and
#   2/(a-1)+1/(a+2)-2/a
#       = (a^2+a+4)/(a(a-1)(a+2)) > 0  for a>1.
# The exact anchor above is the only finite numerical comparison needed.

print("PASS")
print(f"h(6)={h6}")
print(f"c(6)={c6}")
print(f"g(3/2)={g_three_halves}")
print(f"g(c(6))={g_c6}")
print(f"F(6)={F6}")
print(f"F(6)-1={F6_gap}")

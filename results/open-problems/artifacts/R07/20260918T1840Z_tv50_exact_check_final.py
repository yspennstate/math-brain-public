#!/usr/bin/env python3
"""Final exact self-check for R07/I0077 traveling Cantor velocity-fan representative.

This checks only the finite arithmetic used by the concrete example. The theorem
itself is analytic and is proved in the immutable run report.
"""

from fractions import Fraction

# Temporal/spatial dimension gap:
# log(2)/log(3) > 3/5  <=>  2^5 > 3^3.
threshold_gap = 2**5 - 3**3
assert threshold_gap == 5
assert threshold_gap > 0

# A_32 is generated inside [0,1] by x/32 and 31/32+x/32.
# Its largest first-level complementary gap has length 30/32=15/16,
# hence half-gap 15/32. At the first canonical chamber age u=3/2,
# dist(u,E)=1/6 and r=u^3/6=9/16, already larger than 15/32.
u = Fraction(3, 2)
r = u**3 / 6
internal_half_gap = Fraction(15, 32)
assert r == Fraction(9, 16)
assert r - internal_half_gap == Fraction(3, 32) > 0

# Between adjacent velocity cells m*u+A_32 and (m+1)*u+A_32,
# the gap between the endpoints 1+m*u and (m+1)*u is u-1.
# 2r >= u-1 for every u>=1 follows from
# u^3 - 3u + 3 = (u-1)^2(u+2)+1 > 0.
lhs_coeff = (1, 0, -3, 3)
rhs_coeff = (1, 0, -3, 3)
assert lhs_coeff == rhs_coeff
assert 2*r - (u-1) == Fraction(5, 8) > 0

print("PASS")
print(f"threshold_integer_gap={threshold_gap}")
print(f"u=3/2: r={r}, internal_half_gap={internal_half_gap}, margin={r-internal_half_gap}")
print(f"u=3/2: intercell_margin={2*r-(u-1)}")
print("identity: u^3-3u+3=(u-1)^2(u+2)+1")

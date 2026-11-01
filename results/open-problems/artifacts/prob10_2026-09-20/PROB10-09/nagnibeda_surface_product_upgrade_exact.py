#!/usr/bin/env python3
"""Exact arithmetic core for the PROB10-09 Nagnibeda spectral upgrade.

The external theorem input (Bartholdi, arXiv:math/0112108, Thm. 1.3,
quoting Nagnibeda) is
    ||M_2|| <= 0.662816,   ||M_3|| <= 0.552792
for the standard genus-2 and genus-3 surface-group Markov operators.
We deliberately relax these to exact rationals 663/1000 and 553/1000.

Everything after those literature inequalities is checked exactly here.
Decimal gap displays are informational only.
"""
from fractions import Fraction
from decimal import Decimal, getcontext


def phi2(d, p):
    """Radius-two lower witness for E[1-(1-p)^|C(o)|] on T_d."""
    p = Fraction(p)
    s = 1 - p
    return 1 - s * (s + p*s*(1-p*p)**(d-1))**d


# Conservative rational relaxations of the cited rigorous upper bounds.
M2 = Fraction(663, 1000)
M3 = Fraction(553, 1000)
assert M2 > Fraction(662816, 1000000)
assert M3 > Fraction(552792, 1000000)
A2 = 8*M2                    # <= 663/125
A3 = 12*M3                   # <= 1659/250

# X_{2,2}: degree D=16, Q=D-1=15.
p22 = Fraction(11, 100)
R22 = 2*A2                   # <= 1326/125
Q22 = 15
m22 = 5*phi2(6, p22) - 1    # T_6 square T_6 branching margin
z22 = 1/p22
P22 = z22*z22 - R22*z22 + Q22
Disc22 = R22*R22 - 4*Q22
assert m22 > 0
assert Disc22 > 0
assert P22 > 0
assert z22*z22 > Q22
# If z22 were below the smaller positive root, z22^2 < product of roots = Q22.
# Hence P22(z22)>0 and z22^2>Q22 force z22 above the larger root beta.

# Frozen X_{3,4}: degree D=28. Reuse the previously proved exact p_c witness.
p34 = Fraction(19, 400)
m34 = 13*phi2(10, p34) - 1
assert m34 > 0
# Genus 4 keeps the old Freiheitssatz bound 2 + 2 sqrt(13).
# Thus R34 <= c34 + 2 sqrt(13), c34=A3+2.
c34 = A3 + 2
z34 = 1/p34
y34 = z34 - c34
sq34 = y34*y34 - 52       # (2 sqrt(13))^2 = 52
assert y34 > 0 and sq34 > 0
# Therefore z34 > R34. Since beta=(R+sqrt(R^2-108))/2 < R, beta < z34.

# Informational high-precision decimal gaps only; proof above is rational/radical exact.
getcontext().prec = 60
D = Decimal
R22d = D(R22.numerator)/D(R22.denominator)
beta22d = (R22d + (R22d*R22d-D(60)).sqrt())/D(2)
gap22d = D(1)/beta22d - D(11)/D(100)

c34d = D(c34.numerator)/D(c34.denominator)
R34d = c34d + D(2)*D(13).sqrt()
beta34d = (R34d + (R34d*R34d-D(108)).sqrt())/D(2)
gap34d = D(1)/beta34d - D(19)/D(400)

print("PROB10-09 NAGNIBEDA SPECTRAL UPGRADE EXACT CORE")
print("literature_relax_M2:", M2, ">", Fraction(662816,1000000), "PASS")
print("literature_relax_M3:", M3, ">", Fraction(552792,1000000), "PASS")
print("A2_upper:", A2)
print("A3_upper:", A3)
print("X22_activation_margin_positive:", m22 > 0)
print("X22_activation_margin:", m22)
print("X22_R:", R22)
print("X22_discriminant_positive:", Disc22 > 0, "disc=", Disc22)
print("X22_P_at_100_over_11:", P22)
print("X22_z2_minus_Q:", z22*z22-Q22)
print("X22_ROOT_COMPARISON: PASS")
print("X22_gap_decimal_informational:", gap22d)
print("X34_prior_activation_margin_positive:", m34 > 0)
print("X34_prior_activation_margin:", m34)
print("X34_rational_part_c:", c34)
print("X34_y=z-c:", y34)
print("X34_y2_minus_52:", sq34)
print("X34_ROOT_COMPARISON: PASS")
print("X34_gap_decimal_informational:", gap34d)
print("ALL_EXACT_CHECKS_PASS")

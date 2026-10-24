#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt, pi


def cone_h4(x, y):
    x = Fraction(x)
    y = Fraction(y)
    return Fraction(3, 32) * (19*x*x + 40*x*y + 8*y*y)


# Three-bank coordinate frame.
A_dis = cone_h4(1, 0) + cone_h4(1, 0) + cone_h4(0, 1)
assert A_dis == Fraction(69, 16)

# Four-row fully shared Hadamard frame: x=1/2, y=1/4 per row.
A_had = 4 * cone_h4(Fraction(1, 2), Fraction(1, 4))
assert A_had == Fraction(123, 32)

# Near-optimal split p=3,q=1 frame.
A_split = 3 * cone_h4(Fraction(2, 3), 0) + cone_h4(0, 1)
assert A_split == Fraction(25, 8)
assert 4 * A_split / Fraction(20, 1) == Fraction(5, 8)

gamma_star = (63 + 6*sqrt(38)) / 160
assert gamma_star < 5/8
assert 5/8 - gamma_star < 1e-4

# account04/B18 Schur-pivot theorem applied to
# B=(1/m)[[2/3,-1/3,0],[-1/3,2/3,0],[0,0,-1]].
# det(B)=-1/(3m^3), minority pivot a=-1/m, hence
# 2sqrt(pi)/|a det(B)|^(1/4)=2*3^(1/4)*sqrt(pi)*m.
partner_prefactor = 2 * (3**0.25) * sqrt(pi)
assert 4.66 < partner_prefactor < 4.67

print("PASS")
print("A_disjoint =", A_dis)
print("A_hadamard =", A_had)
print("A_split_3_1 =", A_split)
print("gamma_star =", repr(gamma_star))
print("split_gamma =", 5/8)
print("partner_prefactor =", repr(partner_prefactor))

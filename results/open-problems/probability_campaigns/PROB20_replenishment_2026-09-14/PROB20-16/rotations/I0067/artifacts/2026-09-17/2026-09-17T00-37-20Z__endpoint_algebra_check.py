#!/usr/bin/env python3
from fractions import Fraction

d = Fraction(3)
delta = Fraction(-1,2)
q = Fraction(6)

lam = d*q/(d-delta*q)
theta = d/q - d/(2*lam)
beta = Fraction(1,2)*(1-delta/Fraction(2)+d/(2*q))
rhs_critical = 1 - d/(2*q) + delta/Fraction(2)
s_critical = d/q - 1

assert lam == 3
assert theta == 0
assert beta == Fraction(3,4)
assert rhs_critical == Fraction(1,2)
assert s_critical == Fraction(-1,2)

parenthesis = 2 + delta - d/q
assert parenthesis == 1

heat_exp = Fraction(1,2) + d/Fraction(2)*(Fraction(1,3)-Fraction(1,6))
assert heat_exp == Fraction(3,4)

conv_exp = 1 - heat_exp - Fraction(1,2)
assert conv_exp == Fraction(-1,4)
assert conv_exp + Fraction(1,4) == 0

l6_scale = 1 - d/q
assert l6_scale == Fraction(1,2)
assert l6_scale - Fraction(1,2) == 0

ito_effective_B2 = Fraction(1,2) - 1
assert ito_effective_B2 == Fraction(-1,2)

print("status=PASS")
print("d=3 delta=-1/2 q=6")
print("lambda=", lam)
print("theta=", theta)
print("beta=", beta)
print("critical_rhs=", rhs_critical)
print("critical_smoothness=", s_critical)
print("critical_weight_formula=kappa=p/2-1")
print("heat_L3_to_L6_gradient_exponent=", heat_exp)
print("time_convolution_exponent=", conv_exp)
print("weighted_Kato_scaling_exponent=0")
print("ito_wentzell_B2_coefficient=", ito_effective_B2)

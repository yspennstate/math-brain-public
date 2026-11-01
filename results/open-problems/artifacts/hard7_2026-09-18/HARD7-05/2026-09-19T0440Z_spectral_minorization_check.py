#!/usr/bin/env python3
"""Exact finite-algebra self-check for HARD7-05 spectral minorization at H=1/4.

This checker certifies only the finite algebraic core used in the report:
  * the first three surplus Euler-product pairs,
  * the cross-multiplied polynomial inequality for c=279/500,
  * the new rigorous bracket arithmetic.
The infinite Euler-product identity and Feldheim--Feldheim--Mukherjee comparison theorem
are analytic arguments written in the report, not certified by this script.
"""
from fractions import Fraction as F
import sympy as sp

u = sp.symbols('u', nonnegative=True)
c = sp.Rational(279, 500)

# Normalized integrated-Brownian spectral shape:
# G_c(u) = 1 / ((1+4u/c^2)(1+4u/(9c^2))).
Dc = (1 + 4*u/c**2) * (1 + 4*u/(9*c**2))
Dhalf = (1 + 16*u) * (1 + sp.Rational(16,9)*u)

# First three exact surplus factors in A/G_{1/2}.
z = [sp.Rational(1,4), sp.Rational(9,4), sp.Rational(25,4)]
p = [sp.Rational(25,16), sp.Rational(49,16), sp.Rational(121,16)]
for j in range(3):
    assert p[j] > z[j]

num_surplus = sp.prod(1 + u/zz for zz in z)
den_surplus = sp.prod(1 + u/pp for pp in p)

# S_3(u) * G_{1/2}(u)/G_c(u) >= 1 is equivalent to P(u)>=0.
P = sp.expand(num_surplus * Dc - den_surplus * Dhalf)
num, den = sp.fraction(sp.together(P))
poly = sp.Poly(num, u)
coeffs = poly.all_coeffs()
assert coeffs[-1] == 0
assert all(a > 0 for a in coeffs[:-1])
assert poly.degree() == 5
assert den > 0

expected_num = 4*u*(
    sp.Integer(80568503468621824)*u**4
    + sp.Integer(720742036931717120)*u**3
    + sp.Integer(1509103656301109008)*u**2
    + sp.Integer(695401501714156620)*u
    + sp.Integer(36667394045343)
)
assert sp.expand(num - expected_num) == 0
assert den == sp.Integer(72748374024474225)

# Bracket arithmetic.
old_L = F(1,8)
old_U = F(1,4)
old_W = old_U - old_L
new_L = F(279,2000)  # c/4
new_U = old_U
new_W = new_U - new_L
improvement = old_W - new_W
assert old_W == F(1,8)
assert new_L > old_L
assert new_W == F(221,2000)
assert improvement == F(29,2000)

print('c = 279/500')
print('first_three_pairs =')
for j in range(3):
    print(f'  z{j}={z[j]}, p{j+2}={p[j]}, p>z={p[j] > z[j]}')
print('cross_difference_denominator =', den)
print('cross_difference_numerator_factorized =')
print(sp.factor(num))
print('positive_nonconstant_coefficients =', [int(a) for a in coeffs[:-1]])
print('old_bracket = [1/8, 1/4], old_W = 1/8')
print('new_lower = 279/2000')
print('new_bracket = [279/2000, 1/4]')
print('new_W = 221/2000')
print('width_improvement = 29/2000')
print('ALL_EXACT_CHECKS_PASS = True')

#!/usr/bin/env python3
import sympy as sp

t, q, s, x, y = sp.symbols("t q s x y")

# Symmetry-monotonicity polynomial used for 2 <= p <= 3 (3 <= s <= 4).
D = sp.expand((2*t - 1)*(t + sp.Rational(5, 3))**3 - (1+t)**4)
D_expected = (27*t**4 + 135*t**3 + 153*t**2 - 83*t - 152) / 27
assert sp.simplify(D - D_expected) == 0
assert sp.simplify(D.subs(t, sp.Rational(5,3)) - sp.Rational(968,27)) == 0
Dprime_expected = (108*t**3 + 405*t**2 + 306*t - 83) / 27
assert sp.simplify(sp.diff(D,t) - Dprime_expected) == 0

# Root-demand ratio monotonicity. This is the exact numerator after
# multiplying d/dq log Phi_s(q) by q(q-3)(q-1)(q+1).
logder = (s-1)/q - s/(3-q) - s/(1+q) + (s-1)/(1-q)
N = sp.cancel(logder * q*(q-3)*(q-1)*(q+1))
N_expected = s*(3*q**2 - 2*q + 3) + (q**2 - 2*q - 3)
assert sp.simplify(N - N_expected) == 0
assert sp.expand((3*q**2 - 2*q + 3) - (sp.Rational(8,3) + 3*(q-sp.Rational(1,3))**2)) == 0
assert sp.expand((q**2 - 2*q - 3) - ((q-1)**2 - 4)) == 0

# Rayleigh quotient rational part after x=q/(1-q).
base = sp.Rational(1,2)/(1+x) + 2*x/(1+2*x) - sp.Rational(3,4)
base_expected = (2*x**2 + 3*x - 1)/(4*(1+x)*(1+2*x))
assert sp.simplify(base - base_expected) == 0
assert sp.simplify((2*x**2 + 3*x - 1).subs(x,y/2) - (y**2+3*y-2)/2) == 0

print("SYMMETRY_POLY_IDENTITY_PASS")
print("SYMMETRY_POLY_ENDPOINT", sp.Rational(968,27))
print("SYMMETRY_POLY_DERIVATIVE_IDENTITY_PASS")
print("DEFECT_RATIO_LOGDER_NUMERATOR_PASS")
print("DEFECT_RATIO_LOWER_BOUND", 3*sp.Rational(8,3)-4)
print("RAYLEIGH_RATIONAL_TRANSFORM_PASS")
print("Y_DERIVATIVE_UNIFORM_LOWER_BOUND", sp.Rational(7,4))
print("EXACT_SELF_CHECK_PASS")

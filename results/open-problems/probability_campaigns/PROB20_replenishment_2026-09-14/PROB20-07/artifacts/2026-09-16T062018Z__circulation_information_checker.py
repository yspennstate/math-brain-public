#!/usr/bin/env python3
"""Exact symbolic checks for PROB20-07 run 2026-09-16T062018Z."""
import sympy as sp

a = sp.Rational(1, 12)
b = sp.Rational(3, 4)

u, v, r = sp.symbols("u v r", real=True)
F = (sp.Rational(1, 2) - a) * v + a * u + b * u**2 / 2 - a / 2
assert sp.simplify(
    F - sp.Rational(1, 6) - (9*u**2 + 2*u + 10*v - 5) / 24
) == 0

U = r * (9*r + 2) / 10
factor = sp.factor(9*U**2 + 8*U - 10*r)
assert sp.simplify(
    factor
    - 3*r*(243*r**3 + 108*r**2 + 252*r - 280) / 100
) == 0

h = 243*r**3 + 108*r**2 + 252*r - 280
assert sp.diff(h, r) == 729*r**2 + 216*r + 252
assert h.subs(r, sp.Rational(1, 4)) == -sp.Rational(13213, 64)

x1, x2, x3 = sp.symbols("x1 x2 x3", positive=True)
H = 1/x1 + 1/x2 + 1/x3
const = 3*a + sp.Rational(3, 2) + b/2
assert const == sp.Rational(17, 8)
assert sp.Rational(17, 8) - sp.Rational(9, 24) == sp.Rational(7, 4)

p = x1*x2*x3
skew_sq = sp.Rational(1, 4) * (
    1/(x1*x2) + 1/(x2*x3) + 1/(x3*x1)
)
skew_sub = sp.simplify(skew_sq.subs(x3, 1-x1-x2))
target_sub = sp.simplify((1/(4*p)).subs(x3, 1-x1-x2))
assert sp.simplify(skew_sub - target_sub) == 0

prodmin = sp.Rational(1, 6) * sp.Rational(5, 18) * sp.Rational(5, 9)
assert prodmin == sp.Rational(25, 972)
lower_c = sp.sqrt(7*prodmin) / 4
assert sp.simplify(lower_c - 5*sp.sqrt(21)/216) == 0

rho = 2 - 1/b
assert rho == sp.Rational(2, 3)

print("ALL EXACT CIRCULATION/INFORMATION CHECKS PASSED")

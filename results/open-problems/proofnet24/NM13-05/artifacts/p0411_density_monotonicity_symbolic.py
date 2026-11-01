#!/usr/bin/env python3
"""Exact symbolic self-checks for NM13-05 P0411 density monotonicity proof.

This is not a substitute for the written proof. It checks only the algebraic
identities used in the finite d=2 core and the all-dimension margin reduction.
"""
import sympy as sp

u = sp.symbols('u', nonnegative=True, real=True)
Afun = sp.Function('A')
s = sp.sinh(u)
c = sp.cosh(u)
A = Afun(u)
D = 4*A*c**2 + 2*s

# Source closed form has A'(u)=1/(2 cosh u).
Dp = sp.diff(D, u).subs(sp.diff(A, u), 1/(2*c))
Dpp = sp.diff(Dp, u).subs(sp.diff(A, u), 1/(2*c))
assert sp.simplify(Dp - 4*c*(2*A*s + 1)) == 0
assert sp.simplify(Dpp - 8*(A*(2*s**2 + 1) + s)) == 0

B_u = sp.expand((2*Dp**2 - D*Dpp)/16)
B_expected = (4*A**2*s**4 + 2*A**2*s**2 - 2*A**2
              + 4*A*s**3 + 5*A*s + s**2 + 2)
assert sp.simplify(B_u - B_expected) == 0

# Convert x=sinh(u), A=pi/4+atan(x)/2. The lower bound is
# B >= F := 2 - 2 A^2 + 5 A x.
x = sp.symbols('x', nonnegative=True, real=True)
Ax = sp.pi/4 + sp.atan(x)/2
F = 2 - 2*Ax**2 + 5*Ax*x
Fprime = sp.diff(F, x)
Fprime_expected = (Ax*(6 + 10*x**2) + 5*x)/(2*(1+x**2))
assert sp.simplify(Fprime - Fprime_expected) == 0
assert sp.simplify(F.subs(x, 0) - (2 - sp.pi**2/8)) == 0

# General n>=2 dualized margin. If n<=A_local<=2n and
# A_local'<=n/2, Popoviciu gives L''<=n^2/4+n/2 while L'>=n.
n = sp.symbols('n', integer=True, positive=True)
gap = sp.expand(n**2 - (n**2/sp.Integer(4) + n/sp.Integer(2)))
assert sp.factor(gap - n*(3*n-2)/4) == 0

print('PASS: d=2 D_prime identity')
print('PASS: d=2 D_second identity')
print('PASS: d=2 exact 2(D_prime)^2-D D_second reduction')
print('PASS: d=2 F_prime positive-form identity')
print('PASS: d=2 F(0)=2-pi^2/8 identity')
print('PASS: general gap = n(3n-2)/4')
print('NOTE: inequality signs and differentiation-under-integral domination are proved on the report page.')

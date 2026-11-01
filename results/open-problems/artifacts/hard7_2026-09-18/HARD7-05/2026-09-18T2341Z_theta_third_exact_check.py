#!/usr/bin/env python3
"""
Exact algebraic certificate for HARD7-05, run 4.

For H=1/3 and x = exp(-t/9), define

  R(t) = [3(1-x^9)^(8/3) + 8x^9 + 8x^15 - 3 - 3x^24]/(10 x^12),

and the exactly solvable comparison covariance

  K(t) = cosh(8t/9)/cosh(4t/3)
       = x^4 (1+x^16)/(1+x^24).

After clearing positive denominators, R>=K is equivalent to

  F(x) = 3(1+x^24)(1-x^9)^(8/3) + P(x) >= 0,  0<x<=1.

If P>=0 this is immediate. If P<0, cube the positive radical side.
The exact cubic defect

  D(x) = 27(1+x^24)^3(1-x^9)^8 + P(x)^3

factors as x^15 (1-x)^6 Q(x).  Q is reciprocal of degree 108.
Writing y=x+x^{-1}, Q(x)=x^54 q(y), and then z=y-2=(1-x)^2/x,
the polynomial q(z+2) has strictly positive integer coefficients.
Therefore Q(x)>0 for x>0, hence D(x)>0 on 0<x<1.
This proves the strict comparison for t>0.

All checks below are exact symbolic/integer arithmetic.
"""
import sympy as sp
from fractions import Fraction

x, y, z = sp.symbols("x y z")

P = sp.expand(
    (1 + x**24) * (8*x**9 + 8*x**15 - 3 - 3*x**24)
    - 10*x**16 * (1 + x**16)
)

D = sp.expand(
    27 * (1 + x**24)**3 * (1 - x**9)**8
    + P**3
)

Qexpr = sp.cancel(D / (x**15 * (1 - x)**6))
Q = sp.Poly(Qexpr, x, domain=sp.ZZ)

assert sp.expand(D - x**15*(1-x)**6*Q.as_expr()) == 0
assert Q.degree() == 108

# Reciprocal symmetry.
for k in range(109):
    assert Q.nth(k) == Q.nth(108-k)

# Convert reciprocal Q to q(y) with y=x+x^{-1}.
n = 54
S = [sp.Integer(2), y]  # S_k = x^k+x^{-k}
for k in range(2, n+1):
    S.append(sp.expand(y*S[-1] - S[-2]))

q = sp.Integer(Q.nth(n))
for k in range(1, n+1):
    q += Q.nth(n+k) * S[k]
q = sp.Poly(sp.expand(q), y, domain=sp.ZZ)
assert q.degree() == 54

reconstructed = sp.cancel(x**54 * q.as_expr().subs(y, x + 1/x))
assert sp.expand(reconstructed - Q.as_expr()) == 0

qshift = sp.Poly(sp.expand(q.as_expr().subs(y, z + 2)), z, domain=sp.ZZ)
assert qshift.degree() == 54
shift_coeffs = [qshift.nth(k) for k in range(55)]
assert all(c > 0 for c in shift_coeffs)

# Reference persistence exponent:
# m=1/6, c=8/3, theta(K_m(c .)) = c*(3/8)*m = 1/6.
m = Fraction(1, 6)
c = Fraction(8, 3)
theta_ref = c * Fraction(3, 8) * m
assert theta_ref == Fraction(1, 6)

print("P_degree =", sp.Poly(P, x).degree())
print("D_degree =", sp.Poly(D, x).degree())
print("Q_degree =", Q.degree())
print("Q_reciprocal =", True)
print("q_degree =", q.degree())
print("qshift_degree =", qshift.degree())
print("qshift_coeff_count =", len(shift_coeffs))
print("qshift_min_coeff =", min(shift_coeffs))
print("qshift_constant =", qshift.nth(0))
print("qshift_leading =", qshift.nth(54))
print("theta_reference =", f"{theta_ref.numerator}/{theta_ref.denominator}")
print("ALL_EXACT_CHECKS_PASS")

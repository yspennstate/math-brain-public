#!/usr/bin/env python3
"""
Exact finite-arithmetic self-check for HARD7-05.

Special point H=1/5. The analytic proof reduces the all-lag covariance
comparison R_{1/5}(t) >= cosh(12t/5)/cosh(8t/3) to positivity of an
integer reciprocal polynomial. This script certifies the finite algebraic
core exactly over ZZ/QQ; it does not independently audit Slepian's theorem
or Molchan's persistence exponent for the comparison family.
"""
from fractions import Fraction
import sympy as sp

x, y, z = sp.symbols("x y z")

# After x = exp(-t/15), the source/reference comparison is
#   5(1+x^80)(1-x^15)^(12/5) + P(x) >= 0.
P = (1 + x**80) * (12*x**15 + 12*x**21 - 5 - 5*x**36) \
    - 14*x**22*(1 + x**72)

# On the only nontrivial sign region P<0, fifth powers preserve order.
D = 5**5 * (1 + x**80)**5 * (1 - x**15)**12 + P**5
D = sp.Poly(sp.expand(D), x, domain=sp.ZZ)

divisor = sp.Poly(x**21 * (1-x)**10, x, domain=sp.ZZ)
Q, rem = sp.div(D, divisor, domain=sp.ZZ)
assert rem.is_zero
assert Q.degree() == 528

# Exact reciprocity.
coeff = Q.all_coeffs()
assert coeff == list(reversed(coeff))

# Reciprocal reduction Q(x)=x^264 q(x+x^{-1}).
n = 264
assert Q.degree() == 2*n
asc = [Q.nth(i) for i in range(2*n+1)]

S = [sp.Integer(2), y]
for k in range(2, n+1):
    S.append(sp.expand(y*S[-1] - S[-2]))

q_expr = sp.Integer(asc[n])
for k in range(1, n+1):
    assert asc[n-k] == asc[n+k]
    q_expr += asc[n+k] * S[k]
q = sp.Poly(sp.expand(q_expr), y, domain=sp.ZZ)
assert q.degree() == 264

# Direct reconstruction check.
recon = sp.together(x**n * q.as_expr().subs(y, x + 1/x))
num, den = sp.fraction(recon)
assert sp.expand(den - 1) == 0
assert sp.Poly(sp.expand(num - Q.as_expr()), x, domain=sp.ZZ).is_zero

# Translate y=2+z; for x>0, z=x+x^{-1}-2=(sqrt(x)-1/sqrt(x))^2>=0.
qz = sp.Poly(sp.expand(q.as_expr().subs(y, z+2)), z, domain=sp.ZZ)
assert qz.degree() == 264

nonpositive = [(j, int(qz.nth(j))) for j in range(265) if qz.nth(j) <= 0]
assert nonpositive == [(1, int(qz.nth(1)))]

a0 = int(qz.nth(0))
a1 = int(qz.nth(1))
a2 = int(qz.nth(2))
disc = a1*a1 - 4*a0*a2
assert a0 > 0 and a1 < 0 and a2 > 0 and disc < 0
assert all(qz.nth(j) > 0 for j in range(2, 265))

# Exact reference tuning and endpoint margins.
H = Fraction(1,5)
m = Fraction(1,20)
qrate = Fraction(4,3)*H
c = qrate/m
theta_ref = c*Fraction(3,8)*m
g = ((16 - 7*m)*H*H - 9*m)/(18*m)

assert qrate == Fraction(4,15)
assert c == Fraction(16,3)
assert theta_ref == Fraction(1,10)
assert g == Fraction(44,225) > 0

print("D_degree =", D.degree())
print("factor_x_power =", 21)
print("factor_one_minus_x_power =", 10)
print("Q_degree =", Q.degree())
print("Q_reciprocal =", True)
print("q_degree =", q.degree())
print("q_shift_degree =", qz.degree())
print("nonpositive_shift_coefficients =", nonpositive)
print("a0 =", a0)
print("a1 =", a1)
print("a2 =", a2)
print("quadratic_discriminant =", disc)
print("min_coefficient_j_ge_2 =", min(int(qz.nth(j)) for j in range(2,265)))
print("qrate =", qrate)
print("c =", c)
print("theta_reference =", theta_ref)
print("small_lag_margin_g =", g)
print("ALL_EXACT_CHECKS_PASS")

#!/usr/bin/env python3
"""
R19 / I0084 exact self-check for C014-C016.

Checks exact algebra extracted from Hasebe-Kuznetsov Theorem 2, formula (17),
for symmetric free stable curvature, and the rational identity behind the
strict monotonicity of the symmetric boundary parametrization.

This is a self-check, not an independent audit.
"""
from fractions import Fraction
import sympy as sp

a = sp.symbols("a", positive=True)
u, v = sp.symbols("u v", positive=True)
b = 1-a

# Hasebe-Kuznetsov formula (17), n=3 term.
gamma_ratio = sp.expand_func(sp.gamma(1 + 3/a) / sp.gamma(3/a - 1))
expected_ratio = 3*(3-a)/a**2
assert sp.simplify(gamma_ratio - expected_ratio) == 0
x2_coeff_times_pi = -gamma_ratio / sp.factorial(3)
fpp_times_pi = sp.simplify(2*x2_coeff_times_pi)
expected_fpp_times_pi = -(3-a)/a**2
assert sp.simplify(fpp_times_pi - expected_fpp_times_pi) == 0

# Exact rational identity used to prove x'(theta)<0 in the symmetric
# Hasebe-Kuznetsov boundary parametrization. With u=cot(theta),
# v=cot(A), beta=1-alpha, q=theta+A and cot(q)=(uv-1)/(u+v):
# alpha (x'/x) = -alpha^2 v + beta^2 cot(q) - u.
monotone_numerator = sp.expand(
    (-a**2*v + b**2*(u*v-1)/(u+v) - u)*(u+v)
)
monotone_target = -((u+a*v)**2 + b**2)
assert sp.simplify(monotone_numerator - monotone_target) == 0

# n=1 term is exactly 1/pi; n=2 term vanishes by symmetry.
n1_ratio = sp.expand_func(sp.gamma(1 + 1/a) / sp.gamma(1 + 1/a))
assert sp.simplify(n1_ratio - 1) == 0
assert sp.sin(sp.pi) == 0

expected = {
    Fraction(1,2): Fraction(-10,1),
    Fraction(2,3): Fraction(-21,4),
    Fraction(3,4): Fraction(-4,1),
    Fraction(4,5): Fraction(-55,16),
    Fraction(9,10): Fraction(-70,27),
}
for alpha, target in expected.items():
    got = -(3-alpha)/(alpha*alpha)
    assert got == target, (alpha, got, target)

alpha = Fraction(4,5)
p = Fraction(2,1) + alpha
threshold_exponent = alpha / p
assert p == Fraction(14,5)
assert threshold_exponent == Fraction(2,7)
assert -(3-alpha)/(alpha*alpha) == Fraction(-55,16)
assert sp.limit(expected_fpp_times_pi, a, 1, dir="-") == -2

print("R19 I0084 C014-C016 exact self-check")
print("PASS gamma ratio =", gamma_ratio)
print("PASS pi*f''_{alpha,1/2}(0) =", expected_fpp_times_pi)
print("PASS monotonicity identity =", sp.factor(monotone_numerator))
for alpha, target in expected.items():
    print(f"PASS alpha={alpha}: pi*f''(0)={target}")
print("PASS alpha=4/5 source moment exponent p=14/5")
print("PASS alpha=4/5 semigroup threshold exponent alpha/p=2/7")
print("PASS alpha->1- gives pi*f''(0)->-2 (Cauchy consistency)")
print("PASS")

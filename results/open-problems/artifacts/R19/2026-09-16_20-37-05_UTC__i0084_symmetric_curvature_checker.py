#!/usr/bin/env python3
"""
R19 / I0084 exact self-check for C014-C015.

Checks only exact algebra extracted from Hasebe-Kuznetsov Theorem 2,
formula (16), for the symmetric free stable law rho=1/2.

This is a self-check, not an independent audit.
"""
from fractions import Fraction
import sympy as sp

a = sp.symbols("a", positive=True)

# Hasebe-Kuznetsov formula (16), n=3 term:
# a_3 = (1/pi) * Gamma(1+3/a)/(3!*Gamma(2+3(1/a-1)))
#       * sin(3*pi/2).
gamma_ratio = sp.expand_func(sp.gamma(1 + 3/a) / sp.gamma(3/a - 1))
expected_ratio = 3*(3-a)/a**2
assert sp.simplify(gamma_ratio - expected_ratio) == 0

# The Taylor coefficient of x^2 and the second derivative at zero.
x2_coeff_times_pi = -gamma_ratio / sp.factorial(3)
fpp_times_pi = sp.simplify(2*x2_coeff_times_pi)
expected_fpp_times_pi = -(3-a)/a**2
assert sp.simplify(fpp_times_pi - expected_fpp_times_pi) == 0

# n=1 term is exactly 1/pi; n=2 term vanishes by symmetry.
n1_ratio = sp.expand_func(sp.gamma(1 + 1/a) / sp.gamma(1 + 1/a))
assert sp.simplify(n1_ratio - 1) == 0
assert sp.sin(sp.pi) == 0

# Exact rational spot-checks: these values are pi*f''(0).
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

# The requested simplest special case alpha=4/5.
alpha = Fraction(4,5)
p = Fraction(2,1) + alpha
threshold_exponent = alpha / p
assert p == Fraction(14,5)
assert threshold_exponent == Fraction(2,7)
assert -(3-alpha)/(alpha*alpha) == Fraction(-55,16)

# Consistency with the symmetric Cauchy limit alpha -> 1-.
assert sp.limit(expected_fpp_times_pi, a, 1, dir="-") == -2

print("R19 I0084 C014-C015 exact self-check")
print("PASS gamma ratio =", gamma_ratio)
print("PASS pi*f''_{alpha,1/2}(0) =", expected_fpp_times_pi)
for alpha, target in expected.items():
    print(f"PASS alpha={alpha}: pi*f''(0)={target}")
print("PASS alpha=4/5 source moment exponent p=14/5")
print("PASS alpha=4/5 semigroup threshold exponent alpha/p=2/7")
print("PASS alpha->1- gives pi*f''(0)->-2 (Cauchy consistency)")
print("PASS")

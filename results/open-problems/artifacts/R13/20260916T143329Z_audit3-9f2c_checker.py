#!/usr/bin/env python3
"""
R13 Komlos run 3 exact-arithmetic self-check.

Finite algebra only. This certifies:
  (1) the exact finite-sum identity used in the R16 Beck-Fiala audit;
  (2) the exact constants in the Guo-Fang-Lu retained-height estimate at L=3;
  (3) the threshold formula 3(L-2)/L^2 at L=3.

It does NOT replace the analytic BV/Finsler proof and is not an independent audit.
"""
from fractions import Fraction
from math import factorial

print("R13 run-3 exact checker")

# Identity:
# sum_{r=0}^{t-1} binom(t-1,r) r! / t^r
# = (t-1)! / t^(t-1) * sum_{j=0}^{t-1} t^j/j!
for t in range(1, 101):
    lhs = sum(
        Fraction(factorial(t-1), factorial(t-1-r) * (t**r))
        for r in range(t)
    )
    rhs = Fraction(factorial(t-1), t**(t-1)) * sum(
        Fraction(t**j, factorial(j)) for j in range(t)
    )
    assert lhs == rhs, (t, lhs, rhs)
print("finite-sum identity t=1..100: PASS")

# Exact retained-height constants for the GFL lift with vertical half-width L=3.
# baseline = (1/(4L)) * 2 * int_0^(2L) (2L-h) dh = L/2.
# loss under ||rho-rho_h||_1 <= h V is
# (1/(4L)) * int_0^(2L) (2L-h) h dh * V = (L^2/6) V.
L = Fraction(3,1)
baseline = L / 2
loss_coefficient = L*L / 6
threshold_V = Fraction(3,1)*(L-Fraction(2,1))/(L*L)

assert baseline == Fraction(3,2)
assert loss_coefficient == Fraction(3,2)
assert threshold_V == Fraction(1,3)
assert baseline - loss_coefficient*threshold_V == Fraction(1,1)

print("GFL L=3 baseline height = 3/2: PASS")
print("GFL L=3 variation-loss coefficient = 3/2: PASS")
print("GFL height-one threshold V = 1/3: PASS")

# Integral constants in the source normalization:
# int_0^6 (6-h) dh = 18, int_0^6 h(6-h) dh = 36.
I0 = Fraction(6*6,2)
I1 = Fraction(6*6*6,6)
assert I0 == 18
assert I1 == 36
assert Fraction(I0,12) == Fraction(3,2)
assert Fraction(I1,24) == Fraction(3,2)
print("source-normalization integrals 18 and 36: PASS")

# Print exact rational coefficient A_t in E|S_t|=(2/pi) A_t and
# R_t = 6 A_t for t=1..10.
print("t, A_t, R_t=6*A_t")
for t in range(1,11):
    A = Fraction(factorial(t), t**t) * sum(
        Fraction(t**j, factorial(j)) for j in range(t)
    )
    R = 6*A
    print(t, A, R)

print("PASS")

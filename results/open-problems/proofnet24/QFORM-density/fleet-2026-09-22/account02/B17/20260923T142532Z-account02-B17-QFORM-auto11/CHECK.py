from math import pi, sqrt

K = (pi / 2.0) * (sqrt(2.0) + 2.0 ** 0.25)
target = 3.0 * sqrt(2.0)

# Exact rational certificate used in the report:
# 2^(-1/4) < 10/11 iff 11^4 < 2*10^4.
assert 11**4 < 2 * 10**4
# Together with pi < 22/7 this gives
# K/sqrt(2) < (11/7)*(1+10/11) = 3.
from fractions import Fraction
assert Fraction(11, 7) * (1 + Fraction(10, 11)) == 3
assert K < target

print("PASS QFORM-UNEQUAL-OPPOSITE-CUBE-BANKS-BARRIER-v1")
print(f"K_star={K:.15f}")
print(f"3sqrt2={target:.15f}")
print(f"gap={target-K:.15f}")

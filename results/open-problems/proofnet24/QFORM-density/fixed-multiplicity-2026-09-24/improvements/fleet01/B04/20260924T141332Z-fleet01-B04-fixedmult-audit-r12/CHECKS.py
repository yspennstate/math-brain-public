from fractions import Fraction
from math import factorial

# Exact arithmetic certificates for QFORM-FIXED-MULTIPLICITY-9-2510-v1.

# 1. Gamma/Stirling certificate.
# DLMF 5.6.1 at x=19/8 plus Gamma(3/8)=64/33 Gamma(19/8) gives
# C_q^8 < [4096*19^15*pi^2/33^8] exp(-896/57).
# With pi<22/7 and exp(x) > sum_{k=0}^33 x^k/k!, prove C_q < 7993/2000.
x = Fraction(896, 57)
S33 = sum(x**k / factorial(k) for k in range(34))
prefactor = Fraction(4096, 1) * 19**15 * Fraction(22, 7)**2 / 33**8
cq_bound = Fraction(7993, 2000)
assert prefactor < cq_bound**8 * S33

# 2. log 2 < 1733/2500 by a positive Taylor partial sum.
log2_upper = Fraction(1733, 2500)
E6 = sum(log2_upper**k / factorial(k) for k in range(7))
assert E6 > 2

# 3. log(7993/2000) < 2771/2000, hence log C_q < 2771/2000.
logcq_upper = Fraction(2771, 2000)
E8 = sum(logcq_upper**k / factorial(k) for k in range(9))
assert E8 > cq_bound

# 4. Complete outer scalar-pivot constant.
# C_scalar < 810 +100*pi +400 log2 +800 log C_q.
# Use pi<22/7 and the two logarithm certificates above.
C_scalar = (
    Fraction(810, 1)
    + 100 * Fraction(22, 7)
    + 400 * log2_upper
    + 800 * logcq_upper
)
assert C_scalar == Fraction(439244, 175)
assert C_scalar < 2510
assert Fraction(2510, 1) - C_scalar == Fraction(6, 175)

print("QFORM_B04_R12_2510_CHECK_PASS")
print("S33_float", float(S33))
print("gamma_threshold_float", float(prefactor / cq_bound**8))
print("E6_minus_2", float(E6 - 2))
print("E8_minus_cq_bound", float(E8 - cq_bound))
print("scalar_constant", C_scalar, float(C_scalar))
print("margin_to_2510", Fraction(2510, 1) - C_scalar, float(Fraction(2510, 1) - C_scalar))

from fractions import Fraction
import math

rho = Fraction(1, 12)
lP = Fraction(1, 4) - rho
lN = Fraction(1, 4) - rho / 2
detcoef = 4 * lP * lN

assert lP == Fraction(1, 6)
assert lN == Fraction(5, 24)
assert detcoef == Fraction(5, 36)
assert rho / lP == Fraction(1, 2)
assert rho / lN == Fraction(2, 5)

# For tau >= 1/3, the proof gives
# sigma(tau) >= (5 tau/36)/sqrt(1+tau^2/144), which is increasing.
tau = Fraction(1, 3)
sigma0 = (5 * float(tau) / 36) / math.sqrt(1 + float(tau * tau) / 144)
sigma_exact = 5 / (3 * math.sqrt(1297))
assert abs(sigma0 - sigma_exact) < 1e-15

high = 14.34 / math.sqrt(sigma0)
low_opposite = 50 * (3 / 2) ** (3 / 4)
low_same = math.pi * math.sqrt(3)

assert high < 67
assert low_opposite < 68
assert low_same < 6

print("rho=", float(rho))
print("lP=", float(lP), "lN=", float(lN), "detcoef=", float(detcoef))
print("row-range leverage caps=", float(rho / lP), float(rho / lN))
print("sigma0=", repr(sigma0))
print("high_branch_bound<", repr(high))
print("low_opposite_bound<", repr(low_opposite))
print("low_same_bound<", repr(low_same))
print("QFORM_B08_RANK2_BANK_CHECK_PASS")

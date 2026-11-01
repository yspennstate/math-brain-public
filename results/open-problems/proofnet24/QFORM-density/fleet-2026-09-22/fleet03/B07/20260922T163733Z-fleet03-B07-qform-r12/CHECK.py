from fractions import Fraction
from math import comb, e, sqrt

# Exact overlap-class averaging constants.
assert Fraction(1, 4) * Fraction(1, 64) == Fraction(1, 256)
assert Fraction(1, 4) * Fraction(1, 243) == Fraction(1, 972)
assert Fraction(1, 4) * Fraction(1, 81) == Fraction(1, 324)

# The Bernoulli proof uses C(m,3) >= m-2 for every integer m >= 0.
for m in range(500):
    assert comb(m, 3) >= m - 2

# Exponent bookkeeping in the ridge payment:
# gamma^{-1} (gamma^6/E)^{3/16}, together with gamma^6 <= (3/2)E,
# yields E^{-1/6} and multiplier 2 sqrt(2) e (3/2)^{1/48}.
assert Fraction(-1, 1) + Fraction(18, 16) == Fraction(1, 8)
assert Fraction(-3, 16) + Fraction(1, 48) == Fraction(-1, 6)

constant_E_1_256 = 2 * sqrt(2) * e * (Fraction(3, 2)) ** (1 / 48) * 256 ** (1 / 6)
assert constant_E_1_256 < 19.54
print(f"overlap_constants=PASS")
print(f"bernoulli_integer_inequality=PASS")
print(f"ridge_exponents=PASS")
print(f"O0_bound_at_E=1/256: {constant_E_1_256:.12f} < 19.54")

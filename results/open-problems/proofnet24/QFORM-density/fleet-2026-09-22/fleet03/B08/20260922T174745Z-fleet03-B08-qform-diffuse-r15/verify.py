from fractions import Fraction
from math import e, sqrt

# Scalar threshold checks in Lemma 4.1.
assert Fraction(5, 8) < Fraction(2, 3)
assert 32 / (9 * sqrt(3)) > Fraction(16, 9)

# Fractional-ridge exponent check: beta >= 8/15, s=19/10.
assert Fraction(8, 15) * Fraction(19, 10) == Fraction(76, 75)
assert Fraction(76, 75) > 1

# Explicit constant in Theorem 6.1.
C = (20 ** (10 / 19) + 1) * sqrt(152 * sqrt(6 * e / 5))
assert C < 97

print(f"C_5_6={C:.15f}")
print("QFORM_TRANSVERSE_5_6_CHECK_PASS")

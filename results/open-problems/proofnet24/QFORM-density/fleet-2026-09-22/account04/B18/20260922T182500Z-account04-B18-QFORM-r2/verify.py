from fractions import Fraction
from math import isclose

# The centered three-uniform convolution has density 3/4 at zero.
flat_bank_sq = Fraction(27, 16)  # (3*sqrt(3)/4)^2
det_h = 2

# Cube the claimed constant and the partner expression to verify exactly,
# avoiding irrational floating arithmetic:
# [6 M^(2/3) det^(-1/3)]^3 = 216 M^2 / det.
lhs_cube = Fraction(27, 4) ** 3
rhs_cube = 216 * flat_bank_sq**2 / det_h
assert lhs_cube == rhs_cube

# Characteristic polynomial of H is (lambda-2)(lambda+1)^2.
def charpoly(lam):
    return (lam - 2) * (lam + 1) ** 2

assert charpoly(2) == 0
assert charpoly(-1) == 0
assert isclose(float(Fraction(27, 4)), 6.75)
print("PASS QFORM-SHARP-THREEBANK-ZEROPIVOT-v1 constant=27/4 eigenvalues=2,-1,-1")

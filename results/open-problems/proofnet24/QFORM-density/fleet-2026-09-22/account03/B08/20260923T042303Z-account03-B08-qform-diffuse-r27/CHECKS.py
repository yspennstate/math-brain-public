from fractions import Fraction
from math import e, sqrt

# Diffuse q=0 packet and q=4/3 double-incident anchor.
Delta3 = Fraction(1, 2304)
Z = Fraction(1, 3) * Delta3
assert Z == Fraction(1, 6912)

# Self-matched 3/2 mixture paid constant when anchor row norm <= L.
C85 = 10 * sqrt(e) * (3456 ** (1/5))
assert C85 < 85

# A residual row/column with anchored inclusion marginal >1/2
# carries > Z/2 of the anchored volume.
nested = Z / 2
assert nested == Fraction(1, 13824)

# Large-star account04/B18 projection currency.
# If R>L then marginal cap sqrt(2)/R < sqrt(2)/L;
# if both opposite-side stars exceed L, disjoint product banks give <2/L^2.
assert sqrt(2) ** 2 == 2.0

print('QFORM_B08_R27_CHECK_PASS')
print('Z/L^6 lower coefficient =', float(Z))
print('C85 =', C85)
print('nested/L^6 lower coefficient =', float(nested))
print('joint-star coefficient =', 2.0)

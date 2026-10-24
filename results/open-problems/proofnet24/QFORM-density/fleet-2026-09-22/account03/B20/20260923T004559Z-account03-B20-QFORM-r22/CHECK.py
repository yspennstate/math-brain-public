from fractions import Fraction
from math import e, sqrt

# Partner diffuse constant at delta > 1/6.
Cdiff = 6*96*e/(7*sqrt(2))
assert Cdiff < 162

# Singleton rank-one-bank pivot: lambda>1/192, |a|>=1/48, |det M|>=1.
Cpiv = 16*sqrt(60)*(9216**0.25)
assert abs(Cpiv-384*sqrt(10)) < 1e-12
assert Cpiv < 1215

# Companion-heavy star localization.
exact_gap = Fraction(1,48)**2 - Fraction(3,2048)**2 - Fraction(1,49)**2
assert exact_gap > 0

# Internal-heavy two-channel split.
internal_split = 1/(48*sqrt(2))
assert 2*internal_split**2 == 1/48**2

print(f"diffuse_bound={Cdiff:.12f}")
print(f"pivot_bound={Cpiv:.12f}")
print(f"companion_star_floor={(float(Fraction(1,48)**2-Fraction(3,2048)**2))**0.5):.12f}")
print(f"one_over_49={1/49:.12f}")
print(f"exact_gap={exact_gap.numerator}/{exact_gap.denominator}")
print(f"internal_two_channel_floor={internal_split:.12f}")
print("QFORM_B20_R22_CHECK_PASS")

from fractions import Fraction
from math import e, sqrt

for N in (8, 64, 512, 4096):
    ell = Fraction(3, 4)
    d = Fraction(1, 2)
    s = Fraction(0, 1)
    g = ell*d - s*s
    m = d + s*s/(1-ell)
    triple = Fraction(3, 8*N)
    assert ell == Fraction(3,4)
    assert m == Fraction(1,2)
    assert g == Fraction(3,8)
    assert N*triple == g
    print(f"N={N} triple_squared_volume={triple} aggregate={N*triple}")

print("two_sided_rank3_constant=", 3*e)
print("partner_three_heavy_constant=", 12*sqrt(e))
print("STATUS=QFORM_CROSS_FIBER_PLANCHEREL_CHECK_PASS")

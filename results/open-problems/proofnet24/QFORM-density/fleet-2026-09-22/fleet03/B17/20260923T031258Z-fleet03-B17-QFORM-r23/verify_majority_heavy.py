from fractions import Fraction
from math import factorial
import mpmath as mp

# Exact arithmetic certificate for the one-heavy majority-sign theorem.


def P5(x: Fraction) -> Fraction:
    return x - Fraction(2, 3) * x**3 + Fraction(4, 15) * x**5

# 1. Comparison-function forcing sign for R(z).
# c=4/pi <= 200/157 from pi>=157/50.  At z>=2/5 it is enough
# to check (c-1)^2(z^2+c) <= z^2 at the endpoint and upper c.
cU = Fraction(200, 157)
zmin = Fraction(2, 5)
forcing_lhs = (cU - 1) ** 2 * (zmin**2 + cU)
forcing_rhs = zmin**2
assert forcing_lhs < forcing_rhs

# 2. Exact rational enclosure on 2/5 <= z <= 1.
# Since pi<22/7, c=4/pi > 14/11.  Hence
# R(z) <= 1/(z+sqrt(z^2+14/11)).
# D(z) <= P5(z) for z<=1.  On each interval of width 1/40,
# monotonicity gives D(z)+R(z) <= P5(b)+r(a).  Certify
# this is <1021/1000 without floating point by squaring.
cap = Fraction(1021, 1000)
cL = Fraction(14, 11)
for k in range(24):
    a = Fraction(2, 5) + Fraction(k, 40)
    b = a + Fraction(1, 40)
    q = cap - P5(b)
    assert q > 0
    rhs = Fraction(1, 1) / q - a
    if rhs > 0:
        assert a * a + cL > rhs * rhs

# 3. The middle bound lies below the global small-z target
# 29*sqrt(pi)/50, already using pi>157/50.
assert cap**2 < Fraction(29, 50) ** 2 * Fraction(157, 50)

# 4. Large-z elementary certificates.
# sqrt(6)/4 < 613/1000, r(1)<2/5, and r(3/2)<3/10.
assert Fraction(6, 16) < Fraction(613, 1000) ** 2
assert Fraction(25, 11) > Fraction(3, 2) ** 2
assert Fraction(155, 44) > Fraction(11, 6) ** 2

# 5. Analytic strict comparison C_major < 3*sqrt(2).
# Stirling at x=5/4 reduces the comparison to
# exp(71/15)>1682/15.  The degree-10 positive Taylor sum
# is already larger, an exact rational certificate.
x = Fraction(71, 15)
exp_lower = sum(x**k / Fraction(factorial(k), 1) for k in range(11))
assert exp_lower > Fraction(1682, 15)

# Diagnostic values only; none of the assertions above depends on them.
mp.mp.dps = 50
I0 = mp.gamma(mp.mpf(1) / 4) ** 2 * mp.sqrt(3) / (2 * mp.pi)
C_major = mp.mpf(29) / 25 * I0
C_partner = 3 * mp.sqrt(2)
print("QFORM_B17_MAJORITY_HEAVY_CHECK_PASS")
print("forcing_margin_exact", forcing_rhs - forcing_lhs)
print("exp_taylor_margin_exact", exp_lower - Fraction(1682, 15))
print("I0", mp.nstr(I0, 30))
print("C_major", mp.nstr(C_major, 30))
print("3sqrt2", mp.nstr(C_partner, 30))
print("gap", mp.nstr(C_partner - C_major, 30))

from fractions import Fraction
import sympy as sp

p = sp.symbols("p", positive=True)
q = 1 - p
h = -p * sp.log(p) - q * sp.log(q)

# Old weights (1,2) have four distinct subset sums, hence H_old = 2 h(p).
# For new weights (1,1,2), the entropy loss from the collision-free 3h(p) law is
#   2 p(1-p) log 2 + p(1-p) h(p).
# Therefore the one-step entropy increment is
#   I(p)=H_(1,1,2)(p)-H_(1,2)(p)
#       =h(p)-2p(1-p)log2-p(1-p)h(p).
I = sp.simplify(h - 2 * p * q * sp.log(2) - p * q * h)
I2_at_third = sp.simplify(sp.diff(I, p, 2).subs(p, sp.Rational(1, 3)))
target = sp.log(36) - sp.Rational(7, 2)
assert sp.simplify(I2_at_third - target) == 0

# Rigorous positivity with exact rational arithmetic only.
# e = sum_{k>=0}1/k! < 8/3 + (1/24) sum_{j>=0}(1/5)^j = 87/32 < 11/4.
e_upper = Fraction(87, 32)
coarse_upper = Fraction(11, 4)
assert e_upper < coarse_upper

# Hence e^7 < (11/4)^7 < 36^2, so 7 < 2 log 36 and log 36 > 7/2.
power_upper = coarse_upper ** 7
power_target = Fraction(36**2, 1)
assert power_upper < power_target

print("SYMBOLIC_IDENTITY:", I2_at_third)
print("E_UPPER_BOUND:", e_upper, "<", coarse_upper)
print("POWER_CHECK:", power_upper, "<", power_target)
print("CONCLUSION: I''(1/3) = log(36) - 7/2 > 0")
print("PASS")

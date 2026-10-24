from fractions import Fraction
from math import sqrt

cx = Fraction(41413921384333, 62139940601856)
c0 = Fraction(6221, 6450)
rho2 = Fraction(329, 1609088)

assert cx > Fraction(16, 25)
assert rho2 < Fraction(9, 40000)

simple = Fraction(4, 5) * (c0 - Fraction(3, 200))
assert simple == Fraction(24497, 32250)
assert simple > Fraction(3, 4)
assert simple**2 > Fraction(9, 16)

print("x1x2 lower =", float(cx))
print("sqrt tail-ratio-square upper =", sqrt(float(rho2)))
print("rational grouped determinant factor =", simple, float(simple))
print("margin over 3/4 =", simple - Fraction(3, 4))
print("squared factor =", float(simple**2))
print("margin over 9/16 =", simple**2 - Fraction(9, 16))
print("exact composite (without rational relaxations) =", sqrt(float(cx)) * (float(c0) - sqrt(float(rho2))))
print("QFORM_ACTUAL_BICOLOOP_GROUPED_MINOR_CHECK_PASS")

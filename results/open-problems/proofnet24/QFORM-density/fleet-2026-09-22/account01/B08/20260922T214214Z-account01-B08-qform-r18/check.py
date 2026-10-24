from fractions import Fraction
from math import sqrt

s0 = Fraction(329, 3218176)
L0 = Fraction(6221, 6450)
x0 = Fraction(2, 3) - 2*s0 - s0*s0/Fraction(2,1)
rho2 = 4*s0 + 2*s0*s0
q = Fraction(59,100)
D = L0*L0 + rho2 - q/x0
gap = D*D - 4*L0*L0*rho2

assert x0 == Fraction(41413921384333, 62139940601856)
assert D > 0
assert gap > 0
assert L0*L0 > rho2

lower = (float(L0)-sqrt(float(rho2)))**2 * float(x0)
print('s0 =', s0, float(s0))
print('L0 =', L0, float(L0))
print('x0 =', x0, float(x0))
print('rho^2 =', rho2, float(rho2))
print('rho =', sqrt(float(rho2)))
print('D =', D, float(D))
print('D^2-4L0^2rho^2 =', gap, float(gap))
print('certified lower numerical value =', lower)
assert lower > 0.59
print('QFORM_B08_R18_FULL_EXTERIOR_BANK_CHECK_PASS')

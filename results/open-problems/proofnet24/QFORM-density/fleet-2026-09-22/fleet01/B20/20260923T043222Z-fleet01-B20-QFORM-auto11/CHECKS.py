from fractions import Fraction
from math import sqrt, e

W0 = Fraction(1,331776)
delta = Fraction(4,27)*W0
epsilon = delta/Fraction(12288,1)
assert delta == Fraction(1,2239488)
assert epsilon == Fraction(1,27518828544)
assert epsilon/3 == Fraction(1,82556485632)
assert epsilon/12 == Fraction(1,330225942528)
assert 3*epsilon/delta == Fraction(1,4096)
C = 9*sqrt(3*e)*(epsilon.denominator**(1/6))
print('delta =', delta)
print('epsilon =', epsilon)
print('epsilon/3 =', epsilon/3)
print('epsilon/12 =', epsilon/12)
print('3epsilon/delta =', 3*epsilon/delta)
print('diffuse density constant =', repr(C))
assert C < 1412.176
print('QFORM_B20_AUTO11_WEDGE_DISJOINTIZATION_CHECK_PASS')

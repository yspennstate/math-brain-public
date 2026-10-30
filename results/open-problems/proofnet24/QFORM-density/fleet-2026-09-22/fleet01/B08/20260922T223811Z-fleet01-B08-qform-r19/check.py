from fractions import Fraction
from math import e, sqrt

s0 = Fraction(329,3218176)
L0 = Fraction(6221,6450)
lower2 = L0*(1-2*s0-2*s0*s0)
lower3 = L0*(1-s0-Fraction(2,3)*s0*s0)
assert lower2 > Fraction(24,25)
assert lower3 > Fraction(24,25)
assert Fraction(25,48) < Fraction(2,3)

eps = Fraction(1,200)
x = eps*eps
alpha2 = (1+x)/(1+2*x)
assert alpha2 == Fraction(40001,40002)
assert alpha2 > Fraction(3,4)

# source-scale ridge data for H=diag(1,1,eps), g=1/16
g2 = Fraction(1,256)
mu = Fraction(1,1)/(1+g2)
mu3 = x/(g2+x)
trace = 2*mu+mu3
assert mu > Fraction(99,100)
assert trace < Fraction(201,100)
assert x < s0

# partner constant for Delta=1 and outer square a=1
Cgrp = (2**(4/3)+1)*sqrt(3)*2**(1/4)
assert Cgrp < 7.251

print('lower2 =', lower2, float(lower2))
print('lower3 =', lower3, float(lower3))
print('alpha2(eps=1/200) =', alpha2, float(alpha2))
print('mu =', float(mu), 'mu3 =', float(mu3), 'trace =', float(trace))
print('Cgrp =', Cgrp)
print('QFORM_B08_R19_CHECK_PASS')

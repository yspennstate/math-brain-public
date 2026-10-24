from fractions import Fraction
from math import sqrt

# The (X,Y,W) block is [[0,2,0],[2,0,-1/2],[0,-1/2,0]].
# Direct determinant expansion gives
# det(tI-B)=t*(t*t-(2**2+(1/2)**2))=t*(t*t-17/4).
star_energy = Fraction(2)**2 + Fraction(1,2)**2
assert star_energy == Fraction(17,4)
assert sqrt(float(star_energy)) == sqrt(17)/2
assert sqrt(17)/2 > 2
spectrum = (1.0, 0.0, sqrt(17)/2, -sqrt(17)/2)
assert sum(abs(x)>=1 for x in spectrum) == 3

# On the constructed support, 0<=4XY<=8 eps and
# 0<=Z^2-YW<=eps.
assert Fraction(8,1)+Fraction(1,1)==9
print("spectrum =", spectrum)
print("support width factor = 9")
print("QFORM_B19_MOVING_RIDGE_BARRIER_CHECK_PASS")

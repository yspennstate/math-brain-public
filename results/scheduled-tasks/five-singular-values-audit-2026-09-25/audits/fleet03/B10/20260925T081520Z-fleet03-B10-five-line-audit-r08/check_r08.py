from fractions import Fraction as F
from math import factorial

sqrt2u=F(14143,10000)
eu=F(27183,10000)
r6u=F(12849,10000)
assert sqrt2u**2>2
assert r6u**6>F(9,2)
S10=sum(F(1,factorial(k)) for k in range(11))
assert S10+F(12,11*factorial(11))<eu
C3u=3*sqrt2u*eu*r6u
assert C3u<15
assert 2**23*eu**4<F(122,10)**8
g1=F(44,96)-5*sqrt2u/F(96)
g2=F(44,96)-15*sqrt2u/F(96)
g3=F(44,96)-25*sqrt2u/F(96)
assert g1-F(38,100)==F(299,64000)
assert g2-F(237,1000)==F(67,192000)
assert g3-F(9,100)==F(1,38400)
for p in [F(3,2),F(2,1),F(7,3),F(5,1)]:
    a=F(11,13)
    assert 2*a+2*a/(p-1)==2*a*p/(p-1)
print("ALL R08 EXACT CERTIFICATES PASS")

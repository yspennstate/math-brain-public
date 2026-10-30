from fractions import Fraction as F
eta,zeta,a0=F(1,12),F(1,256),F(5,48)
assert eta*eta+zeta==a0*a0==F(25,2304)
s=F(14143,10000)
checks=[(1,F(38,100),F(299,64000)),(2,F(237,1000),F(67,192000)),(3,F(9,100),F(1,38400))]
for m,t,margin in checks:
    k=2*m-1
    g=F(44,96)-F(5*k,96)*s
    assert g-t==margin and g>t
assert F(15)**6-F(26244)*F(11,4)**6==F(40788279,1024)
assert F(61,5)**8-F(8388608)*F(11,4)**4==F(4302512997281,390625)
assert F(167)-F(15)*F(100,9)==F(1,3)
assert F(237,1000)*F(2055,1000)**2-1==F(34277,40000000)
assert F(26)-F(122,10)*F(2055,1000)==F(929,1000)
print("ALL R01 RANDOM-SIGN EXACT CHECKS PASS")

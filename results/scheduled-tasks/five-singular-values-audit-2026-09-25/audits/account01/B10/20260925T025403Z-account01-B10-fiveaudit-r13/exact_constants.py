from fractions import Fraction as F
assert F(14143,10000)**2 > 2
e_lo,e_up=F(65,24),F(49,18)
assert e_lo**3 > 19
assert F(119,100)**4 > 2
assert F(53,25)**4 > e_up**3
I=F(1)-F(1,5)+F(1,18)-F(1,78)+F(1,408)+F(6,65)
assert 4*I < F(15,4)
assert 2*F(119,100)*F(53,25)*F(15,4) < 19
assert 15**6 > 26244*e_up**6
assert F(61,5)**8 > 2**23*e_up**4
for m,t in [(1,F(38,100)),(2,F(237,1000)),(3,F(9,100))]:
    assert (F(44)-5*F(14143,10000)*(2*m-1))/96 > t
assert F(237,1000)*F(411,200)**2 > 1
assert F(61,5)*F(411,200) < 26
assert F(693,200)**2 > 12
assert 77*F(693,200) < 267
print("PASS")

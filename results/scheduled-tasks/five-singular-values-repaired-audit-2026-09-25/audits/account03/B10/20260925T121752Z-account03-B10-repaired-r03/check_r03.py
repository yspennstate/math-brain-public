from fractions import Fraction as F
import math
eta=F(1,12); zeta=F(1,256); a0=F(5,48)
assert eta*eta+zeta == a0*a0 == F(25,2304)
s2=F(14143,10000)
G=[]
for m,thr in [(1,F(38,100)),(2,F(237,1000)),(3,F(9,100))]:
    k=2*m-1
    gl=F(44,96)-F(5*k,96)*s2
    assert gl>thr
    G.append(gl-thr)
assert G == [F(299,64000),F(67,192000),F(1,38400)]
assert F(15)*F(100,9) < 167
assert F(237,1000)*F(2055,1000)**2 > 1
assert F(122,10)*F(2055,1000) < 26
assert F(548,25)*F(693,200) < 76
assert F(76)-F(548,25)*F(693,200) == F(59,1250)
assert 12*77*77 < 267*267
assert 267*267-12*77*77 == 141
assert 16*F(22,7) < 51
bound=16*(F(8)+4*F(1733,2500)+2*F(3))+F(10,27)
assert bound < 269
assert F(269)-bound == F(4469,16875)
assert F(19)**4 > F(2048)*F(68,25)**3*F(63,20)
assert F(19)**4-F(2048)*F(68,25)**3*F(63,20) == F(39009533,78125)
assert 12+5*math.log(2) < 16
print("ALL REPAIRED R03 EXACT/FINITE CHECKS PASS")
print("gamma margins:", ", ".join(str(x) for x in G))
print("half-potential <76 margin:", F(59,1250))
print("diagonal <267 squared margin:", 141)
print("indefinite <269 margin:", F(4469,16875))
print("concentration <19 fourth-power margin:", F(39009533,78125))

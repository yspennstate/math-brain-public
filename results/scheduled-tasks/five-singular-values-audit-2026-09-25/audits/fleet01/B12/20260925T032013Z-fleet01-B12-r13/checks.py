from fractions import Fraction as F
import math

N=12
ep=sum(F(1,math.factorial(n)) for n in range(N+1))
etail=F(1,math.factorial(N+1))*F(N+2,N+1)
eu=ep+etail
assert eu < F(271829,100000)
sq2u=F(14143,10000); assert sq2u**2>2
piu=F(31416,10000)
x=F(6932,10000)
assert sum(x**n/F(math.factorial(n)) for n in range(10))>2
assert sum(F(3)**n/F(math.factorial(n)) for n in range(9))>19
elo=F(271828,100000); b=F(59461,100000); assert b**4>F(1,8)
gu=F(16,5)+F(4,5)/elo+b/elo+(1-b)/(elo*elo)
assert gu<F(471,125)
assert F(119,100)**4>2
assert F(2118,1000)**4>eu**3
sb=2*F(119,100)*F(2118,1000)*F(471,125); assert sb<19
r6=F(1285,1000); assert r6**6>F(9,2)
C3=3*sq2u*eu*r6; assert C3<15
se=F(1649,1000); assert se**2>eu
tn=F(918,1000); assert tn**8>F(1,2)
C2=8*se*tn; assert C2<F(122,10)
g1=(F(44)-5*sq2u)/96; g2=(F(44)-15*sq2u)/96; g3=(F(44)-25*sq2u)/96
assert g1>F(38,100) and g2>F(237,1000) and g3>F(9,100)
assert F(2055,1000)**2*F(237,1000)>1
assert F(122,10)*F(2055,1000)<26
assert 12+5*x<16
inner=piu+4+4*x+12; assert inner<F(2192,100)
s12=F(3465,1000); assert s12**2>12
assert s12*inner<76 and s12*77<267
assert 16*piu<51
indef=16*(8+4*x+6)+F(10,27); assert indef<269
print("PASS")
print("Gamma(1/4) upper",float(gu))
print("small-ball coefficient upper",float(sb))
print("C3 upper",float(C3))
print("C2 upper",float(C2))
print("gamma lower",float(g1),float(g2),float(g3))
print("diagonal truncated upper",float(s12*inner))
print("indefinite upper",float(indef))

from fractions import Fraction as F
import math

assert F(14143,10000)**2 > 2
assert F(99,70)**2 > 2
eta=F(1,12); zeta=F(1,256); a0=F(5,48)
assert eta*eta+zeta == a0*a0

s2u=F(14143,10000)
g1=(F(44)-5*s2u)/96
g2=(F(44)-15*s2u)/96
g3=(F(44)-25*s2u)/96
assert g1-F(38,100)==F(299,64000)
assert g2-F(237,1000)==F(67,192000)
assert g3-F(9,100)==F(1,38400)

S10=sum(F(1,math.factorial(k)) for k in range(11))
eup=S10+F(12,11*math.factorial(11))
assert eup < F(68,25)
assert F(129,100)**6 > F(9,2)
C3u=3*F(99,70)*F(68,25)*F(129,100)
assert C3u < 15
assert 2**23 * F(68,25)**4 < F(61,5)**8
assert 15*F(100,9) < 167
assert 12*77*77 < 267*267
assert 16*F(22,7) < 51

x=F(1733,2500); term=F(1); sx=F(1)
for k in range(1,7):
    term=term*x/k; sx += term
assert sx>2

term=F(1); s3=F(1)
for k in range(1,10):
    term=term*3/k; s3 += term
assert s3>19

lower_e=sum(F(1,math.factorial(k)) for k in range(7))
assert lower_e>F(27,10)
bound=16*(8+4*F(1733,2500)+6)+F(10,27)
assert bound<269

rows,cols,j=3,2,3
assert j>min(rows,cols)
assert min(rows,cols)<j

print("ALL R07 EXACT/FINITE CERTIFICATES PASS")
print("C3 coarse rigorous upper =", float(C3u))
print("indefinite-pair coarse rational upper =", float(bound))

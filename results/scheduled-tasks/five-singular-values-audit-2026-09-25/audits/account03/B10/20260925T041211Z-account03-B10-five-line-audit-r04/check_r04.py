from fractions import Fraction as F
from math import factorial

def atan_partial(x,N):
    return sum(((-1)**n)*x**(2*n+1)/F(2*n+1) for n in range(N+1))

def log2_upper():
    K=2
    s=sum(F(2,(2*k+1)*3**(2*k+1)) for k in range(K+1))
    tail=F(2,2*(K+1)+1)*F(1,3**(2*(K+1)+1))/(1-F(1,9))
    return s+tail

assert F(14143,10000)**2>2
assert F(3465,1000)**2>12

e_lo=sum(F(1,factorial(k)) for k in range(7))
assert e_lo==F(1957,720) and e_lo>F(27,10)
e_hi=e_lo+F(1,factorial(7))/(1-F(1,8))
assert e_hi<F(68,25)

# Machin: pi/4=4 atan(1/5)-atan(1/239).
pi_hi=4*(4*atan_partial(F(1,5),4)-atan_partial(F(1,239),1))
assert pi_hi<F(31416,10000)

ln2_hi=log2_upper()
assert ln2_hi<F(6932,10000)
assert sum(F(3**k,factorial(k)) for k in range(7))>19

eta=F(1,12); zeta=F(1,256); a0=F(5,48)
assert eta*eta+zeta==a0*a0
s2=F(14143,10000)
g1=(44-5*s2)/96
g2=(44-15*s2)/96
g3=(44-25*s2)/96
assert g1-F(38,100)==F(299,64000)
assert g2-F(237,1000)==F(67,192000)
assert g3-F(9,100)==F(1,38400)

assert F(15)*F(100,9)<167
assert F(2055,1000)**2*F(237,1000)>1
assert F(122,10)*F(2055,1000)<26

# Gamma(1/4)<15/4: polynomial upper bound on [0,1], then t^-3/4<=1 on [1,infty).
G01=F(4)-F(4,5)+F(2,9)-F(2,39)+F(1,102)
Gtail=F(720,1957)
assert G01+Gtail<F(15,4)

# 2^(5/4)e^(3/4)Gamma(1/4)<18.921<19.
assert F(119,50)**4>32
assert F(68,25)**3<F(53,25)**4
assert F(119,50)*F(53,25)*F(15,4)==F(18921,1000)<19

assert F(15,2)*ln2_hi<6
assert 12+5*ln2_hi<16

Jhi=F(31416,10000)+4+4*F(6932,10000)+12
assert Jhi<F(2192,100)
assert F(3465,1000)*Jhi<76
assert F(3465,1000)*77<267
assert 16*pi_hi<51

indef=16*(8+4*F(6932,10000)+6)+F(10,27)
assert indef<269

print("ALL R04 EXACT/RIGOROUS CERTIFICATES PASS")
print("gamma margins:",g1-F(38,100),g2-F(237,1000),g3-F(9,100))
print("Gamma(1/4) certified upper:",float(G01+Gtail))
print("concentration coefficient certified upper:",float(F(18921,1000)))
print("diagonal truncated certified upper:",float(F(3465,1000)*Jhi))
print("indefinite-pair certified upper:",float(indef))

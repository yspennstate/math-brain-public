from fractions import Fraction as F
from math import factorial
eta=F(7,75); zeta=F(1,287); a0ub=F(2761,25000); s2=F(99,70)
assert a0ub*a0ub > eta*eta+zeta
g2=(1-eta-s2*a0ub*3)/2; g3=(1-eta-s2*a0ub*5)/2
assert g2==F(2299949,10500000) and g3==F(131983,2100000)
assert F(467,1000)**2<g2
T=lambda x,N:sum((x**k)/F(factorial(k),1) for k in range(N+1))
assert T(F(347,500),4)>2 and T(F(589,200),10)>19
assert sum(F(1,factorial(k)) for k in range(9))+F(10,9*factorial(9))<F(2719,1000)
assert F(257,200)**6>F(9,2)
assert F(1637,500)**2>F(75,7)
assert F(103,25)**4>287 and F(8471,500)**2>287
pi=F(22,7); l2=F(347,500); l19=F(589,200)
C3=3*s2*F(2719,1000)*F(257,200)
nopiv=C3/g3
B=pi+4*l2+4+4*l19
half0=F(61,5)/F(467,1000)
halfp=16*F(103,25)
halfd=1+F(1637,500)*B
par0=F(1637,500)*half0
parp=F(1637,500)*halfp
pard=F(1637,500)+B/eta
defp=pi*F(8471,500)
indp=F(8471,500)*(8+2*l19)
assert nopiv==F(622615653,2639660) and nopiv<236
assert half0<73 and halfp<73 and halfd==F(63036801,875000) and halfd<73
assert par0==F(199714,2335) and par0<236
assert parp==F(674444,3125) and parp<236
assert pard==F(5776163,24500) and pard<236
assert defp==F(93181,1750) and defp<236
assert indp==F(11766219,50000) and indp<236
print("QFORM_B08_R66_FIVE236_CHECK_PASS")
for k,v in [("g2",g2),("g3",g3),("nopiv",nopiv),("half0",half0),("halfp",halfp),("halfd",halfd),("par0",par0),("parp",parp),("pard",pard),("defp",defp),("indp",indp)]: print(k,float(v))

from fractions import Fraction
from decimal import Decimal, getcontext

p=256717
q=800000
d=q-p
a=int('1995237757733917147310102692686664915858011319606812684127301')
b=4_220_452_010_631_561_279
S=q**6*d
t=Fraction(p,q)
Dmm=Fraction(655209040831815247751186134103526570372190622578374697627001555,
             925139970226099634)
Dtail=2*Dmm
R=Fraction(a,b)
beta_mm=R-Dmm/Fraction(2*a*b,1)
beta_tail=R-Dtail/Fraction(2*a*b,1)
scale=t*t/S
lambda_mm=scale*beta_mm
lambda_tail=scale*beta_tail
base=4*t*t
assert Dtail==2*Dmm
assert beta_tail<beta_mm
assert beta_tail*beta_tail > R*R-Dtail/Fraction(b*b,1)
assert 0<base<1 and 0<lambda_tail<lambda_mm<1

def neglog_bounds(z,K=220):
    assert 0<z<1
    u=(1-z)/(1+z)
    u2=u*u
    pw=u
    sm=Fraction(0,1)
    for k in range(K):
        sm += 2*pw/Fraction(2*k+1,1)
        pw *= u2
    tail=2*pw/Fraction(2*K+1,1)/(1-u2)
    return sm,sm+tail

Alo,Ahi=neglog_bounds(base)
Tlo,Thi=neglog_bounds(lambda_tail)
Mlo,Mhi=neglog_bounds(lambda_mm)
Utail_lo=Alo/Thi
Utail_hi=Ahi/Tlo
Umm_lo=Alo/Mhi
Umm_hi=Ahi/Mlo
assert Utail_hi < Umm_lo
L=Fraction(99083249,125000000)
assert L<Utail_lo

sep=None
for digits in range(60,141):
    ten=10**digits
    k=(Utail_hi.numerator*ten)//Utail_hi.denominator+1
    Q=Fraction(k,ten)
    if Utail_hi<Q<Umm_lo:
        sep=(digits,k,ten,Q)
        break
assert sep is not None

getcontext().prec=190
def decf(x):
    return Decimal(x.numerator)/Decimal(x.denominator)
Ud=decf(base).ln()/decf(lambda_tail).ln()
Um=decf(base).ln()/decf(lambda_mm).ln()
print('P02 T02 exact-tail endpoint checker')
print('D_ratio_diag=',decf(Dtail/Dmm))
print('diag_U_tail=',Ud)
print('diag_U_mm=',Um)
print('diag_source_decrease=',Um-Ud)
print('separator_digits=',sep[0])
print('separator_decimal=',format(Decimal(sep[1])/(Decimal(10)**sep[0]),'f'))
print('D_TAIL_EQ_2_D_MM=PASS')
print('EXACT_TWO_STEP_SPECTRAL_MAJORANT=PASS')
print('EXACT_LOG_INTERVALS_DISJOINT=PASS')
print('SOURCE_INTERVAL_STRICTLY_SHRINKS=PASS')
print('LOWER_ENDPOINT_RETAINED=PASS')
print('ALL_EXACT_CHECKS_PASS')

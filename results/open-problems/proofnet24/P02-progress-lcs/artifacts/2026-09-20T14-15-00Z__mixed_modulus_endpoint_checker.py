from fractions import Fraction
from decimal import Decimal, getcontext
p=256717;q=800000;d=q-p
a=int('1995237757733917147310102692686664915858011319606812684127301')
b=4_220_452_010_631_561_279
S=q**6*d
t=Fraction(p,q)
Dold=Fraction(97*a,1_094_462_055_227_467_919)
Dnew=Fraction(655209040831815247751186134103526570372190622578374697627001555,925139970226099634)
R=Fraction(a,b)
beta_old=R-Dold/Fraction(2*a*b,1)
beta_new=R-Dnew/Fraction(2*a*b,1)
scale=t*t/S
lambda_old=scale*beta_old
lambda_new=scale*beta_new
base=4*t*t
assert Dnew>4*Dold
assert beta_new<beta_old
assert beta_new*beta_new > R*R-Dnew/Fraction(b*b,1)
assert 0<base<1 and 0<lambda_new<lambda_old<1

def neglog_bounds(z,K=180):
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
Nlo,Nhi=neglog_bounds(lambda_new)
Olo,Ohi=neglog_bounds(lambda_old)
Unew_lo=Alo/Nhi; Unew_hi=Ahi/Nlo
Uold_lo=Alo/Ohi; Uold_hi=Ahi/Olo
assert Unew_hi < Uold_lo
L=Fraction(99083249,125000000)
assert L<Unew_lo
sep=None
for digits in range(60,121):
    ten=10**digits
    k=(Unew_hi.numerator*ten)//Unew_hi.denominator+1
    Q=Fraction(k,ten)
    if Unew_hi<Q<Uold_lo:
        sep=(digits,k,ten,Q);break
assert sep is not None
getcontext().prec=160
def decf(x): return Decimal(x.numerator)/Decimal(x.denominator)
Ud=decf(base).ln()/decf(lambda_new).ln()
Uo=decf(base).ln()/decf(lambda_old).ln()
print('P02 T02 mixed-modulus endpoint checker')
print('D_ratio_diag=',decf(Dnew/Dold))
print('diag_U_new=',Ud)
print('diag_U_old=',Uo)
print('diag_source_decrease=',Uo-Ud)
print('separator_digits=',sep[0])
print('separator_decimal=',format(Decimal(sep[1])/(Decimal(10)**sep[0]),'f'))
print('D_NEW_GT_4_D_01=PASS')
print('EXACT_TWO_STEP_SPECTRAL_MAJORANT=PASS')
print('EXACT_LOG_INTERVALS_DISJOINT=PASS')
print('SOURCE_INTERVAL_STRICTLY_SHRINKS=PASS')
print('LOWER_ENDPOINT_RETAINED=PASS')
print('ALL_EXACT_CHECKS_PASS')

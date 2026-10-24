from fractions import Fraction
from decimal import Decimal, getcontext

p=256717
q=800000
d=q-p
a=int('1995237757733917147310102692686664915858011319606812684127301')
b=4_220_452_010_631_561_279
S=q**6*d
c7=p**7
vstar=707_440_146_652_911_839+b
D_floor=a//vstar
D_old=D_floor+1500*c7+1
D=Fraction(
184471690248013406739062287587614517847930962166579078150820585,
1046084316655648409)
assert D > D_old
R=Fraction(a,b)
t=Fraction(p,q)
scale=t*t/S
base=4*t*t
beta_old=R-Fraction(D_old,2*a*b)
beta_new=R-D/Fraction(2*a*b,1)
assert beta_new < beta_old
assert beta_new*beta_new > R*R-D/Fraction(b*b,1)
lambda_old=scale*beta_old
lambda_new=scale*beta_new
assert 0 < base < 1
assert 0 < lambda_new < lambda_old < 1

def neglog_bounds(z,K=300):
    assert 0 < z < 1
    u=(1-z)/(1+z)
    u2=u*u
    pw=u
    s=Fraction(0,1)
    for k in range(K):
        s += 2*pw/Fraction(2*k+1,1)
        pw *= u2
    tail=2*pw/Fraction(2*K+1,1)/(1-u2)
    return s,s+tail

Alo,Ahi=neglog_bounds(base)
Nlo,Nhi=neglog_bounds(lambda_new)
Olo,Ohi=neglog_bounds(lambda_old)
Unew_lo=Alo/Nhi
Unew_hi=Ahi/Nlo
Uold_lo=Alo/Ohi
Uold_hi=Ahi/Olo
assert Unew_hi < Uold_lo
L=Fraction(99083249,125000000)
assert L < Unew_lo

getcontext().prec=140
def decf(x): return Decimal(x.numerator)/Decimal(x.denominator)
Ud=(decf(base).ln()/decf(lambda_new).ln())
Uod=(decf(base).ln()/decf(lambda_old).ln())
print('diag_Unew=',Ud)
print('diag_Uold=',Uod)
print('diag_decrease=',Uod-Ud)
print('D_ratio=',decf(D/Fraction(D_old,1)))

for digits in range(60,111):
    scale10=10**digits
    k=(Unew_hi.numerator*scale10)//Unew_hi.denominator + 1
    Q=Fraction(k,scale10)
    if Unew_hi < Q < Uold_lo:
        print('separator_digits=',digits)
        print('separator_num=',k)
        print('separator_den=',scale10)
        print('separator_decimal=',format(Decimal(k)/(Decimal(10)**digits),'f'))
        break
else:
    raise RuntimeError('no separator found')

print('D_old=',D_old)
print('D_new_num=',D.numerator)
print('D_new_den=',D.denominator)
print('D_new_over_D_old_num=',(D/Fraction(D_old,1)).numerator)
print('D_new_over_D_old_den=',(D/Fraction(D_old,1)).denominator)
print('beta_new_num=',beta_new.numerator)
print('beta_new_den=',beta_new.denominator)
print('lambda_new_num=',lambda_new.numerator)
print('lambda_new_den=',lambda_new.denominator)
print('EXACT_DEFECT_STRICTLY_IMPROVES=PASS')
print('EXACT_TWO_STEP_SPECTRAL_MAJORANT=PASS')
print('EXACT_LOG_INTERVALS_DISJOINT=PASS')
print('SOURCE_INTERVAL_STRICTLY_SHRINKS=PASS')
print('ALL_EXACT_CHECKS_PASS')

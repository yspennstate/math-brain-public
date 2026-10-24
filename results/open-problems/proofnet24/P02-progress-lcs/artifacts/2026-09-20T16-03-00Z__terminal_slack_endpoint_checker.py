from fractions import Fraction
from decimal import Decimal, getcontext
p=256717
q=800000
d=q-p
a=int('1995237757733917147310102692686664915858011319606812684127301')
b=4_220_452_010_631_561_279
S=q**6*d
t=Fraction(p,q)
Dmm=Fraction(655209040831815247751186134103526570372190622578374697627001555,925139970226099634)
Dprev=2*Dmm
Dnew=Fraction(7,2)*Dmm
R=Fraction(a,b)
beta_prev=R-Dprev/Fraction(2*a*b,1)
beta_new=R-Dnew/Fraction(2*a*b,1)
scale=t*t/S
lam_prev=scale*beta_prev
lam_new=scale*beta_new
base=4*t*t
assert Dnew == Fraction(7,4)*Dprev
assert beta_new < beta_prev
assert beta_new*beta_new > R*R-Dnew/Fraction(b*b,1)
assert 0<base<1 and 0<lam_new<lam_prev<1

def neglog_bounds(z,K=240):
    assert 0<z<1
    u=(1-z)/(1+z); u2=u*u; pw=u; sm=Fraction(0)
    for k in range(K):
        sm += 2*pw/Fraction(2*k+1)
        pw *= u2
    tail=2*pw/Fraction(2*K+1)/(1-u2)
    return sm,sm+tail
Alo,Ahi=neglog_bounds(base)
Nlo,Nhi=neglog_bounds(lam_new)
Plo,Phi=neglog_bounds(lam_prev)
Unew_lo=Alo/Nhi; Unew_hi=Ahi/Nlo
Uprev_lo=Alo/Phi; Uprev_hi=Ahi/Plo
assert Unew_hi < Uprev_lo
L=Fraction(99083249,125000000)
assert L<Unew_lo
sep=None
for digits in range(60,170):
    ten=10**digits
    k=(Unew_hi.numerator*ten)//Unew_hi.denominator+1
    Q=Fraction(k,ten)
    if Unew_hi<Q<Uprev_lo:
        sep=(digits,k,Q); break
assert sep
getcontext().prec=220
def decf(x): return Decimal(x.numerator)/Decimal(x.denominator)
Ud=decf(base).ln()/decf(lam_new).ln()
Up=decf(base).ln()/decf(lam_prev).ln()
print('P02 T02 terminal-slack-minimization endpoint checker')
print('Dnew_over_Dprev=', decf(Dnew/Dprev))
print('diag_U_new=',Ud)
print('diag_U_prev=',Up)
print('diag_source_decrease=',Up-Ud)
print('separator_digits=',sep[0])
print('separator_decimal=',format(Decimal(sep[1])/(Decimal(10)**sep[0]),'f'))
print('D_NEW_EQ_7_OVER_4_D_PREV=PASS')
print('EXACT_TWO_STEP_SPECTRAL_MAJORANT=PASS')
print('EXACT_LOG_INTERVALS_DISJOINT=PASS')
print('SOURCE_INTERVAL_STRICTLY_SHRINKS=PASS')
print('LOWER_ENDPOINT_RETAINED=PASS')
print('ALL_EXACT_CHECKS_PASS')

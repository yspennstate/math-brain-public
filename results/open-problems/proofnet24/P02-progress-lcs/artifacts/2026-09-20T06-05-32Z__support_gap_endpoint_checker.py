from fractions import Fraction
from math import gcd

p=256717
q=800000
M=5_000_000_000_000_000_000
a=int('1995237757733917147310102692686664915858011319606812684127301')
b=4_220_452_010_631_561_279
S=q**6*(q-p)
coeff=[q**(6-k)*(q-p)*p**k for k in range(7)] + [p**7]
m0=min(coeff)
Wstar=coeff[0]+coeff[7]
assert Wstar==142491860994694633120311956186136958404773
assert gcd(a,b)==1
assert b<=M<2*b
assert a>=Wstar*M
assert 1939*m0 < Wstar < 1940*m0

R=Fraction(a,b)
t=Fraction(p,q)
scale=t*t/S
base=4*t*t
assert 0<base<1

# Previous coefficient-weighted P02 rate.
betaW=R-Fraction(m0,2*a*b)
lambdaW=scale*betaW

# New support-gap two-step rate.  The support checker proves every tight row
# has total coefficient weight to non-tight successors at least Wstar.
betaS=R-Fraction(Wstar,2*a*b)
lambdaS=scale*betaS
assert betaS*betaS > R*R - Fraction(Wstar,b*b)
assert 0<lambdaS<lambdaW<1
assert (R-betaS)/(R-betaW) == Fraction(Wstar,m0)

def neglog_bounds(z,K=160):
    assert 0<z<1
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
Slo,Shi=neglog_bounds(lambdaS)
Wlo,Whi=neglog_bounds(lambdaW)

# 81-decimal separator: U_S < Q < U_W.
Q=Fraction(
    826275942762282625015106581537296632823461996193190023880806183312562944430299551,
    10**81
)
U_S_upper=Ahi/Slo
U_W_lower=Alo/Whi
assert U_S_upper < Q < U_W_lower

L=Fraction(99083249,125000000)
assert L < U_S_upper

print('P02 T02 support-gap endpoint checker')
print(f'S={S}')
print(f'm0={m0}')
print(f'Wstar={Wstar}')
print(f'Wstar_over_m0_num={Wstar}')
print(f'Wstar_over_m0_den={m0}')
print(f'betaS_num={betaS.numerator}')
print(f'betaS_den={betaS.denominator}')
print(f'lambdaS_num={lambdaS.numerator}')
print(f'lambdaS_den={lambdaS.denominator}')
print(f'Q_num={Q.numerator}')
print(f'Q_den={Q.denominator}')
print('EXACT_SUPPORT_GAP_RATE_BEATS_WEIGHTED_RATE_PASS')
print('EXACT_TWO_STEP_SPECTRAL_MAJORANT_PASS')
print('EXACT_LOG_SEPARATOR_PASS')
print('SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS')
print('ALL_EXACT_CHECKS_PASS')

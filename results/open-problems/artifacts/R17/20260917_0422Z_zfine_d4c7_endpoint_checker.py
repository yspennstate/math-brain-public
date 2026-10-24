#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=110
z=Fraction(1283585,4000000)
a=2*z
lam=Fraction(23270168989546870285756517221346667843261607615123844475889614544459633,
             68076744132226637623985889607680000000000000000000000000000000000000000)
U_old=Fraction(826279178542431497521,10**21)
U_new=Fraction(82627917854239849,10**17)
L=Fraction(99083249,125000000)
assert U_new<U_old

def neglog_bounds(x,terms):
    u=(1-x)/(1+x)
    s=Fraction(0); p=u
    for k in range(terms):
        s += p/(2*k+1); p*=u*u
    lo=2*s
    hi=lo+2*p/((2*terms+1)*(1-u*u))
    return lo,hi
Alo,Ahi=neglog_bounds(a,90)
Llo,Lhi=neglog_bounds(lam,180)
Blo=2*Alo/Lhi
Bhi=2*Ahi/Llo
assert Blo<Bhi<U_new<U_old
improve=U_old-U_new
width=U_new-L
D=lambda x: Decimal(x.numerator)/Decimal(x.denominator)
print('R17-C023 exact endpoint compiler')
print('z=',z)
print('lambda=',lam)
print('continuous_lower=',D(Blo))
print('continuous_upper=',D(Bhi))
print('new_upper=',U_new)
print('new_upper_decimal=',D(U_new))
print('old_upper=',U_old)
print('improvement=',improve)
print('improvement_decimal=',D(improve))
print('new_width=',width)
print('new_width_decimal=',D(width))
print('EXACT_LOG_INTERVAL_PASS')
print('ALL_EXACT_CHECKS_PASS')

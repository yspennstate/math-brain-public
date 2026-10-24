#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=110
z=Fraction(320896250000000001555829,10**24)
a=2*z
lam=Fraction(276956593963024041276868865537229787866977713766800486192609348116933979994322388660419915295651421954345692954069536680021619448973121399254142401074736761271584886999617569305776597906676298472939031374055058917968076875499146958477,810234905961502854639100242552083250335501200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
Uold=Fraction(20656979463559945634521013,25000000000000000000000000)
Unew=Fraction(826279178542397825380217,10**24)
L=Fraction(99083249,125000000)
assert 0<a<1 and 0<lam<1 and Unew<Uold

def neglog_bounds(x,m):
    u=(1-x)/(1+x)
    s=Fraction(0); p=u
    for k in range(m):
        s += p/(2*k+1)
        p *= u*u
    lo=2*s
    hi=lo+2*p/((2*m+1)*(1-u*u))
    return lo,hi
alo,ahi=neglog_bounds(a,70)
llo,lhi=neglog_bounds(lam,140)
Blo=2*alo/lhi
Bhi=2*ahi/llo
assert Blo < Bhi < Unew < Uold
width=Unew-L
imp=Uold-Unew

def dec(q): return Decimal(q.numerator)/Decimal(q.denominator)
print('R17-C026 deterministic-floor endpoint compiler')
print('z=',z,sep='')
print('lambda_num=',lam.numerator,sep='')
print('lambda_den=',lam.denominator,sep='')
print('continuous_bound_lower=',dec(Blo),sep='')
print('continuous_bound_upper=',dec(Bhi),sep='')
print('CERTIFIED_NEW_UPPER=',Unew,sep='')
print('CERTIFIED_NEW_UPPER_DECIMAL=',dec(Unew),sep='')
print('PREVIOUS_UPPER=',Uold,sep='')
print('UPPER_DECREASE=',imp,sep='')
print('UPPER_DECREASE_DECIMAL=',dec(imp),sep='')
print('CERTIFIED_NEW_WIDTH=',width,sep='')
print('CERTIFIED_NEW_WIDTH_DECIMAL=',dec(width),sep='')
print('ALL_EXACT_CHECKS_PASS')

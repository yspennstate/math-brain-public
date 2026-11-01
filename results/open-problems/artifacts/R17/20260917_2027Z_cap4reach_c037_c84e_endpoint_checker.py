#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=200
XN=513401; YN=513467; D=1600000
A=Fraction(4*XN*YN,D*D)
LAM=Fraction(
1896106779011875453975548448369940337068581432724586971774448328312731151,
5547051831507839959716016779427840000000000000000000000000000000000000000)
LOW=Fraction(99083249,125000000)
OLD=Fraction(826279175721587835,10**18)
NEW=Fraction(826278839682207703,10**18)
def neglog_bounds(x,n):
    assert 0<x<1
    u=(1-x)/(1+x);s=Fraction(0);p=u
    for k in range(n):
        s += p/Fraction(2*k+1,1); p*=u*u
    lo=2*s
    hi=lo+2*p/(Fraction(2*n+1,1)*(1-u*u))
    return lo,hi
def dec(q): return Decimal(q.numerator)/Decimal(q.denominator)
a_lo,a_hi=neglog_bounds(A,400)
l_lo,l_hi=neglog_bounds(LAM,550)
b_lo=a_lo/l_hi;b_hi=a_hi/l_lo
assert b_lo<=b_hi<NEW<OLD
width=NEW-LOW; improve=OLD-NEW
print('R17 C037 exact endpoint compiler')
print('A_4xy =',A)
print('lambda_num =',LAM.numerator)
print('lambda_den =',LAM.denominator)
print('continuous_bound_lower =',dec(b_lo))
print('continuous_bound_upper =',dec(b_hi))
print('C036_UPPER =',dec(OLD))
print('C037_CERTIFIED_UPPER =',dec(NEW))
print('UPPER_DECREASE_FROM_C036 =',dec(improve))
print('C037_CERTIFIED_WIDTH =',dec(width))
print('EXACT_LOG_INTERVAL_PASS')
print('ALL_EXACT_CHECKS_PASS')

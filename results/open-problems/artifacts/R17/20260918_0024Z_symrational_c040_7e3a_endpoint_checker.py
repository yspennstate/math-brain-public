#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=220
XN=513434; YN=513434; D=1600000
A=Fraction(4*XN*YN,D*D)
LAM=Fraction(
160950714326114089318842815668519935000779914683638667678732754292957,
470861513652369151126436577280000000000000000000000000000000000000000)
LOW=Fraction(99083249,125000000)  # 0.792665992
OLD=Fraction(826278084895431510,10**18)
NEW=Fraction(826277324203068393,10**18)
def neglog_bounds(x,n):
    assert 0 < x < 1
    u=(1-x)/(1+x); s=Fraction(0); p=u
    for k in range(n):
        s += p/Fraction(2*k+1,1)
        p *= u*u
    lo=2*s
    hi=lo+2*p/(Fraction(2*n+1,1)*(1-u*u))
    return lo,hi
def dec(q): return Decimal(q.numerator)/Decimal(q.denominator)
a_lo,a_hi=neglog_bounds(A,400)
l_lo,l_hi=neglog_bounds(LAM,550)
b_lo=a_lo/l_hi; b_hi=a_hi/l_lo
assert b_lo <= b_hi < NEW < OLD
width=NEW-LOW; improve=OLD-NEW
print('R17 C040 exact endpoint compiler')
print('x =', Fraction(XN,D))
print('y =', Fraction(YN,D))
print('A_4xy =',A)
print('lambda_num =',LAM.numerator)
print('lambda_den =',LAM.denominator)
print('continuous_bound_lower =',dec(b_lo))
print('continuous_bound_upper =',dec(b_hi))
print('C039_UPPER =',dec(OLD))
print('C040_CERTIFIED_UPPER =',dec(NEW))
print('UPPER_DECREASE_FROM_C039 =',dec(improve))
print('C040_CERTIFIED_WIDTH =',dec(width))
print('EXACT_LOG_INTERVAL_PASS')
print('ALL_EXACT_CHECKS_PASS')

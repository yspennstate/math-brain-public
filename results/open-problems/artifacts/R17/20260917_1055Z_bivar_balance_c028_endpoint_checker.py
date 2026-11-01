#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=120

X=Fraction(256701,800000)
Y=Fraction(256733,800000)
A=4*X*Y
LAM=Fraction(
7776991210256127379106374160733421396891578035327458704664931125711751,
22751542775836272211450386186240000000000000000000000000000000000000000)
U_OLD=Fraction(103284897223075703,125000000000000000)
U_NEW=Fraction(826279175724058061,10**18)
LOWER=Fraction(99083249,125000000)
assert 0<A<1 and 0<LAM<1 and U_NEW<U_OLD

def neglog_bounds(x, terms):
    u=(1-x)/(1+x)
    s=Fraction(0); p=u
    for k in range(terms):
        s += p/(2*k+1)
        p *= u*u
    lo=2*s
    hi=lo + 2*p/((2*terms+1)*(1-u*u))
    return lo,hi

Alo,Ahi=neglog_bounds(A,80)
Llo,Lhi=neglog_bounds(LAM,160)
Blo=Alo/Lhi
Bhi=Ahi/Llo
assert Blo < Bhi < U_NEW < U_OLD
width=U_NEW-LOWER
improvement=U_OLD-U_NEW

def dec(q): return Decimal(q.numerator)/Decimal(q.denominator)
print('R17-C028 exact bivariate endpoint compiler')
print('x=256701/800000')
print('y=256733/800000')
print('lambda_num='+str(LAM.numerator))
print('lambda_den='+str(LAM.denominator))
print('continuous_bound_lower_decimal='+str(dec(Blo)))
print('continuous_bound_upper_decimal='+str(dec(Bhi)))
print('CERTIFIED_NEW_UPPER='+str(U_NEW))
print('CERTIFIED_NEW_UPPER_DECIMAL='+str(dec(U_NEW)))
print('PREVIOUS_UPPER='+str(U_OLD))
print('UPPER_DECREASE='+str(improvement))
print('UPPER_DECREASE_DECIMAL='+str(dec(improvement)))
print('CERTIFIED_NEW_WIDTH='+str(width))
print('CERTIFIED_NEW_WIDTH_DECIMAL='+str(dec(width)))
print('ALL_EXACT_CHECKS_PASS')

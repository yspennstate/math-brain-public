#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=190
XN=513401;YN=513467;D=1600000
A=Fraction(4*XN*YN,D*D)
LAM=Fraction(338209409229022286277141841733352538972564131089317618416593328196149,
             990560190589175518276395991040000000000000000000000000000000000000000)
LOW=Fraction(99083249,125000000)
OLD=Fraction(825712729153870335,10**18)
NEW=Fraction(825401117105668122,10**18)
def neglog_bounds(x,n):
    u=(1-x)/(1+x); s=Fraction(0); p=u
    for k in range(n):
        s += p/Fraction(2*k+1,1); p*=u*u
    lo=2*s
    hi=lo+2*p/(Fraction(2*n+1,1)*(1-u*u))
    return lo,hi
a_lo,a_hi=neglog_bounds(A,300)
l_lo,l_hi=neglog_bounds(LAM,400)
b_lo=a_lo/l_hi;b_hi=a_hi/l_lo
assert 0<A<1 and 0<LAM<1
assert b_lo<b_hi<NEW<OLD
width=NEW-LOW;improve=OLD-NEW
def dec(q): return Decimal(q.numerator)/Decimal(q.denominator)
print('R17 C035 exact length-three-deficiency-DFA endpoint compiler')
print('a=4xy =',A)
print('lambda_num =',LAM.numerator)
print('lambda_den =',LAM.denominator)
print('continuous_bound_lower =',dec(b_lo))
print('continuous_bound_upper =',dec(b_hi))
print('CERTIFIED_NEW_UPPER =',NEW)
print('CERTIFIED_NEW_UPPER_DECIMAL =',dec(NEW))
print('PREVIOUS_UPPER =',OLD)
print('UPPER_DECREASE =',improve)
print('UPPER_DECREASE_DECIMAL =',dec(improve))
print('CERTIFIED_NEW_WIDTH =',width)
print('CERTIFIED_NEW_WIDTH_DECIMAL =',dec(width))
print('EXACT_LOG_INTERVAL_PASS')
print('ALL_EXACT_CHECKS_PASS')

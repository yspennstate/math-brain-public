#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 140
XN=513401; YN=513467; D=1600000
A = Fraction(4*XN*YN,D*D)
LAM = Fraction(
551931973236940225964428540264110568416180463593380443285347186019,
1615249411672359366368952320000000000000000000000000000000000000000)
LOW = Fraction(99083249,125000000)
OLD = Fraction(826279175721596843,10**18)
NEW = Fraction(826004912603413652,10**18)

def neglog_bounds(x,n):
    u=(1-x)/(1+x)
    s=Fraction(0); p=u
    for k in range(n):
        s += p/Fraction(2*k+1,1)
        p *= u*u
    lo=2*s
    hi=lo + 2*p/(Fraction(2*n+1,1)*(1-u*u))
    return lo,hi

a_lo,a_hi=neglog_bounds(A,220)
l_lo,l_hi=neglog_bounds(LAM,260)
b_lo=a_lo/l_hi
b_hi=a_hi/l_lo
assert 0<A<1 and 0<LAM<1
assert b_lo < b_hi < NEW < OLD
width=NEW-LOW
improve=OLD-NEW

def dec(q): return Decimal(q.numerator)/Decimal(q.denominator)
print('R17 C033 exact deficiency-product endpoint compiler')
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

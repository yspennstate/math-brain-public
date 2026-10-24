#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=180
XN=513401; YN=513467; D=1600000
A=Fraction(4*XN*YN,D*D)
LAM_NEW=Fraction(
1195270706779366137569952676440094043084251172216065059774700641209,
3496757536042215704272894217420800000000000000000000000000000000000)
LAM_C028=Fraction(
34095072675552928056806129922429163230355760757838621576476656857001629,
99744937815289777130664630000025600000000000000000000000000000000000000)
LOW=Fraction(99083249,125000000)
OLD_VALID=Fraction(826279175721596843,10**18)
NEW=Fraction(826279175721587835,10**18)

def neglog_bounds(x,n):
    assert 0 < x < 1
    u=(1-x)/(1+x)
    s=Fraction(0); p=u
    for k in range(n):
        s += p/Fraction(2*k+1,1)
        p *= u*u
    lo=2*s
    hi=lo+2*p/(Fraction(2*n+1,1)*(1-u*u))
    return lo,hi

def dec(q): return Decimal(q.numerator)/Decimal(q.denominator)

a_lo,a_hi=neglog_bounds(A,350)
l_lo,l_hi=neglog_bounds(LAM_NEW,500)
b_lo=a_lo/l_hi
b_hi=a_hi/l_lo
assert LAM_NEW < LAM_C028
assert b_lo <= b_hi < NEW < OLD_VALID
width=NEW-LOW
improve=OLD_VALID-NEW
ldiff=LAM_C028-LAM_NEW
print('R17 C036 exact gauge-corrected endpoint compiler')
print('A=4xy =',A)
print('lambda_new_num =',LAM_NEW.numerator)
print('lambda_new_den =',LAM_NEW.denominator)
print('lambda_C028_num =',LAM_C028.numerator)
print('lambda_C028_den =',LAM_C028.denominator)
print('lambda_C028_minus_new =',ldiff)
print('lambda_C028_minus_new_decimal =',dec(ldiff))
print('continuous_bound_lower =',dec(b_lo))
print('continuous_bound_upper =',dec(b_hi))
print('LAST_VALID_UPPER_C028 =',OLD_VALID)
print('CERTIFIED_NEW_UPPER =',NEW)
print('CERTIFIED_NEW_UPPER_DECIMAL =',dec(NEW))
print('UPPER_DECREASE_FROM_C028 =',improve)
print('UPPER_DECREASE_FROM_C028_DECIMAL =',dec(improve))
print('CERTIFIED_NEW_WIDTH =',width)
print('CERTIFIED_NEW_WIDTH_DECIMAL =',dec(width))
print('EXACT_LAMBDA_IMPROVEMENT_OVER_C028_PASS')
print('EXACT_LOG_INTERVAL_PASS')
print('ALL_EXACT_CHECKS_PASS')

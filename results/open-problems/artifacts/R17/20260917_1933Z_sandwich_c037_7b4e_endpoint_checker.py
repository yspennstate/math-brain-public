#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec=180
XN=513401;YN=513467;D=1600000
A=Fraction(4*XN*YN,D*D)
LAM=Fraction(
165825918177951184619949535340736014158789311064658343958162351341127,
485122975607220304914122014720000000000000000000000000000000000000000)
LAM_C036=Fraction(
1195270706779366137569952676440094043084251172216065059774700641209,
3496757536042215704272894217420800000000000000000000000000000000000)
LOW=Fraction(99083249,125000000)
OLD=Fraction(826279175721587835,10**18)
NEW=Fraction(826278840048067649,10**18)
def neglog_bounds(x,n):
    assert 0<x<1
    u=(1-x)/(1+x);s=Fraction(0);p=u
    for k in range(n):
        s += p/Fraction(2*k+1,1);p*=u*u
    lo=2*s;hi=lo+2*p/(Fraction(2*n+1,1)*(1-u*u))
    return lo,hi
def dec(q):return Decimal(q.numerator)/Decimal(q.denominator)
a_lo,a_hi=neglog_bounds(A,350);l_lo,l_hi=neglog_bounds(LAM,500)
b_lo=a_lo/l_hi;b_hi=a_hi/l_lo
assert LAM<LAM_C036
assert b_lo<=b_hi<NEW<OLD
width=NEW-LOW;improve=OLD-NEW;ldiff=LAM_C036-LAM
print('R17 C037 exact endpoint compiler')
print('A=4xy =',A)
print('lambda_new_num =',LAM.numerator)
print('lambda_new_den =',LAM.denominator)
print('lambda_C036_minus_new_decimal =',dec(ldiff))
print('continuous_bound_lower =',dec(b_lo))
print('continuous_bound_upper =',dec(b_hi))
print('OLD_VALID_UPPER_C036 =',OLD)
print('CERTIFIED_NEW_UPPER =',NEW)
print('CERTIFIED_NEW_UPPER_DECIMAL =',dec(NEW))
print('UPPER_DECREASE_FROM_C036 =',improve)
print('UPPER_DECREASE_FROM_C036_DECIMAL =',dec(improve))
print('CERTIFIED_NEW_WIDTH =',width)
print('CERTIFIED_NEW_WIDTH_DECIMAL =',dec(width))
print('EXACT_LAMBDA_IMPROVEMENT_OVER_C036_PASS')
print('EXACT_LOG_INTERVAL_PASS')
print('ALL_EXACT_CHECKS_PASS')

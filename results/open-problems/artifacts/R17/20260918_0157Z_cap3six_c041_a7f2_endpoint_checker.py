from fractions import Fraction
from decimal import Decimal,getcontext
getcontext().prec=220
XN=YN=513434;D=1600000
A=Fraction(4*XN*YN,D*D)
LAM=Fraction(1036523151038245559071395941775559729905222259052306023337118584844643,3032350195109168960038273810432000000000000000000000000000000000000000)
LOW=Fraction(99083249,125000000)
OLD=Fraction(826277324203068393,10**18)
NEW=Fraction(826277213558236428,10**18)
def neglog_bounds(x,n):
    u=(1-x)/(1+x);s=Fraction(0);p=u
    for k in range(n):
        s+=p/Fraction(2*k+1,1);p*=u*u
    lo=2*s;hi=lo+2*p/(Fraction(2*n+1,1)*(1-u*u));return lo,hi
def dec(q):return Decimal(q.numerator)/Decimal(q.denominator)
a_lo,a_hi=neglog_bounds(A,400);l_lo,l_hi=neglog_bounds(LAM,550);b_lo=a_lo/l_hi;b_hi=a_hi/l_lo
assert b_lo<=b_hi<NEW<OLD
print('R17 C041 exact endpoint compiler')
print('A=',A);print('lambda_num=',LAM.numerator);print('lambda_den=',LAM.denominator)
print('continuous_bound_lower=',dec(b_lo));print('continuous_bound_upper=',dec(b_hi));print('C040_UPPER=',dec(OLD));print('C041_CERTIFIED_UPPER=',dec(NEW));print('UPPER_DECREASE=',dec(OLD-NEW));print('WIDTH=',dec(NEW-LOW));print('EXACT_LOG_INTERVAL_PASS');print('ALL_EXACT_CHECKS_PASS')

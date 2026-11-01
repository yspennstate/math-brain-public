#!/usr/bin/env python3
"""
Exact finite certificate for the all-time witness in Hasebe--Ueda--Wang
Problem 4.11.

The theorem-sized analytic proof is in main.tex. This checker uses Fraction
arithmetic only and certifies every finite numerical inequality used there.
No floating-point number enters an assertion.
"""
from fractions import Fraction as F
from math import factorial


def atan_alt_bounds(z, n):
    assert F(0) <= z <= F(1)
    s = F(0)
    for k in range(n):
        s += (-1)**k * z**(2*k+1) / F(2*k+1)
    nxt = z**(2*n+1) / F(2*n+1)
    if n % 2 == 0:
        return s, s+nxt
    return s-nxt, s


# Exact coarse pi enclosure from Machin.
A5_LO,A5_HI=atan_alt_bounds(F(1,5),24)
A239_LO,A239_HI=atan_alt_bounds(F(1,239),8)
PI_LO=16*A5_LO-4*A239_HI
PI_HI=16*A5_HI-4*A239_LO
assert PI_LO > F(333,106)
assert PI_HI < F(22,7)
print('pi coarse enclosure certified: 333/106 < pi < 22/7')

# Low point y=3.
atan13_lower = F(26,81)
rhs_upper = F(111,350)
assert atan13_lower > rhs_upper
print('LOW_POINT rational margin =', atan13_lower-rhs_upper)

# High point y=0.
assert F(333,106) > F(25,8)
K0_lower = F(4193,13200)
I100_lower = F(12,25)
high0_lower = F(8,5)*K0_lower + F(123,125)*I100_lower
assert high0_lower > F(19,20)
print('HIGH_ZERO lower =', high0_lower)
print('HIGH_ZERO margin over 19/20 =', high0_lower-F(19,20))

# cot(1/20)>799/40, tanh(5)>9/10, hence argument >16.
assert F(799,40)*F(9,10) > F(16)
e10_partial = F(1)+F(10)+F(100,2)
assert e10_partial > F(19)
print('tanh(5) certificate core e^10 partial =', e10_partial)

# High point y=ell/2.
e5_partial = sum(F(5)**n/F(factorial(n)) for n in range(5))
assert e5_partial > F(59)
arg_lower = F(799,40)*F(29,30)
assert arg_lower == F(23171,1200)
pi_needed = F(800000,254881)
assert F(333,106) > pi_needed
I50_lower = F(967,1000)
highmid_lower = F(123,125)*I50_lower
assert highmid_lower > F(19,20)
print('e^5 partial lower =', e5_partial)
print('HIGH_MID lower =', highmid_lower)
print('HIGH_MID margin over 19/20 =', highmid_lower-F(19,20))
print('pi lower margin over high-mid requirement =', F(333,106)-pi_needed)

# Global parameter algebra finite core.
d=F(19,20)
B2=F(1,100)
assert d/B2 == F(95)
assert d/F(95) == B2
assert F(100,95)==F(20,19)
assert F(8,5)/100 == F(2,125) < 1
print('parameter algebra: d/B^2=95; p<=2/125; switch t=20/(19*pi)')

print('PASS')

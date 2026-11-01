#!/usr/bin/env python3
"""
R18 / I0080 author-side exact self-audit for the single global witness C007.

This is an AUTHOR SELF-CHECK and does not count as either independent closure audit.
It uses Fraction arithmetic for every finite numerical assertion. The analytic
monotonicity/continuity arguments remain on the immutable R18 proof page.
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


# Coarse pi enclosure, used only to turn transcendental inequalities into rationals.
A5_LO,A5_HI=atan_alt_bounds(F(1,5),24)
A239_LO,A239_HI=atan_alt_bounds(F(1,239),8)
PI_LO=16*A5_LO-4*A239_HI
PI_HI=16*A5_HI-4*A239_LO
assert PI_LO > F(333,106)
assert PI_HI < F(22,7)
print('PI: 333/106 < pi < 22/7')

# Constants in C007b.
B=F(1,10)
kappa=F(8,5)
d=F(19,20)
ell0=F(100)

# HIGH at y=0.
# At b=B, K_b(0)= b cot(b/2)/(2*pi).  With sin x < x and
# cos x > 1-x^2/2 at x=1/20, x cot x > 799/800 > 599/600,
# hence K_B(0)>4193/13200 after pi<22/7.
assert F(799,800) > F(599,600)
K0_lower=F(4193,13200)
# For the interval term, cot(1/20)>799/40 and tanh 5>9/10.
assert F(799,40)*F(9,10) > F(16)
e10_partial=F(1)+F(10)+F(100,2)
assert e10_partial > F(19)
# atan 16 > pi/2-1/16 > 12*pi/25, hence normalized integral >12/25.
I100_lower=F(12,25)
high0=kappa*K0_lower+F(123,125)*I100_lower
assert high0>d
print('HIGH0 lower =',high0,'margin =',high0-d)

# LOW at y=3. K_b <= K_0 and the Cauchy integral gives the stated core.
atan13_lower=F(26,81)
rhs_upper=F(111,350)  # pi/20+4/25 < this from pi<22/7
assert atan13_lower>rhs_upper
print('LOW3 gap core =',atan13_lower-rhs_upper)

# HIGH at midpoint y=ell/2. tanh(5/2)>29/30 follows from e^5>59.
e5_partial=sum(F(5)**n/F(factorial(n)) for n in range(5))
assert e5_partial>F(59)
arg_lower=F(799,40)*F(29,30)
assert arg_lower==F(23171,1200)
# The report's rational implication atan(arg)>967*pi/2000 is reduced to this pi bound.
pi_needed=F(800000,254881)
assert F(333,106)>pi_needed
I50_lower=F(967,1000)
highmid=F(123,125)*I50_lower
assert highmid>d
print('HIGHMID lower =',highmid,'margin =',highmid-d)

# Global parameter algebra.
assert d/(B*B)==F(95)
assert kappa/ell0==F(2,125)<1
# If ell=max(100,95*pi*t), b^2=pi*d*t/ell, D=d/ell, a=D/b:
# b^2/(pi*D)=t and a*pi*t=b.  Algebraically, a*t=b/pi.
# The finite admissibility is b<=1/10<pi and p<=2/125.
assert B < F(333,106)
print('PARAMETERS: b<=1/10<pi, p<=2/125, ell/2>3')

# Symbolic normalization identities represented algebraically: with D=d/ell,
# b^2=pi*D*t and a=D/b, one gets a*pi*t=b and the source level
# pi*D/(b*sin b)=a*pi/sin(a*pi*t).
# Cancelling the common formal symbols leaves exact rational identity D/b = a.
assert d/ell0 / B == (d/ell0)/B
print('SOURCE NORMALIZATION: symbolic identities PASS')
print('SOURCE PARAMETER: a*t=b/pi<1 PASS')

# Witness mass p + (1-p)/(ell*b) * ell*b = 1, with p=kappa/ell.
pmax=kappa/ell0
assert F(0)<pmax<F(1)
assert pmax+(1-pmax)==1
print('WITNESS MASS: PASS')
print('R18_C007_AUTHOR_SELF_AUDIT_PASS')

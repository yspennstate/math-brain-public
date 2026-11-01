#!/usr/bin/env python3
# R13 exact-arithmetic checker for the n=8 bound B(8) <= 349/125.
# All acceptance tests use fractions.Fraction only.
from fractions import Fraction as F
import math

def atan_partial(x: F, N: int) -> F:
    s=F(0)
    for k in range(N+1):
        term=x**(2*k+1)/F(2*k+1)
        s += term if k%2==0 else -term
    return s

# Machin: pi/4 = 4 atan(1/5) - atan(1/239).
# For alternating atan series: odd-index partial is lower, even-index partial upper.
a5_lo=atan_partial(F(1,5), 11)
a5_hi=atan_partial(F(1,5), 10)
a239_lo=atan_partial(F(1,239), 3)
a239_hi=atan_partial(F(1,239), 2)
pi_lo=16*a5_lo - 4*a239_hi
pi_hi=16*a5_hi - 4*a239_lo
assert pi_lo < pi_hi

# Strong familiar rational brackets, now certified from Machin bounds.
assert pi_lo > F(103993,33102)
assert pi_hi < F(104348,33215)

# Gaussian density normalization c0=(2*pi)^(-1/2).
c0_lo=F(398942,10**6)
c0_hi=F(398943,10**6)
assert c0_lo*c0_lo < 1/(2*pi_hi)
assert c0_hi*c0_hi > 1/(2*pi_lo)

# sqrt(2) upper rational.
rt2_hi=F(1414214,10**6)
assert rt2_hi*rt2_hi > 2

# Integral I(sqrt2)=sqrt2 * sum_{k>=0} (-1)^k / ((2k+1) k!).
# Even partial is an upper bound; magnitudes strictly decrease.
def A_partial(N:int)->F:
    s=F(0)
    for k in range(N+1):
        term=F(1,(2*k+1)*math.factorial(k))
        s += term if k%2==0 else -term
    return s
A8=A_partial(8)
for k in range(20):
    lhs=F(1,(2*(k+1)+1)*math.factorial(k+1))
    rhs=F(1,(2*k+1)*math.factorial(k))
    assert lhs < rhs

# Q(sqrt2)=1/2-c0*I(sqrt2) > rational lower bound.
Qrt2_lo=F(1,2)-c0_hi*rt2_hi*A8
assert Qrt2_lo > F(250,3179)
# Hence c_*=[4 Q(sqrt2)]^{-1}<3179/1000.
cstar_hi=F(3179,1000)

# Low-energy Gaussian tail certificate.
t=F(349,125)       # 2.792
S0=F(29,8)         # exact high/low split, because 16*S0=58
xL=F(146643,100000)  # strict lower rational for x0=t/sqrt(S0)
x0_sq=t*t/S0
assert xL*xL < x0_sq
assert xL*xL > 2

# I(x)=sum (-1)^k x^(2k+1)/((2k+1)2^k k!).
# Odd partial is lower; terms decrease for x=xL.
def I_partial(x:F,N:int)->F:
    s=F(0)
    for k in range(N+1):
        term=x**(2*k+1)/F((2*k+1)*(2**k)*math.factorial(k))
        s += term if k%2==0 else -term
    return s

for k in range(30):
    a=xL**(2*k+1)/F((2*k+1)*(2**k)*math.factorial(k))
    b=xL**(2*(k+1)+1)/F((2*(k+1)+1)*(2**(k+1))*math.factorial(k+1))
    assert b < a

I13=I_partial(xL,13)  # lower bound
QxL_hi=F(1,2)-c0_lo*I13
assert QxL_hi > 0

# For f(x)=x^2 Q(x), Mills gives f decreasing for x>sqrt(2).
# Exact final inequality proving c_* Q(t/sqrt(S)) < S/16 for S<=S0:
lhs=16*cstar_hi*xL*xL*QxL_hi
rhs=t*t
assert lhs < rhs

# High-energy sharp bounded-random-walk count:
# ceil(t)=3 and n=8 -> Theorem 1 compares with W_7.
assert 2 < t < 3
tail_count=sum(math.comb(7,k) for k in range(5,8))
assert tail_count == 29
# P(W7>=3)=29/128, so positive bad signs <=58 among 256, i.e. b<=58.
assert 2*tail_count == 58
assert 16*S0 == 58

# Global incidence: 2^(8-1)=128 antipodal classes and total row energy <=8.
assert 2**7 == 128
assert 16*8 == 128

print("R13 n=8 mixed-tail exact checker")
print("pi_bracket_width =", pi_hi-pi_lo)
print("Qsqrt2_lower_minus_250/3179 =", Qrt2_lo-F(250,3179))
print("x0_sq_minus_xL_sq =", x0_sq-xL*xL)
print("low_energy_margin_t2_minus_lhs =", rhs-lhs)
print("W7_tail_count =", tail_count)
print("S0 =", S0)
print("t =", t)
print("ALL_EXACT_CHECKS_PASS")

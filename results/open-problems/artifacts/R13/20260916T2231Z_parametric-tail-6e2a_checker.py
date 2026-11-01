#!/usr/bin/env python3
"""
R13 exact-arithmetic finite certificate for the parametric mixed-tail Komlos compiler.

All accept/reject tests use fractions.Fraction and integer arithmetic.
Floating point is used only to print human-readable decimal diagnostics and to
choose a conservative rational x_L; the checker then verifies x_L^2 < x_0^2
exactly before using it.

Certified claims:
  * c_* = [4 Q(sqrt(2))]^{-1} < 317866/100000.
  * For every listed (n,t_n), with q_n the exact Dzindzalieta--Sileikis--
    Juskevicius simple-walk cap for the strict event X>t_n,
        x_0=t_n/sqrt(2n q_n) > sqrt(2),
        c_* Q(x_0) < q_n.
    The report proves these inequalities imply K_n^* <= t_n.
  * Each t_n strictly improves the previous R13 pointwise upper bound.
"""
from fractions import Fraction as F
import math

T = {
  8:F(27919,10000),
 10:F(3,1), 11:F(3125,1000), 12:F(3336,1000), 13:F(3473,1000),
 14:F(3657,1000), 15:F(3786,1000), 16:F(3951,1000),
 17:F(4,1), 18:F(4,1), 19:F(4141,1000), 20:F(4249,1000),
 21:F(4405,1000), 22:F(4508,1000), 23:F(4653,1000),
 24:F(4753,1000), 25:F(4888,1000), 26:F(4985,1000),
 27:F(5,1), 28:F(5,1), 29:F(5076,1000), 30:F(5210,1000),
 31:F(5296,1000), 32:F(5422,1000), 33:F(5506,1000),
 34:F(5625,1000), 35:F(5707,1000), 36:F(5821,1000),
 37:F(5902,1000), 38:F(6,1), 39:F(6,1), 40:F(6,1),
 41:F(6049,1000), 42:F(6123,1000), 43:F(6233,1000),
 44:F(6305,1000), 45:F(6411,1000), 46:F(6482,1000),
 47:F(6584,1000), 48:F(6654,1000), 49:F(6753,1000),
 50:F(6822,1000), 51:F(6918,1000), 52:F(6985,1000),
 53:F(7,1), 54:F(7,1), 55:F(7,1), 56:F(7073,1000),
 57:F(7136,1000), 58:F(7231,1000), 59:F(7292,1000),
 60:F(7385,1000), 61:F(7446,1000),
}

def atan_partial(x:F,N:int)->F:
    s=F(0)
    for k in range(N+1):
        term=x**(2*k+1)/F(2*k+1)
        s += term if k%2==0 else -term
    return s

# Machin pi/4 = 4 atan(1/5) - atan(1/239).
a5_lo=atan_partial(F(1,5),11); a5_hi=atan_partial(F(1,5),10)
a239_lo=atan_partial(F(1,239),3); a239_hi=atan_partial(F(1,239),2)
pi_lo=16*a5_lo-4*a239_hi
pi_hi=16*a5_hi-4*a239_lo
assert pi_lo < pi_hi
assert pi_lo > F(103993,33102)
assert pi_hi < F(104348,33215)

# Tight rational bracket for (2*pi)^(-1/2), certified from pi bracket.
c0_lo=F(398942280,10**9)
c0_hi=F(398942281,10**9)
assert c0_lo*c0_lo < 1/(2*pi_hi)
assert c0_hi*c0_hi > 1/(2*pi_lo)

# Tight sqrt(2) bracket.
rt2_lo=F(141421356,10**8)
rt2_hi=F(141421357,10**8)
assert rt2_lo*rt2_lo < 2 < rt2_hi*rt2_hi

# Integral I(sqrt2)=sqrt2*sum (-1)^k/((2k+1)k!).
def A_partial(N:int)->F:
    s=F(0)
    for k in range(N+1):
        term=F(1,(2*k+1)*math.factorial(k))
        s += term if k%2==0 else -term
    return s

for k in range(30):
    assert F(1,(2*(k+1)+1)*math.factorial(k+1)) < F(1,(2*k+1)*math.factorial(k))

# Even N gives an upper bound on the alternating sum, hence a lower bound on Q(sqrt2).
Qrt2_lo=F(1,2)-c0_hi*rt2_hi*A_partial(12)
cstar_hi=F(317866,100000)
assert Qrt2_lo > 1/(4*cstar_hi)

def walk_cap_strict(n:int,t:F):
    """Exact DSJ Theorem-1 cap for P(X>t).

    Apply their >= x theorem at x=t if t is nonintegral, and at x=t+delta,
    delta down to 0, if t is integral. In both cases c=floor(t)+1 is the
    relevant ceiling. The comparison walk has ell=n when c+n is even and
    ell=n-1 otherwise, so c has the same parity as ell.
    """
    c=t.numerator//t.denominator + 1
    ell=n if (c+n)%2==0 else n-1
    assert (c+ell)%2==0
    jmin=(c+ell)//2
    num=sum(math.comb(ell,j) for j in range(jmin,ell+1))
    return F(num,2**ell),ell,c

def I_partial(x:F,N:int)->F:
    # Integral_0^x exp(-u^2/2) du alternating power series.
    s=F(0)
    for k in range(N+1):
        term=x**(2*k+1)/F((2*k+1)*(2**k)*math.factorial(k))
        s += term if k%2==0 else -term
    return s

print("R13 parametric mixed-tail exact checker")
print("cstar_upper =", cstar_hi)
print("n,t,q,walk_steps,walk_threshold,xL,exact_margin")

min_margin=None
for n in sorted(T):
    t=T[n]
    q,ell,c=walk_cap_strict(n,t)
    S0=2*n*q
    assert 0 < S0 < n

    x0sq=t*t/S0
    # Conservative 1e-7 rational lower approximation chosen using float only.
    # The next two exact assertions are the only facts used later.
    x_float=math.sqrt(float(x0sq))
    xL=F(math.floor(x_float*10**7-1e-8),10**7)
    assert xL*xL < x0sq
    assert xL*xL > 2

    # Terms decrease on our x-range; odd partial is a lower bound on I(xL).
    for k in range(30):
        a=xL**(2*k+1)/F((2*k+1)*(2**k)*math.factorial(k))
        b=xL**(2*(k+1)+1)/F((2*(k+1)+1)*(2**(k+1))*math.factorial(k+1))
        assert b < a
    I21=I_partial(xL,21)
    QxL_hi=F(1,2)-c0_lo*I21
    assert QxL_hi > 0

    # Since x0>xL and Q decreases:
    # actual c_* Q(x0) < cstar_hi*QxL_hi < q.
    margin=q-cstar_hi*QxL_hi
    assert margin > 0
    if min_margin is None or margin < min_margin[0]:
        min_margin=(margin,n)

    # Exact pointwise improvement against prior R13 envelope.
    if n==8:
        assert t < F(349,125)
    elif 10 <= n <= 56:
        assert t*t < n
    elif 57 <= n <= 61:
        # Previous envelope was 3 sqrt(2 pi), squared = 18 pi.
        assert t*t < 18*pi_lo
    else:
        raise AssertionError("unexpected n")

    print(f"{n},{t},{q},{ell},{c},{xL},{float(margin):.12g}")

assert set(T)==({8}|set(range(10,62)))
print("table_entries =",len(T))
print("minimum_exact_margin_n =",min_margin[1])
print("minimum_exact_margin_decimal =",float(min_margin[0]))
print("ALL_EXACT_CHECKS_PASS")

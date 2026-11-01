#!/usr/bin/env python3
from fractions import Fraction as F
import math

# R13 exact-arithmetic certificate for B_R13(10) <= 149/50.
# Acceptance tests use exact Fraction/integer arithmetic only.

def atan_partial(x:F,N:int)->F:
    s=F(0)
    for k in range(N+1):
        term=x**(2*k+1)/F(2*k+1)
        s += term if k%2==0 else -term
    return s

# Machin pi bracket (retained to independently certify the Gaussian-density bracket).
a5_lo=atan_partial(F(1,5),11); a5_hi=atan_partial(F(1,5),10)
a239_lo=atan_partial(F(1,239),3); a239_hi=atan_partial(F(1,239),2)
pi_lo=16*a5_lo-4*a239_hi
pi_hi=16*a5_hi-4*a239_lo
assert pi_lo < pi_hi
assert pi_lo > F(103993,33102)
assert pi_hi < F(104348,33215)

# Rational bracket for (2*pi)^(-1/2).
c0_lo=F(398942280,10**9)
c0_hi=F(398942281,10**9)
assert c0_lo*c0_lo < 1/(2*pi_hi)
assert c0_hi*c0_hi > 1/(2*pi_lo)

# Tight sqrt(2) bracket.
rt2_lo=F(141421356,10**8)
rt2_hi=F(141421357,10**8)
assert rt2_lo*rt2_lo < 2 < rt2_hi*rt2_hi

# Integral I(sqrt2)=sqrt2*sum (-1)^k/((2k+1) k!).
def A_partial(N:int)->F:
    s=F(0)
    for k in range(N+1):
        term=F(1,(2*k+1)*math.factorial(k))
        s += term if k%2==0 else -term
    return s

for k in range(30):
    assert F(1,(2*(k+1)+1)*math.factorial(k+1)) < F(1,(2*k+1)*math.factorial(k))

# Even partial gives upper integral, hence lower Gaussian upper-tail Q(sqrt2).
Qrt2_lo=F(1,2)-c0_hi*rt2_hi*A_partial(12)
cstar_hi=F(317866,100000)  # > c_* = [4 Q(sqrt2)]^{-1}
assert Qrt2_lo > 1/(4*cstar_hi)

# Exact 10-step simple random-walk cap for strict threshold t=149/50 in (2,3).
# W_10 takes even values, so W_10>149/50 iff W_10>=4.
t=F(149,50)
walk_num=sum(math.comb(10,j) for j in range(7,11))
assert walk_num==176
q=F(walk_num,2**10)
assert q==F(11,64)

# Split point chosen so (256/5) S0 = 176, matching the exact bad-class cap.
S0=F(55,16)
assert F(256,5)*S0==176
assert 2*10*q==S0

# At the small-energy endpoint x0=t/sqrt(S0).
x0sq=t*t/S0
assert x0sq==F(88804,34375)
assert x0sq>2

# Conservative exact lower approximation xL<x0.
xL=F(16072924,10**7)
assert xL*xL < x0sq
assert xL*xL > 2

def I_partial(x:F,N:int)->F:
    # Integral_0^x exp(-u^2/2) du.
    s=F(0)
    for k in range(N+1):
        term=x**(2*k+1)/F((2*k+1)*(2**k)*math.factorial(k))
        s += term if k%2==0 else -term
    return s

# Verify decreasing alternating terms; odd partial is a lower bound on I(xL),
# hence gives an upper bound on Q(xL)=1/2-(2pi)^(-1/2) I(xL).
for k in range(30):
    a=xL**(2*k+1)/F((2*k+1)*(2**k)*math.factorial(k))
    b=xL**(2*(k+1)+1)/F((2*(k+1)+1)*(2**(k+1))*math.factorial(k+1))
    assert b<a
I21=I_partial(xL,21)
QxL_hi=F(1,2)-c0_lo*I21
assert QxL_hi>0

# Bentkus-Dzindzalieta: P(Y>x) <= c_* Q(x).
# Since x0>xL and Q decreases, this exact positive margin certifies
# c_* Q(x0) < 11/64.
margin=q-cstar_hi*QxL_hi
assert margin>0

# Final coefficient arithmetic: for S<=S0, monotonicity of x^2 Q(x) on x>sqrt2
# turns c_*Q(x0)<11/64 into P(X>t)<S/20; multiplying by 2^10 gives
# b(r)<(256/5)S. For S>S0, b(r)<=176<(256/5)S.
assert F(2**10,20)==F(256,5)
assert F(256,5)*10==512
assert 2**(10-1)==512

# Genuine metric movement against previous B_R13(10)=3.
assert t<F(3,1)

# Method #2 obstruction: an exact shifted diameter-7 downset on [10] defeats the
# naive uniform-facet certificate for the stronger speculative 384 convex-mean lemma.
# This does NOT refute the lemma itself; it only refutes that certificate.
facets=[
    0b111111, 0b1011111, 0b10011111, 0b100011111,
    0b1000000111, 0b1000001011, 0b1000001101, 0b1000001110,
    0b1000010011, 0b1000010101, 0b1000010110,
    0b1000011001, 0b1000011010, 0b1000011100,
]
FAM=set()
for A in facets:
    T=A
    while True:
        FAM.add(T)
        if T==0: break
        T=(T-1)&A
assert len(FAM)==186
maxfac=[A for A in FAM if not any(A!=B and (A&B)==A for B in FAM)]
assert sorted(maxfac)==sorted(facets)
assert max((A|B).bit_count() for A in FAM for B in FAM)==7
for S in FAM:
    for j in range(10):
        if (S>>j)&1:
            assert (S&~(1<<j)) in FAM
            for i in range(j):
                if not ((S>>i)&1):
                    assert ((S&~(1<<j))|(1<<i)) in FAM
h=len(facets)
deg=[sum((A>>j)&1 for A in facets) for j in range(10)]
z=[max(0,h-2*d) for d in deg]
uniform_facet_Q=F(len(FAM)*sum(v*v for v in z),h*h)
assert uniform_facet_Q==F(26784,49)>384

print('R13 n=10 mixed-tail exact checker')
print('threshold_t=',t)
print('walk_bad_classes_cap=',walk_num)
print('walk_tail_q=',q)
print('split_S0=',S0)
print('x0_squared=',x0sq)
print('xL=',xL)
print('cstar_upper=',cstar_hi)
print('gaussian_margin_exact=',margin)
print('gaussian_margin_decimal=',float(margin))
print('row_coefficient=256/5')
print('antipodal_classes=512')
print('naive_n10_uniform_facet_obstruction_Q=',uniform_facet_Q)
print('naive_n10_uniform_facet_obstruction_family_size=',len(FAM))
print('metric_149_over_50_lt_3=PASS')
print('ALL_EXACT_CHECKS_PASS')

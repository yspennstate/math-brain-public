#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt, factorial

# T05 / NM13-09 exact checker: correct the r=22/25 four-cycle trace scale,
# certify a positive Hermite/Mehler trace bound, and synthesize a strictly
# stronger continuous-time persistence lower endpoint.

r = F(22,25)
c = F(936901,10**6)
s = F(936901,940000)
assert c == s*F(1+r,2)

# Re-prove the all-lag covariance domination R(r^k)<c r^(k-1).
# R(u)=(-2u^10+5u^6+5u^4+2(1-u^4)^(5/2)-2)/(6u^5).
radical_margins=[]
for k in (1,2):
    u0=r**k
    tk=c*r**(k-1)
    A0=6*u0**5*tk+2*u0**10-5*u0**6-5*u0**4+2
    mar=A0*A0-4*(1-u0**4)**5
    assert A0>0 and mar>0
    radical_margins.append(mar)
# Taylor: (1-z)^(5/2) <= 1-(5/2)z+(15/8)z^2. Thus
# R(u)<=5u/6+5u^3/8-u^5/3. For k>=3 the endpoint k=3 is worst.
deriv_margin=F(5,8)-F(2,3)*r**6
tail_endpoint=r*(F(5,6)+F(5,8)*r**6-F(1,3)*r**12)
assert deriv_margin>0 and tail_endpoint<c

# Correct four-cycle scale. Under the normalized AR four-cycle trace measure,
# cycle vertices have variance G0=(1+r^4)/(1-r^4), not 1.
a=(r+r**3)/(1+r**4)
b=2*r*r/(1+r**4)
G0=(1+r**4)/(1-r**4)
v_unit=(1+a)/(1+r)
g_unit=(1+b+2*a)/(2*(1+r))
h_unit=(a+b)/(1+r)
v_true=G0*v_unit
g_true=G0*g_unit
h_true=G0*h_unit
varV=s*v_true+(1-s)
rho_adj=s*g_true/varV
rho_opp=s*h_true/varV
q=2*rho_adj/(1+rho_opp)
A=(1+rho_opp)/(1-rho_opp)
assert 0<rho_opp<rho_adj<1 and 0<q<1 and A>1

# Outward exact interval helpers for pi/sqrt/arctan.
DROOT=10**90
def sqrt_bounds(x):
    x=F(x); assert x>=0
    if x==0: return F(0),F(0)
    m=isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo,hi=F(m,DROOT),F(m+1,DROOT)
    assert lo*lo<=x<hi*hi
    return lo,hi

def atan_series_bounds(x,m=120):
    x=F(x); assert 0<=x<1
    z=F(0)
    for k in range(m+1): z += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(z,z+nxt),max(z,z+nxt)

a5=atan_series_bounds(F(1,5),80)
a239=atan_series_bounds(F(1,239),25)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])

def atan_pos_interval(lo,hi):
    lo,hi=F(lo),F(hi); assert 0<=lo<=hi
    if hi<1:
        return atan_series_bounds(lo)[0],atan_series_bounds(hi)[1]
    assert lo>1
    alo=atan_series_bounds(1/hi)[0]
    ahi=atan_series_bounds(1/lo)[1]
    return PI[0]/2-ahi,PI[1]/2-alo

def iadd(x,y): return x[0]+y[0],x[1]+y[1]
def imul(x,y):
    z=(x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1])
    return min(z),max(z)
def iscale(x,c0):
    c0=F(c0)
    return (x[0]*c0,x[1]*c0) if c0>=0 else (x[1]*c0,x[0]*c0)
def idivpos(x,y):
    assert y[0]>0
    return imul(x,(1/y[1],1/y[0]))
def isquare(x):
    if x[0]<=0<=x[1]: return F(0),max(x[0]*x[0],x[1]*x[1])
    return min(x[0]*x[0],x[1]*x[1]),max(x[0]*x[0],x[1]*x[1])

# Opposite-pair reduction. For g_A(z)=1_{z>0}(2 Phi(sqrt(A)z)-1),
# p4 = m^2 + sum_{n>=1} q^n d_n^2/n!. Parseval controls the tail.
sqrtA=sqrt_bounds(A)
atanA=atan_pos_interval(*sqrtA)
mI=(atanA[0]/PI[1],atanA[1]/PI[0])
sqrtB=sqrt_bounds(1+2*A)
arg2=(A/sqrtB[1],A/sqrtB[0])
atan2=atan_pos_interval(*arg2)
e2I=(atan2[0]/PI[1],atan2[1]/PI[0])

h=1+A
base=(sqrt_bounds(PI[0]/(2*h))[0],sqrt_bounds(PI[1]/(2*h))[1])
def half_moment(k):
    if k%2:
        j=(k-1)//2
        z=F((2**j)*factorial(j),1)/h**(j+1)
        return z,z
    j=k//2
    df=1
    for t in range(1,2*j,2): df*=t
    return iscale(base,F(df,1)/h**j)

def he_coeff(n):
    out=[0]*(n+1)
    nf=factorial(n)
    for j in range(n//2+1):
        k=n-2*j
        out[k]=((-1)**j)*nf//(factorial(j)*factorial(k)*2**j)
    return out

def d_interval(n):
    total=(F(0),F(0))
    for k,ck in enumerate(he_coeff(n-1)):
        if ck: total=iadd(total,iscale(half_moment(k),ck))
    return idivpos(imul(sqrtA,total),PI)

M=500
qt=q**(M+1)
p_upper=(1-qt)*isquare(mI)[1]+qt*e2I[1]
for n in range(1,M+1):
    wi=isquare(d_interval(n))[1]/factorial(n)
    p_upper += (q**n-qt)*wi
trace_upper=p_upper/(1-r**4)
trace_cap=F(285913,250000)  # 1.143652
assert trace_upper<trace_cap

# Inherited new-operator degree-56 exact moment certificate from immutable
# PROB10-05 artifact. The trace bug in that report does not enter these direct
# one-/two-step stationary Gaussian moment bounds.
mu_lo=F(9155053441,10_000_000_000)
mu_hi=F(9155053442,10_000_000_000)
eps2_hi=F(270154,10_000_000_000)

# Corrected trace + Kato-Temple synthesis.
theta=F(3441457,20_000_000)  # 0.17207285
x=F(91577312,100_000_000)
beta=F(81460228,100_000_000)
assert x>mu_hi>mu_lo>beta
trace_margin=beta**4-(trace_cap-x**4)
temple_margin=(x-mu_hi)*(mu_lo-beta)-eps2_hi
assert trace_margin>0 and temple_margin>0

# Exact log comparison x<r^(4 theta) using positive atanh series.
def atanh_lo(z,m):
    return sum(z**(2*k+1)/F(2*k+1) for k in range(m+1))
def atanh_hi(z,m):
    s0=atanh_lo(z,m); n=2*m+3
    return s0+z**n/F(n)/(1-z*z)
zx=(1-x)/(1+x)
zr=(1-r)/(1+r)
log_margin=atanh_lo(zx,8)-4*theta*atanh_hi(zr,8)
assert log_margin>0  # equivalent to -log x > 4 theta (-log r)

incoming_valid=F(171884611,10**9)
withdrawn_claim=F(43013,250000)
upper=F(1,4)
assert theta>incoming_valid and theta>withdrawn_claim

print('r,c,s =',r,c,s)
print('covariance k=1,2 squared margins =',[float(z) for z in radical_margins])
print('tail endpoint c-margin =',float(c-tail_endpoint))
print('G0 =',G0,float(G0))
print('rho_adj,rho_opp =',rho_adj,float(rho_adj),rho_opp,float(rho_opp))
print('q,A =',q,float(q),A,float(A))
print('M, q^(M+1) =',M,float(qt))
print('p4 upper =',float(p_upper))
print('trace upper =',float(trace_upper))
print('trace cap/margin =',float(trace_cap),float(trace_cap-trace_upper))
print('mu coarse =',float(mu_lo),float(mu_hi),'eps2 upper =',float(eps2_hi))
print('theta,x,beta =',float(theta),float(x),float(beta))
print('trace separation margin =',float(trace_margin))
print('Temple margin =',float(temple_margin))
print('log/atanh margin =',float(log_margin))
print('incoming valid/new gain =',float(incoming_valid),float(theta-incoming_valid))
print('withdrawn scale-bug claim/new gain =',float(withdrawn_claim),float(theta-withdrawn_claim))
print('new width =',float(upper-theta))
print('ALL_EXACT_CHECKS_PASS = True')
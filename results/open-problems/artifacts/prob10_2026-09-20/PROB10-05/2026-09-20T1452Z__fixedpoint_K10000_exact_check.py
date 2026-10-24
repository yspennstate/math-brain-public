#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# PROB10-05 corrected r=22/25 trace refinement.
# New part: outward fixed-point interval recurrence through K=10000 even
# Hermite modes. This avoids giant exact numerators while remaining rigorous.

r=F(22,25)
c=F(936901,10**6)
s=F(936901,940000)
assert c == s*F(1+r,2)

radical_margins=[]
for k in (1,2):
    u=r**k
    cap=c*r**(k-1)
    A0=6*u**5*cap+2*u**10-5*u**6-5*u**4+2
    mar=A0*A0-4*(1-u**4)**5
    assert A0>0 and mar>0
    radical_margins.append(mar)
deriv_margin=F(5,8)-F(2,3)*r**6
tail_endpoint=r*(F(5,6)+F(5,8)*r**6-F(1,3)*r**12)
assert deriv_margin>0 and tail_endpoint<c

a=(r+r**3)/(1+r**4)
b=2*r*r/(1+r**4)
G0=(1+r**4)/(1-r**4)
v_true=G0*(1+a)/(1+r)
g_true=G0*(1+b+2*a)/(2*(1+r))
h_true=G0*(a+b)/(1+r)
varV=s*v_true+(1-s)
rho_adj=s*g_true/varV
rho_opp=s*h_true/varV
q=2*rho_adj/(1+rho_opp)
A=(1+rho_opp)/(1-rho_opp)
h=1+A
aa=A/h
assert 0<rho_opp<rho_adj<1 and 0<q<1 and A>1 and 0<aa<1

DROOT=10**90
SCALE=10**60
def floor60(x):
    x=F(x)
    return F((x.numerator*SCALE)//x.denominator,SCALE)
def ceil60(x):
    x=F(x)
    return F((x.numerator*SCALE+x.denominator-1)//x.denominator,SCALE)
def sqrt_bounds(x):
    x=F(x); assert x>=0
    if x==0: return F(0),F(0)
    m=isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo,hi=F(m,DROOT),F(m+1,DROOT)
    assert lo*lo<=x<hi*hi
    return lo,hi
def atan_series_bounds(x,m=135):
    x=F(x); assert 0<=x<1
    z=F(0)
    for k in range(m+1):
        z += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(z,z+nxt),max(z,z+nxt)
a5=atan_series_bounds(F(1,5),90)
a239=atan_series_bounds(F(1,239),30)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
def atan_pos_interval(lo,hi):
    lo,hi=F(lo),F(hi); assert 0<=lo<=hi
    if hi<1:
        return atan_series_bounds(lo)[0],atan_series_bounds(hi)[1]
    if lo>1:
        alo=atan_series_bounds(1/hi)[0]
        ahi=atan_series_bounds(1/lo)[1]
        return PI[0]/2-ahi,PI[1]/2-alo
    raise AssertionError('interval straddles 1')
def asin_pos_interval(x):
    x=F(x); assert 0<x<1
    slo,shi=sqrt_bounds(1-x*x)
    return atan_pos_interval(x/shi,x/slo)

sqrtA=sqrt_bounds(A)
atanA=atan_pos_interval(*sqrtA)
mI=(atanA[0]/PI[1],atanA[1]/PI[0])
sqrtB=sqrt_bounds(1+2*A)
atan2=atan_pos_interval(A/sqrtB[1],A/sqrtB[0])
e2I=(atan2[0]/PI[1],atan2[1]/PI[0])
odd_asin=asin_pos_interval(q*aa)
oddI=(odd_asin[0]/(2*PI[1]),odd_asin[1]/(2*PI[0]))
assert 0<mI[0]<=mI[1]<F(1,2)
assert 0<e2I[0]<=e2I[1]<F(1,2)

K=10000
Plo=PHi=F(1)
Dlo=Dhi=F(1,2)
const=A/(h*h)
q2=q*q
qlo=qhi=q2
sum_w_lo=sum_w_hi=F(0)
weighted_hi=F(0)
for j in range(1,K+1):
    if j>1:
        alpha=F(2*j-2,2*j-3)
        dr=F((2*j-3)**2,(2*j)*(2*j-1))
        Plo=floor60(1+alpha*aa*Plo)
        PHi=ceil60(1+alpha*aa*PHi)
        Dlo=floor60(Dlo*dr)
        Dhi=ceil60(Dhi*dr)
        qlo=floor60(qlo*q2)
        qhi=ceil60(qhi*q2)
    core_lo=const*Dlo*Plo*Plo
    core_hi=const*Dhi*PHi*PHi
    wlo=floor60(core_lo/(PI[1]*PI[1]))
    whi=ceil60(core_hi/(PI[0]*PI[0]))
    assert 0<wlo<=whi
    sum_w_lo=floor60(sum_w_lo+wlo)
    sum_w_hi=ceil60(sum_w_hi+whi)
    weighted_hi=ceil60(weighted_hi+qhi*whi)

m2_lo=mI[0]*mI[0]
m2_hi=mI[1]*mI[1]
even_total_hi=e2I[1]/2-m2_lo
rem_hi=even_total_hi-sum_w_lo
assert rem_hi>0
qtail_hi=ceil60(qhi*q2)
p_upper=m2_hi+oddI[1]+weighted_hi+qtail_hi*rem_hi
trace_upper=p_upper/(1-r**4)
trace_cap=F(1143510223,1_000_000_000)
assert trace_upper<trace_cap

mu_lo=F(9155053441,10_000_000_000)
mu_hi=F(9155053442,10_000_000_000)
eps2_hi=F(270154,10_000_000_000)

theta=F(8603667,50_000_000)
x=F(228943227,250_000_000)
beta=F(8145371,10_000_000)
assert x>mu_hi>mu_lo>beta
trace_margin=beta**4-(trace_cap-x**4)
temple_margin=(x-mu_hi)*(mu_lo-beta)-eps2_hi
assert trace_margin>0 and temple_margin>0
def atanh_lo(z,m):
    return sum(z**(2*k+1)/F(2*k+1) for k in range(m+1))
def atanh_hi(z,m):
    s0=atanh_lo(z,m)
    n=2*m+3
    return s0+z**n/F(n)/(1-z*z)
zx=(1-x)/(1+x)
zr=(1-r)/(1+r)
log_margin=atanh_lo(zx,10)-4*theta*atanh_hi(zr,10)
assert log_margin>0

incoming=F(15664,91031)
upper=F(1,4)
assert theta>incoming

print('r,c,s =',r,c,s)
print('covariance squared margins k=1,2 =',[float(z) for z in radical_margins])
print('tail endpoint c-margin =',float(c-tail_endpoint))
print('G0 =',float(G0))
print('rho_adj,rho_opp,q,A =',float(rho_adj),float(rho_opp),float(q),float(A))
print('K =',K,'qtail upper =',float(qtail_hi))
print('even residual upper =',float(rem_hi))
print('trace upper =',float(trace_upper))
print('trace cap/margin =',float(trace_cap),float(trace_cap-trace_upper))
print('theta,x,beta =',float(theta),float(x),float(beta))
print('trace separation margin =',float(trace_margin))
print('Temple margin =',float(temple_margin))
print('log/atanh margin =',float(log_margin))
print('incoming valid =',float(incoming),'gain =',float(theta-incoming))
print('old width =',float(upper-incoming),'new width =',float(upper-theta))
print('ALL_EXACT_CHECKS_PASS = True')

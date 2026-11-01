#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# PROB10-05 exact checker after the normalized four-cycle scale correction.
# It sums the entire odd Hermite sector in closed form and computes K=1000
# corrected even modes by an O(K) rational recurrence.

r = F(22,25)
c = F(936901,10**6)
s = F(936901,940000)
assert c == s*F(1+r,2)

# All-lag Lamperti covariance bridge R(r^k)<c r^(k-1).
radical_margins=[]
for k in (1,2):
    u0=r**k
    tk=c*r**(k-1)
    A0=6*u0**5*tk+2*u0**10-5*u0**6-5*u0**4+2
    mar=A0*A0-4*(1-u0**4)**5
    assert A0>0 and mar>0
    radical_margins.append(mar)
deriv_margin=F(5,8)-F(2,3)*r**6
tail_endpoint=r*(F(5,6)+F(5,8)*r**6-F(1,3)*r**12)
assert deriv_margin>0 and tail_endpoint<c

# Correct normalized four-cycle scale.
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

# Outward exact interval helpers for pi/sqrt/arctan/arcsin.
DROOT=10**110
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
    for k in range(m+1): z += F((-1)**k,2*k+1)*x**(2*k+1)
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

# Mean m=E g_A and second moment E2=E g_A^2 from the corrected reduction.
sqrtA=sqrt_bounds(A)
atanA=atan_pos_interval(*sqrtA)
mI=(atanA[0]/PI[1],atanA[1]/PI[0])
sqrtB=sqrt_bounds(1+2*A)
arg2=(A/sqrtB[1],A/sqrtB[0])
atan2=atan_pos_interval(*arg2)
e2I=(atan2[0]/PI[1],atan2[1]/PI[0])
assert 0<mI[0]<=mI[1]<F(1,2)
assert 0<e2I[0]<=e2I[1]<F(1,2)

# Closed form for the full odd Hermite sector:
# sum_{j>=0} q^(2j+1)d_{2j+1}^2/(2j+1)! = asin(q*aa)/(2*pi).
odd_asin=asin_pos_interval(q*aa)
oddI=(odd_asin[0]/(2*PI[1]),odd_asin[1]/(2*PI[0]))

# Exact O(K) recurrence for corrected even modes.
# J_j=I_{2j-1}=(-1)^(j-1)(2j-3)!! P_j/h,
# P_1=1, P_j=1+((2j-2)/(2j-3))*aa*P_{j-1}.
# w_j=d_{2j}^2/(2j)! = A D_j P_j^2/(pi^2 h^2),
# D_1=1/2 and D_j/D_{j-1}=(2j-3)^2/((2j)(2j-1)).
K=1000
P=F(1)
D=F(1,2)
const_num=A/(h*h)
sum_w_lo=F(0); sum_w_hi=F(0); weighted_hi=F(0)
q2=q*q
qpow=q2
for j in range(1,K+1):
    if j>1:
        P=1+F(2*j-2,2*j-3)*aa*P
        D=D*F((2*j-3)**2,(2*j)*(2*j-1))
        qpow*=q2
    core=const_num*D*P*P
    wlo=core/(PI[1]*PI[1])
    whi=core/(PI[0]*PI[0])
    assert 0<wlo<=whi
    sum_w_lo+=wlo
    sum_w_hi+=whi
    weighted_hi+=qpow*whi

m2_lo=mI[0]*mI[0]
m2_hi=mI[1]*mI[1]
even_total_lo=e2I[0]/2-m2_hi
even_total_hi=e2I[1]/2-m2_lo
rem_lo=even_total_lo-sum_w_hi
rem_hi=even_total_hi-sum_w_lo
assert 0<rem_lo<=rem_hi
qtail=qpow*q2
p_upper=m2_hi+oddI[1]+weighted_hi+qtail*rem_hi
trace_upper=p_upper/(1-r**4)
trace_cap=F(1143529,1_000_000)  # 1.143529
assert trace_upper<trace_cap

# Same-operator direct degree-56 moment certificate; unaffected by the cycle
# normalization bug because it was computed under the stationary one-step and
# two-step Gaussian law, not under the normalized cyclic trace measure.
mu_lo=F(9155053441,10_000_000_000)
mu_hi=F(9155053442,10_000_000_000)
eps2_hi=F(270154,10_000_000_000)

# Kato-Temple synthesis.
theta=F(15664,91031)  # 0.17207324977205568...
x=F(91577295,100_000_000)
beta=F(81454563,100_000_000)
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
log_margin=atanh_lo(zx,9)-4*theta*atanh_hi(zr,9)
assert log_margin>0

incoming_valid=F(3441457,20_000_000)
upper=F(1,4)
assert theta>incoming_valid

print('r,c,s =',r,c,s)
print('covariance k=1,2 squared margins =',[float(z) for z in radical_margins])
print('tail endpoint c-margin =',float(c-tail_endpoint))
print('G0 =',G0,float(G0))
print('rho_adj,rho_opp,q,A =',float(rho_adj),float(rho_opp),float(q),float(A))
print('K =',K,'q^(2K+2) =',float(qtail))
print('m interval =',float(mI[0]),float(mI[1]))
print('E2 interval =',float(e2I[0]),float(e2I[1]))
print('odd weighted sector interval =',float(oddI[0]),float(oddI[1]))
print('even computed mass upper =',float(sum_w_hi))
print('even residual interval =',float(rem_lo),float(rem_hi))
print('p upper =',float(p_upper))
print('trace upper =',float(trace_upper))
print('trace cap/margin =',float(trace_cap),float(trace_cap-trace_upper))
print('theta,x,beta =',float(theta),float(x),float(beta))
print('trace separation margin =',float(trace_margin))
print('Temple margin =',float(temple_margin))
print('log/atanh margin =',float(log_margin))
print('incoming valid =',float(incoming_valid),'gain =',float(theta-incoming_valid))
print('old width =',float(upper-incoming_valid),'new width =',float(upper-theta))
print('ALL_EXACT_CHECKS_PASS = True')

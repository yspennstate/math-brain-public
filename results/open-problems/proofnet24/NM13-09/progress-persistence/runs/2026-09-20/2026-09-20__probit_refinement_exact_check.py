#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# NM13-09 exact self-check for T05 integrated-fBM persistence at H=1/4.
# New ingredient: after equicorrelation domination of the softened four-cycle,
# use the proved pointwise inequality
#   Phi(x)Phi(-x) <= exp(-x^2/2)/(4*sqrt(1+x^2/5))
# and 1/(1+y) <= 1-y+y^2 to sharpen the fourth-trace bound.
# All theorem-deciding finite comparisons below are exact rational/integer
# arithmetic, with pi/sqrt/asin enclosed by outward rational intervals.

r=F(7,8)
s=F(24861,25000)

# Source sampled covariance comparator parameters.
c=s*(1+r)/2

def Ppoly(z):
    return 2+2*z-3*z*z-2*z**3-2*z**4

cov_margins=[]
for k in range(1,6):
    u=r**k
    cap=c*r**(k-1)
    z=u*u
    T=Ppoly(z)+6*u**5*(cap-u)/(1-u*u)
    margin=T*T-4*(1+z)**2*(1-z*z)**3
    assert T>0 and margin>0
    cov_margins.append(margin)
# For k>=6, u<=r^6<1/2 and z=u^2<=1/4. The report proves
# P(z)^2-4(1+z)^2(1-z^2)^3=z^3 Q(z),
# Q(z)>=4-7z-20z^2>=1, so R(u)<=u< c r^(k-1).
assert r**6 < F(1,2)
assert c/r > 1
assert F(4)-F(7,4)-F(20,16) == 1

# Normalized softened Gaussian four-cycle correlations.
a=(r+r**3)/(1+r**4)
b=2*r*r/(1+r**4)
v=(1+a)/(1+r)
g=(1+b+2*a)/(2*(1+r))
h=(a+b)/(1+r)
varV=s*v+(1-s)
rho_adj=s*g/varV
rho_opp=s*h/varV
assert a==F(6328,6497)
assert b==F(6272,6497)
assert v==F(6840,6497)
assert g==F(6780,6497)
assert h==F(6720,6497)
assert varV==F(170952323,162425000)
assert rho_adj==F(168557580,170952323)
assert rho_opp==F(167065920,170952323)
assert 0 < rho_opp < rho_adj < 1

def atan_series_bounds(x,m):
    x=F(x)
    assert 0<=x<1
    ss=F(0)
    for k in range(m+1):
        ss += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(ss,ss+nxt),max(ss,ss+nxt)

# Machin: pi = 16 atan(1/5)-4 atan(1/239).
a5=atan_series_bounds(F(1,5),90)
a239=atan_series_bounds(F(1,239),30)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
assert PI[0]>3 and PI[1]<4

DROOT=10**80
def sqrt_bounds(x):
    x=F(x)
    assert x>=0
    m=isqrt((DROOT*DROOT*x.numerator)//x.denominator)
    lo,hi=F(m,DROOT),F(m+1,DROOT)
    assert lo*lo<=x<hi*hi
    return lo,hi

def asin_bounds_pos(rho):
    rho=F(rho)
    assert 0<rho<1
    slo,shi=sqrt_bounds(1-rho*rho)
    tlo,thi=slo/rho,shi/rho
    assert thi<1
    atan_lo,_=atan_series_bounds(tlo,140)
    _,atan_hi=atan_series_bounds(thi,140)
    return PI[0]/2-atan_hi,PI[1]/2-atan_lo

asin_adj=asin_bounds_pos(rho_adj)
sqrt_ratio=sqrt_bounds((1-rho_adj)/(1+rho_adj))

# If C^2=rho/(1-rho), A=1+2C^2=(1+rho)/(1-rho), then
# E[e^{-C^2 Z^2}/(1+C^2 Z^2/5)]
# <= A^{-1/2}[1-q+3q^2], q=rho/[5(1+rho)],
# by 1/(1+y)<=1-y+y^2 and exact Gaussian derivatives.
q=rho_adj/(5*(1+rho_adj))
factor=1-q+3*q*q
J_upper=sqrt_ratio[1]*factor

# Equicorrelation/probit identity gives
# p4 <= asin(rho_adj)/pi + J/16.
p4_upper=asin_adj[1]/PI[0] + J_upper/16
pref=1/(1-r**4)
trace_upper=pref*p4_upper
trace_cap=F(27279,25000)  # 1.09116
trace_margin=trace_cap-trace_upper
assert trace_margin>0

# Inherited exact degree-18 quasimode coarsenings, certified by the archived
# HARD7-05 frontier checker at the same r,s.
mu_lo=F(9116948312,10_000_000_000)
mu_hi=F(9116948313,10_000_000_000)
eps2_hi=F(47004495,100_000_000_000)

# New target theta*=413/2500=0.1652. Since 4 theta*=413/625,
# x^625<r^413 proves x<r^(4 theta*).
theta_target=F(413,2500)
x=F(915543,1_000_000)
assert x**625 < r**413
assert x>mu_hi

# Fourth-trace tail separates every non-Perron spectral point.
beta=F(9869,12500)  # 0.78952
tail_margin=beta**4-(trace_cap-x**4)
assert tail_margin>0
assert mu_lo>beta

# Temple contradiction under lambda_1>=r^(4 theta*).
temple_lower=(x-mu_hi)*(mu_lo-beta)
temple_margin=temple_lower-eps2_hi
assert temple_margin>0

old_lower=F(16517,100000)
new_lower=theta_target
source_upper=F(1,4)
old_width=source_upper-old_lower
new_width=source_upper-new_lower
assert old_width==F(8483,100000)
assert new_width==F(53,625)
assert old_width-new_width==F(3,100000)

print('c =',c,float(c),'c/r =',float(c/r))
print('covariance squared margins k=1..5 =',[float(m) for m in cov_margins])
print('tail check r^6 < 1/2 =',r**6<F(1,2))
print('rho_adj =',rho_adj,float(rho_adj))
print('rho_opp =',rho_opp,float(rho_opp))
print('q =',q,float(q),'factor =',factor,float(factor))
print('sqrt ratio ~',float(sqrt_ratio[1]))
print('J upper <',float(J_upper))
print('p4 upper <',float(p4_upper))
print('trace upper <',float(trace_upper))
print('trace cap =',trace_cap,float(trace_cap))
print('trace cap margin >',float(trace_margin))
print('x =',x,float(x),'power check =',x**625<r**413)
print('beta =',beta,float(beta))
print('spectral-tail margin >',float(tail_margin))
print('Temple lower >',float(temple_lower))
print('Temple contradiction margin >',float(temple_margin))
print('old lower =',old_lower,float(old_lower))
print('new lower =',new_lower,float(new_lower))
print('old width =',old_width,float(old_width))
print('new width =',new_width,float(new_width))
print('metric improvement =',old_width-new_width,float(old_width-new_width))
print('ALL_EXACT_CHECKS_PASS = True')

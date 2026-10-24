#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# NM13-09 exact self-check: HGR/maximal-correlation sharpening of the
# four-cycle orthant trace for the softened AR-edge comparator.
# Every theorem-deciding comparison is exact Fraction/integer arithmetic.
# Irrational pi/sqrt/asin quantities are enclosed by rational intervals.

r=F(7,8)
s=F(24861,25000)

# Normalized Gaussian four-cycle data inherited/independently recomputed.
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

# Exact source sampled covariance domination. For H=1/4 and Lamperti
# variable u=exp(-tau/4), algebra gives
# R(u)-u=(1-u^2)/(6u^5)*[-P(u^2)+2(1+u^2)(1-u^4)^(3/2)].
# For u=r^k and cap b=c r^(k-1), R(u)<b follows after isolating
# the radical and squaring when T=P(u^2)+6u^5(b-u)/(1-u^2)>0.
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
# For k>=6, u<=r^6<1/2. On z=u^2<=1/4,
# P(z)^2-4(1+z)^2(1-z^2)^3 = z^3 Q(z),
# Q(z)=8z^5+16z^4+8z^3-20z^2-7z+4 >= 4-7z-20z^2 >=1.
# Also P(z)>0, hence R(u)<=u; and c/r>1 gives u<cap.
assert r**6<F(1,2)
assert c/r>1
assert F(4)-F(7,4)-F(20,16)==F(1)

# Canonical correlation between opposite-pair Gaussian blocks
# (V0,V2) and (V1,V3). In symmetric/antisymmetric coordinates the
# cross-covariance has rank one, giving kappa=2*rho_adj/(1+rho_opp).
kappa=2*rho_adj/(1+rho_opp)
assert 0<kappa<1

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

DROOT=10**70
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
    atan_lo,_=atan_series_bounds(tlo,120)
    _,atan_hi=atan_series_bounds(thi,120)
    # asin(rho)=pi/2-atan(sqrt(1-rho^2)/rho).
    return PI[0]/2-atan_hi,PI[1]/2-atan_lo

asin_adj=asin_bounds_pos(rho_adj)
asin_opp=asin_bounds_pos(rho_opp)
# q = E sign(X)sign(Y) = 2/pi asin(rho).
qadj_hi=2*asin_adj[1]/PI[0]
qopp_hi=2*asin_opp[1]/PI[0]
qadj_lo=2*asin_adj[0]/PI[1]
qopp_lo=2*asin_opp[0]/PI[1]
assert 0<qadj_lo<=qadj_hi<1
assert 0<qopp_lo<=qopp_hi<1

# HGR/Gebelein bound for the four-sign moment:
# m4 <= qopp^2 + kappa(1-qopp^2)
#     = kappa + (1-kappa) qopp^2.
# Therefore p4 <= [1+4 qadj + 2 qopp + m4]/16.
m4_hi=kappa+(1-kappa)*qopp_hi*qopp_hi
p4_hi=(1+4*qadj_hi+2*qopp_hi+m4_hi)/16
pref=1/(1-r**4)
trace_hi=pref*p4_hi
trace_cap=F(110263,100000)
trace_margin=trace_cap-trace_hi
assert trace_margin>0

# Inherited exact degree-18 quasimode coarsenings from the current
# HARD7-05 frontier point (r=7/8,s=24861/25000).
mu_lo=F(9116948312,10_000_000_000)
mu_hi=F(9116948313,10_000_000_000)
eps2_hi=F(47004495,100_000_000_000)

# New source target theta*=16483/100000. Since 4 theta*=16483/25000,
# x^25000 < r^16483 proves x<r^(4 theta*).
theta_target=F(16483,100000)
x=F(4578621,5_000_000)
assert x**25000<r**16483
assert x>mu_hi

# Improved fourth-trace tail separates every non-Perron spectral point.
beta=F(198751,250000)
tail_margin=beta**4-(trace_cap-x**4)
assert tail_margin>0
assert mu_lo>beta

# Temple contradiction under lambda_1 >= r^(4 theta*).
temple_lower=(x-mu_hi)*(mu_lo-beta)
temple_margin=temple_lower-eps2_hi
assert temple_margin>0

old_lower=F(103,625) # 0.1648
source_upper=F(1,4)
new_lower=theta_target
old_width=source_upper-old_lower
new_width=source_upper-new_lower
assert old_width==F(213,2500)
assert new_width==F(8517,100000)
assert old_width-new_width==F(3,100000)

print('c =',c,float(c),'c/r =',float(c/r))
print('covariance squared margins k=1..5 =',[float(m) for m in cov_margins])
print('tail check r^6 < 1/2 =',r**6<F(1,2))
print('rho_adj =',rho_adj,float(rho_adj))
print('rho_opp =',rho_opp,float(rho_opp))
print('kappa =',kappa,float(kappa))
print('qadj in',float(qadj_lo),float(qadj_hi))
print('qopp in',float(qopp_lo),float(qopp_hi))
print('m4 upper <',float(m4_hi))
print('p4 upper <',float(p4_hi))
print('trace upper <',float(trace_hi))
print('trace cap =',trace_cap,float(trace_cap))
print('trace cap margin >',float(trace_margin))
print('x =',x,float(x),'power check =',x**25000<r**16483)
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

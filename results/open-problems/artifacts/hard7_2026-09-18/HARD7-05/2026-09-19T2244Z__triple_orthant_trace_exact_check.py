#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

# HARD7-05 exact self-check for the three-coordinate softened trace bound.
# Every theorem-deciding comparison is exact Fraction/integer arithmetic.
# Irrational pi, sqrt and asin quantities are enclosed by rational intervals
# from Machin's formula, integer square-root bracketing, and alternating atan
# series. The degree-18 quasimode bounds are inherited from the immediately
# preceding exact checker:
# artifacts/hard7_2026-09-18/HARD7-05/
# 2026-09-19T2140Z__softening_frontier_exact_check.py
# commit e515d477a4a8f9b7436c0e51d128d0d92913715c.

r=F(7,8)
s=F(24861,25000)

# Normalized four-cycle covariance.
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

# The trivariate correlation matrix is positive definite.
det3=1-2*rho_adj**2-rho_opp**2+2*rho_adj**2*rho_opp
assert det3>0

def atan_series_bounds(x,m):
    x=F(x)
    assert 0<=x<1
    ss=F(0)
    for k in range(m+1):
        ss += F((-1)**k,2*k+1)*x**(2*k+1)
    nxt=F((-1)**(m+1),2*(m+1)+1)*x**(2*(m+1)+1)
    return min(ss,ss+nxt),max(ss,ss+nxt)

# Machin: pi = 16 atan(1/5)-4 atan(1/239).
a5=atan_series_bounds(F(1,5),80)
a239=atan_series_bounds(F(1,239),25)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
assert PI[0]>3 and PI[1]<4

DROOT=10**60
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
    atan_lo,_=atan_series_bounds(tlo,100)
    _,atan_hi=atan_series_bounds(thi,100)
    # asin(rho)=pi/2-atan(sqrt(1-rho^2)/rho).
    return PI[0]/2-atan_hi,PI[1]/2-atan_lo

asin_adj=asin_bounds_pos(rho_adj)
asin_opp=asin_bounds_pos(rho_opp)

# P(V0,V1,V2<0) =
# 1/8 + [2 asin(rho_adj)+asin(rho_opp)]/(4 pi).
p3_upper=F(1,8)+(2*asin_adj[1]+asin_opp[1])/(4*PI[0])
pref=1/(1-r**4)
trace_upper=pref*p3_upper
trace_cap=F(110273,100000)
trace_margin=trace_cap-trace_upper
assert trace_margin>0

# Inherited exact degree-18 quasimode coarsenings.
mu_lo=F(9116948312,10_000_000_000)
mu_hi=F(9116948313,10_000_000_000)
eps2_hi=F(47004495,100_000_000_000)

# New target theta*=103/625. Since 4 theta*=412/625,
# x^625 < r^412 proves x<r^(4 theta*).
theta_target=F(103,625)
x=F(183147,200000)
assert x**625<r**412
assert x>mu_hi

# Improved fourth-trace tail separates every non-Perron spectral point.
beta=F(9938,12500)
tail_margin=beta**4-(trace_cap-x**4)
assert tail_margin>0
assert mu_lo>beta

# Temple contradiction under lambda_1 >= r^(4 theta*).
temple_lower=(x-mu_hi)*(mu_lo-beta)
temple_margin=temple_lower-eps2_hi
assert temple_margin>0

old_lower=F(1647,10000)
new_lower=theta_target
source_upper=F(1,4)
old_width=source_upper-old_lower
new_width=source_upper-new_lower
assert old_width==F(853,10000)
assert new_width==F(213,2500)
assert old_width-new_width==F(1,10000)

print("a,b =",a,b)
print("edge variance/covariances =",v,g,h)
print("soft var =",varV,float(varV))
print("rho_adj =",rho_adj,float(rho_adj))
print("rho_opp =",rho_opp,float(rho_opp))
print("det3 >",float(det3))
print("three-coordinate trace upper <",float(trace_upper))
print("trace cap =",trace_cap,float(trace_cap))
print("trace cap margin >",float(trace_margin))
print("x =",x,float(x),"power check =",x**625<r**412)
print("beta =",beta,float(beta))
print("spectral-tail margin >",float(tail_margin))
print("Temple lower >",float(temple_lower))
print("Temple contradiction margin >",float(temple_margin))
print("new lower =",new_lower,float(new_lower))
print("new width =",new_width,float(new_width))
print("metric improvement =",old_width-new_width,float(old_width-new_width))
print("ALL_EXACT_CHECKS_PASS = True")

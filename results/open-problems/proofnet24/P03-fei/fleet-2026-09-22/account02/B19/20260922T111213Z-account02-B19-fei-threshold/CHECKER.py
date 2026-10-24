#!/usr/bin/env python3
import math

def h2(q):
    if q == 0.0 or q == 1.0:
        return 0.0
    return -q*math.log2(q)-(1.0-q)*math.log2(1.0-q)

def jprime(q):
    x=math.sqrt(q/(1.0-q))
    return ((1.0-x*x)/(x*math.log(2.0)))*math.log((1.0+x)/(1.0-x))

def a_root(K):
    lo,hi=0.0,0.5
    for _ in range(200):
        mid=(lo+hi)/2.0
        if mid == 0.0 or h2(mid)/mid > K:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

def iproj_c(v,q,N):
    lo=1e-12
    hi=1.0
    def f(c):
        return 1.0-c-(1.0-c*q/v)**N
    for _ in range(250):
        mid=(lo+hi)/2.0
        if f(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

print("THRESHOLD_FLEX_CONSTANTS")
for K in (4.0,6.0,8.0,10.0,12.0):
    a=a_root(K)
    lam=math.log2(1.0+2.0**(-K))/(K+jprime(a))
    d=max(6,math.ceil(K+3.0))
    q=2.0**(1-d)
    ordinary=h2(q)/q
    cos=((d-1)*h2(q)-q*jprime(q))/(d*q)
    assert ordinary>K and cos>K
    print("K=%.0f aK=%.15g lambdaK=%.15g d=%d q=%.15g min_factor_ratio=%.15g" %
          (K,a,lam,d,q,min(ordinary,cos)))

K=8.0
a=a_root(K)
lam=math.log2(1.0+2.0**(-K))/(K+jprime(a))
print("K8_visible_coeff=%.15g" % (128.0*lam/105.0))
print("K8_hidden_coeff=%.15g" % (64.0*lam/105.0))
print("K8_if_closed_global_C=%.15g" % (K+2.0/math.log(2.0)))

d=11
q=2.0**(1-d)
for m in (1,2,4,8,16):
    N=d*m
    v=1.0-(1.0-q)**(2*m)
    mu=N*q/v
    c=iproj_c(v,q,N)
    assert mu>1.0 and c+1e-12>=v
    print("tensor d=%d m=%d mu=%.12g c_over_v=%.12g psi_cross_positive_excess=%s raw_UK_over_J_lower=%.12g" %
          (d,m,mu,c/v, str(4*q*q > 4*(c/v)*q*q), 4*(K+jprime(q))*q*d*max(0,m-1)))

print("THRESHOLD_FLEX_REGRESSION_PASS")

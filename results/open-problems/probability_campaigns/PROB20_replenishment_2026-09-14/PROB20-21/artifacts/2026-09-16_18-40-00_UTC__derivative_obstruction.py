#!/usr/bin/env python3
from fractions import Fraction
from math import comb

K=55

def ln_bounds(q):
    q=Fraction(q)
    assert q>0
    if q==1: return Fraction(0),Fraction(0)
    e=q.numerator.bit_length()-q.denominator.bit_length()
    scale=Fraction(2**e,1) if e>=0 else Fraction(1,2**(-e))
    s=q/scale
    while s<1:
        s*=2; e-=1
    while s>=2:
        s/=2; e+=1
    t=(s-1)/(s+1)
    z=Fraction(0)
    for k in range(K+1):
        z += Fraction(2,2*k+1)*t**(2*k+1)
    rem=Fraction(2,2*K+3)*t**(2*K+3)/(1-t*t)
    l2,u2=ln2_bounds()
    if e>=0:
        return z+e*l2,z+rem+e*u2
    return z+e*u2,z+rem+e*l2

def ln2_bounds():
    t=Fraction(1,3)
    z=Fraction(0)
    for k in range(K+1):
        z += Fraction(2,2*k+1)*t**(2*k+1)
    rem=Fraction(2,2*K+3)*t**(2*K+3)/(1-t*t)
    return z,z+rem

def atanh_bounds(x):
    x=Fraction(x)
    assert -1 < x < 1
    lo,hi=ln_bounds((1+x)/(1-x))
    return lo/2,hi/2

def imul(iv, q):
    lo,hi=iv; q=Fraction(q)
    return (lo*q,hi*q) if q>=0 else (hi*q,lo*q)

def iadd(a,b): return a[0]+b[0],a[1]+b[1]
def isub(a,b): return a[0]-b[1],a[1]-b[0]

def derivative_interval(n,rho):
    rho=Fraction(rho)
    eps=Fraction(1,2**(n-1))
    total=(Fraction(0),Fraction(0))
    for k in range(n):
        weight=Fraction(comb(n-1,k),2**n)
        R=(1+rho)**k*(1-rho)**(n-1-k)
        Rp=R*(Fraction(k,1+rho)-Fraction(n-1-k,1-rho))
        gp=rho-eps*(1+rho)*R
        gm=-rho-eps*(1-rho)*R
        gpp=1-eps*(R+(1+rho)*Rp)
        gmp=-1-eps*(-R+(1-rho)*Rp)
        term=iadd(imul(atanh_bounds(gp),gpp), imul(atanh_bounds(gm),gmp))
        total=iadd(total, imul(term,weight))
    return isub(atanh_bounds(rho),total)

for rho in (Fraction(4,5),Fraction(17,20)):
    lo,hi=derivative_interval(7,rho)
    print('rho',rho,'Dprime_lo',float(lo),'Dprime_hi',float(hi))
    if rho==Fraction(4,5): assert lo>0
    else: assert hi<0
print('PROB20-21 DERIVATIVE OBSTRUCTION: PASS')

#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import log2

def fwht(a):
    a=list(a); s=1
    while s<len(a):
        for i in range(0,len(a),2*s):
            for j in range(i,i+s):
                x,y=a[j],a[j+s]; a[j],a[j+s]=x+y,x-y
        s*=2
    return a

def entropy(p):
    return sum(-float(x)*log2(float(x)) for x in p if x)

def upper_potential(p,d):
    total=0.0
    for S,ps in enumerate(p):
        if not ps: continue
        pi=sum(p[T] for T in range(1<<d) if T&S==S)
        total += float(ps)*log2(float(pi/ps))
    return total

def influence(vals,d):
    ans=Fraction(0)
    for i in range(d):
        c=sum(vals[x]!=vals[x^(1<<i)] for x in range(1<<d))
        ans += Fraction(c,1<<d)
    return ans

checks=0
max_h_err=max_i_err=max_u_err=0.0
for d in range(2,11):
    N=1<<d; delta=Fraction(1,N)
    for h in range(1,d+1):
        z=(1<<h)-1
        vals=[-1 if x in (0,z) else 1 for x in range(N)]
        w=fwht(vals)
        p=[Fraction(a*a,N*N) for a in w]
        assert sum(p)==1
        p0=(1-4*delta)**2
        for S,ps in enumerate(p):
            target=p0 if S==0 else (16*delta*delta if ((S&z).bit_count()%2==0) else 0)
            assert ps==target
            checks+=1
        I=influence(vals,d)
        Itarget=4*(d-1)*delta if h==1 else 4*d*delta
        assert I==Itarget
        H=entropy(p)
        m=8*float(delta)*(1-2*float(delta)); M=N//2-1
        Hform=(-(1-m)*log2(1-m) if m<1 else 0.0) - (m*log2(m) if m else 0.0) + (m*log2(M) if M>1 else 0.0)
        U=upper_potential(p,d)
        empty=float(p0)*log2(1/float(p0)) if p0 else 0.0
        if h==1:
            Uform=empty+4*(d-1)*float(delta)*(1-4*float(delta))
        else:
            Uform=empty+4*(d-2)*float(delta)-16*(d-1)*float(delta)**2
            if h%2==0: Uform += (2**(4-h))*float(delta)
        max_h_err=max(max_h_err,abs(H-Hform))
        max_i_err=max(max_i_err,abs(float(I)-float(Itarget)))
        max_u_err=max(max_u_err,abs(U-Uform))
        assert abs(H-Hform)<2e-12
        assert abs(U-Uform)<2e-12
        assert H < 4*float(I)+1e-12
        assert U < 3*float(I)+1e-12
        checks+=6

print("TWO_POINT_OVERLAP_PASS")
print("dimensions=2..10; all distances h=1..d")
print("exact_rational_assertions", checks)
print("max_entropy_formula_error", f"{max_h_err:.3e}")
print("max_influence_formula_error", f"{max_i_err:.3e}")
print("max_upper_potential_formula_error", f"{max_u_err:.3e}")
print("seed=None")

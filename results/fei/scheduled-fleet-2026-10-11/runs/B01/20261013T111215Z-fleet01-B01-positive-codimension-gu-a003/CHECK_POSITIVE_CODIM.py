#!/usr/bin/env python3
"""Finite reconstruction for the canonical positive-codimension theorem."""
from fractions import Fraction
from math import comb, log, log1p, log2

LOG2E=1/log(2)

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for base in range(0,len(a),2*h):
            for j in range(base,base+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return a

def truth(t,k,a,c):
    out=[]
    for mask in range(1<<(2*t+k)):
        x=mask&((1<<t)-1); y=(mask>>t)&((1<<t)-1); z=mask>>(2*t)
        e=((x&y).bit_count()+(a&x).bit_count()+(c&z).bit_count()
           +int(y==0 and z==0))&1
        out.append(1 if e==0 else -1)
    return out

def restrict(f,i,b):
    n=len(f).bit_length()-1; out=[]
    for s in range(1<<(n-1)):
        lo=s&((1<<i)-1); hi=s>>i
        out.append(f[lo|(b<<i)|(hi<<(i+1))])
    return out

def probs(f):
    N=len(f); return [Fraction(w*w,N*N) for w in fwht(f)]

def upper_u(f):
    p=probs(f); q=p[:]; n=len(f).bit_length()-1
    for i in range(n):
        for s in range(1<<n):
            if not ((s>>i)&1):q[s]+=q[s|(1<<i)]
    return sum(float(v)*log2(float(q[s]/v)) for s,v in enumerate(p) if v)

def influence(f,i):
    return Fraction(sum(f[s]!=f[s^(1<<i)] for s in range(len(f))),len(f))

def B(k):
    if k==0:return 0.0
    if k==1:return 2.0
    return (8*k+22)*2.0**(-k)

def scalar_u(t,k,h,l):
    if k==0:return float(t)
    de=2.0**(-t); ep=2.0**(-k); dust=4*ep*ep
    muc=(1-2*ep)**2; D=4*ep*(1-2.0**(-l)); A=2.0**(t-h)
    L=0.0
    for j in range(h):
        L+=comb(h,j)*log1p(-D*2.0**(-(t-j)))*LOG2E
    E=0.0
    if muc:E+=muc*log2((A-D)/muc)
    for j in range(l):
        E+=comb(l,j)*dust*log2((A-4*ep*(1-2.0**(-j)))/dust)
    for j in range(k+1):
        cnt=comb(k,j)-(comb(l,j) if j<=l else 0)
        if cnt and j<k:E+=cnt*dust*(k-j)
    return t+de*(-(t-h)+L+E)

def scalar_gi(t,k,h,l):
    p=scalar_u(t,k,h,l); g=0.0
    if t:
        for bit,count in ((1,h),(0,t-h)):
            if not count:continue
            hp=h-bit
            g+=count*(p-(scalar_u(t-1,k+1,hp,l)+scalar_u(t-1,k+1,hp,l+1))/2)
            g+=count*(p-(scalar_u(t-1,k,hp,l)+(t-1))/2)
    if k:
        for bit,count in ((1,l),(0,k-l)):
            if count:g+=count*(p-(scalar_u(t,k-1,h,l-bit)+t)/2)
    rare=2.0**(1-t-k)
    ii=t+l*(1-rare)+(k-l)*rare
    return g,ii

checks=0; truth_cases=0; scalar_cases=0; max_ratio=(-1,None)

# Exact truth-table reconstruction through total physical dimension nine.
for t in range(5):
  for k in range(6):
    if t+k==0 or 2*t+k>9:continue
    for a in range(1<<t):
      for c in range(1<<k):
        f=truth(t,k,a,c); n=2*t+k
        u=upper_u(f); su=scalar_u(t,k,a.bit_count(),c.bit_count())
        assert abs(u-su)<2e-11; checks+=1
        infs=[influence(f,i) for i in range(n)]; ii=sum(infs)
        if t+k>=2:
            rho=Fraction(2,1<<(t+k))
            expected=Fraction(t)+c.bit_count()*(1-rho)+(k-c.bit_count())*rho
            assert ii==expected; checks+=1
        g=sum(u-(upper_u(restrict(f,i,0))+upper_u(restrict(f,i,1)))/2
              for i in range(n))
        sg,si=scalar_gi(t,k,a.bit_count(),c.bit_count())
        assert abs(g-sg)<5e-10 and abs(float(ii)-si)<2e-14; checks+=2
        assert g<=64*float(ii)+5e-10; checks+=1
        if ii and g/float(ii)>max_ratio[0]:max_ratio=(g/float(ii),(t,k,a,c))
        truth_cases+=1

# Scalar law, deviation lemma, aggregate bound, and sharp entropy endpoint.
for t in range(25):
  for k in range(65):
    if t+k==0:continue
    for h in range(t+1):
      for l in range(k+1):
        u=scalar_u(t,k,h,l)
        assert abs(u-t)<=B(k)+2e-10; checks+=1
        g,ii=scalar_gi(t,k,h,l)
        assert g<=64*ii+1e-8; checks+=1
        scalar_cases+=1

# The two elementary coefficient maxima used in the all-parameter proof.
for k in range(1,2049):
    A=2.5*B(k)+B(k+1)
    D=k*(B(k)+0.5*B(k-1))
    assert A<=30+1e-14 and D<=32+1e-14
    checks+=2

print(f"PASS checks={checks} truth_cases={truth_cases} scalar_cases={scalar_cases}")
print(f"max finite G/I={max_ratio[0]:.15f} at t,k,a,c={max_ratio[1]}")
print("truth-table scope: all affine a,c with 2t+k<=9, t<=4, k<=5")
print("scalar scope: all 0<=t<=24, 0<=k<=64 and all Hamming weights")
print("analytic coefficient scope checked: 1<=k<=2048")
print("proof scope: all parameters, physical restrictions, and disjoint products")

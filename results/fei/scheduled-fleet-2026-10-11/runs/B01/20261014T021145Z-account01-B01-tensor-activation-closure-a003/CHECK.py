#!/usr/bin/env python3
"""Audit for the tensor/activation closure GU' theorem."""
from fractions import Fraction
from math import log, log2
import random

LN2=log(2.0)
M=2/LN2
RHO=(1+LN2)/4
LAM=4/(1-LN2)
CSTAR=LAM*M
K0=8/3
A0=K0+CSTAR
TOL=3e-9

def fwht(v):
    a=[Fraction(x) for x in v]; h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return [x/len(a) for x in a]

def caps(p):
    q=list(p); n=len(q).bit_length()-1
    for j in range(n):
        bit=1<<j
        for s in range(1<<n):
            if not s&bit:q[s]+=q[s|bit]
    return q

def U(f):
    p=[x*x for x in fwht(f)]; pi=caps(p)
    return sum(float(x)*log2(float(y/x)) for x,y in zip(p,pi) if x)

def restrict(f,j,b):
    n=len(f).bit_length()-1; out=[]
    for z in range(1<<(n-1)):
        lo=z&((1<<j)-1); hi=z>>j
        out.append(f[lo|(b<<j)|(hi<<(j+1))])
    return tuple(out)

def I(f):
    n=len(f).bit_length()-1
    return sum(Fraction(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f)) for j in range(n))

def G(f):
    u=U(f); n=len(f).bit_length()-1
    return sum(u-(U(restrict(f,j,0))+U(restrict(f,j,1)))/2 for j in range(n))

def phi(h):
    h=abs(float(h))
    return 0 if h==0 else 2*h*h*(log2(1/h)+1/LN2)

def Phi(f):
    a=fwht(f); n=len(f).bit_length()-1
    return sum(phi(a[1<<j]) for j in range(n))

def product(f,g):return tuple(f[x]*g[y] for y in range(len(g)) for x in range(len(f)))
def activate(f):return tuple(f[x>>1] if not x&1 else 1 for x in range(2*len(f)))

def zlog(x):return 0 if x==0 else x*log2(1/x)
def R(t):
    x=(1+t)**2/4; y=(1-t)**2/4
    e=zlog(x)+(0 if y==0 else y*log2(2/(1-t)))
    u=0 if t==0 else t*t*log2(1/(t*t))
    return e-u/2+(1-t*t)/4

rng=random.Random(0xB01A003)
scalar=0
for j in range(200001):
    t=-1+2*j/200000
    J=(1-t)/2
    assert R(t)<=K0*J+TOL
    scalar+=1

base=[]
for n in range(4):
    for mask in range(1<<(1<<n)):
        base.append(tuple(1 if mask>>x&1 else -1 for x in range(1<<n)))

product_checks=activation_checks=invariant_checks=restriction_checks=0
for _ in range(3000):
    f=rng.choice(base); g=rng.choice(base)
    if len(f)*len(g)>256: continue
    q=product(f,g)
    assert abs(U(q)-U(f)-U(g))<TOL
    assert abs(float(I(q))-float(I(f))-float(I(g)))<TOL
    assert abs(G(q)-G(f)-G(g))<TOL
    assert Phi(q)<=Phi(f)+Phi(g)+TOL
    product_checks+=4

generated=[(1,),(-1,),(1,-1),(-1,1)]
for _ in range(300):
    if rng.random()<.55:
        f=rng.choice(generated)
        if len(f)<=512: generated.append(activate(f))
    else:
        f,g=rng.choice(generated),rng.choice(generated)
        if len(f)*len(g)<=1024: generated.append(product(f,g))

for f in generated:
    i=float(I(f)); u=U(f); g=G(f); p=Phi(f)
    assert g+LAM*p<=A0*i+TOL
    assert g<=A0*i+TOL
    assert u<=A0*i+TOL
    assert (sum(zlog(float(x*x)) for x in fwht(f) if x) <= (2+2*A0)*i+TOL)
    invariant_checks+=4
    F=activate(f)
    J=(1-sum(f)/len(f))/2
    assert Phi(F)<=RHO*p+M*J+TOL
    assert G(F)+LAM*Phi(F)<=A0*float(I(F))+TOL
    activation_checks+=2
    n=len(f).bit_length()-1
    for j in range(n):
        for b in (0,1):
            h=restrict(f,j,b)
            assert G(h)+LAM*Phi(h)<=A0*float(I(h))+TOL
            restriction_checks+=1

print(f"scalar_checks={scalar}")
print(f"product_checks={product_checks}")
print(f"generated_functions={len(generated)}")
print(f"activation_checks={activation_checks}")
print(f"invariant_endpoint_checks={invariant_checks}")
print(f"restriction_checks={restriction_checks}")
print(f"lambda={LAM:.15f}")
print(f"Cstar={CSTAR:.15f}")
print(f"GU_constant={A0:.15f}")
print(f"FEI_constant={2+2*A0:.15f}")
print("PASS")

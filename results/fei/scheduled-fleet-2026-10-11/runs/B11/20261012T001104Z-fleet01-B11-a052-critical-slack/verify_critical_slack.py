#!/usr/bin/env python3
from fractions import Fraction
from math import log2

def walsh(vals):
    a=[int(v) for v in vals]
    n=(len(a)).bit_length()-1
    for j in range(n):
        step=1<<j
        for base in range(0,len(a),2*step):
            for t in range(step):
                u=a[base+t]; v=a[base+t+step]
                a[base+t]=u+v; a[base+t+step]=u-v
    return a

def spectrum(vals):
    N=len(vals)
    return [Fraction(z*z,N*N) for z in walsh(vals)]

def influence(vals):
    n=(len(vals)).bit_length()-1
    N=len(vals)
    out=[]
    for i in range(n):
        flips=sum(vals[x]!=vals[x^(1<<i)] for x in range(N))
        out.append(Fraction(flips,N))
    return out

def entropy(vals):
    return sum(-float(p)*log2(float(p)) for p in spectrum(vals) if p)

def child(vals,i,s):
    return [vals[x] for x in range(len(vals)) if ((x>>i)&1)==s]

checks=0
tested=0
for n in range(1,5):
    N=1<<n
    for mask in range(1,1<<N-1):
        vals=[1 if (mask>>x)&1 else -1 for x in range(N)]
        inf=influence(vals); I=sum(inf,Fraction())
        if not I: continue
        H=entropy(vals); R=H/float(I)
        for i,Ii in enumerate(inf):
            if not Ii: continue
            cs=[child(vals,i,s) for s in (0,1)]
            Is=[sum(influence(c),Fraction()) for c in cs]
            Hs=[entropy(c) for c in cs]
            delta=H-sum(Hs)/2
            lhs=delta-R*float(Ii)
            rhs=sum(float(J)*(R-h/float(J)) for J,h in zip(Is,Hs) if J)/2
            assert abs(lhs-rhs)<2e-10
            checks+=1
        tested+=1

print(f"truth_tables={tested}")
print(f"identity_assertions={checks}")
print("failures=0")
print("floating entropy is diagnostic; the theorem is the exact algebraic proof")

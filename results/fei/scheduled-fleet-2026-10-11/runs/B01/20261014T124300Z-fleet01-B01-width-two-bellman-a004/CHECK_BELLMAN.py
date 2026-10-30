#!/usr/bin/env python3
"""Exhaustive finite test of the width-two signed Bellman selector."""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import log, log2


def fwht(v):
    a=[Fraction(x) for x in v]; h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                x,y=a[k],a[k+h]; a[k],a[k+h]=x+y,x-y
        h*=2
    return tuple(x/len(a) for x in a)


def caps(p):
    a=list(p); n=len(a).bit_length()-1
    for i in range(n):
        for s in range(len(a)):
            if not s>>i&1: a[s]+=a[s|1<<i]
    return tuple(a)


def restrict(v,i,b):
    n=len(v).bit_length()-1; out=[]
    for z in range(1<<(n-1)):
        lo=z&((1<<i)-1); hi=z>>i
        out.append(v[lo|(b<<i)|(hi<<(i+1))])
    return tuple(out)


def xr(x,y): return 0.0 if x==0 else float(x)*log2(float(y/x))
def pair(a,b): return xr(a,a+b)+xr(b,a+b)
def q(t): return 0.0 if t==0 else float(t)*log2(1/float(t))+2*float(t)/log(2)


@lru_cache(None)
def stats(v):
    h=fwht(v); p=tuple(x*x for x in h); pi=caps(p); n=len(v).bit_length()-1
    U=sum(xr(x,y) for x,y in zip(p,pi))
    I=sum(s.bit_count()*float(x) for s,x in enumerate(p))
    B=0.0; inf=[]
    for i in range(n):
        inf.append(sum((p[s] for s in range(len(p)) if s>>i&1),Fraction(0)))
        B+=sum(pair(p[s],p[s|1<<i]) for s in range(len(p)) if not s>>i&1)
    G=n*U
    for i in range(n): G-=.5*(stats(restrict(v,i,0))[0]+stats(restrict(v,i,1))[0])
    return U,I,B,G-B,p,tuple(inf)


def blocks(n):
    ans=[0]
    for k in (1,2):
        for C in combinations(range(n),k):
            ans.append(sum(1<<i for i in C))
    return ans


@lru_cache(None)
def theta(v,X):
    p=stats(v)[4]; inf=stats(v)[5]; n=len(v).bit_length()-1; ans=0.0
    for i in range(n):
        if X>>i&1: ans+=q(inf[i])
        else:
            e=Fraction(0); sub=X
            while True:
                e+=p[(1<<i)|sub]
                if sub==0: break
                sub=(sub-1)&X
            ans+=q(e)
    return ans


cstar=29/2+4/log(2)
def L(v):
    U,I,B,M,_,_=stats(v)
    return M+2*U-cstar*I


@lru_cache(None)
def max_theta2(v):
    n=len(v).bit_length()-1
    return max((theta(v,X),X) for X in blocks(n))


worst=(-1e100,None); tested_states=0; positive_states=0
for n in range(1,5):
    for tail in product((-1,1),repeat=(1<<n)-1):
        v=(-1,)+tail
        if stats(v)[1]==0: continue
        for Y in blocks(n):
            choices=[]
            for x in range(n):
                a,b=restrict(v,x,0),restrict(v,x,1)
                ta,Za=max_theta2(a); tb,Zb=max_theta2(b)
                charge=L(v)-.5*(L(a)+L(b))+2*theta(v,Y)-ta-tb
                choices.append((charge,x,Za,Zb))
            best=min(choices)
            tested_states+=1
            positive_states+=best[0]>1e-10
            if best[0]>worst[0]: worst=(best[0],(n,v,Y,best))

print('status=DIAGNOSTIC_COMPLETE')
print(f'cstar={cstar:.15f}')
print(f'tested_nonconstant_states={tested_states}')
print(f'positive_bellman_states={positive_states}')
print(f'worst_best_charge={worst[0]:.15g}')
print(f'worst_dimension={worst[1][0]}')
print(f'worst_inherited_block={worst[1][2]}')
print(f'worst_choice={worst[1][3]}')

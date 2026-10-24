"""A025 continuation certificate v1. No external writes; exact rational arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from functools import lru_cache
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'
OUT.mkdir(exist_ok=True)
PI=(Q(1,2),Q(1,4),Q(1,4))
checks=0
def check(x):
    global checks
    checks+=1
    assert x, checks
def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,default=str)+'\n',encoding='utf-8',newline='')

def ln2_bounds():
    z=Q(1,3); v=z; s=Q(0)
    for j in range(40): s+=2*v/(2*j+1); v/=9
    return s,s+2*v/(81*(1-z*z))
L2=ln2_bounds()
@lru_cache(None)
def log2_bounds(x):
    k=0
    while x<1: x*=2; k-=1
    while x>=2: x/=2; k+=1
    z=(x-1)/(x+1); v=z; s=Q(0)
    for j in range(40): s+=2*v/(2*j+1); v*=z*z
    tail=2*v/(81*(1-z*z))
    return k+s/L2[1],k+(s+tail)/L2[0]
def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(a,q): return a[0]*q,a[1]*q
def sub(a,b): return a[0]-b[1],a[1]-b[0]
def fwht(f):
    a=list(f); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h): u,v=a[i],a[i+h]; a[i]=u+v; a[i+h]=u-v
        h*=2
    return a
def entropy(f):
    n=len(f); ans=(Q(0),Q(0))
    for v,c in Counter(abs(x) for x in fwht(f)).items():
        if v:
            p=Q(v*v,n*n); lo,hi=log2_bounds(1/p)
            ans=add(ans,(c*p*lo,c*p*hi))
    return ans
def infs(f):
    return [Q(sum(f[j]!=f[j^(1<<i)] for j in range(len(f))),len(f)) for i in range(len(f).bit_length()-1)]
def influence(f): return sum(infs(f),Q(0))
def restrict(f,i,b):
    return [v for j,v in enumerate(f) if (j>>i)&1==b]
def bank(cores):
    return sum((2*PI[j]*PI[k]*influence([u*v for u,v in zip(cores[j],cores[k])]) for j in range(3) for k in range(j+1,3)),Q(0))
def terminal(cores):
    it=sum((p*influence(g) for p,g in zip(PI,cores)),Q(0))
    ht=(Q(0),Q(0))
    for p,g in zip(PI,cores): ht=add(ht,scale(entropy(g),p))
    return it,ht,(8*it-ht[1],8*it-ht[0])
def actual(cores):
    n=len(cores[0]); f=[]
    for b in range(2):
        for a in range(2):
            label=0 if a else (1 if b else 2)
            f.extend(cores[label])
    return f
def erasure(f,i):
    a=fwht(f); N=len(f); ans=(Q(0),Q(0))
    for s in range(N):
        if (s>>i)&1: continue
        p=Q(a[s]**2,N*N); q=Q(a[s|(1<<i)]**2,N*N)
        if p and q:
            ans=add(ans,scale(log2_bounds((p+q)/p),p))
            ans=add(ans,scale(log2_bounds((p+q)/q),q))
    return ans

def build(m,t):
    # Bit order: y[0:m], x, z, activation[0:t], then A,B.
    cores=[[],[],[]]; mask=(1<<m)-1
    for j in range(1<<(m+2+t)):
        y=j&mask; x=(j>>m)&1; z=1-2*((j>>(m+1))&1)
        b=1-2*(sum(((y>>i)&1)*((y>>(i+1))&1) for i in range(0,m,2))%2)
        active=(j>>(m+2))==0
        for k in range(3):
            v=z*b*(-1 if k and x==0 and y==k-1 else 1)
            cores[k].append(v if active else 1)
    return cores


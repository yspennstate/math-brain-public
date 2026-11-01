from fractions import Fraction as Q
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import json,time,hashlib

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0
def ck(v):
    global checks
    assert v
    checks+=1
def cutoff():
    if time.perf_counter()-start>55:raise RuntimeError('Frozen internal 55-second cutoff reached; no automatic continuation')
def save(name,obj):
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
        h*=2
    return [Q(x,len(a)) for x in a]
def inf(a):
    n=(len(a)-1).bit_length()
    return [Q(sum(a[x]!=a[x^(1<<j)] for x in range(len(a))),len(a)) for j in range(n)]

# Rational coefficient vectors of logarithms of primes. Equal vectors
# certify equal entropy expressions without evaluating any logarithm.
@lru_cache(None)
def factors(n):
    out=[];d=2
    while d*d<=n:
        e=0
        while n%d==0:n//=d;e+=1
        if e:out.append((d,e))
        d+=1 if d==2 else 2
    if n>1:out.append((n,1))
    return tuple(out)
@lru_cache(None)
def logvec(q):
    out=defaultdict(Q)
    for p,e in factors(q.numerator):out[p]+=e
    for p,e in factors(q.denominator):out[p]-=e
    return {p:v for p,v in out.items() if v}
def add(*terms):
    out=defaultdict(Q)
    for scale,v in terms:
        for p,c in v.items():out[p]+=scale*c
    return {p:c for p,c in out.items() if c}
def scalar(x):return {2:Q(x)} if x else {}
def entropy(probs):
    out={}
    for p in probs:
        if p:out=add((1,out),(-p,logvec(p)))
    return out
def cross(P,R):
    out={}
    for s,p in P.items():
        if p:
            ck(R.get(s,Q(0))>0)
            out=add((1,out),(-p,logvec(R[s])))
    return out
def Lv(p):return add((-p,logvec(p))) if p else {}
def binary(p):return add((1,Lv(p)),(1,Lv(1-p)))
def activation_tax(r):
    p=Q(1,1<<r)
    return add((1,scalar(2*r*p*(2-p))),(1,Lv((1-p)**2)))
def erasure_sum(r):
    total={}
    for k in range(1,r+1):
        s=Q(1,1<<(k-1));m=1-s;q=(1+m*m)/2;e=s*s/(2*(1+m*m))
        B=add((q,binary(e)),(1,scalar((1-m*m)/2)))
        total=add((1,total),(Q(1,1<<(r-k)),B))
    return total

def witness(gh,r):
    law={(r,t,0):h*h for t,h in enumerate(gh) if h}
    for i in reversed(range(r)):
        out=defaultdict(Q);s=Q(1,1<<(r-i-1))
        for child in [{(i,0,0):Q(1)},law]:
            for (j,t,U),w in child.items():
                u=Q(1) if t==0 and U==0 else Q(0)
                v=s*gh[t] if t else (1-s if U==0 else -s)
                theta=(u-v)**2/(2*(u*u+v*v))
                for z,prob in [(0,1-theta),(1,theta)]:
                    if prob:out[(j,t,U|(z<<i))]+=w*prob/2
        law=dict(out)
    return law
def closed_W(j,t,U,gh,r):
    p=Q(1,1<<r)
    if t:return p*p*gh[t]**2 if j==r else Q(0)
    if j==r:return Q(0)
    if U>> (j+1):return Q(0)
    eps=[]
    for i in range(r):
        s=Q(1,1<<(r-i-1));eps.append(s*s/(2*(1+(1-s)**2)))
    prob=Q(1,1<<(j+1))
    if U==0:
        for i in range(j+1):prob*=1-eps[i]
        return prob
    m=U.bit_length()-1
    if m>j:return Q(0)
    prob*=eps[m]*Q(1,1<<m)
    for i in range(m+1,j+1):prob*=1-eps[i]
    return prob

# Outward intervals. Signed quotients use all four corners, including
# negative log numerators (the repaired B09 convention).
def mul_interval(c,I):return (c*I[0],c*I[1]) if c>=0 else (c*I[1],c*I[0])
def lnsmall(z,N=32):
    t=(z-1)/(z+1);ck(0<=t<=Q(1,3))
    total=sum((2*t**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
    tail=2*t**(2*N+1)/(Q(2*N+1)*(1-t*t))
    return total,total+tail
LN2=lnsmall(Q(2))
@lru_cache(None)
def logint(q):
    k=0;z=q
    while z<1:z*=2;k-=1
    while z>=2:z/=2;k+=1
    lo,hi=lnsmall(z);ka,kb=mul_interval(Q(k),LN2);lo+=ka;hi+=kb
    cs=[lo/LN2[0],lo/LN2[1],hi/LN2[0],hi/LN2[1]]
    return min(cs),max(cs)
def vint(V):
    lo=hi=Q(0)
    for prime,c in V.items():
        a,b=mul_interval(c,(Q(1),Q(1)) if prime==2 else logint(Q(prime)))
        lo+=a;hi+=b
    return lo,hi
def iv(I):return {'lo':str(I[0]),'hi':str(I[1])}
def vec(V):return {str(p):str(c) for p,c in sorted(V.items())}


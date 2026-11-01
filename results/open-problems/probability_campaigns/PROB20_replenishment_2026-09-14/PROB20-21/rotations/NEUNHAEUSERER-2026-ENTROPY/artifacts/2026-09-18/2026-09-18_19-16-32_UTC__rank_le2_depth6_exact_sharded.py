#!/usr/bin/env python3
"""Exact finite certificate for the rank<=2 depth-six frontier of NEUNHAEUSERER-2026-ENTROPY.

The theorem certified here is structural, not a bounded weight-box search:
for six arbitrary positive-real weights, if the span of all active primitive
subset-difference relations has dimension at most two, then the entropy of the
iid Bernoulli(p) weighted sum is strictly concave for every 0<p<1.

Every mathematical PASS decision below uses only exact integer/Fraction
arithmetic.  The central interval is combined in the run report with the
already-proved arbitrary-depth endpoint theorem and complement symmetry.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, combinations
from collections import Counter
from math import gcd, comb
import hashlib
import argparse

M=6
EPS=F(1,128*(M**4)*(2**M))

RELS=[]
for v in product((-1,0,1), repeat=M):
    if 1 not in v or -1 not in v: continue
    if next(x for x in v if x)<0: v=tuple(-x for x in v)
    if v not in RELS: RELS.append(v)
assert len(RELS)==301

def plucker_key(u,v):
    z=[u[i]*v[j]-u[j]*v[i] for i in range(M) for j in range(i+1,M)]
    if not any(z): return None
    g=0
    for x in z: g=gcd(g,abs(x))
    z=[x//g for x in z]
    if next(x for x in z if x)<0: z=[-x for x in z]
    return tuple(z)

def span_has_nonnegative(u,v):
    if (all(x>=0 for x in v) and any(x>0 for x in v)) or (all(x<=0 for x in v) and any(x<0 for x in v)):
        return True
    for s in (1,-1):
        lo=hi=None; ok=True
        for a,b in zip(u,v):
            a=s*a
            if b==0:
                if a<0: ok=False; break
            else:
                t=F(-a,b)
                if b>0: lo=t if lo is None or t>lo else lo
                else: hi=t if hi is None or t<hi else hi
        if ok and not (lo is not None and hi is not None and lo>hi): return True
    return False

def in_span2(w,u,v):
    for i in range(M):
        for j in range(i+1,M):
            d=u[i]*v[j]-u[j]*v[i]
            if d:
                an=w[i]*v[j]-w[j]*v[i]
                bn=u[i]*w[j]-u[j]*w[i]
                return all(d*w[k]==an*u[k]+bn*v[k] for k in range(M))
    raise AssertionError('dependent basis')

def collision_signature(active):
    parent=list(range(1<<M))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b: parent[b]=a
    for rel in active:
        pos=[j for j,x in enumerate(rel) if x==1]
        neg=[j for j,x in enumerate(rel) if x==-1]
        zero=[j for j,x in enumerate(rel) if x==0]
        p0=sum(1<<j for j in pos); n0=sum(1<<j for j in neg)
        for zm in range(1<<len(zero)):
            common=sum((1<<j) for t,j in enumerate(zero) if (zm>>t)&1)
            union(p0|common,n0|common)
    cls={}
    for mask in range(1<<M):
        r=find(mask); cls.setdefault(r,[0]*(M+1))[mask.bit_count()]+=1
    return tuple(sorted(tuple(c) for c in cls.values()))

SPANS={}
for i,j in combinations(range(len(RELS)),2):
    k=plucker_key(RELS[i],RELS[j])
    if k is not None: SPANS.setdefault(k,(RELS[i],RELS[j]))
assert len(SPANS)==34250
POS2={k:uv for k,uv in SPANS.items() if not span_has_nonnegative(*uv)}
assert len(POS2)==26900

SIG2=set()
for u,v in POS2.values():
    active=[r for r in RELS if in_span2(r,u,v)]
    SIG2.add(collision_signature(active))
assert len(SIG2)==66
SIG1={collision_signature([r]) for r in RELS}
assert len(SIG1)==9
SIG0=collision_signature([])
SIGS=tuple(sorted(SIG2|SIG1|{SIG0}))
assert len(SIGS)==76
DIGEST=hashlib.sha256(repr(SIGS).encode('utf-8')).hexdigest()
assert DIGEST=='2472702c0e8eee6b1306667025977517de76f7a108dd4029bc37ca43c1e87d83'

def q_poly(c):
    out=[F(0)]*(M+1)
    for k,ck in enumerate(c):
        if not ck: continue
        for j in range(M-k+1): out[k+j]+=F(ck*comb(M-k,j)*((-1)**j))
    while len(out)>1 and out[-1]==0: out.pop()
    return tuple(out)
def deriv(a): return (F(0),) if len(a)==1 else tuple(F(i)*a[i] for i in range(1,len(a)))
POLY={}
for c in {c for sig in SIGS for c in sig}:
    q=q_poly(c); POLY[c]=(q,deriv(q),deriv(deriv(q)))

def bern_bounds(coeff,a,b):
    d=len(coeff)-1
    if d==0: return coeff[0],coeff[0]
    h=b-a; power=[F(0)]*(d+1)
    for j,cj in enumerate(coeff):
        for r in range(j+1): power[r]+=cj*comb(j,r)*(a**(j-r))*(h**r)
    beta=[]
    for k in range(d+1):
        beta.append(sum((power[j]*F(comb(k,j),comb(d,j)) for j in range(k+1)),F(0)))
    return min(beta),max(beta)
def imul(I,J):
    z=(I[0]*J[0],I[0]*J[1],I[1]*J[0],I[1]*J[1]); return min(z),max(z)
def square_lo(I):
    a,b=I
    if a<=0<=b: return F(0)
    return min(a*a,b*b)
def floor_log2(x):
    k=x.numerator.bit_length()-x.denominator.bit_length()
    while F(2)**k>x: k-=1
    while F(2)**(k+1)<=x: k+=1
    return k

def atanh_log_unit(y,N=6):
    assert F(1)<=y<F(2)
    z=(y-1)/(y+1); zz=z*z; term=z; s=F(0)
    for j in range(N): s+=term/F(2*j+1); term*=zz
    lo=2*s; hi=lo+2*term/(F(2*N+1)*(1-zz)); return lo,hi

def log2_bounds(N=8):
    z=F(1,3); zz=z*z; term=z; s=F(0)
    for j in range(N): s+=term/F(2*j+1); term*=zz
    lo=2*s; return lo,lo+2*term/(F(2*N+1)*(1-zz))
LOG2=log2_bounds()
@lru_cache(maxsize=None)
def log_bounds(x):
    assert x>0
    k=floor_log2(x); y=x/(F(2)**k); lo,hi=atanh_log_unit(y)
    if k>=0: return lo+k*LOG2[0],hi+k*LOG2[1]
    return lo+k*LOG2[1],hi+k*LOG2[0]

def ratio(c,p):
    t=p/(1-p)
    return sum(F(ck)*(t**k) for k,ck in enumerate(c))

def compress(sig): return tuple(sorted((c,m) for c,m in Counter(sig).items()))

def F_lower(csig,a,b):
    out=F(0)
    for c,mult in csig:
        q=bern_bounds(POLY[c][0],a,b); q1=bern_bounds(POLY[c][1],a,b); q2=bern_bounds(POLY[c][2],a,b)
        if q[0]<=0: return None
        L=(log_bounds(ratio(c,a))[0],log_bounds(ratio(c,b))[1])
        out += mult*(imul(q2,L)[0]+square_lo(q1)/q[1])
    return out

def certify(csig,maxdepth=26):
    leaves=0; md=0; minlo=None; stack=[(EPS,F(1,2),0)]
    while stack:
        a,b,d=stack.pop(); lo=F_lower(csig,a,b)
        if lo is not None and lo>0:
            leaves+=1; md=max(md,d); minlo=lo if minlo is None or lo<minlo else minlo; continue
        if d>=maxdepth: return False,leaves,md,(a,b,lo)
        m=(a+b)/2; stack.append((m,b,d+1)); stack.append((a,m,d+1))
    return True,leaves,md,minlo

ap=argparse.ArgumentParser(); ap.add_argument("--start",type=int,required=True); ap.add_argument("--stop",type=int,required=True); z=ap.parse_args()
TOTAL_LEAVES=0; MAX_DEPTH=0; GLOBAL_MIN=None
for i,sig in enumerate(SIGS[z.start:z.stop],start=z.start):
    ok,leaves,md,minlo=certify(compress(sig)); assert ok
    TOTAL_LEAVES+=leaves; MAX_DEPTH=max(MAX_DEPTH,md); GLOBAL_MIN=minlo if GLOBAL_MIN is None or minlo<GLOBAL_MIN else GLOBAL_MIN
print('central exact shard PASS',z.start,z.stop,'leaves',TOTAL_LEAVES,'maxdepth',MAX_DEPTH,'min_positive',GLOBAL_MIN>0,'min_decimal',float(GLOBAL_MIN))

from pathlib import Path
from fractions import Fraction as Q
from math import comb, isqrt
from functools import lru_cache
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
def ck(x):
    global checks
    assert x
    checks+=1
def add(a,b,c=Q(1)):
    r=a.copy()
    for x,v in b.items():
        r[x]=r.get(x,Q(0))+c*v
        if not r[x]: del r[x]
    return r
@lru_cache(None)
def logform(z):
    if z<=1: return {}
    # Small integers are prime-factorized; large integers remain explicit log arguments.
    if z>1000000:
        a=isqrt(z)
        if a*a==z: return {x:2*c for x,c in logform(a).items()}
        return {z:Q(1)}
    r={}; p=2
    while p*p<=z:
        while z%p==0: r[p]=r.get(p,Q(0))+1; z//=p
        p+=1
    if z>1: r[z]=r.get(z,Q(0))+1
    return r
def G(a,b):
    r={}
    for z,c in [(a+b,a+b),(a,-a),(b,-b)]:
        if z: r=add(r,logform(z),Q(c))
    return r
def entropy(W):
    D=len(W)**2; out={2:Q(2*((len(W)-1).bit_length()))}
    for w in W:
        if w: out=add(out,logform(w*w),-Q(w*w,D))
    return out
P=192; SCALE=1<<P; TERMS=80
def ceildiv(a,b): return -(-a//b)
@lru_cache(None)
def ln_unit(a,b):
    ck(b<=a<=2*b)
    zn=a-b; zd=a+b
    zl=zn*SCALE//zd; zu=ceildiv(zn*SCALE,zd)
    z2l=zl*zl//SCALE; z2u=ceildiv(zu*zu,SCALE)
    tl,tu=zl,zu; lo=hi=0
    for j in range(TERMS):
        lo+=2*tl//(2*j+1); hi+=ceildiv(2*tu,2*j+1)
        tl=tl*z2l//SCALE; tu=ceildiv(tu*z2u,SCALE)
    hi+=ceildiv(2*SCALE*9,161*3**161*8)
    return Q(lo,SCALE),Q(hi,SCALE)
LN2=ln_unit(2,1)
@lru_cache(None)
def log_interval(z):
    if z==1: return Q(0),Q(0)
    e=z.bit_length()-1
    if z==1<<e: return Q(e),Q(e)
    lo,hi=ln_unit(z,1<<e)
    return e+lo/LN2[1],e+hi/LN2[0]
def enclose(expr):
    lo=hi=Q(0)
    for z,c in expr.items():
        a,b=log_interval(z)
        lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
    return lo,hi
def scale(expr,c): return {x:v*c for x,v in expr.items() if v*c}
def forms(expr): return {str(x):str(c) for x,c in sorted(expr.items())}
def packet_hist_add(hist,a,b,m=1):
    pair=tuple(sorted((a*a,b*b)))
    hist[pair]=hist.get(pair,0)+m
def compressed(k,l,typ):
    r=2*k+l; a=1+3*k+l; N=1<<r
    hist={}
    if typ=='paired':
        ck(k>0); delta=a-4
        for u in range(k):
            for v in range(l+1):
                mult=comb(k-1,u)*3**u*comb(l,v)
                L=a-4*u-2*v
                if u==v==0: packet_hist_add(hist,N-2*a,-2*(L-4))
                else: packet_hist_add(hist,-2*L,-2*(L-4),mult)
                packet_hist_add(hist,-2*(L-4),-2*(L-4),mult)
    else:
        ck(l>0); delta=a-2
        for u in range(k+1):
            for v in range(l):
                mult=comb(k,u)*3**u*comb(l-1,v)
                L=a-4*u-2*v
                if u==v==0: packet_hist_add(hist,N-2*a,-2*(L-2))
                else: packet_hist_add(hist,-2*L,-2*(L-2),mult)
    ck(sum(hist.values())==N//2)
    B={}
    for (x,y),m in hist.items(): B=add(B,G(x,y),Q(m,N*N))
    d=Q(2*delta,N)
    return hist,B,d
def Aset(k,l):
    r=2*k+l
    return {0}|{1<<i for i in range(r)}|{(1<<(2*j))|(1<<(2*j+1)) for j in range(k)}
def fwht(t):
    a=list(t); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for x in range(j,j+h): a[x],a[x+h]=a[x]+a[x+h],a[x]-a[x+h]
        h*=2
    return a
def certify_table(t):
    W=fwht(t); N=len(t); r=(N-1).bit_length()
    ck(sum(w*w for w in W)==N*N)
    ds=[]; bs=[]; hs=[]
    for i in range(r):
        direct=Q(2*sum(t[x]!=t[x|(1<<i)] for x in range(N) if not(x>>i&1)),N)
        spectral=Q(sum(W[x]**2 for x in range(N) if x>>i&1),N*N)
        ck(direct==spectral); ds.append(direct)
        hist={}
        for x in range(N):
            if not(x>>i&1): packet_hist_add(hist,W[x],W[x|(1<<i)])
        hs.append(hist)
        B={}
        for (a,b),m in hist.items(): B=add(B,G(a,b),Q(m,N*N))
        bs.append(B)
    return W,ds,bs,hs
def restriction_kind(A,r,i,value):
    free=[j for j in range(r) if j!=i]
    Ar={sum(((x>>j)&1)<<s for s,j in enumerate(free)) for x in A if (x>>i&1)==value}
    if not Ar or len(Ar)==1<<(r-1): return 'constant'
    if value:
        ck(Ar=={0} or (len(Ar)==2 and 0 in Ar and max(Ar).bit_count()==1))
        return 'point-defect-with-possible-dummy'
    ck(0 in Ar and all(x.bit_count()<=2 for x in Ar))
    edges=[x for x in Ar if x.bit_count()==2]
    ck(all(not(a&b) for s,a in enumerate(edges) for b in edges[s+1:]))
    ck({x for x in Ar if x.bit_count()==1}=={1<<j for j in range(r-1)})
    return 'partial-matching'

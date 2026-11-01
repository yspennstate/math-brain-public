"""Independent integer Walsh / boundary / symbolic entropy verification, v1.1."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
def factor(n):
    d=2; out={}
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def add(a,b,scale=F(1)):
    c=a.copy()
    for p,v in b.items():
        c[p]=c.get(p,F(0))+scale*v
        if not c[p]: del c[p]
    return c
@lru_cache(maxsize=4096)
def ent(t):
    if not t:return {}
    a=factor(t.numerator); b=factor(t.denominator)
    return {p:t*(b.get(p,0)-a.get(p,0)) for p in set(a)|set(b) if b.get(p,0)!=a.get(p,0)}
@lru_cache(maxsize=4096)
def phi(a,b): return add(add(ent(a),ent(b)),ent(a+b),-1)
def scale(a,t):return {p:v*t for p,v in a.items() if v*t}
def walsh(vals):
    w=vals.copy(); step=1
    while step<len(w):
        for j in range(0,len(w),2*step):
            for l in range(j,j+step):a,b=w[l],w[l+step];w[l]=a+b;w[l+step]=a-b
        step*=2
    return [F(a,len(w)) for a in w]
checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b);checks+=1
def coordinate(vals,w,i):
    influence=F(sum(vals[t]!=vals[t^(1<<i)] for t in range(len(vals))),len(vals))
    spectral=sum(v*v for t,v in enumerate(w) if t&(1<<i))
    eq(influence,spectral)
    erasure={}
    for t,a in enumerate(w):
        if not t&(1<<i):erasure=add(erasure,phi(a*a,w[t|(1<<i)]**2))
    return influence,erasure
def bent(x,k):return -1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2))%2 else 1
def b05(k,r):
    delta=F(1,2**k);s=F(1,2**(k//2));p=F(1,2**r);m=s-delta;a=1-m;t=p*a
    bx=add(scale(phi((s-delta)**2,(s+delta)**2),p/(4*delta)),{2:p*(F(1,2)-delta/2)-2*p*m*m})
    bx=add(bx,scale(phi(a*a,m*m),p-p*p))
    bx=add(bx,phi((1-t)**2,p*p*m*m))
    bz=add({2:2*t-2*t*t},phi((1-t)**2,t*t))
    # Selector computed from the four signed-coefficient multiplicity classes.
    e=p*p*delta*delta; by={}
    # Walsh bent: #positive=(2^k+2^(k/2))/2; empty is positive.
    np=(2**k+2**(k//2))//2-1;nn=(2**k-2**(k//2))//2
    for c,num in [(s,np),(-s,nn)]:by=add(by,scale(phi(p*p*(c-delta)**2,e),num*2**r))
    by=add(by,scale(phi(p*p*(m-1)**2,e),2**r-1))
    by=add(by,phi((1-t)**2,e))
    n=k+r+1;vals=[]
    for v in range(2**n):
        x=v&((1<<k)-1);z=(v>>k)&((1<<r)-1);y=v>>(k+r)
        vals.append(1 if z else (bent(x,k)-2*int(x==0 and y==1)))
    w=walsh(vals)
    for i in range(n):
        inf,B=coordinate(vals,w,i)
        if i<k:eq(inf,p*(F(1,2)+delta));eq(B,bx)
        elif i<k+r:eq(inf,t);eq(B,bz)
        else:eq(inf,p*delta);eq(B,by)
    return {'family':'B05','k':k,'r':r,'n':n,'coordinates_checked':n}
def a062(k):
    M=2**(k-1);q=F(1,2**k);v=F(1,4**M);n=k+1+2*M
    vals=[]
    for a in range(2**n):
        z=a&((1<<k)-1);y=(a>>k)&1;x=a>>(k+1)
        g=(1 if y==0 else -1)*bent(x,2*M)
        vals.append(g if z==0 else 1)
    w=walsh(vals)
    by=add(scale(phi(F(1),v),q-q*q),phi((1-q)**2,q*q*v))
    bz=add({2:2*q-2*q*q},phi((1-q)**2,q*q))
    for i in range(n):
        inf,B=coordinate(vals,w,i)
        if i<k:eq(inf,q);eq(B,bz)
        elif i==k:eq(inf,q);eq(B,by)
        else:eq(inf,q/2);eq(B,{2:q})
    return {'family':'A062','k':k,'M':M,'n':n,'coordinates_checked':n}
start=time.perf_counter();cases=[b05(4,8),b05(4,9)]+[a062(k) for k in (1,2,3)]
out={'helper_version':'check.py/v1.1','cases':cases,'assertions_passed':checks,'failed':0,'arithmetic':'integer Walsh, Fraction boundary and formal prime-log coefficient equality','runtime_seconds':time.perf_counter()-start}
(ROOT/'out'/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))

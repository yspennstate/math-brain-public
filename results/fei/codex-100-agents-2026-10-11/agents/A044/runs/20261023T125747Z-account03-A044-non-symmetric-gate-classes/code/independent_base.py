from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib
root=Path(__file__).resolve().parents[1]
assert (root/'out/FROZEN_INDEPENDENT.json').exists()
start=time.perf_counter();checks=0
def ck(x):
    global checks
    assert x;checks+=1
def cell(t):
    j=0
    while t<=F(1,2):t*=2;j+=1
    return j
def direct(values,p):
    n=len(p);N=1<<n;c=[];v=[]
    for S in range(N):
        mean=F(0)
        for x in range(N):
            weight=F(1);sign=1
            for i in range(n):
                if S>>i&1:
                    weight/=2
                    if not x>>i&1:sign=-sign
                else:weight*=p[i] if x>>i&1 else 1-p[i]
            mean+=sign*weight*values[x]
        c.append(mean)
        prod=F(1)
        for i in range(n):
            if S>>i&1:prod*=4*p[i]*(1-p[i])
        v.append(prod)
    P=[v[s]*c[s]**2 for s in range(N)]
    W=[v[s]/4**cell(abs(c[s])) if s and c[s] else F(0) for s in range(N)]
    w=1-P[0];Z=sum(W)
    Q=[P[0]]+[w*W[s]/Z if w else F(0) for s in range(1,N)]
    return c,P,W,Q,w,Z
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def times(k,a):return (k*a[0],k*a[1]) if k>=0 else (k*a[1],k*a[0])
def minus(a,b):return plus(a,times(-1,b))
z=F(1,3)
lo=2*sum((z**(2*i+1)/F(2*i+1) for i in range(32)),F(0))
LN2=(lo,lo+2*z**65/(65*(1-z*z)))
@lru_cache(None)
def log(x):
    if x==1:return F(0),F(0)
    if x<1:return times(-1,log(1/x))
    j=0
    while x>=2:x/=2;j+=1
    z=(x-1)/(x+1)
    lo=2*sum((z**(2*i+1)/F(2*i+1) for i in range(32)),F(0))
    hi=lo+2*z**65/(65*(1-z*z))
    return plus((lo,hi),times(j,LN2))
def mant(c,P):
    r=(F(0),F(0))
    for s in range(1,len(P)):
        if P[s]:r=plus(r,times(P[s],log(1/(abs(c[s])*2**cell(abs(c[s])))**2)))
    return r
def norm(d):return times(d[4],log(d[5]/d[4]))
def KL(P,Q):
    r=(F(0),F(0))
    for p,q in zip(P,Q):
        if p:r=plus(r,times(p,log(p/q)))
    return r

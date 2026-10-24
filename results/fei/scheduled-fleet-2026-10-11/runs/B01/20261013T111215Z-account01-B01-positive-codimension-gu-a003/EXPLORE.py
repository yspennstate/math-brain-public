#!/usr/bin/env python3
from fractions import Fraction
from math import log2

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return a

def truth(t,k,a,c):
    out=[]
    for mask in range(1<<(2*t+k)):
        x=mask&((1<<t)-1); y=(mask>>t)&((1<<t)-1); z=mask>>(2*t)
        e=((x&y).bit_count()+(a&x).bit_count()+(c&z).bit_count()+int(y==0 and z==0))&1
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

def U(f):
    p=probs(f); q=p[:]; n=len(f).bit_length()-1
    for i in range(n):
        for s in range(1<<n):
            if not (s>>i)&1:q[s]+=q[s|(1<<i)]
    return sum(float(v)*log2(float(q[s]/v)) for s,v in enumerate(p) if v)

def inf(f,i):
    return Fraction(sum(f[s]!=f[s^(1<<i)] for s in range(len(f))),len(f))

best=(-1,None)
bestcoord=(-1,None)
for t in range(0,5):
  for k in range(0,5):
    if t+k==0 or 2*t+k>10: continue
    for a in range(1<<t):
      for c in range(1<<k):
        f=truth(t,k,a,c); u=U(f); n=2*t+k
        ii=sum(inf(f,i) for i in range(n))
        if not ii: continue
        ds=[u-(U(restrict(f,i,0))+U(restrict(f,i,1)))/2 for i in range(n)]
        for i,dv in enumerate(ds):
            iv=float(inf(f,i))
            if iv and dv/iv>bestcoord[0]: bestcoord=(dv/iv,(t,k,a,c,i,dv,iv,u))
        ratio=sum(ds)/float(ii)
        if ratio>best[0]:best=(ratio,(t,k,a,c,u,float(ii),ds))
    print('slice',t,k,'best',best,'coord',bestcoord)
print('FINAL',best)
print('COORD',bestcoord)

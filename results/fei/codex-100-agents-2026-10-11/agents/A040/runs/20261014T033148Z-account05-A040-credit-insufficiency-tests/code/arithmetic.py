# Provenance: A040 stage-3 own helper prefix, no author code.
"""Independent physical-cube review. No author executable is imported."""
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import json, time, sys, hashlib
ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic(); CHECKS=0
def check(ok):
 global CHECKS
 assert ok
 CHECKS+=1
def add(*terms):
 z={}
 for a,v in terms:
  for p,c in v.items():z[p]=z.get(p,F(0))+a*c
 return {p:c for p,c in z.items() if c}
@lru_cache(None)
def fac(n):
 z={};p=2
 while p*p<=n:
  while n%p==0:z[p]=z.get(p,0)+1;n//=p
  p=3 if p==2 else p+2
 if n>1:z[n]=z.get(n,0)+1
 return z
@lru_cache(None)
def lv(x):
 x=F(x);return add((1,fac(x.numerator)),(-1,fac(x.denominator)))
@lru_cache(None)
def ent_atom(p):return add((-p,lv(p))) if p else {}
def ent(P):return add(*[(1,ent_atom(p)) for p in P if p])
@lru_cache(None)
def h(d):return ent([d,1-d])
@lru_cache(None)
def log_bounds(p):
 p=F(p);shift=p.numerator.bit_length()-p.denominator.bit_length();v=p/F(2)**shift
 if v<1:v*=2;shift-=1
 def ln(x):
  t=(x-1)/(x+1);m=24
  low=2*sum((t**(2*j+1)/F(2*j+1) for j in range(m)),F(0))
  return low,low+2*t**(2*m+1)/((2*m+1)*(1-t*t))
 a,b=ln(v);c,d=ln(F(2));return shift+a/d,shift+b/c
def bounds(v):
 lo=hi=F(0)
 for p,c in v.items():
  a,b=log_bounds(p);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
 return lo,hi
def packed(v):
 lo,hi=bounds(v);grid=10**25
 return {'prime_log_vector':{str(p):str(c) for p,c in sorted(v.items())},'lower':str(F(lo.numerator*grid//lo.denominator,grid)),'upper':str(F(-((-hi.numerator*grid)//hi.denominator),grid))}
def fwht(v):
 a=list(v);stride=1
 while stride<len(a):
  for base in range(0,len(a),2*stride):
   for j in range(base,base+stride):x,y=a[j],a[j+stride];a[j],a[j+stride]=x+y,x-y
  stride*=2
 return tuple(a)
def halves(v,i):
 return tuple(v[x] for x in range(len(v)) if not(x>>i&1)),tuple(v[x|(1<<i)] for x in range(len(v)) if not(x>>i&1))
def infs(v):
 N=len(v)
 return tuple(F(sum(v[x]!=v[x|(1<<i)] for x in range(N) if not(x>>i&1)),N//2) for i in range(N.bit_length()-1))
@lru_cache(None)
def spectrum(v):
 N=len(v);W=fwht(v);P=tuple(F(w*w,N*N) for w in W);d=infs(v)
 check(sum(P)==1)
 check(d==tuple(sum((p for s,p in enumerate(P) if s>>i&1),F(0)) for i in range(len(d))))
 H=ent(P);TC=add(*[(1,h(x)) for x in d],(-1,H))
 return P,d,H,TC,W
def core(kind,k):
 if kind=='dictator':return (1,-1)
 vals=[]
 for x in range(1<<(k+(2 if kind=='selector' else 1))):
  data=x&((1<<k)-1);b=(-1)**sum((data>>(2*j)&1)*(data>>(2*j+1)&1) for j in range(k//2))
  if kind=='selector' and (x>>k&1) and data==0:b=-b
  z=x>>(k+(1 if kind=='selector' else 0))&1
  vals.append((-1)**z*b)
 return tuple(vals)
def build(L,R,T,g):
 n=1+L+R+T;out=[];A=[]
 for c in range(1<<n):
  X=c&1;W=((c>>1)&((1<<L)-1))==((1<<L)-1)
  U=((c>>(1+L))&((1<<R)-1))==((1<<R)-1)
  V=((c>>(1+L+R))&((1<<T)-1))==((1<<T)-1)
  A.append(int((X and (U or V)) or (W and U and V)))
 for v in range((1<<n)*len(g)):out.append(g[v>>n] if A[v&((1<<n)-1)] else 1)
 return tuple(out),tuple(A),n
def signed_influence_indicator(A):return sum(infs(tuple(1-2*a for a in A)))/2
def odd_faces(v):
 N=len(v);total=0
 for i in range(N.bit_length()-1):
  for j in range(i):
   mask=(1<<i)|(1<<j)
   total+=sum(v[x]*v[x|(1<<i)]*v[x|(1<<j)]*v[x|mask]<0 for x in range(N) if x&mask==0)
 return F(2*total,N)

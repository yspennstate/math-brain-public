from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import json,time,sys
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; N=0
def ck(x):
 global N
 N+=1
 assert x,N
def fw(t):
 a=list(t); k=1
 while k<len(a):
  for i in range(0,len(a),2*k):
   for j in range(k):
    u,v=a[i+j],a[i+j+k]; a[i+j],a[i+j+k]=u+v,u-v
  k*=2
 return {s:F(v,len(a)) for s,v in enumerate(a) if v}
def add(*xs):
 r={}
 for d in xs:
  for k,v in d.items(): r[k]=r.get(k,F(0))+v
 return {k:v for k,v in r.items() if v}
def scale(d,c): return {k:v*c for k,v in d.items() if v*c}
@lru_cache(None)
def log(q):
 q=F(q); assert q>0; r={}
 for n,sgn in [(q.numerator,1),(q.denominator,-1)]:
  d=2
  while d*d<=n:
   while n%d==0: r[d]=r.get(d,0)+sgn; n//=d
   d+=1
  if n>1: r[n]=r.get(n,0)+sgn
 return {k:F(v) for k,v in r.items() if v}
def H(p): return add(*(scale(log(v),-v) for v in p.values() if v))
def CE(p,q): return add(*(scale(log(q[k]),-v) for k,v in p.items() if v))
def KL(p,q): return add(CE(p,q),scale(H(p),-1))
def unit(q):
 z=(q-1)/(q+1); z2=z*z; power=z; s=F(0)
 for k in range(48): s+=2*power/F(2*k+1); power*=z2
 e=2*abs(power)/(97*(1-z2)); return s-e,s+e
L2=unit(F(2))
@lru_cache(None)
def ln(q):
 q=F(q); k=0
 while q>=2: q/=2; k+=1
 while q<1: q*=2; k-=1
 lo,hi=unit(q)
 return lo+k*(L2[0] if k>=0 else L2[1]),hi+k*(L2[1] if k>=0 else L2[0])
def interval(expr):
 lo=hi=F(0)
 for q,v in expr.items():
  a,b=ln(q); lo+=v*(a if v>=0 else b); hi+=v*(b if v>=0 else a)
 return lo,hi
def spec(t): return {s:v*v for s,v in fw(t).items()}
TABLES=[[1 if w>>x&1 else -1 for x in range(4)] for w in range(16)]
def ref(j,mass=F(1)):
 return {s:mass*F(1+(j%2),3)**s.bit_count()*F(2-(j%2),3)**(2-s.bit_count()) for s in range(4)}
def calibrate(R,p):
 e=p.get(0,F(0)); out={0:e}
 if e<1:
  for s,v in R.items():
   if s: out[s]=(1-e)*v/(1-R[0])
 return {s:v for s,v in out.items() if v}

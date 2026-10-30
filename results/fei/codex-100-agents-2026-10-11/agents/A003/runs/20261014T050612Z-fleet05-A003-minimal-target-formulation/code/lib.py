from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,math
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();count=0
def check(ok):
 global count
 count+=1
 assert ok,count
 assert time.perf_counter()-start<58,'frozen time limit'
def fw(values):
 a=list(values);step=1
 while step<len(a):
  for p in range(0,len(a),2*step):
   for j in range(p,p+step):
    u,v=a[j],a[j+step];a[j],a[j+step]=u+v,u-v
  step*=2
 return [Q(x,len(a)) for x in a]
@lru_cache(None)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def add(*terms):
 out={}
 for scale,item in terms:
  for p,v in item.items():out[p]=out.get(p,Q(0))+scale*v
 return {p:v for p,v in out.items() if v}
@lru_cache(None)
def xlog(x):
 if not x:return {}
 return add((x,factors(x.numerator)),(-x,factors(x.denominator)))
@lru_cache(None)
def phi(a,b):return add((1,xlog(a+b)),(-1,xlog(a)),(-1,xlog(b)))
def entropy(p):return add(*[(-1,xlog(v)) for v in p])
def edge(p,i):return add(*[(1,phi(p[t],p[t|(1<<i)])) for t in range(len(p)) if not t&(1<<i)])
def inf(p,i):return sum((v for t,v in enumerate(p) if t&(1<<i)),Q(0))
def majority(M,fixed):
 n=M-len(fixed)
 return [1 if sum(fixed)+n-2*b.bit_count()>0 else -1 for b in range(1<<n)]
def law(coeff):return [v*v for v in coeff]
def normalize(p,n):
 a=p[0];v=1-a
 if not v:return
 r=[Q(0)]+[x/v for x in p[1:]]
 B=add(*[(1,edge(p,i)) for i in range(n)])
 Br=add(*[(1,edge(r,i)) for i in range(n)])
 t0=add(*[(1,phi(a,p[1<<i])) for i in range(n)])
 check(B==add((v,Br),(1,t0)))
 check(add((1,entropy(p)),(-1,B))==add((1,phi(a,v)),(v,entropy(r)),(-v,Br),(-1,t0)))

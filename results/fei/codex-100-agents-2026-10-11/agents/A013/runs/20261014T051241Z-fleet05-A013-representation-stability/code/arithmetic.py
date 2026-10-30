from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def check(b):
 global checks
 checks+=1
 if time.perf_counter()-start>50:raise RuntimeError('50 second internal cutoff')
 if not b:raise AssertionError(checks)
def fwht(t):
 a=list(t);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):
    u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
  h*=2
 return [F(x,len(a)) for x in a]
@lru_cache(None)
def factors(n):
 out=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:out.append((p,e))
  p+=1
 if n>1:out.append((n,1))
 return tuple(out)
@lru_cache(None)
def lv(x):
 x=F(x);assert x>0;a={}
 for p,e in factors(x.numerator):a[p]=F(e)
 for p,e in factors(x.denominator):a[p]=a.get(p,F(0))-e
 return {p:e for p,e in a.items() if e}
def add(a,b,k=F(1)):
 a=dict(a)
 for p,v in b.items():
  a[p]=a.get(p,F(0))+k*v
  if not a[p]:del a[p]
 return a
def mul(a,k):return {p:v*k for p,v in a.items() if v*k}
def H(p):
 a={}
 for x in p:
  if x:a=add(a,lv(1/x),x)
 return a
def CE(p,q):
 a={}
 for x,y in zip(p,q):
  if x:
   check(y>0);a=add(a,lv(1/y),x)
 return a
def lniv(x):
 u=(x-1)/(x+1);lo=sum((2*u**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
 return lo,lo+2*u**41/(41*(1-u*u))
lnlo,lnhi=lniv(F(2));check(lnlo>F(2,3));check(lnhi<1)
@lru_cache(None)
def logiv(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 lo,hi=lniv(x);return F(k)+lo/lnhi,F(k)+hi/lnlo
def iv(v):
 lo=hi=F(0)
 for p,c in v.items():
  a,b=logiv(p);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
 return lo,hi
def nonneg(v):check(not v or iv(v)[0]>=0)
def refs(p):
 u=[F(1,len(p))]*len(p)
 return [p,u,[(a+b)/2 for a,b in zip(p,u)]]
def cal(p,r,shared):
 rem=1-sum(p[s] for s in shared);old=1-sum(r[s] for s in shared)
 assert not rem or old>0
 return [p[s] if s in shared else (rem*r[s]/old if rem else F(0)) for s in range(len(p))]
def influence(t,n):return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(n)]


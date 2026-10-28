from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,sys,time
R=Path(__file__).resolve().parents[1];O=R/'out';assert (O/'FROZEN_SPEC.json').exists();start=time.perf_counter();pilot='--pilot' in sys.argv;checks=0

def ck(v):
 global checks
 checks+=1
 assert v,checks
 assert time.perf_counter()-start<55,'frozen 55s guard'

def fft(v):
 a=list(v);h=1
 while h<len(a):
  for i in range(0,len(a),h*2):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return tuple(F(x,len(a)) for x in a)
def direct(v):return tuple(F(sum(z*(-1 if (x&s).bit_count()%2 else 1) for x,z in enumerate(v)),len(v)) for s in range(len(v)))
@lru_cache(None)
def spectrum(v):
 a=fft(v);p=tuple(x*x for x in a);ck(sum(p)==1);return p
@lru_cache(None)
def factors(n):
 out=[];p=2
 while p*p<=n:
  count=0
  while n%p==0:n//=p;count+=1
  if count:out.append((p,count))
  p=3 if p==2 else p+2
 if n>1:out.append((n,1))
 return tuple(out)
@lru_cache(None)
def logform(x):
 assert x>0
 d=dict(factors(x.numerator))
 for p,k in factors(x.denominator):d[p]=d.get(p,0)-k
 return tuple((p,F(k)) for p,k in d.items() if k)
def linear(*terms):
 d={}
 for scale,form in terms:
  for p,k in form:d[p]=d.get(p,F(0))+scale*k
 return tuple(sorted((p,k) for p,k in d.items() if k))
def ce(p,q):
 terms=[]
 for x,y in zip(p,q):
  if x:ck(y>0);terms.append((-x,logform(y)))
 return linear(*terms)
def ins(x,j,b):return x%2**j+(x//2**j)*2**(j+1)+b*2**j
def children(v,j):return [tuple(v[ins(x,j,b)] for x in range(len(v)//2)) for b in (0,1)]
def marginal(v,j):return tuple(v[ins(x,j,0)]+v[ins(x,j,1)] for x in range(len(v)//2))
def erasure(p,j):
 terms=[]
 for x in range(len(p)//2):
  p0,p1=p[ins(x,j,0)],p[ins(x,j,1)];w=p0+p1
  for y in [p0,p1]:
   if y:terms.append((y,logform(w/y)))
 return linear(*terms)
def dstar(p,q,j):
 terms=[]
 for x in range(1,len(p)//2):
  ps=[p[ins(x,j,b)] for b in (0,1)];qs=[q[ins(x,j,b)] for b in (0,1)];w=sum(ps);v=sum(qs)
  for a,b in zip(ps,qs):
   if a:ck(v>0 and b>0);terms.append((a,logform(a*v/(w*b))))
 return linear(*terms)
@lru_cache(None)
def controller(a):
 b=tuple(1-v*v for v in a);return b,fft(a),fft(b),F(sum(b),len(b))
@lru_cache(None)
def wrapper(a,h,sigma):
 b,_,_,_=controller(a);return tuple(a[x]+sigma*b[x]*h[y] for y in range(len(h)) for x in range(len(a)))
def reference(a,h,sigma,q):
 b,A,B,beta=controller(a);m=F(sum(h),len(h));out=tuple((A[u]+sigma*m*B[u])**2 if v==0 else B[u]**2*q[v] for v in range(len(h)) for u in range(len(a)));ck(sum(out)==1);return out
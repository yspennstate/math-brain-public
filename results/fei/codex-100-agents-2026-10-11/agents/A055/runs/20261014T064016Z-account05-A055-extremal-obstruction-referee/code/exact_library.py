from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parents[1]
MODE=sys.argv[1]; START=time.perf_counter(); N=0
def ck(v):
 global N
 assert v, N
 N+=1
 assert time.perf_counter()-START<55
def add(*ds):
 r={}
 for d in ds:
  for p,c in d.items():r[p]=r.get(p,Q(0))+c
 return {p:c for p,c in r.items() if c}
def scale(d,c):return {p:c*v for p,v in d.items() if c*v}
@lru_cache(None)
def fac(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def lg(q):return add(fac(q.numerator),scale(fac(q.denominator),-1))
def ent(ps):return add(*(scale(lg(p),-p) for p in ps if p))
@lru_cache(None)
def ln(p):
 k=p.bit_length()-1;r=Q(p,1<<k);z=(r-1)/(r+1)
 if p==2:z=Q(1,3);k=0
 low=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(32)),Q(0))
 tail=2*z**65/(65*(1-z*z))
 if k:
  a,b=ln(2);low+=k*a;tail+=k*(b-a)
 return low,low+tail
def iv(d):
 a=b=Q(0)
 for p,c in d.items():
  l,h=ln(p);a+=c*(l if c>=0 else h);b+=c*(h if c>=0 else l)
 return a,b
def nonneg(d):ck(not d or iv(d)[0]>=0)
def enc(d):return {str(p):str(c) for p,c in d.items()}
def bits(d):
 a,b=iv(d);l,h=ln(2);v=[a/l,a/h,b/l,b/h];return [str(min(v)),str(max(v))]
def fw(f):
 return [Q(sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(len(f))),len(f)) for s in range(len(f))]
def restrict(f,i,b):
 return [f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(f)//2)]
def data(f):
 a=fw(f);p=[x*x for x in a];ck(sum(p)==1)
 I=sum(s.bit_count()*x for s,x in enumerate(p));n=len(f).bit_length()-1
 ck(I==Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f)) for i in range(n)),len(f)))
 return a,ent(p),I


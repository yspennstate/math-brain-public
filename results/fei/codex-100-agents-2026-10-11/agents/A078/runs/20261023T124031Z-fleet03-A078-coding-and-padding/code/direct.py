from fractions import Fraction as F
from itertools import product
from functools import lru_cache
from pathlib import Path
import json,time,hashlib
def plus(*terms):
 z={}
 for c,d in terms:
  for p,v in d.items():z[p]=z.get(p,F(0))+c*v
 return {p:v for p,v in z.items() if v}
@lru_cache(None)
def prime(n):
 z={};p=2
 while p*p<=n:
  while n%p==0:z[p]=z.get(p,0)+1;n//=p
  p+=1
 if n>1:z[n]=z.get(n,0)+1
 return z
@lru_cache(None)
def gg(x):
 if not x:return {}
 q=x*x
 return plus(*[(-q*s,{p:F(v) for p,v in prime(n).items()}) for n,s in [(q.numerator,1),(q.denominator,-1)]])
@lru_cache(None)
def spectrum(v):
 return tuple(F(sum(y*(-1 if (i&s).bit_count()%2 else 1) for i,y in enumerate(v)),len(v)) for s in range(len(v)))
def entropy(v):return plus(*[(1,gg(a)) for a in spectrum(v)])
@lru_cache(None)
def lg(p):
 if p==2:return F(1),F(1)
 def ln(x):
  a=(x-1)/(x+1)
  lo=sum((2*a**(2*k+1)/F(2*k+1) for k in range(24)),F(0))
  return lo,lo+2*a**49/(49*(1-a*a))
 k=p.bit_length()-1;a,b=ln(F(p,2**k));c,d=ln(F(2))
 return F(k)+a/d,F(k)+b/c
def positive(x):
 lo=F(0)
 for p,c in x.items():
  a,b=lg(p);lo+=c*(a if c>=0 else b)
 return lo>=0
def child(v,i,b):return tuple(y for x,y in enumerate(v) if (x>>i)&1==b)
def influence(v,i):return F(sum(y!=v[x^(1<<i)] for x,y in enumerate(v)),len(v))

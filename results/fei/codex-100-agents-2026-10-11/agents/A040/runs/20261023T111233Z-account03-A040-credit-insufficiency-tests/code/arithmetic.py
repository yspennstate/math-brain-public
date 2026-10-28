from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys,itertools,hashlib
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
Z=(F(0),F(0))
GRID=2**120
def rounded(a):return F(a[0].numerator*GRID//a[0].denominator,GRID),F(-((-a[1].numerator*GRID)//a[1].denominator),GRID)
def ck(b):
 global checks
 assert b
 checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('frozen runtime exceeded')
def add(a,b):return rounded((a[0]+b[0],a[1]+b[1]))
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
@lru_cache(None)
def lnunit(x):
 z=(x-1)/(x+1);s=F(0);t=z
 for k in range(36):s+=t/F(2*k+1);t*=z*z
 rem=2*t/F(73)/(1-z*z)
 return 2*s,2*s+rem
L2=lnunit(F(2))
@lru_cache(None)
def log(x):
 assert x>0
 k=x.numerator.bit_length()-x.denominator.bit_length();v=x/F(2)**k
 if v<1:v*=2;k-=1
 l,u=lnunit(v)
 return rounded((l/L2[1]+k,u/L2[0]+k))
@lru_cache(None)
def entterm(x):return scale(log(x),-x) if x else Z
def entropy(p):
 o=Z
 for x in p:o=add(o,entterm(x))
 return o
def kl(p,q):
 o=Z
 for x,y in zip(p,q):
  if x:assert y>0;o=add(o,scale(sub(log(x),log(y)),x))
 return o
@lru_cache(None)
def spectrum(g):
 v=list(g);h=1
 while h<len(v):
  for b in range(0,len(v),2*h):
   for i in range(b,b+h):a,c=v[i],v[i+h];v[i],v[i+h]=a+c,a-c
  h*=2
 return tuple(F(a,len(g)) for a in v)
def law(g):return tuple(a*a for a in spectrum(g))
def infl(g,i):return F(sum(g[x]!=g[x^(1<<i)] for x in range(len(g))),len(g))
def influence(g):return sum((infl(g,i) for i in range(len(g).bit_length()-1)),F(0))
def restrict(g,i,b):return tuple(y for x,y in enumerate(g) if (x>>i)&1==b)

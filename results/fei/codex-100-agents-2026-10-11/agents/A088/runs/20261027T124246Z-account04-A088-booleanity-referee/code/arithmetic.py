from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys,itertools,hashlib
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0

def ck(v):
 global checks
 assert v
 checks+=1
 assert time.monotonic()-start<60

Q=1<<100
@lru_cache(None)
def ln_interval(x):
 x=F(x); k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 z=(x-1)/(x+1); zn=z; low=0
 for j in range(32):
  term=2*zn/(2*j+1); low+=term.numerator*Q//term.denominator
  zn*=z*z
 rem=2*zn/(65*(1-z*z)); hi=low+32+(rem.numerator*Q+rem.denominator-1)//rem.denominator
 if k:
  a,b=ln_interval(F(2)) if x!=2 else (None,None)
  low,hi=(low+k*a,hi+k*b) if k>=0 else (low+k*b,hi+k*a)
 return low,hi
# Avoid recursive ln(2) reduction.
z=F(1,3); t=z; ls=0
for j in range(32):
 term=2*t/(2*j+1);ls+=term.numerator*Q//term.denominator;t*=z*z
rem=2*t/(65*(1-z*z)); LN2=(ls,ls+32+(rem.numerator*Q+rem.denominator-1)//rem.denominator)
ln_interval.cache_clear()
# separate normalized logarithm, integer exponent handled against known ln2
@lru_cache(None)
def log2i(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 a,b=ln_interval(x)
 return F(a,LN2[1])+k,F(b,LN2[0])+k

def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def H(p):
 a=(F(0),F(0))
 for v in p:
  if v:a=add(a,scale(log2i(v),-v))
 return a
def CE(p,q):
 a=(F(0),F(0))
 for v,u in zip(p,q):
  if v:
   ck(u>0);a=add(a,scale(log2i(u),-v))
 return a

def spec(t):
 a=list(t);N=len(a);h=1
 while h<N:
  for i in range(0,N,2*h):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return tuple(F(x*x,N*N) for x in a)
def inf(t):
 n=len(t).bit_length()-1
 return sum(F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n))
def res(t,i,v):return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(v<<i)] for x in range(len(t)//2))
def marg(q,i):return tuple(q[(x&((1<<i)-1))|((x>>i)<<(i+1))]+q[(x&((1<<i)-1))|((x>>i)<<(i+1))|(1<<i)] for x in range(len(q)//2))
def phase(n,edges):return tuple((-1)**(sum(((x>>i)&1)*((x>>j)&1) for i,j in edges)%2) for x in range(1<<n))
def rank(n,edges):
 rows=[sum(1<<j for j in range(n) if (min(i,j),max(i,j)) in edges) for i in range(n)];r=0
 for j in range(n):
  z=next((k for k in range(r,n) if rows[k]>>j&1),None)
  if z is not None:
   rows[r],rows[z]=rows[z],rows[r]
   for k in range(n):
    if k!=r and rows[k]>>j&1:rows[k]^=rows[r]
   r+=1
 return r


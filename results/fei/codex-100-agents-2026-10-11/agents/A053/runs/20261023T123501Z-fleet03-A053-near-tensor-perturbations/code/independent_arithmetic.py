from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache
from collections import Counter
import json,time
RUNDIR=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
 if time.perf_counter()-start>55:raise RuntimeError('55 second guard')
def direct(f):
 return [sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(f)) for s in range(len(f))]
def directional(f,v):
 return Q(sum(y!=f[x^v] for x,y in enumerate(f)),len(f))
def inf(f):
 return sum(directional(f,1<<j) for j in range((len(f)-1).bit_length()))
def restrict(f,i,b):
 n=(len(f)-1).bit_length()
 out=[]
 for x in range(1<<n):
  if (x>>i)&1==b:out.append(f[x])
 return out
@lru_cache(None)
def ln_interval(x):
 z=(x-1)/(x+1);z2=z*z;v=z;s=Q(0)
 for j in range(32):s+=2*v/Q(2*j+1);v*=z2
 err=2*abs(v)/(65*(1-z2))
 return s-err,s+err
L2=ln_interval(Q(2));ck(L2[0]>Q(2,3))
@lru_cache(None)
def logs(x):
 power=0
 while x<1:x*=2;power-=1
 while x>=2:x/=2;power+=1
 lo,hi=ln_interval(x)
 return power+lo/L2[1],power+hi/L2[0]
@lru_cache(None)
def entropy_key(key,N):
 low=high=Q(0)
 for v,k in key:
  if v:
   p=Q(v,N*N);l,h=logs(p);low-=k*p*h;high-=k*p*l
 return low,high
def ent(f):
 w=direct(f)
 return entropy_key(tuple(sorted(Counter(v*v for v in w).items())),len(f))
def affine_min(f):
 n=(len(f)-1).bit_length();basis={};total=Q(0)
 costs=sorted((min(directional(f,v),1-directional(f,v)),v) for v in range(1,1<<n))
 for cost,v in costs:
  x=v
  for bit,pivot in sorted(basis.items(),reverse=True):
   if x>>bit&1:x^=pivot
  if x:
   basis[x.bit_length()-1]=x;total+=cost
   if len(basis)==n:break
 ck(len(basis)==n)
 return total

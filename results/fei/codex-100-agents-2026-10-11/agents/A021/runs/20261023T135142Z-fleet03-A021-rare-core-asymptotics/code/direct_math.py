from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
ROOT=Path(__file__).resolve().parents[1];count=0
def ck(x,label):
 global count
 count+=1;assert x,(count,label)
def add(*xs):
 d={}
 for x in xs:
  for b,c in x.items():d[b]=d.get(b,F(0))+c
 return {b:c for b,c in d.items() if c}
def scale(x,c):return {b:a*c for b,a in x.items() if a*c}
def log(x):
 x=F(x);ans={}
 for n,s in [(x.numerator,1),(x.denominator,-1)]:
  p=2
  while n>1:
   while n%p==0:ans[p]=ans.get(p,0)+s;n//=p
   p+=1
 return {p:F(c) for p,c in ans.items() if c}
@lru_cache(None)
def li(n):
 k=n.bit_length()-1;y=F(n,2**k)
 def ln(y):
  z=(y-1)/(y+1);s=F(0);term=z
  for j in range(48):s+=2*term/(2*j+1);term*=z*z
  return s,s+2*term/(97*(1-z*z))
 a,b=ln(y);c,d=ln(F(2));return k+a/d,k+b/c
def lower(x):return sum((c*li(p)[0 if c>=0 else 1] for p,c in x.items()),F(0))
def spectrum(a):
 N=len(a);return [F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(a))**2,N*N) for s in range(N)]

from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def fw(v):
 a=list(v);step=1
 while step<len(a):
  for i in range(0,len(a),2*step):
   for j in range(i,i+step):a[j],a[j+step]=a[j]+a[j+step],a[j]-a[j+step]
  step*=2
 return [F(z,len(a)) for z in a]
def insert(W,j,b):return (W&((1<<j)-1))|((W>>j)<<(j+1))|(b<<j)
def inf(v):return [F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v)) for j in range(len(v).bit_length()-1)]
@lru_cache(None)
def log(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def ln(z):
  w=(z-1)/(z+1);lo=2*sum((w**(2*i+1)/F(2*i+1) for i in range(32)),F(0))
  return lo,lo+2*w**65/(65*(1-w*w))
 a,b=ln(x);c,d=ln(F(2));lo=F(k)+a/d;hi=F(k)+b/c;scale=2**100
 return F((lo.numerator*scale)//lo.denominator,scale),F(-((-hi.numerator*scale)//hi.denominator),scale)
def ce(P,Q):
 lo=hi=F(0)
 for p,q in zip(P,Q):
  if p:
   ck(q>0);a,b=log(1/q);lo+=p*a;hi+=p*b
 return lo,hi
def entropy(P):return ce(P,P)
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def avg(a,b):return (a[0]+b[0])/2,(a[1]+b[1])/2
def display(x):return [str(x[0]),str(x[1])]

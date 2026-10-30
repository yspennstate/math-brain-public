from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import json
BITS=384;GRID=1<<BITS
def series(z):
 s=Q(0);w=z
 for j in range(48):s+=2*w/(2*j+1);w*=z*z
 return s,s+2*w/(97*(1-z*z))
LN=series(Q(1,3))
def rnd(x):return Q((x[0]*GRID).__floor__(),GRID),Q((x[1]*GRID).__ceil__(),GRID)
def add(*xs):return sum((x[0] for x in xs),Q(0)),sum((x[1] for x in xs),Q(0))
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def scale(c,x):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
@lru_cache(None)
def ell(x):
 if not x:return Q(0),Q(0)
 assert 0<x<=1
 if x>Q(1,2):
  l,h=series((1-x)/(1+x));return rnd((x*l/LN[1],x*h/LN[0]))
 k=x.numerator.bit_length()-x.denominator.bit_length();y=x/Q(2)**k
 if y<1:y*=2;k-=1
 z=(y-1)/(y+1);Z=1<<192
 l=series(Q((z*Z).__floor__(),Z))[0];h=series(Q((z*Z).__ceil__(),Z))[1]
 return rnd((-x*(k+h/LN[0]),-x*(k+l/LN[1])))
def ent(ps):return rnd(add(*(ell(p) for p in ps)))
def ent_counts(cs):return rnd(add(*(scale(count,ell(mass)) for mass,count in cs.items() if mass)))
def h2(p):return add(ell(p),ell(1-p))
def walsh(tab):
 w=list(tab);s=1
 while s<len(w):
  for j in range(0,len(w),2*s):
   for i in range(j,j+s):u,v=w[i],w[i+s];w[i],w[i+s]=u+v,u-v
  s*=2
 return [Q(x,len(w)) for x in w]
def overlap(x,y):return max(x[0],y[0])<=min(x[1],y[1])
def dump(path,obj):path.write_text(json.dumps(obj,indent=2,default=str),encoding='utf-8')

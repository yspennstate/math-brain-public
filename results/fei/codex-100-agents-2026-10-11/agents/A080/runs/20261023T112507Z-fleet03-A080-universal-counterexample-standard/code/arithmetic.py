"""Positive-series log enclosures, integer fixed point, no floating decisions."""
from fractions import Fraction as Q
from functools import lru_cache
import json
BITS=384
GRID=1<<BITS
TERMS=96
def floor(q):return q.numerator//q.denominator
def ceil(q):return -((-q.numerator)//q.denominator)
def round_iv(lo,hi):return Q(floor(lo*GRID),GRID),Q(ceil(hi*GRID),GRID)
def add(*xs):return sum((x[0] for x in xs),Q(0)),sum((x[1] for x in xs),Q(0))
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def scale(c,x):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def series(z):
 assert 0<=z<=Q(1,3)
 zl=floor(z*GRID);zh=ceil(z*GRID)
 wl,wh=zl,zh
 sl=sh=0
 zzl=zl*zl//GRID;zzh=(zh*zh+GRID-1)//GRID
 for j in range(TERMS):
  sl+=2*wl//(2*j+1);sh+=(2*wh+2*j)//(2*j+1)
  wl=wl*zzl//GRID;wh=(wh*zzh+GRID-1)//GRID
 # 2*z^(193)/(193*(1-z*z)) <= 9/(772*3^191).
 tail=Q(9,772*3**191)
 return Q(sl,GRID),Q(sh+ceil(tail*GRID),GRID)
LN=series(Q(1,3))
@lru_cache(None)
def ell(x):
 if not x:return Q(0),Q(0)
 assert 0<x<=1
 k=x.numerator.bit_length()-x.denominator.bit_length()
 y=x/Q(2)**k
 if y<1:y*=2;k-=1
 lo,hi=series((y-1)/(y+1))
 return round_iv(-x*(k+hi/LN[0]),-x*(k+lo/LN[1]))
def ent(ps):return add(*(ell(p) for p in ps))
def h2(p):return add(ell(p),ell(1-p))
def overlap(x,y):return max(x[0],y[0])<=min(x[1],y[1])
def dump(path,obj):path.write_text(json.dumps(obj,indent=2,default=str),encoding='utf-8')

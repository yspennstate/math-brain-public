from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); pilot='--pilot' in sys.argv;checks=0;limit=55 if pilot else 175
def ck(c):
 global checks
 checks+=1
 assert c
 if time.perf_counter()-start>limit:raise RuntimeError('frozen runtime limit')
def add(*terms):
 d={}
 for a,b in terms:
  for k,v in a.items():d[k]=d.get(k,F(0))+v*b
 return {k:v for k,v in d.items() if v}
@lru_cache(None)
def fac(a):
 d={};k=2
 while k*k<=a:
  while a%k==0:d[k]=d.get(k,0)+1;a//=k
  k+=1
 if a>1:d[a]=d.get(a,0)+1
 return d
def logv(q):return add((fac(q.numerator),1),(fac(q.denominator),-1))
def entropy(ws):
 d={}
 for w in ws:
  if w:d=add((d,1),(logv(w),-w))
 return d
@lru_cache(None)
def logbound(k):
 shift=k.bit_length()-1;z=F(1,3) if k==2 else F(k-2**shift,k+2**shift)
 lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
 hi=lo+2*z**65/(65*(1-z*z))
 if k!=2:
  a,b=logbound(2);lo+=shift*a;hi+=shift*b
 scale=1<<112
 return F(lo.numerator*scale//lo.denominator,scale),F(-((-hi.numerator*scale)//hi.denominator),scale)
def interval(v):
 lo=hi=F(0)
 for k,c in v.items():
  a,b=logbound(k);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return lo,hi
def ge(v):
 if not v:return True
 lo,hi=interval(v);ck(lo>0 or hi<0);return lo>0
def nonneg(v):ck(ge(v))
def vec(v):return {str(k):str(x) for k,x in sorted(v.items())}
def serial(q):
 if isinstance(q,F):return str(q)
 if isinstance(q,dict):return {str(k):serial(v) for k,v in q.items()}
 if isinstance(q,(tuple,list)):return [serial(v) for v in q]
 return q
def save(name,obj):(ROOT/'out'/name).write_text(json.dumps(serial(obj),indent=2)+'\n',encoding='utf-8')
@lru_cache(None)
def spec(h):
 a=list(h);N=len(a);w=1
 while w<N:
  for i in range(0,N,2*w):
   for j in range(w):u=a[i+j];v=a[i+j+w];a[i+j]=u+v;a[i+j+w]=u-v
  w*=2
 return tuple(F(x*x,N*N) for x in a)
def direct(h):
 N=len(h)
 return tuple(F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(h))**2,N*N) for s in range(N))
@lru_cache(None)
def raw(h):return entropy(spec(h))
def energy(h,A):return sum((p*(s&A).bit_count() for s,p in enumerate(spec(h))),F(0))
def edges(h,A):return F(sum((h[x]-h[x^(1<<i)])**2 for i in range(len(h).bit_length()-1) if A>>i&1 for x in range(len(h))),4*len(h))
def mass(h):return F(sum(v*v for v in h),len(h))
@lru_cache(None)
def children(h,A):
 n=len(h).bit_length()-1;a=[i for i in range(n) if A>>i&1];c=[i for i in range(n) if not A>>i&1]
 def scatter(z,ids):return sum((z>>j&1)<<i for j,i in enumerate(ids))
 return tuple(tuple(h[scatter(x,a)|scatter(y,c)] for y in range(1<<len(c))) for x in range(1<<len(a)))
@lru_cache(None)
def ledger(h,A):
 ch=children(h,A);avg={}
 for v in ch:avg=add((avg,1),(raw(v),F(1,len(ch))))
 L=add((raw(h),1),(avg,-1));m={}
 for s,q in enumerate(spec(h)):m[s&~A]=m.get(s&~A,F(0))+q
 B=add((raw(h),1),(entropy(m.values()),-1));J=add((L,1),(B,-1))
 return L,B,J
def components(h):
 rem={x for x,v in enumerate(h) if v};out=[];n=len(h).bit_length()-1
 while rem:
  seed=min(rem);rem.remove(seed);vis={seed};todo=[seed]
  while todo:
   x=todo.pop()
   for i in range(n):
    y=x^(1<<i)
    if y in rem:rem.remove(y);vis.add(y);todo.append(y)
  out.append(tuple(int(x in vis) for x in range(len(h))))
 return out
def projection(h,A):return {x&A for x,v in enumerate(h) if v}

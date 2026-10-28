from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import json,time,math
BASE=Path(__file__).resolve().parent.parent
START=time.monotonic();COUNT=0
def ck(x):
 global COUNT
 COUNT+=1;assert x,COUNT;assert time.monotonic()-START<60
S=1<<160
def iv(x):
 x=F(x)*S;return x.numerator//x.denominator,-((-x.numerator)//x.denominator)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,q):
 q=F(q);x,y=(a[0]*q,a[1]*q) if q>=0 else (a[1]*q,a[0]*q)
 return x.numerator//x.denominator,-((-y.numerator)//y.denominator)
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v)//S,-((-max(v))//S)
def series(q):
 z=iv((q-1)/(q+1));z2=mul(z,z);power=z;out=(0,0)
 for j in range(40):out=add(out,scale(power,F(2,2*j+1)));power=mul(power,z2)
 # Range-reduced z in [0,1/3], tail after j39 <= 2*(1/3)^81/(81*(1-1/9)).
 tail=iv(F(2,3**81)*F(9,81*8))[1]
 return out[0],out[1]+tail
LN2=series(F(2))
@lru_cache(maxsize=None)
def log(q):
 q=F(q);assert q>0;e=0
 if q==1:return 0,0
 while q>=2:q/=2;e+=1
 while q<1:q*=2;e-=1
 if q==1:return iv(e)
 a=add(series(q),scale(LN2,e))
 vals=[F(x*S,y) for x in a for y in LN2]
 return min(vals).numerator//min(vals).denominator,-((-max(vals).numerator)//max(vals).denominator)
def sm(items):
 o=(0,0)
 for x in items:o=add(o,x)
 return o
def ent(p):return sm(scale(log(q),-q) for q in p if q)
def kl(p,q):return sm(scale(log(a/b),a) for a,b in zip(p,q) if a)
def encode(a):return [str(F(a[0],S)),str(F(a[1],S))]
def diag(a):return float(F(a[0]+a[1],2*S))
def law(tab):
 a=list(tab);step=1
 while step<len(a):
  for i in range(0,len(a),2*step):
   for j in range(step):u,v=a[i+j],a[i+j+step];a[i+j],a[i+j+step]=u+v,u-v
  step*=2
 return [F(x*x,len(tab)**2) for x in a]
def restrict(tab,i,y):return [tab[(t&((1<<i)-1))|(y<<i)|((t>>i)<<(i+1))] for t in range(len(tab)//2)]
def marg(p):return [sum(v for s,v in enumerate(p) if s>>i&1) for i in range((len(p)-1).bit_length())]
def prodlaw(d):return [math.prod(v if s>>j&1 else 1-v for j,v in enumerate(d)) for s in range(1<<len(d))]
def erase(p,i):return [p[s]+p[s|(1<<i)] for s in range(len(p)) if not s>>i&1]
def info(tab):
 p=law(tab);d=marg(p);H=ent(p);TC=sub(sm(ent([v,1-v]) for v in d),H)
 ck(sum(p)==1)
 for i,v in enumerate(d):ck(v==F(sum(tab[x]!=tab[x^(1<<i)] for x in range(len(tab))),len(tab)))
 return p,d,H,TC,sub(iv(4*sum(d)),H)
def step(tab,Q,coords,i):
 j=coords.index(i);P=law(tab);T=erase(P,j);QT=erase(Q,j)
 tabs=[restrict(tab,j,y) for y in [0,1]];ps=[law(t) for t in tabs]
 ck(T==[(a+b)/2 for a,b in zip(*ps)])
 k=[[ps[y][s]/(2*T[s]) if T[s] else F(1,2) for s in range(len(T))] for y in [0,1]]
 out=[sum(q*ky for q,ky in zip(QT,k[y])) for y in [0,1]]
 refs=[[q*ky/out[y] for q,ky in zip(QT,k[y])] for y in [0,1]]
 ck(sum(out)==1)
 for y in [0,1]:
  ck(sum(refs[y])==1)
  for s in range(len(T)):
   if ps[y][s]:
    # Exact likelihood factorization; no interval overlap used as equality proof.
    ck((ps[y][s]/2)/(QT[s]*k[y][s])==F(1,2)/out[y]*(ps[y][s]/refs[y][s]))
 for s in range(len(P)):
  if P[s]:
   small=(s&((1<<j)-1))|((s>>(j+1))<<j)
   ck(P[s]/Q[s]==T[small]/QT[small]*((P[s]/T[small])/(Q[s]/QT[small])))
 E=sub(kl(P,Q),kl(T,QT));O=kl([F(1,2)]*2,out)
 return [(tabs[y],refs[y],[c for c in coords if c!=i]) for y in [0,1]],E,O,sum(1 for q in T if not q)

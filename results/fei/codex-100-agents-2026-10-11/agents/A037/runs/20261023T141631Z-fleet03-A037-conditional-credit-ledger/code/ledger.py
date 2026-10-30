"""Exact full-tree ledger, including conditional node identities and deferred resets."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from math import lcm
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();C=0;nodes=resets=strict=0
def ck(x):
 global C
 C+=1;assert x,C;assert time.perf_counter()-start<55
@lru_cache(None)
def law(t):return tuple(F(sum(v*(-1)**((s&z).bit_count()%2) for z,v in enumerate(t))**2,len(t)**2) for s in range(len(t)))
def add(a,b,c=F(1)):
 r=a.copy()
 for p,v in b.items():r[p]=r.get(p,F(0))+c*v
 return {p:v for p,v in r.items() if v}
@lru_cache(None)
def factors(k):
 a={};d=2
 while d*d<=k:
  while k%d==0:a[d]=a.get(d,0)+1;k//=d
  d+=1
 if k>1:a[k]=a.get(k,0)+1
 return a
@lru_cache(None)
def logs(x):return add({p:F(v) for p,v in factors(x.numerator).items()},{p:F(v) for p,v in factors(x.denominator).items()},-1)
def KL(p,q):
 r={}
 for a,b in zip(p,q):
  if a:r=add(r,logs(a/b),a)
 return r
def sign(v):
 if not v:return 0
 d=lcm(*(x.denominator for x in v.values()));a=b=1
 for p,x in v.items():
  k=int(x*d)
  if k>0:a*=p**k
  else:b*=p**(-k)
 return (a>b)-(a<b)
alpha=F(1,6)
def profile(p,S):
 q=[(1-alpha)*x for x in p];q[0]+=alpha*p[0];q[S]+=alpha*(1-p[0]);return tuple(q)
def walk(t,q,S):
 global nodes,resets,strict
 p=law(t);A=KL(p,q)
 if len(t)==1:return {},{},A
 nodes+=1;kids=[tuple(t[z] for z in range(y,len(t),2)) for y in [0,1]];pcs=[law(c) for c in kids]
 pb=tuple(p[2*z]+p[2*z+1] for z in range(len(p)//2));qb=tuple(q[2*z]+q[2*z+1] for z in range(len(q)//2))
 E=add(A,KL(pb,qb),-1);out=[];olds=[]
 for pc in pcs:
  joint=tuple(b*x/(2*a) if a else F(0) for a,b,x in zip(pb,qb,pc));r=sum(joint);ck(r>0);out.append(r);olds.append(tuple(x/r for x in joint))
 O=KL((F(1,2),F(1,2)),out);ck(sign(E)>=0 and sign(O)>=0)
 T=S>>1;news=olds[:];sigma={}
 if S and p[S] and q==profile(p,S) and pcs[0]==pcs[1]:
  resets+=1
  news=[profile(pc,T) if T else pc for pc in pcs]
  for pc,old,new in zip(pcs,olds,news):sigma=add(sigma,add(KL(pc,new),KL(pc,old),-1),F(1,2))
  sg=sign(sigma);ck(sg<=0);strict+=sg<0
 local=add(E,O)
 for pc,new in zip(pcs,news):local=add(local,KL(pc,new),F(1,2))
 ck(local==add(A,sigma))
 credit=add({},sigma,-1);paid=add(E,O);terminal={}
 for tchild,new in zip(kids,news):
  cc,pp,aa=walk(tchild,new,T);credit=add(credit,cc,F(1,2));paid=add(paid,pp,F(1,2));terminal=add(terminal,aa,F(1,2))
 # Conditional no-double-spending identity at THIS reached node, not only root.
 ck(add(add(credit,paid),terminal)==A);ck(sign(credit)>=0);ck(sign(add(A,credit,-1))>=0)
 return credit,paid,terminal
trees=0
for n in range(1,4):
 for f in range(1<<(1<<n)):
  t=tuple(1-2*((f>>z)&1) for z in range(1<<n));p=law(t)
  for S in range(1,1<<n):
   if p[S]:walk(t,profile(p,S),S);trees+=1
out={'status':'PASS','functions':276,'trees':trees,'internal_nodes':nodes,'eligible_reset_nodes':resets,'strict_release_nodes':strict,'assertions':C,'seconds':time.perf_counter()-start,'arithmetic':'Exact prime-log vectors, rational complete physical kernels, integer sign certificates','all_conditional_node_identities_checked':True}
(R/'out/LEDGER.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))

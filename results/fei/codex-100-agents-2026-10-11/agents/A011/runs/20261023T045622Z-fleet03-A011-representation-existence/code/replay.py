import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
import time,json
import shared
RUN=Path(__file__).resolve().parents[1]; start=time.monotonic();checks=0
def ck(v):
 global checks
 checks+=1;assert v,checks
@lru_cache(maxsize=64)
def prob(v):
 N=len(v)
 return tuple(F(sum((-z if (x&T).bit_count()%2 else z) for x,z in enumerate(v)),N)**2 for T in range(N))
def cost(P,Q):
 weights=defaultdict(F)
 for p,q in zip(P,Q):
  if p:ck(q>0);weights[q]+=p
 lo=hi=F(0)
 for q,p in weights.items():a,b=shared.log(1/q);lo+=p*a;hi+=p*b
 return lo,hi
def Dhi(v,q):P=prob(v);return cost(P,q)[1]-cost(P,P)[0]
def old(sign,source,ref,pads,active):
 a=len(source).bit_length()-1;n=a+pads;N=2**n
 v=tuple(source[x%len(source)]-2*source[0]*(active and x==0) for x in range(2*N))
 if not active:return v,tuple(ref)+(F(0),)*(len(v)-len(ref))
 P=prob(v);beta=F(6,2*N);m=[P[y]+P[N+y] for y in range(N)]
 R=tuple((((ref[y] if y<len(ref) else 0)+beta/F(N))/(1+beta))*P[u*N+y]/m[y] for u in range(2) for y in range(N))
 ck(sum(R)==(sum(ref)+beta)/(1+beta));return v,R
def second(v,Q,pt):
 if pt is None:return tuple(v*4),tuple(Q)+(F(0),)*(3*len(Q))
 N=len(v);v2=tuple(v[y]-2*v[pt]*(u==0 and y==pt) for u in range(4) for y in range(N));P=prob(v2)
 t=F(1,N);beta=2*t;m=[sum(P[u*N+y] for u in range(4)) for y in range(N)]
 R=tuple((Q[y]+beta*t)/(1+beta)*P[u*N+y]/m[y] for u in range(4) for y in range(N))
 ck(sum(R)==(sum(Q)+beta)/(1+beta));return v2,R
def edge(v):
 n=len(v).bit_length()-1
 return F(2*sum(v[x]!=v[x+2**j] for x in range(len(v)) for j in range(n) if not (x>>j&1)),len(v))
roots=frontiers=0
for sign in [-1,1]:
 g=(sign,-sign);ref=(F(1,9),F(2,9));c=cost(prob(g),ref);C0=c[1];K=4*C0+15
 v1,Q1=old(sign,g,ref,6,True);I1=edge(v1);rho1=F(1,256);G1=2*rho1*7;U=min(C0+1,K*G1)
 for point in [0,2]:
  v2,Q2=second(v1,Q1,point);I2=edge(v2);rho2=F(1,1024);d1=sum(v1[point]!=v1[point^(1<<j)] for j in range(8));G2=2*rho2*(10-d1)
  ck(I2==I1+G2-2*rho2*d1);Hroot=cost(prob(v2),prob(v2));off=F(0);pt=point;src=g;model=ref
  for depth in range(1,8):
   pads=max(6-depth,0);idx=1 if depth<=6 else 0
   if depth==7:src=(g[0],);model=(sum(ref),);other=(g[1],);othermodel=model
   else:other=src;othermodel=model
   def without(x):return x%2**idx+(x//2**(idx+1))*2**idx
   ap=None if pt is None or pt>>idx&1 else without(pt);op=without(pt) if pt is not None and pt>>idx&1 else None
   va,qa=old(sign,src,model,pads,True);vo,qo=old(sign,other,othermodel,pads,False)
   aa,aq=second(va,qa,ap);oo,oq=second(vo,qo,op)
   lam=F(1,2**depth);off+=lam*Dhi(oo,oq);Lhi=Hroot[1]+off+lam*Dhi(aa,aq)
   ck(K*I2-Lhi-U>=(F(11,32)*C0+F(135,16))+K*(G1+G2));frontiers+=1
   pt=ap
   if time.monotonic()-start>55:raise RuntimeError('frozen55second cutoff')
  roots+=1
# Guard the boundary premise: constant original source has Ig=0 but positive H(F2).
g=(1,1);v1,Q1=old(1,g,(F(1),F(0)),6,True);v2,Q2=second(v1,Q1,0)
ck(edge(g)==0);ck(cost(prob(v2),prob(v2))[0]>0)
out={'status':'PASS','roots':roots,'frontiers':frontiers,'constant_source_exclusion':1,'assertions':checks,'seconds':time.monotonic()-start,'independence':'direct character sums, independent models and edge enumeration; imports only pinned logarithm primitive, not primary checker'}
(RUN/'out/REPLAY_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))

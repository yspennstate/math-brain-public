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
roots=cuts=0
def verify(seed,edits):
 global roots,cuts
 f=seed.copy();R=len(edits);N=len(f);n=(N-1).bit_length();p=Q(1,N)
 for x in edits:f[x]=-f[x]
 w=direct(seed);s=[i for i,v in enumerate(w) if v]
 ck(all((x^y).bit_count()>=3 for x,y in combinations(s,2)))
 ck(len(s)*(n+1)<=N)
 h=ent(f)
 for i in range(n):
  ch=[restrict(f,i,b) for b in (0,1)]
  a,b=map(ent,ch);Lupper=h[1]-(a[0]+b[0])/2
  ck(Lupper<(10*R+Q(17,2)*R*R)*p)
  I=directional(f,1<<i)
  if I:ck(Lupper<(5*R+Q(17,4)*R*R)*I)
  ck(inf(f)==I+(inf(ch[0])+inf(ch[1]))/2)
  cuts+=1
 roots+=1
for s in range(8):
 for sign in (-1,1):
  seed=[sign*(-1 if (x&s).bit_count()%2 else 1) for x in range(8)]
  for R in (1,2,3):
   for E in combinations(range(8),R):verify(seed,E)
seed=[]
for x in range(64):
 y0=(x&7).bit_count()%2;y1=((x>>3)&7).bit_count()%2
 seed.append(-1 if y0==y1==0 else 1)
for E in [(0,),(0,1),(0,7),(0,63),(0,1,2),(0,1,7),(0,1,2,3),(0,7,56,63)]:
 verify(seed,E)
guards=[]
for k in (2,3):
 n=k+4;N=1<<n;p=Q(1,1<<k);f=[]
 for x in range(N):
  a,b,c,z=[(x>>i)&1 for i in range(4)]
  active=(x>>4)==0
  f.append(-1 if active and (a*b+a*c+b*c+z*a)%2 else 1)
 fp=[f[y^(((y&1))<<4)] for y in range(N)]
 ck(ent(f)==ent(fp))
 I=inf(f);Ip=inf(fp);ck(Ip-I==p/4)
 old=[];new=[]
 for u in range(4):
  g=[f[(x<<2)|u] for x in range(N//4)]
  gp=[fp[(x<<2)|u] for x in range(N//4)]
  ck(Counter(v*v for v in direct(g))==Counter(v*v for v in direct(gp)))
  old.append(affine_min(g));new.append(affine_min(gp))
 ck(old==new)
 originalQ=directional(f,1)+directional(f,2)
 newQ=directional(fp,1)+directional(fp,2)
 rho=I-originalQ-sum(old)/4
 rhop=Ip-newQ-sum(new)/4
 ck(originalQ==p);ck(rho==p/4);ck(rhop==p/4)
 ck(newQ+rhop-(Ip-I)==originalQ+rho)
 guards.append({'k':k,'Delta':str(Ip-I),'original_query_plus_release':str(originalQ+rho),'apparent_new':str(newQ+rhop),'compensated':str(newQ+rhop-(Ip-I))})
out={'status':'PASS','assertions':checks,'roots':roots,'coordinate_cuts':cuts,'A052_actual_guards':guards,'runtime_seconds':time.perf_counter()-start,'method':'independent direct character sums, physical directional edges, own atanh32 rational intervals and greedy directional minima; no imported main helpers'}
(RUNDIR/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

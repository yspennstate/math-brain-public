import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
import json,time
import shared
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=zero=0
def ck(v):
 global checks
 checks+=1;assert v,checks
def walsh(v):
 a=list(v);step=1
 while step<len(a):
  for base in range(0,len(a),2*step):
   for x in range(base,base+step):a[x],a[x+step]=a[x]+a[x+step],a[x]-a[x+step]
  step*=2
 return [F(x,len(a)) for x in a]
def ps(v):return [x*x for x in walsh(v)]
def source_children(g,Q,idx):
 N=len(g)//2
 def insert(x,b):return x%(1<<idx)+b*(1<<idx)+(x//(1<<idx))*(1<<(idx+1))
 gs=[[g[insert(x,b)] for x in range(N)] for b in (0,1)];P=ps(g);kids=[ps(h) for h in gs];s=sum(Q);raw=[[],[]]
 for T in range(N):
  p=P[insert(T,0)]+P[insert(T,1)];q=Q[insert(T,0)]+Q[insert(T,1)]
  for bit in (0,1):raw[bit].append(q*kids[bit][T]/p if p else q)
 Z=[sum(x) for x in raw];ck(sum(Z)==2*s);return gs,[[s*x/Z[b] for x in raw[b]] for b in (0,1)]
def complete(P,Q):
 agg=defaultdict(F)
 for p,q in zip(P,Q):
  if p:ck(q>0);agg[q]+=p
 lo=hi=F(0)
 for q,p in agg.items():a,b=shared.log(1/q);lo+=p*a;hi+=p*b
 return lo,hi
def restrict(v,coords,fixed):
 free=[i for i in coords if i not in fixed];base=sum(bit<<i for i,bit in fixed.items());out=[]
 for x in range(2**len(free)):
  orig=base|sum(((x>>k)&1)<<i for k,i in enumerate(free));out.append(v[orig])
 return out,free
gold=json.loads((R/'out/GOLD.json').read_text(encoding='utf-8'));nodes=frontiers=atomcomparisons=0
for fixture in gold:
 a,b,M=fixture['a'],fixture['b'],fixture['M'];N=a+b+M;g=[1 if fixture['label']>>x&1 else -1 for x in range(2**a)];Q=[F(i+1,3*sum(range(1,len(g)+1))) for i in range(len(g))];globaltruth=[];old=[g[x%len(g)] for x in range(2**(a+b))]
 globaltruth.append(old*(2**M))
 for j,z in enumerate(fixture['points'],1):
  old=old*2;old[z]=-old[z];globaltruth.append(old*(2**(M-j)))
 rootIg=F(sum(g[x]!=g[x^(1<<i)] for x in range(len(g)) for i in range(a)),len(g));sourcecost=complete(ps(g),Q);C0=sourcecost[1]/rootIg;K=4*C0+15;U=(C0+F(37,8))*rootIg;Pfull=ps(globaltruth[-1]);I=sum(S.bit_count()*p for S,p in enumerate(Pfull));cmap={};Hroot=None
 for node in fixture['nodes']:
  fixed={int(i):bit for i,bit in node['fixed'].items()};sg=g[:];sq=Q[:];remaining=list(range(a))
  for coord,bit in node['path']:
   if coord<a:
    gs,qs=source_children(sg,sq,remaining.index(coord));sg,sq=gs[bit],qs[bit];remaining.remove(coord)
  ck(sg==node['g']);ck(sq==[F(x) for x in node['Q']]);truth,free=restrict(globaltruth[0],list(range(N)),fixed);ref=sq+[F(0)]*(len(truth)-len(sq))
  for j,z in enumerate(fixture['points'],1):
   D=a+b+j;oldD=D-1;truth,free=restrict(globaltruth[j],list(range(N)),fixed);P=ps(truth);oldfree=[i for i in free if i<oldD];newfree=[i for i in free if oldD<=i<D];n=len(oldfree);r=len(newfree);oldsize=2**n;newsize=2**r;hit=all(bit==((z>>i)&1 if i<oldD else 0) for i,bit in fixed.items() if i<D)
   if hit:
    rho=F(1,oldsize*newsize);beta=(6 if j==1 else 8 if j==2 else 4*(1+4*j*(j+1)))*rho;out=[]
    for u in range(newsize):
     for T in range(oldsize):
      marginal=sum(P[v*oldsize+T] for v in range(newsize));floor=(ref[T]+beta/F(oldsize))/(1+beta)
      if marginal:q=floor*P[u*oldsize+T]/marginal
      else:ck(r==0);q=floor;zero+=1
      out.append(q)
    expected=(sum(ref)+beta)/(1+beta);ref=out+[F(0)]*(len(P)-len(out));ck(sum(ref)==expected)
   # On a miss the original full frequency vector already embeds zero new frequencies.
   ck(sum(P)==1);ck(0<sum(ref)<=1)
  records={S:(m,F(p),F(q)) for S,m,p,q in node['records']};unused=node['unused'];mask=sum(1<<i for i in unused);counts=Counter()
  for T,(p,q) in enumerate(zip(P,ref)):
   S=sum(((T>>k)&1)<<i for k,i in enumerate(free));rep=S&~mask
   if S&mask:rep|=1<<unused[0]
   m,pp,qq=records[rep];ck(p==pp);ck(q==qq);counts[rep]+=1;atomcomparisons+=1
  for S,(m,p,q) in records.items():ck(counts[S]==m)
  ce=complete(P,ref);hh=complete(P,P);dd=(ce[0]-hh[1],ce[1]-hh[0]);key=tuple(tuple(x) for x in node['path']);cmap[key]=(ce,hh,dd)
  if not key:Hroot=hh
  nodes+=1
  if time.monotonic()-start>300:raise RuntimeError('frozen replay deadline')
 # Replay all stored physical frontiers from independent full node distributions.
 leaves=[()]
 for node in fixture['nodes']:
  key=tuple(tuple(x) for x in node['path']);children=[k for k in cmap if len(k)==len(key)+1 and k[:-1]==key]
  if not children:continue
  ck(key in leaves);leaves.remove(key);leaves+=children;Dhi=sum(F(1,2**len(k))*cmap[k][2][1] for k in leaves);ck(K*I-Hroot[1]-Dhi-U>0);frontiers+=1
out={'status':'PASS','sequences':len(gold),'literal_nodes':nodes,'literal_atom_comparisons':atomcomparisons,'frontiers':frontiers,'zero_data_fibers_retained':zero,'max_literal_dimension':16,'exact_assertions':checks,'seconds':time.monotonic()-start,'independence':'Literal global Boolean tables and independent restriction, physical source inheritance and model recursion; primary checker not imported; only certified logarithm primitive shared'}
(R/'out/REPLAY.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='');print(json.dumps(out))

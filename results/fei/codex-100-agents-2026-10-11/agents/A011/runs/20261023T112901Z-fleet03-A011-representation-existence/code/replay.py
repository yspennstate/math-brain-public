import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
import json,time
import shared
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(v):
 global checks
 checks+=1;assert v,checks
def transform(v):
 a=list(v);N=len(a);d=1
 while d<N:
  for base in range(0,N,2*d):
   for x in range(base,base+d):a[x],a[x+d]=a[x]+a[x+d],a[x]-a[x+d]
  d*=2
 return [F(x,N) for x in a]
def prob(v):return [z*z for z in transform(v)]
def CE(P,Q):
 agg=defaultdict(F)
 for p,q in zip(P,Q):
  if p:ck(q>0);agg[q]+=p
 lo=hi=F(0)
 for q,p in agg.items():a,b=shared.log(1/q);lo+=p*a;hi+=p*b
 return lo,hi
def physicalI(v):
 n=len(v).bit_length()-1
 return F(2*sum(v[x]!=v[x+2**i] for i in range(n) for x in range(len(v)) if x>>i&1==0),len(v))
def children(g,Q,idx):
 N=len(g)//2
 def ins(x,b):return x%(2**idx)+b*2**idx+(x//2**idx)*2**(idx+1)
 gs=[[g[ins(x,b)] for x in range(N)] for b in [0,1]];Ps=[prob(z) for z in gs];Pg=prob(g)
 marg=[Pg[ins(x,0)]+Pg[ins(x,1)] for x in range(N)];rr=[Q[ins(x,0)]+Q[ins(x,1)] for x in range(N)];s=sum(Q)
 raw=[[rr[x]*Ps[b][x]/marg[x] if marg[x] else rr[x] for x in range(N)] for b in [0,1]];Z=[sum(x) for x in raw];ck(sum(Z)==2*s)
 qs=[[s*z/Z[b] for z in raw[b]] for b in [0,1]];ck(all(sum(q)==s for q in qs));return gs,qs
def restriction_source(fixture,model):
 a=fixture['a'];g=[1 if fixture['label']>>x&1 else -1 for x in range(2**a)];Q=[F(x+1,3*sum(range(1,len(g)+1))) for x in range(len(g))];remaining=list(range(a))
 for orig,bit in sorted((int(i),v) for i,v in model['fixed'].items() if int(i)<a):
  idx=remaining.index(orig);gs,qs=children(g,Q,idx);g,Q=gs[bit],qs[bit];remaining.remove(orig)
 ck(g==model['g']);ck(Q==[F(x) for x in model['R']]);return g,Q
def literal_model(fixture,model):
 a,b=fixture['a'],fixture['b'];jmax=model['j'];g,Q=restriction_source(fixture,model);src=model['src'];pads=model['pads'];fixed={int(i):v for i,v in model['fixed'].items()}
 n0=len(src)+len(pads);v=[g[x%len(g)] for x in range(2**n0)];ref=Q+[F(0)]*(len(v)-len(Q))
 for j,point in enumerate(fixture['points'][:jmax],1):
  hit=all((point>>i&1)==bit for i,bit in fixed.items());remaining=src+pads+list(range(a+b,a+b+j-1));local=sum((point>>orig&1)<<k for k,orig in enumerate(remaining));N=len(v)
  old=v;v=old*2
  if hit:
   v[local]=-v[local];P=prob(v);marg=[P[T]+P[N+T] for T in range(N)];rho=F(1,2*N);beta=(6 if j==1 else 8 if j==2 else 4*(1+4*j*(j+1)))*rho
   ref=[(ref[T]+beta/F(N))/(1+beta)*P[u*N+T]/marg[T] for u in range(2) for T in range(N)]
  else:ref=ref+[F(0)]*N
 P=prob(v);records={S:(m,F(p),F(q)) for S,m,p,q in model['records']};unused=model['unused_local'];mask=sum(1<<i for i in unused);counts=Counter()
 for S,(p,q) in enumerate(zip(P,ref)):
  representative=S&~mask
  if S&mask:representative|=1<<unused[0]
  multiplicity,expectedP,expectedQ=records[representative];ck(p==expectedP);ck(q==expectedQ);counts[representative]+=1
 for S,(m,p,q) in records.items():ck(counts[S]==m)
 ck(sum(P)==1);ck(0<sum(ref)<=1)
 c=CE(P,ref);h=CE(P,P);return c,h,(c[0]-h[1],c[1]-h[0]),v
gold=json.loads((R/'out/GOLD.json').read_text(encoding='utf-8'));nodes=frontiers=0
for fixture in gold:
 a=fixture['a'];g=[1 if fixture['label']>>x&1 else -1 for x in range(2**a)];Q=[F(x+1,3*sum(range(1,len(g)+1))) for x in range(len(g))];Ig=physicalI(g);c=CE(prob(g),Q);C0=c[1]/Ig;K=4*C0+15;U=(C0+F(37,8))*Ig
 byname={x['node']:x for x in fixture['models'] if x['j']==fixture['M']};rootmodel=byname['root'];rootcost,H,rootD,truth=literal_model(fixture,rootmodel);I=physicalI(truth)
 # Literal edge degree of each pre-edit table verifies the actual physical bank.
 original=[g[x%len(g)] for x in range(2**(a+fixture['b']))];current=original;Gsum=Esum=F(0)
 for j,p in enumerate(fixture['points'],1):
  n=len(current).bit_length()-1;d=sum(current[p]!=current[p^(1<<i)] for i in range(n));rho=F(1,2*len(current));Gsum+=2*rho*(n+1-d);Esum+=2*rho*d;current=current*2;current[p]=-current[p]
 ck(current==truth);ck(I==Ig+Gsum-Esum);ck(K*I-rootcost[1]-U>=(F(241,1024)*C0+F(54191,8192))*Ig+K*Gsum);nodes+=1
 off=F(0)
 for depth in range(1,a+fixture['b']+1):
  ca,ha,da,va=literal_model(fixture,byname['active'+str(depth)]);co,ho,do,vo=literal_model(fixture,byname['other'+str(depth)]);lam=F(1,2**depth);off+=lam*do[1];Lhi=H[1]+off+lam*da[1]
  ck(K*I-Lhi-U>=(F(241,1024)*C0+F(54191,8192))*Ig+K*Gsum);frontiers+=1;nodes+=2
  if time.monotonic()-start>300:raise RuntimeError('amended300second cutoff')
# An actual Boolean guard against universal positive-floor fixed-dimension admission.
for N in range(2,9):
 source=[1 if x&1 else -1 for x in range(2**N)];target=[-1 if x.bit_count()%2 else 1 for x in range(2**N)];M=sum(s!=t for s,t in zip(source,target));ck(M==2**(N-1));P=prob(target);ck(sum(p!=0 for p in P)==1);ck(P[-1]==1);ck(physicalI(source)==1)
out={'status':'PASS','sequences':len(gold),'literal_models_compared_atomwise':nodes,'maximum_M_frontiers':frontiers,'max_literal_dimension':16,'parity_guards':7,'exact_assertions':checks,'seconds':time.monotonic()-start,'independence':'Own literal tables, original-source physical inheritance, fresh-floor models, integer transform and literal edges; primary checker not imported; shares only pinned rigorous logarithm primitive'}
(R/'out/REPLAY_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='');print(json.dumps(out))

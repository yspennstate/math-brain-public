from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
R=Path(__file__).resolve().parents[1];T0=time.perf_counter();C=0
def ck(x):
 global C
 assert x,C;C+=1
def fw(v):
 a=list(v);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def ch(s,t):return 1-2*((s&t).bit_count()%2)
def sp(v):return [F(x*x,len(v)**2) for x in fw(v)]
@lru_cache(maxsize=12000)
def fac(n):
 out=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:out.append((p,e))
  p+=1
 if n>1:out.append((n,1))
 return tuple(out)
def addlog(a,w,x):
 if not w:return
 for sign,n in ((1,x.numerator),(-1,x.denominator)):
  for p,e in fac(n):a[p]=a.get(p,F(0))+sign*e*w
def clean(a):return {p:x for p,x in a.items() if x}
def lin(*terms):
 a={}
 for w,b in terms:
  for p,x in b.items():a[p]=a.get(p,F(0))+w*x
 return clean(a)
def ent(v):
 a={}
 for x in v:
  if x:addlog(a,-x,x)
 return clean(a)
def kl(p,q):
 a={}
 for x,y in zip(p,q):
  if x:ck(y>0);addlog(a,x,x/y)
 return clean(a)
def phi(a,b):
 z={}
 if a:addlog(z,a,(a+b)/a)
 if b:addlog(z,b,(a+b)/b)
 return clean(z)
@lru_cache(maxsize=4000)
def ln(p):
 k=p.bit_length()-1;r=F(p,1<<k)
 def series(x):
  z=(x-1)/(x+1);N=18
  low=sum(2*z**(2*j+1)/F(2*j+1) for j in range(N));tail=2*z**(2*N+1)/F(2*N+1)/(1-z*z)
  return low,low+tail
 lo,hi=series(r);l2,h2=series(F(2));return lo+k*l2,hi+k*h2
def lower(sig,constant=F(0)):
 ans=constant
 for p,x in sig.items():
  lo,hi=ln(p);ans+=x*(lo if x>=0 else hi)
 return ans
def infl(v):
 return F(sum(v[s]!=v[s^(1<<j)] for s in range(len(v)) for j in range((len(v)-1).bit_length())),len(v))
def policies(y,p):
 if p==0:return (1 if y==0 else 0),(2 if y==0 else 0)
 if p==1:return (1 if y==0 else 0),(1 if y==1 else 0)
 if p==2:return y&3,(3*y+1)&3
 return (y^(y>>1))&3,(y+2*(y>>1)+1)&3
def Bsig(u,v):
 n=len(u);a=[x/n for x in fw(u)];b=[x/n for x in fw(v)]
 rho=2-sum(x*x for x in a+b);out={2:rho/2}
 for x,y in zip(a,b):out=lin((1,out),(1,phi(((x+y)/2)**2,((x-y)/2)**2)))
 return clean(out),rho,a,b
def case(phase,t,L,shift,policy):
 n=1<<t;labels=[sum(((s&m).bit_count()%2)<<j for j,m in enumerate(L)) for s in range(n)]
 c=[ch(s,shift)*(1-2*((phase>>labels[s])&1)) for s in range(n)]
 ev=[policies(y,policy) for y in labels]
 g=[c[s]*(1-2*((ev[s][0]>>u)&1)) for u in range(2) for s in range(n)]
 h=[c[s]*(1-2*((ev[s][1]>>v)&1)) for v in range(2) for s in range(n)]
 u=[F(g[s]+g[n+s],2) for s in range(n)];v=[F(h[s]+h[n+s],2) for s in range(n)]
 G=[g[s+n*i] for j in range(2) for i in range(2) for s in range(n)]
 H=[h[s+n*j] for j in range(2) for i in range(2) for s in range(n)];parent=G+H
 pg=sp(g);ph=sp(h);pf=sp(parent);ig=infl(g);ih=infl(h);ip=infl(parent)
 rg=sum(pg[n:]);rh=sum(ph[n:]);ck(rg>0 and rh>0)
 d=F(sum(x!=y for x,y in zip(G,H)),4*n);ds=min(d,1-d)
 ck(ip==(ig+ih)/2+d);ck(d==(1-sum(x*y for x,y in zip(u,v))/n)/2)
 ck(rg==1-sum(x*x for x in u)/n);ck(rh==1-sum(x*x for x in v)/n)
 ck(rg==F(sum(g[s]!=g[s+n] for s in range(n)),n));ck(rh==F(sum(h[s]!=h[s+n] for s in range(n)),n))
 mix=[pf[i]+pf[i+4*n] for i in range(4*n)];B=lin((1,ent(pf)),(-1,ent(mix)))
 formula,rho,a,b=Bsig(u,v);ck(B==formula);ck(rho==rg+rh)
 u0=[sum(u[s]*ch(s,shift) for s in range(n) if labels[s]==y)/F(n,8) for y in range(8)]
 v0=[sum(v[s]*ch(s,shift) for s in range(n) if labels[s]==y)/F(n,8) for y in range(8)]
 quotient,rr,_,_=Bsig(u0,v0);ck(quotient==B);ck(rr==rho)
 ck(lower(lin((1,{2:4*ds}),(-1,B)),rho)>=0)
 delta=lin((1,ent(pf)),(-F(1,2),ent(pg)),(-F(1,2),ent(ph)))
 ck(lower(lin((1,{2:4*ds}),(-1,delta)),2*ds+rho)>=0)
 RG=pg[:n]+[F(15,16)*x+rg/F(16*n) for x in pg[n:]]
 RH=ph[:n]+[F(15,16)*x+rh/F(16*n) for x in ph[n:]]
 Q=[]
 for z in range(2):
  for k in range(4*n):Q.append(pf[z*4*n+k] if k<n else RG[k]/4 if k<2*n else RH[k-n]/4 if k<3*n else F(0))
 ck(sum(Q)==1 and sum(RG)==1 and sum(RH)==1)
 dg=kl(pg,RG);dh=kl(ph,RH);df=kl(pf,Q);ck(df==lin((F(1,2),dg),(F(1,2),dh)))
 ceg=lin((1,ent(pg)),(1,dg));ceh=lin((1,ent(ph)),(1,dh));cep=lin((1,ent(pf)),(1,df))
 ck(lower(lin((1,{2:4*ig}),(-1,ceg)))>=0);ck(lower(lin((1,{2:4*ih}),(-1,ceh)))>=0)
 # ln2 times K I_parent - CE_parent - old averaged shared debit.
 shared=ig+ih-rho
 gap=lower(lin((1,{2:4*ip}),(-1,cep)),2*ip-shared);ck(gap>=0)
 # EXACT variance conversion and both-old-debit ownership, in natural units.
 oldG=2*(ig-rg);oldH=2*(ih-rh);debit=rho
 initial=2*(ig+ih)-oldG-oldH
 ck(initial/2==debit);ck((oldG+oldH)/2==shared)
 if policy==0:ck(B=={2:rho/2});ck(delta=={2:rho})
 return gap,len(parent)
mode=sys.argv[1];cnt=0;min_gap=None;maxn=0
jobs=((p,3,[1,2,4],0,q) for p in range(256) for q in range(4)) if mode=='base' else ((p,t,L,s,q) for p in [0,1,3,7,16,17,19,23] for t,L in [(4,[3,6,12]),(5,[7,14,28]),(6,[15,22,45])] for s in [0,1] for q in [0,1])
for args in jobs:
 gap,n=case(*args);cnt+=1;maxn=max(maxn,n);min_gap=gap if min_gap is None else min(min_gap,gap);ck(time.perf_counter()-T0<55)
out={'status':'PASS','mode':mode,'cases':cnt,'assertions':C,'largest_parent_truth_table':maxn,'minimum_certified_parent_gap_nats':str(min_gap),'seconds':time.perf_counter()-T0,'both_private':True,'old_shared_debit':'(I_shared(G)+I_shared(H))/ln2 preserved','reference':'15/16 true whole private law plus1/16 uniform, both full KL retained'}
(R/'out'/('FIXTURES_'+mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))

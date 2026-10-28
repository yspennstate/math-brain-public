import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json,time,hashlib
import shared
RUN=Path(__file__).resolve().parents[1]; start=time.monotonic(); checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def scale(x,s):return x[0]*s,x[1]*s
@lru_cache(maxsize=256)
def spectrum(v):
 a=list(v);N=len(a);d=1
 while d<N:
  for i in range(0,N,2*d):
   for j in range(i,i+d):a[j],a[j+d]=a[j]+a[j+d],a[j]-a[j+d]
  d*=2
 return tuple(F(z*z,N*N) for z in a)
def ce(P,Q):
 agg=defaultdict(F)
 for p,q in zip(P,Q):
  if p: ck(q>0);agg[q]+=p
 lo=hi=F(0)
 for q,p in agg.items():a,b=shared.log(1/q);lo+=p*a;hi+=p*b
 return lo,hi
def ent(P):return ce(P,P)
def debt(P,Q):return sub(ce(P,Q),ent(P))
def influence(v):
 n=len(v).bit_length()-1
 return F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v)) for j in range(n)),len(v))
def split_index(x,j,bit):return (x%2**j)+bit*2**j+(x//2**j)*2**(j+1)
def remove(x,j):return (x%2**j)+(x//2**(j+1))*2**j
def source_split(g,Q):
 gs=[tuple(g[2*x+b] for x in range(len(g)//2)) for b in [0,1]]
 Ps=[spectrum(x) for x in gs];P=spectrum(g);s=sum(Q)
 m=[P[2*x]+P[2*x+1] for x in range(len(g)//2)]
 marg=[Q[2*x]+Q[2*x+1] for x in range(len(g)//2)]
 raw=[[marg[x]*Ps[b][x]/m[x] if m[x] else marg[x] for x in range(len(m))] for b in [0,1]]
 Z=[sum(z) for z in raw];ck(sum(Z)==2*s);refs=[tuple(s*z/Z[b] for z in raw[b]) for b in [0,1]]
 for q in refs:ck(sum(q)==s)
 return gs,refs
def point(v,Q,r,point,factor):
 N=len(v);rho=F(1,N*2**r);beta=factor*rho
 vv=tuple(v[y]-2*v[point]*(u==0 and y==point) for u in range(2**r) for y in range(N))
 P=spectrum(vv);q=[sum(P[u*N+y] for u in range(2**r)) for y in range(N)]
 qq=[(Q[y]+beta/F(N))/(1+beta) for y in range(N)]
 ck(all(z>0 for z in q));R=tuple(qq[y]*P[u*N+y]/q[y] for u in range(2**r) for y in range(N))
 ck(sum(R)==(sum(Q)+beta)/(1+beta));ck(sum(P)==1)
 return vv,R
def old(g,Q,b,r,edited):
 v=tuple(g[x%len(g)] for x in range(len(g)*2**(b+r)))
 q=tuple(Q[x] if x<len(Q) else F(0) for x in range(len(v)))
 if not edited:return v,q
 data=tuple(g[x%len(g)] for x in range(len(g)*2**b));ref=tuple(Q[x] if x<len(Q) else F(0) for x in range(len(data)))
 return point(data,ref,r,0,F(6))
def new_model(v,Q,r,pt):
 if pt is not None:return point(v,Q,r,pt,F(8))
 return tuple(v*2**r),tuple(Q)+(F(0),)*(len(Q)*(2**r-1))
def run_root(a,label,mode,kind,b=6,r1=1,r2=1):
 g=tuple(1 if label>>x&1 else -1 for x in range(2**a));P=spectrum(g);Ig=influence(g)
 Q=P if mode==0 else tuple(z/2 for z in P) if mode==1 else tuple(F(x+1,3*sum(range(1,2**a+1))) for x in range(2**a))
 c=ce(P,Q);C0=c[1]/Ig;K=4*C0+15;D1=a+b+r1;D2=D1+r2;rho1=F(1,2**D1);rho2=F(1,2**D2)
 pts=[0,2**(a+b),2**a-1,2**a,2**(a+b-1)+2**(a+b)]
 pt=pts[kind];v1,q1=old(g,Q,b,r1,True);v2,q2=new_model(v1,q1,r2,pt);I1=influence(v1);I2=influence(v2)
 d=sum(g[0]!=g[1<<j] for j in range(a));d1=sum(v1[pt]!=v1[pt^(1<<j)] for j in range(D1))
 G1=2*rho1*(D1-d);E1=2*rho1*d;G2=2*rho2*(D2-d1);E2=2*rho2*d1
 ck(I1==Ig+G1-E1);ck(I2==Ig+G1+G2-E1-E2)
 U=min((C0+1)*Ig,K*G1);H1=ent(spectrum(v1));H2=ent(spectrum(v2));oldoff=(F(0),F(0));newoff=(F(0),F(0))
 Dparent=debt(spectrum(v2),q2);signed=ce(spectrum(v2),q2);rootcost=signed
 margin=(F(19,32)*C0+F(75,8))*Ig+K*(G1+G2)
 ck(K*I2-rootcost[1]>=margin);ck(K*I2-rootcost[1]-U>0)
 ck(H2[1]<=F(3,2)*ent(P)[1]+60*rho1*D1+60*rho2*D2)
 currg=g;currQ=Q;remainb=b;currentpt=pt;frontiers=0;positive_resets=0;negative_resets=0
 for depth in range(1,b+a+1):
  if remainb:
   idx=len(currg).bit_length()-1;remainb-=1;otherg=currg;otherQ=currQ
  else:
   idx=0;gs,refs=source_split(currg,currQ);currg,otherg=gs;currQ,otherQ=refs
  otherpt=None;activept=None
  if currentpt is not None:
   if currentpt>>idx&1:otherpt=remove(currentpt,idx)
   else:activept=remove(currentpt,idx)
  va,qa=old(currg,currQ,remainb,r1,True);vo,qo=old(otherg,otherQ,remainb,r1,False)
  na,nqa=new_model(va,qa,r2,activept);no,nqo=new_model(vo,qo,r2,otherpt)
  # Direct physical children of CURRENT F2 Boolean truth table.
  ck(all(na[x]==v2[split_index(x,idx,0)] for x in range(len(na))))
  ck(all(no[x]==v2[split_index(x,idx,1)] for x in range(len(no))))
  lam=F(1,2**depth);Da=debt(spectrum(na),nqa);Do=debt(spectrum(no),nqo)
  reset=sub(scale(add(Da,Do),F(1,2)),Dparent)
  if reset[0]>0:positive_resets+=1
  if reset[1]<0:negative_resets+=1
  signed=add(signed,scale(reset,2*lam))
  oldoff=add(oldoff,scale(debt(spectrum(vo),qo),lam));newoff=add(newoff,scale(Do,lam))
  L1=add(H1,add(oldoff,scale(debt(spectrum(va),qa),lam)))
  L2=add(H2,add(newoff,scale(Da,lam)))
  ck(K*I1-L1[1]-U>=0)
  ck(L2[1]<=F(13,4)*c[1]+105*rho1*D1+100*rho2*D2)
  ck(K*I2-L2[1]>=margin)
  ck(K*I2-L2[1]-U>=(F(11,32)*C0+F(135,16))*Ig+K*(G1+G2))
  ck(max(signed[0],L2[0])<=min(signed[1],L2[1]))
  # Old bill is retained; the true operation debit is L2-L1, not a KL-only charge.
  delta=sub(L2,L1);prev=(K*I1-L1[1]-U,K*I1-L1[0]-U)
  carry=add(prev,(K*(I2-I1)-delta[1],K*(I2-I1)-delta[0]));new=(K*I2-L2[1]-U,K*I2-L2[0]-U)
  ck(max(carry[0],new[0])<=min(carry[1],new[1]));ck(carry[0]>0)
  v2=na;Dparent=Da;currentpt=activept;frontiers+=1
  if time.monotonic()-start>55:raise RuntimeError('frozen55second cutoff')
 return frontiers,positive_resets,negative_resets

if __name__=='__main__':
 mode=sys.argv[1];roots=frontiers=pos=neg=0
 if mode=='grid':
  for a in range(1,17):
   for b in range(6,17):
    for r in range(1,13):
     for s in range(1,13):
      q=b+r;d1=a+q;d2=d1+s;x=F(d1,a*2**(q+1));y=F(d2,a*2**(q+s+1))
      ck(x<=F(1,32));ck(y<=F(9,512));ck(F(1,2**q)+F(d1,a*2**(q+s))<=F(5,128));ck(2*x<=F(1,16));ck(105*x+100*y<=F(645,128));roots+=1
 else:
  fixtures=[(1,1),(1,2)]+[(2,l) for l in range(1,15)]+[(3,l) for l in [1,23,105,126]]
  fixtures=[(1,1)] if mode=='pilot' else fixtures[int(mode)*5:(int(mode)+1)*5]
  for a,label in fixtures:
   for model in range(3):
    for kind in range(5):
     f,p,n=run_root(a,label,model,kind);roots+=1;frontiers+=f;pos+=p;neg+=n
 out={'status':'PASS','mode':mode,'roots_or_grid_tuples':roots,'frontiers':frontiers,'positive_signed_resets':pos,'negative_signed_resets':neg,'exact_assertions':checks,'seconds':time.monotonic()-start,'helper_sha256':hashlib.sha256(Path(shared.__file__).read_bytes()).hexdigest()}
 (RUN/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))

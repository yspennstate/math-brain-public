import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json,time,hashlib
import shared
RUN=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
limit_seconds=300 if len(sys.argv)>1 and sys.argv[1] in ['0','1','2','3','4','5'] else 55
def ck(v):
 global checks
 checks+=1;assert v,checks
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def mul(x,s):return x[0]*s,x[1]*s
def fw(v):
 a=list(v);d=1
 while d<len(a):
  for z in range(0,len(a),2*d):
   for i in range(z,z+d):a[i],a[i+d]=a[i]+a[i+d],a[i]-a[i+d]
  d*=2
 return tuple(F(z,len(a)) for z in a)
def cost_rows(rows,entropy=False):
 agg=defaultdict(F)
 for S,mult,p,q in rows:
  if p:ck(q>0);agg[p if entropy else q]+=mult*p
 lo=hi=F(0)
 for q,p in agg.items():a,b=shared.log(1/q);lo+=p*a;hi+=p*b
 return lo,hi
def Itruth(g):return F(sum(g[x]!=g[x^(1<<j)] for x in range(len(g)) for j in range(len(g).bit_length()-1)),len(g))
def source_split(g,Q):
 P=tuple(z*z for z in fw(g));gs=[tuple(g[2*x+b] for x in range(len(g)//2)) for b in [0,1]];Ps=[tuple(z*z for z in fw(v)) for v in gs]
 rr=[Q[2*x]+Q[2*x+1] for x in range(len(g)//2)];m=[P[2*x]+P[2*x+1] for x in range(len(g)//2)];s=sum(Q)
 raw=[[rr[x]*Ps[b][x]/m[x] if m[x] else rr[x] for x in range(len(m))] for b in [0,1]];Z=[sum(v) for v in raw]
 ck(sum(Z)==2*s);refs=[tuple(s*z/Z[b] for z in raw[b]) for b in [0,1]]
 for q in refs:ck(sum(q)==s)
 return gs,refs
def point_list(a,b,M,policy):
 D0=a+b;out=[0]
 for j in range(2,M+1):
  prev=D0+j-1
  if policy==0:z=0
  elif policy==1:z=(1<<a) if j%3==2 else (1<<(a+b-1)) if j%3==0 else (2**a-1)|(1<<(prev-1))
  else:z=(1<<(prev-1)) if j%3==2 else (2**a-1) if j%3==0 else (1<<a)|(1<<(prev-1))
  out.append(z)
 return out
def value(g,a,b,points,j,x):
 ans=g[x%(2**a)]
 for i in range(j):
  if x%(2**(a+b+i+1))==points[i]:ans=-ans
 return ans
class Model:
 def __init__(self,g,Q,a,b,points,fixed,src,pads):
  self.g=g;self.Q=Q;self.a=a;self.b=b;self.points=points;self.fixed=fixed;self.src=src;self.pads=pads;self.n0=len(src)+len(pads);self.amp0=fw(g)
  self.hit=[all((p>>i&1)==v for i,v in fixed.items()) for p in points]
  self.local=[];self.sign=[]
  # Reconstruct original source values only to evaluate actual operation signs.
  for j,p in enumerate(points):
   rem=src+pads+list(range(a+b,a+b+j));self.local.append(sum((p>>orig&1)<<k for k,orig in enumerate(rem)))
  self.dist=[len(src)+pads.index(i) for i in [a,a+b-1] if i in pads]
  self.unused=[len(src)+k for k,i in enumerate(pads) if i not in [a,a+b-1]]
  self.signs=None
 @lru_cache(maxsize=None)
 def calc(self,j,S):
  if j==0:
   return (self.amp0[S] if S<len(self.amp0) else F(0),self.Q[S] if S<len(self.Q) else F(0))
  n=self.n0+j-1;T=S%(2**n);U=S//(2**n);amp,qprev=self.calc(j-1,T)
  if not self.hit[j-1]:return (amp,qprev) if U==0 else (F(0),F(0))
  rho=F(1,2**(n+1));phase=self.signs[j-1]*(-1 if (T&self.local[j-1]).bit_count()%2 else 1)
  new=(amp if U==0 else 0)-2*rho*phase
  beta=(6 if j==1 else 8 if j==2 else 4*(1+4*j*(j+1)))*rho
  marginal=amp*amp-4*rho*phase*amp+2*F(1,2**(2*n))
  ck(marginal>0)
  q=(qprev+beta/F(2**n))/(1+beta)*new*new/marginal
  return new,q
 def rows(self,j):
  positions=list(range(len(self.src)))+self.dist+list(range(self.n0,self.n0+j));u=len(self.unused)
  rows=[];mass=Pmass=I=F(0)
  for mask in range(2**len(positions)):
   S=sum(((mask>>k)&1)<<p for k,p in enumerate(positions))
   for nz in range(2 if u else 1):
    W=S|((1<<self.unused[0]) if nz else 0);mult=(2**u-1) if nz else 1
    amp,q=self.calc(j,W);p=amp*amp;rows.append((W,mult,p,q));mass+=mult*q;Pmass+=mult*p
    I+=p*(mult*S.bit_count()+(u*2**(u-1) if nz else 0))
  expected=sum(self.Q)
  for i in range(1,j+1):
   if self.hit[i-1]:
    rho=F(1,2**(self.n0+i));beta=(6 if i==1 else 8 if i==2 else 4*(1+4*i*(i+1)))*rho;expected=(expected+beta)/(1+beta)
  ck(Pmass==1);ck(mass==expected)
  return rows,I,mass
 def measure(self,j):
  rows,I,mass=self.rows(j);CE=cost_rows(rows);H=cost_rows(rows,True)
  return CE,H,sub(CE,H),I,mass,rows
def make_model(g,Q,a,b,points,fixed,src,pads,signs):
 m=Model(g,Q,a,b,points,fixed,src,pads);m.signs=signs;return m
def run_sequence(a,label,mode,policy,M=4,b=12,export=False):
 g=tuple(1 if label>>x&1 else -1 for x in range(2**a));P=tuple(z*z for z in fw(g));Q=P if mode==0 else tuple(p/2 for p in P) if mode==1 else tuple(F(i+1,3*sum(range(1,len(P)+1))) for i in range(len(P)))
 points=point_list(a,b,M,policy);signs=[value(g,a,b,points,j,p) for j,p in enumerate(points)]
 src=list(range(a));pads=list(range(a,a+b));root=make_model(g,Q,a,b,points,{},src,pads,signs)
 c=cost_rows([(i,1,p,q) for i,(p,q) in enumerate(zip(P,Q))]);Ig=Itruth(g);C0=c[1]/Ig;K=4*C0+15;U=(C0+F(37,8))*Ig
 rootdata=[None]+[root.measure(j) for j in range(1,M+1)];physical=Ig;Gsum=F(0);roots=frontiers=pos=neg=0;gold=[];pastL={};pastC={};pastI=Ig
 for j in range(1,M+1):
  n=a+b+j-1;p=points[j-1];d=sum(value(g,a,b,points,j-1,p)!=value(g,a,b,points,j-1,p^(1<<i)) for i in range(n));rho=F(1,2**(n+1));G=2*rho*(n+1-d);E=2*rho*d;Gsum+=G;physical+=G-E
  CE,H,D,I,mass,rows=rootdata[j];ck(I==physical);margin=(F(241,1024)*C0+F(54191,8192))*Ig+K*Gsum
  ck(K*I-CE[1]-U>=margin);roots+=1
  if j>=3:ck(CE[1]<=(1+F(1,8*j*(j+1)))*pastC[0][1]+36*(1+4*j*(j+1))*rho*(n+1))
  pastL[0]=CE;pastC[0]=CE
  off=(F(0),F(0));CEoff=(F(0),F(0));signed=CE;parentD=D;currg=g;currQ=Q;currsrc=src[:];currpads=pads[:];fixed={}
  if export:gold.append(export_model(root,j,'root',rows))
  for depth in range(1,b+a+1):
   if currpads:
    orig=currpads.pop(0);otherg=currg;otherQ=currQ
   else:
    orig=currsrc.pop(0);gs,refs=source_split(currg,currQ);currg,otherg=gs;currQ,otherQ=refs
   fixed0={**fixed,orig:0};fixed1={**fixed,orig:1}
   aa=make_model(currg,currQ,a,b,points,fixed0,currsrc[:],currpads[:],signs);oo=make_model(otherg,otherQ,a,b,points,fixed1,currsrc[:],currpads[:],signs)
   ma=aa.measure(j);mo=oo.measure(j);lam=F(1,2**depth);Da=ma[2];Do=mo[2]
   reset=sub(mul(add(Da,Do),F(1,2)),parentD)
   if reset[0]>0:pos+=1
   if reset[1]<0:neg+=1
   signed=add(signed,mul(reset,2*lam));off=add(off,mul(Do,lam));CEoff=add(CEoff,mul(mo[0],lam));Cbar=add(CEoff,mul(ma[0],lam));L=add(H,add(off,mul(Da,lam)))
   ck(K*I-L[1]-U>=margin)
   ck(max(signed[0],L[0])<=min(signed[1],L[1]))
   if j>=3:ck(Cbar[1]<=(1+F(1,8*j*(j+1)))*pastC[depth][1]+36*(1+4*j*(j+1))*rho*(n+1))
   if j>=2:
    delta=sub(L,pastL[depth]);oldbank=(K*pastI-pastL[depth][1]-U,K*pastI-pastL[depth][0]-U)
    carry=add(oldbank,(K*(I-pastI)-delta[1],K*(I-pastI)-delta[0]));newbank=(K*I-L[1]-U,K*I-L[0]-U)
    ck(max(carry[0],newbank[0])<=min(carry[1],newbank[1]));ck(carry[0]>0)
   pastL[depth]=L;pastC[depth]=Cbar
   if export and j==M:
    gold.append(export_model(aa,j,'active'+str(depth),ma[-1]));gold.append(export_model(oo,j,'other'+str(depth),mo[-1]))
   fixed=fixed0;parentD=Da;frontiers+=1
   if time.monotonic()-start>limit_seconds:raise RuntimeError('frozen runtime cutoff '+str(limit_seconds))
  # Clear lru caches including bound instance keys before next target prefix.
  root.calc.cache_clear();pastI=I
 if export:return {'a':a,'b':b,'label':label,'mode':mode,'policy':policy,'M':M,'points':points,'models':gold}
 return roots,frontiers,pos,neg
def export_model(model,j,node,rows):
 return {'node':node,'j':j,'g':list(model.g),'R':[str(z) for z in model.Q],'fixed':model.fixed,'src':model.src,'pads':model.pads,'unused_local':model.unused,'records':[[S,m,str(p),str(q)] for S,m,p,q in rows]}
if __name__=='__main__':
 mode=sys.argv[1];roots=frontiers=pos=neg=sequences=0
 if mode=='gold':
  values=[run_sequence(1,1,2,1,3,export=True),run_sequence(2,1,2,0,2,export=True)];(RUN/'out/GOLD.json').write_text(json.dumps(values),encoding='utf-8',newline='');sequences=2
 elif mode=='grid':
  for a in range(1,17):
   for b in range(12,33):
    L=a+b;s=F(0)
    for M in range(1,129):
     s+=F((1+M*(M+1))*(L+M),2**M);tail=F(M**3+(L+7)*M*M+(5*L+23)*M+9*L+34,2**M)
     ck(s+tail==9*L+34);ck(F(9*b+43,2**(b+1))<=F(151,8192));ck(F(b+3,2**b)<=F(15,4096));roots+=1
  prod=F(1);eta=F(0)
  for j in range(3,513):
   e=F(1,8*j*(j+1));eta+=e;prod*=1+e;ck(eta==F(1,24)-F(1,8*(j+1)));ck(prod<=F(24,23));ck(4*F(1+4*j*(j+1),2**j)<=25);ck(F(864+4606*j*(j+1),23)<=201*(1+j*(j+1)))
  ck(4*F(4081,4096)-F(11,4)-1==F(241,1024));ck(15*F(4081,4096)-201*F(151,8192)-F(37,8)==F(54191,8192))
  # A094 new coefficient step, reconstructed without changing its source models.
  ck(F(7,8)*4-F(3,2)==2);ck(F(7,8)*15-F(61,8)==F(11,2));ck(F(7,8)*4-F(5,2)==1);ck(F(7,8)*15-F(15,2)==F(45,8));ck(F(11,2)-F(37,8)==F(7,8))
  for N in range(2,65):
   M=2**(N-1);S=F(N,2**N)*(M+F(M*(M+1)*(M+2),3));ck(S>=F(N,3)*2**(2*N-3))
 else:
  fixtures=[(1,1),(1,2)]+[(2,l) for l in [1,3,6,7]]+[(3,l) for l in [1,23,105,126]]
  cases=[(a,l,q,p) for a,l in fixtures for q in range(3) for p in range(3)]
  cases=[(1,1,1,1)] if mode=='pilot' else cases[int(mode)*15:(int(mode)+1)*15]
  for a,l,q,p in cases:
   rr,ff,pp,nn=run_sequence(a,l,q,p,3 if mode=='pilot' else 4);roots+=rr;frontiers+=ff;pos+=pp;neg+=nn;sequences+=1
 out={'status':'PASS','mode':mode,'sequences':sequences,'target_prefixes_or_grid_tuples':roots,'frontiers':frontiers,'positive_resets':pos,'negative_resets':neg,'exact_assertions':checks,'seconds':time.monotonic()-start,'compression':'exact per-atom values with multiplicities and unused-pad Hamming sums; no orbit extrapolation'}
 (RUN/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8',newline='');print(json.dumps(out))

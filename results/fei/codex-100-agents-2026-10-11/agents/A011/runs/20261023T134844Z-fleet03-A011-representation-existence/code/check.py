import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import json,time
import shared
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0;zero_fibers=0
def ck(v):
 global checks
 checks+=1;assert v,checks
def fw(v):
 a=list(v);d=1
 while d<len(a):
  for k in range(0,len(a),2*d):
   for i in range(k,k+d):a[i],a[i+d]=a[i]+a[i+d],a[i]-a[i+d]
  d*=2
 return tuple(F(z,len(a)) for z in a)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,x):return a[0]*x,a[1]*x
def cost(rows,entropy=False):
 agg=defaultdict(F)
 for S,m,p,q in rows:
  if p:ck(q>0);agg[p if entropy else q]+=m*p
 lo=hi=F(0)
 for q,p in agg.items():l,h=shared.log(1/q);lo+=p*l;hi+=p*h
 return lo,hi
def Itruth(v):
 n=len(v).bit_length()-1
 return F(2*sum(v[x]!=v[x^(1<<i)] for x in range(len(v)) for i in range(n)),2*len(v))
def split(g,Q,idx):
 N=len(g)//2
 def ins(T,b):return (T%(1<<idx))+b*(1<<idx)+(T//(1<<idx))*(1<<(idx+1))
 gs=[tuple(g[ins(x,b)] for x in range(N)) for b in (0,1)];P=tuple(z*z for z in fw(g));PP=[tuple(z*z for z in fw(h)) for h in gs]
 mm=[P[ins(T,0)]+P[ins(T,1)] for T in range(N)];rr=[Q[ins(T,0)]+Q[ins(T,1)] for T in range(N)];s=sum(Q)
 raw=[[rr[T]*PP[b][T]/mm[T] if mm[T] else rr[T] for T in range(N)] for b in (0,1)];Z=[sum(x) for x in raw];ck(sum(Z)==2*s)
 refs=[tuple(s*x/Z[b] for x in raw[b]) for b in (0,1)];ck(all(sum(x)==s for x in refs));return gs,refs
def points(a,b,M,scenario):
 out=[0]
 for j in range(2,M+1):
  if scenario==2:z=0
  elif scenario==0:z=(1<<a) if j==2 else (1<<(a+b-1))|1
  else:z=(1<<(a+b+j-2)) if j==2 else 1|(1<<a)
  out.append(z)
 return out
def value(g,a,b,pts,j,x):
 v=g[x%len(g)]
 for k in range(1,j+1):
  old=a+b+k-1
  if x%(1<<old)==pts[k-1] and not(x>>old&1):v=-v
 return v
class Node:
 def __init__(self,g,Q,a,b,M,pts,signs,fixed=None,path=None):
  self.g=g;self.Q=Q;self.a=a;self.b=b;self.M=M;self.pts=pts;self.signs=signs;self.fixed=fixed or {};self.path=path or [];self.src=[i for i in range(a) if i not in self.fixed];self.A=fw(g);self.children=None
 def child(self,coord):
  ck(coord not in self.fixed)
  if coord<self.a:gs,refs=split(self.g,self.Q,self.src.index(coord))
  else:gs=[self.g]*2;refs=[self.Q]*2
  self.children=[Node(gs[bit],refs[bit],self.a,self.b,self.M,self.pts,self.signs,{**self.fixed,coord:bit},self.path+[(coord,bit)]) for bit in (0,1)];return self.children
 def hit(self,j):
  D=self.a+self.b+j;old=D-1
  return all(bit==((self.pts[j-1]>>i)&1 if i<old else 0) for i,bit in self.fixed.items() if i<D)
 def free(self,D):return [i for i in range(D) if i not in self.fixed]
 @lru_cache(None)
 def calc(self,j,S):
  global zero_fibers
  if j==0:
   if S&~sum(1<<i for i in self.src):return F(0),F(0)
   T=sum(((S>>i)&1)<<k for k,i in enumerate(self.src));return self.A[T],self.Q[T]
  old=self.a+self.b+j-1;T=S%2**old;U=S//2**old;A,Q=self.calc(j-1,T)
  if not self.hit(j):return (A,Q) if U==0 else (F(0),F(0))
  n=len(self.free(old));r=int(old not in self.fixed);t=F(1,2**n);p=F(1,2**r);rho=t*p;phase=self.signs[j-1]*(-1 if (T&self.pts[j-1]).bit_count()%2 else 1)
  amp=(A if U==0 else 0)-2*rho*phase;data=A*A-4*rho*phase*A+4*p*t*t;beta=(6 if j==1 else 8 if j==2 else 4*(1+4*j*(j+1)))*rho
  floor=(Q+beta*t)/(1+beta)
  if not data:ck(r==0 and amp==0);zero_fibers+=1;return amp,floor
  return amp,floor*amp*amp/data
 def measure(self,j):
  D=self.a+self.b+j;free=self.free(D);unused=[i for i in free if self.a<i<self.a+self.b-1];positions=[i for i in free if i not in unused];u=len(unused);rows=[];mass=Pmass=I=F(0)
  for mask in range(2**len(positions)):
   S=sum(((mask>>k)&1)<<i for k,i in enumerate(positions))
   for nz in range(2 if u else 1):
    W=S|((1<<unused[0]) if nz else 0);mult=2**u-1 if nz else 1;A,q=self.calc(j,W);p=A*A;rows.append((W,mult,p,q));Pmass+=mult*p;mass+=mult*q;I+=p*(mult*S.bit_count()+(u*2**(u-1) if nz else 0))
  expected=sum(self.Q)
  for k in range(1,j+1):
   if self.hit(k):
    rho=F(1,2**len(self.free(self.a+self.b+k)));beta=(6 if k==1 else 8 if k==2 else 4*(1+4*k*(k+1)))*rho;expected=(expected+beta)/(1+beta)
  ck(Pmass==1);ck(mass==expected);ck(0<mass<=1);ce=cost(rows);h=cost(rows,True)
  return ce,h,sub(ce,h),rows,unused,I
def make_tree(g,Q,a,b,M,pts,signs,scenario):
 root=Node(g,Q,a,b,M,pts,signs);nodes=[root];expansions=[];N=a+b+M
 if scenario<2:
  if scenario==0:order=list(range(N-1,a+b-1,-1))+list(range(a-1,-1,-1))+list(range(a+b-1,a-1,-1))
  else:
   order=list(range(a-1,-1,-1));pads=list(range(a,a+b));ctrl=list(range(a+b,N))
   while pads or ctrl:
    if pads:order.append(pads.pop(0))
    if ctrl:order.append(ctrl.pop(0))
  active=root
  for depth,coord in enumerate(order):
   ch=active.child(coord);nodes+=ch;expansions.append(active);active=ch[0 if scenario==0 else depth%2]
 else:
  leaves=[root]
  for coord in list(range(N-1,a+b-1,-1))+[0]:
   new=[]
   for v in leaves:
    ch=v.child(coord);nodes+=ch;expansions.append(v);new+=ch
   leaves=new
 return root,nodes,expansions
def run(a,label,mode,scenario,M=3,export=False):
 g=tuple(1 if label>>x&1 else -1 for x in range(2**a));P=tuple(z*z for z in fw(g));Q=P if mode==0 else tuple(p/2 for p in P) if mode==1 else tuple(F(i+1,3*sum(range(1,len(P)+1))) for i in range(len(P)))
 pts=points(a,12,M,scenario);signs=[value(g,a,12,pts,j,z) for j,z in enumerate(pts)];root,nodes,expansions=make_tree(g,Q,a,12,M,pts,signs,scenario);c=cost([(i,1,p,q) for i,(p,q) in enumerate(zip(P,Q))]);Ig=Itruth(g);C0=c[1]/Ig;K=4*C0+15;U=(C0+F(37,8))*Ig;I=Ig;Gsum=F(0);frontiers=roots=multi=positive=negative=0;pastL={};pastC={};pastI=Ig;gold=[]
 for j in range(1,M+1):
  D=a+12+j;rho=F(1,2**D);z=pts[j-1];degree=sum(value(g,a,12,pts,j-1,z)!=value(g,a,12,pts,j-1,z^(1<<i)) for i in range(D-1));G=2*rho*(D-degree);E=2*rho*degree;I+=G-E;Gsum+=G
  measured={v:v.measure(j) for v in nodes};ce,H,div,rr,unused,Is=measured[root];ck(Is==I);margin=(F(6311,23552)*C0+F(18111,4096))*Ig+K*Gsum;ck(K*I-ce[1]-U>=margin);roots+=1
  leaves=[root];signed=ce
  def frontier_test(index):
   nonlocal frontiers,multi
   lam=lambda v:F(1,2**len(v.path));C=(F(0),F(0));DD=(F(0),F(0));hitmass=F(0);hits=0
   for v in leaves:
    C=add(C,mul(measured[v][0],lam(v)));DD=add(DD,mul(measured[v][2],lam(v)))
    if v.hit(j):hitmass+=lam(v)*F(1,2**len(v.free(D)));hits+=1
   ck(hitmass==rho)
   if hits>1:multi+=1
   L=add(H,DD);ck(K*I-L[1]-U>=margin);ck(max(signed[0],L[0])<=min(signed[1],L[1]))
   if j>=3:ck(C[1]<=(1+F(1,8*j*(j+1)))*pastC[index][1]+64*(1+4*j*(j+1))*rho*D)
   if j>=2:
    debit=sub(L,pastL[index]);old=(K*pastI-pastL[index][1]-U,K*pastI-pastL[index][0]-U);carry=add(old,(K*(I-pastI)-debit[1],K*(I-pastI)-debit[0]));ck(carry[0]>0);ck(max(carry[0],K*I-L[1]-U)<=min(carry[1],K*I-L[0]-U))
   pastL[index]=L;pastC[index]=C;frontiers+=int(index>0)
  frontier_test(0)
  for index,v in enumerate(expansions,1):
   dd=sub(mul(add(measured[v.children[0]][2],measured[v.children[1]][2]),F(1,2)),measured[v][2]);signed=add(signed,mul(dd,F(1,2**len(v.path))))
   if dd[0]>0:positive+=1
   if dd[1]<0:negative+=1
   leaves.remove(v);leaves+=v.children;frontier_test(index)
   if time.monotonic()-start>(55 if sys.argv[1]=='pilot' else 300):raise RuntimeError('frozen deadline')
  if export and j==M:
   for v in nodes:
    gold.append({'fixed':v.fixed,'path':v.path,'g':list(v.g),'Q':[str(x) for x in v.Q],'unused':measured[v][4],'records':[[S,m,str(p),str(q)] for S,m,p,q in measured[v][3]]})
  root.calc.cache_clear();pastI=I
 if export:return {'a':a,'b':12,'M':M,'label':label,'mode':mode,'scenario':scenario,'points':pts,'nodes':gold}
 return {'sequences':1,'target_prefixes':roots,'frontiers':frontiers,'multiple_hit_frontiers':multi,'positive_resets':positive,'negative_resets':negative}
if __name__=='__main__':
 mode=sys.argv[1];tot=defaultdict(int)
 if mode=='gold':
  data=[run(1,1,2,0,3,True),run(2,1,2,2,2,True)];(R/'out/GOLD.json').write_text(json.dumps(data),encoding='utf-8',newline='');tot['sequences']=2
 elif mode=='scalar':
  for a in range(1,17):
   for b in range(12,33):
    L=a+b;s=F(0)
    for M in range(1,129):
     s+=F((1+M*(M+1))*(L+M),2**M);tail=F(M**3+(L+7)*M*M+(5*L+23)*M+9*L+34,2**M);ck(s+tail==9*L+34);ck(F(9*b+43,2**(b+1))<=F(151,8192));tot['scalar_tuples']+=1
  for j in range(3,513):ck(5+16*j*(j+1)<=2**(j+5));ck(F(1536+7294*j*(j+1),23)<=320*(1+j*(j+1)))
  ck(4*F(4081,4096)-F(125,46)-1==F(6311,23552));ck(15*F(4081,4096)-320*F(151,8192)-F(37,8)==F(18111,4096))
 else:
  cases=[(a,l,q,p) for a,l in [(1,1),(1,2),(2,1),(2,6),(3,23),(3,105)] for q in range(3) for p in range(3)];cases=[(1,1,2,0)] if mode=='pilot' else cases[int(mode)*9:(int(mode)+1)*9]
  for a,l,q,p in cases:
   for k,v in run(a,l,q,p,2 if mode=='pilot' else 3).items():tot[k]+=v
 result={'status':'PASS','mode':mode,**tot,'zero_data_fibers_retained':zero_fibers,'exact_assertions':checks,'seconds':time.monotonic()-start}
 (R/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8',newline='');print(json.dumps(result))

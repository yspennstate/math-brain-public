"""Independent literal Walsh and prime-log identity audit; frozen24."""
from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];START=time.monotonic();N=0
def ck(a,s):
 global N
 N+=1
 assert a,s
 assert time.monotonic()-START<55,'frozen guard'
def spec(t):
 n=len(t)
 return [F(sum(v*(-1 if (x&m).bit_count()%2 else 1) for x,v in enumerate(t)),n)**2 for m in range(n)]
def rem(t,j,y):
 return [t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(y<<j)] for x in range(len(t)//2)]
def er(p,j):
 return [p[(x&((1<<j)-1))|((x>>j)<<(j+1))]+p[(x&((1<<j)-1))|((x>>j)<<(j+1))|(1<<j)] for x in range(len(p)//2)]
def qlaw(p):
 if sum(x>0 for x in p)==1:return p[:]
 q=[p[0]]+[F(5,6)*x for x in p[1:]];q[-1]+=F(1,6)*(1-p[0]);return q
def lift(t,q,qu):
 p=spec(t);w=(len(q)-1).bit_length()
 return [p[i] if i>>1==0 else q[(i>>1)&((1<<w)-1)]*qu[i>>(w+1)]/4 for i in range(len(p))]
def prime(n):
 d={};k=2
 while k*k<=n:
  while n%k==0:d[k]=d.get(k,0)+1;n//=k
  k+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def add(a,b,c=F(1)):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,F(0))+c*v
 return {k:v for k,v in out.items() if v}
def logvec(x):
 return add(prime(x.numerator),prime(x.denominator),F(-1))
def kl(p,q):
 out={}
 for a,b in zip(p,q):
  if a:out=add(out,logvec(a/b),a)
 return out
def select(v,u,eps,sgn):
 core=[sgn*a*b for b in u for a in v]
 return [eps if x%2==0 else core[x>>1] for x in range(2*len(core))]
def one(w,k,sp,eps,sgn):
 v=[(-1 if (x&((1<<k)-1)).bit_count()%2 else 1)*(-1 if x==0 else 1) for x in range(1<<w)]
 u=[1] if sp==0 else [1,-1];p=spec(v);q=qlaw(p);qu=qlaw(spec(u));t=select(v,u,eps,sgn)
 P=spec(t);Q=lift(t,q,qu);ll=[b/a if a else F(1) for a,b in zip(p,q)]
 B=[a*ll[(i>>1)&((1<<w)-1)] for i,a in enumerate(P)]
 j=k+1;pb=er(P,j);qb=er(Q,j);bb=er(B,j);rs=[];lhs={};fresh={}
 for y in [0,1]:
  ct=rem(t,j,y);cp=spec(ct);ker=[a/(2*b) if b else F(1,2) for a,b in zip(cp,pb)]
  r=sum(a*b for a,b in zip(qb,ker));rs.append(r)
  old=[a*b/r for a,b in zip(qb,ker)]
  vy=rem(v,k,y);py=spec(vy);qy=qlaw(py);new=lift(ct,qy,qu)
  ck(sum(old)==sum(new)==sum(cp)==1,'normalized full children')
  ck(sum(a*b for a,b in zip(bb,ker))==r,'independent spectator cancellation')
  lhs=add(lhs,add(kl(cp,new),kl(cp,old),F(-1)),F(1,2));fresh=add(fresh,kl(py,qy),F(1,4))
 rhs=add(add(fresh,kl(pb,bb),F(-1)),kl([F(1,2)]*2,rs))
 ck(lhs==rhs,'EXACT prime-log complete normalized reset identity')
 d=F(1,1<<w);A=F(1,2)+4*d*d;alpha=F(1,6)
 coarse=[A,4*d*d,F(1,2)-8*d*d];coarseB=[A-2*alpha*d*d,alpha/2+(4-6*alpha)*d*d,F(5,6)*(F(1,2)-8*d*d)]
 # Group the erased outer law by its target data mask, after removing x.
 q0=qf=p0=pf=F(0)
 for i,(a,b) in enumerate(zip(pb,bb)):
  target=(i>>1)&((1<<(w-1))-1)
  if target==0:p0+=a;q0+=b
  if target==(1<<(w-1))-1:pf+=a;qf+=b
 ck([p0,pf,1-p0-pf]==coarse and [q0,qf,1-q0-qf]==coarseB,'literal coarsened three masses')
 gap=add(logvec(F(6,5)),{},F(0));gap={z:-v/F(4) for z,v in gap.items()}
 gap=add(gap,logvec(1-2*alpha*d*d/A),A)
 gap=add(gap,logvec((2*alpha+(16-24*alpha)*d*d)/(alpha+(16-32*alpha)*d*d)),4*d*d)
 ck(add(fresh,kl(coarse,coarseB),F(-1))==gap,'EXACT coarsened cancellation formula')
 return {'w':w,'k':k,'spectator':sp,'epsilon':eps,'sign':sgn,'outcomes':list(map(str,rs)),'sigma_prime_log':{str(z):str(v) for z,v in lhs.items()}}
rows=[one(w,k,sp,eps,s) for w,k in [(3,1),(4,1),(4,2)] for sp in [0,1] for eps in [1,-1] for s in [1,-1]]
out={'status':'PASS','cases':len(rows),'checks':N,'runtime_seconds':time.monotonic()-START,'method':'literal Walsh, independently normalized kernels, exact prime-log equality','external_review':'PENDING','rows':rows}
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

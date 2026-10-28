from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,json,time,hashlib
import exact as E
R=Path(__file__).resolve().parents[1];START=time.monotonic();COUNT=0
stats=dict(tables=0,queries=0,updates=0,trees=0,affine_fixtures=0,moment_fixtures=0,handoff_queries=0,activation_fixtures=0)
def ck(x):
 global COUNT
 COUNT+=1
 assert x,COUNT
 assert time.monotonic()-START<55,'55 second frozen cap'
def neg(x):return E.sc(-1,x)
def equal(a,b):ck(a==b)
def nonneg(x):ck(not x or E.bounds(x)[0]>=0)
@lru_cache(None)
def spec(f):
 N=len(f)
 return tuple(F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(f))**2,N*N) for s in range(N))
def influence(f):
 n=len(f).bit_length()-1
 return sum(F(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f)) for j in range(n))
def profile(p,q,theta):
 cells=[0 if s==0 else 1+s.bit_count()%2 for s in range(len(p))]
 pc=[sum(p[s] for s,c in enumerate(cells) if c==j) for j in range(3)]
 qc=[sum(q[s] for s,c in enumerate(cells) if c==j) for j in range(3)]
 rc=[(1-theta)*a+theta*b for a,b in zip(qc,pc)]
 u=tuple(q[s]*rc[c]/qc[c] if qc[c] else F(0) for s,c in enumerate(cells))
 equal(sum(u),1)
 fee=E.kl(u,q);G=E.add(E.kl(p,u),neg(E.kl(p,q)),fee)
 if 0<theta<1:
  # Zero q-cells have zero true and new cell mass and are omitted jointly.
  ids=[j for j in range(3) if qc[j]]
  qq=tuple(qc[j] for j in ids);rr=tuple(rc[j] for j in ids)
  equal(G,E.sc(-(1-theta)/theta,E.add(E.kl(rr,qq),E.kl(qq,rr))))
 else:equal(G,{})
 nonneg(neg(G));stats['updates']+=1
 return u,fee,G
def query(f,q,j):
 p=spec(f);mp=E.marg(p,j);mq=E.marg(q,j)
 fs=[E.child(f,j,t) for t in [0,1]];ps=[spec(h) for h in fs]
 equal(tuple((a+b)/2 for a,b in zip(*ps)),mp)
 L=E.add(E.kl(p,q),neg(E.kl(mp,mq)))
 J=E.sc(F(1,2),E.add(*(E.kl(x,mp) for x in ps)))
 equal(E.sc(F(1,2),E.add(*(E.kl(x,mq) for x in ps))),E.add(E.kl(p,q),J,neg(L)))
 d=F(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f))
 equal(d,sum(p[s] for s in range(len(p)) if s&(1<<j)))
 nonneg(L);nonneg(J)
 if J:
  hi=E.bounds(J)[1];ln2hi=E.ln_bounds(F(2))[1];ck(hi*ln2hi<=2*d)
 else:ck(True)
 dh=E.add(E.ent(p),E.sc(F(-1,2),E.add(*(E.ent(x) for x in ps))))
 equal(E.add(dh,L,E.sc(F(1,2),E.add(*(E.ce(x,mq) for x in ps)))),E.add(E.ce(p,q),J))
 stats['queries']+=1
 return fs,mq,L,J,dh
def tree(f,q,depth=0):
 p=spec(f);n=len(f).bit_length()-1
 if n==0 or (depth==1 and f[0]<0):return E.ce(p,q),{},influence(f)
 theta=[F(0),F(1,2),F(1)][(depth+int(f[0]<0))%3]
 u,fee,G=profile(p,q,theta)
 fs,mq,L,J,dh=query(f,u,(depth+int(f[-1]<0))%n)
 vals=[tree(h,mq,depth+1) for h in fs]
 bill=E.add(fee,dh,L,E.sc(F(1,2),E.add(*(x[0] for x in vals))))
 credit=E.add(G,J,E.sc(F(1,2),E.add(*(x[1] for x in vals))))
 equal(bill,E.add(E.ce(p,q),credit))
 terminal_I=(vals[0][2]+vals[1][2])/2
 surplus=E.add(bill,neg(E.ce(p,q)))
 if surplus:
  ck(E.bounds(surplus)[1]*E.ln_bounds(F(2))[1]<=2*(influence(f)-terminal_I))
 return bill,credit,terminal_I
def moment(n):
 N=1<<n;k=n-1;eps=F(1,2**(4*n));p=(F(1,N),)*N
 f=tuple((-1)**sum((x>>(2*j))&3==0 for j in range(n//2)) for x in range(N))
 equal(spec(f),p);equal(influence(f),F(n,2))
 q=tuple(p[s]*(1+(1-eps)*(-1)**((s&((1<<k)-1)).bit_count())) if s&(1<<k) else p[s] for s in range(N))
 equal(sum(q),1);equal(q[0],p[0]);ck(all(x>0 for x in q))
 # Inclusion-exclusion then supplies every low-order marginal, not just moments.
 for U in range(N):
  if U.bit_count()<=n-2:equal(sum(q[s]-p[s] for s in range(N) if s&U==U),0)
 a=F(1,4);D=E.add({2:F(n)},E.sc(-a,E.logq(2-eps)))
 equal(E.kl(p,q),D)
 for j in range(k):equal(E.marg(q,j),E.marg(p,j))
 nonneg(E.add(D,{2:-F(n)+a}));nonneg(E.add({2:F(n)},neg(D)))
 ck(1<2-eps<2)
 stats['moment_fixtures']+=1
def handoff():
 for flip in [-1,1]:
  for vertex in range(8):
   f=tuple(flip*(-1 if x==vertex else 1) for x in range(8));p=spec(f);q=(F(1,8),)*8
   equal(E.ce(p,q),{2:F(3)});equal(influence(f),F(3,4))
   for j in range(3):
    fs,mq,L,J,dh=query(f,q,j);mp=E.marg(p,j);Gs=[]
    for h in fs:
     pp=spec(h);raw=tuple(x*y/z if z else x for x,y,z in zip(mq,pp,mp));Z=sum(raw);u=tuple(x/Z for x in raw)
     G=E.add(E.kl(u,mq),E.kl(pp,u),neg(E.kl(pp,mq)));Gs.append(G)
     if pp[0]==1:equal(G,{})
     else:
      equal(u,(F(1,16),F(5,16),F(5,16),F(5,16)));equal(G,{5:F(3,16)})
    equal(E.sc(F(1,2),E.add(*Gs)),{5:F(3,32)});stats['handoff_queries']+=1
 # A matched AND2 projected constant child cannot be replaced in reverse direction.
 f=(-1,1,1,1);p=spec(f);mq=E.marg(p,0);pp=spec(E.child(f,0,1))
 ck(any(a>0 and b==0 for a,b in zip(mq,pp)))
def affine():
 p=(F(1,4),)*4;u=(F(1,4),F(1,8),F(3,8),F(1,4))
 for lam in [F(1,2),F(2),F(3)]:
  raw=tuple(x*lam**s.bit_count() for s,x in enumerate(u));q=tuple(x/sum(raw) for x in raw)
  equal(p[0],u[0]);equal(sum(x*s.bit_count() for s,x in enumerate(p)),sum(x*s.bit_count() for s,x in enumerate(u)))
  equal(E.kl(p,q),E.add(E.kl(p,u),E.kl(u,q)));stats['affine_fixtures']+=1
 # An extreme affine slice gives a zero-mass boundary outside true support.
 p=(F(1),F(0));q=(F(1,4),F(3,4));equal(E.kl(p,q),E.add(E.kl(p,p),E.kl(p,q)))
def activation():
 for n in range(3):
  N=1<<n
  for table in range(1<<N):
   h=tuple(1 if table&(1<<x) else -1 for x in range(N))
   for m in [1,2]:
    ng=1+m*n;g=tuple((-1 if x&1 else 1)*__import__('functools').reduce(lambda a,b:a*b,(h[(x>>(1+j*n))&(N-1)] for j in range(m)),1) for x in range(1<<ng));pg=spec(g);equal(pg[0],0)
    for r in [1,2]:
     prob=F(1,1<<r);f=tuple(g[x>>r] if x&((1<<r)-1)==0 else 1 for x in range(1<<(r+ng)));pf=spec(f)
     Ar=E.add({2:2*r*prob*(2-prob)},E.sc(-(1-prob)**2,E.logq((1-prob)**2)))
     equal(E.ent(pf),E.add(Ar,E.sc(prob,E.ent(pg))));equal(influence(f),prob*(influence(g)+r))
     q=tuple((x+F(1,len(pf)))/2 for x in pf);qD=sum(q[s] for s in range(len(q)) if s>>r)
     rg=tuple(sum(q[u+(s<<r)] for u in range(1<<r))/qD if s else F(0) for s in range(len(pg)))
     equal(sum(rg),1)
     nonneg(E.add(E.ce(pf,q),neg(Ar),E.sc(-prob,E.ce(pg,rg))))
     stats['activation_fixtures']+=1
def run(pilot):
 cap=2 if pilot else 3
 for n in range(cap+1):
  N=1<<n
  for table in range(1<<N):
   f=tuple(1 if table&(1<<x) else -1 for x in range(N));p=spec(f);equal(sum(p),1);stats['tables']+=1
   for q in [p,tuple((x+F(1,N))/2 for x in p)]:
    for theta in [F(0),F(1,2),F(1)]:profile(p,q,theta)
    for j in range(n):query(f,q,j)
    if n<=2:tree(f,q);stats['trees']+=1
 affine();handoff()
 for n in ([4] if pilot else [4,6,8,10]):moment(n)
 if not pilot:activation()
 obj=dict(status='PASS',exact_assertions=COUNT,seconds=time.monotonic()-START,**stats,scope='Bounded exact checks plus separate analytic proof; no initial influence-priced source')
 (R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8');print(json.dumps(obj))
if __name__=='__main__':run('--pilot' in sys.argv)

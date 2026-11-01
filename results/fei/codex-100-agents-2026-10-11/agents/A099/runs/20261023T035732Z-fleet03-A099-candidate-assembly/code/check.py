"""A099 v8 independent finite reconstruction. No author checker imported."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, sys, time, hashlib
R=Path(__file__).resolve().parents[1]
START=time.monotonic(); COUNT=0; STATS=dict(instances=0,policies=0,queries=0,resets=0,later_returns=0,old_nonconstant=0,positive_first=0)
def ck(x):
 global COUNT
 COUNT+=1
 assert x,COUNT
 assert time.monotonic()-START<55,'frozen time cap'
def save(name,obj): (R/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
@lru_cache(None)
def logq(q):
 d={}
 for k,sgn in [(q.numerator,1),(q.denominator,-1)]:
  p=2
  while p*p<=k:
   while k%p==0:d[p]=d.get(p,0)+sgn;k//=p
   p+=1
  if k>1:d[k]=d.get(k,0)+sgn
 return {p:F(v) for p,v in d.items() if v}
def add(*ds):
 r={}
 for d in ds:
  for k,v in d.items():r[k]=r.get(k,F(0))+v
 return {k:v for k,v in r.items() if v}
def sc(a,d):return {k:a*v for k,v in d.items() if a*v}
def ce(p,q):return add(*(sc(-a,logq(b)) for a,b in zip(p,q) if a))
def ent(p):return ce(p,p)
def kl(p,q):return add(ce(p,q),sc(-1,ent(p)))
@lru_cache(None)
def ln_bounds(x):
 z=(x-1)/(x+1); z2=z*z
 y=z;s=F(0)
 for k in range(18):s+=2*y/(2*k+1);y*=z2
 return s,s+2*y/(37*(1-z2))
@lru_cache(None)
def log_bounds(p):
 if p==2:return F(1),F(1)
 k=p.bit_length()-1;x=F(p,2**k);a,b=ln_bounds(x);c,d=ln_bounds(F(2))
 return k+a/d,k+b/c
def bounds(e):
 lo=hi=F(0)
 for p,v in e.items():
  a,b=log_bounds(p)
  lo+=v*(a if v>=0 else b);hi+=v*(b if v>=0 else a)
 return lo,hi
def nonnegative(e):
 if e:ck(bounds(e)[0]>=0)
 else:ck(True)
def insert(x,j,b):return (x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)
def marg(p,j):return tuple(p[insert(t,j,0)]+p[insert(t,j,1)] for t in range(len(p)//2))
def child(f,j,b):return tuple(f[insert(t,j,b)] for t in range(len(f)//2))
@lru_cache(None)
def spec(f):
 w=list(f);step=1
 while step<len(w):
  for a in range(0,len(w),2*step):
   for b in range(a,a+step):w[b],w[b+step]=w[b]+w[b+step],w[b]-w[b+step]
  step*=2
 return tuple(F(x*x,len(w)**2) for x in w)
def cal(q,z):
 if z==1:return (F(1),)+(F(0),)*(len(q)-1)
 ck(q[0]<1)
 return (z,)+tuple((1-z)*x/(1-q[0]) for x in q[1:])
def node(f,q,s,d,gamma,m,policy,path=(),seen=False):
 p=spec(f);n=len(f).bit_length()-1
 ck(sum(p)==sum(q)==sum(s)==1)
 ck(all(not a or b>0 for a,b in zip(p,q)))
 # Deterministic, outcome-sensitive internal reset policies; all branches retained.
 reset=(policy==1 and len(path)>=1 and path[0]==0) or (policy==2 and len(path)>=2 and path[-1]==1)
 if reset:
  fresh=cal(s,p[0]);delta=add(ce(p,fresh),sc(-1,ce(p,q)))
  STATS['resets']+=1
  if seen:
   ck(fresh==cal(q,p[0]))
   ck(delta==sc(-1,kl((p[0],1-p[0]),(q[0],1-q[0]))))
   STATS['later_returns']+=1;nonnegative(sc(-1,delta))
  else:
   if delta and bounds(delta)[0]>0:STATS['positive_first']+=1
  q=fresh;seen=True
 # Outcome-sensitive stopping retains nonconstant complete terminals.
 if n==0 or (len(path)>=2 and path[0]==1 and policy==1):
  if not seen and p[0]<1:STATS['old_nonconstant']+=1
  return ce(p,q)
 j=(len(path)+int(f[0]<0))%n
 pp=marg(p,j);qq=marg(q,j);ss=marg(s,j);dd=marg(d,j)
 fs=[child(f,j,b) for b in (0,1)];ps=[spec(h) for h in fs]
 ck(tuple((a+b)/2 for a,b in zip(*ps))==pp)
 # Independent physical edge count agrees with spectral influence.
 physical=F(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f))
 ck(physical==sum(p[t] for t in range(len(p)) if t&(1<<j)))
 B=add(ent(p),sc(-1,ent(pp)))
 refund=add(kl(p,q),sc(-1,kl(pp,qq)))
 actual=add(ce(p,q),sc(F(-1,2),add(*(ce(x,qq) for x in ps))))
 ck(actual==add(B,refund));nonnegative(refund)
 # The same exact identity holds for the comparison SUBprobability.
 dr=add(kl(p,d),sc(-1,kl(pp,dd)))
 ck(add(ce(p,d),sc(F(-1,2),add(*(ce(x,dd) for x in ps))))==add(B,dr))
 nonnegative(dr)
 STATS['queries']+=1
 vals=[node(h,qq,ss,dd,gamma,m,policy,path+(b,),seen) for b,h in enumerate(fs)]
 return add(B,sc(F(1,2),add(*vals)))
def run(pilot):
 n=2 if pilot else 3;N=2**n
 for table in range(2**N):
  f=tuple(1 if table&(1<<x) else -1 for x in range(N));p=spec(f);m=p[0]
  for eta in (F(1,4),F(1,2)):
   s=cal(tuple((1-eta)*x+eta/N for x in p),m)
   d=tuple(x if y else F(0) for x,y in zip(s,p))
   ck(d[0]==m and sum(d)<=1)
   for gamma in (F(1,2),F(3,4)):
    if m==1:q=s
    else:
     rest=1-m-gamma*sum(d[1:]);q=(m,)+tuple(gamma*x+rest*y/(1-m) for x,y in zip(d[1:],p[1:]))
    ck(sum(q)==1 and q[0]>=m and all(q[i]>=gamma*d[i] for i in range(1,N)))
    STATS['instances']+=1;c=ce(p,d);L=sc(-1,logq(gamma));bound=add(c,sc(1-m*m,L))
    for policy in range(3):
     ledger=node(f,q,s,d,gamma,m,policy)
     nonnegative(add(bound,sc(-1,ledger)));STATS['policies']+=1
 # Source-shape change control: actual parity3 -> two nonconstant parity2 children.
 f=tuple((-1)**x.bit_count() for x in range(8));h=child(f,0,0);p=spec(h)
 q=(F(0),F(1,4),F(1,4),F(1,2));r=(F(0),F(1,3),F(1,3),F(1,3))
 ck(spec(child(f,0,1))==p and p[0]==0 and p[3]==1)
 delta=add(ce(p,r),sc(-1,ce(p,q)))
 ck(delta==add(logq(F(3)),sc(-1,logq(F(2)))))
 lo,hi=bounds(delta);ck(lo>F(1,2))
 save('SHAPE_CONTROL.json',{'actual_function':'parity3, query coordinate0, either parity2 child','P':list(map(str,p)),
  'Q':list(map(str,q)),'R':list(map(str,r)),'signed_cost':'log2(3)-1','lower':str(lo),'upper':str(hi),
  'scope':'Excluded changed nonempty profile, not an FEI counterexample; both children nonconstant.'})
 result=dict(status='PASS',arithmetic='Fraction + exact prime-log cancellation + 18-term outward rational atanh intervals',
  n=n,Boolean_tables=2**N,exact_assertions=COUNT,seconds=time.monotonic()-START,**STATS)
 save('PILOT.json' if pilot else 'EXACT_RECONSTRUCTION.json',result);print(json.dumps(result))
if __name__=='__main__':run('--pilot' in sys.argv)

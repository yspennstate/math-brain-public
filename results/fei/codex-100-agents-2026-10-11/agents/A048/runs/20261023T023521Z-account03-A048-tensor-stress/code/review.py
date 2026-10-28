from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time,hashlib
import intervals as a
B=Path(__file__).resolve().parents[1]
start=time.monotonic();count=0
def check(v):
 global count
 count+=1
 if not v:raise AssertionError(count)
def overlap(u,v):return max(u[0],v[0])<=min(u[1],v[1])
def ce(p,q):
 s=a.const(0)
 for x,y in zip(p,q):
  if x:s=a.sub(s,a.scale(a.log2(y),x))
 return s
def inf(v):return sum((a.influence(v,i) for i in range((len(v)-1).bit_length())),F(0))
def surplus(v):return a.sub(a.const(4*inf(v)),a.entropy(a.spec(v)))
def lift(v,q):
 p=a.spec(v);mu=sum(v,F(0))/len(v);u=p[0]
 qc=[u]+[(1-u)*x/(1-q[0]) for x in q[1:]] if u<1 else [F(1)]+[F(0)]*(len(p)-1)
 fv=a.fixture(v);pf=a.spec(fv);Q=[F(0)]*len(pf)
 for j in range(8):Q[j]=pf[j]
 for s in range(1,len(p)):
  for j in (0,1,4,5):Q[8*s+j]=qc[s]/16
 check(sum(Q)==sum(qc)==1)
 check(all(not x or y>0 for x,y in zip(pf,Q)))
 for s in range(1,len(p)):
  for j in (0,1,4,5):check(pf[8*s+j]==p[s]/16)
 check(pf[2]==pf[3]==F(1,4))
 check(pf[0]==pf[1]==(1+mu)**2/16)
 check(pf[4]==pf[5]==(1-mu)**2/16)
 A=a.sub(ce(pf,Q),a.entropy(pf));Ac=a.sub(ce(p,qc),a.entropy(p))
 check(overlap(A,a.scale(Ac,F(1,4))))
 t=F(sum(x==-1 for x in v),len(v))
 check(inf(fv)==1+t/2+inf(v)/4)
 check(ce(pf,Q)[1]<=3+ce(p,qc)[1]/4+F(1,2**80))
 return fv,Q
records=[]
for n in range(3):
 for vals in product((-1,1),repeat=2**n):
  p=a.spec(vals);q=[(x+F(1,len(p)))/2 for x in p]
  fv,Q=lift(vals,q)
  children,qs=a.node(fv,Q,2)
  check(overlap(a.entropy(a.spec(children[0])),a.const(2)))
  for coordinate in (None,0,1):
   if coordinate is None:leaves=children;weights=[F(1,2)]*2
   else:
    cs,qq=a.node(children[1],qs[1],coordinate)
    leaves=[children[0]]+list(cs);weights=[F(1,2),F(1,4),F(1,4)]
   S=a.const(0)
   for w,leaf in zip(weights,leaves):S=a.add(S,a.scale(surplus(leaf),w))
   floor=1 if coordinate==1 else 2
   check(S[0]>=floor-F(1,2**75))
   # Equality cases are enclosed; the analytic proof establishes the floor.
  records.append({'n':n,'values':list(vals)})

# A distinct nonmatching supplier on a two-bit point defect.
seed=(1,1,1,-1);p=a.spec(seed);v=1-p[0]
q=[p[0]]+[F(7,8)*x+(v/8 if i==3 else 0) for i,x in enumerate(p[1:],1)]
f,Q=lift(seed,q);pf=a.spec(f)
check(ce(p,q)[1]<4*inf(seed)-F(1,4))
Mf=a.sub(a.const(4*inf(f)),ce(pf,Q));check(Mf[0]>1)
def tensor(law,T):
 out=[F(1)]
 for _ in range(T):out=[x*y for y in law for x in out]
 return out
sparse=[]
for T in (1,2):
 pp=tensor(pf,T);qq=tensor(Q,T);nb=5*T
 for k in (0,1,2):
  alpha=F(1,2**k);N=1<<(nb+k+1)
  vals=[]
  for w in range(N):
   controls=w&((1<<k)-1);z=(w>>k)&1;data=w>>(k+1);zv=(-1)**z
   for j in range(T):zv*=f[(data>>(5*j))&31]
   vals.append(zv if controls==(1<<k)-1 else 1)
  actual=a.spec(vals);ref=[F(0)]*N;expected=[F(0)]*N
  for control in range(1<<k):
   mass=(1-alpha)**2 if control==0 else alpha**2
   ref[control]=expected[control]=mass
   for s in range(len(pp)):
    j=control|(1<<k)|(s<<(k+1))
    ref[j]=alpha**2*qq[s];expected[j]=alpha**2*pp[s]
  check(actual==expected and sum(ref)==1)
  check(inf(vals)==alpha*(k+1+T*inf(f)))
  quotient=[(1-alpha)**2]+[alpha**2]*((1<<(k+1))-1)
  check(sum(quotient)==1)
  h0=a.entropy(quotient)
  check(overlap(a.entropy(actual),a.add(h0,a.scale(a.entropy(pf),alpha*T))))
  check(overlap(ce(actual,ref),a.add(h0,a.scale(ce(pf,Q),alpha*T))))
  beta=a.sub(a.const(4*alpha*(k+1)),h0)
  check(beta[0]>0)
  sparse.append({'T':T,'k':k,'bits':nb+k+1,'margin_interval':a.outiv(a.sub(a.const(4*inf(vals)),ce(actual,ref)))})

# Signed algebra with genuinely differing factor accounts; rational exact identities.
for T,k,omega in product(range(1,6),range(4),(F(0),F(1,8),F(1,4))):
 alpha=F(1,2**k);Ss=[F(1+j,1) for j in range(T)];Ms=[F(3+j,2) for j in range(T)]
 beta=F(k+1,7);S=4*alpha+alpha*sum(Ss);M=beta+alpha*sum(Ms)
 net=S-M;J=max(F(0),net)
 check(S-J==min(S,M))
 check(S-J-alpha*T*omega>=alpha*T*(1-omega))
 # Arbitrary booked signed seed net is scaled ONCE, no positive part until aggregation.
 e=sum(Ss)-sum(Ms)-F(9,4);A=F(9,4)
 outerA=alpha*A;outere=4*alpha-beta+alpha*e
 check(outerA+outere==S-M)

out={'status':'PASS','assertions':count,'channel_assertions':a.COUNT,'core_cases':len(records),'frontier_policies':3*len(records),'direct_sparse_cases':sparse,'scalar_cases':60,'arithmetic_seconds':time.monotonic()-start,'arithmetic':'exact Fraction coefficients and rational outward logarithm intervals; no floating signs','analytic_boundary':'Equality floors and all-dimensional implications are proved in PROOF.md, not inferred from interval overlap.'}
(B/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ('status','assertions','channel_assertions','core_cases','frontier_policies','scalar_cases','arithmetic_seconds')}))

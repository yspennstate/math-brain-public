from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
def save(name,x): (R/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
save('out/FROZEN_SPEC.json',dict(helper='audit.py v1',family='all 16 labelled Boolean functions on two uniform bits; independent generic three-atom stochastic maps',domain='three full source laws; both coordinate orders and all four outcomes; generic maps columns from six half-grid simplex vectors, p=0,1/4,1/2,3/4 and r=0,1/2,1',case_count='384 physical paths, 1296 generic map/calibration cases, 576 child shape transports; eight exact parity controls',symmetry='none',arithmetic='Fraction laws and prime-factor symbolic logarithms; no floating signs',memory_estimate_MB=80,max_runtime_seconds=55))
start=time.monotonic(); count=0
def check(b):
 global count
 count+=1
 assert b,count
 assert time.monotonic()-start<55
def cal(s,p):
 if p==1:return [F(1)]+[F(0)]*(len(s)-1)
 assert s[0]<1
 return [p]+[(1-p)*x/(1-s[0]) for x in s[1:]]
def marginal(s,j):
 n=(len(s)-1).bit_length(); out=[F(0)]*(len(s)//2)
 for a,x in enumerate(s):out[(a&((1<<j)-1))|((a>>(j+1))<<j)]+=x
 return out
def spec(t):
 return [F(sum(v*(-1 if (a&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t))**2 for a in range(len(t))]
def restrict(t,j,b):return [t[(x&((1<<j)-1))|(b<<j)|((x>>j)<<(j+1))] for x in range(len(t)//2)]
def logs(x):
 out={}
 for z,sign in [(x.numerator,1),(x.denominator,-1)]:
  d=2
  while d*d<=z:
   while z%d==0:out[d]=out.get(d,0)+sign;z//=d
   d+=1
  if z>1:out[z]=out.get(z,0)+sign
 return {k:F(v) for k,v in out.items() if v}
def add(*terms):
 out={}
 for scale,d in terms:
  for k,v in d.items():out[k]=out.get(k,F(0))+scale*v
 return {k:v for k,v in out.items() if v}
def ce(p,q):return add(*[(-x,logs(y)) for x,y in zip(p,q) if x])
def kl(p,q):return add((1,ce(p,q)),(-1,ce(p,p)))
sources=[[F(1,4)]*4,[F(x,10) for x in [1,2,3,4]],[F(x,10) for x in [4,3,2,1]]]
paths=transports=chains=0
for t in product([-1,1],repeat=4):
 p=spec(t)
 for s in sources:
  for order in permutations(range(2)):
   for bits in product(range(2),repeat=2):
    old=s;raw=s;truth=list(t);labels=[0,1]
    for label,b in zip(order,bits):
     j=labels.index(label); old=cal(old,spec(truth)[0]);old=marginal(old,j);raw=marginal(raw,j)
     truth=restrict(truth,j,b);labels.remove(label)
     check(cal(old,spec(truth)[0])==cal(raw,spec(truth)[0]))
    paths+=1
  for j in range(2):
   v=marginal(s,j); children=[spec(restrict(t,j,b)) for b in range(2)]
   # Parent CE minus child average equals erasure plus fiber KL.
   erasure={};refund={}
   for a in range(2):
    a0=a&((1<<j)-1)|((a>>j)<<(j+1)); a1=a0|(1<<j)
    mass=p[a0]+p[a1]
    if mass:
     pp=[p[a0]/mass,p[a1]/mass]; qq=[s[a0]/v[a],s[a1]/v[a]]
     erasure=add((1,erasure),(mass,ce(pp,pp)))
     refund=add((1,refund),(mass,kl(pp,qq)))
   check(add((1,ce(p,s)),(-F(1,2),ce(children[0],v)),(-F(1,2),ce(children[1],v)),(-1,erasure),(-1,refund))=={})
   chains+=1
   for source in sources:
    ss=marginal(source,j)
    for child in children:
     c=child[0];fresh=cal(ss,c)
     shape={}
     if c<1:
      # One remaining bit has only one nonempty atom: shape is identically zero.
      shape=add(*[(x,logs((v[k]/(1-v[0]))/(ss[k]/(1-ss[0])))) for k,x in enumerate(child) if k and x])
     check(add((1,ce(child,fresh)),(-1,ce(child,v)),(-1,shape),(1,kl([c,1-c],[v[0],1-v[0]])))=={})
     transports+=1
simplex=[[F(a,2),F(b,2),F(2-a-b,2)] for a in range(3) for b in range(3-a)]
generic=0
for a,b in product(simplex,repeat=2):
 def apply(s):return [s[0]*(i==0)+s[1]*a[i]+s[2]*b[i] for i in range(3)]
 for s in [[F(1,3)]*3,[F(1,2),F(1,3),F(1,6)],[F(0),F(1,4),F(3,4)]]:
  for p in [F(0),F(1,4),F(1,2),F(3,4)]:
   for r in [F(0),F(1,2),F(1)]:
    x=apply(cal(s,p));y=apply(s)
    if r<1 and y[0]==1:continue
    check(cal(x,r)==cal(y,r));generic+=1
# Actual Boolean parity2, fixed I=2, covariance=-1: arbitrary full reference
# shape costs cannot be bounded using only these physical-tree quantities.
p=spec([-1,1,1,-1]); q=[F(1,4)]*4
for k in range(2,10):
 eps=F(1,2**k); ss=[F(1,4),F(3,8)*(1-eps),F(3,8)*(1-eps),F(3,4)*eps]
 check(sum(ss)==1)
 check(ce(p,cal(ss,0))=={2:F(k)})
 check(ce(p,cal(q,0))=={3:F(1)})
save('out/VALIDATION.json',dict(status='PASS',exact_assertions=count,physical_paths=paths,generic_cases=generic,query_chain_cases=chains,child_transport_cases=transports,parity_controls=8,runtime_seconds=time.monotonic()-start,scope='independent implementation; no imported peer helper; child transport tests have one nonempty atom and hence zero shape; parity controls exercise changing shape on the original two-bit law'))
print(json.dumps(json.loads((R/'out/VALIDATION.json').read_text())))

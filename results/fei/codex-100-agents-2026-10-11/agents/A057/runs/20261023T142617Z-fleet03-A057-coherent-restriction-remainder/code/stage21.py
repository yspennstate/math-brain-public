from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
R.joinpath('out').mkdir(parents=True,exist_ok=True)
from fractions import Fraction as Q
from functools import lru_cache
import time
def write(p,v): p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
spec={'helper_version':'A057-independent-review-v1','family':'ALL Boolean signs on three uniform bits; exact source F=b-C+C G tag on four paired exterior bits; selected actual cylinder controls','parameter_domain':'256 core truth tables, each of three core queries; source controls all 256 cores at four fixed X histories and three fixed tag histories','case_count':768,'symmetry':'none','arithmetic':'rational Walsh coefficients; exact rational prime-log expressions; rational atanh log bounds with proved tail','memory_estimate_MB':80,'max_runtime_seconds':55,'pilot':'first16 core tables; under60sec','search':'none; independently reproduce a supplied theorem'}
write(R/'SPEC.json',spec)
def add(a,b,k=Q(1)):
 r=dict(a)
 for p,v in b.items():
  r[p]=r.get(p,Q(0))+k*v
  if not r[p]: del r[p]
 return r
def logexpr(q):
 r={}
 for n,s in [(q.numerator,1),(q.denominator,-1)]:
  p=2
  while p*p<=n:
   while n%p==0:r[p]=r.get(p,0)+s;n//=p
   p+=1
  if n>1:r[n]=r.get(n,0)+s
 return {p:Q(v) for p,v in r.items() if v}
def eta(q):return {} if not q else {p:-q*v for p,v in logexpr(q).items()}
@lru_cache(None)
def ln_interval(q):
 z=(q-1)/(q+1); terms=40
 s=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
 return s,s+2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
@lru_cache(None)
def logbounds(p):
 if p==2:return Q(1),Q(1)
 k=p.bit_length()-1; a,b=ln_interval(Q(p,2**k));c,d=ln_interval(Q(2))
 return k+a/d,k+b/c
def bounds(e):
 lo=hi=Q(0)
 for p,v in e.items():
  a,b=logbounds(p);lo+=v*(a if v>=0 else b);hi+=v*(b if v>=0 else a)
 return lo,hi
checks=0
def nonneg(e):
 global checks
 checks+=1
 assert not e or bounds(e)[0]>=0,e
def equal(a,b):
 global checks
 checks+=1;assert not add(a,b,-1)
def walsh(f):
 a=list(f);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
  h*=2
 return [Q(v,len(a)) for v in a]
@lru_cache(None)
def entropy(f):
 r={}
 for x in walsh(f):r=add(r,eta(x*x))
 return r
def restrict(f,i,a):
 return tuple(v for x,v in enumerate(f) if ((x>>i)&1)==a)
def inf(f,i):return Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
def influence(f):return sum((inf(f,i) for i in range(len(f).bit_length()-1)),Q(0))
def debit(f,i):return add(entropy(f),add(entropy(restrict(f,i,0)),entropy(restrict(f,i,1))),-Q(1,2))
def source(g,xhist,tag):
 free=[i for i in range(4) if i not in xhist];a=[]
 for y in range(len(g)):
  for z in ([0,1] if tag is None else [tag]):
   for mask in range(1<<len(free)):
    x=dict(xhist);x.update({j:(mask>>k)&1 for k,j in enumerate(free)})
    b=(-1)**(x[0]*x[1]+x[2]*x[3]);C=int(all(x.values()))
    a.append(b-C+C*g[y]*((-1)**z))
 return tuple(a),len(free)+(tag is None)
def run(limit):
 global checks
 checks=0;start=time.perf_counter();states=0
 for table in range(limit):
  g=tuple(1-2*((table>>x)&1) for x in range(8));Ig=influence(g)
  for i in range(3):
   d=inf(g,i);delta=min(d,1-d);D=debit(g,i)
   # Independent exact isoperimetric lower bound.
   nonneg(add({2:Ig-d},eta(delta),-1))
   # kappa=(3 log2(3)+1)/(log2(3)+1): certify after multiplication.
   prod={}
   # Avoid products of logarithms: use rigorous interval for D and kappa.
   dl,du=bounds(D);elllo,ellhi=logbounds(3)
   kaplo=3-Q(2)/(1+elllo)
   assert du<=kaplo*Ig or not D
   checks+=1
   for a in [0,1]:
    child=restrict(g,i,a)
    # old-prefix released influence is accounted once in conditional mean.
   assert Ig==d+(influence(restrict(g,i,0))+influence(restrict(g,i,1)))/2
   checks+=1
  for xhist in [{},{0:0},{0:1},{0:1,1:1,2:1,3:1}]:
   t=Q(0) if any(v==0 for v in xhist.values()) else Q(1,2**(4-len(xhist)))
   for tag in [None,0,1]:
    f,offset=source(g,xhist,tag);states+=1
    E=add(entropy(f),entropy(g),-t)
    nonneg(E)
    # E <= r+h2(t), irrespective of inaccessible core entropy.
    top=add({2:Q(4-len(xhist))},add(eta(t),eta(1-t)))
    nonneg(add(top,E,-1))
    D=debit(f,offset)
    Eg=[]
    for a in [0,1]:
     gc=restrict(g,0,a);fc,_=source(gc,xhist,tag)
     equal(entropy(fc),entropy(restrict(f,offset,a)))
     Eg.append(add(entropy(fc),entropy(gc),-t))
    rhs=add({p:t*v for p,v in debit(g,0).items()},add(E,add(Eg[0],Eg[1]),-Q(1,2)))
    equal(D,rhs)
  assert time.perf_counter()-start<55,'Frozen runtime cap reached; do not enlarge domain.'
 return {'status':'PASS','core_tables':limit,'universal_core_query_cases':3*limit,'actual_source_states':states,'exact_assertions':checks,'seconds':time.perf_counter()-start,'all_dimensional_claim':'Written independent reconstruction, not extrapolation from these finite cases.'}
import sys
pilot='--pilot' in sys.argv
result=run(16 if pilot else 256)
write(R/'out'/('pilot.json' if pilot else 'validation.json'),result)
print(json.dumps(result))

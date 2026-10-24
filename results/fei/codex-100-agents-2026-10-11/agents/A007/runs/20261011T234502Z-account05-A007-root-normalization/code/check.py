"""Independent A009 review and activated-tribes ledger, version A007-stage2-v1."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import factorial
from functools import lru_cache
import time, json, sys

RUN=Path(__file__).resolve().parents[1]
spec=dict(helper_version='A007-stage2-v1',families=['actual A009 singleton-petal activations','affine-plane monotone DNF','activated tribes m=2^w'],
 parameter_domain={'singleton_review':'r=1..3,m=1..4 (12 cases)','geometry':'prime Q in {2,3,5,7,17,19}; complete Boolean physical boundary census Q=2,3 only',
 'activation':'r=1..3,w=1..2,m=2^w (6 cases,n<=11)','KKT':'one Boolean and three abstract rational certificates','epsilon':'all integers Q=16..128 (113 cases)'},
 case_count={'singleton':12,'geometry':6,'activation':6,'KKT':4,'epsilon':113},symmetry='none except parameterized family symmetry justified analytically',
 arithmetic='integer Walsh; Fraction ledger and physical boundaries; base-two log intervals from rational atanh with 24 terms',
 memory_estimate_bytes=60_000_000,max_runtime_seconds=60,automatic_dimension_escalation=False)
if '--freeze' in sys.argv:
 (RUN/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf8'); print(json.dumps(spec)); raise SystemExit
assert json.loads((RUN/'FROZEN_SPEC.json').read_text())==spec
started=time.perf_counter(); checks=0; run_count=0
def ck(t):
 global checks
 checks+=1
 assert t,checks
def walsh(values):
 a=list(values); h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):
    x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
  h*=2
 return [F(x*(-1 if i.bit_count()%2 else 1),len(a)) for i,x in enumerate(a)]
def influence(values,n):
 return [F(sum(values[x]!=values[x^(1<<j)] for x in range(len(values))),len(values)) for j in range(n)]
def ln_unit(x):
 z=(x-1)/(x+1); k=24
 s=2*sum((z**(2*j+1)/F(2*j+1) for j in range(k)),F(0))
 e=2*z**(2*k+1)/F(2*k+1)/(1-z*z)
 return s,s+e
LN2=ln_unit(F(2))
@lru_cache(None)
def log_bounds(x):
 x=F(x); k=x.numerator.bit_length()-x.denominator.bit_length()
 y=x/(F(2)**k)
 while y<1: k-=1; y*=2
 while y>=2: k+=1; y/=2
 lo,hi=ln_unit(y)
 # y>=1, so ln y>=0; division orientations are exact.
 return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
def add(ledger,x,c):
 x=F(x); ledger[x]=ledger.get(x,F(0))+F(c)
def enclose(ledger):
 lo=hi=F(0)
 for x,c in ledger.items():
  a,b=log_bounds(x)
  lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
 return lo,hi

# KKT, reconstructed root marginal law directly from all nonempty root sets.
kkt=[([F(1,2)]*2,[F(1,4)]*2,F(15,16),[F(17,32)]*2,F(19,272)),
 ([F(1,3),F(2,3)],[F(1,4),F(1,8)],F(3,4),[F(317,300),F(517,300)],F(2)),
 ([F(2,5),F(3,5)],[F(1,8),F(1,2)],F(1,2),[F(941,730),F(1629,730)],F(3)),
 ([F(1,2)]*2,[F(1,4)]*2,F(3,4),[F(61,68)]*2,F(1))]
for lam,pi,v,c,y in kkt:
 x=[a*b for a,b in zip(lam,pi)]; d=(1+x[0])*(1+x[1])-1
 root=[x[0]/d,x[1]/d,x[0]*x[1]/d]
 ck(sum(root)==1); rm=[root[0]+root[2],root[1]+root[2]]
 for l in range(2): ck(c[l]-v*rm[l]==lam[l]*y)
 ck(sum(lam)==1)
ck(-F(1,16)/(1+F(1,16))==-F(1,17)); ck(F(1,4)+F(1,4)<1)

geometries=[]
for q in [2,3,5,7,17,19]:
 lines=[]
 for slope in range(q):
  for intercept in range(q): lines.append(frozenset(x*q+(slope*x+intercept)%q for x in range(q)))
 for x in range(q): lines.append(frozenset(x*q+y for y in range(q)))
 ck(len(set(lines))==q*(q+1))
 for j in range(q*q): ck(sum(j in l for l in lines)==q+1)
 for a,b in combinations(lines,2): ck(len(a&b)<=1)
 boundary=None
 if q<=3:
  masks=[sum(1<<j for j in l) for l in lines]
  truth=[any(x&m==m for m in masks) for x in range(1<<(q*q))]
  alphas=[]
  for j in range(q*q):
   counts=[0]*len(lines); total=0
   for x in range(1<<(q*q)):
    if x&(1<<j): continue
    xp=x|(1<<j)
    if not truth[x] and truth[xp]:
     eligible=[i for i,m in enumerate(masks) if xp&m==m]
     ck(all(j in lines[i] for i in eligible)); total+=1; counts[min(eligible)]+=1
   alphas.append(F(total,1<<(q*q-1)))
   ck(sum(counts)==total)
  ck(len(set(alphas))==1); boundary=str(alphas[0])
 geometries.append(dict(Q=q,lines=len(lines),alpha_exact=boundary))
for q in range(16,129):
 eps=F(q*(q+1),2**(q-1)); ck(eps<F(1,2)); ck(F((q+1)*(q+2),2**q)<eps)
 ck(1/F((q+1)*(1-eps))<=F(2,q+1))
ck((1-F(24,59))*(1+F(11,48))==F(35,48))
ck(F(48,5)*F(35,48)==7)

def family(r,w,m,bound,trace=False):
 global run_count
 p=F(1,2**r); rho=F(1,2**w); q=(1-rho)**m; b=1-q; n=r+m*w
 cm=(1<<r)-1; petals=[((1<<w)-1)<<(r+l*w) for l in range(m)]
 truth=[2*int(x&cm==cm and any(x&z==z for z in petals))-1 for x in range(1<<n)]
 hats=walsh(truth); influence_direct=influence(truth,n); ic=2*r*p*b; idata=2*p*q*m*w*rho/(1-rho)
 ck(sum(influence_direct)==ic+idata)
 ck(sum(z*z for z in hats)==1); v=1-hats[0]**2; ck(v==4*p*b*(1-p*b))
 d=(1+p*rho/F(m))**m-1
 ledger={}; add(ledger,d,v); ek=et=F(0); rank={}; congestion={}; labels={}; cr_use=[F(0)]*m
 for a,amp in enumerate(hats):
  if a==0 or amp==0: continue
  weight=amp*amp; u=(a&cm).bit_count(); touched=[l for l,z in enumerate(petals) if a&z]; t=len(touched)
  ck(amp==(2*p*b if not t else -2*p*F(1) * product_coeff(a,petals,rho)))
  k=1 if u else t; ek+=weight*k; et+=weight*t
  # Root surprisal is exactly r+w per root; posterior entropy accounts only actual traces.
  add(ledger,2,weight*k*(r+w))
  if t:
   add(labels,m,weight*t)
   if u: add(labels,factorial(t),-weight)
  for l in (touched if t else range(m)):
   if t: cr_use[l]+=weight
   else: cr_use[l]+=weight/F(m)
  selected_core=0
  for j in range(r):
   if a&(1<<j):
    add(rank,F(j+1,selected_core+1),weight*F(6,5)); selected_core+=1
  for l in touched:
   s=(a&petals[l]).bit_count(); before=0
   for j in range(w):
    if a&(1<<(r+l*w+j)):
     add(rank,F(r+j+1,u+before+1),weight*F(6,5)); before+=1
   if u: add(congestion,F(u+s,s),weight*F(6,5)*F(t-1,t))
  if trace:
   traces=set()
   roots=touched if t else list(range(m))
   for root in (roots if u else [None]):
    children=[l for l in touched if l!=root]
    orders=permutations(children) if u else [tuple()]
    for order in orders:
     owners={l:a&petals[l] for l in touched}
     if u: owners[root]=owners.get(root,0)|(a&cm)
     ck(sum(x.bit_count() for x in owners.values())==a.bit_count())
     ck(all((x & (cm|petals[l]))==x for l,x in owners.items()))
     if u: ck(all(owners[root]&cm& (cm|petals[l]) for l in children))
     traces.add((root,tuple(sorted(owners.items())),tuple(order)))
   ck(len(traces)==(factorial(t) if u and t else m if u else 1)); run_count+=len(traces)
 for part in [rank,congestion,labels]:
  for x,c in part.items(): add(ledger,x,c)
 ck(ek-v==4*p*p*q*(m*rho-b))
 ck(et==4*p*q*m*rho)
 # Core-only labels were canceled against H(root) in forming labels above.
 lo,hi=enclose(ledger); ck(hi<=bound*(ic+idata))
 if w==1 and r==1 and m==2: ck(cr_use==[F(17,32)]*2)
 return dict(r=r,w=w,m=m,dimension=n,variance=str(v),I_core=str(ic),I_data=str(idata),
             excess_roots=str(ek-v),residual_interval=[str(lo),str(hi)],ratio_upper=str(hi/(ic+idata)),
             approximate_ratio=float(hi/(ic+idata)))
def product_coeff(a,petals,rho):
 result=F(1)
 for mask in petals: result*= -rho if a&mask else 1-rho
 return result

singleton=[family(r,1,m,F(8)) for r in range(1,4) for m in range(1,5)]
tribes=[family(r,w,2**w,F(26,5),True) for r in range(1,4) for w in range(1,3)]
elapsed=time.perf_counter()-started
ck(elapsed<60)
result=dict(helper_version=spec['helper_version'],assertions_passed=checks,elapsed_seconds=elapsed,
            actual_constructed_partition_traces=run_count,geometry=geometries,singleton=singleton,activated_tribes=tribes,
            arithmetic=spec['arithmetic'],proof_of_all_parameter_bounds='REVIEW_A009.md and REPORT.md; finite signs use rational intervals')
(RUN/'out'/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k not in ['singleton','activated_tribes','geometry']}))

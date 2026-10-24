"""Independent Fourier representation and guard reconstruction, no FWHT."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json,time
RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter();checks=0
def ok(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
@lru_cache(None)
def coeffs(t):
 return tuple(Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t)))
def spec(t):return tuple(v*v for v in coeffs(t))
def entropy(p):
 result={}
 for v in p:
  if not v:continue
  for value,sign in [(v.numerator,-v),(v.denominator,v)]:
   divisor=2
   while value>1:
    while value%divisor==0:
     result[divisor]=result.get(divisor,Q(0))+sign;value//=divisor
    divisor+=1
 return {p:c for p,c in result.items() if c}
def combine(terms):
 out={}
 for w,t in terms:
  for p,c in t.items():out[p]=out.get(p,Q(0))+w*c
 return {p:c for p,c in out.items() if c}
def restriction(t,i,b):
 return tuple(v for x,v in enumerate(t) if (x>>i)&1==b)
def restrict_state(st,i,b):
 labels,gs=st;k=len(labels).bit_length()-1
 if i<k:return restriction(labels,i,b),gs
 return labels,tuple(restriction(g,i-k,b) for g in gs)
def full(st):
 labels,gs=st
 return tuple(gs[j][x] for x in range(len(gs[0])) for j in labels)
def js(st):
 labels,gs=st;w=[Q(labels.count(j),len(labels)) for j in range(3)]
 q=tuple(sum(w[j]*spec(gs[j])[t] for j in range(3)) for t in range(len(gs[0])))
 return combine([(1,entropy(q))]+[(-a,entropy(spec(g))) for a,g in zip(w,gs)])
labels=tuple([0]*3+[1]*3+[2]*2)
point3=tuple(1-2*(x==0) for x in range(8))
majority=tuple(1 if x.bit_count()>=2 else -1 for x in range(8))
point2=tuple(1-2*(x%4==0) for x in range(8))
gs=tuple(tuple(g[x]*(1-2*z) for z in range(2) for x in range(8)) for g in [point3,majority,point2])
root=(labels,gs)
for assignment in product((-1,0,1),repeat=7):
 st=root
 for i in range(6,-1,-1):
  if assignment[i]>=0:st=restrict_state(st,i,assignment[i])
 ls,ss=st;k=len(ls).bit_length()-1;t=full(st);P=spec(t)
 w=[Q(ls.count(j),len(ls)) for j in range(3)]
 q=tuple(sum(w[j]*spec(ss[j])[a] for j in range(3)) for a in range(len(ss[0])))
 marginal=tuple(sum(P[(a<<k)+b] for b in range(1<<k)) for a in range(len(ss[0])))
 ok(q==marginal);ok(sum(P)==1)
 for i in range(k):
  spectral=sum(p for a,p in enumerate(P) if (a>>i)&1)
  edges=Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
  gradients=sum(Q(sum((ss[ls[y]][x]-ss[ls[y^(1<<i)]][x])**2 for x in range(len(ss[0]))),4*len(ls)*len(ss[0])) for y in range(len(ls)))
  ok(spectral==edges==gradients)
 if time.perf_counter()-START>55:raise RuntimeError('frozen 55 second limit')
reference=json.loads((RUN/'out/check.json').read_text(encoding='utf-8'))
ok(js(root)=={int(p):Q(c) for p,c in reference['fixture_root']['J'].items()})
first_children=[restrict_state(root,3,b) for b in (0,1)]
debit=combine([(1,js(root))]+[(-Q(1,2),js(s)) for s in first_children])
ok(debit=={int(p):Q(c) for p,c in reference['first_DATA_debit'].items()})
# Isospectral, common-character refund guard. Keep a third duplicate label unused.
left=tuple((1-2*(x==0))*(1-2*z) for z in range(2) for x in range(4))
right=tuple((1-2*(x==1))*(1-2*z) for z in range(2) for x in range(4))
guard=((0,1),(left,right,left));ok(not js(guard))
for b in (0,1):
 child=restrict_state(guard,1,b);ok(js(child)=={2:Q(1)})
 ok(all(len(set(g))==2 for g in child[1]))
 for c in (0,1):ok(not js(restrict_state(child,1,c)))
# Without fresh independent cubes the source mixture is not the actual spectrum.
shared_sources=((1,-1),(-1,1));shared_labels=(0,1)
shared_actual=tuple(shared_sources[shared_labels[x]][x] for x in range(2))
shared_mixture=tuple((spec(shared_sources[0])[i]+spec(shared_sources[1])[i])/2 for i in range(2))
ok(shared_actual==(1,1));ok(spec(shared_actual)!=shared_mixture)
# Auxiliary scalar signs use the already separately tested main interval routine.
import check
and_guard=((0,1),((1,1),(1,-1),(1,1)))
ags=check.stats(and_guard)
ok(ags['J']==check.const(1));ok(ags['L']==check.const(1));ok(ags['H']==check.const(2))
vals=[Q(-2),Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1),Q(2)]
for a,b in product(vals,repeat=2):
 pair=[a*a,b*b];mean=sum(pair)/2
 defect=check.sub(check.atom(mean),check.scale(check.ent(pair),Q(1,2)))
 ok(check.nonnegative(check.sub(check.const(Q(3,4)*(a-b)**2),defect)))
result={'status':'PASS','assertions':checks,'fixture_restrictions':2187,'scalar_pairs':49,'refund_guard':{'root_J':0,'after_first_DATA_J':1,'first_debit':-1,'next_weighted_debit':1,'signed_total':0,'positive_part_total':1,'all_first_source_children_nonconstant':True},'seconds':round(time.perf_counter()-START,6),'independence':'direct character sums and flips; no FWHT or main spectra; only auxiliary scalar interval signs reuse main arithmetic'}
(RUN/'out/independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))

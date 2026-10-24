from pathlib import Path
from fractions import Fraction as F
import json,time,sys
R=Path(__file__).resolve().parents[1];mode=sys.argv[1];assert mode in ('pilot','full')
spec={'helper':'A028-mixed-boundary-bank-v1','family':'same frozen actual controller/shared-core families as entropy check; all physical one-query restrictions',
'domain':'controllers0..1 and shared cores0..1 plus four partially shared core tables in pilot; controllers0..2 and shared cores0..2 plus all16 partially shared tables in full',
'case_count':216 if mode=='pilot' else 11704,'arithmetic':'truth tables, independent directed edge counts, exact Fraction',
'symmetry':'none','memory_estimate_MB':32,'maximum_runtime_seconds':55 if mode=='pilot' else 300,'max_dimension':5,'automatic_escalation':False}
(R/'out'/f'MIXED_BANK_SPEC_{mode}.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.monotonic();checks=0;count=0;queries=0
def ck(q):
 global checks
 assert q;checks+=1
def tables(n):
 for c in range(1<<(1<<n)):yield tuple(-1 if (c>>x)&1 else 1 for x in range(1<<n))
def inf(t):
 return sum((F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(len(t).bit_length()-1)),F(0))
def ii(t,j):return F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t))
def sl(t,j,v):return tuple(t[x] for x in range(len(t)) if ((x>>j)&1)==v)
def case(a,g,h):
 global count,queries
 p=F(a.count(-1),len(a));prod=tuple(x*y for x,y in zip(g,h));IK=inf(prod)
 bank=2*p*(1-p)*IK
 for j in range(len(a).bit_length()-1):
  p0=F(sl(a,j,0).count(-1),len(a)//2);p1=F(sl(a,j,1).count(-1),len(a)//2)
  child=2*p0*(1-p0)*IK/2+2*p1*(1-p1)*IK/2
  ck(bank-child==(p0-p1)**2*IK/2>=0);queries+=1
 for j in range(len(g).bit_length()-1):
  child=0
  for v in [0,1]:
   gv,hv=sl(g,j,v),sl(h,j,v)
   child+=p*(1-p)*inf(tuple(x*y for x,y in zip(gv,hv)))
  release=2*p*(1-p)*ii(prod,j)
  ck(bank-child==release>=0)
  spent=(1-p)*ii(g,j)+p*ii(h,j)
  ck(release<=2*spent);queries+=1
 ck(bank<=2*((1-p)*inf(g)+p*inf(h)))
 count+=1
 if time.monotonic()-start>spec['maximum_runtime_seconds']:raise RuntimeError('frozen cutoff')
for nc in range((1 if mode=='pilot' else 2)+1):
 for a in tables(nc):
  for nd in range((1 if mode=='pilot' else 2)+1):
   for g in tables(nd):
    for h in tables(nd):case(a,g,h)
  cores=[(-1,-1,-1,-1),(1,1,1,1),(1,-1,1,-1),(1,1,-1,-1)] if mode=='pilot' else list(tables(2))
  for g in cores:
   for h in cores:
    gg=tuple(g[z+2*x] for y in range(2) for x in range(2) for z in range(2))
    hh=tuple(h[z+2*y] for y in range(2) for x in range(2) for z in range(2))
    case(a,gg,hh)
ck(count==spec['case_count'])
out={'helper':spec['helper'],'mode':mode,'status':'PASS','cases':count,'one_query_instances':queries,
'assertions_passed':checks,'compute_seconds':time.monotonic()-start,'arithmetic':'independent truth-table edges/Fraction',
'scope':'all-dimensional adaptive telescoping follows from exact local identities in DERIVATION.md'}
(R/'out'/f'mixed_bank_{mode}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

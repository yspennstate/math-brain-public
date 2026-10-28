"""Exhaust the original seven-bit circuit's 3^7 physical restrictions at K=3."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
from itertools import product
import time,json,hashlib
import review as rv

R=Path(__file__).resolve().parents[1]
start=time.perf_counter()
spec={'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'Every physical restriction of literal AND-of-OR(3,2,2)','domain':'all labelled patterns in {fixed0,fixed1,free}^7 at K=3','case_count':2187,'physical_query_rows':5103,'symmetry':'none; memoization only of byte-identical full truth tables, no states omitted','arithmetic':'direct integer characters, exact symbolic prime logs, exact integer comparisons, rational stopping hull0','memory_estimate_MB':90,'maximum_runtime_seconds':55,'dimension_escalation':False}
(R/'out/HULL_FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8',newline='\n')
original=tuple(rv.circuit([rv.point(3),rv.point(2),rv.point(2)]))
@lru_cache(None)
def stat(v):return rv.stats(v)
@lru_cache(None)
def table(pattern):
 free=[j for j,t in enumerate(pattern) if t==2]
 out=[]
 for x in range(1<<len(free)):
  full=sum((t if t!=2 else (x>>free.index(j))&1)<<j for j,t in enumerate(pattern))
  out.append(original[full])
 return tuple(out)
hulls={};queries=0;smallest=None;slacks=[]
patterns=sorted(product(range(3),repeat=7),key=lambda p:p.count(2))
for pattern in patterns:
 vals=table(pattern);s=stat(vals);slack=rv.sub({1:3*s['I']},s['H'])
 sign,cert=rv.integer_sign(slack);rv.ck(sign>=0)
 if s['I']:
  lo,hi=rv.bounds(rv.scale(1/s['I'],s['H']))
  if smallest is None or lo>smallest[0]:smallest=(lo,hi,pattern)
 for local,j in enumerate(k for k,t in enumerate(pattern) if t==2):
  queries+=1;ps=[]
  for outcome in [0,1]:
   p=list(pattern);p[j]=outcome;p=tuple(p);ps.append(p)
   rv.ck(table(p)==tuple(rv.child(list(vals),local,outcome)))
  rv.ck(s['I']-(stat(table(ps[0]))['I']+stat(table(ps[1]))['I'])/2==s['edges'][local])
  rv.ck((hulls[ps[0]]+hulls[ps[1]])/2==0)
 # Immediate stopping deficit (H-3I)_+ and all mean continuation hulls are0.
 hulls[pattern]=F(0)
 if time.perf_counter()-start>55:raise RuntimeError('frozen 55s cap exceeded')
rv.ck(len(hulls)==2187 and queries==5103)
rv.ck(hulls[(2,)*7]==0)
out={'status':'PASS','all_physical_restrictions':len(hulls),'full_query_rows':queries,'root_full_stopping_deficit_hull_K3':'0','all_K_ge3_extension':'Every immediate deficit decreases with K; all descendant hulls stay0 by finite-tree induction.','largest_H_over_I_interval':rv.ar.pretty(smallest[:2]),'largest_ratio_pattern':list(smallest[2]),'unique_full_truth_tables_evaluated':stat.cache_info().currsize,'exact_assertions':rv.checks,'seconds':time.perf_counter()-start,'helper_sha256':spec['helper_sha256'],'conclusion':'This proposed U_K overprotects a Boolean family whose TRUE full stopping deficit hull is already0; it is not unavoidable FEI debt.'}
(R/'out/RESTRICTION_HULL.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['largest_H_over_I_interval']}))

from pathlib import Path
from fractions import Fraction as F
import json,hashlib,time,sys
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[0]/'20261012T010436Z-account05-A018-shared-data-collision-law/code/check_lead.py'
source=OLD.read_text(encoding='utf8');ns={'__file__':str(OLD),'__name__':'arithmetic_only'}
exec(compile(source.split("\nresult={'helper_version'")[0],str(OLD),'exec'),ns)
fw=ns['fw'];entropy=ns['entropy_scaled'];add=ns['ints_add'];grid=ns['grid'];SCALE=ns['SCALE']
k=1 if '--pilot' in sys.argv else 2;L=1<<k;N=2*L;den=N*N
start=time.perf_counter();checks=0;violations=0;indeterminate=0;best=None;witness=None
def ck(v):
 global checks
 checks+=1;assert v
 assert time.perf_counter()-start < (60 if k==1 else 120)
def save(name,obj):(ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf8')
modules=[]
for mask in range(1<<N):
 v=[1-2*((mask>>x)&1) for x in range(N)]
 branches=[[v[z+2*y] for y in range(L)] for z in (0,1)]
 a,b=map(fw,branches)
 w=fw(v);ck(w==[a[t]+b[t] if z==0 else a[t]-b[t] for t in range(L) for z in (0,1)])
 modules.append((v,a,b,entropy(w,k+1)))
for im,(v,a,b,E) in enumerate(modules):
 for jm,(v2,a2,b2,E2) in enumerate(modules):
  w=[a[t]*a2[u]+b[t]*b2[u] if z==0 else a[t]*a2[u]-b[t]*b2[u] for u in range(L) for t in range(L) for z in (0,1)]
  EP=entropy(w,2*k+1)
  excess=add((1,EP),(-(L*L),E),(-(L*L),E2))
  lo,hi=grid(excess)
  # Entropy excess <=1 from the exact shared-label data TC identity.
  ck(hi<=((2*L*L)**2)*ns['ln_grid'](2)[0])
  if lo>0:
   violations+=1
   if best is None or lo>best:
    best=lo;witness={'module_masks':[im,jm],'private_bits_per_module':k,'excess_natural_prime_log_numerator':excess,'probability_denominator':(2*L*L)**2,'excess_natural_interval':[str(lo/(SCALE*(2*L*L)**2)),str(hi/(SCALE*(2*L*L)**2))],'parent_walsh_integers':w}
    if not (ROOT/'out/FIRST_COUNTEREXAMPLE.json').exists():save('FIRST_COUNTEREXAMPLE.json',witness)
  elif hi>0:indeterminate+=1
  # Independently check one representative of each new best by actual truth table and edges.
  if witness and witness['module_masks']==[im,jm]:
   truth=[v[z+2*t]*v2[z+2*u] for u in range(L) for t in range(L) for z in (0,1)]
   ck(fw(truth)==w)
   pden=(2*L*L)**2
   for bit in range(2*k+1):
    ck(sum(q*q for s,q in enumerate(w) if s&(1<<bit))*len(truth)==sum(truth[x]!=truth[x^(1<<bit)] for x in range(len(truth)))*pden)
result={'status':'PASS','helper_version':'A018-shared-separator-product-v3','helper_source_sha256':hashlib.sha256(source.encode()).hexdigest(),'ordered_module_pairs':len(modules)**2,'strict_entropy_subadditivity_violations':violations,'inconclusive_signs':indeterminate,'best_certified_witness':witness,'checks':checks,'elapsed_seconds':time.perf_counter()-start,'note':'Finite counterexample refutes uncorrected shared-selector entropy transfer, not FEI. Universal +1 proof is analytic in REPORT.'}
save('PRODUCT_PILOT.json' if k==1 else 'PRODUCT_CHECK.json',result)
print(json.dumps({key:result[key] for key in ('status','ordered_module_pairs','strict_entropy_subadditivity_violations','inconclusive_signs','checks','elapsed_seconds')},indent=2))

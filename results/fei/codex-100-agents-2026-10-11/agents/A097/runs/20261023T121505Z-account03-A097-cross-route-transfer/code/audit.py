"""Independent direct physical character reproduction; integer floor-class grid."""
from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
spec={'helper_version':'A097-direct-floor-audit-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'actual128-vertex G=a+b*g, g negative at3-bit indices0,7; both64-vertex children; all denominator24 positive coherent seed floors','domain':'one root/two complete children;45 feasible positive tail triples with qdist>=1/3','case_count':{'roots':1,'children':2,'rational_floor_laws':45},'symmetry':'none','arithmetic':'direct integer characters, Fraction, exact probability-ratio weight histogram; integer cubic-product certificate; no approximate logarithms','memory_estimate_MB':30,'max_runtime_seconds':20}
(R/'out/AUDIT_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
def ok(x):
 global checks
 checks+=1
 assert x,checks
 if time.perf_counter()-start>20:raise RuntimeError('20-second audit limit')
def f(v):return tuple(F(sum(a*(-1 if (i&s).bit_count()%2 else 1) for i,a in enumerate(v)),len(v)) for s in range(len(v)))
def p(v):return tuple(x*x for x in f(v))
A=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1);B=tuple(1-x*x for x in A)
h=tuple(-1 if i in (0,7) else 1 for i in range(8));truth=tuple(a+b*z for z in h for a,b in zip(A,B))
pc=p(truth);bc=f(B);ac=f(A);ok(sum(x*x for x in bc)==F(3,8));ok(sum(x>0 for x in pc)<=64)
I=F(sum(truth[i]!=truth[i^(1<<j)] for j in range(7) for i in range(128)),128);ok(I==F(35,16))
histograms=[]
for bit in (0,1):
 child=tuple(a for i,a in enumerate(truth) if i>>4&1==bit);actual=p(child)
 marginal=[]
 for k in range(64):
  i=(k&15)+((k>>4)<<5);ok(pc[i]*pc[i+16]==0);marginal.append(pc[i]+pc[i+16])
 ok(tuple(marginal)==actual)
 seedref=(F(1,4),F(5,24),F(5,24),F(1,3));new=tuple((ac[u]+F(1,2)*bc[u])**2 if t==0 else bc[u]**2*seedref[t] for t in range(4) for u in range(16));ok(sum(new)==1)
 hist={}
 for a,b in zip(actual,new):
  if a:ok(b>0);ratio=a/b;hist[ratio]=hist.get(ratio,F(0))+a
 ok(hist=={F(1):F(23,32),F(3,4):F(3,32),F(6,5):F(3,16)})
 histograms.append({str(k):str(v) for k,v in hist.items()})
 # Equivalent minimal seed law is NOT needed for ordinary inheritance; it is required only for declared admission.
 ok(F(1,4)<F(1,3));ok(F(3,4)*F(6,5)**2==F(27,25));ok(F(27,25)>1);ok(F(27,25)<2)
rows=[]
for k in range(8,17):
 for i in range(1,18-k):
  j=18-k-i;ok(j>0);ok(i*j*k<=200);ok(i*j*k==200 if (i,j,k)==(5,5,8) else i*j*k<200)
  rows.append((i,j,k,i*j*k))
ok(len(rows)==45);ok(F(35,4)-6-F(1,4)-F(3,32)==F(77,32))
result={'status':'PASS','exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'direct_root_influence':str(I),'both_full_child_ratio_weight_histograms':histograms,'delta_bits':'(3/32)log2(27/25)','rational_floor_laws':len(rows),'unique_product_maximizer':'(5,5,8)/24','all_floor_products':rows,'original_bank':'35/4','old_booking':'1/4','remaining_lower_bound':'>77/32','necessity_scope':'Declared coherent fixed-vacuum floor class only; ordinary inherited reference remains valid outside this class'}
(R/'out/INDEPENDENT_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','exact_assertions','runtime_seconds','rational_floor_laws']}))

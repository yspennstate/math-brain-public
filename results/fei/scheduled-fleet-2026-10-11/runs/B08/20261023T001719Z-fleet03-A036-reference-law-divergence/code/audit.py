from pathlib import Path
from fractions import Fraction as F
import itertools,json,time
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter()
spec={'helper':'independent literal adaptive variance audit v1','actual_family':'two width-three disjoint point defects','domain':'all first-query coordinates, both adaptive second-coordinate choices among the other five','case_count':150,'symmetry':'none labelled','arithmetic':'literal physical values and Fraction conditional means/variances','memory_estimate_mb':20,'max_runtime_seconds':30}
(ROOT/'out'/'AUDIT_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
X=list(range(64));values=[[1-2*((x&7)==7) for x in X],[1-2*(((x>>3)&7)==7) for x in X]]
def variance(indices,j):
 mu=F(sum(values[j][x] for x in indices),len(indices));return 1-mu*mu
initial=sum(variance(X,j) for j in (0,1));cases=0;strict=0
for first in range(6):
 others=[j for j in range(6) if j!=first]
 for second0,second1 in itertools.product(others,repeat=2):
  after=F(0)
  for b in (0,1):
   second=second0 if b==0 else second1
   for c in (0,1):
    cell=[x for x in X if ((x>>first)&1)==b and ((x>>second)&1)==c]
    after+=F(len(cell),64)*sum(variance(cell,j) for j in (0,1))
  assert after<=initial;strict+=after<initial;cases+=1
  assert time.perf_counter()-start<30
assert cases==150
assert 8**5<2*7**5
# Width-zero, width-one, and biased width-two activation references including
# source zeros: exact normalization and KL sector multipliers are algebraic.
boundaries=[]
for w in range(4):
 n=1<<w;delta=F(1,n)
 p=([F(1)] if w==0 else [(1-2*delta)**2]+[4*delta*delta]*(n-1))
 q=p[:] if w<=1 else [p[0]]+[F(7,8)*a for a in p[1:]]
 if w>=2:q[-1]+=(1-p[0])/8
 for sign in (-1,1):
  mu=sign if w==0 else sign*(1-2*delta)
  for eps in (-1,1):
   src=[(eps+mu)**2/4,(eps-mu)**2/4]
   ref=src[:]
   for s in range(1,n):src.extend([p[s]/4]*2);ref.extend([q[s]/4]*2)
   assert sum(src)==sum(ref)==1
   for s in range(1,n):
    if p[s]:assert src[2*s]/ref[2*s]==p[s]/q[s]
   boundaries.append({'width':w,'core_sign':sign,'control_sign':eps,'mass':'1'})
out={'status':'PASS','adaptive_policies':cases,'strict_variance_contractions':strict,'initial_sum_variances':str(initial),'activation_endpoint_cases':len(boundaries),'literal_sample_space':64,'seconds':time.perf_counter()-start,'independent_of_walsh_and_interval_helper':True}
(ROOT/'out'/'AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))

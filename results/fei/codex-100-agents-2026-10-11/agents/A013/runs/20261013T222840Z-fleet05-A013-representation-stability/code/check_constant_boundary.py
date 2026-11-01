from pathlib import Path
from fractions import Fraction as F
from itertools import product
import time,json
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;cases=constant=zero_literal=0
def check(b):
 global checks
 checks+=1
 if time.perf_counter()-start>50:raise RuntimeError('50 second internal cutoff')
 if not b:raise AssertionError(checks)
tables=[[1 if m>>x&1 else -1 for x in range(4)] for m in range(16)]
for g in tables:
 for h in tables:
  gates=[]
  for v in range(4):
   if g[v]==1:gates.append({0:v&1,1:v>>1,3:0})
   if h[v]==1:gates.append({0:v&1,2:v>>1,3:1})
  for hist in product([-1,0,1],repeat=4):
   fixed={j:v for j,v in enumerate(hist) if v>=0};free=[j for j in range(4) if hist[j]<0]
   retained=[]
   for gate in gates:
    if any(j in fixed and fixed[j]!=v for j,v in gate.items()):continue
    child={j:v for j,v in gate.items() if j not in fixed};removed=len(gate)-len(child)
    check(F(1,1<<len(child))==F(1,8)*(1<<removed));retained.append(child)
   truth=[]
   for bits in product([0,1],repeat=len(free)):
    values=dict(fixed);values.update(zip(free,bits));x=sum(v<<j for j,v in values.items())
    f=g[x&3] if values[3]==0 else h[(x&1)|(((x>>2)&1)<<1)]
    cover=any(all(values[j]==v for j,v in gate.items()) for gate in retained)
    check(cover==(f==1));truth.append(f)
   is_constant=len(set(truth))==1
   if any(not gate for gate in retained):check(is_constant and truth[0]==1);zero_literal+=1
   if not retained:check(is_constant and truth[0]==-1)
   if is_constant:constant+=1;check(F(1)==1)
   else:
    nc=len(retained);check(nc>0)
    for gate in retained:
     check(len(gate)>0);density=F(1,1<<len(gate));pi=min(density,F(1,2));check(pi==density)
     odds=pi/nc;check(odds/(1+odds)==pi/(nc+pi))
   cases+=1
result={'helper':'A013-cell-cover-full-history-v1','status':'PASS','partial_assignment_cases':cases,'constant_children':constant,'zero_literal_histories':zero_literal,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start}
(R/'out/CONSTANT_BOUNDARY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

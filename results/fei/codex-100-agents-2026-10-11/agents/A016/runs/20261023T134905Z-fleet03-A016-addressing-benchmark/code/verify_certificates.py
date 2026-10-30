from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();count=0
def ck(x,msg):
 global count
 assert x,msg
 count+=1
 assert time.perf_counter()-start<60,'frozen runtime'
def E(x):
 a,b,c,d,e=[(x>>i)&1 for i in range(5)]
 return (1-2*int(a==b==c==0))*(1-2*int(a==d==e==0))
def direct(values):
 n=len(values);return [F(sum(v*(-1 if (s&t).bit_count()%2 else 1) for s,v in enumerate(values))**2,n*n) for t in range(n)]
orig=direct([E(x) for x in range(32)])
data=json.loads((R/'out/BLOCK_CHECK.json').read_text(encoding='utf-8'))
ck(len(data['rows'])==243,'all3^5 rows present')
ck({tuple(x['assignment']) for x in data['rows']}==set(product([-1,0,1],repeat=5)),'no missing physical partial assignment')
counter=[]
for row in data['rows']:
 raw=row['assignment'];fixed={i:v for i,v in enumerate(raw) if v!=-1};unfixed=[i for i in range(5) if i not in fixed]
 def value(y,rem):return E(sum(v<<i for i,v in fixed.items())+sum(((y>>j)&1)<<i for j,i in enumerate(rem)))
 restricted=[value(y,unfixed) for y in range(1<<len(unfixed))]
 ess=[i for j,i in enumerate(unfixed) if any(restricted[x]!=restricted[x^(1<<j)] for x in range(len(restricted)))]
 ck(ess==row['essential'],'independent literal essential-coordinate reconstruction')
 vals=[value(y,ess) for y in range(1<<len(ess))]
 ck(vals==row['values'],'direct actual cleaned truth')
 P=direct(vals);Q=[]
 for t in range(1<<len(ess)):
  Q.append(sum((orig[s] for s in range(32) if all(((s>>i)&1)==((t>>j)&1) for j,i in enumerate(ess))),F(0)))
 ck(P==list(map(F,row['P'])) and Q==list(map(F,row['Q'])),'independent direct characters and ORIGINAL marginal')
 I=F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals)) for j in range(len(ess))),len(vals))
 ck(I==F(row['I']),'independent actual physical influence')
 D=len(vals)**2;power=4*I*D;ck(power.denominator==1,'integral cleared influence')
 lhs=1<<int(power);rhs=1
 for pp,qq in zip(P,Q):
  ex=pp*D;ck(ex.denominator==1 and (not ex or qq>0),'supported integral spectrum')
  lhs*=qq.numerator**int(ex);rhs*=qq.denominator**int(ex)
 ck(lhs==int(row['integer_certificate']['lhs']) and rhs==int(row['integer_certificate']['rhs']),'saved integer certificate independently regenerated')
 ck(lhs>=rhs,'integer inequality independently verified')
 delta=Q[0]-F(sum(vals),len(vals))**2
 ck(delta==F(row['R0_minus_mean_squared']),'vacuum-shortcut counterexample audit')
 if delta<0:counter.append({'assignment':raw,'R0':str(Q[0]),'mean':str(F(sum(vals),len(vals))),'difference':str(delta)})
res={'status':'PASS','assertions':count,'rows':243,'seconds':time.perf_counter()-start,'independence':'direct characters/physical edges/integer products; no original helper import','vacuum_shortcut_counterexamples':counter}
(R/'out/INDEPENDENT_INTEGER_CHECK.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:res[k] for k in ['status','rows','assertions','seconds']}))

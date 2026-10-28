from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0
P=R.parents[2]/'A048/runs/20261023T063715Z-account03-A048-tensor-stress/out/FACTOR_CERTIFICATE.json'
def ck(v):
 global COUNT
 assert v;COUNT+=1
 if time.perf_counter()-START>55:raise TimeoutError('frozen55s')
d=json.loads(P.read_text(encoding='utf-8'));seen=set();minimum=None
for row in d['rows']:
 n=row['n'];t=tuple(row['values']);ck(len(t)==1<<n);ck((n,t) not in seen);seen.add((n,t))
 p=[]
 for s in range(1<<n):
  v=sum(x*(-1 if (s&z).bit_count()%2 else 1) for z,x in enumerate(t));p.append(F(v*v,(1<<n)**2))
 I=sum((F(sum(t[z]!=t[z^(1<<j)] for z in range(len(t))),len(t)) for j in range(n)),F(0))
 weights={F(0):F(0),F(1):F(0),F(1,16):F(1,4),F(1,4):F(1,2),F(9,16):F(15,32)}
 ck(all(v in weights for v in p));Hup=sum((weights[v] for v in p),F(0));variance=1-p[0];slack=4*I-Hup-F(7,4)*variance
 ck(slack>=0);ck([str(v) for v in p]==row['spectrum']);ck(I==F(row['I']));ck(variance==F(row['variance']));ck(Hup==F(row['H_upper']));ck(slack==F(row['slack']))
 if I:minimum=slack if minimum is None else min(minimum,slack)
ck(len(seen)==278);ck(all(sum(k==n for k,t in seen)==1<<(1<<n) for n in range(4)));ck(minimum==F(1,64));ck(3**12>2**19);ck(6**15<2**4*5**15);ck(7**6<2**17);ck(F(319,192)>F(407,256))
out={'status':'PASS','cases':278,'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'scope':'independent literal character sums and directed physical edges recompute every supplied row/completeness/entropy rational envelope; no producer import','minimum_nonconstant_rational_slack':str(minimum),'five_reset_budget':'6log2(6/5)<8/5<7/4 by exact6^15<2^4*5^15','fourbit_boundary':'7^6<2^17 and319/192>407/256'}
(R/'out/CERTIFICATE_REVIEW.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'));print(json.dumps(out))

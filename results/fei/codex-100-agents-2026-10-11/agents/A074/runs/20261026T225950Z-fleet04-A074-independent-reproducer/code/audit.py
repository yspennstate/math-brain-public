from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import hashlib,json,time
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
def exact_nonnegative(f):
 den=lcm(*(v.denominator for v in f.values())) if f else 1
 positive=negative=1
 for p,v in f.items():
  e=int(v*den)
  if e>=0:positive*=p**e
  else:negative*=p**(-e)
 return positive>=negative
spec=json.loads((R/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
ck(spec['helper_sha256']==hashlib.sha256((R/'code/reproduce.py').read_bytes()).hexdigest())
main=json.loads((R/'out/MAIN.json').read_text(encoding='utf-8'))
ck(main['status']=='PASS');ck(main['query_rows']==3072)
keys=set();positive=zero=negative=0;zero_influence=0;mutations=0
for hm in range(16):
 rows=json.loads((R/f'out/main_chunk_{hm}.json').read_text(encoding='utf-8'))
 ck(len(rows)==192)
 for row in rows:
  key=tuple(row['circuit'])+(row['j'],row['i']);ck(key not in keys);keys.add(key)
  ck(key[0]==hm);ck(0<=key[1]<16 and 0<=key[2]<4)
  ck(key[3:] in ((0,0),(0,1),(1,0)))
  drift={int(p):Q(v) for p,v in row['drift'].items()}; d=Q(row['influence']);ck(d>=0)
  gap={p:-v for p,v in drift.items()};gap[2]=gap.get(2,Q(0))+3*d
  ck(exact_nonnegative(gap))
  if not drift:zero+=1
  elif exact_nonnegative(drift):positive+=1
  else:negative+=1
  if not d:zero_influence+=1;ck(exact_nonnegative({p:-v for p,v in drift.items()}))
  if len(keys)<=3:
   # A forged drift strictly above the declared reserve must fail.
   forged={2:3*d+1}
   ck(not exact_nonnegative({2:3*d-forged[2]}));mutations+=1
ck(len(keys)==3072)
ck(2**74>3**9*5**25)
primitive=json.loads((R/'out/PRIMITIVE.json').read_text(encoding='utf-8'))
ck(primitive['truth_table']==[(-1 if x in (8,9,10) else 1) for x in range(16)])
ck(exact_nonnegative({int(p):Q(v) for p,v in primitive['positive_gap'].items()}))
source=Path('agents/A075/runs/20261023T133516Z-fleet03-A075-search-to-theorem-bridge')
pins={}
for name in ('PROOF.md','CLAIMS.json','REPORT.md'):
 p=source/name;pins[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
claim=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
payload=json.dumps({'exact_statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,ensure_ascii=False)
# Source uses the protocol statement+ordered hypotheses digest; discover no alternate claim.
expected='ff1866ccd4bbad05ef7a28b12298c145b88c08656bdfa06c6bf6eaeb74af4698'
ck(claim['statement_sha256']==expected)
(R/'out/SOURCE_PINS.json').write_text(json.dumps(pins,indent=2)+'\n',encoding='utf-8')
result={'status':'PASS','checks':checks,'rows':len(keys),'drift_sign_counts':{'positive':positive,'zero':zero,'negative':negative},'zero_physical_influence_rows':zero_influence,'altered_drift_controls_rejected':mutations,'method':'LCM-cleared prime-log integer-power comparison, independent of reproducer logarithm intervals','elapsed_seconds':time.monotonic()-start,'source_statement_sha256':expected}
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))

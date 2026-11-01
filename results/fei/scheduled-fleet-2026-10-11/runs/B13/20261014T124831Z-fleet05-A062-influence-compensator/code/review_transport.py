from pathlib import Path
from fractions import Fraction as F
import json,time
run=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=queries=0
def eq(a,b):
 global assertions
 assert a==b,(a,b)
 assertions+=1
def mean(v): return F(sum(v),len(v))
cores=[tuple(1 if mask>>x&1 else -1 for x in range(4)) for mask in range(16)]
for u in cores:
 for v in cores:
  U=tuple(u[x&3] for x in range(16)); V=tuple(v[x>>2] for x in range(16))
  delta=F(sum(a!=b for a,b in zip(U,V)),16)
  eq(delta,(1-mean(u)*mean(v))/2)
  for i in range(4):
   children=[]
   for s in (0,1):
    a=tuple(U[x] for x in range(16) if x>>i&1==s)
    b=tuple(V[x] for x in range(16) if x>>i&1==s)
    d=F(sum(x!=y for x,y in zip(a,b)),8)
    eq(d,(1-mean(a)*mean(b))/2)
    # The unqueried block has its original mean, independently of outcome.
    eq(mean(b) if i<2 else mean(a),mean(v) if i<2 else mean(u))
    children.append(d)
   eq(delta,sum(children)/2)
   # A fixed inherited own-history reserve is consequently harmonic.
   r=F(7,3)
   eq(delta*r,sum(d*r for d in children)/2)
   queries+=1
out={'reviewer':'A062','claim_id':'A030-CONDITIONAL-TWO-CORE-CONTROLLER-TRANSFER','version':1,'scope':'actual independent-core mismatch coefficient and its martingale transport under one-block data queries; fixed inherited controller reserve only','verdict':'HOLDS_AT_STATED_SCOPE','bundled_claim_accepted':False,'core_pairs':256,'query_cases':queries,'assertions':assertions,'failures':0,'runtime_seconds':time.perf_counter()-start}
(run/'out/TRANSPORT_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

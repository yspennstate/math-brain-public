from pathlib import Path
from fractions import Fraction as F
import json,time
import check as C
R=Path(__file__).resolve().parents[1]
for n in range(3):
 N=1<<n
 for table in range(1<<N):
  f=tuple(1 if table&(1<<x) else -1 for x in range(N));p=C.E.spec(f)
  for b in [F(1),F(1,64)]:
   cs=((1-b)/2,(1-b)/2);ws=(0,N-1)
   q=tuple(b*p[u]+sum(c for c,w in zip(cs,ws) if w==u) for u in range(N))
   for j in range(n):
    for mode in [0,1]:C.query(f,q,b,cs,ws,j,mode)
f=(1,1,1,1);p=C.E.spec(f);b=F(1,2);q=(b,F(0),1-b,F(0))
out,B,rel,klrel,do=C.query(f,q,b,(1-b,),(2,),0,1)
C.ck(bool(do));C.nonneg(do)
A=C.E.kl(p,q);children=C.E.sc(F(1,2),C.E.add(*(C.E.kl(C.E.spec(x[0]),x[1]) for x in out)))
C.ck(A!=children)
obj=dict(status='PASS',boundary_queries=C.queries,exact_assertions=C.count,seconds=time.monotonic()-C.START,missing_outcome_KL_negative_control='literal KL equality without D_out rejected on constant2/ghost input',formal_status='RUNTIME_UNVERIFIED; no Lean acceptance')
(R/'out/BOUNDARY_VALIDATION.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
print(json.dumps(obj))

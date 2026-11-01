"""Exact finite audit of the universal-family polynomial debt coefficient."""
from pathlib import Path
from fractions import Fraction as Q
import time,json
r=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0; rows=[]
for C in range(65):
    m=8*C+4; t=m; k=m//2; z=m-k; delta=Q(1,1<<m)
    slope=z*(z-1)-C*m
    assert slope>0; checks+=1
    for L in [1,2,8,64]:
        budget_upper=C*delta*(L*m+t)
        bill_lower=delta*L*z*(z-1)
        debt_lower=delta*(L*slope-C*t)
        assert bill_lower-budget_upper==debt_lower; checks+=1
        assert debt_lower>0; checks+=1
        rows.append({'C':C,'m':m,'L':L,'exact_unpaid_lower':str(debt_lower)})
assert time.perf_counter()-start<10
out={'status':'PASS','assertions':checks,'rows':len(rows),'seconds':time.perf_counter()-start,
     'scope':'polynomial all-L coefficient audit; analytic Boolean family is in PROOF section9',
     'cases':rows}
(r/'out/AMPLIFICATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='cases'}))

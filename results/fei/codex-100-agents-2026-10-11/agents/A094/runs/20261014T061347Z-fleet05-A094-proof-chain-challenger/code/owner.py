from pathlib import Path
from fractions import Fraction as F
import json,time
run=Path(__file__).resolve().parents[1];start=time.perf_counter();src=json.loads((run/'out/INCOMING_SHOCK_CERTIFICATE.json').read_text());rows=[]
for row in src['rows']:
    n=row['n'];t=F(row['t']);d=1-t;bill=1+10*(n+1)*t
    assert d>=F(3,4)
    assert bill<=F(34,3)*d
    rows.append({'n':n,'query_influence':str(d),'source_bound_full_root_bill':str(bill),'owned_query_budget':str(F(34,3)*d)})
out={'status':'PASS','assertions':2*len(rows),'runtime_seconds':time.perf_counter()-start,'rows':rows,'analytic_all_n_reason':'(n+1)2^-n decreases from3/4 atn2, query influence>=3/4. Full inherited child+innovation ledger equals rootCE, not renewed descendant cost.'}
(run/'out/OWNER_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

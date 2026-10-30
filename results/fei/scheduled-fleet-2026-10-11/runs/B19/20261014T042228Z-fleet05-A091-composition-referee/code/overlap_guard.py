import audit as a
import exact as e
from exact import Q,check
from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv
rows=[]
for n in range(2 if pilot else 3):
    for mask in range(1<<(1<<n)):
        h=e.tab(mask,n);mu=a.mean(h);p=Q(1,2);b=Q(1,2);nu=1-b*(1-mu)
        # Three private controllers: A is a two-bit point, B a one-bit point.
        # Both selected output descriptions use ONE actual h data block.
        F=tuple(h[x>>3] if (x%4==0 or (x>>2)&1==0) else 1 for x in range(1<<(3+n)))
        P=a.spec(F)[1];actual=sum(v for s,v in enumerate(P) if s&1)
        edges=Q(sum(F[x]!=F[x^1] for x in range(len(F))),len(F));check(actual,edges)
        check(actual,p*(1-b)*(1-mu)/2)
        independent=p*(1-mu*nu)/2;check(independent-actual,p*b*(1-mu*mu)/2)
        if 1-mu*mu:assert independent>actual
        else:check(independent,actual)
        rows.append({'n':n,'mask':mask,'mean':str(mu),'actual_query_influence':str(actual),'independent_copy_estimate':str(independent),'exact_excess':str(independent-actual)})
assert time.perf_counter()-start<55
out={'status':'PASS','pilot':pilot,'cases':len(rows),'strict_nonconstant_scope_guards':sum(Q(x['exact_excess'])>0 for x in rows),'constant_endpoints':sum(Q(x['exact_excess'])==0 for x in rows),'exact_assertions':e.COUNT,'runtime_seconds':time.perf_counter()-start,'scope':'Product-of-means override equality is false for shared physical data; no FEI disproof and no refutation of the disjoint-data theorem','required_core_merge':'Both selected descriptions are h on the SAME cube; selector is the union A OR B, not two independent data labels','rows':rows}
(R/'out'/('OVERLAP_PILOT.json' if pilot else 'OVERLAP_GUARD.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

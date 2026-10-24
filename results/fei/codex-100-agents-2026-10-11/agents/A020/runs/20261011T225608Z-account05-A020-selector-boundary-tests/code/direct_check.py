"""Independent O(N^2) Fourier reconstruction of the 32 named fixtures."""
from verify import ROOT, table, Q
import json,time
started=time.perf_counter();d=json.loads((ROOT/'out'/'fixtures.json').read_text());checks=0
for r in d['named_fixtures']:
    a,m=r['a'],r['m'];v=table(r['mask'],a+m);N=len(v)
    w=[sum(v[x]*(-1)**((x&t).bit_count()) for x in range(N)) for t in range(N)]
    assert w==r['ledger']['walsh'];checks+=N
    for i in range(a+m):
        influence=Q(sum(v[x]!=v[x^(1<<i)] for x in range(N)),N)
        assert influence==Q(r['ledger']['influences'][i]);checks+=1
out=dict(status='PASS',named_tables=32,exact_assertions=checks,runtime_seconds=time.perf_counter()-started,method='direct character sum, physical disagreeing edge count; no FWHT')
(ROOT/'out'/'direct_check.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))

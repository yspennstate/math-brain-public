"""Persisted equivalent of the executed independent inline bitset checker."""
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter()
f=json.loads((R/'out/boolean_counterexample.json').read_text(encoding='utf-8'))['truth_table']
fm=sum(int(v<0)<<i for i,v in enumerate(f))
edges=[(i,j) for i in range(6) for j in range(i+1,6)]
mon=[sum(int((x>>i&1) and (x>>j&1))<<x for x in range(64)) for i,j in edges]
lin=[sum(((x&s).bit_count()%2)<<x for x in range(64)) for s in range(64)]
qm=[0]*32768;best=polar=64;checks=0
for a in range(32768):
    if a:
        low=a&-a;qm[a]=qm[a^low]^mon[low.bit_length()-1]
    v=qm[a]^fm
    for l in lin:
        u=(v^l).bit_count();d=min(u,64-u);best=min(best,d)
        if a&31:polar=min(polar,d)
        checks+=1
assert (best,polar)==(12,14)
print(json.dumps({'status':'PASS','case_count':checks,'nearest_quadratic':best,'nearest_selected_polar_quadratic':polar,'elapsed_seconds':time.perf_counter()-start}))

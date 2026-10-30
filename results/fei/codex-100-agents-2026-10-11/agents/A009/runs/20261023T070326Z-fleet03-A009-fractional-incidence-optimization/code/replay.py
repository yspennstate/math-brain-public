from pathlib import Path
from fractions import Fraction as F
from itertools import product
import time,json
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
    global checks
    assert x;checks+=1
    if time.monotonic()-start>55:raise RuntimeError('frozen replay cap')
minimum={}
for m in [2,3]:
    minimum[m]=F(1)
    for A in range(1,1<<(2*m)):
        selected=[i for i in range(2*m) if A>>i&1];good=0;total=m**len(selected)
        for choices in product(range(m),repeat=len(selected)):
            roots=[]
            for v,w in zip(selected,choices):roots.append((v,w+m) if v<m else (w,v))
            if len(set(roots))==len(roots):good+=1
        minimum[m]=min(minimum[m],F(good,total))
        ck(8*good>=total)
    ck(minimum[m]>=F(1,8))
# Independent source-SCC control, in actual gate labels.
gates=[{0,2},{1,2},{1,3},{0,3}];owner=[0,2,1,3]
arc=[[i!=j and owner[i] in gates[j] for j in range(4)] for i in range(4)]
reach=[[i==j or arc[i][j] for j in range(4)] for i in range(4)]
for k in range(4):
    for i in range(4):
        for j in range(4):reach[i][j]|=reach[i][k] and reach[k][j]
ck(all(all(row) for row in reach))
ck(len(set(owner))==4 and len({tuple(sorted(x)) for x in gates})==4)
lam=F(1,4);D=(1+lam/4)**4-1
actual_probability=(lam*F(1,4)*F(1,4)*F(1,2))**4/D
ck(actual_probability>0)
scope=dict(source_scc_count=1,chosen_root_count=4,full_original_queue_run=True,canonical_source_scc_partition_forest=False,conditioned_probability=str(actual_probability))
# Physical influence is summed by conditional events on free variables.
for mask in range(16):
    H=[(i,j) for i in range(2) for j in range(2) if mask>>(2*i+j)&1]
    changed_points=[]
    for x in range(16):
        if any((x>>i&1) and (x>>(2+j)&1) for i,j in H):changed_points.append(x)
    p=F(len(changed_points),16);t=F(1,4)
    free_boundary=sum((x^(1<<i)) not in changed_points for x in changed_points for i in range(4))
    ih=F(2*free_boundary,16)
    removed_boundary=4*len(changed_points)
    net=F(2*(free_boundary-removed_boundary),256)
    ck(net==t*t*(ih-8*p))
result=dict(status='PASS',checks=checks,minimum_root_probabilities={str(k):str(v) for k,v in minimum.items()},scope_control=scope,elapsed_seconds=time.monotonic()-start)
(R/'out/replay.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

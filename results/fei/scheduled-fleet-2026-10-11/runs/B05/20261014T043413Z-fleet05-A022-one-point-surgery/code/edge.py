from pathlib import Path
from fractions import Fraction as Q
import json,time
RUN=Path(__file__).resolve().parents[1]
rows=json.loads((RUN/'out/full_CASES.json').read_text())
assert len(rows)==12
START=time.perf_counter(); checks=0; receipts=[]
for row in rows:
    k=row['k']; D=row['vertices']; masks=row['controller_masks'];N=1<<(k+2)
    lookup=dict(zip(D,masks))
    base=[]
    for x in range(1<<k):
        parity=sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(k//2))%2
        base.append(1-2*parity)
    f=tuple(base[x]*(1-2*((lookup.get(x,0)>>z)&1)) for z in range(4) for x in range(1<<k))
    inf=[]
    for i in range(k+2):
        step=1<<i
        edges=sum(f[x]!=f[x+step] for start in range(0,N,2*step) for x in range(start,start+step))
        inf.append(Q(2*edges,N))
    observed={'I_data':sum(inf[:k]),'I_controller':sum(inf[k:]),'I_access':sum(inf[:k:2]),'I_terminal_data':sum(inf[1:k:2])}
    for key,value in observed.items():
        assert value==Q(row[key]);checks+=1
    expected=sum(Q(sum(((mask>>z)&1)!=((mask>>(z^(1<<i)))&1) for z in range(4)),4) for mask in masks for i in range(2))/(1<<k)
    assert expected==sum(inf[k:]);checks+=1
    receipts.append({'case':row['case'],'influences_natural_order':list(map(str,inf))})
    assert time.perf_counter()-START<1800
result={'verdict':'PASS','cases':len(rows),'checks':checks,'runtime_seconds':time.perf_counter()-START,'method':'natural-coordinate direct Boolean edges; no Walsh or logarithm code','receipts':receipts}
(RUN/'out/EDGE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='receipts'}))

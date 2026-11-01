from pathlib import Path
from fractions import Fraction as F
import json,time
import verify_absorption as h
R=Path(__file__).resolve().parents[1]
frozen=json.loads((R/'FROZEN_TRANSPORT.json').read_text(encoding='utf-8'))
start=time.perf_counter();counts={'cases':0,'positive_transport':0,'negative_transport':0,'constant_children':0}
for mask in range(256):
    f=[1 if mask>>x&1 else -1 for x in range(8)]
    for bit in [0,1]:
        p=h.spec(h.restrict(f,0,bit));v=[F(1,4)]*4;s=[F(x,10) for x in range(1,5)]
        fresh=h.cal(s,p[0]);actual=h.sub(h.ce(p,fresh),h.ce(p,v))
        transport=(F(0),F(0))
        for t in range(1,4):
            if p[t]:transport=h.add(transport,h.mul(p[t],h.log((v[t]/(1-v[0]))/(s[t]/(1-s[0])))))
        binary=(F(0),F(0))
        for a,b in [(p[0],v[0]),(1-p[0],1-v[0])]:
            if a:binary=h.add(binary,h.mul(a,h.log(a/b)))
        predicted=h.sub(transport,binary)
        h.ck(max(actual[0],predicted[0])<=min(actual[1],predicted[1]))
        h.ck(h.cal(v,p[0])==h.cal(h.cal(v,F(1,2)),p[0]))
        counts['cases']+=1
        if transport[0]>0:counts['positive_transport']+=1
        if transport[1]<0:counts['negative_transport']+=1
        if p[0]==1:counts['constant_children']+=1
h.ck(counts['cases']==frozen['case_count']);h.ck(counts['positive_transport']>0);h.ck(counts['negative_transport']>0)
out={'status':'EXACT_PASS','counts':counts,'assertions':h.ASSERTS,'runtime_seconds':time.perf_counter()-start,'scope':'exact finite decomposition checks; universal formula proved in MINIMAL_TARGET.md; no universal transport-budget bound proved'}
(R/'out/TRANSPORT_VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))

from pathlib import Path
from collections import Counter
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();counts=Counter();violations=[]
chars=[[1-2*((s&x).bit_count()%2) for x in range(8)] for s in range(8)]
for k in range(390625):
    h=[];d=k
    for _ in range(8):h.append(d%5-2);d//=5
    z=[sum(a*b for a,b in zip(h,c))**2 for c in chars];total=sum(z)
    if total==0:continue
    marg=[sum(z[s] for s in range(8) if s&(1<<i)) for i in range(3)]
    good=True
    for s in range(8):
        p=1
        for i in range(3):p*=marg[i] if s&(1<<i) else total-marg[i]
        if p!=z[s]*total**2:good=False;break
    if not good:continue
    N=sum(0<v<total and 2*v!=total for v in marg);m=sum(2*v==total for v in marg)
    counts[(N,m)]+=1
    if N>=2:violations.append(h)
expected=json.loads((R/'out'/'three_endpoint.json').read_text(encoding='utf-8'))
rows=[{'N':n,'fair':f,'count':v} for (n,f),v in sorted(counts.items())]
assert not violations and rows==expected['counts'];assert sum(counts.values())==2208
out={'result':'PASS','case_count':390625,'independent_product_count':sum(counts.values()),'histogram_matches':True,'rows_with_two_nonfair':0,'runtime_seconds':time.perf_counter()-start}
(R/'out'/'independent_three.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))

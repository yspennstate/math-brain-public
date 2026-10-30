from pathlib import Path
from math import gcd
from functools import reduce
import json,time
root=Path(__file__).resolve().parents[1];start=time.perf_counter();counts=[]
for m in range(1,5):
    P=1<<m;mon=[0]+[1<<i for i in range(m)]+[(1<<i)|(1<<j) for i in range(m) for j in range(i+1,m)]
    hist={};tested=0
    for q in range(1<<len(mon)):
        W=[(4 if s&1 else 1)*(-1)**sum(1 for j,v in enumerate(mon) if q>>j&1 and s&v==v) for s in range(P)]
        inv=[sum(W[s]*(-1)**((s&y).bit_count()) for s in range(P)) for y in range(P)]
        div=reduce(gcd,map(abs,inv));height=max(map(abs,inv))//div
        assert height>2
        hist[height]=hist.get(height,0)+1;tested+=1
    counts.append({'m':m,'quadratic_phases':tested,'primitive_inverse_height_histogram':hist})
assert sum(c['quadratic_phases'] for c in counts)==2196
out={'status':'PASS','counts':counts,'method':'Direct character sums; gcd primitive inverse rejects every rational scaling into an integer row of height<=2','runtime_seconds':time.perf_counter()-start}
(root/'out'/'quadratic_review.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))

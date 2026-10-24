from pathlib import Path
from itertools import combinations
import json
root=Path(__file__).resolve().parents[1]
weights=(2,1,1,1)
vals=[2*int(sum(w for j,w in enumerate(weights) if x>>j&1)>=3)-1 for x in range(16)]
assert all(any(vals[x]!=vals[x^(1<<j)] for x in range(16)) for j in range(4))
rows=[]
for k in (2,3):
    for block in combinations(range(4),k):
        outside=[j for j in range(4) if j not in block]
        cofactors=[]
        for a in range(1<<k):
            fixed=sum(1<<j for z,j in enumerate(block) if a>>z&1)
            cofactor=tuple(vals[fixed|sum(1<<j for z,j in enumerate(outside) if b>>z&1)]
                           for b in range(1<<len(outside)))
            cofactors.append(cofactor)
        count=len(set(cofactors))
        assert count>=3
        rows.append({'block':list(block),'distinct_rows':count,'cofactors':[list(a) for a in cofactors]})
assert len(rows)==10
out={'status':'PASS','case_count':1,'essential':True,'prime':True,'truth_table':vals,'blocks':rows,
     'all_arity_bridge':'Analytic proof for weights (2,1,...,1), threshold 3, n_light>=3; finite fixture is not extrapolated'}
(root/'out'/'PRIME_FIXTURE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('PASS: essential four-input two-weight prime; all 10 proper blocks have at least three cofactor rows')

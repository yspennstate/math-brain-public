from functools import lru_cache
from fractions import Fraction
from pathlib import Path
import json,time

start=time.perf_counter(); R=Path(__file__).resolve().parent
n=9;full=511
coords=[(x,y) for y in range(3) for x in range(3)]
edges=[(i,j) for i in range(n) for j in range(i+1,n)
 if (coords[j][0]-coords[i][0],coords[j][1]-coords[i][1]) in
 [(1,0),(0,1),(-1,1)]]
def truth(m):
    visited=set();stack=[i for i in [0,3,6] if m&(1<<i)]
    while stack:
        i=stack.pop()
        if i in visited:continue
        visited.add(i)
        if i in [2,5,8]:return 1
        for a,b in edges:
            j=b if a==i else a if b==i else -1
            if j>=0 and m&(1<<j) and j not in visited:stack.append(j)
    return 0
f=[truth(m) for m in range(512)]
@lru_cache(None)
def opt(state):
    # Enumerate all consistent full inputs, rather than infer stopping by extrema.
    inputs=[m for m in range(512) if all(v<0 or ((m>>i)&1)==v for i,v in enumerate(state))]
    values={f[m] for m in inputs}
    if len(values)==1:return 0
    children=[]
    for i,v in enumerate(state):
        if v<0:
            s0=list(state);s1=list(state);s0[i]=0;s1[i]=1
            children.append(opt(tuple(s0))+opt(tuple(s1)))
    return len(inputs)+min(children)
state=(-1,)*9
costs=[]
for i in range(9):
    s0=list(state);s1=list(state);s0[i]=0;s1[i]=1
    costs.append(512+opt(tuple(s0))+opt(tuple(s1)))
nums=[sum(f[m]!=f[m^(1<<i)] for m in range(512)) for i in range(9)]
assert costs==[2468,2312,2220,2312,2252,2312,2220,2312,2468]
assert nums==[52,104,156,104,164,104,156,104,52]
assert opt(state)==2220
paths=[m for m in range(512) if f[m] and all(not f[m^(1<<i)] for i in range(9) if m&(1<<i))]
assert all(f[m]==any(m&p==p for p in paths) for m in range(512))
result={'edges':edges,'minimal_positive_masks':paths,'positive_inputs':sum(f),
 'influence_numerators_over_512':nums,'first_query_cost_sums_over_512':costs,
 'optimal_cost':str(Fraction(opt(state),512)),'states':opt.cache_info().currsize,
 'all_512_DNF_equivalences_checked':True,'seconds':time.perf_counter()-start}
(R/'independent_greedy_check.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result))

from pathlib import Path
from fractions import Fraction as Q
import json,time
RUN=Path(__file__).resolve().parents[1];START=time.perf_counter();checks=0
def ck(x):
    global checks
    assert x;checks+=1
    if time.perf_counter()-START>60:raise TimeoutError('frozen cap')
def influences(f):
    N=len(f);n=N.bit_length()-1;out=[]
    for i in range(n):
        step=1<<i
        out.append(Q(2*sum(f[x]!=f[x+step] for a in range(0,N,2*step) for x in range(a,a+step)),N))
    return out
records=[]
rows=json.loads((RUN/'out/full_CASES.json').read_text())
ck(len(rows)==14)
for row in rows:
    k=row['k'];kind=row['seed'];D=row['vertices'];masks=row['controller_masks'];N=1<<k
    if kind=='bent':b=tuple(1-2*(sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(k//2))%2) for x in range(N))
    elif kind=='tensor':b=tuple(1-2*((((x&1)*((x>>1)&1))+(x>>2).bit_count())%2) for x in range(N))
    else:b=tuple(1-2*(x.bit_count()%2) for x in range(N))
    lookup=dict(zip(D,masks))
    f=tuple(b[x]*(1-2*((lookup.get(x,0)>>z)&1)) for z in range(8) for x in range(N))
    inf=influences(f);ck(sum(inf[:k])==Q(row['I_data']));ck(sum(inf[k:])==Q(row['I_controller']))
    ck(Q(sum(f[z*N+x]!=b[x] for z in range(8) for x in range(N)),8*N)==Q(row['p']))
    ci=sum(sum(influences(tuple(1-2*((mask>>z)&1) for z in range(8)))) for mask in masks)/N
    ck(ci==sum(inf[k:]));ck(sum(influences(b))==Q(row['I_seed']))
    records.append({'case':row['case'],'direct_influences':list(map(str,inf))})
# A dense paired terminal really can lose its entire raw boundary under the character.
k=6;first=(1,0,0)
fiber=[sum(first[i]<<(2*i) for i in range(3))+sum(((t>>i)&1)<<(2*i+1) for i in range(3)) for t in range(8)]
D=tuple(fiber[t] for t in range(8) if t&1)
b=tuple(1-2*(sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))%2) for x in range(64))
f=tuple(b[x]*(-1 if x in D else 1) for x in range(64))
raw=tuple(-1 if t&1 else 1 for t in range(8));actual=tuple(f[x] for x in fiber)
ck(sum(influences(raw))==1);ck(sum(influences(actual))==0);ck(set(actual)=={1})
ck(Q(len(D),64)==Q(1,16));ck(sum(influences(f))>=Q(k,4))
diag1={'kind':'dense_leaf_character_cancellation','vertices':D,'first_pair_bits':first,'raw_I':'1','actual_I':'0','p':'1/16','root_I':str(sum(influences(f))),'scope':'refutes raw-to-character leaf influence monotonicity without its support guard, not FEI'}
b=tuple(1-2*(x&1) for x in range(256));ii=sum(influences(b))
ck(ii==1);ck(7*ii-8==-1)
diag2={'kind':'low_influence_ambient_capacity_failure','k':8,'seed':'x0 with seven dummy bits','p':'0','I_data':str(ii),'ambient_capacity':'8','rate7_capacity_gap':'-1','scope':'ambient k budget cannot be paid at rate7 without seed capacity; actual H=0, no FEI refutation'}
result={'verdict':'PASS','root_cases':14,'diagnostic_cases':2,'checks':checks,'runtime_seconds':time.perf_counter()-START,'method':'direct natural Boolean edges; no Walsh/log helper','roots':records,'diagnostics':[diag1,diag2]}
(RUN/'out/EDGE_FRONTIER_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('roots','diagnostics')}))

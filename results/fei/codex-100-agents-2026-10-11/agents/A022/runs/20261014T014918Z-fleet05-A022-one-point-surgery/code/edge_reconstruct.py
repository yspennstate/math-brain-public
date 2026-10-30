from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import time,json
RUN=Path(__file__).resolve().parents[1];START=time.perf_counter();CHECKS=0
def ck(v):
    global CHECKS
    assert v
    CHECKS+=1
def sign(v,k):
    value=1
    for j in range(0,k,2):
        if v&(1<<j) and v&(1<<(j+1)):value=-value
    return value
def edges(f,j):return sum(f[x]!=f[x^(1<<j)] for x in range(len(f)) if not x&(1<<j))
def insert(prefix,partner,k):
    return sum(((prefix>>j)&1)<<(2*j) | ((partner>>j)&1)<<(2*j+1) for j in range(k//2))
@lru_cache(maxsize=60)
def core_edges(k,v):
    b=tuple(sign(x,k) for x in range(1<<k));h=tuple(-s if x==v else s for x,s in enumerate(b))
    return tuple(Q(2*edges(b,j),len(b)) for j in range(k)),tuple(Q(2*edges(h,j),len(h)) for j in range(k))
@lru_cache(maxsize=6672)
def controller(t,mask):
    f=tuple(-1 if mask&(1<<z) else 1 for z in range(1<<t))
    return Q(mask.bit_count(),len(f)),sum(Q(2*edges(f,j),len(f)) for j in range(t))
cases=fibers=0
for line in (RUN/'out/full_CASES.jsonl').open(encoding='utf-8'):
    if time.perf_counter()-START>1800:raise TimeoutError('frozen cap')
    row=json.loads(line);k=row['k'];t=row['t'];v=row['v'];mask=row['controller_mask'];m=k//2
    alpha,Ia=controller(t,mask);delta=Q(1,1<<k);before,after=core_edges(k,v)
    inf=tuple((1-alpha)*x+alpha*y for x,y in zip(before,after))
    dataI=sum(inf);removed=sum(inf[j] for j in range(0,k,2));terminaldata=Q(0);terminalctrl=Q(0)
    for prefix in range(1<<m):
        f=[]
        for z in range(1<<t):
            for partner in range(1<<m):
                x=insert(prefix,partner,k)
                s=sign(x,k)
                f.append(-s if x==v and mask&(1<<z) else s)
        leaf=tuple(f)
        terminaldata+=sum(Q(2*edges(leaf,j),len(leaf)) for j in range(m))/(1<<m)
        terminalctrl+=sum(Q(2*edges(leaf,m+j),len(leaf)) for j in range(t))/(1<<m)
        fibers+=1
    ck(dataI==Q(row['I_data']));ck(delta*Ia==Q(row['I_ctrl']))
    ck(removed==Q(row['I_access']));ck(terminaldata==Q(row['I_terminal_data']))
    ck(terminalctrl==Q(row['I_terminal_ctrl']));ck(removed+terminaldata==dataI)
    ck(terminalctrl==delta*Ia);ck(row['access_bad_credit']=='0')
    cases+=1
result={'cases':cases,'fibers':fibers,'checks':CHECKS,'runtime_seconds':time.perf_counter()-START,
    'verdict':'PASS','method':'direct natural-coordinate pair truth tables, edited cube edges, physical fibers; no Walsh/log helper',
    'review_scope':'author second implementation; not independent-human acceptance'}
(RUN/'out/EDGE_RECONSTRUCTION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

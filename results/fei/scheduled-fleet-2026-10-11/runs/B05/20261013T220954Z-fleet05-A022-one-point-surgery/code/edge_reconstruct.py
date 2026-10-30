"""Independent truth/edge representation: no Fourier transform or log kernel."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import time,json
RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter();CHECKS=0;counts=Counter()
def ck(v):
    global CHECKS
    assert v
    CHECKS+=1
def cuts(f,j):return sum(f[v]!=f[v^(1<<j)] for v in range(len(f)) if not ((v>>j)&1))
def insert(a,t,k):
    return sum(((a>>j)&1)<<(2*j) | ((t>>j)&1)<<(2*j+1) for j in range(k//2))
@lru_cache(maxsize=5000)
def core(k,D):
    N=1<<k;M=1<<(k//2);defect=set(D)
    # Construct signs by multiplying the pair truth tables, not a Walsh recurrence.
    b=tuple((-1)**sum(1 for j in range(0,k,2) if (v>>j)&1 and (v>>(j+1))&1) for v in range(N))
    h=tuple(-b[v] if v in defect else b[v] for v in range(N))
    inf=tuple(Q(1,4)+Q(cuts(h,j),N) for j in range(k))
    mean=Q(sum(b)+sum(h),2*N)
    leafI=Q(0)
    for a in range(M):
        ref=tuple(b[insert(a,t,k)] for t in range(M))
        edited=tuple(h[insert(a,t,k)] for t in range(M))
        expected=tuple((-1)**((a&t).bit_count()%2) for t in range(M))
        ck(ref==expected)
        E=tuple(t for t in range(M) if ref[t]!=edited[t]);ck(len(E)<=4)
        Iref=sum(Q(2*cuts(ref,j),M) for j in range(k//2))
        Iedit=sum(Q(2*cuts(edited,j),M) for j in range(k//2))
        leafI+=(Iref+Iedit)/(2*M)
        u=Q(len(E),M)
        if 0<u<=Q(1,4):
            g=tuple(-1 if t in E else 1 for t in range(M))
            orig=tuple(Q(2*cuts(g,j),M) for j in range(k//2))
            ck(all(q<=2*u<=Q(1,2) for q in orig))
            ck(Iedit>=sum(orig))
            # Exact integer reformulation of boundary>=s log2(M/s).
            s=len(E);boundary=sum(cuts(g,j) for j in range(k//2))
            ck((2**boundary)*(s**s)>=M**s)
        elif u>Q(1,4):
            ck(k//2<=3)
            ck(Iedit>=Q(2*(k//2),M) or min(edited)==max(edited))
        counts['leaf_fibers']+=1
    ck(leafI==sum(inf[j] for j in range(1,k,2)))
    # In each prefix restriction the unedited first-coordinate derivative is 1/2.
    for q in range(k//2):
        for prefix in range(1<<q):
            verts=[v for v in range(N) if all(((v>>(2*j))&1)==((prefix>>j)&1) for j in range(q))]
            changed=sum(b[v]!=b[v^(1<<(2*q))] for v in verts)
            ck(changed*2==len(verts))
            changed_edit=sum(h[v]!=h[v^(1<<(2*q))] for v in verts)
            ck(Q(changed+changed_edit,2*len(verts))>=Q(1,4))
            counts['prefix_derivatives']+=1
    return inf,mean,leafI
cases=0
for line in (RUN/'out'/'full_CASES.jsonl').open(encoding='utf-8'):
    if time.perf_counter()-START>60:raise TimeoutError('frozen independent cap')
    row=json.loads(line);k=row['k'];r=row['r'];D=tuple(row['D']);p=Q(1,1<<r)
    inf,mean,leafI=core(k,D);dy=Q(len(D),1<<k)
    removed=p*(r*(1-mean)+sum(inf[j] for j in range(0,k,2))+dy)
    terminal=p*leafI
    ck(removed==Q(row['I_removed']));ck(terminal==Q(row['I_terminal']))
    ck(removed+terminal==Q(row['I']));ck(row['access_bad_credit']=='0')
    cases+=1
result={'helper':'edge-reconstruct-v1','cases':cases,'checks':CHECKS,'counts':dict(counts),
    'runtime_seconds':time.perf_counter()-START,'representation':'direct pair truth tables, labelled cube edges, exact integer isoperimetry products; NO Fourier or log kernel',
    'verdict':'PASS','independence':'different author implementation, not independent human review'}
(RUN/'out'/'EDGE_RECONSTRUCTION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

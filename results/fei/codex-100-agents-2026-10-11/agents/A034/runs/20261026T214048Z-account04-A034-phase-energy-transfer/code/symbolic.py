from fractions import Fraction as Q
from pathlib import Path
import itertools,json,time,hashlib
RUNDIR=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def need(v):
    global checks
    checks+=1
    assert v
    assert time.monotonic()-start<55
def corr(a,b,i):
    # E[a(y)b(y+e_i)], using only physical affine equations and character averages.
    A,ma,sa=a;B,mb,sb=b
    C=dict(A);sgn=sa*sb*(-1 if i in mb else 1)
    for j,v in B.items():
        v=v^(j==i)
        if j in C and C[j]!=v:return Q(0)
        C[j]=v
    for j in ma^mb:
        if j not in C:return Q(0)
        if C[j]:sgn=-sgn
    return Q(sgn,2**len(C))
def energy(cells,i):
    mu=sum((Q(1,2**len(a[0])) for a in cells),Q(0))
    return (mu-sum((corr(a,b,i) for a in cells for b in cells),Q(0)))/2
groups_seen=set();cases=0
for ks in ([1,12,23,34],[1,2,14,25],[1,2,14,15],[1,2,3,4]):
    for signs in itertools.product((-1,1),repeat=4):
        for mask_pattern in range(4):
            cells=[]
            for t,(k,sgn) in enumerate(zip(ks,signs)):
                fixed={j:1 for j in range(k-1)};fixed[k-1]=0
                mask=set()
                if mask_pattern&1:mask.add(35)
                if mask_pattern&2:mask.add((t*7+3)%36)
                cells.append((fixed,mask,sgn))
            groups=[];prev=None
            for a in cells:
                k=len(a[0])
                if prev is None or k-prev>10:groups.append([]) # R=64*4^2=2^10
                groups[-1].append(a);prev=k
            groups_seen.add(len(groups))
            for i in range(36):
                eg=[energy(g,i) for g in groups];eu=energy(cells,i)
                need(eu>=0 and all(e>=0 for e in eg))
                need(2*eu>=sum(eg))
                for g,e in zip(groups,eg):
                    need(e==0 or e>=Q(1,2**(max(len(a[0]) for a in g)+1)))
            cases+=1
need(cases==256);need(groups_seen=={1,2,3,4})
out=dict(status='PASS',cases=cases,assertions=checks,groups_seen=sorted(groups_seen),
         seconds=time.monotonic()-start,helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(RUNDIR/'out/symbolic.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))

"""A030-plateau-exact-v2. Exact spectra, restrictions, and edge influences."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations, product
import json, time, hashlib

START = time.perf_counter()
ROOT = Path(__file__).resolve().parents[1]
checks = 0
counts = dict(seeds=0, replicated_functions=0, replication_nodes=0,
              spectator_functions=0, spectator_nodes=0,
              defect_functions=0, defect_nodes=0, compression_leaves=0)

def ck(test):
    global checks
    checks += 1
    assert test, checks
    if time.perf_counter() - START > 59:
        raise RuntimeError('Frozen 60-second pilot budget exceeded')

def walsh(table):
    a = table.copy()
    w = 1
    while w < len(a):
        for s in range(0, len(a), 2*w):
            for j in range(s, s+w):
                u,v = a[j],a[j+w]
                a[j],a[j+w] = u+v,u-v
        w *= 2
    return {s: Q(v,len(a)) for s,v in enumerate(a) if v}

def masses(a):
    return sorted(v*v for v in a.values())

def influences(a,n):
    return [sum((v*v for s,v in a.items() if s>>i&1), Q(0)) for i in range(n)]

def edges(table,n):
    return [Q(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table)) for i in range(n)]

def restrict(table,n,fixed):
    free = [i for i in range(n) if i not in fixed]
    base = sum(v<<i for i,v in fixed.items())
    return [table[base | sum(((x>>j)&1)<<i for j,i in enumerate(free))]
            for x in range(1<<len(free))],free

def replicate(seed,n,L):
    return [seed[sum(((x>>(i*L)&((1<<L)-1)).bit_count()%2)<<i for i in range(n))]
            for x in range(1<<(n*L))]

def spectator(seed,n,m):
    return [seed[x&((1<<n)-1)] * (-1 if (x>>n).bit_count()%2 else 1)
            for x in range(1<<(n+m))]

def verify_spectators(seed,n,m,defect=False):
    a = walsh(seed); di = influences(a,n)
    table = spectator(seed,n,m); N=n+m; b=walsh(table)
    ck(b=={s | (((1<<m)-1)<<n):v for s,v in a.items()})
    ck(influences(b,N)==di+[Q(1)]*m)
    ck(edges(table,N)==di+[Q(1)]*m)
    for k in range(m+1):
        for bits in product((0,1),repeat=k):
            fixed = {n+j:v for j,v in enumerate(bits)}
            child,free=restrict(table,N,fixed); c=walsh(child)
            ck(masses(c)==masses(a))
            ck(sum(influences(c,len(free)))==sum(di)+m-k)
            counts['defect_nodes' if defect else 'spectator_nodes']+=1
    counts['defect_functions' if defect else 'spectator_functions']+=1

for n in range(1,4):
    for mask in range(1<<(1<<n)):
        seed=[-1 if mask>>x&1 else 1 for x in range(1<<n)]
        counts['seeds']+=1
        a=walsh(seed); di=influences(a,n)
        ck(sum(masses(a))==1); ck(di==edges(seed,n))
        for L in ([2,3] if n<=2 else [2]):
            N=n*L; table=replicate(seed,n,L); b=walsh(table)
            code=lambda s:sum(((1<<L)-1)<<(i*L) for i in range(n) if s>>i&1)
            ck(b=={code(s):v for s,v in a.items()})
            ck(influences(b,N)==[q for q in di for _ in range(L)])
            ck(edges(table,N)==influences(b,N))
            for k in range(L):
                for A in combinations(range(N),k):
                    for bits in product((0,1),repeat=k):
                        fixed=dict(zip(A,bits)); child,free=restrict(table,N,fixed)
                        c=walsh(child)
                        expected={sum(((code(s)>>i)&1)<<j for j,i in enumerate(free)):
                                  v*(-1 if sum((code(s)>>i&1)*u for i,u in fixed.items())%2 else 1)
                                  for s,v in a.items()}
                        ck(c==expected); ck(masses(c)==masses(a))
                        ci=[di[i//L] for i in free]
                        ck(influences(c,len(free))==ci)
                        counts['replication_nodes']+=1
            # Entire compression partition: retain first coordinate of each block.
            A=[i for i in range(N) if i%L]
            for bits in product((0,1),repeat=len(A)):
                child,free=restrict(table,N,dict(zip(A,bits))); c=walsh(child)
                ck(masses(c)==masses(a)); ck(influences(c,n)==di)
                counts['compression_leaves']+=1
            counts['replicated_functions']+=1
        for m in (1,2): verify_spectators(seed,n,m)

records=[]
for r in range(2,9):
    seed=[-1]+[1]*((1<<r)-1); a=walsh(seed); p=Q(1,1<<r)
    ck(a[0]==1-2*p)
    ck(all(v==-2*p for s,v in a.items() if s))
    ck(sum(influences(a,r))==2*r*p)
    for m in (1,2,3):
        verify_spectators(seed,r,m,True)
        records.append(dict(r=r,m=m,core_influence=str(2*r*p),
                            amplification=str(1+Q(m,1)/(2*r*p))))

ck(counts['seeds']==276)
ck(counts['replicated_functions']==296)
ck(counts['replication_nodes']==4736)
ck(counts['spectator_functions']==552)
ck(counts['spectator_nodes']==2760)
ck(counts['defect_functions']==21)
ck(counts['defect_nodes']==175)
out=dict(status='PASS',helper_version='A030-plateau-exact-v2',checks=checks,
         counts=counts,elapsed_seconds=time.perf_counter()-START,
         arithmetic='integer Walsh and Fraction; entropy certified via exact squared-mass multiset',
         code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         point_defect_records=records)
(ROOT/'out'/'validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='point_defect_records'},indent=2))

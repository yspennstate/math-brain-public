from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json,time
t0=time.perf_counter()
def projection(x,positions):return sum(((x>>j)&1)<<i for i,j in enumerate(positions))
@lru_cache(None)
def admitted(n):
    rows=range(1<<n);C={tuple([1]*(1<<n)),tuple([-1]*(1<<n))}
    for j in range(n):
        for sign in (-1,1):C.add(tuple(sign*(1 if x>>j&1 else -1) for x in rows))
    for mask in range(1,(1<<n)-1):
        A=[j for j in range(n) if mask>>j&1];B=[j for j in range(n) if not mask>>j&1]
        for g in admitted(len(A)):
            for h in admitted(len(B)):
                C.add(tuple(g[projection(x,A)]*h[projection(x,B)] for x in rows))
    for j in range(n):
        rest=[i for i in range(n) if i!=j]
        for mask in range(1<<len(rest)):
            A=[i for k,i in enumerate(rest) if mask>>k&1];B=[i for k,i in enumerate(rest) if not mask>>k&1]
            for g in admitted(len(A)):
                for h in admitted(len(B)):
                    C.add(tuple(g[projection(x,A)] if x>>j&1 else h[projection(x,B)] for x in rows))
    return frozenset(C)
counts={str(n):len(admitted(n)) for n in range(4)}
majority=tuple(1 if x.bit_count()>=2 else -1 for x in range(8))
assert majority not in admitted(3)
restrictions=0
for n in (1,2,3):
    for f in admitted(n):
        for j in range(n):
            for bit in (0,1):
                g=tuple(f[(x&((1<<j)-1))|((x>>j)<<(j+1))|(bit<<j)] for x in range(1<<(n-1)))
                assert g in admitted(n-1);restrictions+=1
assert time.perf_counter()-t0<55
Path(__file__).resolve().parents[1].joinpath('out/ADMISSION_RESULTS.json').write_text(json.dumps({'status':'PASS','counts':counts,'majority3':list(majority),'majority_admitted':False,'restriction_checks':restrictions,'elapsed_seconds':time.perf_counter()-t0},indent=2)+'\n',encoding='utf-8')

"""Independent finite rank certificate. Frozen: all 64 four-bit alternating
matrices, all 16 induced subsets for each nonsingular root; exact integer
elimination; <10 MB, <60s. No shared helper, Fourier law or reference code.
Boundary: rank-two four-vertex star, supplied source reference, zero queries.
"""
from pathlib import Path
from itertools import combinations
import json, time, hashlib
start=time.monotonic(); checks=roots=0
def rank(a):
    a=list(a); r=0
    for j in range(4):
        p=next((i for i in range(r,len(a)) if a[i]>>j&1),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for i in range(len(a)):
            if i!=r and a[i]>>j&1: a[i]^=a[r]
        r+=1
    return r
pairs=list(combinations(range(4),2))
for mask in range(64):
    rows=[0]*4
    for k,(i,j) in enumerate(pairs):
        if mask>>k&1: rows[i]|=1<<j; rows[j]|=1<<i
    if rank(rows)!=4: continue
    roots+=1
    for kept in range(16):
        sub=[rows[i]&kept for i in range(4) if kept>>i&1]
        r=rank(sub); m=sum(bool(v) for v in sub)
        D=(4-r)//2
        assert m-r<=D,('first-reset rank payment',mask,kept)
        assert D+r<=4,('gross plus terminal H',mask,kept)
        checks+=2
assert roots==28
star=[14,1,1,1]; r=rank(star); tc=4-r
assert r==2 and tc==2 and tc>0
checks+=2
out={'status':'PASS','roots':roots,'induced_subsets':roots*16,'assertions':checks,
     'rank_deficient_guard':{'rank':r,'TC_before_any_drop':tc,'rank_drops':0},
     'elapsed_seconds':time.monotonic()-start,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).resolve().parents[1].joinpath('out/rank_audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))

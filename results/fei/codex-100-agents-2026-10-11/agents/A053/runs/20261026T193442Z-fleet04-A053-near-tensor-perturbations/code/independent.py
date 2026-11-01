from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
import time,json
ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    checks+=1
    assert x,checks
def plus(u,v): return (u[0]+v[0],u[1]+v[1])
def scale(a,u): return (a*u[0],a*u[1])
def diff(u,v): return plus(u,scale(-1,v))
def sign(u):
    from math import lcm
    den=lcm(u[0].denominator,u[1].denominator)
    a,b=int(u[0]*den),int(u[1]*den)
    p=pow(2,max(0,a))*pow(3,max(0,b))
    q=pow(2,max(0,-a))*pow(3,max(0,-b))
    return (p>q)-(p<q)
@lru_cache(None)
def deficit(mask):
    f=[1-2*((mask>>x)&1) for x in range(8)]
    H=(Q(6),Q(0))
    for s in range(8):
        w=sum(f[x]*(1-2*((x&s).bit_count()%2)) for x in range(8))
        if not w: continue
        z=w*w; a=b=0
        while z%2==0: z//=2; a+=1
        while z%3==0: z//=3; b+=1
        ck(z==1)
        H=diff(H,(Q(w*w*a,64),Q(w*w*b,64)))
    I=Q(sum(f[x]!=f[x^(1<<j)] for j in range(3) for x in range(8)),8)
    return diff(H,(2*I,Q(0)))
mu=deficit(1)
ck(mu==(Q(5,2),Q(-9,8))); ck(sign(mu)>0)
seed=[(-1 if (x&7)==0 else 1)*(-1 if (x>>3)==0 else 1) for x in range(64)]
roots=0; banks=0; fibres=0
for r in (0,1,2):
    for edits in combinations(range(64),r):
        G=seed.copy()
        for x in edits: G[x]*=-1
        roots+=1
        for queried in (0,1):
            ds=[]; occupied=0
            for y in range(8):
                row=[G[(y<<3)|x] if queried==0 else G[(x<<3)|y] for x in range(8)]
                orig=[seed[(y<<3)|x] if queried==0 else seed[(x<<3)|y] for x in range(8)]
                e=sum(a!=b for a,b in zip(row,orig)); occupied+=bool(e)
                mask=sum((v==-1)<<x for x,v in enumerate(row))
                d=deficit(mask); ds.append(d); fibres+=1
                ck(e>0 or d==mu)
                ck(sign(d)>0 or e>=1)
            certified=sum(sign(d)<=0 for d in ds)
            ck(certified<=r); ck(occupied<=r)
            total=(Q(0),Q(0)); positive=(Q(0),Q(0))
            for d in ds:
                total=plus(total,scale(Q(1,8),d))
                if sign(d)>0: positive=plus(positive,scale(Q(1,8),d))
            lower=diff(mu,scale(Q(r,8),plus(mu,(Q(6),Q(0)))))
            ck(sign(diff(total,lower))>=0)
            ck(sign(diff(positive,scale(1-Q(r,8),mu)))>=0)
            banks+=1
result=dict(status='PASS',roots=roots,complete_banks=banks,complete_fibres=fibres,
            checks=checks,seconds=time.perf_counter(),cached_tables=deficit.cache_info().currsize)
# seconds in the original certificate is CPU time, not elapsed wall time.
result['seconds']=time.process_time()
(ROOT/'out'/'INDEPENDENT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

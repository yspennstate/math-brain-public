"""Frozen exhaustive pilot: integer certificates, all adaptive trees, n<=4."""
import json, time
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

START=time.monotonic()
OUT=Path(__file__).resolve().parents[1]/'out'
checks=0

def canonical(n,t):
    return t if not t&1 else t^((1<<(1<<n))-1)

def walsh(n,t):
    a=[1-2*((t>>x)&1) for x in range(1<<n)]
    h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h]; a[k],a[k+h]=u+v,u-v
        h*=2
    return a

def children(n,t,i):
    lo=hi=0
    for x in range(1<<(n-1)):
        y=(x&((1<<i)-1))|((x>>i)<<(i+1))
        lo|=((t>>y)&1)<<x
        hi|=((t>>(y|(1<<i)))&1)<<x
    return lo,hi

def influence_numerator(n,t):
    return sum(((t>>x)^(t>>(x^(1<<i))))&1 for x in range(1<<n) for i in range(n))

@lru_cache(None)
def packet(A,B):
    # exp2((A+B)log2(A+B)-A log2 A-B log2 B)
    if not A or not B: return (1,1)
    return (pow(A+B,A+B),pow(A,A)*pow(B,B))

@lru_cache(None)
def solve(n,t):
    global checks
    N=1<<n
    if n==0: return (0,(0,0,0),(-1,-1,-1))
    a=walsh(n,t)
    inf=influence_numerator(n,t)
    assert sum(v*v for v in a)==N*N
    assert sum(s.bit_count()*v*v for s,v in enumerate(a))==N*inf
    checks+=2
    maxima=[0,0,0]; choices=[-1,-1,-1]
    for i in range(n):
        l,h=children(n,t,i)
        _,lc,_=solve(n-1,canonical(n-1,l))
        _,hc,_=solve(n-1,canonical(n-1,h))
        count=influence_numerator(n-1,l^h)
        numer=denom=1; dn=0
        for s in range(N):
            if s&(1<<i): continue
            A,B=a[s]**2,a[s|(1<<i)]**2
            u,v=packet(min(A,B),max(A,B)); numer*=u; denom*=v; dn+=B
        disagreement=(l^h).bit_count()
        assert dn==2*N*disagreement
        checks+=1
        for j,K in enumerate((2,3,4)):
            bad=numer>(denom<<(K*dn))
            value=lc[j]+hc[j]+(count if bad else 0)
            if value>maxima[j]: maxima[j]=value; choices[j]=i
    return inf,tuple(maxima),tuple(choices)

rows=[]; cases=0
for n in range(5):
    best=[Fraction(0)]*3; witness=[None]*3
    for t in range(0,1<<(1<<n),2):
        cases+=1
        inf,cost,choice=solve(n,t)
        if inf:
            for j in range(3):
                r=Fraction(cost[j],inf)
                if r>best[j]: best[j]=r; witness[j]={'truth_table_negative_bits':t,'root_coordinate':choice[j],'cost_numerator':cost[j],'influence_numerator':inf}
        if time.monotonic()-START>60: raise RuntimeError('Frozen 60-second cap exceeded')
    rows.append({'n':n,'max_ratios':{str(K):str(best[j]) for j,K in enumerate((2,3,4))},'witnesses':witness})
    print(json.dumps(rows[-1]),flush=True)
result={'cases':cases,'assertions_passed':checks,'seconds':time.monotonic()-START,'rows':rows,'cache':str(solve.cache_info()),'arithmetic':'exact integer powers and rational ratios'}
(OUT/'EXACT_TREE_RESULTS.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result),flush=True)

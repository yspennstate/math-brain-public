"""Separate direct-character / GF2 elimination check, frozen version 1."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import json,time
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter()
cases=checks=0
def require(ok):
    global checks
    checks+=1
    assert ok
def rank(rows):
    pivots={}
    for v in rows:
        while v:
            p=v.bit_length()-1
            if p not in pivots:
                pivots[p]=v
                break
            v^=pivots[p]
    return len(pivots)
for m in range(5):
    pairs=list(combinations(range(m),2))
    for coefficients in range(1 << (1+m+len(pairs))):
        constant=coefficients & 1
        linear=coefficients >> 1 & ((1 << m)-1)
        polar=[0]*m
        selected=[]
        for k,(i,j) in enumerate(pairs):
            if coefficients >> (1+m+k) & 1:
                selected.append((i,j))
                polar[i]^=1 << j
                polar[j]^=1 << i
        truth=[(-1)**(constant+((linear & v).bit_count()%2)+sum((v >> i & 1)*(v >> j & 1) for i,j in selected)) for v in range(1 << m)]
        # Independent transform: sum characters directly, no FWHT.
        raw=[sum(f*((-1)**((t & v).bit_count()%2)) for v,f in enumerate(truth)) for t in range(1 << m)]
        r=rank(polar)
        support=[t for t,a in enumerate(raw) if a]
        require(r%2==0)
        require(len(support)==1 << r)
        require(all(raw[t]**2==1 << (2*m-r) for t in support))
        require(sum(a*a for a in raw)==1 << (2*m))
        spectral=Fraction(sum(t.bit_count()*a*a for t,a in enumerate(raw)),1 << (2*m))
        direct=Fraction(sum(truth[v]!=truth[v ^ (1 << i)] for i in range(m) for v in range(1 << m)),1 << m)
        require(spectral==direct)
        require(r<=2*direct)
        cases+=1
result={'helper_version':1,'status':'PASS','all_quadratic_phase_cases':cases,'domain':'m=0,1,2,3,4; all constants, linear and quadratic coefficients','assertions':checks,'arithmetic':'integer direct-character sums and separate GF2 row elimination; rational direct/spectral influence','runtime_seconds':time.perf_counter()-start,'independent_reviewer':False}
(ROOT/'out/quadratic_core.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

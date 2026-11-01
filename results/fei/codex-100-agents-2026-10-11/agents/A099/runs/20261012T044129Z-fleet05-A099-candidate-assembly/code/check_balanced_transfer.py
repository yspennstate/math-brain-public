"""Frozen 80-case exact check of balanced activation, A099 v1."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json
import sys
import time

RUN = Path(__file__).resolve().parents[1]
COUNT = 0
def check(actual, expected):
    global COUNT
    COUNT += 1
    assert actual == expected, (actual, expected)

def fwht(values):
    a = list(values)
    step = 1
    while step < len(a):
        for block in range(0, len(a), 2*step):
            for j in range(step):
                x,y = a[block+j], a[block+j+step]
                a[block+j], a[block+j+step] = x+y, x-y
        step *= 2
    return [F(x,len(a)) for x in a]

@lru_cache(None)
def factors(n):
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d,0)+1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n,0)+1
    return out

def log_form(q):
    assert q > 0
    out = dict(factors(q.numerator))
    for p,v in factors(q.denominator).items():
        out[p] = out.get(p,0)-v
    return {p:F(v) for p,v in out.items() if v}

def add(*forms):
    out = {}
    for form in forms:
        for p,v in form.items():
            out[p] = out.get(p,F(0))+v
    return {p:v for p,v in out.items() if v}

def scale(form,c):
    return {p:v*c for p,v in form.items() if v*c}

def ent(q):
    return scale(log_form(q),-q) if q else {}

def phi(r,s):
    return add(ent(r), ent(s), scale(ent(r+s),-1)) if r+s else {}

def erasures(p):
    n = len(p).bit_length()-1
    return [add(*(phi(p[t],p[t|(1<<i)]) for t in range(len(p)) if not t&(1<<i))) for i in range(n)]

def physical_influences(values):
    n = len(values).bit_length()-1
    return [F(sum(values[x]!=values[x^(1<<i)] for x in range(len(values))),len(values)) for i in range(n)]

start = time.perf_counter()
pilot = '--pilot' in sys.argv
cases = 0
records = []
for n in ([1] if pilot else [1,2]):
    for mask in range(1<<(1<<n)):
        seed = [1 if (mask>>x)&1 else -1 for x in range(1<<n)]
        aseed = fwht(seed)
        pseed = [a*a for a in aseed]
        dseed = physical_influences(seed)
        Bseed = add(*erasures(pseed))
        for m in [1,2]:
            dim = m*n+1
            h = []
            for x in range(1<<dim):
                sign = -1 if (x>>(m*n))&1 else 1
                for block in range(m):
                    sign *= seed[(x>>(block*n))&((1<<n)-1)]
                h.append(sign)
            ah = fwht(h)
            ph = [a*a for a in ah]
            dh = physical_influences(h)
            Bh = erasures(ph)
            check(ah[0],F(0))
            check(add(*Bh),scale(Bseed,m))
            check(dh, dseed*m+[F(1)])
            check(sum(dh), m*sum(dseed)+1)
            # All mean-to-singleton phi packets vanish, even when h has
            # a nonzero singleton at the fresh balancing coordinate.
            check(add(*(phi(ph[0],ph[1<<i]) for i in range(dim))),{})
            for k in [1,2]:
                delta = F(1,1<<k)
                f = [h[x>>k] if x&((1<<k)-1)==0 else 1 for x in range(1<<(dim+k))]
                af = fwht(f)
                pf = [a*a for a in af]
                df = physical_influences(f)
                Bf = erasures(pf)
                check(sum(pf),F(1))
                check(df,[delta]*k+[delta*d for d in dh])
                check(sum(df),delta*(m*sum(dseed)+1+k))
                for index,a in enumerate(af):
                    U = index&((1<<k)-1)
                    S = index>>k
                    expected = delta*ah[S] if S else (-delta if U else 1-delta)
                    check(a,expected)
                remainder = {}
                for i in range(dim):
                    extra = add(scale(phi(F(1),ph[1<<i]),delta*(1-delta)),
                                phi((1-delta)**2,delta**2*ph[1<<i]))
                    check(Bf[k+i], add(scale(Bh[i],delta),extra))
                    remainder = add(remainder,extra)
                check(add(*Bf[k:]),add(scale(Bseed,m*delta),remainder))
                cases += 1
                records.append({'n':n,'seed_mask':mask,'m':m,'k':k,'dimension':dim+k,
                                'seed_influence':str(sum(dseed)), 'activated_influence':str(sum(df)),
                                'root_pairs_balanced_core_zero':True,'aggregate_data_identity_exact':True})
elapsed = time.perf_counter()-start
check(cases,16 if pilot else 80)
assert elapsed < 60
output = {'helper_version':'A099-balanced-erasure-transfer-v1','cases':cases,
          'exact_assertions':COUNT,'failures':0,'runtime_seconds':elapsed,
          'arithmetic':'Fraction probabilities and prime-log coefficient cancellation; no floating logarithms',
          'lower_bound_proof':'B_data(F)=delta*m*B(seed)+sum(nonnegative phi packets); control erasures nonnegative',
          'cases_checked':records}
destination = RUN/'out'/('PILOT.json' if pilot else 'EXACT_TRANSFER.json')
destination.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in output.items() if k!='cases_checked'},indent=2))

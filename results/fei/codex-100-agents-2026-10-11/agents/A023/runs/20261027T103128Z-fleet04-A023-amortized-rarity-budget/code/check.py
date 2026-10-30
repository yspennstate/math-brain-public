"""Exact bounded verification; run --freeze before running checks."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import itertools
import json
import sys
import time

RUN = Path(__file__).resolve().parents[1]
OUT = RUN / 'out'
OUT.mkdir(exist_ok=True)

def save(name, obj):
    (OUT/name).write_text(json.dumps(obj, indent=2)+'\n', encoding='utf-8')

SPEC = dict(helper_version='A023-stage23-exact-v1',
    helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    actual_Boolean_family='ALL truth tables n=0..3; point defects n=2..12',
    parameter_domain='278 truth tables; every partial physical restriction; every finite adaptive stopped tree with a persistent prefix-free mark, verified by exact Bellman envelope and full-tree n<=2 enumeration',
    case_count=dict(truth_tables=278, point_defect_fixtures=11),
    symmetry='none; no truth-table quotient',
    arithmetic='integer Walsh and direct characters; Fraction influence and ledger; rational atanh-series log enclosures',
    memory_estimate_MB=80, maximum_runtime_seconds=60,
    search=False, heavy_job=False,
    failure_modes=['wrong physical reach','mark not persistent','clipped signed debt','reuse across descendants','I=0 smoothing','old reference not normalized','Bellman only deterministic policies','unpaid query KL'])

if '--freeze' in sys.argv:
    save('FROZEN_SPEC.json',SPEC)
    print('Frozen specification saved; no checks run.')
    raise SystemExit(0)
assert json.loads((OUT/'FROZEN_SPEC.json').read_text(encoding='utf-8')) == SPEC
start=time.perf_counter()
counts=dict(tables=0, states=0, query_nodes=0, tree_mark_ledgers=0,
            rational_log_checks=0, assertions=0, point_defect_fixtures=0)

def ck(ok):
    counts['assertions']+=1
    assert ok
    if time.perf_counter()-start>60:
        raise TimeoutError('frozen 60-second cap')

@lru_cache(None)
def walsh(t):
    a=list(t); h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):
                a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return tuple(a)

@lru_cache(None)
def influence(t):
    n=len(t).bit_length()-1
    return F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t)) for i in range(n)),len(t))

def child(t,i,b):
    return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))

def ia(t,i):
    return F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))

def logint(x, terms=24):
    """ln(x) exact interval using range reduction and atanh series."""
    assert x>0
    k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    def base(z):
        y=(z-1)/(z+1)
        lo=2*sum((y**(2*j+1))/F(2*j+1) for j in range(terms))
        err=2*y**(2*terms+1)/F(2*terms+1)/(1-y*y)
        return lo,lo+err
    lo,hi=base(x); a,b=base(F(2))
    return (lo+k*a,hi+k*b) if k>=0 else (lo+k*b,hi+k*a)

def log2int(x):
    a,b=logint(x); c,d=logint(F(2))
    if a>=0: return a/d,b/c
    return a/c,b/d

def klint(p,q):
    lo=hi=F(0)
    for a,b in zip(p,q):
        if a:
            l,u=log2int(a/b); lo+=a*l; hi+=a*u
    return lo,hi

@lru_cache(None)
def envelopes(t, marked):
    """Max error of Q+marked terminal I+unmarked terminal I-root I.
    Max conversion envelope uses terminal D<=I; persistence is explicit.
    Include stop, each physical query with independently chosen children,
    and optional first mark (only if unmarked).
    """
    j=influence(t)
    vals=[F(0)]
    for i in range(len(t).bit_length()-1):
        vals.append(ia(t,i)+(envelopes(child(t,i,0),marked)+envelopes(child(t,i,1),marked))/2-j)
        # Child errors are relative to their own I, so use partition explicitly.
        vals[-1]+= (influence(child(t,i,0))+influence(child(t,i,1)))/2
    if not marked: vals.append(envelopes(t,True))
    ck(all(v==0 for v in vals))
    return max(vals)

@lru_cache(None)
def all_ledgers(t,marked):
    """All triples (Q,L_M,L_U) for all trees and marks; n<=2 only."""
    j=influence(t)
    result={(F(0),j if marked else F(0),F(0) if marked else j)}
    for i in range(len(t).bit_length()-1):
        for a in all_ledgers(child(t,i,0),marked):
            for b in all_ledgers(child(t,i,1),marked):
                result.add((ia(t,i)+(a[0]+b[0])/2,(a[1]+b[1])/2,(a[2]+b[2])/2))
    if not marked: result.update(all_ledgers(t,True))
    for q,m,u in result:
        ck(q+m+u==j); counts['tree_mark_ledgers']+=1
    return frozenset(result)

for n in range(4):
    for bits in range(1<<(1<<n)):
        t=tuple(1-2*((bits>>x)&1) for x in range(1<<n)); counts['tables']+=1
        a=walsh(t)
        ck(sum(x*x for x in a)==len(t)**2)
        direct=tuple(sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(len(t))) for s in range(len(t)))
        ck(a==direct)
        ck(influence(t)==F(sum(s.bit_count()*x*x for s,x in enumerate(a)),len(t)**2))
        for i in range(n):
            ck(influence(t)==ia(t,i)+(influence(child(t,i,0))+influence(child(t,i,1)))/2)
            counts['query_nodes']+=1
        ck(envelopes(t,False)==0)
        if n<=2: all_ledgers(t,False)
        j=influence(t); p=tuple(F(x*x,len(t)**2) for x in a)
        if j:
            e=min(F(1,2),j/4); q=tuple((1-e)*x+e/len(t) for x in p)
            ck(sum(q)==1 and all(x>0 for x in q))
            lo,hi=klint(p,q); ck(lo>=-F(1,10**15)); ck(hi<=j)
            counts['rational_log_checks']+=1
        else: ck(max(p)==1)

for n in range(2,13):
    # Analytic-family formulas independently checked by explicit edges.
    t=(-1,)+(1,)*((1<<n)-1)
    j=influence(t); q=ia(t,0)+ia(child(t,0,0),0)/2
    marked=(influence(child(child(t,0,0),0,0))+influence(child(child(t,0,0),0,1)))/4
    ck(j==F(2*n,1<<n)); ck(q==F(4,1<<n)); ck(marked==F(2*(n-2),1<<n)); ck(q+marked==j)
    counts['point_defect_fixtures']+=1

counts['states']=envelopes.cache_info().currsize
result=dict(status='PASS',counts=counts,elapsed_seconds=time.perf_counter()-start,
    finite_scope='all truth tables n<=3; Bellman envelope over every adaptive stopped physical policy/persistent mark; all distinct exact ledger triples n<=2',
    universal_scope='analytic proof in PROOF.md, not finite inference',
    source_sha256=SPEC['helper_sha256'])
save('validation.json',result)
print(json.dumps(result))

"""Frozen exact finite checks; no floating point or optimization."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json, time, hashlib

assertions = 0
def check(ok):
    global assertions
    assert ok
    assertions += 1

def factors(n):
    ans = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            ans[p] = ans.get(p, 0)+1
            n //= p
        p += 1
    if n > 1: ans[n] = ans.get(n, 0)+1
    return ans

def clean(d): return {p:a for p,a in d.items() if a}
def plus(*terms):
    d = defaultdict(F)
    for scale, term in terms:
        for p, a in term.items(): d[p] += scale*a
    return clean(d)

def entropy(probs):
    d = defaultdict(F)
    for a in probs:
        if not a: continue
        for p,e in factors(a.numerator).items(): d[p] -= a*e
        for p,e in factors(a.denominator).items(): d[p] += a*e
    return clean(d)

def direct(t):
    return [sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t))]
def fwht(t):
    a = list(t); h = 1
    while h < len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):
                u,v = a[j],a[j+h]; a[j],a[j+h] = u+v,u-v
        h *= 2
    return a
def spectrum(t):
    a = direct(t)
    check(a == fwht(t))
    p = [F(x*x,len(t)**2) for x in a]
    check(sum(p) == 1)
    return p
def infl(p): return sum((s.bit_count()*a for s,a in enumerate(p)),F(0))
def edge_infl(t):
    n = (len(t)-1).bit_length()
    return [F(sum(t[x] != t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n)]
def table(n,b): return [1 if (b>>x)&1 else -1 for x in range(1<<n)]
def children(t,A,n):
    ai = [i for i in range(n) if (A>>i)&1]
    bi = [i for i in range(n) if not (A>>i)&1]
    return [[t[sum(((x>>j)&1)<<i for j,i in enumerate(ai))+sum(((y>>j)&1)<<i for j,i in enumerate(bi))] for y in range(1<<len(bi))] for x in range(1<<len(ai))]

start=time.perf_counter(); counts=defaultdict(int)
for n in range(4):
    for b in range(1<<(1<<n)):
        t=table(n,b); p=spectrum(t); h=entropy(p); ii=edge_infl(t)
        check(infl(p)==sum(ii)); counts['truth_tables']+=1
        for A in range(1,1<<n):
            ps=[spectrum(u) for u in children(t,A,n)]
            N=len(ps); B=[i for i in range(n) if not (A>>i)&1]
            q=[sum(p[s] for s in range(1<<n) if sum(((s>>i)&1)<<j for j,i in enumerate(B))==v) for v in range(1<<len(B))]
            check(q==[sum(z[v] for z in ps)/N for v in range(len(q))])
            avgh=plus(*[(F(1,N),entropy(z)) for z in ps]); hq=entropy(q)
            M=plus((1,h),(-1,hq)); J=plus((1,hq),(-1,avgh))
            check(plus((1,h),(-1,avgh))==plus((1,M),(1,J)))
            check(infl(p)==sum(infl(z) for z in ps)/N+sum(ii[i] for i in range(n) if (A>>i)&1))
            counts['nonempty_block_checks']+=1

for a in range(16):
    for b in range(16):
        t,u=table(2,a),table(2,b); p,q=spectrum(t),spectrum(u)
        pq=spectrum([t[x]*u[y] for y in range(4) for x in range(4)])
        check(pq==[p[x]*q[y] for y in range(4) for x in range(4)])
        check(entropy(pq)==plus((1,entropy(p)),(1,entropy(q))))
        check(infl(pq)==infl(p)+infl(q)); counts['tensor_pairs']+=1

for b in (1,2):
    g=table(1,b); pg=spectrum(g)
    for r in (1,2,3):
        p=F(1,1<<r)
        t=[g[x] if z==0 else 1 for z in range(1<<r) for x in range(2)]
        sp=spectrum(t)
        scalar=2*r*p*(2-p)
        expected=plus((p,entropy(pg)),(1,entropy([(1-p)**2])),(scalar,{2:F(1)}))
        check(entropy(sp)==expected)
        check(infl(sp)==p*(infl(pg)+r))
        check(F(t.count(-1),len(t))==p/2); counts['activation_cases']+=1

# A concrete restriction does not preserve the ratio: two-bit point defect.
sp=spectrum([1,1,1,-1]); check(entropy(sp)=={2:F(2)}); check(infl(sp)==1)
for u in children([1,1,1,-1],1,2): check(entropy(spectrum(u))=={})

out={'helper_version':'A051-exact-identities-v1','status':'PASS','counts':dict(counts),'assertions':assertions,'arithmetic':'Integer/Fraction/exact prime-log vectors','runtime_seconds':time.perf_counter()-start,'floating_sign_certificates':0,'full_FEI':'OPEN'}
target=Path(__file__).resolve().parent.parent/'out'/'CHECK_OUTPUT.json'
target.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

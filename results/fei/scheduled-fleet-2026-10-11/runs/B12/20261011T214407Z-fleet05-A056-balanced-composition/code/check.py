"""A056 v1: exact disjoint substitution checks; no numerical logarithms."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json, time, hashlib

RUN = Path(__file__).resolve().parents[1]
def table(n, code):
    return tuple(1 if (code >> x) & 1 else -1 for x in range(1 << n))
def char(x, s):
    return -1 if (x & s).bit_count() % 2 else 1
def walsh(t):
    return [Q(sum(v * char(x, s) for x, v in enumerate(t)), len(t)) for s in range(len(t))]
def influence(p):
    return sum((s.bit_count() * v for s, v in enumerate(p)), Q(0))
def factors(n):
    d, out = 2, {}
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0)+1
            n //= d
        d += 1
    if n > 1: out[n] = out.get(n, 0)+1
    return out
def add(a,b,c=Q(1)):
    out = a.copy()
    for k,v in b.items(): out[k] = out.get(k,Q(0))+c*v
    return {k:v for k,v in out.items() if v}
def entropy(p):
    out = {}
    for v in p:
        if not v: continue
        for n, sign in [(v.denominator,1),(v.numerator,-1)]:
            out = add(out,{k:Q(sign*e)*v for k,e in factors(n).items()})
    return out
def compose(h,gs):
    lens=[(len(g).bit_length()-1) for g in gs]
    vals=[]
    for x in range(1 << sum(lens)):
        idx, shift=0,0
        for i,(g,n) in enumerate(zip(gs,lens)):
            val=g[(x >> shift)&((1 << n)-1)]
            if val == -1: idx |= 1 << i
            shift += n
        vals.append(h[idx])
    return tuple(vals)

def check(h, gs):
    k=len(gs)
    a=[walsh(g) for g in gs]
    m=[v[0] for v in a]
    v=[1-z*z for z in m]
    active=[i for i in range(k) if v[i]]
    b={}
    weights={}
    for mask in range(1 << k):
        if any((mask >> i)&1 and not v[i] for i in range(k)): continue
        value=Q(0)
        for y in range(1 << k):
            prob=Q(1); term=Q(h[y])
            for i in range(k):
                yi=char(y,1 << i)
                prob *= (1+m[i]*yi)/2
                if (mask >> i)&1: term *= yi-m[i]
            value += prob*term
        scale=Q(1)
        for i in range(k):
            if (mask >> i)&1: scale *= v[i]
        b[mask]=value/scale
        weights[mask]=value*value/scale
    assert sum(weights.values()) == 1
    full=walsh(compose(h,gs)); p=[z*z for z in full]
    # Direct coefficient identity in an unnormalized centered basis.
    for s,coef in enumerate(full):
        blockmask=0; amp=Q(1); shift=0
        for i,g in enumerate(gs):
            n=len(g).bit_length()-1
            sub=(s >> shift)&((1 << n)-1)
            if sub:
                blockmask |= 1 << i
                amp *= a[i][sub]
            shift += n
        assert coef == b.get(blockmask,Q(0))*amp
    w=[sum((mass for mask,mass in weights.items() if (mask >> i)&1),Q(0)) for i in range(k)]
    rhs=entropy(list(weights.values()))
    irhs=Q(0)
    for i in active:
        q=[z*z/v[i] for z in a[i][1:]]
        assert sum(q) == 1
        rhs=add(rhs,entropy(q),w[i])
        irhs += w[i]*influence([z*z for z in a[i]])/v[i]
    assert entropy(p) == rhs
    assert influence(p) == irhs
    assert full[0] == b[0]
    return {'mean':str(full[0]),'influence':str(influence(p)),
            'entropy_prime_log_coefficients':{str(k):str(z) for k,z in entropy(p).items()},
            'spectrum':[str(z) for z in p], 'outer_weights':{str(k):str(z) for k,z in weights.items()}}

def main():
    start=time.perf_counter(); cases=0
    for hc in range(16):
        for ac in range(16):
            for bc in range(16):
                check(table(2,hc),[table(2,ac),table(2,bc)])
                cases += 1
    # Balanced three-bit majority, restricted to first coordinate +1.
    maj=tuple(1 if sum(char(x,1 << i) for i in range(3))>0 else -1 for x in range(8))
    or2=tuple(maj[x << 1] for x in range(4))
    and2=tuple(1 if x==0 else -1 for x in range(4))
    witness=check(and2,[or2,(1,-1)])
    # Physical restrictions of every balanced two-bit child, all partial assignments.
    restrictions=0
    for hc in range(16):
        for ac in range(16):
            a=table(2,ac)
            if sum(a): continue
            for fixed in product([None,1,-1],repeat=2):
                free=[i for i,z in enumerate(fixed) if z is None]
                child=[]
                for x in range(1 << len(free)):
                    idx=0
                    for i,z in enumerate(fixed):
                        bit=(x >> free.index(i))&1 if z is None else int(z==-1)
                        idx |= bit << i
                    child.append(a[idx])
                check(table(2,hc),[tuple(child),(1,-1)])
                restrictions += 1
    result={'helper_version':'A056-v1','all_two_bit_outer_and_two_bit_children':cases,
            'balanced_subcases':16*6*6,'physical_restriction_cases':restrictions,
            'arithmetic':'Fraction, integer Walsh, exact prime-log entropy vectors',
            'failed_assertions':0,'runtime_seconds':time.perf_counter()-start,
            'restricted_majority_AND_witness':witness}
    (RUN/'out'/'checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()

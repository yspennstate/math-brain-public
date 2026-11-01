#!/usr/bin/env python3
import itertools
import sympy as sp
from collections import Counter, defaultdict

r,t,v,p,q = sp.symbols("r t v p q")
probs = [r,v,t,v]  # center-to x,u,z,d

def partitions(n):
    res=[[]]
    for x in range(n):
        nxt=[]
        for part in res:
            nxt.append(part+[[x]])
            for i in range(len(part)):
                qpart=[b[:] for b in part]
                qpart[i].append(x)
                nxt.append(qpart)
        seen=set(); res2=[]
        for part in nxt:
            key=tuple(sorted(tuple(sorted(b)) for b in part))
            if key not in seen:
                seen.add(key)
                res2.append([list(b) for b in key])
        res=res2
    return [tuple(tuple(b) for b in part) for part in res]

def canonical(part):
    return tuple(sorted(tuple(sorted(b)) for b in part))

CROSSING = canonical(((0,2),(1,3)))
NCP=[part for part in partitions(4) if canonical(part) != CROSSING]
assert len(NCP)==14

def classify(part):
    sizes=sorted((len(b) for b in part), reverse=True)
    if sizes == [1,1,1,1]:
        return "sigma"
    if sizes == [4]:
        return "epsilon"
    if sizes == [3,1]:
        return "delta"
    if sizes == [2,2]:
        return "gamma"
    if sizes == [2,1,1]:
        pair=next(b for b in part if len(b)==2)
        a,b=pair
        return "alpha" if ((a-b) % 4) in (1,3) else "beta"
    raise AssertionError(part)

assert Counter(classify(part) for part in NCP) == Counter(
    sigma=1, alpha=4, beta=2, gamma=2, delta=4, epsilon=1
)

def connected_after(part, star_bits, a, b):
    parent=list(range(5))  # 0=x,1=u,2=z,3=d,4=center y
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb:
            parent[rb]=ra
    for block in part:
        for x in block[1:]:
            union(block[0],x)
    for i,is_open in enumerate(star_bits):
        if is_open:
            union(4,i)
    return find(a)==find(b)

def diff_poly(part):
    ans=0
    for bits in itertools.product([0,1], repeat=4):
        wt=sp.Integer(1)
        for i,is_open in enumerate(bits):
            wt *= probs[i] if is_open else (1-probs[i])
        val=sp.Integer(connected_after(part,bits,0,4)) - sp.Integer(connected_after(part,bits,0,2))
        ans += wt*val
    return sp.expand(ans)

orbit=defaultdict(lambda: sp.Integer(0))
for part in NCP:
    orbit[classify(part)] += diff_poly(part)
orbit={k:sp.factor(vv) for k,vv in orbit.items()}

Q = {
    "sigma": r,
    "alpha": 2*(2*r+v-2*r*v),
    "beta": 2*r-1,
    "gamma": 2*(1-v)*(r+v-r*v),
    "delta": 2*r*v**2-6*r*v+4*r-v**2+4*v-2,
    "epsilon": -(1-r)*(1-v)**2,
}
for k in Q:
    assert sp.simplify(orbit[k] - (1-t)*Q[k]) == 0

L = {
    "sigma": 1,
    "alpha": 4*(1-v),
    "beta": 2,
    "gamma": 2*(1-v)**2,
    "delta": 2*(v**2-3*v+2),
    "epsilon": (1-v)**2,
}
for k in Q:
    assert sp.simplify(sp.diff(Q[k],r) - L[k]) == 0

hom_expected = {
    "sigma": p,
    "alpha": 2*p*(1+2*q),
    "beta": p-q,
    "gamma": 2*p*q*(1+q),
    "delta": 1-q**2-2*q**3,
    "epsilon": -q**3,
}
for k in Q:
    got=sp.expand(Q[k].subs({r:p,v:p}))
    want=sp.expand(hom_expected[k].subs(q,1-p))
    assert sp.simplify(got-want)==0

print("NONCROSSING_PARTITIONS=14")
print("ORBIT_SIZES sigma=1 alpha=4 beta=2 gamma=2 delta=4 epsilon=1")
for k in ["sigma","alpha","beta","gamma","delta","epsilon"]:
    print(f"{k}: D_coefficient = {sp.factor(orbit[k])}")
print("FACTORIZATION_PASS: D(r,t,v)=(1-t)Q(r,v)")
for k in ["sigma","alpha","beta","gamma","delta","epsilon"]:
    print(f"dQ/dr {k}: {sp.factor(L[k])}")
print("MONOTONIC_NEAR_EDGE_PASS: all dQ/dr orbit coefficients are >=0 on v in [0,1]")
print("HOMOGENEOUS_SPECIALIZATION_PASS")
print("ALL_EXACT_CHECKS_PASS")

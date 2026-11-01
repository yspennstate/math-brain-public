#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from itertools import product
from collections import defaultdict
import math

CHECKS = 0

def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def canon_partition(part):
    return tuple(sorted((tuple(sorted(b)) for b in part), key=lambda x:(len(x), x)))

def set_partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for rest in set_partitions(items[1:]):
        # singleton block
        yield ((first,),) + rest
        # insert first in each existing block
        for i in range(len(rest)):
            new = [tuple(b) for b in rest]
            new[i] = tuple(sorted((first,) + new[i]))
            yield tuple(new)

def unique_partitions(items):
    d = {}
    for p in set_partitions(tuple(items)):
        cp = canon_partition(p)
        d[cp] = cp
    return list(d.values())

def rising(theta, r):
    out = 1
    for j in range(r):
        out *= theta + j
    return out

def ewens_prob(part, theta):
    r = sum(len(b) for b in part)
    k = len(part)
    num = theta ** k
    for b in part:
        num *= math.factorial(len(b)-1)
    return Fraction(num, rising(theta, r))

# 1) Exact Ewens EPPF normalization.
for theta in range(1, 13):
    for r in range(1, 8):
        ps = unique_partitions(range(r))
        s = sum((ewens_prob(p,theta) for p in ps), Fraction(0))
        check(s == 1, f"Ewens normalization failed theta={theta}, r={r}")

# 2) Exact sampling consistency under deletion of the final label.
for theta in range(1, 9):
    for r in range(1, 7):
        big = unique_partitions(range(r+1))
        agg = defaultdict(Fraction)
        for p in big:
            restricted=[]
            for b in p:
                bb=tuple(x for x in b if x<r)
                if bb:
                    restricted.append(bb)
            agg[canon_partition(restricted)] += ewens_prob(p,theta)
        small = unique_partitions(range(r))
        for p in small:
            check(agg[p] == ewens_prob(p,theta),
                  f"sampling consistency failed theta={theta}, r={r}, p={p}")

# 3) Pair-collision probability is exactly 1/(theta+1).
for theta in range(1, 101):
    for r in range(2, 8):
        pr = Fraction(0)
        for p in unique_partitions(range(r)):
            same = any(0 in b and 1 in b for b in p)
            if same:
                pr += ewens_prob(p,theta)
        check(pr == Fraction(1,theta+1),
              f"pair collision failed theta={theta}, r={r}: {pr}")

# 4) Kingman tangent: specified pair-only event is c+O(c^2),
# and all non-Kingman merger mass is O_r(c^2). Exact bounded-grid check.
# We record conservative bounds depending only on r<=7.
max_pair_ratio = Fraction(0)
max_bad_ratio = Fraction(0)
for theta in range(3, 101):
    c = Fraction(1,theta+1)
    for r in range(2, 8):
        ps = unique_partitions(range(r))
        # specified pair {0,1}, all others singleton
        target = canon_partition(((0,1),) + tuple((j,) for j in range(2,r)))
        p_pair = ewens_prob(target,theta)
        pair_ratio = abs(p_pair-c)/(c*c)
        if pair_ratio > max_pair_ratio:
            max_pair_ratio = pair_ratio
        # bad = any merger pattern with deficiency >=2
        bad = Fraction(0)
        for p in ps:
            deficiency = r-len(p)
            if deficiency >= 2:
                bad += ewens_prob(p,theta)
        bad_ratio = bad/(c*c)
        if bad_ratio > max_bad_ratio:
            max_bad_ratio = bad_ratio
        check(pair_ratio <= 30, f"pair tangent grid bound failed theta={theta},r={r}")
        check(bad_ratio <= 1000, f"bad mass grid bound failed theta={theta},r={r}")

# 5) Exact N=3 root-degree law for C019.
theta = 3
N = 3
delta = Fraction(1,N)
c = Fraction(1,theta+1)
u = delta*c/Fraction(2,1)
check(c == Fraction(1,4), "N=3 c")
check(u == Fraction(1,24), "N=3 u")

ORIG = frozenset(range(3))
def blockcanon(blocks):
    return canon_partition(tuple(tuple(sorted(b)) for b in blocks))

def split_id(S):
    S=frozenset(S)
    if len(S)==0 or len(S)==3:
        return None
    if len(S)==1:
        return next(iter(S))
    return next(iter(ORIG-S))

def mark_outcomes(blocks):
    out=defaultdict(Fraction)
    ids=[split_id(b) for b in blocks]
    for bits in product((0,1), repeat=len(blocks)):
        p=Fraction(1)
        add=set()
        for bit,sid in zip(bits,ids):
            if bit:
                p*=u
                if sid is not None:
                    add.add(sid)
            else:
                p*=1-u
        out[frozenset(add)] += p
    return out

def ewens_merge_outcomes(blocks):
    r=len(blocks)
    out=defaultdict(Fraction)
    for p in unique_partitions(range(r)):
        prob=ewens_prob(p,theta)
        merged=[]
        for g in p:
            U=set()
            for idx in g:
                U.update(blocks[idx])
            merged.append(frozenset(U))
        out[blockcanon(merged)] += prob
    return out

def one_step(state):
    blocks_t, marks = state
    blocks=tuple(frozenset(b) for b in blocks_t)
    out=defaultdict(Fraction)
    for add,p1 in mark_outcomes(blocks).items():
        m2=frozenset(set(marks)|set(add))
        for nb,p2 in ewens_merge_outcomes(blocks).items():
            out[(nb,m2)] += p1*p2
    check(sum(out.values(),Fraction(0))==1, f"one-step law not normalized state={state}")
    return out

@lru_cache(None)
def absorption_degree_law(state):
    blocks_t, marks = state
    if len(blocks_t)==1:
        deg = 0 if len(marks)==0 else (2 if len(marks)==1 else 3)
        return {deg:Fraction(1)}
    trans=one_step(state)
    p_self=trans.pop(state, Fraction(0))
    den=1-p_self
    check(den>0, f"absorbing recursion zero escape state={state}")
    accum=defaultdict(Fraction)
    for ns,p in trans.items():
        law=absorption_degree_law(ns)
        for d,q in law.items():
            accum[d] += p*q
    return {d:q/den for d,q in accum.items()}

start=(blockcanon(({0},{1},{2})), frozenset())
law=absorption_degree_law(start)
p_none=law.get(0,Fraction(0))
p_deg2=law.get(2,Fraction(0))
p_deg3=law.get(3,Fraction(0))
check(p_none+p_deg2+p_deg3==1, "root law sum")
check(p_none == Fraction(25124855,39907503), f"p_none mismatch {p_none}")
check(p_deg2 == Fraction(4318756,13302501), f"p_deg2 mismatch {p_deg2}")
check(p_deg3 == Fraction(1826380,39907503), f"p_deg3 mismatch {p_deg3}")
reduced = p_deg3/(1-p_none)
check(reduced == Fraction(456595,3695662), f"reduced witness mismatch {reduced}")

previous = [
    Fraction(0,1), Fraction(1,10), Fraction(1,22), Fraction(1,6),
    Fraction(1,728), Fraction(1,7), Fraction(1,71), Fraction(1,71),
    Fraction(0,1), Fraction(0,1), Fraction(2,105),
    Fraction(21521,4909716), Fraction(35,1296), Fraction(14,2201),
    Fraction(2,17), Fraction(40589,352998), Fraction(70135,515173),
    Fraction(81178,877951),
]
for idx,x in enumerate(previous, start=1):
    check(reduced != x, f"C019 witness collides with C{idx:03d}")

print("R11 I0054 C019 Ewens-boundary ancestral compiler exact checker")
print("Ewens EPPF normalization: PASS")
print("sampling consistency under deletion: PASS")
print("pair collision c_theta = 1/(theta+1): PASS")
print("large-theta Kingman tangent finite-grid checks: PASS")
print(f"max |p_pair-c|/c^2 on grid = {max_pair_ratio}")
print(f"max non-Kingman-mass/c^2 on grid = {max_bad_ratio}")
print(f"N=3 theta={theta} delta={delta} c={c} mark_u={u}")
print(f"N=3 P(no visible refinement)={p_none}")
print(f"N=3 P(raw degree-2)={p_deg2}")
print(f"N=3 P(raw degree-3)={p_deg3}")
print(f"N=3 reduced root degree-3 witness={reduced}")
print("comparison with C001-C018 retained witnesses: PASS")
print(f"exact checks executed: {CHECKS}")
print("ALL_EXACT_CHECKS_PASS")

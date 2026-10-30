#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product

N = 8
COVERS = [
    (1,2),(1,6),(2,0),(2,7),(3,0),(3,4),
    (4,7),(5,7),(6,0),(6,4),(6,5),
]
HEAVY = (2,0,5)  # x,y,a
CHAIN_COVER = [(1,2,0),(3,4,7),(6,5)]
ANTICHAIN = (2,3,5)

def closure(n, edges):
    r = [[False]*n for _ in range(n)]
    for u,v in edges:
        r[u][v] = True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]:
                        r[i][j] = True
    assert not any(r[i][i] for i in range(n))
    return r

R = closure(N, COVERS)

def is_cover(u,v):
    return R[u][v] and not any(k not in (u,v) and R[u][k] and R[k][v] for k in range(N))

assert sorted((u,v) for u in range(N) for v in range(N) if u != v and is_cover(u,v)) == sorted(COVERS)

def enumerate_extensions():
    pred = [0]*N
    for j in range(N):
        for i in range(N):
            if R[i][j]:
                pred[j] |= 1 << i
    full = (1 << N) - 1
    out = []
    def rec(mask, word):
        if mask == full:
            out.append(tuple(word))
            return
        for v in range(N):
            if not (mask >> v) & 1 and pred[v] & ~mask == 0:
                rec(mask | (1 << v), word + [v])
    rec(0, [])
    return out

EXT = enumerate_extensions()
E = len(EXT)
assert E == 108
POS = []
for L in EXT:
    p = [0]*N
    for i,v in enumerate(L):
        p[v] = i
    POS.append(p)

def count_before(u,v):
    return sum(p[u] < p[v] for p in POS)

def incomparable(u,v):
    return not R[u][v] and not R[v][u]

def chain(seq):
    return all(R[seq[i]][seq[i+1]] for i in range(len(seq)-1))

assert all(chain(c) for c in CHAIN_COVER)
assert sorted(v for c in CHAIN_COVER for v in c) == list(range(N))
assert all(incomparable(u,v) for u,v in combinations(ANTICHAIN,2))

def max_antichain_size():
    best = 0
    for mask in range(1 << N):
        if mask.bit_count() <= best:
            continue
        S = [i for i in range(N) if (mask >> i) & 1]
        if all(incomparable(u,v) for u,v in combinations(S,2)):
            best = len(S)
    return best
assert max_antichain_size() == 3

def connected(use_incomparability):
    adj = [set() for _ in range(N)]
    for u,v in combinations(range(N),2):
        comp = R[u][v] or R[v][u]
        if ((not comp) if use_incomparability else comp):
            adj[u].add(v); adj[v].add(u)
    seen = {0}; stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u] - seen:
            seen.add(v); stack.append(v)
    return len(seen) == N
assert connected(False) and connected(True)

def autonomous_subsets():
    out = []
    for mask in range(1,(1 << N)-1):
        if mask.bit_count() == 1:
            continue
        S = [i for i in range(N) if (mask >> i) & 1]
        ok = True
        for z in range(N):
            if z in S:
                continue
            rel = None
            for s in S:
                q = -1 if R[z][s] else (1 if R[s][z] else 0)
                if rel is None:
                    rel = q
                elif q != rel:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(S))
    return out
assert autonomous_subsets() == []

PAIR_COUNTS = {}
for u,v in combinations(range(N),2):
    if incomparable(u,v):
        PAIR_COUNTS[(u,v)] = count_before(u,v)

EXPECTED = {
    (0,4):31,
    (0,5):27,
    (0,7):75,
    (1,3):82,
    (2,3):33,
    (2,4):85,
    (2,5):79,
    (2,6):35,
    (3,5):94,
    (3,6):60,
    (4,5):47,
}
assert PAIR_COUNTS == EXPECTED
BALANCED = {pair:c for pair,c in PAIR_COUNTS.items() if E <= 3*c <= 2*E}
assert BALANCED == {(3,6):60,(4,5):47}

x,y,a = HEAVY
assert is_cover(x,y) and incomparable(a,x) and incomparable(a,y)
A = count_before(a,x)
C = count_before(y,a)
H = E-A-C
assert (A,H,C) == (29,52,27)
assert 11*A < 3*E and 11*C < 3*E and 3*H > E

def maximal(S):
    return [u for u in S if not any(u != v and R[u][v] for v in S)]
def minimal(S):
    return [u for u in S if not any(u != v and R[v][u] for v in S)]

def canonical_sets(x,y,a):
    TL = maximal([t for t in range(N) if R[t][a] and incomparable(t,x)])
    UL = minimal([s for s in range(N) if R[x][s] and incomparable(s,a)])
    UR = minimal([u for u in range(N) if R[a][u] and incomparable(u,y)])
    TR = maximal([r for r in range(N) if R[r][y] and incomparable(r,a)])
    CL = sorted(set(TL) | (set(UL)-{y}))
    CR = sorted(set(UR) | (set(TR)-{x}))
    return TL,UL,UR,TR,CL,CR

TL,UL,UR,TR,CL,CR = canonical_sets(x,y,a)
assert (TL,UL,UR,TR,CL,CR) == ([6],[0],[7],[2,3],[6],[3,7])

lam = {v:0 for v in CL}
rho = {v:0 for v in CR}
BL = BR = 0
for p in POS:
    if not (p[x] < p[a] < p[y]):
        continue
    left = [v for v in CL if p[x] < p[v] < p[a]]
    if left:
        BL += 1
        v = min(left, key=lambda z:p[z])
        lam[v] += 1
    right = [v for v in CR if p[a] < p[v] < p[y]]
    if right:
        BR += 1
        v = min(right, key=lambda z:p[z])
        rho[v] += 1

assert (BL,BR,lam,rho) == (23,25,{6:23},{3:6,7:19})
assert 33*lam[6] > 2*E
assert 33*rho[7] > 2*E

# Lead r16 boundary-anchor recoding: all immediate boundary pairs remain unbalanced.
boundary = {
    "F2_6_pair_(6,2)_minority_2<6": count_before(2,6),
    "F3_7_pair_(0,7)_minority_7<0": count_before(7,0),
    "F4_3_pair_(3,2)_minority_2<3": count_before(2,3),
}
assert boundary == {
    "F2_6_pair_(6,2)_minority_2<6":35,
    "F3_7_pair_(0,7)_minority_7<0":33,
    "F4_3_pair_(3,2)_minority_2<3":33,
}
assert all(3*c < E for c in boundary.values())

def strong(u,v):
    if R[u][v]:
        return True
    if R[v][u]:
        return False
    return 3*count_before(u,v) > 2*E

def interior(u,v):
    return [z for z in range(N) if z not in (u,v) and strong(u,z) and strong(z,v)]

assert interior(x,a) == []
assert interior(a,y) == []

# The two same-left-ray blockers 6 (F2) and 3 (F4) form the width-saturating gate,
# and their cross-pair is exactly where a balance witness appears.
assert incomparable(3,6)
assert all(incomparable(u,v) for u,v in combinations((2,3,6),2))
assert count_before(3,6) == 60
assert E <= 3*count_before(3,6) <= 2*E

# Both lead-selected >2E/33 packets create genuine reciprocal heavy children.
def heavy_counts(x,y,a):
    assert is_cover(x,y) and incomparable(a,x) and incomparable(a,y)
    aa = count_before(a,x)
    cc = count_before(y,a)
    hh = E-aa-cc
    return aa,hh,cc

left_child = (6,5,2)
right_child = (5,7,0)
assert heavy_counts(*left_child) == (35,44,29)
assert heavy_counts(*right_child) == (27,48,33)
assert count_before(6,2) == 73 and 3*73 > 2*E
assert count_before(5,2) == 29 and 3*29 < E
assert count_before(5,0) == 81 and 3*81 > 2*E
assert count_before(7,0) == 33 and 3*33 < E

# The same balanced cross-pair (4,5) is exposed on the immediate child frontiers.
Lsets = canonical_sets(*left_child)
Rsets = canonical_sets(*right_child)
assert 4 in (set(Lsets[1])-{left_child[1]})  # UL\{y}
assert 4 in (set(Rsets[3])-{right_child[0]}) # TR\{x}
assert count_before(4,5) == 47 and E <= 3*47 <= 2*E

print("POS3_R16_OPPOSITE_RAY_FRONTIER_ADVERSARY_PASS")
print("E", E)
print("covers", COVERS)
print("chain_cover", CHAIN_COVER, "antichain", ANTICHAIN)
print("connected_comparability", connected(False), "connected_incomparability", connected(True))
print("autonomous_nontrivial", autonomous_subsets())
print("heavy_state", HEAVY, "A_H_C", (A,H,C),
      "fractions", tuple(str(Fraction(z,E)) for z in (A,H,C)))
print("canonical", {"TL":TL,"UL":UL,"UR":UR,"TR":TR,"CL":CL,"CR":CR})
print("bad_swap", {"BL":BL,"BR":BR,"lambda":lam,"rho":rho,"2E/33":str(Fraction(2*E,33))})
print("boundary_minorities", {k:str(Fraction(v,E)) for k,v in boundary.items()})
print("old_span_interiors", {"x_to_a":interior(x,a),"a_to_y":interior(a,y)})
print("same_left_ray_gate_cross", "(3,6)", str(Fraction(count_before(3,6),E)))
print("children", {"left":left_child,"left_AHC":heavy_counts(*left_child),
                   "right":right_child,"right_AHC":heavy_counts(*right_child)})
print("child_exposed_balance", "(4,5)", str(Fraction(count_before(4,5),E)))
print("all_incomparable_probabilities")
for pair,c in sorted(PAIR_COUNTS.items()):
    print(pair, c, "/", E, "=", Fraction(c,E),
          "BALANCED" if E <= 3*c <= 2*E else "UNBALANCED")

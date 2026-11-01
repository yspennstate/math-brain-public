#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict

# NM13-05 / C0146 exact positive-q counterexample.
# Pure standard-library exact arithmetic; no floating point is used for claims.

V = tuple(range(7))
E = (
    (0,1),(0,2),(0,3),(0,4),(0,5),
    (1,2),(1,3),(1,4),(1,6),(5,6),
)
M = len(E)
DIST = 0  # distinguished edge index, e*=(0,1)

def component_count(mask):
    p = list(V)
    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x
    for i,(u,v) in enumerate(E):
        if (mask >> i) & 1:
            a,b = find(u),find(v)
            if a != b:
                p[b] = a
    return len({find(v) for v in V})

def connected_without(skip=None):
    verts = [v for v in V if v != skip]
    if len(verts) <= 1:
        return True
    adj = {v: [] for v in verts}
    for u,v in E:
        if u == skip or v == skip:
            continue
        adj[u].append(v)
        adj[v].append(u)
    seen = {verts[0]}
    stack = [verts[0]]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(verts)

assert len(set(E)) == M
assert all(u < v for u,v in E)
assert connected_without()
assert all(connected_without(v) for v in V)  # 2-connected witness

# Count configurations simultaneously by (edge count r, cycle nullity c).
# For n=7, c(A)=|A|-7+k(A), where k(A) is the component count.
all_count = defaultdict(int)
edge_count = defaultdict(int)
for mask in range(1 << M):
    r = mask.bit_count()
    k = component_count(mask)
    c = r - len(V) + k
    assert c >= 0
    all_count[(r,c)] += 1
    if (mask >> DIST) & 1:
        edge_count[(r,c)] += 1

expected_all = {
    0:[1,0,0,0,0],
    1:[10,0,0,0,0],
    2:[45,0,0,0,0],
    3:[117,3,0,0,0],
    4:[185,25,0,0,0],
    5:[168,81,3,0,0],
    6:[68,123,19,0,0],
    7:[0,74,45,1,0],
    8:[0,0,39,6,0],
    9:[0,0,0,10,0],
    10:[0,0,0,0,1],
}
expected_edge = {
    0:[0,0,0,0,0],
    1:[1,0,0,0,0],
    2:[9,0,0,0,0],
    3:[33,3,0,0,0],
    4:[62,22,0,0,0],
    5:[60,63,3,0,0],
    6:[24,84,18,0,0],
    7:[0,44,39,1,0],
    8:[0,0,30,6,0],
    9:[0,0,0,9,0],
    10:[0,0,0,0,1],
}
for r in range(M+1):
    assert [all_count[(r,c)] for c in range(5)] == expected_all[r]
    assert [edge_count[(r,c)] for c in range(5)] == expected_edge[r]

# q -> 0 forest mechanism: the edge marginal decreases between fixed forest
# sizes 5 and 6, yielding an exact Hall obstruction to an inclusion coupling.
forest5 = all_count[(5,0)]
forest6 = all_count[(6,0)]
edge_forest5 = edge_count[(5,0)]
edge_forest6 = edge_count[(6,0)]
f5 = Fraction(edge_forest5, forest5)
f6 = Fraction(edge_forest6, forest6)
assert (forest5, forest6, edge_forest5, edge_forest6) == (168,68,60,24)
assert f5 == Fraction(5,14)
assert f6 == Fraction(6,17)
assert f5 - f6 == Fraction(1,238) > 0

# Forest-fugacity edge marginal N(x)/D(x).
D = [1,10,45,117,185,168,68]
N = [0,1,9,33,62,60,24]

def conv(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out

def derivative(a):
    return [(i+1)*a[i+1] for i in range(len(a)-1)]

A = conv(derivative(N), D)
B = conv(N, derivative(D))
L = max(len(A),len(B))
A += [0]*(L-len(A))
B += [0]*(L-len(B))
deriv_num = [A[i]-B[i] for i in range(L)]
while deriv_num and deriv_num[-1] == 0:
    deriv_num.pop()

# -(2x+1)^4(3x^6-34x^5-85x^4-82x^3-40x^2-10x-1).
linear4 = [1,8,24,32,16]  # (1+2x)^4, ascending coefficients
sextic = [-1,-10,-40,-82,-85,-34,3]
factorized = [-z for z in conv(linear4,sextic)]
assert deriv_num == factorized

# Direct positive-q source counterexample.
q = Fraction(1,40000)
x1 = Fraction(20)
x2 = Fraction(25)
p1 = Fraction(1,2001)
p2 = Fraction(1,1601)
assert p1 == x1*q/(1+x1*q)
assert p2 == x2*q/(1+x2*q)
assert 0 < p1 < p2 < 1

def transformed_edge_probability(q,x):
    den = Fraction(0)
    num = Fraction(0)
    for mask in range(1 << M):
        r = mask.bit_count()
        c = r - len(V) + component_count(mask)
        w = (x**r) * (q**c)
        den += w
        if (mask >> DIST) & 1:
            num += w
    return num/den

def original_fk_edge_probability(q,p):
    den = Fraction(0)
    num = Fraction(0)
    for mask in range(1 << M):
        r = mask.bit_count()
        k = component_count(mask)
        w = (p**r) * ((1-p)**(M-r)) * (q**k)
        den += w
        if (mask >> DIST) & 1:
            num += w
    return num/den

P1 = transformed_edge_probability(q,x1)
P2 = transformed_edge_probability(q,x2)
P1_original = original_fk_edge_probability(q,p1)
P2_original = original_fk_edge_probability(q,p2)
assert P1 == P1_original
assert P2 == P2_original
assert P1 == Fraction(72488985858351,205113593435351)
assert P2 == Fraction(108671022567040625,307499119349131441)
drop = P1-P2
assert drop == Fraction(
    395372934751065824378379416,
    63072249347906220400541234970791,
)
assert drop > 0

# A monotone coupling for p1 < p2 would force the increasing event
# {distinguished edge open} to have nondecreasing probability. The exact
# strict reverse inequality above therefore certifies nonexistence.
print("vertices", len(V))
print("edges", M)
print("edge_list", E)
print("distinguished_edge", E[DIST])
print("forest_counts_r0_to_r6", D)
print("edge_forest_counts_r0_to_r6", N)
print("forest_level_5_edge_prob", f5)
print("forest_level_6_edge_prob", f6)
print("forest_level_drop", f5-f6)
print("q", q)
print("p1", p1)
print("p2", p2)
print("x1", x1)
print("x2", x2)
print("edge_prob_p1", P1)
print("edge_prob_p2", P2)
print("exact_edge_marginal_drop", drop)
print("original_weight_match", P1 == P1_original and P2 == P2_original)
print("graph_is_2_connected", connected_without() and all(connected_without(v) for v in V))
print("ALL_EXACT_CHECKS_PASS")

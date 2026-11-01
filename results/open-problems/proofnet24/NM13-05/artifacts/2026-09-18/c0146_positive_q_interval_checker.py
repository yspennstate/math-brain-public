#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict

V = tuple(range(7))
E = (
    (0,1),(0,2),(0,3),(0,4),(0,5),
    (1,2),(1,3),(1,4),(1,6),(5,6),
)
M = len(E)
DIST = 0


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
        adj[u].append(v); adj[v].append(u)
    seen = {verts[0]}; stack=[verts[0]]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==len(verts)

assert connected_without() and all(connected_without(v) for v in V)

# Exact counts by (r,c), recomputed by exhaustive enumeration.
all_count = defaultdict(int)
edge_count = defaultdict(int)
for mask in range(1 << M):
    r = mask.bit_count()
    c = r - len(V) + component_count(mask)
    assert c >= 0
    all_count[(r,c)] += 1
    if (mask >> DIST) & 1:
        edge_count[(r,c)] += 1

# q=0 (arboreal-gas) fixed-level obstruction.
f5 = Fraction(edge_count[(5,0)], all_count[(5,0)])
f6 = Fraction(edge_count[(6,0)], all_count[(6,0)])
assert f5 == Fraction(5,14)
assert f6 == Fraction(6,17)
assert f5-f6 == Fraction(1,238)

# For q>0, after x=p/[q(1-p)] the FK weight is proportional to x^r q^c.
# Return coefficient lists in ascending powers of q for denominator and edge numerator.
def q_polys(x):
    maxc = max(c for r,c in all_count if all_count[(r,c)])
    D = [0]*(maxc+1)
    N = [0]*(maxc+1)
    for (r,c),a in all_count.items():
        D[c] += a * (x**r)
    for (r,c),a in edge_count.items():
        N[c] += a * (x**r)
    while D and D[-1] == 0: D.pop()
    while N and N[-1] == 0: N.pop()
    return D,N

D20,N20 = q_polys(20)
D25,N25 = q_polys(25)

assert D20 == [4920154201,102855224000,1057225600000,5274880000000,10240000000000]
assert N20 == [1738187620,61901144000,819081600000,4762880000000,10240000000000]
assert D25 == [18316309626,482490281250,6230253906250,39068603515625,95367431640625]
assert N25 == [6470052525,289686375000,4820097656250,35253906250000,95367431640625]


def conv(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out

A=conv(N20,D25)
B=conv(N25,D20)
H=[a-b for a,b in zip(A,B)]
while H and H[-1]==0: H.pop()
expected_H=[
    3526524430622595,
    -118321183332671706000,
    -4653083103659709181250,
    -73613777846263924687500,
    -612669333551171376953125,
    -2953816334960937500000000,
    -8152236328125000000000000,
    -9765625000000000000000000,
]
assert H == expected_H
assert H[0] > 0 and all(a < 0 for a in H[1:])


def eval_poly(coeffs,q):
    s=Fraction(0)
    p=Fraction(1)
    for a in coeffs:
        s += a*p
        p *= q
    return s

q0=Fraction(1,40000)
Hq0=eval_poly(H,q0)
assert Hq0 == Fraction(148264850531649684141892281,262144000000)
assert Hq0 > 0

# Since H has positive constant term and all other coefficients negative,
# H'(q)<0 for every q>0; hence H(q)>=H(q0)>0 on 0<q<=q0.
# Therefore N20/D20 > N25/D25 throughout that interval.
for q in (Fraction(1,1000000), Fraction(1,40000)):
    assert eval_poly(H,q) > 0
    P20 = eval_poly(N20,q) / eval_poly(D20,q)
    P25 = eval_poly(N25,q) / eval_poly(D25,q)
    assert P20 > P25

# Endpoint rational source witness.
p1 = Fraction(20)*q0/(1+Fraction(20)*q0)
p2 = Fraction(25)*q0/(1+Fraction(25)*q0)
assert p1 == Fraction(1,2001)
assert p2 == Fraction(1,1601)
assert p1 < p2
P1=eval_poly(N20,q0)/eval_poly(D20,q0)
P2=eval_poly(N25,q0)/eval_poly(D25,q0)
assert P1 == Fraction(72488985858351,205113593435351)
assert P2 == Fraction(108671022567040625,307499119349131441)
drop=P1-P2
assert drop == Fraction(395372934751065824378379416,63072249347906220400541234970791)
assert drop > 0

print('vertices',len(V))
print('edges',M)
print('edge_list',E)
print('distinguished_edge',E[DIST])
print('forest_level_5_edge_prob',f5)
print('forest_level_6_edge_prob',f6)
print('forest_level_drop',f5-f6)
print('D20',D20)
print('N20',N20)
print('D25',D25)
print('N25',N25)
print('H_coefficients',H)
print('H_at_1_over_40000',Hq0)
print('positive_interval','0 < q <= 1/40000')
print('q_endpoint',q0)
print('p1_endpoint',p1)
print('p2_endpoint',p2)
print('edge_prob_p1',P1)
print('edge_prob_p2',P2)
print('exact_edge_marginal_drop',drop)
print('graph_is_2_connected',connected_without() and all(connected_without(v) for v in V))
print('ALL_EXACT_CHECKS_PASS')

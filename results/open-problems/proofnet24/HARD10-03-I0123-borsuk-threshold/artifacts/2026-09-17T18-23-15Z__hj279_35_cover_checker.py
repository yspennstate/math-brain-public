#!/usr/bin/env python3
"""Exact finite certificate for I0123's Hall--Janko--Wales rank-62 candidate.

Pure Python / integer arithmetic only.  The graph is reconstructed from the
source-described 5^2:4 Cayley model of the Hall--Janko graph, its 280 decads
are recovered as the maximum independent sets, the regular two-graph relation
(intersection size 2) is formed, and the 279-vertex descendant is obtained by
Seidel switching at one decade and deleting it.

The decisive certificate is an explicit 35-clique partition of the descendant,
so its clique-cover number is <=35 (hence certainly <64).  Therefore this
particular rank-62 two-distance candidate cannot be a Borsuk counterexample in
R^62.
"""
from collections import Counter

# ---------- bitset helpers ----------
def bits(x):
    while x:
        b = x & -x
        yield b.bit_length() - 1
        x ^= b


def make_adj(n):
    return [0] * n


def add_edge(adj, u, v):
    assert u != v
    adj[u] |= 1 << v
    adj[v] |= 1 << u


def edge_count(adj):
    return sum(a.bit_count() for a in adj) // 2


def degree_set(adj):
    return {a.bit_count() for a in adj}


def common_hist(adj):
    n = len(adj)
    eh = Counter()
    nh = Counter()
    for u in range(n):
        for v in range(u + 1, n):
            c = (adj[u] & adj[v]).bit_count()
            if (adj[u] >> v) & 1:
                eh[c] += 1
            else:
                nh[c] += 1
    return eh, nh


def complement(adj):
    n = len(adj)
    full = (1 << n) - 1
    out = [0] * n
    for i in range(n):
        out[i] = full ^ (1 << i) ^ adj[i]
    return out


# ---------- Hall--Janko Cayley graph on F_5^2 semidirect C_4 ----------
# The order-4 automorphism is T(x,y)=(-2y,-2x), all arithmetic mod 5.
def T1(v):
    x, y = v
    return ((-2 * y) % 5, (-2 * x) % 5)


def Tpow(v, t):
    for _ in range(t % 4):
        v = T1(v)
    return v


def mul(g, h):
    (x, y), t = g
    (a, b), s = h
    a, b = Tpow((a, b), t)
    return (((x + a) % 5, (y + b) % 5), (t + s) % 4)


def inv(g):
    (x, y), t = g
    # -(T^{-t}(x,y)), -t
    a, b = Tpow((x, y), (-t) % 4)
    return (((-a) % 5, (-b) % 5), (-t) % 4)


# Source display: four 5x5 blocks are the neighbors of the starred identity.
# Centered display coordinates i,j in {0,...,4} represent i-2,j-2 in F_5.
raw = [
    ['.....', 'X....', '...X.', '...X.'],
    ['..XX.', 'XX...', 'X..X.', 'XXX.X'],
    ['.X.X.', 'XXX.X', '..X..', '..X..'],  # source has .X*X. in block 0
    ['.XX..', 'X...X', 'XXX..', 'X.X..'],
    ['.....', '...X.', '..XXX', '..X.X'],
]

S = set()
for i in range(5):
    for t in range(4):
        assert len(raw[i][t]) == 5
        for j, ch in enumerate(raw[i][t]):
            if ch == 'X':
                S.add((((i - 2) % 5, (j - 2) % 5), t))
assert len(S) == 36
assert (((0, 0), 0)) not in S
assert {inv(s) for s in S} == S

elts = [((x, y), t) for t in range(4) for x in range(5) for y in range(5)]
idx = {g: i for i, g in enumerate(elts)}
assert len(idx) == 100

HJ = make_adj(100)
for i, g in enumerate(elts):
    for s in S:
        j = idx[mul(g, s)]
        if i < j:
            add_edge(HJ, i, j)
assert degree_set(HJ) == {36}
assert edge_count(HJ) == 1800
hj_eh, hj_nh = common_hist(HJ)
assert hj_eh == Counter({14: 1800})
assert hj_nh == Counter({12: 3150})

# ---------- enumerate all maximal HJ independent sets exactly ----------
# Independent sets of HJ are cliques of its complement.
HJc = complement(HJ)
maximal_size_hist = Counter()
decad_masks = []

# Pivoted Bron--Kerbosch on integer bitsets.
def bronk(R, P, X):
    if P == 0 and X == 0:
        rsz = R.bit_count()
        maximal_size_hist[rsz] += 1
        if rsz == 10:
            decad_masks.append(R)
        return
    PX = P | X
    if PX:
        # deterministic pivot: maximum |P cap N(u)|, then smallest u
        best_u = None
        best_score = -1
        for u in bits(PX):
            score = (P & HJc[u]).bit_count()
            if score > best_score or (score == best_score and (best_u is None or u < best_u)):
                best_u, best_score = u, score
        cand = P & ~HJc[best_u]
    else:
        cand = P
    while cand:
        vb = cand & -cand
        v = vb.bit_length() - 1
        bronk(R | vb, P & HJc[v], X & HJc[v])
        P &= ~vb
        X |= vb
        cand &= ~vb

bronk(0, (1 << 100) - 1, 0)
assert maximal_size_hist == Counter({4: 1575, 6: 100800, 7: 28800, 10: 280})
assert len(decad_masks) == 280
assert len(set(decad_masks)) == 280
# Canonical ordering by vertex tuple, independent of traversal order.
decad_masks.sort(key=lambda m: tuple(bits(m)))

# ---------- the regular two-graph relation on the 280 decads ----------
inter_hist = Counter()
A = make_adj(280)
for i in range(280):
    for j in range(i + 1, 280):
        z = (decad_masks[i] & decad_masks[j]).bit_count()
        inter_hist[z] += 1
        if z == 2:
            add_edge(A, i, j)
assert inter_hist == Counter({0: 20160, 2: 18900})
assert degree_set(A) == {135}
assert edge_count(A) == 18900
a_eh, a_nh = common_hist(A)
assert a_eh == Counter({70: 18900})
assert a_nh == Counter({60: 20160})

# ---------- Seidel descendant at vertex 0, then delete 0 ----------
# Switch across N_A(0) vs the remaining non-neighbors, so vertex 0 becomes isolated.
N0 = A[0]
D = make_adj(279)
# New labels 0..278 correspond to old vertices 1..279.
for oi in range(1, 280):
    ni = oi - 1
    inN_i = (N0 >> oi) & 1
    for oj in range(oi + 1, 280):
        nj = oj - 1
        inN_j = (N0 >> oj) & 1
        e = (A[oi] >> oj) & 1
        if inN_i != inN_j:
            e ^= 1
        if e:
            add_edge(D, ni, nj)

assert degree_set(D) == {150}
assert edge_count(D) == 20925
d_eh, d_nh = common_hist(D)
assert d_eh == Counter({85: 20925})
assert d_nh == Counter({75: 17856})

# Exact spectrum/multiplicity deduction from SRG parameters.
v, k, lam, mu = 279, 150, 85, 75
# x^2 -(lam-mu)x -(k-mu)= x^2 -10x -75=(x-15)(x+5)
r, s = 15, -5
assert r + s == lam - mu
assert r * s == -(k - mu)
# multiplicities f,g solve f+g=v-1, k+r f+s g=0.
f_num = -k - s * (v - 1)
f_den = r - s
assert f_num % f_den == 0
f = f_num // f_den
g = v - 1 - f
assert (f, g) == (62, 216)
assert k + r * f + s * g == 0

# Complement is the (279,128,52,64) relation.
H = complement(D)
assert degree_set(H) == {128}
h_eh, h_nh = common_hist(H)
assert h_eh == Counter({52: 17856})
assert h_nh == Counter({64: 20925})

# ---------- deterministic DSATUR coloring of H ----------
def dsatur_coloring(adj):
    n = len(adj)
    colors = [-1] * n
    satsets = [set() for _ in range(n)]
    degs = [a.bit_count() for a in adj]
    uncolored = set(range(n))
    while uncolored:
        # maximum saturation, then maximum degree, then smallest vertex id
        vtx = min(uncolored, key=lambda u: (-len(satsets[u]), -degs[u], u))
        forbidden = satsets[vtx]
        c = 0
        while c in forbidden:
            c += 1
        colors[vtx] = c
        uncolored.remove(vtx)
        for w in bits(adj[vtx]):
            if w in uncolored:
                satsets[w].add(c)
    return colors

colors = dsatur_coloring(H)
num_colors = max(colors) + 1
assert num_colors == 35
classes = [[] for _ in range(num_colors)]
for i, c in enumerate(colors):
    classes[c].append(i)

# Verify this is an exact partition and each class is an independent set in H,
# equivalently a clique of D.  This is the actual cover certificate.
flat = [x for C in classes for x in C]
assert sorted(flat) == list(range(279))
assert len(flat) == len(set(flat)) == 279
for C in classes:
    mask = sum(1 << u for u in C)
    for u in C:
        assert H[u] & (mask ^ (1 << u)) == 0
        assert (D[u] & (mask ^ (1 << u))).bit_count() == len(C) - 1

expected_classes = [
[0,2,3,5,7,8,16,21,24,121,241],
[9,27,79,81,87,145,180,197,278],
[28,32,36,39,40,46,48,228,267],
[11,12,44,45,53,99,106,210,216],
[18,41,84,102,151,157,196,211],
[31,50,67,71,74,78,129,147,163,221,264],
[33,63,66,83,100,101,117,126,135,137,231],
[34,42,68,103,107,123,159,167,169,186,191,219],
[15,19,82,85,98,149,162,206],
[22,26,58,77,108,118,119,133,173,174,183,268],
[10,89,176,218,220,223,236,242,250,251],
[47,55,56,59,65,69,91,97,165],
[38,86,88,105,150,235,259,275],
[20,94,144,156,182,198,201,244,252],
[29,52,96,122,160,171,190,204,247],
[4,43,75,90,112,139,141,155,168,185,187],
[6,114,116,140,154,172,179,202],
[35,49,131,143,200,207,225,253],
[25,30,109,125,128,193,237,255],
[113,120,148,177,181,192,243,263],
[70,95,233,249,257,261,269],
[17,124,146,166,215,226,232,256],
[1,73,80,92,158,164,195,270],
[51,136,170,199,214,239,240,274],
[127,134,153,161,194,208,245],
[57,62,72,132,152,234,238],
[13,104,138,175,184,213,258],
[23,93,110,142,178,205,262,273],
[60,222,224,227,246],
[61,76,111,229,248,254,266],
[14,271,272,277],
[37,130,188,212,265],
[54,64,115,189,276],
[209,217,230,260],
[203],
]
assert classes == expected_classes

sizes = sorted((len(C) for C in classes), reverse=True)
assert sizes == [12,12,11,11,11,11,10,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,5,5,5,4,4,1]

print('I0123_HJ279_35_COVER_CERTIFICATE_PASS')
print('Hall-Janko Cayley: vertices=100 degree=36 edges=1800 srg=(100,36,14,12)')
print('HJ maximal independent sets by size=', dict(sorted(maximal_size_hist.items())))
print('HJ decads=280; pair intersections=', dict(sorted(inter_hist.items())))
print('decad relation A: srg=(280,135,70,60)')
print('descendant D: vertices=279 srg=(279,150,85,75) spectrum=150^1,15^62,(-5)^216')
print('complement H: srg=(279,128,52,64)')
print('deterministic DSATUR colors(H)=', num_colors)
print('therefore clique_cover(D) <=', num_colors)
print('class_sizes_desc=', sizes)
print('color_classes=', classes)

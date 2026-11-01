from itertools import combinations
from collections import Counter

# Exact finite certificate for two explicit rank-62 strongly-regular/two-distance routes.
# (A) Grassmann/Steiner graph on the 2-dimensional subspaces of F_2^6:
#     srg(651,90,33,9), spectrum 90^1,27^62,(-3)^588.
#     The 63 point-stars are cliques and cover all 651 vertices.
# (B) Hamming/lattice graph H(2,32): srg(1024,62,30,2),
#     spectrum 62^1,30^62,(-2)^961.  Its 32 rows are cliques and partition all vertices.
# Therefore neither explicit rank-62 two-distance realization can refute Borsuk in R^62.

# --- A. J_2(6,2) / block graph of S(2,3,63) ---
# Over F_2 every projective point has a unique nonzero vector representative.
PTS = tuple(range(1, 64))  # nonzero vectors of F_2^6
assert len(PTS) == 63

# Each 2D subspace has exactly the three nonzero vectors {u,v,u+v}; XOR is addition over F_2.
line_set = set()
for u, v in combinations(PTS, 2):
    line_set.add(frozenset((u, v, u ^ v)))
LINES = tuple(sorted(line_set, key=lambda L: tuple(sorted(L))))
assert len(LINES) == 651
assert {len(L) for L in LINES} == {3}

# Adjacency: nontrivial intersection, i.e. two projective lines meet in one point.
adj = [set() for _ in LINES]
for i, j in combinations(range(len(LINES)), 2):
    inter = LINES[i] & LINES[j]
    assert len(inter) <= 1
    if inter:
        adj[i].add(j)
        adj[j].add(i)
assert {len(a) for a in adj} == {90}

lam, mu = set(), set()
for i, j in combinations(range(len(LINES)), 2):
    common = len(adj[i] & adj[j])
    if j in adj[i]:
        lam.add(common)
    else:
        mu.add(common)
assert lam == {33}
assert mu == {9}

# For each of the 63 projective points, all lines through it form a clique.
stars = {p: tuple(i for i, L in enumerate(LINES) if p in L) for p in PTS}
assert {len(S) for S in stars.values()} == {31}
coverage = Counter(i for S in stars.values() for i in S)
assert coverage == Counter({i: 3 for i in range(651)})
for S in stars.values():
    for i, j in combinations(S, 2):
        assert j in adj[i]
# Hence 63 cliques cover every vertex (indeed each line lies in three point-stars).
assert len(stars) == 63

# Verify the advertised nontrivial eigenvalues/multiplicities from the SRG equations.
v, k, la, m = 651, 90, 33, 9
# r,s are roots x^2 -(la-m)x -(k-m)=0 = x^2-24x-81.
r, s = 27, -3
assert r*r - (la-m)*r - (k-m) == 0
assert s*s - (la-m)*s - (k-m) == 0
# Trace and dimension equations: k + f r + g s = 0; 1+f+g=v.
f, g = 62, 588
assert 1 + f + g == v
assert k + f*r + g*s == 0

# --- B. H(2,32) / 32 x 32 lattice graph ---
q = 32
V = tuple((a, b) for a in range(q) for b in range(q))
assert len(V) == 1024

def rook_adj(x, y):
    return x != y and (x[0] == y[0] or x[1] == y[1])

rows = [tuple((a, b) for b in range(q)) for a in range(q)]
assert len(rows) == 32
assert {len(R) for R in rows} == {32}
assert {x for R in rows for x in R} == set(V)
assert sum(len(R) for R in rows) == len(V)  # rows are disjoint, so a partition
for R in rows:
    for x, y in combinations(R, 2):
        assert rook_adj(x, y)

# Check the SRG parameters by elementary formulas for H(2,q).
v2 = q*q
k2 = 2*(q-1)
la2 = q-2
mu2 = 2
assert (v2, k2, la2, mu2) == (1024, 62, 30, 2)
# H(2,q) spectrum: 2(q-1)^1, (q-2)^[2(q-1)], (-2)^[(q-1)^2].
r2, f2, s2, g2 = q-2, 2*(q-1), -2, (q-1)**2
assert (r2, f2, s2, g2) == (30, 62, -2, 961)
assert 1 + f2 + g2 == v2
assert k2 + f2*r2 + g2*s2 == 0

print('I0123_RANK62_SRG_COVER_SCREEN_PASS')
print('J2(6,2): vertices=651, srg=(651,90,33,9), positive eigenspace multiplicity=62')
print('J2(6,2): 63 point-star cliques, each size 31, cover all 651 vertices; each line occurs in exactly 3 stars')
print('H(2,32): vertices=1024, srg=(1024,62,30,2), positive eigenspace multiplicity=62')
print('H(2,32): 32 row cliques, each size 32, partition all 1024 vertices')
print('CONCLUSION: these two explicit rank-62 two-distance realizations are partitionable into <=63 smaller-diameter parts and cannot be R^62 Borsuk counterexamples')

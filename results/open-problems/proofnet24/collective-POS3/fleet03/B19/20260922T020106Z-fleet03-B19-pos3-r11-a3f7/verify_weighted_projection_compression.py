from fractions import Fraction
from itertools import combinations

N = 9
REL = [
    (0,2),(0,3),(0,4),
    (1,4),(1,5),
    (2,5),
    (3,6),(3,7),
    (4,7),(4,8),
    (5,8),(6,8),
]
C = (2,5,8)
Q_ORDER = (0,1,3,4,6,7)

less = [[False]*N for _ in range(N)]
for a,b in REL:
    less[a][b] = True
for k in range(N):
    for i in range(N):
        if less[i][k]:
            for j in range(N):
                if less[k][j]:
                    less[i][j] = True

pred = [sum(1 << i for i in range(N) if less[i][j]) for j in range(N)]
exts = []
def enum(mask, seq):
    if mask == (1 << N)-1:
        exts.append(tuple(seq))
        return
    for x in range(N):
        if not (mask >> x) & 1 and pred[x] & ~mask == 0:
            enum(mask | (1 << x), seq + [x])
enum(0, [])

assert len(exts) == 349
assert all(less[C[i]][C[i+1]] for i in range(len(C)-1))

Q = set(Q_ORDER)
projected = [tuple(x for x in L if x in Q) for L in exts]
assert all(len(t) == 6 for t in projected)

# Exact projection multiplicities W_C(tau).
weights = {}
for tau in projected:
    weights[tau] = weights.get(tau, 0) + 1
assert sum(weights.values()) == 349

# Q has width <=2 via explicit chain partition.
A = (0,3,6)
B = (1,4,7)
assert all(less[A[i]][A[i+1]] for i in range(2))
assert all(less[B[i]][B[i+1]] for i in range(2))

def weighted_pair(x,y):
    nxy = 0
    gap_num = 0
    for tau,w in weights.items():
        p = {v:i for i,v in enumerate(tau)}
        if p[x] < p[y]:
            nxy += w
        gap_num += w*(p[y]-p[x])
    return nxy, gap_num

# Every incomparable pair wholly inside Q is outside [1/3,2/3].
rows = []
for x,y in combinations(Q_ORDER,2):
    if less[x][y] or less[y][x]:
        continue
    nxy,g = weighted_pair(x,y)
    bal = min(nxy,349-nxy)
    rows.append((x,y,nxy,bal,g))
    assert 3*bal < 349
assert len(rows) == 6
assert max(r[3] for r in rows) == 113

# Consecutive reference-order boundaries are all strong in the displayed direction.
boundary = []
for x,y in zip(Q_ORDER,Q_ORDER[1:]):
    assert not less[x][y] and not less[y][x]
    nxy,g = weighted_pair(x,y)
    assert 3*nxy > 2*349
    boundary.append((x,y,nxy,g))

expected = [
    (0,1,244,265),
    (1,3,247,320),
    (3,4,255,376),
    (4,6,236,281),
    (6,7,261,310),
]
assert boundary == expected

# Weighted boundary-rank-gap telescope: sum gaps <= k-1 = 5.
gap_sum = sum(r[3] for r in boundary)
assert gap_sum == 1552
assert gap_sum <= 5*349
compressed = [(x,y,g) for x,y,nxy,g in boundary if g <= 349]
assert compressed == [(0,1,265),(1,3,320),(4,6,281),(6,7,310)]

# Projected rank atoms at the displayed reference ranks.
atoms = {}
for ref_rank,q in enumerate(Q_ORDER):
    num = 0
    for tau,w in weights.items():
        if tau.index(q) == ref_rank:
            num += w
    atoms[q] = num
expected_atoms = {0:244, 1:142, 3:153, 4:142, 6:148, 7:261}
assert atoms == expected_atoms
assert all(81*v > 349 for v in atoms.values())

# Parent P is not a POS3 counterexample: both balanced pairs use the deleted chain.
def full_pair(x,y):
    c = 0
    for L in exts:
        p = {v:i for i,v in enumerate(L)}
        c += p[x] < p[y]
    return c
assert full_pair(2,3) == 156
assert full_pair(5,6) == 156
assert 349 <= 3*156 <= 2*349

print("E", len(exts))
print("projection_support", len(weights))
print("Q_incomparable_rows", rows)
print("boundary_rows", boundary)
print("boundary_gap_sum", f"{gap_sum}/349")
print("compressed_boundaries", compressed)
print("projected_rank_atoms", atoms)
print("parent_balanced_pairs", [(2,3,156),(5,6,156)])
print("POS3_B19_WEIGHTED_PROJECTION_COMPRESSION_PASS")

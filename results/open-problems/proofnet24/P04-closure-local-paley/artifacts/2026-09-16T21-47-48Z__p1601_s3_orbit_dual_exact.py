#!/usr/bin/env python3
"""Exact p=1601 finite dual certificate for P04/I0101.

Source target: Randomstrasse101 Conjecture 27, two-localized Paley graph.
This proves the source inequality at p=1601 only. It does NOT prove the
eventual quantifier.

Acceptance uses integer arithmetic throughout. A frozen integer weight is
stored for each lexicographically ordered unordered nonedge pair. The script
independently reconstructs the graph and S3 action, verifies that the frozen
weights are constant on S3 pair-orbits, and proves 26 I - B positive definite
by fraction-free Bareiss/Sylvester.
"""
from collections import Counter, deque
import base64, hashlib, zlib

P = 1601
T = 26
OFFSET = 8
WEIGHTS_ZLIB_B64 = """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[... ELLIPSIZATION ...]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"""
EXPECTED_RAW_SHA256 = "fe5a88d5acd86372a24b3b6b3c20d28a50a39527bc6bf6fcbb403004921b0191"

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    q = 3
    while q*q <= n:
        if n % q == 0:
            return False
        q += 2
    return True

def chi(a):
    a %= P
    if a == 0:
        return 0
    v = pow(a, (P-1)//2, P)
    assert v in (1, P-1)
    return 1 if v == 1 else -1

assert is_prime(P)
assert P % 4 == 1

# Source graph G_{p,2}.
V = [x for x in range(P) if x not in (0,1) and chi(x)==1 and chi(x-1)==1]
assert len(V) == (P-5)//4 == 399
idx = {x:i for i,x in enumerate(V)}
n = len(V)
A = [[0]*n for _ in range(n)]
nonedges = []
edges = 0
for i,x in enumerate(V):
    for j in range(i+1,n):
        y = V[j]
        if chi(x-y) == 1:
            A[i][j] = A[j][i] = 1
            edges += 1
        else:
            nonedges.append((i,j))
assert edges == 39501
assert len(nonedges) == 39900

# Frozen lexicographic nonedge weights.
raw = zlib.decompress(base64.b64decode(WEIGHTS_ZLIB_B64))
assert hashlib.sha256(raw).hexdigest() == EXPECTED_RAW_SHA256
assert len(raw) == len(nonedges)
pair_weight = {pair: int(b)-OFFSET for pair,b in zip(nonedges, raw)}
assert Counter(pair_weight.values()) == Counter({-6: 12, -5: 162, -4: 711, -3: 2556, -2: 7731, -1: 13302, 0: 11310, 1: 3804, 2: 303, 3: 9})

# S3 generators r(x)=1-x and s(x)=1/x preserve V and adjacency.
def r(x):
    return (1-x) % P

def s(x):
    return pow(x, -1, P)

for x in V:
    assert r(x) in idx and s(x) in idx
for i,x in enumerate(V):
    for j in range(i+1,n):
        a = A[i][j]
        ir,jr = idx[r(x)],idx[r(V[j])]
        is_,js_ = idx[s(x)],idx[s(V[j])]
        assert A[min(ir,jr)][max(ir,jr)] == a
        assert A[min(is_,js_)][max(is_,js_)] == a

# Enumerate unordered nonedge-pair S3 orbits and verify frozen weights invariant.
def canon_pair(i,j):
    return (i,j) if i<j else (j,i)

unseen = set(nonedges)
orbit_sizes = Counter()
orbit_weight_counts = Counter()
while unseen:
    seed = next(iter(unseen))
    q = deque([seed])
    orb = set()
    while q:
        i,j = q.popleft()
        pair = canon_pair(i,j)
        if pair in orb:
            continue
        orb.add(pair)
        x,y = V[pair[0]],V[pair[1]]
        for f in (r,s):
            ni,nj = idx[f(x)],idx[f(y)]
            npair = canon_pair(ni,nj)
            assert npair in pair_weight
            if npair not in orb:
                q.append(npair)
    vals = {pair_weight[e] for e in orb}
    assert len(vals) == 1
    w = next(iter(vals))
    orbit_sizes[len(orb)] += 1
    orbit_weight_counts[w] += 1
    unseen.difference_update(orb)

assert orbit_sizes == Counter({6:6600, 3:100})
assert orbit_weight_counts == Counter({-6: 2, -5: 27, -4: 120, -3: 431, -2: 1299, -1: 2229, 0: 1898, 1: 640, 2: 52, 3: 2})

# Exact S3-invariant anharmonic sign multiset on unordered pairs.
# F0=xy-1, F1=xy-x-y, F2=x+y-1.  The sorted Legendre-symbol triple
# is invariant under diagonal S3.
class_counts = Counter()
for (i,j) in nonedges:
    x,y = V[i],V[j]
    sig = tuple(sorted((chi(x*y-1), chi(x*y-x-y), chi(x+y-1))))
    class_counts[sig] += 1
assert class_counts == Counter({(-1, -1, -1): 5154, (-1, -1, 0): 147, (-1, -1, 1): 14748, (-1, 1, 1): 14856, (0, 1, 1): 153, (1, 1, 1): 4842})

# Build the edge-fixed theta-dual matrix B:
# B_ii=1, B_ij=1 on graph edges, frozen integer weights on nonedges.
B = [[0]*n for _ in range(n)]
for i in range(n):
    B[i][i] = 1
for i in range(n):
    for j in range(i+1,n):
        if A[i][j]:
            v = 1
        else:
            v = pair_weight[(i,j)]
        B[i][j] = B[j][i] = v

# Independent full S3 invariance check for B.
for i,x in enumerate(V):
    for j,y in enumerate(V):
        assert B[idx[r(x)]][idx[r(y)]] == B[i][j]
        assert B[idx[s(x)]][idx[s(y)]] == B[i][j]

# M = T I - B.  Bareiss pivots equal the leading principal determinants.
M = [[(T if i==j else 0)-B[i][j] for j in range(n)] for i in range(n)]

def symmetric_bareiss_leading_dets(M):
    X = [row[:] for row in M]
    N = len(X)
    prev = 1
    dets = []
    for k in range(N-1):
        pivot = X[k][k]
        assert pivot > 0, (k, pivot)
        dets.append(pivot)
        for i in range(k+1,N):
            aik = X[i][k]
            for j in range(i,N):
                num = X[i][j]*pivot - aik*X[k][j]
                assert num % prev == 0
                val = num // prev
                X[i][j] = val
                X[j][i] = val
        prev = pivot
    assert X[N-1][N-1] > 0
    dets.append(X[N-1][N-1])
    return dets

leading = symmetric_bareiss_leading_dets(M)
assert len(leading) == n
assert all(x>0 for x in leading)

# Exact source-threshold comparison: T < (2/3)sqrt(P).
threshold_numerator = 4*P - 9*T*T
assert threshold_numerator == 320 > 0

print("P04-I0101-P1601-S3-ORBIT-DUAL=PASS")
print(f"p={P} n={n} edges={edges} nonedges={len(nonedges)}")
print(f"vertex_orbit_input_check=S3_GENERATORS_PASS")
print(f"nonedge_pair_orbit_size_counts={dict(sorted(orbit_sizes.items()))}")
print(f"orbit_weight_counts={dict(sorted(orbit_weight_counts.items()))}")
print(f"pair_weight_counts={dict(sorted(Counter(pair_weight.values()).items()))}")
print(f"anharmonic_sign_class_counts={dict(sorted(class_counts.items()))}")
print(f"t={T} exact_threshold_numerator_4p_minus_9t2={threshold_numerator}")
print(f"bareiss_positive_leading_minors={len(leading)}")
print(f"final_determinant_digits={len(str(leading[-1]))}")
print("EDGE_FIXED_FEASIBILITY=PASS")
print("S3_INVARIANCE=PASS")
print("ANHARMONIC_INVARIANT_COUNTS=PASS")
print("SYLVESTER_BAREISS_PD=PASS")
print("THETA_LT_26_LT_2SQRT_P_OVER_3=PASS")

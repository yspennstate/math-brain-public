#!/usr/bin/env python3
"""
P03 / I0111 finite stuck-recovery diagnostic.

Exact rational computation on Q_4 for the rooted positive-density target problem
appearing in Hermon's transitive-chain hitting-time criterion.

This is NOT a source-level theorem or a proof of Salez Problem 2.2.
It tests and refutes the exact route "an expectation-worst deterministic target
may be chosen root-stabilizer invariant" at alpha = 1/2 on Q_4.

Rate-one continuous-time simple random walk:
    L = P - I,  P(x,y)=1/4 on cube neighbors.
For a surviving domain S containing the root 0 and target A=V\\S,
    K_S = I - P_{S,S}.
The mean exit/hitting time is e_0^T K_S^{-1} 1 and
the second moment is 2 e_0^T K_S^{-2} 1.
"""

from fractions import Fraction
from itertools import combinations
from collections import Counter

D = 4
N = 1 << D
ROOT = 0
ALPHA_NUM = 1
ALPHA_DEN = 2
MAX_DOMAIN = N * (ALPHA_DEN - ALPHA_NUM) // ALPHA_DEN

NEIGHBORS = {
    v: tuple(v ^ (1 << i) for i in range(D))
    for v in range(N)
}
WEIGHT = {v: v.bit_count() for v in range(N)}
LAYERS = {
    k: tuple(v for v in range(N) if WEIGHT[v] == k)
    for k in range(D + 1)
}

def solve_fraction(A, b):
    """Gauss-Jordan solve over Q."""
    n = len(A)
    M = [
        [Fraction(x) for x in A[i]] + [Fraction(b[i])]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if M[r][col] != 0), None)
        assert pivot is not None
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]
        p = M[col][col]
        M[col] = [x / p for x in M[col]]
        for r in range(n):
            if r == col:
                continue
            f = M[r][col]
            if f != 0:
                M[r] = [
                    M[r][j] - f * M[col][j]
                    for j in range(n + 1)
                ]
    return [M[i][-1] for i in range(n)]

def torsion_stats(S):
    """Return exact mean, second moment, variance, CV^2 for exit from S."""
    S = tuple(sorted(S))
    assert ROOT in S
    idx = {v: i for i, v in enumerate(S)}
    n = len(S)
    K = [
        [Fraction(int(i == j), 1) for j in range(n)]
        for i in range(n)
    ]
    for i, v in enumerate(S):
        for w in NEIGHBORS[v]:
            if w in idx:
                K[i][idx[w]] -= Fraction(1, D)
    one = [Fraction(1) for _ in range(n)]
    u = solve_fraction(K, one)
    mean = u[idx[ROOT]]
    v = solve_fraction(K, u)
    second = 2 * v[idx[ROOT]]
    var = second - mean * mean
    cv2 = var / (mean * mean)
    return mean, second, var, cv2

def layer_profile(S):
    c = Counter(WEIGHT[v] for v in S)
    return tuple(c[k] for k in range(D + 1))

def internal_edges(S):
    S = set(S)
    return sum(
        1 for v in S for w in NEIGHBORS[v] if w in S
    ) // 2

# Domain monotonicity implies a maximum over |S|<=8 is attained at |S|=8.
# Enumerate all such rooted domains exactly.
best = Fraction(-1)
max_sets = []
mean_hist = Counter()

for rest in combinations(range(1, N), MAX_DOMAIN - 1):
    S = (ROOT,) + rest
    mean, _, _, _ = torsion_stats(S)
    mean_hist[mean] += 1
    if mean > best:
        best = mean
        max_sets = [S]
    elif mean == best:
        max_sets.append(S)

assert sum(mean_hist.values()) == 6435
assert best == Fraction(4, 1)
assert len(max_sets) == 12

shape_counts = Counter(
    (layer_profile(S), internal_edges(S))
    for S in max_sets
)
expected_shapes = Counter({
    ((1, 3, 3, 1, 0), 12): 4,
    ((1, 4, 3, 0, 0), 10): 8,
})
assert shape_counts == expected_shapes

representatives = {}
for S in max_sets:
    key = (layer_profile(S), internal_edges(S))
    representatives.setdefault(key, S)

face_key = ((1, 3, 3, 1, 0), 12)
ball_key = ((1, 4, 3, 0, 0), 10)
face_rep = representatives[face_key]
ball_rep = representatives[ball_key]

face_stats = torsion_stats(face_rep)
ball_stats = torsion_stats(ball_rep)
assert face_stats == (
    Fraction(4), Fraction(32), Fraction(16), Fraction(1)
)
assert ball_stats == (
    Fraction(4), Fraction(80, 3), Fraction(32, 3), Fraction(2, 3)
)

# The full root stabilizer of Q_4 is S_4, acting by coordinate permutations.
# Its deterministic invariant subsets are exactly unions of Hamming-weight layers.
kinv = []
for mask in range(1 << (D + 1)):
    if not (mask & 1):  # must contain layer 0/root
        continue
    layer_indices = tuple(k for k in range(D + 1) if (mask >> k) & 1)
    S = tuple(v for k in layer_indices for v in LAYERS[k])
    if len(S) <= MAX_DOMAIN:
        kinv.append((torsion_stats(S)[0], layer_indices, len(S), torsion_stats(S)))

kinv_best = max(row[0] for row in kinv)
kinv_best_rows = [row for row in kinv if row[0] == kinv_best]
assert kinv_best == Fraction(8, 3)
assert {(row[1], row[2]) for row in kinv_best_rows} == {
    ((0, 1), 5),
    ((0, 1, 4), 6),
}
assert best / kinv_best == Fraction(3, 2)

print("P03-I0111-Q4-WORST-SET-DIAGNOSTIC=PASS")
print("scope=finite_route_kill_not_source_theorem")
print("graph=Q4")
print("root=0")
print("target_mass_lower_bound=1/2")
print("max_surviving_domain_size=8")
print("rooted_size8_domains_checked=6435")
print(f"distinct_exact_mean_values={len(mean_hist)}")
print(f"global_best_mean={best}")
print(f"global_maximizer_count={len(max_sets)}")
print("global_maximizer_shape_census=" + repr(sorted(shape_counts.items(), key=repr)))
print(f"face_representative={face_rep}")
print(f"face_stats_mean_m2_var_cv2={face_stats}")
print(f"other_representative={ball_rep}")
print(f"other_stats_mean_m2_var_cv2={ball_stats}")
print(f"root_stabilizer_invariant_candidates_checked={len(kinv)}")
print(f"root_stabilizer_invariant_best_mean={kinv_best}")
print("root_stabilizer_invariant_best_layers=" + repr(
    sorted((row[1], row[2]) for row in kinv_best_rows)
))
print(f"global_to_invariant_best_ratio={best / kinv_best}")
print("EXACT_ROOT_STABILIZER_RESTRICTION_FAILS=PASS")
print("MEAN_MAXIMIZERS_HAVE_DIFFERENT_SECOND_MOMENTS=PASS")

from itertools import product
from collections import deque, defaultdict

# CONDITIONAL H2 SELF-CHECK ONLY.
# This script does NOT implement Cerf's source definitions (51.1)-(52.1).
# It certifies the finite route diagnostics reported by R09 for the
# section-neighborhood hypothesis H2 on n=8.

N = 8
ALL = range(1 << N)

def is_increasing(fam):
    return all((s | (1 << i)) in fam
               for s in fam for i in range(N) if not ((s >> i) & 1))

def section_boundary(fam, i):
    others = [j for j in range(N) if j != i]
    out = set()
    for y in range(1 << (N - 1)):
        s0 = 0
        for k, j in enumerate(others):
            if (y >> k) & 1:
                s0 |= 1 << j
        if (s0 | (1 << i)) in fam and s0 not in fam:
            out.add(y)
    return out

def radius1(B, d):
    out = set(B)
    for y in B:
        for k in range(d):
            out.add(y ^ (1 << k))
    return out

def h2_contrib(fam):
    n1 = []
    ext = []
    bnd = []
    for i in range(N):
        Bi = section_boundary(fam, i)
        Ni = radius1(Bi, N - 1)
        n1.append(len(Ni))
        ext.append(len(Ni - Bi))
        bnd.append(len(Bi))
    return tuple(n1), tuple(ext), tuple(bnd)

def h2_obj(fam):
    n1, ext, bnd = h2_contrib(fam)
    return sum(n1), sum(ext), sum(bnd)

def profile(fam):
    return tuple(sum(1 for s in fam if s.bit_count() == k) for k in range(N + 1))

def tuple_of(s):
    return tuple(i + 1 for i in range(N) if (s >> i) & 1)

# Five bulk coordinates x1,...,x5 and three control bits x6,x7,x8.
Y = range(8)
ORDER = [(y, z) for y in Y for z in Y if (y & ~z) == 0]

def valid_t(t):
    return t[0] == 6 and all(t[y] >= t[z] for y, z in ORDER)

def family_from_t(t):
    fam = set()
    for s in ALL:
        a = sum((s >> j) & 1 for j in range(5))
        y = ((s >> 5) & 1) | (((s >> 6) & 1) << 1) | (((s >> 7) & 1) << 2)
        if a >= t[y]:
            fam.add(s)
    return fam

records = {}
for vals in product(range(7), repeat=7):
    t = (6,) + vals
    if not valid_t(t):
        continue
    fam = family_from_t(t)
    assert is_increasing(fam)
    records[t] = h2_obj(fam)

assert len(records) == 19704

TW = (6, 5, 5, 3, 4, 2, 2, 1)
T903 = (6, 3, 5, 3, 4, 1, 2, 1)
TSTAR = (6, 3, 5, 3, 4, 1, 2, 0)

FW = family_from_t(TW)
F903 = family_from_t(T903)
FSTAR = family_from_t(TSTAR)

assert h2_obj(FW) == (902, 644, 258)
assert len(FW) == 107
assert profile(FW) == (0, 0, 0, 0, 25, 45, 28, 8, 1)

assert h2_obj(F903) == (903, 645, 258)
assert len(F903) == 127
assert profile(F903) == (0, 0, 0, 5, 35, 50, 28, 8, 1)

assert h2_obj(FSTAR) == (908, 652, 256)
assert len(FSTAR) == 128
assert profile(FSTAR) == (0, 0, 0, 6, 35, 50, 28, 8, 1)

# Global lexicographic optimum within all 19,704 control-threshold maps.
best_key = max((obj[0], obj[1]) for obj in records.values())
best_maps = [t for t, obj in records.items() if (obj[0], obj[1]) == best_key]
assert best_key == (908, 652)
assert len(best_maps) == 6
assert TSTAR in best_maps
assert all(records[t] == (908, 652, 256) for t in best_maps)

# B6: deformation landscape around the compact weighted-threshold map TW.
def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def l1(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))

by_hamming = defaultdict(list)
by_l1 = defaultdict(list)
for t, obj in records.items():
    by_hamming[hamming(t, TW)].append((obj, t))
    by_l1[l1(t, TW)].append((obj, t))

hamming_counts = {d: len(v) for d, v in by_hamming.items()}
hamming_best = {
    d: max(v, key=lambda z: (z[0][0], z[0][1]))
    for d, v in by_hamming.items()
}
assert hamming_counts == {
    0: 1, 1: 22, 2: 200, 3: 994,
    4: 2998, 5: 5638, 6: 6338, 7: 3513
}
assert hamming_best[0] == ((902, 644, 258), TW)
assert hamming_best[1][0] == (898, 642, 256)
assert hamming_best[2] == ((903, 645, 258), T903)
assert hamming_best[3] == ((908, 652, 256), TSTAR)

l1_best = {
    d: max(v, key=lambda z: (z[0][0], z[0][1]))
    for d, v in by_l1.items()
}
assert l1_best[0] == ((902, 644, 258), TW)
assert l1_best[1][0] == (898, 642, 256)
assert l1_best[2][0] == (892, 624, 268)
assert l1_best[3] == ((903, 645, 258), T903)
assert l1_best[4] == ((908, 652, 256), TSTAR)

valid_set = set(records)

def unit_neighbors(t):
    # One threshold entry +/-1, keeping t(000)=6 and monotonicity.
    for i in range(1, 8):
        for delta in (-1, 1):
            v = t[i] + delta
            if 0 <= v <= 6:
                u = list(t)
                u[i] = v
                u = tuple(u)
                if u in valid_set:
                    yield u

unit_tw = list(unit_neighbors(TW))
assert len(unit_tw) == 14
assert max(records[u][0] for u in unit_tw) == 898
assert all(records[u][0] < records[TW][0] for u in unit_tw)

# Shortest unit-step path to any strictly better psi2 has length exactly 3.
q = deque([TW])
prev = {TW: None}
target = None
while q:
    t = q.popleft()
    if t != TW and records[t][0] > records[TW][0]:
        target = t
        break
    for u in unit_neighbors(t):
        if u not in prev:
            prev[u] = t
            q.append(u)

path = []
x = target
while x is not None:
    path.append(x)
    x = prev[x]
path.reverse()

expected_path = [
    TW,
    (6, 4, 5, 3, 4, 2, 2, 1),
    (6, 3, 5, 3, 4, 2, 2, 1),
    T903,
]
assert path == expected_path
assert [records[t] for t in path] == [
    (902, 644, 258),
    (892, 624, 268),
    (892, 624, 268),
    (903, 645, 258),
]

# Exact bottleneck certificate:
# no psi2>902 state lies in the unit-step component of TW if psi2>=893
# is imposed, while the displayed path reaches 903 with minimum 892.
q = deque([TW])
seen = {TW}
while q:
    t = q.popleft()
    for u in unit_neighbors(t):
        if u not in seen and records[u][0] >= 893:
            seen.add(u)
            q.append(u)
assert all(records[t][0] <= 902 for t in seen)
assert min(records[t][0] for t in expected_path) == 892
# Therefore the optimal maximin bottleneck from TW to any better state is 892.

# B12: exact external-boundary decomposition.
for t in records:
    fam = family_from_t(t)
    n1, ext, bnd = h2_contrib(fam)
    assert all(n1[i] == ext[i] + bnd[i] for i in range(N))
    obj = h2_obj(fam)
    assert obj[0] == obj[1] + obj[2]

assert h2_contrib(FW) == (
    (109, 109, 109, 109, 109, 119, 119, 119),
    (88, 88, 88, 88, 88, 78, 78, 48),
    (21, 21, 21, 21, 21, 41, 41, 71),
)
assert h2_contrib(F903) == (
    (115, 115, 115, 115, 115, 125, 78, 125),
    (92, 92, 92, 92, 92, 64, 57, 64),
    (23, 23, 23, 23, 23, 61, 21, 61),
)
assert h2_contrib(FSTAR) == (
    (114, 114, 114, 114, 114, 126, 86, 126),
    (92, 92, 92, 92, 92, 64, 64, 64),
    (22, 22, 22, 22, 22, 62, 22, 62),
)

# B26: the final 903 -> 908 jump is caused by one sporadic cube point.
assert F903 <= FSTAR
added = FSTAR - F903
assert len(added) == 1
added_point = next(iter(added))
assert tuple_of(added_point) == (6, 7, 8)

n903, e903, b903 = h2_contrib(F903)
ns, es, bs = h2_contrib(FSTAR)
delta_n1 = tuple(a - b for a, b in zip(ns, n903))
delta_ext = tuple(a - b for a, b in zip(es, e903))
delta_bnd = tuple(a - b for a, b in zip(bs, b903))
assert delta_n1 == (-1, -1, -1, -1, -1, 1, 8, 1)
assert delta_ext == (0, 0, 0, 0, 0, 0, 7, 0)
assert delta_bnd == (-1, -1, -1, -1, -1, 1, 1, 1)
assert tuple(a - b for a, b in zip(h2_obj(FSTAR), h2_obj(F903))) == (5, 7, -2)

# The 903 family is the weighted family plus exactly 20 states,
# concentrated on the three middle layers 3,4,5.
assert FW <= F903
mid_added = F903 - FW
assert len(mid_added) == 20
assert tuple(sum(1 for s in mid_added if s.bit_count() == k) for k in range(9)) == (
    0, 0, 0, 5, 10, 5, 0, 0, 0
)

print("SELF_CHECK_ONLY_H2_NOT_SOURCE_VERIFIED")
print("valid_control_threshold_maps=", len(records))
print("weighted_map=", TW, "score=", records[TW], "size=", len(FW), "profile=", profile(FW))
print("hamming_distance_counts=", dict(sorted(hamming_counts.items())))
print("best_hd1=", hamming_best[1])
print("best_hd2=", hamming_best[2])
print("best_hd3=", hamming_best[3])
print("unit_neighbors_of_weighted=", len(unit_tw), "best_neighbor_psi2=", max(records[u][0] for u in unit_tw))
print("shortest_better_path_length=", len(expected_path) - 1)
print("shortest_better_path=", [(t, records[t]) for t in expected_path])
print("no_better_reachable_while_psi2_ge_893=", True, "high_component_size=", len(seen))
print("optimal_maximin_bottleneck_to_better=", 892)
print("decomposition_identity=psi2=psi2m1+ordinary_boundary_sum verified_for_all_maps")
print("weighted_contrib=", h2_contrib(FW))
print("first_better_903_contrib=", h2_contrib(F903))
print("class_optimum_contrib=", h2_contrib(FSTAR))
print("sporadic_added_point=", tuple_of(added_point))
print("sporadic_score_delta=", tuple(a-b for a,b in zip(h2_obj(FSTAR), h2_obj(F903))))
print("sporadic_N1_delta=", delta_n1)
print("sporadic_external_boundary_delta=", delta_ext)
print("sporadic_ordinary_boundary_delta=", delta_bnd)
print("weighted_to_903_added_states=", len(mid_added), "layer_profile=", tuple(sum(1 for s in mid_added if s.bit_count()==k) for k in range(9)))
print("class_global_lexicographic_best=", best_key, "number_best_maps=", len(best_maps))
print("ALL_CLAIMS_CONDITIONAL_ON_H2_NOT_CERF_SOURCE_FUNCTIONALS")
print("PASS")

from itertools import product, permutations

N = 8
ALL = range(1 << N)

UPPER_MIN = [
    (1,2,5,6), (1,3,5,6), (2,4,5,6), (3,4,5,6), (1,3,5,7), (2,3,5,7),
    (1,4,5,7), (1,2,3,4,6,7), (2,5,6,7), (4,5,6,7), (1,2,3,8), (1,3,4,8),
    (2,3,4,8), (1,5,8), (2,5,8), (3,5,8), (4,5,8), (2,3,6,8), (1,4,6,8),
    (5,6,8), (1,2,7,8), (2,4,7,8), (3,4,7,8), (5,7,8), (1,6,7,8), (3,6,7,8)
]

def mask(t):
    out = 0
    for i in t:
        out |= 1 << (i - 1)
    return out

def up_family(minsets):
    mins = [mask(t) for t in minsets]
    return {s for s in ALL if any((s & m) == m for m in mins)}

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

def h2_obj(fam):
    n1 = b = 0
    for i in range(N):
        Bi = section_boundary(fam, i)
        b += len(Bi)
        n1 += len(radius1(Bi, N - 1))
    return (n1, n1 - b, b)

def perm_mask(s, p):
    out = 0
    for i in range(N):
        if (s >> i) & 1:
            out |= 1 << p[i]
    return out

def tuple_of(s):
    return tuple(i + 1 for i in range(N) if (s >> i) & 1)

# ---------- B15: fully asymmetric explicit upper-out candidate ----------
U = up_family(UPPER_MIN)
assert is_increasing(U)
fixed5 = mask((1,2,3,4,5))
assert fixed5 not in U
assert h2_obj(U) == (924, 670, 254)
level_profile = tuple(sum(1 for s in U if s.bit_count() == k) for k in range(N + 1))
assert level_profile == (0,0,0,6,34,49,28,8,1)
included_w3 = tuple(sorted(tuple_of(s) for s in U if s.bit_count() == 3))
excluded_w5 = tuple(sorted(tuple_of(s) for s in ALL if s.bit_count() == 5 and s not in U))
assert included_w3 == (
    (1,5,8),(2,5,8),(3,5,8),(4,5,8),(5,6,8),(5,7,8)
)
assert excluded_w5 == (
    (1,2,3,4,5),(1,2,3,4,6),(1,2,3,4,7),(1,2,3,6,7),
    (1,2,4,6,7),(1,3,4,6,7),(2,3,4,6,7)
)
aut_count = 0
for p in permutations(range(N)):
    if all(perm_mask(s, p) in U for s in U):
        aut_count += 1
assert aut_count == 1

# ---------- B10/B24: deterministic S5-control-bit family class ----------
# y encodes x6 + 2*x7 + 4*x8.  t(y) is the minimum number of ones
# among x1,...,x5 required for inclusion.  Coordinatewise monotonicity
# is exactly t(y) >= t(z) whenever y <= z bitwise.  t(000)=6 forces
# omission of the fixed five-set {1,...,5}.
Y = range(8)
ORDER = [(y,z) for y in Y for z in Y if (y & ~z) == 0]

def family_from_t(t):
    fam = set()
    for s in ALL:
        a = sum((s >> j) & 1 for j in range(5))
        y = ((s >> 5) & 1) | (((s >> 6) & 1) << 1) | (((s >> 7) & 1) << 2)
        if a >= t[y]:
            fam.add(s)
    return fam

valid_count = 0
best = None
best_t = []
for vals in product(range(7), repeat=7):
    t = (6,) + vals
    if not all(t[y] >= t[z] for y,z in ORDER):
        continue
    valid_count += 1
    fam = family_from_t(t)
    assert fixed5 not in fam and is_increasing(fam)
    obj = h2_obj(fam)
    key = (obj[0], obj[1])
    if best is None or key > (best[0], best[1]):
        best = obj
        best_t = [t]
    elif key == (best[0], best[1]):
        best_t.append(t)

assert valid_count == 19704
assert best == (908, 652, 256)
assert len(best_t) == 6
canonical_t = (6,5,4,2,3,3,1,0)
assert canonical_t in best_t
Fcontrol = family_from_t(canonical_t)
assert len(Fcontrol) == 128

# ---------- Compact weighted-threshold derandomization ----------
weights = (3,3,3,3,3,5,5,7)
threshold = 18
Fw = {
    s for s in ALL
    if sum(weights[i] for i in range(N) if (s >> i) & 1) >= threshold
}
assert is_increasing(Fw)
assert fixed5 not in Fw
assert len(Fw) == 107
assert h2_obj(Fw) == (902, 644, 258)

# ---------- Recompute old S5 x S3 invariant benchmark ----------
def family_from_thresholds(thr):
    fam = set()
    for s in ALL:
        a = sum((s >> j) & 1 for j in range(5))
        b = s.bit_count() - a
        if b >= thr[a]:
            fam.add(s)
    return fam

def nonincreasing_thresholds(length, maxval):
    def rec(pos, last, prefix):
        if pos == length:
            yield tuple(prefix)
            return
        for v in range(last, -1, -1):
            prefix.append(v)
            yield from rec(pos + 1, v, prefix)
            prefix.pop()
    yield from rec(0, maxval, [])

restricted = []
for thr in nonincreasing_thresholds(6, 4):
    if thr[5] < 1:
        continue
    fam = family_from_thresholds(thr)
    assert fixed5 not in fam
    restricted.append((h2_obj(fam), thr))
assert len(restricted) == 84
restricted_best = max(restricted, key=lambda x: (x[0][0], x[0][1]))
assert restricted_best == ((862,584,278),(4,3,3,1,1,1))

assert 924 > 908 > 902 > 862
assert 670 > 652 > 644 > 584

print("SELF_CHECK_ONLY_H2_NOT_SOURCE_VERIFIED")
print("n=8 factor-two-free H2 objectives: (psi2, psi2m1, ordinary_boundary_sum)")
print("fully_asymmetric_upper_out=", h2_obj(U), "family_size=", len(U),
      "aut_group_size=", aut_count, "level_profile=", level_profile)
print("included_weight3=", included_w3)
print("excluded_weight5=", excluded_w5)
print("S5_control_map_count=", valid_count,
      "best=", best, "number_of_equivalent_best_maps=", len(best_t),
      "canonical_t=", canonical_t, "family_size=", len(Fcontrol))
print("weighted_threshold=", weights, "threshold=", threshold,
      "score=", h2_obj(Fw), "family_size=", len(Fw))
print("S5xS3_restricted_count=", len(restricted), "best=", restricted_best)
print("asymmetry_score_chain_psi2=862<902<908<924")
print("asymmetry_score_chain_psi2m1=584<644<652<670")
print("ALL_CLAIMS_CONDITIONAL_ON_H2_NOT_CERF_SOURCE_FUNCTIONALS")
print("PASS")

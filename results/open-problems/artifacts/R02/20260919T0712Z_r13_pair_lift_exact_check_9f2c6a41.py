#!/usr/bin/env python3
"""
R02 exact self-check: direct pair-lift obstruction for the R13 six-row
projective exact-cover pattern.

This does NOT prove anything about all sign matrices. It checks only the
specific lift described in the accompanying R02 report.

Construction L_eq:
- Start with the six R13 support/sign rows on six signing coordinates.
- For a nonzero row coordinate, encode its sign by an equal bit-pair.
- For a zero coordinate, encode an arbitrary unequal bit-pair.
- Quotient 12-bit words by global complement.
- Ask whether the union of all folded radius-3 Hamming balls around every
  possible lifted center covers F_2^12/<1>.

The checker also tests the dual-polarity lift L_neq obtained by swapping
"equal" and "unequal".
"""
from itertools import product

ROWS = [
    (-1, +1,  0, -1,  0, -1),
    (+1,  0, +1,  0, +1, -1),
    ( 0,  0, -1, +1,  0, -1),
    (+1, +1,  0, +1,  0, +1),
    (-1,  0, -1,  0, +1, +1),
    (-1,  0, +1, +1,  0,  0),
]
N = 12
MASK = (1 << N) - 1


def comp(x):
    return MASK ^ x


def canon(x):
    return min(x, comp(x))


def hd(x, y):
    return (x ^ y).bit_count()


def folded_dist(x, c):
    return min(hd(x, c), hd(x, comp(c)))


def pack(bits):
    x = 0
    for b in bits:
        x = (x << 1) | b
    return x


def lift_equal_on_support(row, zero_orients):
    """Nonzero -> equal pair carrying row sign; zero -> arbitrary unequal pair."""
    it = iter(zero_orients)
    bits = []
    for s in row:
        if s == +1:
            bits += [1, 1]
        elif s == -1:
            bits += [0, 0]
        else:
            o = next(it)
            bits += [1, 0] if o == +1 else [0, 1]
    return canon(pack(bits))


def lift_unequal_on_support(row, zero_signs):
    """Nonzero -> oriented unequal pair carrying row sign; zero -> arbitrary equal pair."""
    it = iter(zero_signs)
    bits = []
    for s in row:
        if s == +1:
            bits += [1, 0]
        elif s == -1:
            bits += [0, 1]
        else:
            z = next(it)
            bits += [1, 1] if z == +1 else [0, 0]
    return canon(pack(bits))


def family(builder):
    groups = []
    for row in ROWS:
        z = sum(s == 0 for s in row)
        cs = sorted({builder(row, a) for a in product((-1, +1), repeat=z)})
        groups.append(cs)
    return groups, sorted({c for g in groups for c in g})


def reps():
    return [x for x in range(1 << N) if x < comp(x)]


def pair_type(x):
    """1 means unequal pair; 0 means equal pair."""
    bits = [((x >> (N - 1 - k)) & 1) for k in range(N)]
    return tuple(int(bits[2*j] != bits[2*j+1]) for j in range(6))


def uncovered(centers):
    return [x for x in reps() if all(folded_dist(x, c) > 3 for c in centers)]


groups_eq, centers_eq = family(lift_equal_on_support)
groups_neq, centers_neq = family(lift_unequal_on_support)

assert [len(g) for g in groups_eq] == [4, 4, 8, 4, 4, 8]
assert [len(g) for g in groups_neq] == [4, 4, 8, 4, 4, 8]
assert len(centers_eq) == 32
assert len(centers_neq) == 32
assert len(reps()) == 2048

u_eq = uncovered(centers_eq)
u_neq = uncovered(centers_neq)
assert len(u_eq) == 32
assert len(u_neq) == 32

T_EQ = (1, 0, 1, 1, 0, 1)
T_NEQ = tuple(1-t for t in T_EQ)
assert {pair_type(x) for x in u_eq} == {T_EQ}
assert {pair_type(x) for x in u_neq} == {T_NEQ}

all_eq_type = [x for x in reps() if pair_type(x) == T_EQ]
all_neq_type = [x for x in reps() if pair_type(x) == T_NEQ]
assert len(all_eq_type) == 32
assert len(all_neq_type) == 32
assert set(all_eq_type) == set(u_eq)
assert set(all_neq_type) == set(u_neq)

# Structural distance floor for L_eq, independent of signs/orientations:
# if U is the set of unequal target pairs and S a row support, the best
# possible pairwise Hamming contribution before equal-sign mismatches is
# |U cap S| + |U^c cap S^c|.
U = {i for i, t in enumerate(T_EQ) if t}
floors = []
for row in ROWS:
    S = {i for i, s in enumerate(row) if s != 0}
    floor = len(U & S) + len((set(range(6)) - U) & (set(range(6)) - S))
    floors.append(floor)
assert floors == [4, 4, 5, 4, 4, 5]
assert min(floors) == 4

# The two full polarity families together cover. This means the exact
# obstruction is to either naive one-polarity lift separately, not to the
# 64-center union. No claim is made here about selecting only 12 of those 64.
combined = sorted(set(centers_eq) | set(centers_neq))
assert len(combined) == 64
assert len(uncovered(combined)) == 0

print("R02_R13_PAIR_LIFT_EXACT_SELF_CHECK_PASS")
print("projective_universe=2048")
print("eq_group_sizes=4,4,8,4,4,8")
print("eq_centers=32")
print("eq_uncovered=32")
print("eq_uncovered_pair_type=101101")
print("eq_support_distance_floors=4,4,5,4,4,5")
print("neq_centers=32")
print("neq_uncovered=32")
print("neq_uncovered_pair_type=010010")
print("combined_centers=64")
print("combined_uncovered=0")
print("claim_scope=naive_pair_lift_only;_not_all_sign_matrices")

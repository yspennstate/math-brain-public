from itertools import combinations, permutations
from fractions import Fraction


def closure(n, mask):
    pairs = list(combinations(range(n), 2))
    reach = [0] * n
    for k, (i, j) in enumerate(pairs):
        if (mask >> k) & 1:
            reach[i] |= 1 << j
    for k in range(n):
        for i in range(n):
            if (reach[i] >> k) & 1:
                reach[i] |= reach[k]
    return tuple(reach)


def rel(R, u, v):
    if (R[u] >> v) & 1:
        return -1
    if (R[v] >> u) & 1:
        return 1
    return 0


def cover(R, x, y):
    if rel(R, x, y) != -1:
        return False
    return not any(
        z not in (x, y) and rel(R, x, z) == -1 and rel(R, z, y) == -1
        for z in range(len(R))
    )


def extension(order, R):
    p = {v: i for i, v in enumerate(order)}
    for u in range(len(R)):
        bits = R[u]
        while bits:
            b = bits & -bits
            v = b.bit_length() - 1
            if p[u] >= p[v]:
                return False
            bits -= b
    return True


def swap(order, u, v):
    w = list(order)
    i, j = w.index(u), w.index(v)
    w[i], w[j] = w[j], w[i]
    return tuple(w)


def active_blockers(order, R, x, y, a):
    p = {v: i for i, v in enumerate(order)}
    left = order[p[x] + 1 : p[a]]
    right = order[p[a] + 1 : p[y]]
    L = [v for v in left if rel(R, x, v) == -1 or rel(R, v, a) == -1]
    U = [v for v in right if rel(R, a, v) == -1 or rel(R, v, y) == -1]
    return L, U


posets = triples = strong = middle_extensions = 0
min_left_excess = None
min_right_excess = None

for n in range(3, 7):
    seen = set()
    for mask in range(1 << (n * (n - 1) // 2)):
        R = closure(n, mask)
        if R in seen:
            continue
        seen.add(R)
        posets += 1
        exts = [p for p in permutations(range(n)) if extension(p, R)]
        E = len(exts)
        for x in range(n):
            for y in range(n):
                if not cover(R, x, y):
                    continue
                for a in range(n):
                    if a in (x, y) or rel(R, a, x) != 0 or rel(R, a, y) != 0:
                        continue
                    triples += 1
                    A = [L for L in exts if L.index(a) < L.index(x)]
                    H = [L for L in exts if L.index(x) < L.index(a) < L.index(y)]
                    C = [L for L in exts if L.index(y) < L.index(a)]
                    assert len(A) + len(H) + len(C) == E
                    if not (
                        Fraction(len(H) + len(C), E) > Fraction(2, 3)
                        and Fraction(len(C), E) < Fraction(1, 3)
                    ):
                        continue
                    strong += 1
                    middle_extensions += len(H)

                    badL = badU = 0
                    Lseen = set()
                    Useen = set()
                    for L in H:
                        if not extension(swap(L, x, a), R):
                            badL += 1
                            bl, bu = active_blockers(L, R, x, y, a)
                            assert bl
                            Lseen.update(bl)
                        if not extension(swap(L, a, y), R):
                            badU += 1
                            bl, bu = active_blockers(L, R, x, y, a)
                            assert bu
                            Useen.update(bu)

                    assert badL >= len(H) - len(A) > 0
                    assert badU >= len(H) - len(C) > 0
                    assert Lseen and Useen and Lseen.isdisjoint(Useen)

                    Lcap = set()
                    Ucap = set()
                    for v in range(n):
                        if v in (x, y, a):
                            continue
                        if (
                            (rel(R, x, v) == -1 and rel(R, v, a) == 0)
                            or (rel(R, v, a) == -1 and rel(R, v, x) == 0)
                        ):
                            Lcap.add(v)
                        if (
                            (rel(R, a, v) == -1 and rel(R, v, y) == 0)
                            or (rel(R, v, y) == -1 and rel(R, v, a) == 0)
                        ):
                            Ucap.add(v)
                    assert Lseen <= Lcap
                    assert Useen <= Ucap
                    assert Lcap.isdisjoint(Ucap)

                    le = badL - (len(H) - len(A))
                    ue = badU - (len(H) - len(C))
                    min_left_excess = le if min_left_excess is None else min(min_left_excess, le)
                    min_right_excess = ue if min_right_excess is None else min(min_right_excess, ue)

print("naturally_labelled_transitive_closures", posets)
print("cover_incomparable_triples", triples)
print("strong_cover_flips", strong)
print("middle_extensions_checked", middle_extensions)
print("minimum_left_bad_minus_H_minus_A", min_left_excess)
print("minimum_right_bad_minus_H_minus_C", min_right_excess)

# Sharp five-point witness from account01/B19.
n = 5
R = [0] * n
for u, v in [(0, 2), (0, 3), (1, 2)]:
    R[u] |= 1 << v
for k in range(n):
    for i in range(n):
        if (R[i] >> k) & 1:
            R[i] |= R[k]
R = tuple(R)
exts = [p for p in permutations(range(n)) if extension(p, R)]
x, y, a = 0, 2, 4
A = [L for L in exts if L.index(a) < L.index(x)]
H = [L for L in exts if L.index(x) < L.index(a) < L.index(y)]
C = [L for L in exts if L.index(y) < L.index(a)]
badL = []
badU = []
Lseen = set()
Useen = set()
for L in H:
    if not extension(swap(L, x, a), R):
        badL.append(L)
        bl, bu = active_blockers(L, R, x, y, a)
        Lseen.update(bl)
    if not extension(swap(L, a, y), R):
        badU.append(L)
        bl, bu = active_blockers(L, R, x, y, a)
        Useen.update(bu)
print("sharp_witness_E_A_H_C", len(exts), len(A), len(H), len(C))
print("sharp_witness_bad_left_right", len(badL), len(badU))
print("sharp_witness_active_left_vertices", sorted(Lseen))
print("sharp_witness_active_right_vertices", sorted(Useen))
print("POS3_TWO_SIDED_ACTIVE_BLOCKER_REGRESSION_PASS")

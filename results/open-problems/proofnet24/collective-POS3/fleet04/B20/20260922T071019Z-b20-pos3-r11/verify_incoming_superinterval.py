#!/usr/bin/env python3
"""Deterministic regression for the POS3 incoming-superinterval lemma.

Enumerates every naturally labelled transitive closure through n=6, restricts
to width <=3, and checks incoming Hasse witnesses, family capacity,
disjointness, and endpoint-event containment. Standard library only.
"""
from itertools import combinations
from collections import defaultdict


def closure_from_edge_subset(n, mask):
    succ = [0] * n
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for k, (i, j) in enumerate(pairs):
        if (mask >> k) & 1:
            succ[i] |= 1 << j
    for k in range(n):
        kb = 1 << k
        for i in range(n):
            if succ[i] & kb:
                succ[i] |= succ[k]
    return tuple(succ)


def pred_from_succ(n, succ):
    pred = [0] * n
    for i in range(n):
        for j in range(n):
            if (succ[i] >> j) & 1:
                pred[j] |= 1 << i
    return tuple(pred)


def incomparable(succ, a, b):
    return not (((succ[a] >> b) & 1) or ((succ[b] >> a) & 1))


def cover(succ, a, b):
    if not ((succ[a] >> b) & 1):
        return False
    n = len(succ)
    return not any(
        z != a and z != b and ((succ[a] >> z) & 1) and ((succ[z] >> b) & 1)
        for z in range(n)
    )


def width_at_most_three(n, succ):
    for four in combinations(range(n), 4):
        if all(incomparable(succ, a, b) for a, b in combinations(four, 2)):
            return False
    return True


def linear_extensions(n, pred):
    out = []
    def rec(order, used):
        if len(order) == n:
            out.append(tuple(order))
            return
        for v in range(n):
            if not ((used >> v) & 1) and (pred[v] & ~used) == 0:
                rec(order + [v], used | (1 << v))
    rec([], 0)
    return out


def valid_order(order, succ):
    pos = [0] * len(order)
    for i, v in enumerate(order):
        pos[v] = i
    for u in range(len(order)):
        bits = succ[u]
        while bits:
            low = bits & -bits
            v = low.bit_length() - 1
            if pos[u] >= pos[v]:
                return False
            bits -= low
    return True


def count_event(extensions, before, after):
    return sum(L.index(before) < L.index(after) for L in extensions)


stats = defaultdict(int)
max_family = 0
failures = []

for n in range(3, 7):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    closures = {
        closure_from_edge_subset(n, mask)
        for mask in range(1 << len(pairs))
    }
    stats[f"closures_n{n}"] = len(closures)

    for succ in closures:
        if not width_at_most_three(n, succ):
            continue
        stats["width3_posets"] += 1
        pred = pred_from_succ(n, succ)
        extensions = linear_extensions(n, pred)
        cov = {(i, j) for i in range(n) for j in range(n) if cover(succ, i, j)}

        for x, y in cov:
            for a in range(n):
                if a in (x, y) or not incomparable(succ, a, x) or not incomparable(succ, a, y):
                    continue
                stats["triples"] += 1
                I1 = {r for r in range(n) if (r, x) in cov and incomparable(succ, r, a)}
                I2 = {r for r in range(n) if (a, r) in cov and incomparable(succ, r, x)}
                J1 = {r for r in range(n) if (y, r) in cov and incomparable(succ, r, a)}
                J2 = {r for r in range(n) if (r, a) in cov and incomparable(succ, r, y)}
                families = [I1, I2, J1, J2]
                max_family = max(max_family, *(len(S) for S in families))
                assert all(len(S) <= 2 for S in families)
                for i, j in combinations(range(4), 2):
                    assert not (families[i] & families[j])

                # Global event containment used in the symbolic proof.
                A = count_event(extensions, a, x)  # x<y is forced, so this is |A|.
                C = count_event(extensions, y, a)  # x<y is forced, so this is |C|.
                for r in I1:
                    assert count_event(extensions, a, r) <= A
                for r in I2:
                    assert count_event(extensions, r, x) <= A
                for r in J1:
                    assert count_event(extensions, r, a) <= C
                for r in J2:
                    assert count_event(extensions, y, r) <= C

                for L in extensions:
                    pos = {v: i for i, v in enumerate(L)}
                    if pos[a] < pos[x] < pos[y]:
                        swapped = list(L)
                        swapped[pos[a]], swapped[pos[x]] = swapped[pos[x]], swapped[pos[a]]
                        if not valid_order(swapped, succ):
                            stats["left_incoming"] += 1
                            witnesses = [r for r in I1 | I2 if pos[a] < pos[r] < pos[x]]
                            assert witnesses
                    if pos[x] < pos[y] < pos[a]:
                        swapped = list(L)
                        swapped[pos[y]], swapped[pos[a]] = swapped[pos[a]], swapped[pos[y]]
                        if not valid_order(swapped, succ):
                            stats["right_incoming"] += 1
                            witnesses = [r for r in J1 | J2 if pos[y] < pos[r] < pos[a]]
                            assert witnesses

print("natural_transitive_closures_n3", stats["closures_n3"])
print("natural_transitive_closures_n4", stats["closures_n4"])
print("natural_transitive_closures_n5", stats["closures_n5"])
print("natural_transitive_closures_n6", stats["closures_n6"])
print("width_at_most_three_posets", stats["width3_posets"])
print("cover_incomparable_triples", stats["triples"])
print("left_incoming_defects", stats["left_incoming"])
print("right_incoming_defects", stats["right_incoming"])
print("maximum_incoming_family_size", max_family)
print("failures", len(failures))
print("POS3_INCOMING_SUPERINTERVAL_CHECK_PASS")

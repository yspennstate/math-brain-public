#!/usr/bin/env python3
"""Exact finite verifier for HARD8-01 checkpoint 7.

Standard-library only. No floating point, randomness, external solver, or
solver-timeout inference is used.

It exhaustively checks every five-state one-idempotent SI automaton with the
fixed simple idempotent e:0->1 and an unordered alphabet of one or two distinct
permutation letters. Since all simple idempotents are conjugate in S_5, fixing
e loses no examples within this alphabet-size census.
"""

from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations

INF = 10**9


def compose(a, b):
    return tuple(b[a[i]] for i in range(len(a)))


def subset_image(S, a):
    return frozenset(a[x] for x in S)


def group_bfs(gens, n):
    identity = tuple(range(n))
    queue = deque([identity])
    dist = {identity: 0}
    group = [identity]
    while queue:
        g = queue.popleft()
        for p in gens:
            h = compose(g, p)
            if h not in dist:
                dist[h] = dist[g] + 1
                group.append(h)
                queue.append(h)
    return tuple(group), dist


def hole_bellman(n, gens, s=0, t=1):
    group, group_dist = group_bfs(gens, n)
    goal = frozenset(set(range(n)) - {t})

    @lru_cache(None)
    def F(H):
        if H == goal:
            return 0
        best = INF
        for u in group:
            Hu = subset_image(H, u)
            if s in Hu or t in Hu:
                continue
            H2 = frozenset(set(Hu) | {s})
            candidate = group_dist[u] + F(H2)
            if candidate < best:
                best = candidate
        return best

    start = frozenset({s})
    start_value = F(start)
    values = {}
    for mask in range(1 << n):
        H = frozenset(i for i in range(n) if (mask >> i) & 1)
        if s in H and t not in H:
            value = F(H)
            if value < INF:
                values[H] = value
    return start_value, values, group, group_dist


def prefix_constrained_optimum(n, group, group_dist, s=0, t=1):
    """Minimum travel among canonical paths with L_k <= k(n-1) at every prefix."""
    budget = n - 1
    start = frozenset({s})
    goal = frozenset(set(range(n)) - {t})
    current = {start: 0}
    for k in range(1, n - 1):
        nxt = {}
        for H, spent in current.items():
            for u in group:
                Hu = subset_image(H, u)
                if s in Hu or t in Hu:
                    continue
                H2 = frozenset(set(Hu) | {s})
                spent2 = spent + group_dist[u]
                if spent2 > k * budget:
                    continue
                if spent2 < nxt.get(H2, INF):
                    nxt[H2] = spent2
        current = nxt
        if not current:
            return INF
    return current.get(goal, INF)


def exhaustive_five_state_census():
    n = 5
    all_perms = list(permutations(range(n)))
    processed = synchronizing = prefix_failures = prefix_penalties = 0
    f_distribution = Counter()
    group_order_distribution = Counter()
    viable_two_hole_distribution = Counter()
    max_diameter = 0
    min_credit_margin = INF
    equality_signature = Counter()

    def process(index_set):
        nonlocal processed, synchronizing, prefix_failures, prefix_penalties
        nonlocal max_diameter, min_credit_margin
        gens = tuple(all_perms[i] for i in index_set)
        F0, values, group, group_dist = hole_bellman(n, gens)
        processed += 1
        if F0 >= INF:
            return
        synchronizing += 1
        prefix_opt = prefix_constrained_optimum(n, group, group_dist)
        if prefix_opt >= INF:
            prefix_failures += 1
        if prefix_opt != F0:
            prefix_penalties += 1
        f_distribution[F0] += 1
        group_order_distribution[len(group)] += 1
        diameter = max(group_dist.values())
        max_diameter = max(max_diameter, diameter)
        viable_two = sum(1 for H in values if len(H) == 2)
        viable_two_hole_distribution[viable_two] += 1
        margin = 12 - F0 - (viable_two - 1)
        min_credit_margin = min(min_credit_margin, margin)
        if margin == 0:
            equality_signature[(F0, viable_two, len(group), diameter)] += 1

    for i in range(len(all_perms)):
        process((i,))
    for i, j in combinations(range(len(all_perms)), 2):
        process((i, j))

    assert processed == 7260
    assert synchronizing == 5760
    assert prefix_failures == 0
    assert prefix_penalties == 0
    assert sorted(f_distribution.items()) == [
        (3, 1770), (4, 954), (5, 1272), (6, 990), (7, 492),
        (8, 204), (9, 60), (10, 6), (12, 12),
    ]
    assert sorted(group_order_distribution.items()) == [
        (4, 24), (5, 84), (8, 36), (10, 180), (12, 48),
        (20, 720), (24, 108), (60, 1140), (120, 3420),
    ]
    assert sorted(viable_two_hole_distribution.items()) == [(1, 264), (3, 5496)]
    assert max_diameter == 14
    assert min_credit_margin == 0
    assert equality_signature == Counter({
        (12, 1, 5, 4): 12,
        (10, 3, 120, 10): 6,
    })
    return {
        "processed": processed,
        "synchronizing": synchronizing,
        "prefix_failures": prefix_failures,
        "prefix_penalties": prefix_penalties,
        "F_distribution": sorted(f_distribution.items()),
        "group_order_distribution": sorted(group_order_distribution.items()),
        "viable_two_hole_distribution": sorted(viable_two_hole_distribution.items()),
        "max_positive_cayley_diameter": max_diameter,
        "min_start_credit_margin": min_credit_margin,
        "equality_signature": sorted(equality_signature.items()),
    }


def verify_c5_greedy_trap():
    cycle = (1, 2, 3, 4, 0)
    F0, values, group, group_dist = hole_bellman(5, (cycle,), 0, 1)
    assert F0 == 12
    assert frozenset({0, 2}) not in values
    assert frozenset({0, 3}) not in values
    assert values[frozenset({0, 4})] == 8
    transitions = []
    H = frozenset({0})
    for u in group:
        Hu = subset_image(H, u)
        if 0 in Hu or 1 in Hu:
            continue
        H2 = frozenset(set(Hu) | {0})
        transitions.append((group_dist[u], tuple(sorted(H2)), values.get(H2)))
    transitions.sort()
    assert transitions == [
        (2, (0, 2), None),
        (3, (0, 3), None),
        (4, (0, 4), 8),
    ]
    return transitions


def main():
    census = exhaustive_five_state_census()
    trap = verify_c5_greedy_trap()
    print("ALPHABETS_CHECKED", census["processed"])
    print("SYNCHRONIZING", census["synchronizing"])
    print("PREFIX_FAILURES", census["prefix_failures"])
    print("PREFIX_OPTIMUM_PENALTIES", census["prefix_penalties"])
    print("BELLMAN_TRAVEL_DISTRIBUTION", census["F_distribution"])
    print("GROUP_ORDER_DISTRIBUTION", census["group_order_distribution"])
    print("VIABLE_TWO_HOLE_DISTRIBUTION", census["viable_two_hole_distribution"])
    print("MAX_POSITIVE_CAYLEY_DIAMETER", census["max_positive_cayley_diameter"])
    print("MIN_START_CREDIT_MARGIN", census["min_start_credit_margin"])
    print("EQUALITY_SIGNATURE", census["equality_signature"])
    print("C5_FIRST_TRANSITIONS", trap)
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()

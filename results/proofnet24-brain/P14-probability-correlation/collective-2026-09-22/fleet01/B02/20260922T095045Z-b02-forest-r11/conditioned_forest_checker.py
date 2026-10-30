#!/usr/bin/env python3
"""Exact finite check for the FOREST conditioned-disconnection subproblem.

For each n=3,...,6, fix terminals u=0,v=1 and enumerate every simple graph H
on [n] in which uv is absent. For every pair of distinct present edges e,f,
count uniformly all forests A of H with u and v disconnected and verify

    D_e D_f - D D_ef >= 0.

Fixing the terminal pair loses no cases up to relabelling. All arithmetic is
integer and exhaustive; no randomness or external service is used.
"""
from itertools import combinations


def forest_and_disconnected(mask, edges, n):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, (a, b) in enumerate(edges):
        if (mask >> i) & 1:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[rb] = ra
    return find(0) != find(1)


def zeta(arr, m):
    arr = arr[:]
    for i in range(m):
        bit = 1 << i
        for mask in range(1 << m):
            if mask & bit:
                arr[mask] += arr[mask ^ bit]
    return arr


def check_n(n):
    edges = [e for e in combinations(range(n), 2) if e != (0, 1)]
    m = len(edges)
    size = 1 << m

    base = [int(forest_and_disconnected(mask, edges, n))
            for mask in range(size)]
    D = zeta(base, m)

    D_e = []
    for i in range(m):
        D_e.append(zeta(
            [base[s] if ((s >> i) & 1) else 0 for s in range(size)], m
        ))

    total = negative = zero = positive = 0
    min_gap = None
    max_gap = None

    for i, j in combinations(range(m), 2):
        D_ef = zeta(
            [base[s] if (((s >> i) & 1) and ((s >> j) & 1)) else 0
             for s in range(size)], m
        )
        for H in range(size):
            if not (((H >> i) & 1) and ((H >> j) & 1)):
                continue
            gap = D_e[i][H] * D_e[j][H] - D[H] * D_ef[H]
            total += 1
            if gap < 0:
                negative += 1
            elif gap == 0:
                zero += 1
            else:
                positive += 1
            min_gap = gap if min_gap is None else min(min_gap, gap)
            max_gap = gap if max_gap is None else max(max_gap, gap)

    assert negative == 0
    return {
        "n": n,
        "candidate_edges_excluding_uv": m,
        "graphs": size,
        "marked_pair_instances": total,
        "negative": negative,
        "zero": zero,
        "positive": positive,
        "min_gap": min_gap,
        "max_gap": max_gap,
    }


def main():
    rows = [check_n(n) for n in range(3, 7)]
    for row in rows:
        print(row)
    print("TOTAL_MARKED_PAIR_INSTANCES", sum(r["marked_pair_instances"] for r in rows))
    print("TOTAL_NEGATIVE", sum(r["negative"] for r in rows))
    print("STATUS=PASS")


if __name__ == "__main__":
    main()

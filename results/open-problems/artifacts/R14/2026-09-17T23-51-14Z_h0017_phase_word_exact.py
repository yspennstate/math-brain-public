#!/usr/bin/env python3
"""
Exact-arithmetic checker for R14-H0017 finite-word phase-switch construction.

For every N/E word of length m=5, construct two disjoint monotone corridors in
a finite square lattice box. The unique shortest path from the origin to the
halfspace {x+y >= 2k} must begin with the k-th prescribed letter.

All weights are positive integers. Dijkstra uses exact integer arithmetic.
"""

from itertools import product
from heapq import heappush, heappop
from collections import defaultdict

MWORD = 5


def pN(j):
    if j == 0:
        return (0, 0)
    if j % 2:
        k = (j + 1) // 2
        return (k - 1, k)
    k = j // 2
    return (k - 1, k + 1)


def pE(j):
    x, y = pN(j)
    return (y, x)


def canon(a, b):
    return (a, b) if a < b else (b, a)


def build(word):
    m = len(word)
    R = m + 1
    BIG = 100 * m + 100
    verts = [(x, y) for x in range(-R, R + 1) for y in range(-R, R + 1)]
    edges = []
    for x, y in verts:
        if x < R:
            edges.append(((x, y), (x + 1, y)))
        if y < R:
            edges.append(((x, y), (x, y + 1)))
    W = {canon(a, b): BIG for a, b in edges}

    Aprev = Bprev = 0
    for k, s in enumerate(word, 1):
        delta = -1 if s == "N" else +1
        A = 10 * k + delta
        B = 10 * k - delta
        blockA = A - Aprev
        blockB = B - Bprev
        assert blockA >= 8 and blockB >= 8

        W[canon(pN(2*k-2), pN(2*k-1))] = 1
        W[canon(pN(2*k-1), pN(2*k))] = blockA - 1
        W[canon(pE(2*k-2), pE(2*k-1))] = 1
        W[canon(pE(2*k-1), pE(2*k))] = blockB - 1
        Aprev, Bprev = A, B

    return verts, edges, W


def dijkstra(verts, edges, W):
    root = (0, 0)
    adj = defaultdict(list)
    for a, b in edges:
        w = W[canon(a, b)]
        adj[a].append((b, w))
        adj[b].append((a, w))

    INF = 10**100
    dist = {v: INF for v in verts}
    count = {v: 0 for v in verts}
    first = {v: set() for v in verts}
    dist[root] = 0
    count[root] = 1
    pq = [(0, root)]

    while pq:
        d, u = heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            fs = {v} if u == root else first[u]
            if nd < dist[v]:
                dist[v] = nd
                count[v] = count[u]
                first[v] = set(fs)
                heappush(pq, (nd, v))
            elif nd == dist[v]:
                count[v] += count[u]
                first[v] |= fs
    return dist, count, first


def check_word(word):
    verts, edges, W = build(word)
    dist, count, first = dijkstra(verts, edges, W)
    rows = []
    for k, s in enumerate(word, 1):
        targets = [v for v in verts if v[0] + v[1] >= 2*k]
        best = min(dist[v] for v in targets)
        winners = [v for v in targets if dist[v] == best]
        assert len(winners) == 1, (word, k, winners)
        v = winners[0]
        assert count[v] == 1, (word, k, "nonunique geodesic", count[v])
        expected = (0, 1) if s == "N" else (1, 0)
        assert first[v] == {expected}, (word, k, first[v], expected)
        assert best == 10*k - 1, (word, k, best)
        rows.append((k, s, best, v, expected))
    return rows


def main():
    words = ["".join(w) for w in product("NE", repeat=MWORD)]
    for word in words:
        check_word(word)
    sample = "NENEN"
    rows = check_word(sample)
    print(f"EXHAUSTIVE_WORDS={len(words)}")
    print("SAMPLE=" + sample)
    for k, s, best, v, expected in rows:
        print(f"k={k} prescribed={s} cost={best} target={v} first={expected}")
    print("ALL_32_WORDS_PASS")


if __name__ == "__main__":
    main()

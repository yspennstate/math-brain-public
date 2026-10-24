"""Exhaustively check the finite self-dual crossing identity for n <= 3."""

from collections import deque


def grid(n, slit=False):
    points = [(x, y) for x in range(n + 1) for y in range(n)]
    if slit:
        points = [p for p in points if p[0] != n // 2]
    index = {p: i for i, p in enumerate(points)}
    edges = []
    for x, y in points:
        for q in ((x + 1, y), (x, y + 1)):
            if q in index:
                edges.append((index[x, y], index[q]))
    starts = [index[p] for p in points if p[0] == 0]
    targets = {index[p] for p in points if p[0] == n}
    return len(points), edges, starts, targets


def count_crossings(n, slit=False):
    vertices, edges, starts, targets = grid(n, slit)
    total = 1 << len(edges)
    hits = 0
    for mask in range(total):
        neighbors = [[] for _ in range(vertices)]
        for bit, (u, v) in enumerate(edges):
            if mask & (1 << bit):
                neighbors[u].append(v)
                neighbors[v].append(u)
        seen = set(starts)
        pending = deque(starts)
        while pending:
            u = pending.popleft()
            for v in neighbors[u]:
                if v not in seen:
                    seen.add(v)
                    pending.append(v)
        hits += bool(seen & targets)
    return hits, total


for n in (1, 2, 3):
    hits, total = count_crossings(n)
    assert 2 * hits == total, (n, hits, total)
    print(f"full n={n}: {hits}/{total} = 1/2")
for n in (2, 3):
    hits, total = count_crossings(n, slit=True)
    assert hits == 0, (n, hits, total)
    print(f"slit n={n}: {hits}/{total} = 0")

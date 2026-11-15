"""Small local check of the uncoloured constructions in FPRAS Lemma 6.4."""
from collections import Counter
from itertools import combinations

def edge(u, v):
    return tuple(sorted((u, v)))

def matching(edges, n):
    degree = Counter(v for e in edges for v in e)
    return len(edges) == n // 2 and all(degree[v] == 1 for v in range(n))

def union(a, b):
    return Counter(a) + Counter(b)

def patterns(path):
    through = {edge(path[i], path[i + 1]) for i in range(0, len(path) - 1, 2)}
    interior = {edge(path[i], path[i + 1]) for i in range(1, len(path) - 2, 2)}
    chord = edge(path[0], path[-1])
    closed = interior | {chord}
    return through, interior, closed, chord

def repair(through, path):
    result = set(through)
    result.remove(edge(path[0], path[1]))
    if len(path) > 2:
        result.remove(edge(path[-2], path[-1]))
        result.add(edge(path[1], path[-2]))
    return result

def audit_pair(a, b, original, n):
    assert matching(a, n) and matching(b, n)
    out = union(a, b)
    added, dropped = out - original, original - out
    assert sum(added.values()) == sum(dropped.values()) <= 4
    rebuilt = out.copy()
    rebuilt.subtract(added)
    rebuilt.update(dropped)
    assert +rebuilt == original

cells = switch_cases = error_cases = 0
for n in range(4, 15, 2):
    o0 = {edge(i, (i + 1) % n) for i in range(0, n, 2)}
    o1 = {edge(i, (i + 1) % n) for i in range(1, n, 2)}
    original = union(o0, o1)
    for rest in combinations(range(1, n), 3):
        corners = (0,) + rest
        ends = corners + (n,)
        if any((ends[j + 1] - ends[j]) % 2 == 0 for j in range(4)):
            continue
        paths = [tuple(i % n for i in range(ends[j], ends[j + 1] + 1))
                 for j in range(4)]
        data = [patterns(path) for path in paths]
        cells += 1
        p = tuple(j for j in range(4) if data[j][0] <= o0)
        assert len(p) == 2
        ap = set().union(*(d[1] for d in data)) | {data[j][3] for j in p}
        # In a one-bag complete graph every arc is good: both choices are legal.
        for good in ((0, 2), (1, 3)):
            guide_parts = [repair(d[0], paths[j]) if j in good else d[0]
                           for j, d in enumerate(data)]
            guide = set().union(*guide_parts)
            audit_pair(ap, guide, original, n)
            switch_cases += 1
        for xy in ((0, 2), (1, 3)):
            if any(len(paths[j]) == 2 for j in xy):
                continue
            for y, x in (xy, xy[::-1]):
                a0 = o0 if data[x][0] <= o0 else o1
                parts = [data[j][2] if j in xy else repair(data[j][0], paths[j])
                         for j in range(4)]
                b0 = set().union(*parts)
                audit_pair(a0, b0, original, n)
                assert data[x][2] <= b0
                a1 = (a0 - data[y][0]) | data[y][2]
                b1 = (b0 - data[y][2]) | data[y][0]
                assert union(a1, b1) == union(a0, b0)
                audit_pair(a1, b1, original, n)
                assert data[x][2] <= b1
                error_cases += 1
print(f"orders 4,6,8,10,12,14: {cells} cells; "
      f"{switch_cases} switch encodings; {error_cases} ordered error encodings "
      "(both contexts checked); all assertions passed")

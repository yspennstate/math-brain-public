#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction

TARGETS = [
    Fraction(1,7), Fraction(1,3), Fraction(2,5), Fraction(5,7),
    Fraction(8,7), Fraction(4,3), Fraction(7,5), Fraction(12,7),
]

def ratio(n, edges):
    m = len(edges)
    D = C = 0
    for mask in range(1 << m):
        parent = list(range(n))
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        ok = True
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                ru, rv = find(u), find(v)
                if ru == rv:
                    ok = False
                    break
                parent[ru] = rv
        if not ok:
            continue
        if find(0) == find(1):
            C += 1
        else:
            D += 1
    assert D > 0
    return Fraction(C, D), D, C

ratios = {}
examples = {}
for k in range(3):
    n = k + 2
    all_edges = list(combinations(range(n), 2))
    vals = set()
    for emask in range(1 << len(all_edges)):
        edges = tuple(all_edges[i] for i in range(len(all_edges)) if (emask >> i) & 1)
        r, D, C = ratio(n, edges)
        vals.add(r)
        examples.setdefault((k, r), (edges, D, C))
    ratios[k] = sorted(vals)

for k in range(3):
    print(f"k={k} ratios:", " ".join(map(str, ratios[k])))

for t in TARGETS:
    mk = next((k for k in range(3) if t in ratios[k]), None)
    assert mk is not None
    edges, D, C = examples[(mk, t)]
    print(f"target {t} min_internal={mk} D={D} C={C} edges={edges}")

assert ratios[0] == [Fraction(0), Fraction(1)]
assert ratios[1] == [Fraction(0), Fraction(1,3), Fraction(1), Fraction(4,3)]
assert all(next(k for k in range(3) if t in ratios[k]) == (1 if t in {Fraction(1,3), Fraction(4,3)} else 2) for t in TARGETS)
print("EXACT_CHECK_PASS")

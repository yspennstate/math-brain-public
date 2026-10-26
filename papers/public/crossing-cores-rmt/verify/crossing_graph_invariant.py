import os
"""Does the chord-intersection graph G_x(pi) of Proposition 4.3 determine
the volume?  Group all 105 order-eight pairings by the ISOMORPHISM CLASS
of their crossing graph and see whether the volume is constant."""
import sys
from itertools import combinations, permutations
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact

def crossing_graph(pm):
    n = len(pm)
    pairs = [(i, pm[i]) for i in range(n) if i < pm[i]]
    m = len(pairs)
    edges = set()
    for x, y in combinations(range(m), 2):
        a, b = pairs[x]; c, d = pairs[y]
        if a < c < b < d or c < a < d < b:
            edges.add((x, y))
    return m, edges

def canon(m, edges):
    best = None
    for p in permutations(range(m)):
        e = frozenset(tuple(sorted((p[x], p[y]))) for x, y in edges)
        key = tuple(sorted(e))
        if best is None or key < best:
            best = key
    return best

groups = {}
for pm in tk_core.all_pairings(8):
    m, e = crossing_graph(pm)
    key = canon(m, e)
    v = pairing_volume_exact(pm, "T")
    groups.setdefault(key, set()).add(v)

bad = {k: v for k, v in groups.items() if len(v) > 1}
print(f"distinct crossing-graph isomorphism classes at order 8: {len(groups)}")
print(f"classes carrying more than one volume: {len(bad)}")
for k, vs in list(bad.items())[:5]:
    print(f"   edges {sorted(k)} -> {sorted(str(x) for x in vs)}")
if not bad:
    print("THE CROSSING GRAPH DETERMINES THE VOLUME at order 8")
    for k, vs in sorted(groups.items(), key=lambda kv: len(kv[0])):
        print(f"   {len(k)} edges {sorted(k)} -> {list(vs)[0]}")

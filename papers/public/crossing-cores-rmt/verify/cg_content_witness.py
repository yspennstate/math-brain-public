import os
"""Name the witness pair: two inequivalent diagrams, one interlacement
graph, one volume.  No volume recomputation needed to find them."""
import sys
from itertools import combinations, permutations
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact

def cg(pm):
    n = len(pm)
    pairs = [(i, pm[i]) for i in range(n) if i < pm[i]]
    m = len(pairs); e = set()
    for x, y in combinations(range(m), 2):
        a,b = pairs[x]; c,d = pairs[y]
        if a < c < b < d or c < a < d < b: e.add((x,y))
    return m, e

def canon(m, e):
    best = None
    for p in permutations(range(m)):
        k = tuple(sorted(tuple(sorted((p[x],p[y]))) for x,y in e))
        if best is None or k < best: best = k
    return best

def dihedral_canon(pm):
    n2 = len(pm); best = None
    for r in range(n2):
        for s in (1, -1):
            new = [0]*n2
            for i in range(n2):
                new[(s*i + r) % n2] = (s*pm[i] + r) % n2
            t = tuple(new)
            if best is None or t < best: best = t
    return best

def word_of(pm):
    lab, nxt, out = {}, 0, []
    for i in range(len(pm)):
        c = min(i, pm[i])
        if c not in lab: lab[c] = chr(97+nxt); nxt += 1
        out.append(lab[c])
    return "".join(out)

TARGETS = [((0,1),(0,2),(1,3),(2,4)), ((0,1),(0,2),(0,3),(1,4))]
seen = {t: {} for t in TARGETS}
for pm in tk_core.all_pairings(10):
    m, e = cg(pm)
    k = canon(m, e)
    if k in seen:
        d = dihedral_canon(pm)
        if d not in seen[k]: seen[k][d] = pm
for t in TARGETS:
    print(f"graph {t}:")
    for d, pm in seen[t].items():
        print(f"    {word_of(pm)}   vol {pairing_volume_exact(pm,'T')}")

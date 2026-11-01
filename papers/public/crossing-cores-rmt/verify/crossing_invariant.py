import os
"""Do the crossing number, the nesting number, or the pair determine the
volume at order eight?"""
import sys
from itertools import combinations
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact

def cr_ne(pm):
    n = len(pm)
    pairs = [(i, pm[i]) for i in range(n) if i < pm[i]]
    cr = ne = 0
    for (a,b),(c,d) in combinations(pairs, 2):
        if a < c < b < d or c < a < d < b: cr += 1
        elif a < c < d < b or c < a < b < d: ne += 1
    return cr, ne

data = []
for pm in tk_core.all_pairings(8):
    data.append((cr_ne(pm), pairing_volume_exact(pm, "T")))

for name, key in (("crossing number", lambda k: k[0]),
                  ("nesting number", lambda k: k[1]),
                  ("(crossing, nesting)", lambda k: k)):
    g = {}
    for k, v in data:
        g.setdefault(key(k), set()).add(v)
    bad = {a: vs for a, vs in g.items() if len(vs) > 1}
    print(f"{name:22s}: {len(g)} classes, {len(bad)} carry multiple volumes")
    for a, vs in list(bad.items())[:3]:
        print(f"      {a} -> {sorted(str(v) for v in vs)}")

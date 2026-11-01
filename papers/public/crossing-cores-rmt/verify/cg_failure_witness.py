import os
"""The single failing class at order ten: which words share the crossing
graph {(0,1),(2,3)} on five chords yet differ in volume?"""
import sys
from itertools import combinations, permutations
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact
from fractions import Fraction as Fr

def cg(pm):
    n = len(pm)
    pairs = [(i, pm[i]) for i in range(n) if i < pm[i]]
    m = len(pairs)
    e = set()
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

def word_of(pm):
    lab, nxt, out = {}, 0, []
    for i in range(len(pm)):
        c = min(i, pm[i])
        if c not in lab: lab[c] = chr(97+nxt); nxt += 1
        out.append(lab[c])
    return "".join(out)

def nestings(pm):
    n = len(pm)
    pairs = [(i, pm[i]) for i in range(n) if i < pm[i]]
    ne = 0
    for (a,b),(c,d) in combinations(pairs, 2):
        if a < c < d < b or c < a < b < d: ne += 1
    return ne

TARGET = ((0,1),(2,3))
found = {}
for pm in tk_core.all_pairings(10):
    m, e = cg(pm)
    if canon(m, e) != TARGET: continue
    v = pairing_volume_exact(pm, "T")
    found.setdefault(v, []).append(pm)
for v in sorted(found, reverse=True):
    pm = found[v][0]
    print(f"volume {v}: {len(found[v])} words, e.g. {word_of(pm)}  "
          f"nestings={nestings(pm)}")

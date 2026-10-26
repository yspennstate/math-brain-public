import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
from exact_volume import pairing_volume_exact
from fractions import Fraction as Fr
def wpm(w):
    pos = {}
    for i, ch in enumerate(w):
        pos.setdefault(ch, []).append(i)
    pm = [0]*len(w)
    for ch,(a,b) in pos.items():
        pm[a], pm[b] = b, a
    return tuple(pm)
def states(w):
    pm = wpm(w); n = len(pm); s = set(); out = []
    for l in range(n):
        c = min(l, pm[l])
        if c in s: s.discard(c)
        else: s.add(c)
        out.append(frozenset(s))
    return out
for w in ("abcdabcd", "abacbdcd", "abcadbcd"):
    st = states(w)
    v = pairing_volume_exact(wpm(w), "T")
    print(f"{w}: {len(set(st))} distinct prefix states, p_T = {v} = {float(v):.5f}")

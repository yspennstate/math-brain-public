import os
"""Does the Dyck path (height sequence of open chords) determine the
volume?  Group all 105 order-eight pairings by height sequence and check
whether the volume is constant on each group."""
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact
from fractions import Fraction as Fr

def heights(pm):
    n = len(pm); s = set(); out = []
    for l in range(n):
        c = min(l, pm[l])
        if c in s: s.discard(c)
        else: s.add(c)
        out.append(len(s))
    return tuple(out)

groups = {}
for pm in tk_core.all_pairings(8):
    h = heights(pm)
    v = pairing_volume_exact(pm, "T")
    groups.setdefault(h, set()).add(v)

split = {h: vs for h, vs in groups.items() if len(vs) > 1}
print(f"distinct height sequences at order 8: {len(groups)}")
print(f"height sequences carrying MORE THAN ONE volume: {len(split)}")
for h, vs in list(split.items())[:6]:
    print(f"   {h} -> {sorted(str(v) for v in vs)}")
if not split:
    print("the Dyck path determines the volume at order 8")

"""Adjacent colouring form: sign of D = P_+ - P_-/t (see colour_split.py and README). python colour_split_sign.py V m seed cnt"""
import sys, random
from collections import defaultdict

from e1_swap import comps
V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed)
sign = defaultdict(int); PP = PM = 0
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    for fi in range(m):
        for v, w in (H[fi], H[fi][::-1]):
            for u in range(V):
                if u in (v, w): continue
                D = defaultdict(int)
                for mask in range(1 << m):
                    if mask >> fi & 1: continue
                    red = [H[j] for j in range(m) if mask >> j & 1]
                    blue = [H[j] for j in range(m) if not mask >> j & 1]
                    kr, fr = comps(V, red)
                    if fr(u) == fr(v): continue
                    kb, fb = comps(V, blue)
                    if fb(u) != fb(v) or fr(w) == fr(u): continue
                    bm = [H[j] for j in range(m) if not mask >> j & 1 and j != fi]
                    kb2, fb2 = comps(V, bm)
                    if fb2(u) != fb2(v): continue
                    d = (kb2 - kb) - (1 if fr(v) != fr(w) else 0)
                    if d == 1: D[kr + kb] += 1; PP += 1
                    elif d == -1: D[kr + kb - 1] -= 1; PM += 1
                vals = [c for c in D.values() if c]
                sign['zero' if not vals else 'pos' if min(vals) > 0 else 'neg' if max(vals) < 0 else 'mixed'] += 1
print(V, m, seed, dict(sign), 'P+ total', PP, 'P- total', PM)

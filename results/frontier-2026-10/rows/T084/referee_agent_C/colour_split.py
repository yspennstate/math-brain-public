"""Adjacent colouring form, f = vw, split by the flip of f. Bad colourings (f red) flip injectively onto the good
colourings G* with w not reaching u in red and f not a u-v bridge in blue; the cluster total moves by
delta = [f bridge in blue] - [v, w apart in red - f]. Left over: G1 (w reaches u in red) and G2 (w does not, but f is a
u-v bridge in blue). E1 here reads G1 + G2 + sum_{G*} (t^k - t^(k+delta)) >= 0. Sharper test: is
G1 + G2 >= the shifted terms alone, level by level, i.e. G1_k + G2_k >= #{G* : k + delta = k, delta != 0}?
python colour_split.py V m seed cnt"""
import sys, random
from collections import defaultdict
from e1_swap import comps

V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed)
tot = e1_fail = sharp_fail = 0
ex = None
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    for fi in range(m):
        for v, w in (H[fi], H[fi][::-1]):
            for u in range(V):
                if u in (v, w):
                    continue
                left = defaultdict(int)   # G1 + G2 by level
                need = defaultdict(int)   # shifted G* terms landing at each level
                e1 = defaultdict(int)
                for mask in range(1 << m):
                    if mask >> fi & 1:
                        continue          # enumerate good colourings: f blue
                    red = [H[j] for j in range(m) if mask >> j & 1]
                    blue = [H[j] for j in range(m) if not mask >> j & 1]
                    kr, fr = comps(V, red)
                    if fr(u) == fr(v):
                        continue
                    kb, fb = comps(V, blue)
                    if fb(u) != fb(v):
                        continue
                    k = kr + kb
                    e1[k] += 1
                    if fr(w) == fr(u):
                        left[k] += 1      # G1
                        continue
                    bm = [H[j] for j in range(m) if not mask >> j & 1 and j != fi]
                    kb2, fb2 = comps(V, bm)
                    if fb2(u) != fb2(v):
                        left[k] += 1      # G2
                        continue
                    d = (kb2 - kb) - (1 if fr(v) != fr(w) else 0)
                    e1[k + d] -= 1
                    if d:
                        need[k + d] += 1
                        left[k] += 0
                tot += 1
                if any(c < 0 for c in e1.values()):
                    e1_fail += 1
                if any(left[k] < need[k] for k in need):
                    sharp_fail += 1
                    if ex is None:
                        ex = (H, (v, w), u, dict(left), dict(need))
print('V %d m %d seed %d: adjacent cases %d, E1 fails %d, sharp (G1+G2 >= shifted) fails %d'
      % (V, m, seed, tot, e1_fail, sharp_fail))
print('first sharp failure:', ex)

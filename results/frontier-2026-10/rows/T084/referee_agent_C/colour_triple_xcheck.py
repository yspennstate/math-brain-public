"""Cross-check: for f = vw in H, D (flip-of-f split on H, colour_split_sign.py) equals -T shifted by one, where T is
statement S's count on H - f: D[j] = -T[j + 1]. python colour_triple_xcheck.py V m seed cnt"""
import sys, random
from collections import defaultdict
from e1_swap import comps

V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed)
agree = disagree = 0
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    for fi in range(m):
        for v, w in (H[fi], H[fi][::-1]):
            for u in range(V):
                if u in (v, w):
                    continue
                D = defaultdict(int)
                for mask in range(1 << m):
                    if mask >> fi & 1:
                        continue
                    red = [H[j] for j in range(m) if mask >> j & 1]
                    blue = [H[j] for j in range(m) if not mask >> j & 1]
                    kr, fr = comps(V, red)
                    if fr(u) == fr(v):
                        continue
                    kb, fb = comps(V, blue)
                    if fb(u) != fb(v) or fr(w) == fr(u):
                        continue
                    kb2, fb2 = comps(V, [H[j] for j in range(m) if not mask >> j & 1 and j != fi])
                    if fb2(u) != fb2(v):
                        continue
                    dl = (kb2 - kb) - (1 if fr(v) != fr(w) else 0)
                    if dl == 1:
                        D[kr + kb] += 1
                    elif dl == -1:
                        D[kr + kb - 1] -= 1
                H2 = H[:fi] + H[fi + 1:]
                T = defaultdict(int)
                for mask in range(1 << (m - 1)):
                    red = [H2[j] for j in range(m - 1) if mask >> j & 1]
                    kr, fr = comps(V, red)
                    if fr(u) == fr(v) or fr(u) == fr(w):
                        continue
                    blue = [H2[j] for j in range(m - 1) if not mask >> j & 1]
                    kb, fb = comps(V, blue)
                    if fb(u) != fb(v):
                        continue
                    bvw, rvw = fb(v) == fb(w), fr(v) == fr(w)
                    if bvw != rvw:
                        T[kr + kb] += 1 if bvw else -1
                lhs = {j: c for j, c in D.items() if c}
                rhs = {j - 1: -c for j, c in T.items() if c}
                if lhs == rhs:
                    agree += 1
                else:
                    disagree += 1
print('V %d m %d seed %d: D == -T shifted in %d cases, differs in %d' % (V, m, seed, agree, disagree))

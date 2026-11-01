"""Statement S: H a multigraph, u, v, w three vertices. Among 2-colourings of H with red separating u from v and from w
and blue joining u to v, at every k(red) + k(blue):
    #{v ~ w in blue, v !~ w in red} >= #{v !~ w in blue, v ~ w in red}.
For H = H' - f with f = vw this is exactly 'D has no positive coefficient' in the flip-of-f split (README). Here it is
tested for arbitrary triples, with no edge vw required. python colour_triple.py V m seed cnt"""
import sys, random
from collections import defaultdict
from e1_swap import comps

V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed)
cases = fails = 0
ex = None
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    for u in range(V):
        for v in range(V):
            for w in range(V):
                if len({u, v, w}) < 3:
                    continue
                T = defaultdict(int)
                for mask in range(1 << m):
                    red = [H[j] for j in range(m) if mask >> j & 1]
                    kr, fr = comps(V, red)
                    if fr(u) == fr(v) or fr(u) == fr(w):
                        continue
                    blue = [H[j] for j in range(m) if not mask >> j & 1]
                    kb, fb = comps(V, blue)
                    if fb(u) != fb(v):
                        continue
                    bvw, rvw = fb(v) == fb(w), fr(v) == fr(w)
                    if bvw != rvw:
                        T[kr + kb] += 1 if bvw else -1
                cases += 1
                if any(c < 0 for c in T.values()):
                    fails += 1
                    if ex is None:
                        ex = (H, u, v, w, dict(T))
print('V %d m %d seed %d: triples %d, S fails %d' % (V, m, seed, cases, fails))
if ex:
    print('first failure:', ex)

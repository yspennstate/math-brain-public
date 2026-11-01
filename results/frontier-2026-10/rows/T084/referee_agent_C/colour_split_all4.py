"""Every multigraph on 4 vertices with m edges (multiplicities over the 6 vertex pairs), every adjacent (f = vw, u):
the flip-of-f split (colour_split.py). Counts cases where E1 fails and where D = P_+ - P_-/t has a positive
coefficient. python colour_split_all4.py m"""
import sys, itertools
from collections import defaultdict
from e1_swap import comps

m = int(sys.argv[1])
V = 4
pairs = list(itertools.combinations(range(V), 2))
cases = e1_fail = d_pos = 0
for mult in itertools.product(range(m + 1), repeat=6):
    if sum(mult) != m:
        continue
    H = [p for p, c in zip(pairs, mult) for _ in range(c)]
    seen = set()
    for fi in range(m):
        for v, w in (H[fi], H[fi][::-1]):
            for u in range(V):
                if u in (v, w) or (H[fi], v, u) in seen:
                    continue
                seen.add((H[fi], v, u))   # parallel copies of f give the same case
                E = defaultdict(int); D = defaultdict(int)
                for mask in range(1 << m):
                    red = [H[j] for j in range(m) if mask >> j & 1]
                    blue = [H[j] for j in range(m) if not mask >> j & 1]
                    kr, fr = comps(V, red)
                    if fr(u) == fr(v):
                        continue
                    kb, fb = comps(V, blue)
                    if fb(u) != fb(v):
                        continue
                    if mask >> fi & 1:
                        E[kr + kb] -= 1
                        continue
                    E[kr + kb] += 1
                    if fr(w) == fr(u):
                        continue
                    kb2, fb2 = comps(V, [H[j] for j in range(m) if not mask >> j & 1 and j != fi])
                    if fb2(u) != fb2(v):
                        continue
                    dl = (kb2 - kb) - (1 if fr(v) != fr(w) else 0)
                    if dl == 1:
                        D[kr + kb] += 1
                    elif dl == -1:
                        D[kr + kb - 1] -= 1
                cases += 1
                e1_fail += any(c < 0 for c in E.values())
                d_pos += any(c > 0 for c in D.values())
print('all multigraphs on 4 vertices with %d edges: adjacent cases %d, E1 fails %d, D with a positive coefficient %d'
      % (m, cases, e1_fail, d_pos), flush=True)

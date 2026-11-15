# Exact check: 5-state padding of the K5P four-state family (a,b,u,v + e hung on v), merges giving ratio -> 2.
import sys
sys.path.insert(0, r'~\agent_run\k5')
from fractions import Fraction as F
import importlib.util
spec = importlib.util.spec_from_file_location('cfc', r'~\agent_run\k5\check_fork_comb.py')
src = open(spec.origin).read().split('print("N states')[0]
ns = {}; exec(src, ns)
tmix, lump = ns['tmix'], ns['lump']

def fam(t, pad, eps=None):
    t = F(t); n = 5 if pad else 4
    w = [[F(0)] * n for _ in range(n)]
    def s(x, y, v):
        w[x][y] += v
        if x != y: w[y][x] += v
    a, b, u, v = 0, 1, 2, 3
    s(a, u, 1); s(b, u, 1); s(u, v, t**2); s(a, a, t - 1); s(b, b, t - 1); s(v, v, t**6)
    if pad:
        e = 4; s(e, v, t**8); s(e, e, t**9)
    return w

for t in (10, 100, 1000):
    w4 = fam(t, False); r4 = tmix(lump(w4, [[0], [1], [2, 3]])) / tmix(w4)
    w5 = fam(t, True)
    r5a = tmix(lump(w5, [[0], [1], [2, 3, 4]])) / tmix(w5)       # 5 -> 3
    r5b = tmix(lump(w5, [[0], [1], [2, 3], [4]])) / tmix(w5)     # one merge 5 -> 4
    print(t, f"{float(r4):.9f} pad5->3 {float(r5a):.9f} pad5->4 {float(r5b):.9f}", flush=True)

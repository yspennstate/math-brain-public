"""X008 (two spectral addresses, six variables, ONE_BIT_ENDPOINT sec. 3): rebuild the witness, confirm H = 5,
I = 17/8 and the influence vector, then test Lemma G-key (exact) and Theorem G on it."""
import json, math
import numpy as np
from rlib import Spec, walsh, superset_sum, popcounts

g = [1, -1, -1, 0, -1, 0, 0, 1, -1, -1, -1, 0, -1, 0, 0, 1]      # x in least-significant-bit order
h = {1: [3, 11], 2: [5, 13], 3: [6, 14]}                          # edges: low three bits 3, 5, 6; bit 3 free
# variable order (y1, y2, x0, x1, x2, x3): index bits 0,1 = y1,y2 ; bits 2..5 = x0..x3 ; bit value 1 means -1
F = np.zeros(64, dtype=np.int64)
for idx in range(64):
    y1 = 1 - 2 * (idx & 1); y2 = 1 - 2 * ((idx >> 1) & 1)
    x = idx >> 2
    v = g[x]
    if x in h[1]:
        v += y1
    if x in h[2]:
        v += y2
    if x in h[3]:
        v += y1 * y2
    F[idx] = v
assert set(np.unique(F)) <= {-1, 1}
sp = Spec.from_tables(F)
W = walsh(F); P = [int(w) * int(w) for w in W]; Pi = superset_sum(np.array(P, dtype=object)); pc = popcounts(6)
viol = sum(1 for S in range(1, 64) if P[S] * 64 * 64 > (4 ** (int(pc[S]) - 1)) * int(Pi[S]) ** 2)
eqs = sum(1 for S in range(1, 64) if P[S] > 0 and P[S] * 64 * 64 == (4 ** (int(pc[S]) - 1)) * int(Pi[S]) ** 2)
H = float(sp.H()[0]); I = float(sp.I()[0]); U = float(sp.U()[0]); Var = float(sp.Var()[0]); p0 = 1 - Var
rhs = 2 * (I - Var) + 2 * U - (p0 * math.log2(1 / p0) if p0 > 0 else 0.0)
out = dict(H=H, I=I, I_expected=17 / 8, infl=[float(v) for v in sp.infl()[0]], U=U, thmG_rhs=rhs, slack=rhs - H,
           gkey_violations=viol, gkey_equalities=eqs, support=int(sum(1 for v in P if v > 0)))
print(json.dumps(out, indent=1))
with open('x008_results.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, indent=1)

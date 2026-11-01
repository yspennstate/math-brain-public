# Search K/phi24 over scaled cell vertices with every permutation of b (the corner b1e found), floats then exact recheck.
import kfeat, itertools
from fractions import Fraction as F
rho = F(677, 1000)
V = [[-1,-1,-1,3],[-1,-1,1,1],[-1,F(1,3),F(1,3),F(1,3)]]
def parts(a, b, m):
    k0 = kfeat.K(a, b, m); g = kfeat.G[24]; kfeat.G[24] = g + 1; k1 = kfeat.K(a, b, m); kfeat.G[24] = g
    return k0, k1 - k0
best = None
ts = [F(k, 20) for k in range(1, 21)]
for i, j in itertools.product(range(3), range(3)):
    for pb in set(itertools.permutations(V[j])):
        for ta in ts:
            for tb in ts:
                a = [rho*ta*x for x in V[i]]; b = [rho*tb*x for x in pb]
                for m in (0, kfeat.MBIG):
                    k0, p = parts(a, b, m)
                    if p > 0 and (best is None or k0/p < best[0]): best = (k0/p, i, j, pb, ta, tb, m, k0, p)
r, i, j, pb, ta, tb, m, k0, p = best
print("min K/phi24 on scaled vertices:", float(r), "vertex a", i, "scale", ta, "vertex b", j, "perm", pb, "scale", tb, "m=", "M" if m else 0)
print("K true", float(k0), "K at shift -1/10", float(k0 + (F(-1,10) - kfeat.G24_SHIFT)*p), "-> K<0 for shift <", float(kfeat.G24_SHIFT - r))

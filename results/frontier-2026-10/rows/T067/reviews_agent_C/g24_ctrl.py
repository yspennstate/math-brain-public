# K is affine in g24: K(r) = K + (r - shift) * phi24, r = the replaced shift. Find where K first goes negative.
import random, kfeat
from fractions import Fraction as F
rho = F(677, 1000)
V = [[-1,-1,-1,3],[-1,-1,1,1],[-1,F(1,3),F(1,3),F(1,3)],[0,0,0,0]]
def pt(rng):
    w = [rng.random() for _ in range(4)]; t = sum(w); w = [F(x/t).limit_denominator(10**6) for x in w]
    v = [rho*sum(w[k]*V[k][i] for k in range(4)) for i in range(4)]; rng.shuffle(v); return v
def parts(a, b, m):
    k0 = kfeat.K(a, b, m); g = kfeat.G[24]; kfeat.G[24] = g + 1; k1 = kfeat.K(a, b, m); kfeat.G[24] = g
    return k0, k1 - k0
def at(a, b, m, r): k0, p = parts(a, b, m); return k0 + (r - kfeat.G24_SHIFT) * p
x = F(-2735, 10000); y = F(8204, 10000); a = [x, x, x, y]
for r in (F(-1, 10), F(-3, 10)): print('b1e point m=0, shift ->', r, float(at(a, a, 0, r)), '| original', float(kfeat.K(a, a, 0)))
rng = random.Random(67); worst = None
for _ in range(1500):
    a, b, m = pt(rng), pt(rng), rng.choice([0, kfeat.MBIG])
    k0, p = parts(a, b, m)
    if p > 0:
        r = k0 / p
        if worst is None or r < worst[0]: worst = (r, a, b, m)
print("min K/phi24 over 1500 random points (phi24>0):", float(worst[0]), "at m =", "M" if worst[3] else 0, "a =", [round(float(v),4) for v in worst[1]], "b =", [round(float(v),4) for v in worst[2]], "-> K<0 needs shift <", float(kfeat.G24_SHIFT - worst[0]))

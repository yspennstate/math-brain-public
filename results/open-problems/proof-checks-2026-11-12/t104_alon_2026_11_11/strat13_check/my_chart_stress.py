"""Stress the STRAT13 local theorem in the chart (an agent), Fractions only.
Sample h in the l1 ball of radius rho (1/384 edges, 1/648 triangle), mostly near the boundary and along
directions that keep the active weights near zero; keep h with every active weight >= 0; check
F(G(h)) >= ||h||_1/12, F computed from the projector onto range(B) (own code, as in my_collar_check).
Usage: python my_chart_stress.py N SEED
"""
import sys, random, json
from fractions import Fraction as F
from fractions import Fraction
from chart_helpers import invariant, inv2
from collar_algebra import BASES, local_data

N = int(sys.argv[1]); rng = random.Random(int(sys.argv[2]))
RHO = {'edges': F(1, 384), 'triangle': F(1, 648)}
out = {}
for kind, (U, W, X, Y) in BASES.items():
    nu, nw = sum(a * a for a in U), sum(a * a for a in W)
    def G_of(h):
        x, y, k, p, q, v, z = h
        B = [[U[i] + p * X[i] + q * Y[i], W[i] + v * X[i] + z * Y[i]] for i in range(5)]
        K = [[(1 + x) / nu, k / nu], [k / nu, (1 + y) / nw]]
        G = [[sum(B[i][a] * K[a][b] * B[j][b] for a in range(2) for b in range(2)) for j in range(5)] for i in range(5)]
        MM = [[sum(B[i][a] * B[i][b] for i in range(5)) for b in range(2)] for a in range(2)]
        Mi, _ = inv2(MM)
        P = [[sum(B[i][a] * Mi[a][b] * B[j][b] for a in range(2) for b in range(2)) for j in range(5)] for i in range(5)]
        return G, P
    G0, _ = G_of([F(0)] * 7)
    lam0 = (2 + sum(G0[i][i] for i in range(5))) / 4
    active = [(i, j) for i in range(5) for j in range(i + 1, 5) if lam0 / 5 + G0[i][j] == 0]
    Jm = [[F(c) for c in row] for row in local_data(kind)['left_inverse']]
    assert len(Jm) == 7 and len(Jm[0]) == len(active)
    kept = ok = 0; worst = None; tried = 0
    while kept < N and tried < 200 * N:
        tried += 1
        u = [F(rng.randint(0, 1000), 1000) * (rng.random() < .8) for _ in range(len(active))]
        d = [sum(Jm[i][j] * u[j] for j in range(len(active))) + F(rng.randint(-20, 20), 1000) * (rng.random() < .3) for i in range(7)]
        s = sum(abs(a) for a in d)
        if s == 0: continue
        r = RHO[kind] * F(rng.randint(1, 1000), 1000)
        h = [a * r / s for a in d]
        G, P = G_of(h)
        lam = (2 + sum(G[i][i] for i in range(5))) / 4
        if any(lam / 5 + G[i][j] < 0 for i, j in active): continue
        kept += 1
        Fv = invariant(G, P); h1 = sum(abs(a) for a in h)
        ok += Fv >= h1 / 12
        rat = Fv / h1
        if worst is None or rat < worst: worst = rat
    out[kind] = dict(active=len(active), tried=tried, kept=kept, ok=ok, worst_ratio=float(worst) if worst else None)
print(json.dumps(out))

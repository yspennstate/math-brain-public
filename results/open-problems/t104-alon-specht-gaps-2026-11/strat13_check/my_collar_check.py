"""Independent exact check of the STRAT13 collars (an agent).

At random rational points of every collar leaf, in Fractions only:
 1. build R = V V^T, D = 20t - tr R, gap G = 2R/D from the 6 coordinates (own code);
 2. own invariant F(G) from the projector P onto range(G) (formula of collar_algebra.chart, written
    out again in projector form);
 3. check STRAT12 target(p) == 20 D^2 Delta F(G) exactly, and 20 D^2 Delta > 0;
 4. own inverse map p -> chart h (frame + K), rebuild B K B^T and check it equals G permuted;
 5. check edges t+R_ij == (D/2) * (lam/5 + G_ij) with lam = (2+tr G)/4;
 6. at points where every STRAT10 constraint holds, check T6/(20 D^2 Delta) >= ||h||_1/12.
Usage: python my_collar_check.py COLLAR_COVER_JSON N_PER_LEAF SEED
"""
import sys, json, random
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'STRAT12')); sys.path.insert(0, str(HERE / 'STRAT12' / 'STRAT10'))
import exact_bernstein as eb
from zero_face import construct
from collar_boxes import point_bank
from collar_algebra import BASES

target, gs = eb.data()
rr, t_, V_, R_, M_, Delta_, Q_, n_, D_, edges_, P_, num_ = construct()
dic = lambda p: {m[:6]: F(int(c.numerator), int(c.denominator)) if hasattr(c, 'numerator') else F(c)
                 for m, c in p.items() if not any(m[6:])}
Dpoly, Deltapoly = dic(D_), dic(Delta_)

def ev(p, x):
    s = F(0)
    for m, c in p.items():
        term = F(c)
        for xi, e in zip(x, m):
            if e: term *= xi ** e
        s += term
    return s

def Vmat(x):
    t, v1, z1, v2, z2, z = x
    return [(v1, z1), (v2, z2), (1 - t - v1 - v2, -z - z1 - z2), (t, F(0)), (F(-1), z)]

def inv2(a):
    d = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return [[a[1][1] / d, -a[0][1] / d], [-a[1][0] / d, a[0][0] / d]], d

def invariant(G, P):
    n = 5
    tau = sum(G[i][i] for i in range(n))
    M = sum(P[i][i] * G[i][i] for i in range(n))
    diag2 = sum(G[i][i] ** 2 for i in range(n))
    tr2 = sum(G[i][j] ** 2 for i in range(n) for j in range(n))
    QS = sum(P[i][i] * sum(G[i][j] ** 2 for j in range(n)) for i in range(n))
    Rr = sum(P[i][j] * G[i][j] ** 2 for i in range(n) for j in range(n))
    Rr += 2 * sum(P[i][i] * G[i][j] * G[j][j] for i in range(n) for j in range(n))
    return F(9, 80) + (11 * M - 2 * tau) / 8 + (100 * tau * M - 320 * diag2 - 1280 * QS
                                               + 448 * tr2 - 33 * tau * tau) / 320 + Rr

def leaves(t):
    if t['kind'] == 'split':
        for c in t['children']: yield from leaves(c)
    else:
        yield t

cover = json.load(open(sys.argv[1])); N = int(sys.argv[2]); rng = random.Random(int(sys.argv[3]))
bank = point_bank()
names = [k for k in gs if k not in ('scale_guard', 'scale14')]
stats = dict(points=0, identity_ok=0, map_ok=0, edges_ok=0, feasible=0, bound_ok=0, minratio=None)
fails = []
for rec in cover['records']:
    node = rec['node']; kind = bank[node]['kind']; perm = bank[node]['permutation']
    U, W, X, Y = BASES[kind]; nu, nw, nx, ny = [sum(a * a for a in b) for b in (U, W, X, Y)]
    for lf in leaves(rec['tree']):
        if lf['kind'] != 'collar': continue
        box = [tuple(map(F, iv)) for iv in lf['box']]
        for s in range(N):
            if s == 0:
                x = [(a + b) / 2 for a, b in box]
            else:
                x = [a + (b - a) * F(rng.randint(0, 10 ** 6), 10 ** 6) for a, b in box]
            stats['points'] += 1
            V = Vmat(x)
            R = [[V[i][0] * V[j][0] + V[i][1] * V[j][1] for j in range(5)] for i in range(5)]
            D = 20 * x[0] - sum(R[i][i] for i in range(5))
            G = [[2 * R[i][j] / D for j in range(5)] for i in range(5)]
            MM = [[sum(V[i][a] * V[i][b] for i in range(5)) for b in range(2)] for a in range(2)]
            Mi, Dl = inv2(MM)
            P = [[sum(V[i][a] * Mi[a][b] * V[j][b] for a in range(2) for b in range(2)) for j in range(5)] for i in range(5)]
            Fv = invariant(G, P)
            fac = 20 * D * D * ev(Deltapoly, x)
            assert ev(Dpoly, x) == D and ev(Deltapoly, x) == Dl
            tv = ev(target, x)
            ok1 = fac > 0 and tv == fac * Fv
            stats['identity_ok'] += ok1
            # inverse map to chart coordinates
            VV = [V[j] for j in perm]
            C = [[sum(b[i] * VV[i][j] for i in range(5)) / F(nb) for j in range(2)] for b, nb in ((U, nu), (W, nw))]
            E = [[sum(b[i] * VV[i][j] for i in range(5)) / F(nb) for j in range(2)] for b, nb in ((X, nx), (Y, ny))]
            Ci, _ = inv2(C)
            H = [[sum(E[i][j] * Ci[j][k] for j in range(2)) for k in range(2)] for i in range(2)]
            K = [[2 * sum(C[i][j] * C[k][j] for j in range(2)) / D for k in range(2)] for i in range(2)]
            p, v, q, z = H[0][0], H[0][1], H[1][0], H[1][1]
            B = [[U[i] + p * X[i] + q * Y[i], W[i] + v * X[i] + z * Y[i]] for i in range(5)]
            Gc = [[sum(B[i][a] * K[a][b] * B[j][b] for a in range(2) for b in range(2)) for j in range(5)] for i in range(5)]
            ok2 = all(Gc[i][j] == G[perm[i]][perm[j]] for i in range(5) for j in range(5))
            stats['map_ok'] += ok2
            h = [nu * K[0][0] - 1, nw * K[1][1] - 1, nu * K[0][1], p, q, v, z]
            h1 = sum(abs(a) for a in h)
            lam = (2 + sum(G[i][i] for i in range(5))) / 4
            ok3 = all(x[0] + R[i][j] == D / 2 * (lam / 5 + G[i][j]) for i in range(5) for j in range(i + 1, 5))
            stats['edges_ok'] += ok3
            if all(ev(gs[nm], x) >= 0 for nm in names):
                stats['feasible'] += 1
                r = Fv / h1 if h1 else None
                ok4 = h1 > 0 and Fv >= h1 / 12
                stats['bound_ok'] += ok4
                if r is not None and (stats['minratio'] is None or r < stats['minratio']): stats['minratio'] = r
                if not ok4: fails.append((node, 'bound', float(Fv), float(h1)))
            if not (ok1 and ok2 and ok3): fails.append((node, ok1, ok2, ok3))
stats['minratio'] = None if stats['minratio'] is None else float(stats['minratio'])
print(json.dumps(stats))
print('FAILS', len(fails), fails[:5])

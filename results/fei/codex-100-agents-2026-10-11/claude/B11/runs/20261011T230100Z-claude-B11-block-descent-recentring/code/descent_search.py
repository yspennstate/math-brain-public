"""B11 (Claude): local search for large block-descent constant, n=5,6 (EVIDENCE ONLY, float64).
Frozen spec (written before running): objective phi(f) = min over nonempty proper blocks A with
I_A > 1e-12 of L_A / I_A (and, separately, ratio H/I); f:{0,1}^n -> {+1,-1} nonconstant; move =
one truth-table flip, steepest ascent over all 2^n neighbours, stop at a local maximum or 400 steps;
seeds: point defect, random sets of 2..8 points, random tables of density 1/16..1/2, Hamming balls,
tribes/AND-OR, majority; wall budget per (n, objective) given on the command line (default 70 s);
memory < 100 MB; seeds from numpy default_rng(20261011 + n). Also prints phi of point defects n=2..14
from the closed form (restriction of a point defect is a point defect with prob 2^-k, else constant).
"""
import numpy as np, json, sys, time, math
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from descent_scan import hadamard, popc, ent, block_index

def prep(n):
    blocks = []
    for A in range(1, (1 << n) - 1):
        Ab, Cb, idx = block_index(n, A); m = n - len(Ab)
        blocks.append((Ab, idx, hadamard(m), popc(m)))
    return dict(n=n, Hn=hadamard(n), sz=popc(n), blocks=blocks,
                inmask=[np.array([S for S in range(1 << n) if S >> i & 1]) for i in range(n)])

def evaluate(F, P):
    n = P['n']; hat = F @ P['Hn'] / (1 << n); W = hat * hat
    H = ent(W); I = W @ P['sz']
    inf = np.stack([W[:, P['inmask'][i]].sum(1) for i in range(n)], 1)
    phi = np.full(F.shape[0], np.inf)
    for Ab, idx, Hm, szm in P['blocks']:
        m = Hm.shape[0]
        Wa = (F[:, idx] @ Hm / m) ** 2
        L = H - ent(Wa).mean(1); IA = inf[:, Ab].sum(1)
        ok = IA > 1e-12
        phi = np.minimum(phi, np.where(ok, L / np.where(ok, IA, 1), np.inf))
    nc = I > 1e-12
    ratio = np.where(nc, H / np.where(nc, I, 1), -np.inf)
    phi = np.where(nc & np.isfinite(phi), phi, -np.inf)
    return phi, ratio, H, I

def seeds(n, rng):
    N = 1 << n; out = []
    pd = np.ones(N); pd[0] = -1; out.append(('point_defect', pd))
    w = np.array([bin(x).count('1') for x in range(N)])
    for r in range(1, n):
        f = np.where(w <= r - 1, -1.0, 1.0); out.append((f'ball_{r-1}', f))
    maj = np.where(2 * w > n, -1.0, 1.0); out.append(('majority', maj))
    for s in range(2, n):
        # tribes-like: OR of ANDs of width s on disjoint blocks
        f = np.ones(N)
        for x in range(N):
            v = False
            for b0 in range(0, n - s + 1, s):
                if all(x >> (b0 + j) & 1 for j in range(s)): v = True
            f[x] = -1.0 if v else 1.0
        out.append((f'tribes_{s}', f))
    for k in range(2, 9):
        for rep in range(6):
            f = np.ones(N); f[rng.choice(N, k, replace=False)] = -1.0; out.append((f'set{k}', f))
    for p in (1/16, 1/8, 1/4, 1/2):
        for rep in range(8):
            out.append((f'rand{p:g}', np.where(rng.random(N) < p, -1.0, 1.0)))
    return out

def climb(f, P, obj, max_steps=400):
    N = f.shape[0]; cur = f.copy()
    v = evaluate(cur[None, :], P)[0 if obj == 'phi' else 1][0]
    for step in range(max_steps):
        nb = np.repeat(cur[None, :], N, 0); nb[np.arange(N), np.arange(N)] *= -1
        vals = evaluate(nb, P)[0 if obj == 'phi' else 1]
        j = int(np.argmax(vals))
        if vals[j] <= v + 1e-12: break
        cur = nb[j]; v = vals[j]
    return cur, v

def pd_H(m):
    if m <= 0: return 0.0
    e = 2.0 ** (1 - m); c = (1 - e) ** 2
    t0 = -c * math.log2(c) if c > 0 else 0.0
    return t0 + (2 ** m - 1) * 4.0 ** (1 - m) * 2 * (m - 1)

if __name__ == '__main__':
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 70.0
    res = {'point_defect_phi': {}}
    for n in range(2, 15):
        Hn = pd_H(n); In = n * 2.0 ** (1 - n)
        vals = [(Hn - 2.0 ** (-k) * pd_H(n - k)) / (k * 2.0 ** (1 - n)) for k in range(1, n)]
        res['point_defect_phi'][n] = dict(phi=min(vals), argk=1 + int(np.argmin(vals)), ratio=Hn / In)
    print('pd', json.dumps(res['point_defect_phi']), flush=True)
    for n in (5, 6):
        P = prep(n); rng = np.random.default_rng(20261011 + n)
        for obj in ('phi', 'ratio'):
            t0 = time.time(); best = (-np.inf, None, None); tried = 0
            S = seeds(n, rng)
            while time.time() - t0 < budget:
                name, f = S[tried % len(S)] if tried < len(S) else ('rand_restart', np.where(rng.random(1 << n) < rng.choice([1/16, 1/8, 1/4, 1/2]), -1.0, 1.0))
                tried += 1
                g, v = climb(f, P, obj)
                if v > best[0]: best = (v, g, name)
            phi, ratio, H, I = evaluate(best[1][None, :], P)
            key = f'n{n}_{obj}'
            res[key] = dict(best=float(best[0]), seed=best[2], climbs=tried, phi=float(phi[0]), ratio=float(ratio[0]),
                            H=float(H[0]), I=float(I[0]), minus_points=[int(x) for x in np.where(best[1] < 0)[0]],
                            seconds=round(time.time() - t0, 1))
            print(key, json.dumps(res[key]), flush=True)
    json.dump(res, open(sys.argv[1], 'w'), indent=1)

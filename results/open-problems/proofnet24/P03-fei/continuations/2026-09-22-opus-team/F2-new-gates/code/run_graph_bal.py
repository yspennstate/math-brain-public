"""Exact-balance annealing over Aut(H)-invariant partial cores (plain group, no duality).
Every move changes one or two orbits so that sum c0 stays 0.
usage: python run_graph_bal.py H restarts iters T0 T1
"""
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import sys, time
import numpy as np
import graphs
from orbsa2 import Model2, phi_sum, add_row
from holecore import summarize2 as summarize

name = sys.argv[1]; restarts = int(sys.argv[2]); iters = int(sys.argv[3])
T0 = float(sys.argv[4]); T1 = float(sys.argv[5])
bip = {'k33': (3, 3), 'k34': (3, 4), 'k44': (4, 4), 'k35': (3, 5), 'k25': (2, 5)}
a, b = bip[name]
m, perms, E = graphs.kab(a, b)
t = time.time()
M = Model2(m, perms)
N = M.N
print(f"{name}: m={m} orbits={M.no} build {time.time()-t:.1f}s", flush=True)
prop = np.array([-1 if graphs.has_pm_bip(x, E, a, b) else 1 for x in range(N)], dtype=np.int64)
vprop = np.zeros(M.no, dtype=np.int64)
vprop[M.rep] = prop
size = M.size
by_size = {}
for o in range(M.no):
    by_size.setdefault(int(size[o]), []).append(o)


def balance_greedy(v, rng):
    v = v.copy()
    bal = int((size * v).sum())
    tries = 0
    while bal != 0 and tries < 100000:
        tries += 1
        sgn = 1 if bal > 0 else -1  # too many +1 cells: move some +1 orbit down
        cands = [o for o in range(M.no) if v[o] == sgn and size[o] <= abs(bal)]
        if not cands:
            cands = [o for o in range(M.no) if v[o] == sgn]
        o = cands[rng.integers(len(cands))]
        # hole (change by size) or flip (2*size)
        if 2 * size[o] <= abs(bal) and rng.random() < 0.3:
            v[o] = -sgn
        else:
            v[o] = 0
        bal = int((size * v).sum())
    return v


def state(v):
    W = v @ M.B
    Ev = M.E @ v
    Dvv = int((M.D * v * v).sum()); vEv = int(v @ Ev)
    Ha, I2a, _, _ = M.aux(v)
    return W, Ev, Dvv, vEv, Ha, I2a


def ratio(Hc, Dvv, vEv, Ha, I2a):
    I = (Dvv - vEv + I2a) / (2.0 * N)
    return (Hc + Ha) / (I - 1.0) if I > 1 + 1e-12 else -1e9


def anneal(v, iters, T0, T1, rng):
    W, Ev, Dvv, vEv, Ha, I2a = state(v)
    Hc = phi_sum(W, M.phi)
    R = ratio(Hc, Dvv, vEv, Ha, I2a)
    best, bestR = v.copy(), R
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        o1 = rng.integers(M.no)
        nv1 = (-1, 0, 1)[rng.integers(3)]
        if nv1 == v[o1]:
            continue
        d1 = int(size[o1]) * (nv1 - v[o1])
        # compensating orbit
        opts = []
        for s2, dv2 in ((abs(d1), -np.sign(d1)), (abs(d1) // 2 if abs(d1) % 2 == 0 else -1, -2 * np.sign(d1))):
            if s2 <= 0:
                continue
            for o2 in by_size.get(s2, []):
                if o2 == o1:
                    continue
                nv2 = v[o2] + dv2
                if -1 <= nv2 <= 1:
                    opts.append((o2, int(nv2)))
        if not opts:
            continue
        o2, nv2 = opts[rng.integers(len(opts))]
        moves = [(o1, nv1), (o2, nv2)]
        old = {o: v[o] for o, _ in moves}
        Dvv_n, vEv_n = Dvv, vEv
        Ev_n = Ev.copy()
        for o, nvv in moves:
            dv = nvv - v[o]
            Dvv_n += M.D[o] * (nvv * nvv - v[o] * v[o])
            vEv_n += 2 * dv * Ev_n[o] + M.E[o, o] * dv * dv
            Ev_n += M.E[:, o] * dv
            add_row(W, M.B, o, dv)
            v[o] = nvv
        Hc_n = phi_sum(W, M.phi)
        if any(old[o] == 0 or nvv == 0 for o, nvv in moves):
            Ha_n, I2a_n, _, _ = M.aux(v)
        else:
            Ha_n, I2a_n = Ha, I2a
        R_n = ratio(Hc_n, Dvv_n, vEv_n, Ha_n, I2a_n)
        if R_n >= R or rng.random() < np.exp((R_n - R) / T):
            Dvv, vEv, Ev, Hc, Ha, I2a, R = Dvv_n, vEv_n, Ev_n, Hc_n, Ha_n, I2a_n, R_n
            if R > bestR:
                bestR, best = R, v.copy()
        else:
            for o, nvv in moves:
                add_row(W, M.B, o, old[o] - nvv)
                v[o] = old[o]
    return best, bestR


rng = np.random.default_rng(3)
bestall = (-1e9, None)
for r in range(restarts):
    if r % 2 == 0:
        v0 = balance_greedy(vprop, rng)
        kind = 'pm'
    else:
        v0 = balance_greedy(rng.choice([-1, 1], size=M.no).astype(np.int64), rng)
        kind = 'rand'
    t = time.time()
    b1, R1 = anneal(v0.copy(), iters, T0, T1, rng)
    b1, R1 = anneal(b1.copy(), iters // 4, 1e-9, 1e-10, rng)
    c = M.c0(b1)
    s = summarize(c, m)
    assert int(c.sum()) == 0
    print(f"  restart {r} ({kind}): R = {R1:.12f} (check {s['R']:.12f}) holes={s['holes']} ngroups={s['ngroups']} "
          f"nvars={s['nvars']} I={s['I']:.5f} t={time.time()-t:.0f}s", flush=True)
    if R1 > bestall[0]:
        bestall = (R1, b1.copy())
np.save(f"../logs/graphbal_best_{name}.npy", M.c0(bestall[1]).astype(np.int8))
print("BEST", name, bestall[0])

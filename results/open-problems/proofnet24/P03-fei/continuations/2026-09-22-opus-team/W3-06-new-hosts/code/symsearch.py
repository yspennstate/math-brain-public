"""Search over cores invariant under a coordinate group G and anti-invariant under A = complement o pi
(c0(A x) = -c0(x)), holes filled by coins with the optimal grouping (maximum matching; see hc.py).
Exhaustive when the number of orbit pairs is <= EXH_MAX, orbit-level simulated annealing otherwise."""
import numpy as np
import numba as nb
import time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hc import phi_table, hole_matching, evaluate
from orbenum import perm_cells, cell_orbits, orbit_data, enum_all

EXH_MAX = 18


@nb.njit(cache=True)
def matching_table_nb(orb, pair_a, pair_b, forced_mask_cells, m, npairs):
    N = 1 << m
    T = np.zeros(1 << npairs, dtype=np.int64)
    Hh = np.zeros(1 << npairs, dtype=np.int64)
    c = np.ones(N, dtype=np.int64)
    for mask in range(1 << npairs):
        for x in range(N):
            o = orb[x]
            z = forced_mask_cells[x]
            if not z:
                for j in range(npairs):
                    if (mask >> j) & 1:
                        if o == pair_a[j] or o == pair_b[j]:
                            z = True
                            break
            c[x] = 0 if z else 1
        M, mate = hole_matching(c, m)
        T[mask] = M
        h = 0
        for x in range(N):
            if c[x] == 0:
                h += 1
        Hh[mask] = h
    return T, Hh


def setup(G, m, pi):
    N = 1 << m
    orb, reps, maps = cell_orbits(G, m)
    no = len(reps)
    sizes, K, E = orbit_data(orb, reps, m)
    A = (N - 1) ^ perm_cells(pi, m)
    Aorb = np.array([orb[A[reps[o]]] for o in range(no)])
    for o in range(no):
        cells = np.where(orb == o)[0]
        if not np.all(orb[A[cells]] == Aorb[o]):
            return None
    if not np.all(Aorb[Aorb] == np.arange(no)):
        return None
    forced = [o for o in range(no) if Aorb[o] == o]
    pairs = [(o, int(Aorb[o])) for o in range(no) if Aorb[o] != o and o < Aorb[o]]
    npairs = len(pairs)
    Kd = np.zeros((no, npairs), dtype=np.int64)
    P = np.zeros((no, npairs), dtype=np.int64)
    for j, (a, b) in enumerate(pairs):
        Kd[:, j] = K[:, a] - K[:, b]
        P[a, j] = 1; P[b, j] = -1
    L = -E.astype(np.int64).copy()
    np.fill_diagonal(L, 0)
    L[np.diag_indices(no)] = -L.sum(axis=1)
    Q = P.T @ L @ P
    return dict(m=m, N=N, orb=orb, no=no, sizes=sizes, pairs=pairs, npairs=npairs, forced=forced, Kd=Kd, P=P, Q=Q,
                forced_cells=int(sizes[forced].sum()) if forced else 0)


@nb.njit(cache=True)
def eval_pairs(v, Kd, Q, sizes, m, phi, orb, pair_a, pair_b, forced_cells_mask):
    N = 1 << m
    ns = Kd.shape[0]
    npairs = v.shape[0]
    Hc = 0.0
    for s in range(ns):
        w = 0
        for j in range(npairs):
            w += v[j] * Kd[s, j]
        if w < 0:
            w = -w
        Hc += sizes[s] * phi[w]
    D = 0
    for j in range(npairs):
        for k in range(npairs):
            D += v[j] * Q[j, k] * v[k]
    c = np.ones(N, dtype=np.int64)
    for x in range(N):
        z = forced_cells_mask[x]
        if not z:
            o = orb[x]
            for j in range(npairs):
                if v[j] == 0 and (o == pair_a[j] or o == pair_b[j]):
                    z = True
                    break
        c[x] = 0 if z else 1
    M, mate = hole_matching(c, m)
    h = 0
    for x in range(N):
        if c[x] == 0:
            h += 1
    H = Hc + (2.0 * m * h - 4.0 * M) / N
    I = (D + (m + 2) * h - 2 * M) / (2.0 * N)
    if I <= 1.0 + 1e-12:
        return -1e9, H, I
    return H / (I - 1.0), H, I


@nb.njit(cache=True)
def anneal_pairs(v0, Kd, Q, sizes, m, phi, orb, pair_a, pair_b, fmask, iters, T0, T1, seed):
    np.random.seed(seed)
    v = v0.copy()
    npairs = v.shape[0]
    R, H, I = eval_pairs(v, Kd, Q, sizes, m, phi, orb, pair_a, pair_b, fmask)
    best = v.copy(); bestR = R
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        j = np.random.randint(npairs)
        old = v[j]
        r = np.random.randint(2)
        new = old
        if old == -1:
            new = 0 if r == 0 else 1
        elif old == 0:
            new = -1 if r == 0 else 1
        else:
            new = -1 if r == 0 else 0
        v[j] = new
        Rn, Hn, In = eval_pairs(v, Kd, Q, sizes, m, phi, orb, pair_a, pair_b, fmask)
        if Rn >= R or np.random.random() < np.exp((Rn - R) / T):
            R = Rn
            if R > bestR:
                bestR = R; best[:] = v
        else:
            v[j] = old
    return best, bestR


def run(name, G, m, pi, topk=10, log=None, anneal_iters=20000, restarts=8):
    t0 = time.time()
    st = setup(G, m, pi)
    if st is None:
        return None
    N = st['N']
    phi = phi_table(N)
    npairs = st['npairs']
    pa = np.array([a for a, b in st['pairs']], dtype=np.int64)
    pb = np.array([b for a, b in st['pairs']], dtype=np.int64)
    fmask = np.isin(st['orb'], st['forced'])
    head = f"{name}: m={m} |G|={len(G)} pi={pi} orbits={st['no']} pairs={npairs} forced holes={st['forced_cells']}"
    results = []
    if npairs <= EXH_MAX:
        Mtab, htab = matching_table_nb(st['orb'], pa, pb, fmask, m, npairs)
        Rs, Vs = enum_all(st['Kd'], st['Q'], st['sizes'], npairs, m, phi, Mtab, htab, topk)
        for r, v in zip(Rs, Vs):
            if r > -1e8:
                results.append((float(r), v.copy()))
        mode = 'exhaustive'
    else:
        rng = np.random.default_rng(12345)
        cell_pair = np.zeros(st['N'], dtype=np.int64)
        for j, (a, b) in enumerate(st['pairs']):
            cell_pair[st['orb'] == a] = j; cell_pair[st['orb'] == b] = j
        cell_forced = fmask.copy()
        assert npairs <= 62
        for rs in range(restarts):
            v0 = rng.integers(-1, 2, size=npairs).astype(np.int64)
            best, bestR = anneal2(v0, st['Kd'], st['Q'], st['sizes'], m, phi, cell_pair, cell_forced,
                                  anneal_iters, 0.08, 0.0003, rs + 1)
            results.append((float(bestR), best.copy()))
        results.sort(key=lambda t: -t[0])
        mode = f'anneal {restarts}x{anneal_iters}'
    out = []
    for r, v in results[:topk]:
        u = st['P'] @ v
        c0 = u[st['orb']]
        ev = evaluate(c0, m, phi)
        out.append((r, v.tolist(), ev))
    best = out[0][0] if out else float('nan')
    msg = head + f" [{mode}] best R = {best:.10f} ({time.time()-t0:.1f}s)"
    print(msg, flush=True)
    if log:
        log.write(msg + "\n")
        for r, v, ev in out[:3]:
            log.write(f"    {r:.10f} v={v} holes={ev['holes']} pairs={ev['pairs']} singles={ev['singles']} "
                      f"nvars={ev['nvars']} I={ev['I']:.6f} H={ev['H']:.6f}\n")
        log.flush()
    return out, st


@nb.njit(cache=True)
def _state_eval(W, sizes, phi, m, D, h, M):
    N = 1 << m
    Hc = 0.0
    for s in range(W.shape[0]):
        w = W[s]
        if w < 0:
            w = -w
        Hc += sizes[s] * phi[w]
    H = Hc + (2.0 * m * h - 4.0 * M) / N
    I = (D + (m + 2) * h - 2 * M) / (2.0 * N)
    if I <= 1.0 + 1e-12:
        return -1e9
    return H / (I - 1.0)


@nb.njit(cache=True)
def _holes_M(v, cell_pair, cell_forced, m):
    N = 1 << m
    c = np.ones(N, dtype=np.int64)
    h = 0
    for x in range(N):
        j = cell_pair[x]
        if cell_forced[x] or v[j] == 0:
            c[x] = 0
            h += 1
    M, mate = hole_matching(c, m)
    return h, M


@nb.njit(cache=True)
def anneal2(v0, Kd, Q, sizes, m, phi, cell_pair, cell_forced, iters, T0, T1, seed):
    np.random.seed(seed)
    v = v0.copy()
    npairs = v.shape[0]
    ns = Kd.shape[0]
    W = np.zeros(ns, dtype=np.int64)
    for s in range(ns):
        for j in range(npairs):
            W[s] += v[j] * Kd[s, j]
    Qv = np.zeros(npairs, dtype=np.int64)
    for j in range(npairs):
        for k in range(npairs):
            Qv[j] += Q[j, k] * v[k]
    D = 0
    for j in range(npairs):
        D += v[j] * Qv[j]
    cache = dict()
    mask = 0
    for j in range(npairs):
        if v[j] == 0:
            mask |= (1 << j)
    h, M = _holes_M(v, cell_pair, cell_forced, m)
    cache[mask] = (h, M)
    R = _state_eval(W, sizes, phi, m, D, h, M)
    best = v.copy(); bestR = R
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        j = np.random.randint(npairs)
        old = v[j]
        r = np.random.randint(2)
        if old == -1:
            new = 0 if r == 0 else 1
        elif old == 0:
            new = -1 if r == 0 else 1
        else:
            new = -1 if r == 0 else 0
        dv = new - old
        for s in range(ns):
            W[s] += dv * Kd[s, j]
        Dn = D + 2 * dv * Qv[j] + dv * dv * Q[j, j]
        v[j] = new
        nmask = mask
        if new == 0:
            nmask |= (1 << j)
        else:
            nmask &= ~(1 << j)
        if nmask in cache:
            hn, Mn = cache[nmask]
        else:
            hn, Mn = _holes_M(v, cell_pair, cell_forced, m)
            cache[nmask] = (hn, Mn)
        Rn = _state_eval(W, sizes, phi, m, Dn, hn, Mn)
        if Rn >= R or np.random.random() < np.exp((Rn - R) / T):
            R = Rn; D = Dn; mask = nmask
            for k in range(npairs):
                Qv[k] += Q[k, j] * dv
            if R > bestR:
                bestR = R; best[:] = v
        else:
            v[j] = old
            for s in range(ns):
                W[s] -= dv * Kd[s, j]
    return best, bestR

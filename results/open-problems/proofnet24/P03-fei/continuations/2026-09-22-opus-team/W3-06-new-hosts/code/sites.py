"""Coin completion of a monotone (or any) Boolean host f on m variables.

If Pr[f true] < 1/2 the deficit d = N - 2t is filled by turning d false cells into holes; holes are grouped by a
maximum matching (hc.py).  A false-false site {a, b} (cube edge) costs  dI = 2(m - T)/N  (T = true neighbours of a
and b other than each other; F2 Section 1), so sites are chosen greedily by T, then improved by local search
(swap one site for another) under the exact objective.  If Pr > 1/2 the dual is used.

Mixed sites (one true cell, one false cell, an edge of the boundary) keep the balance; their cost is
    dI = 2(m - 1 - OPP)/N,   OPP = (s(a) - 1) + (s(b) - 1),  s = sensitivity (number of disagreeing neighbours),
so a mixed site is free when s(a) + s(b) = m + 1 and pays for itself when s(a) + s(b) > m + 1.
"""
import numpy as np
import numba as nb
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hc import fwht, phi_table, evaluate, dirichlet, hole_matching


@nb.njit(cache=True)
def site_costs(val, m):
    """for every cube edge {x, x^e_i} with x < y and both FALSE (+1): T = number of TRUE (-1) neighbours of x and y
    other than each other.  Returns arrays (x, i, T)."""
    N = val.shape[0]
    cnt = 0
    for x in range(N):
        if val[x] != 1:
            continue
        for i in range(m):
            y = x ^ (1 << i)
            if y > x and val[y] == 1:
                cnt += 1
    xs = np.empty(cnt, dtype=np.int64); isx = np.empty(cnt, dtype=np.int64); Ts = np.empty(cnt, dtype=np.int64)
    k = 0
    for x in range(N):
        if val[x] != 1:
            continue
        for i in range(m):
            y = x ^ (1 << i)
            if y > x and val[y] == 1:
                T = 0
                for j in range(m):
                    if j != i:
                        if val[x ^ (1 << j)] == -1:
                            T += 1
                        if val[y ^ (1 << j)] == -1:
                            T += 1
                xs[k] = x; isx[k] = i; Ts[k] = T
                k += 1
    return xs, isx, Ts


def complete(truth, m, local_iters=2000, seed=0, verbose=False):
    """truth: bool array (True = TRUE).  Returns (best evaluation dict, c0)."""
    N = 1 << m
    t = int(truth.sum())
    flip = False
    if 2 * t > N:
        truth = ~truth[::-1].copy()   # dual: f*(x) = not f(not x), same H and I
        t = int(truth.sum()); flip = True
    d = N - 2 * t
    val = np.where(truth, -1, 1).astype(np.int64)
    if d == 0:
        ev = evaluate(val, m)
        return ev, val
    xs, isx, Ts = site_costs(val, m)
    order = np.argsort(-Ts, kind='stable')
    used = np.zeros(N, dtype=bool)
    c0 = val.copy()
    npairs = d // 2
    chosen = []
    for k in order:
        if len(chosen) >= npairs:
            break
        x = xs[k]; y = x ^ (1 << isx[k])
        if used[x] or used[y]:
            continue
        used[x] = used[y] = True
        chosen.append((int(x), int(y)))
        c0[x] = 0; c0[y] = 0
    if d % 2 == 1:
        # one singleton hole: the false cell with most true neighbours
        best = None
        for x in range(N):
            if c0[x] == 1:
                s = sum(1 for i in range(m) if c0[x ^ (1 << i)] == -1)
                if best is None or s > best[0]:
                    best = (s, x)
        c0[best[1]] = 0
    if len(chosen) < npairs:
        # not enough disjoint false edges; fill with singles
        rest = npairs - len(chosen)
        cand = [x for x in range(N) if c0[x] == 1]
        for x in cand[:2 * rest]:
            c0[x] = 0
    phi = phi_table(N)
    ev = evaluate(c0, m, phi)
    R = ev['R']
    # local search: move one site to another candidate edge
    rng = np.random.default_rng(seed)
    cand_edges = [(int(xs[k]), int(xs[k] ^ (1 << isx[k]))) for k in order[:min(len(order), 20 * npairs + 200)]]
    for it in range(local_iters):
        if not chosen:
            break
        j = rng.integers(len(chosen))
        a, b = chosen[j]
        e = cand_edges[rng.integers(len(cand_edges))]
        if c0[e[0]] != 1 or c0[e[1]] != 1:
            continue
        c0[a] = 1; c0[b] = 1; c0[e[0]] = 0; c0[e[1]] = 0
        ev2 = evaluate(c0, m, phi)
        if ev2['R'] > R + 1e-12:
            R = ev2['R']; ev = ev2; chosen[j] = e
        else:
            c0[a] = 0; c0[b] = 0; c0[e[0]] = 1; c0[e[1]] = 1
    ev['dual_used'] = flip
    ev['Tmax'] = int(Ts.max()) if len(Ts) else -1
    ev['sites_T_hist'] = np.bincount(Ts[order[:npairs]] if len(Ts) else [0]).tolist()
    return ev, c0


if __name__ == '__main__':
    # sanity: PM(K33) must give Numaro's value
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from pm_hosts import pm_general, upset_table
    E33 = [(r, 3 + c) for r in range(3) for c in range(3)]
    _, pm33 = pm_general(6, E33)
    ev, c0 = complete(upset_table(9, pm33), 9, local_iters=200)
    print('PM(K33) completion:', ev)

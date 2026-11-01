"""Exhaustive search over cores invariant under a coordinate group G, anti-invariant under an anti-map A
(c0(A x) = -c0(x)), with the optimal coin grouping (maximum matching of the holes, see hc.py).

cells x in {0,1}^m; G = list of coordinate permutations (perm[i] = image of coordinate i); A = cell permutation
x -> complement(pi x) for a coordinate permutation pi normalising G (or pi = identity).
Orbits O of G on cells.  A maps orbits to orbits; orbits with A(O) = O are forced holes; the others come in pairs
(O, A(O)) with values (v, -v), v in {-1, 0, 1}.  Balance holds automatically.
Orbit-level quantities (exact integers):
    K[s, o] = sum_{x in O_o} chi_{S_s}(x) for a representative S_s of every orbit (Walsh transform is G-covariant)
    E[o, o'] = number of cube edges between O_o and O_o'
"""
import numpy as np
import numba as nb
import itertools, time, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hc import fwht, phi_table, hole_matching, evaluate, popc


def perm_cells(perm, m):
    """cell map x -> pi(x) for coordinate perm (bit i of x moves to bit perm[i])."""
    N = 1 << m
    out = np.zeros(N, dtype=np.int64)
    for i in range(m):
        out |= ((np.arange(N) >> i) & 1) << perm[i]
    return out


def close_group(gens, m):
    """generate the full permutation group from generators (tuples)."""
    idp = tuple(range(m))
    G = {idp}
    frontier = [idp]
    while frontier:
        nf = []
        for g in frontier:
            for h in gens:
                k = tuple(h[g[i]] for i in range(m))
                if k not in G:
                    G.add(k); nf.append(k)
        frontier = nf
    return sorted(G)


def cell_orbits(G, m):
    N = 1 << m
    maps = np.array([perm_cells(g, m) for g in G])
    orb = -np.ones(N, dtype=np.int64)
    reps = []
    no = 0
    for x in range(N):
        if orb[x] < 0:
            ims = np.unique(maps[:, x])
            orb[ims] = no
            reps.append(x)
            no += 1
    return orb, np.array(reps), maps


def orbit_data(orb, reps, m):
    N = 1 << m
    no = len(reps)
    sizes = np.bincount(orb, minlength=no)
    # K[s, o] = sum_{x in O_o} (-1)^{|S_s & x|}
    x = np.arange(N)
    K = np.zeros((no, no), dtype=np.int64)
    for s, S in enumerate(reps):
        chi = 1 - 2 * (np.array([bin(int(v)).count('1') for v in (x & S)]) & 1)
        K[s] = np.bincount(orb, weights=chi, minlength=no).astype(np.int64)
    E = np.zeros((no, no), dtype=np.int64)
    for i in range(m):
        y = x ^ (1 << i)
        sel = y > x
        np.add.at(E, (orb[x[sel]], orb[y[sel]]), 1)
    E = E + E.T - np.diag(np.diag(E))  # symmetric; diagonal = internal edges counted once
    return sizes, K, E


def matching_table(orb, pair_orbits, forced, m, npairs):
    """M[mask] = maximum matching of holes = forced orbits + orbits of pairs j with bit j of mask set."""
    N = 1 << m
    T = np.zeros(1 << npairs, dtype=np.int64)
    H = np.zeros(1 << npairs, dtype=np.int64)
    base = np.isin(orb, forced)
    memb = [np.isin(orb, pair_orbits[j]) for j in range(npairs)]
    for mask in range(1 << npairs):
        hole = base.copy()
        for j in range(npairs):
            if (mask >> j) & 1:
                hole |= memb[j]
        c = np.where(hole, 0, 1).astype(np.int64)
        M, _ = hole_matching(c, m)
        T[mask] = M
        H[mask] = int(hole.sum())
    return T, H


@nb.njit(cache=True)
def enum_core(Kd, Kf_unused, Ed, sizes_pair, npairs, m, phi, Mtab, htab, topk, Dconst):
    """Enumerate v in {-1,0,1}^npairs (v[0] restricted to {0,1} by the global sign symmetry is NOT assumed).
    Kd[s, j]  : Walsh contribution of pair j at value +1 (K[s,O_j] - K[s,A O_j])
    Ed        : quadratic form for D as a function of pair values: D = Dconst + sum_j lin[j]|v_j| ... handled by
                 explicit recomputation D = sum_{j<k} Q[j,k] terms passed in Ed as a (npairs+1) x (npairs+1) matrix
                 of edge counts in 'pair space' (see driver)."""
    return 0


def run_group(name, G, m, anti_perm, topk=20, log=None, extra_forced=()):
    t0 = time.time()
    N = 1 << m
    orb, reps, maps = cell_orbits(G, m)
    no = len(reps)
    sizes, K, E = orbit_data(orb, reps, m)
    # anti-map on cells: x -> complement(pi x)
    pic = perm_cells(anti_perm, m)
    A = (N - 1) ^ pic
    Aorb = np.array([orb[A[reps[o]]] for o in range(no)])
    # check A maps orbits to orbits consistently
    for o in range(no):
        cells = np.where(orb == o)[0]
        assert np.all(orb[A[cells]] == Aorb[o]), "anti-map does not normalise G"
    forced = [o for o in range(no) if Aorb[o] == o] + list(extra_forced)
    pairs = []
    for o in range(no):
        if Aorb[o] != o and o < Aorb[o]:
            pairs.append((o, int(Aorb[o])))
    npairs = len(pairs)
    msg = f"{name}: m={m} |G|={len(G)} orbits={no} pairs={npairs} forced-hole orbits={len(forced)} " \
          f"forced holes={int(sizes[forced].sum()) if forced else 0}"
    print(msg, flush=True)
    if log: log.write(msg + "\n"); log.flush()
    Mtab, htab = matching_table(orb, [list(p) for p in pairs], forced, m, npairs)
    # Walsh: W0(s) = sum_j v_j (K[s,a_j] - K[s,b_j])
    Kd = np.zeros((no, npairs), dtype=np.int64)
    for j, (a, b) in enumerate(pairs):
        Kd[:, j] = K[:, a] - K[:, b]
    # D as quadratic form in the full orbit vector u (u_a = v_j, u_b = -v_j, forced = 0)
    # D(u) = sum_{o<o'} E[o,o'] (u_o - u_o')^2 ; build matrix L = Laplacian of the orbit graph
    L = -E.astype(np.int64).copy()
    np.fill_diagonal(L, 0)
    L[np.diag_indices(no)] = -L.sum(axis=1)
    # map pair vector -> orbit vector: u = P v
    P = np.zeros((no, npairs), dtype=np.int64)
    for j, (a, b) in enumerate(pairs):
        P[a, j] = 1; P[b, j] = -1
    Q = P.T @ L @ P       # D = v^T Q v
    phi = phi_table(N)
    best = enum_all(Kd, Q, sizes, npairs, m, phi, Mtab, htab, topk)
    Rs, Vs = best
    out = []
    for r, v in zip(Rs, Vs):
        if r < -1e8:
            continue
        u = P @ v
        c0 = u[orb]
        ev = evaluate(c0, m)
        out.append((float(r), v.tolist(), ev))
    msg = f"{name}: done in {time.time()-t0:.1f}s; best R = {out[0][0]:.12f}" if out else f"{name}: nothing"
    print(msg, flush=True)
    if log:
        log.write(msg + "\n")
        for r, v, ev in out:
            log.write(f"  {r:.12f} v={v} holes={ev['holes']} pairs={ev['pairs']} singles={ev['singles']} "
                      f"nvars={ev['nvars']} I={ev['I']:.6f} H={ev['H']:.6f}\n")
        log.flush()
    return out, dict(orb=orb, pairs=pairs, forced=forced, P=P)


@nb.njit(cache=True)
def enum_all(Kd, Q, sizes, npairs, m, phi, Mtab, htab, topk):
    N = 1 << m
    ns = Kd.shape[0]
    v = -np.ones(npairs, dtype=np.int64)
    W = np.zeros(ns, dtype=np.int64)
    for s in range(ns):
        for j in range(npairs):
            W[s] += v[j] * Kd[s, j]
    # D = v^T Q v, keep Qv
    Qv = np.zeros(npairs, dtype=np.int64)
    for j in range(npairs):
        for k in range(npairs):
            Qv[j] += Q[j, k] * v[k]
    D = 0
    for j in range(npairs):
        D += v[j] * Qv[j]
    mask = 0
    outR = np.full(topk, -1e9)
    outV = np.zeros((topk, npairs), dtype=np.int64)
    total = 1
    for j in range(npairs):
        total *= 3
    for t in range(total):
        # evaluate
        Hc = 0.0
        for s in range(ns):
            w = W[s]
            if w < 0:
                w = -w
            Hc += sizes[s] * phi[w]
        h = htab[mask]
        M = Mtab[mask]
        H = Hc + (2.0 * m * h - 4.0 * M) / N
        I = (D + (m + 2) * h - 2 * M) / (2.0 * N)
        if I > 1.0 + 1e-12:
            R = H / (I - 1.0)
            if R > outR[topk - 1]:
                i = topk - 1
                while i > 0 and outR[i - 1] < R:
                    outR[i] = outR[i - 1]
                    for q in range(npairs):
                        outV[i, q] = outV[i - 1, q]
                    i -= 1
                outR[i] = R
                for q in range(npairs):
                    outV[i, q] = v[q]
        # increment odometer with incremental updates
        j = 0
        while j < npairs:
            old = v[j]
            new = old + 1
            carry = False
            if new > 1:
                new = -1
                carry = True
            dv = new - old
            # update W
            for s in range(ns):
                W[s] += dv * Kd[s, j]
            # update D: D' = D + 2 dv Qv[j] + dv^2 Q[j,j]
            D += 2 * dv * Qv[j] + dv * dv * Q[j, j]
            for k in range(npairs):
                Qv[k] += Q[k, j] * dv
            v[j] = new
            if new == 0:
                mask |= (1 << j)
            else:
                mask &= ~(1 << j)
            if not carry:
                break
            j += 1
    return outR, outV

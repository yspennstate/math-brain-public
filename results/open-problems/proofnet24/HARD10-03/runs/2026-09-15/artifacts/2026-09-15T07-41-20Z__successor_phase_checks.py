#!/usr/bin/env python3
"""
HARD10-03 numerical finite-graph checks for the successor-phase identities.

This is a sanity check, not the proof. On a cycle graph C_n, enumerate the full
interchange process on S_n and compare:

(1) At any phase s, the displacement between label 0 and its final successor
    Y = pi_beta(0), after both are evolved to phase s, has exactly the same
    distribution as a single tagged particle at time beta.

(2) The Palm intensity of a transposition directly swapping label 0 with Y is
    degree * p_beta(0,0), independent of s.

(3) The Palm intensity of a transition from nonadjacent to adjacent for the
    pair (0,Y) is phase-independent. On a sufficiently large cycle it equals
      2 * (p_beta(0,1) + p_beta(0,2))
    in d=1, agreeing with the Z^d formula specialized to d=1.

The matrix exponentials are floating point. The report contains the exact
infinite-lattice derivation.
"""
import itertools
import numpy as np
from scipy.linalg import expm


def compose(P, Q):
    return tuple(P[Q[i]] for i in range(len(Q)))


def tau(n, a, b):
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def edges_cycle(n):
    return [(i, (i + 1) % n) for i in range(n)]


def cyc_dist(n, a, b):
    k = (b - a) % n
    return min(k, n - k)


def interchange_generator(n):
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    edges = edges_cycle(n)
    taus = [tau(n, *e) for e in edges]
    N = len(perms)
    G = np.zeros((N, N))
    for p in perms:
        i = idx[p]
        for tr in taus:
            q = compose(tr, p)
            G[i, idx[q]] += 1.0
            G[i, i] -= 1.0
    return perms, idx, edges, taus, G


def tagged_generator(n):
    L = np.zeros((n, n))
    for a, b in edges_cycle(n):
        L[a, b] += 1
        L[b, a] += 1
        L[a, a] -= 1
        L[b, b] -= 1
    return L


def check(n=6, beta=1.7, s=0.6):
    perms, idx, edges, taus, G = interchange_generator(n)
    identity = tuple(range(n))
    i0 = idx[identity]
    ps = expm(s * G)[i0]
    pt = expm((beta - s) * G)[i0]
    ptag = expm(beta * tagged_generator(n))[0]

    successor_hist = np.zeros(n)
    direct_intensity = 0.0
    entry_intensity = 0.0

    for iq, Q in enumerate(perms):
        pq = ps[iq]
        if pq < 1e-17:
            continue
        for ir, R in enumerate(perms):
            w = pq * pt[ir]
            if w < 1e-19:
                continue

            P = compose(R, Q)
            Y = P[0]
            a = Q[0]
            b = Q[Y]
            successor_hist[(b - a) % n] += w

            for e, tr in zip(edges, taus):
                Q2 = compose(tr, Q)
                P2 = compose(R, Q2)
                Y2 = P2[0]
                a0, b0 = Q[0], Q[Y2]
                a1, b1 = Q2[0], Q2[Y2]

                if Y2 != 0 and {a0, b0} == set(e) and a1 == b0 and b1 == a0:
                    direct_intensity += w

                if cyc_dist(n, a0, b0) != 1 and cyc_dist(n, a1, b1) == 1:
                    entry_intensity += w

    direct_target = 2.0 * ptag[0]
    entry_target = 2.0 * (ptag[1] + ptag[2])

    return {
        "n": n,
        "beta": beta,
        "s": s,
        "successor_hist_max_error": float(np.max(np.abs(successor_hist - ptag))),
        "direct_intensity": float(direct_intensity),
        "direct_target": float(direct_target),
        "direct_error": float(abs(direct_intensity - direct_target)),
        "entry_intensity": float(entry_intensity),
        "entry_target": float(entry_target),
        "entry_error": float(abs(entry_intensity - entry_target)),
    }


if __name__ == "__main__":
    for s in (0.0, 0.2, 0.6, 1.2, 1.7):
        out = check(n=6, beta=1.7, s=s)
        print(out)
        assert out["successor_hist_max_error"] < 2e-12
        assert out["direct_error"] < 2e-12
        assert out["entry_error"] < 2e-12

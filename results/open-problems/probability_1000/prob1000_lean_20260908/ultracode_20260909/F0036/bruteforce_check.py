"""
Independent check of the pair-reachability DP in pmrca_sim.py: on small random arrow
configurations, enumerate ALL paths from time 0 explicitly, form all pairs, keep pairs
(pi, pi') with pi(0) <= pi'(0), pi(u) < pi'(u) for 0 < u < t, pi(t) = pi'(t), and collect
their first meeting sites.  Compare the resulting set with the DP's PMRCA sites.
"""
import numpy as np, itertools, sys

def arrows(L, T, eps, rng):
    R = np.zeros((T, L), bool); Lf = np.zeros((T, L), bool)
    for s in range(T):
        u = rng.random(L)
        R[s] = u < (1 - eps)/2 + eps
        Lf[s] = u >= (1 - eps)/2
    return R, Lf

def all_paths(L, T, R, Lf):
    # paths from every even site at time 0, length T (positions at times 0..T); killed at boundary
    paths = [[x] for x in range(0, L, 2)]
    done = []
    for s in range(T):
        new = []
        for p in paths:
            x = p[-1]; ext = False
            if R[s, x] and x + 1 < L: new.append(p + [x + 1]); ext = True
            if Lf[s, x] and x - 1 >= 0: new.append(p + [x - 1]); ext = True
            if not ext: done.append(p)      # killed at the boundary: keep the partial path
        paths = new
    return paths + done

def brute_pmrca(L, T, R, Lf):
    paths = all_paths(L, T, R, Lf)
    sites = set()
    for a, b in itertools.combinations(paths, 2):
        if a[0] > b[0] or (a[0] == b[0] and a[1] > b[1]): a, b = b, a
        # first meeting time
        for t in range(1, min(len(a), len(b))):
            if a[t] == b[t]:
                if all(a[u] < b[u] for u in range(1, t)):
                    sites.add((a[t], t))
                break
            if a[t] > b[t]:
                break
    return sites

def dp_pmrca(L, T, R, Lf):
    occ = np.zeros(L, bool); occ[0::2] = True
    A = None; sites = set()
    for s in range(T):
        Rs, Ls = R[s], Lf[s]
        occ_new = np.zeros(L, bool)
        occ_new[1:] |= occ[:-1] & Rs[:-1]
        occ_new[:-1] |= occ[1:] & Ls[1:]
        if s >= 1:
            p = np.arange(0, L - 2)
            d = A[p, p + 2] & Rs[p] & Ls[p + 2]
            for x in p[d]: sites.add((int(x) + 1, s + 1))
            B = np.zeros_like(A)
            m = A & Rs[:, None] & Rs[None, :]; B[1:, 1:] |= m[:-1, :-1]
            m = A & Rs[:, None] & Ls[None, :]; B[1:, :-1] |= m[:-1, 1:]
            m = A & Ls[:, None] & Rs[None, :]; B[:-1, 1:] |= m[1:, :-1]
            m = A & Ls[:, None] & Ls[None, :]; B[:-1, :-1] |= m[1:, 1:]
            np.fill_diagonal(B, False); A = B
        else:
            A = np.triu(occ_new[:, None] & occ_new[None, :], 1)
            # time-1 meetings (t=1: the open interval (0,1) is empty) are counted by neither
        occ = occ_new
    return sites

rng = np.random.default_rng(12345)
tot_b = tot_d = 0; mism = 0
for trial in range(300):
    L = int(rng.integers(6, 13)); T = int(rng.integers(3, 9)); eps = float(rng.choice([0.1, 0.3, 0.5]))
    R, Lf = arrows(L, T, eps, rng)
    b = {z for z in brute_pmrca(L, T, R, Lf) if z[1] >= 2}
    d = {z for z in dp_pmrca(L, T, R, Lf) if z[1] >= 2}
    tot_b += len(b); tot_d += len(d)
    if b != d:
        mism += 1
        if mism <= 3: print("MISMATCH", L, T, eps, sorted(b - d), sorted(d - b))
print("trials 300, brute total", tot_b, "dp total", tot_d, "mismatching trials", mism)

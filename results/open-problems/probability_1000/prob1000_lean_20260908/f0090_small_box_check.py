"""Exact small-box control for the F0090 coding bound (2026-09-10, claude-prob1000-0910).

Critical bond percolation on an m x m array of sites (p = 1/2), f = +-1 indicator of a left-right crossing.
Computes the exact spectral distribution by a Walsh-Hadamard transform over all 2^E configurations, then
    H(S)              spectral entropy (bits),
    I(f) = E|S|       total influence,
    E|S_r|            expected number of dyadic r-squares (on the site grid) hit by the spectral sample,
    bound             1 + 4 * sum_{r >= 2} E|S_r| + c0 * E|S_1|,
and the same for the pivotal set P. The inequality H <= bound is Shannon's; this script is a positive control
that the objects are being computed as the memo defines them (P[S cap B != 0] via the conditional-variance
identity is checked against the direct Fourier sum). Feasible up to about E = 24 edges (m = 4).
"""
import itertools, math, sys
import numpy as np

def edges(m):
    E = []
    for i in range(m):
        for j in range(m):
            if j + 1 < m: E.append(((i, j), (i, j + 1)))
            if i + 1 < m: E.append(((i, j), (i + 1, j)))
    return E

def crossing_table(m, E):
    n = len(E); N = 1 << n
    f = np.empty(N, dtype=np.float64)
    idx = {(i, j): i * m + j for i in range(m) for j in range(m)}
    for c in range(N):
        parent = list(range(m * m))
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]; a = parent[a]
            return a
        for k in range(n):
            if c >> k & 1:
                a, b = find(idx[E[k][0]]), find(idx[E[k][1]])
                if a != b: parent[a] = b
        left = {find(idx[(i, 0)]) for i in range(m)}
        right = {find(idx[(i, m - 1)]) for i in range(m)}
        f[c] = 1.0 if left & right else -1.0
    return f

def wht(a):
    a = a.copy(); h = 1; n = len(a)
    while h < n:
        a = a.reshape(-1, 2, h)
        x, y = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :] = x + y; a[:, 1, :] = x - y
        a = a.reshape(n); h *= 2
    return a

def main(m):
    E = edges(m); n = len(E); N = 1 << n
    f = crossing_table(m, E)
    fhat = wht(f) / N                      # fhat[S] for S encoded as a bitmask over edges
    spec = fhat ** 2                        # spectral distribution, sums to 1
    assert abs(spec.sum() - 1) < 1e-9
    H = -np.sum(spec[spec > 0] * np.log2(spec[spec > 0]))
    popcount = np.array([bin(s).count("1") for s in range(N)])
    I = float(np.sum(spec * popcount))
    # site squares: edge k lies in the square of its first endpoint's site (for the dyadic hierarchy on sites)
    site_of_edge = [E[k][0] for k in range(n)]
    def hit_prob_spec(mask):        # P[S cap mask != 0] from the spectrum
        return float(spec[(np.arange(N) & mask) != 0].sum())
    def hit_prob_condvar(mask):     # E[Var(f | bits outside mask)]
        out = (np.arange(N) & ~mask) & (N - 1)
        # group by outside configuration
        order = np.argsort(out, kind="stable"); o = out[order]; fv = f[order]
        cuts = np.flatnonzero(np.diff(o)) + 1
        tot = 0.0
        for grp in np.split(fv, cuts):
            tot += grp.var() * len(grp)
        return tot / N
    scales = []
    r = 1; bound_terms = {}
    while r <= m:
        es = 0.0
        for i0 in range(0, m, r):
            for j0 in range(0, m, r):
                mask = 0
                for k in range(n):
                    si, sj = site_of_edge[k]
                    if i0 <= si < i0 + r and j0 <= sj < j0 + r: mask |= 1 << k
                if mask:
                    p1 = hit_prob_spec(mask)
                    if r == 1 and (i0, j0) == (0, 0):
                        p2 = hit_prob_condvar(mask)
                        assert abs(p1 - p2) < 1e-9, (p1, p2)
                    es += p1
        bound_terms[r] = es; r *= 2
    bound = 1 + 4 * sum(v for r, v in bound_terms.items() if r >= 2) + 2 * bound_terms[1]
    print(f"m={m} sites, {n} edges: H(S)={H:.4f} bits, I(f)=E|S|={I:.4f}, E|S_r|={ {r: round(v,4) for r,v in bound_terms.items()} }, coding bound={bound:.3f}, H/I={H/I:.3f}")

if __name__ == "__main__":
    for m in [int(a) for a in sys.argv[1:]] or [2, 3, 4]:
        main(m)

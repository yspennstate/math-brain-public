"""Structural descriptors of a Boolean function.

coin set: a set Y of variables that pairwise do not interact, i.e. fhat(S) = 0 whenever |S & Y| >= 2
(equivalently D_y D_y' f = 0 for y != y' in Y).  Then f(x,y) = c0(x) + sum_{y in Y} a_y(x) y with {-1,0,1}-valued
c0, a_y of pairwise disjoint supports: a core c0 on the other variables with holes A_y = supp(a_y) read from the
coin y (F2's 'core with holes').  kappa(f) = largest coin set.
"""
import numpy as np
import itertools
from core import walsh_int, relevant, compress


def interaction_matrix(tt):
    """M[i,j] = sum_{S >= {i,j}} fhat(S)^2 (i != j)."""
    tt = np.ascontiguousarray(tt, dtype=np.int8)
    N = tt.shape[0]
    n = int(round(np.log2(N)))
    W = walsh_int(tt).astype(np.float64) / N
    P = W * W
    S = np.arange(N)
    M = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            m = (((S >> i) & 1) == 1) & (((S >> j) & 1) == 1)
            M[i, j] = M[j, i] = P[m].sum()
    return M


def max_coin_set(tt, tol=1e-14):
    """Largest set of pairwise non-interacting relevant variables (exhaustive for <= 20 relevant variables)."""
    M = interaction_matrix(tt)
    rel = relevant(tt)
    k = len(rel)
    adj = [[M[rel[a], rel[b]] > tol for b in range(k)] for a in range(k)]
    best = []
    # simple branch and bound max independent set
    order = sorted(range(k), key=lambda a: sum(adj[a]))

    def rec(cands, cur):
        nonlocal best
        if len(cur) + len(cands) <= len(best):
            return
        if not cands:
            if len(cur) > len(best):
                best = cur[:]
            return
        v = cands[0]
        rest = cands[1:]
        rec([u for u in rest if not adj[v][u]], cur + [v])
        rec(rest, cur)

    rec(order, [])
    return sorted(rel[a] for a in best)


def core_with_holes(tt, Y):
    """Given a coin set Y, return core c0 (dict over assignments of the other relevant variables) and holes."""
    tt = np.asarray(tt, dtype=np.int8)
    N = tt.shape[0]
    n = int(round(np.log2(N)))
    rel = relevant(tt)
    X = [i for i in rel if i not in Y]
    core = {}
    holes = {y: [] for y in Y}
    for a in range(1 << len(X)):
        base = 0
        for j, i in enumerate(X):
            if (a >> j) & 1:
                base |= 1 << i
        vals = set()
        dep = []
        for y in Y:
            if tt[base] != tt[base | (1 << y)]:
                dep.append(y)
        if not dep:
            core[a] = 'T' if tt[base] == -1 else 'F'
        else:
            assert len(dep) == 1, 'not a coin set'
            y = dep[0]
            core[a] = ('~' if tt[base] == -1 else '') + 'y%d' % y   # value at y=0 (+1)
            holes[y].append(a)
    return X, core, holes


def hole_shape(cells, m):
    """Dimension of the smallest subcube containing the cells, and whether they form exactly a subcube."""
    if not cells:
        return None
    a0 = cells[0]
    free = 0
    for c in cells:
        free |= c ^ a0
    d = bin(free).count('1')
    return d, (len(cells) == (1 << d))

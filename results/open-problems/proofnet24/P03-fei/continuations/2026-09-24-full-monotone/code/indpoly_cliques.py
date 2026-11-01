"""I(G; -1) for the overlap graph of all k-cliques inside K_L (two k-cliques adjacent iff they share an edge).

Z_1(x) = I(G_{S(x)}; -1) is the packing expansion of the zero-set indicator restricted to the satisfied terms; if it
grows like the number of packings on dense configurations, moment bounds on the packing expansion fail and the proof
has to go through single-coordinate (Parseval) estimates instead. Exact enumeration for small k, L.
"""
import itertools, functools, sys
print = functools.partial(print, flush=True)


def ind_poly_minus1(adj, nv):
    """sum over independent sets of (-1)^{|I|}, by the deletion-contraction recursion I(G) = I(G - v) - I(G - N[v])."""
    sys.setrecursionlimit(10000)
    memo = {}
    def rec(mask):
        if mask == 0:
            return 1
        if mask in memo:
            return memo[mask]
        v = (mask & -mask).bit_length() - 1
        r = rec(mask & ~(1 << v)) - rec(mask & ~(1 << v) & ~adj[v])
        memo[mask] = r
        return r
    return rec((1 << nv) - 1)


def count_indep(adj, nv):
    memo = {}
    def rec(mask):
        if mask == 0:
            return 1
        if mask in memo:
            return memo[mask]
        v = (mask & -mask).bit_length() - 1
        r = rec(mask & ~(1 << v)) + rec(mask & ~(1 << v) & ~adj[v])
        memo[mask] = r
        return r
    return rec((1 << nv) - 1)


for k in (3, 4):
    for L in range(k, 10 if k == 3 else 9):
        cl = list(itertools.combinations(range(L), k))
        nv = len(cl)
        if nv > 60:
            break
        adj = [0] * nv
        for i in range(nv):
            for j in range(nv):
                if i != j and len(set(cl[i]) & set(cl[j])) >= 2:
                    adj[i] |= 1 << j
        val = ind_poly_minus1(adj, nv)
        cnt = count_indep(adj, nv)
        print(f"k={k} L={L}: {nv} cliques, independent sets {cnt}, I(G;-1) = {val}")

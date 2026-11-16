"""H at symmetric weighted graphs whose top Laplacian eigenvalue is repeated: disjoint unions of cliques balanced
so their tops agree, odd cycles, and a few small graphs. Same quantities as t104_subclique.py (H, its limit along
small random perturbations, slack, relative gap between the two top eigenvalues).
usage: python t104_degen_family.py nmin nmax
"""
import importlib.util
import itertools
import sys
import numpy as np

here = __file__.replace("t104_degen_family.py", "t104_np_hsearch.py")
nmin, nmax = int(sys.argv[1]), int(sys.argv[2])


def cliques(sizes):
    """disjoint uniform cliques, each edge of K_a weighted 1/a so every clique has top eigenvalue 1"""
    out, v = {}, 0
    for a in sizes:
        for i, j in itertools.combinations(range(v, v + a), 2):
            out[(i, j)] = 1.0 / a
        v += a
    return out, v


def cycle(c):
    return {tuple(sorted((i, (i + 1) % c))): 1.0 for i in range(c)}, c


def family(n):
    fam = []
    for parts in [(2, 2), (2, 3), (3, 3), (2, 2, 2), (2, 4), (3, 4), (4, 4), (2, 2, 3), (2, 3, 3)]:
        e, v = cliques(parts)
        if v <= n:
            fam.append(("cliques " + "+".join("K%d" % a for a in parts), e, 2.0 - 2.0 / sum(a - 1 for a in parts)))
    for c in (5, 7):
        if c <= n:
            fam.append(("C_%d" % c, cycle(c)[0], None))
    fam.append(("triangle+pendant", {(0, 1): 1, (0, 2): 1, (1, 2): 1, (2, 3): 1}, None))
    if n >= 5:
        fam.append(("K4 minus edge", {(0, 1): 1, (0, 2): 1, (0, 3): 1, (1, 2): 1, (1, 3): 1}, None))
    return fam


for n in range(nmin, nmax + 1):
    sys.argv = ["t104_np_hsearch.py", str(n), "1", "1", "1", "1"]
    spec = importlib.util.spec_from_file_location("hs%d" % n, here)
    h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
    rng = np.random.default_rng(5)
    idx = {p: t for t, p in enumerate(h.pairs)}
    for name, e, pred in family(n):
        w = np.zeros(h.m)
        for p, x in e.items():
            w[idx[p]] = x
        w /= w.sum()
        v, sl, g = h.values(w[None, :], h.GRID)
        V = rng.exponential(size=(200, h.m)); V /= V.sum(1, keepdims=True)
        lim = h.values(w[None, :] + 1e-6 * (V - w[None, :]), h.GRID)[0].min()
        tail = "" if pred is None else "  2-2/D %+.6f  diff %.1e" % (pred, abs(v[0] - pred))
        print("n %d  %-20s H %+.6f  min H at 1e-6 over 200 dirs %+.6f  slack %+.6f  gap12 %.1e%s"
              % (n, name, v[0], lim, sl[0], g[0], tail), flush=True)

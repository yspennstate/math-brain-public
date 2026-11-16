"""s_inf next to the single-edge equality case: one edge (1,2) of weight 1, all others 0.

The symmetry group is S_2 x S_{n-2}. A first order perturbation adds nonnegative weight on the other edges (and
renormalises). Two orbits of edges: type a (from {0,1} to the rest) and type b (inside the rest). This script prints
s_inf at the edge, the top gap, the first derivatives along one edge of each type (renormalised) by Richardson
differences, and the minimum of s_inf / eps over random nonnegative directions.

usage: python t104_edge_local.py nmin nmax ndirs
"""
import sys
import numpy as np

src = open(__file__.replace("t104_edge_local.py", "t104_star_local.py"), encoding="utf-8").read()
head = src[src.index("import numpy as np"):src.index("star = np.zeros")]


def build(n):
    g = {"__name__": "lib"}
    exec("import sys\n" + head.replace("n = int(sys.argv[1]); NDIR = int(sys.argv[2]); rng = np.random.default_rng(int(sys.argv[3]))", "n = %d" % n), g)
    return g


rng = np.random.default_rng(7)
for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    g = build(n)
    pairs, parts = g["pairs"], g["parts"]
    edge = np.zeros(len(pairs)); edge[pairs.index((0, 1))] = 1.0
    s0, gap0 = parts(edge)
    va = np.zeros(len(pairs)); va[pairs.index((0, 2))] = 1.0
    vb = np.zeros(len(pairs)); vb[pairs.index((2, 3))] = 1.0

    def d1(v):
        ds = [parts(edge + t * v)[0] / t for t in (2e-6, 1e-6)]
        return 2 * ds[1] - ds[0]

    pa, pb = d1(va), d1(vb)
    # random nonnegative directions on the other edges
    others = [k for k, p in enumerate(pairs) if p != (0, 1)]
    worst = np.inf; worst_eps2 = np.inf
    for _ in range(int(sys.argv[3])):
        v = np.zeros(len(pairs))
        b = rng.exponential(size=len(others)) * (rng.random(len(others)) < 0.5)
        if b.sum() == 0:
            b[0] = 1.0
        v[others] = b / b.sum()
        for e in (1e-3, 1e-5):
            worst = min(worst, parts(edge + e * v)[0] / e)
    # the edge weight itself is fixed by normalisation; a pure rescale does nothing
    print("n %2d  s(edge) %+.2e  gap %.4f  d/da %.6f  d/db %.6f  min s/eps over random dirs %.6f" %
          (n, s0, gap0, pa, pb, worst), flush=True)

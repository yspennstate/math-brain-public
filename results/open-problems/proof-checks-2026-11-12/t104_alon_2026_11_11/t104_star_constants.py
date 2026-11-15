"""The two constants of s_inf at the uniform star: c (second derivative along a leaf-weight deviation, per |delta|^2)
and c1 (first derivative per unit of leaf-leaf weight), plus the cross coefficient, by Richardson-extrapolated
differences. By the S_{n-1} symmetry of the star these numbers determine the first and second order terms.

usage: python t104_star_constants.py nmin nmax
"""
import sys
import numpy as np

src = open(__file__.replace("t104_star_constants.py", "t104_star_local.py"), encoding="utf-8").read()
head = src[src.index("import numpy as np"):src.index("star = np.zeros")]


def build(n):
    g = {"__name__": "lib"}
    sys.argv = ["x", str(n), "1", "1"]
    exec("import sys\n" + head.replace("n = int(sys.argv[1]); NDIR = int(sys.argv[2]); rng = np.random.default_rng(int(sys.argv[3]))", "n = %d" % n), g)
    return g


for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    g = build(n)
    pairs, parts = g["pairs"], g["parts"]
    star = np.zeros(len(pairs))
    for j in range(1, n):
        star[pairs.index((0, j))] = 1.0 / (n - 1)
    vd = np.zeros(len(pairs)); vd[pairs.index((0, 1))] = 1 / np.sqrt(2); vd[pairs.index((0, 2))] = -1 / np.sqrt(2)
    ve = np.zeros(len(pairs)); ve[pairs.index((1, 2))] = 1.0
    ve2 = np.zeros(len(pairs)); ve2[pairs.index((2, 3))] = 1.0

    def f(v, t):
        return parts(star + t * v)[0]

    # c: s(t vd) = c t^2 + O(t^4) (odd terms vanish: the swap of leaves 1, 2 maps vd to -vd)
    cs = [f(vd, t) / t ** 2 for t in (2e-3, 1e-3)]
    c = (4 * cs[1] - cs[0]) / 3
    # c1: s(t ve) = c1 t + O(t^2), one-sided (t >= 0)
    ds = [f(ve, t) / t for t in (2e-6, 1e-6)]
    c1 = 2 * ds[1] - ds[0]
    # cross: s(t vd + u ve) - s(t vd) - s(u ve) = k t u + ...; edge (1,2) touches both changed leaves
    t, u = 1e-3, 1e-6
    k12 = (f(vd + (u / t) * ve, t) - f(vd, t) - f(ve, u)) / (t * u)
    k23 = (f(vd + (u / t) * ve2, t) - f(vd, t) - f(ve2, u)) / (t * u)
    print("n %2d  c %.6f  c1 %.6f  cross(edge 12) %+.4f  cross(edge 23) %+.4f" % (n, c, c1, k12, k23), flush=True)

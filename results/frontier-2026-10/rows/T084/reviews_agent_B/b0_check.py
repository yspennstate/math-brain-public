"""Check b_0 = lowest Bernstein coefficient against p^2(1-p)^2 E[d_e d_f k] / normalisation: at u -> 0, N/u -> (Z_e Z_f - Z Z_ef)'s
u-derivative at q = 1, which should equal Z^2 * p^2 (1-p)^2 E_Bern[d_e d_f k] with Z = (1+lam)^m, p = lam/(1+lam).
Exact rationals, K4 and a random 6-vertex graph."""
import itertools
from fractions import Fraction as Fr
from bern_general import numerator, comps

for n, edges, e, f in ((4, list(itertools.combinations(range(4), 2)), 0, 1), (4, list(itertools.combinations(range(4), 2)), 0, 5),
                       (6, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3), (1, 4), (0, 5)], 0, 7)):
    N = numerator(n, edges, edges.index(edges[e]), f)
    m = len(edges)
    for lam in (Fr(1, 3), Fr(2), Fr(7, 5)):
        a1 = sum(c * lam ** i for (i, j), c in N.items() if j == 1)  # coefficient of u^1
        p = lam / (1 + lam); E = Fr(0)
        for mask in range(1 << m):
            if mask >> e & 1 or mask >> f & 1: continue
            w = p ** bin(mask).count("1") * (1 - p) ** (m - 2 - bin(mask).count("1"))
            E += w * (comps(n, edges, mask | 1 << e | 1 << f) - comps(n, edges, mask | 1 << e) - comps(n, edges, mask | 1 << f) + comps(n, edges, mask))
        pred = (1 + lam) ** (2 * m) * p ** 2 * (1 - p) ** 2 * E
        print(n, e, f, lam, "u^1 coeff == Z^2 p^2(1-p)^2 E[dd k]" if a1 == pred else ("DIFF", a1, pred), "E>=0" if E >= 0 else "E<0")

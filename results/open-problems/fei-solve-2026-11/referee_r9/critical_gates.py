"""Critical limit per gate: stack gate g at its own fixed point (mean pinned), from each realizable bottom (one real layer)."""
import numpy as np
from scipy.optimize import brentq
from tower_recompute import PM, T, dual, G, compose, LEAF
gates = {"M": G(PM(3)), "D": G(dual(PM(3))), "P": G(PM(4)), "Pd": G(dual(PM(4))), "Q2": G(dual(T(2, 2))),
         "T26": G(T(2, 6)), "dT26": G(dual(T(2, 6))), "T35": G(T(3, 5)), "dT35": G(dual(T(3, 5))), "dT43": G(dual(T(4, 3)))}
probe = compose(LEAF, *gates["M"])[0]
def mean_out(g, mu):
    st = (mu, mu * mu) + tuple(probe[2:])
    return compose(st, *g)[0][0]
res = []
for gn, g in gates.items():
    xs = np.linspace(-0.98, 0.98, 197)
    vals = [mean_out(g, x) - x for x in xs]
    roots = [brentq(lambda x: mean_out(g, x) - x, xs[i], xs[i + 1], xtol=1e-14)
             for i in range(len(xs) - 1) if vals[i] * vals[i + 1] < 0]
    for m in roots:
        for bn, b in gates.items():
            st = compose(LEAF, *b)[0]
            st = (m, m * m) + tuple(st[2:])
            try:
                for _ in range(50):
                    st, r = compose(st, *g)
                    st = (m, m * m) + tuple(st[2:])
            except AssertionError:
                continue
            res.append((r, gn, round(m, 6), bn))
res.sort(reverse=True)
for row in res[:15]:
    print(f"{row[0]:.10f}  gate {row[1]} at mean {row[2]}  bottom {row[3]}")

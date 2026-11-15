# Critical-point limit, corrected 18:4x: pin the mean at M's fixed point in the +-1 convention (true = -1),
# m* = 1 - 2 p* = -0.03492. The 18:2x version pinned at +0.03492 (sign bug) and its 4.49769 is void.
import itertools
from scipy.optimize import brentq
from tower_recompute import PM, dual, G, compose, LEAF
M, D = G(PM(3)), G(dual(PM(3)))
def phi(p):
    tot = 0.0
    for x in range(512):
        bits = [(x >> k) & 1 for k in range(9)]
        if any(all(bits[r * 3 + s[r]] for r in range(3)) for s in itertools.permutations(range(3))):
            tot += p ** sum(bits) * (1 - p) ** (9 - sum(bits))
    return tot
ps = brentq(lambda p: phi(p) - p, 0.3, 0.95, xtol=1e-15)
mfix = 1 - 2 * ps
assert mfix < 0
st, _ = compose(LEAF, *D)
print("D mean", st[0], "M fixed point mean", mfix)
st = (mfix, mfix ** 2) + tuple(st[2:])
out = []
for k in range(1, 61):
    st, r = compose(st, *M)
    out.append(r)
    st = (mfix, mfix ** 2) + tuple(st[2:])
print("pinned k=1..60 every 5:", [f"{x:.10f}" for x in out[::5]])
print("pinned limit", f"{out[-1]:.12f}", "max", f"{max(out):.12f} at k={out.index(max(out))+1}")

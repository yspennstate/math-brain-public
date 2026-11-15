from tower_recompute import PM, dual, G, compose, LEAF
from scipy.optimize import brentq
M, D = G(PM(3)), G(dual(PM(3)))
import itertools
def phi(p):  # P(PM(K33) true) when each edge true w.p. p
    tot = 0.0
    for x in range(512):
        bits = [(x >> k) & 1 for k in range(9)]
        if any(all(bits[r * 3 + s[r]] for r in range(3)) for s in itertools.permutations(range(3))):
            tot += p ** sum(bits) * (1 - p) ** (9 - sum(bits))
    return tot
ps = brentq(lambda p: phi(p) - p, 0.3, 0.95)
print(f"M fixed point p* = {ps:.10f}  (mean in +-1 convention {1-2*ps:+.10f})")
for name, seq in (("M^k", [M] * 13), ("D,M^k", [D] + [M] * 13), ("D^k", [D] * 13)):
    st = LEAF
    out = []
    for k, g in enumerate(seq):
        st, r = compose(st, *g)
        out.append(f"{r:.10f}/{st[0]:+.4f}")
    print(name, " ".join(out[:13]))

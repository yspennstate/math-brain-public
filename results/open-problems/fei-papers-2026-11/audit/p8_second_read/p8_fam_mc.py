"""Paper 8 Prop. family49 / family14: Monte Carlo volumes of omega_l (T) and eta_l (T and H)."""
import numpy as np
from p8_moment_mc import vol
def pairs_of(word):
    pos = {}
    for i, c in enumerate(word, 1):
        pos.setdefault(c, []).append(i)
    return [tuple(x) for x in pos.values()], len(word)
rng = np.random.default_rng(3); N = 4_000_000
def v(word, kind):
    pr, n = pairs_of(word); return vol(pr, n, kind, N, rng)
for l in (1, 2, 3):
    ch = [f"c{i}" for i in range(1, l + 1)]
    om = list("abab") + ch + list("dede") + ch[::-1]
    et = list("abcabc") + ch + list("defdef") + ch[::-1]
    print(f"l={l} omega T {v(om,'T')[0]:.4f} (4/9=0.4444) | eta T {v(et,'T')[0]:.4f} H {v(et,'H')[0]:.4f} (1/4)")

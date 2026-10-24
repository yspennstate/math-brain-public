"""Can a smoother window kill the (4/3)^K growth, or is the growth in the WEIGHT itself?

The absolute sum sum_m c(m) |kernel(m/2^K)| grows while the signed sum stays O(1).  Round 1 proposed
replacing the sharp octave indicator by a nonnegative smooth majorant, whose kernel decays fast, and
asked whether that removes the growth.

The test that settles it without choosing a window: look at where the WEIGHT lives.
Let Cum(u) = sum_{0 < m <= u 2^K} c(m) on the consecutive block, so any kernel bound
|G(m/2^K)| <= B(u) gives sum_m c(m)|G| <= integral of B against dCum.
If Cum(u) = (4/3)^K Phi(u) with Phi a FIXED bounded profile, then every kernel with G(0) != 0 picks up
the (4/3)^K factor near the origin and no window shape can help: the growth is in the arithmetic.
If instead the weight sits at large u, a decaying kernel kills it and the majorant lane is alive.
"""
import numpy as np

def block_weights(K):
    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64); c = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c = np.concatenate([c * 0.5, c, c * 0.5])
    B = 2 ** (K + 1) - 1
    sel = (nu >= 1) & (nu <= B)
    m, cm = nu[sel], c[sel]
    o = np.argsort(m)
    return m[o].astype(float), cm[o]

US = [0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0]
print("Cum(u) = sum of c(m) over 0 < m <= u*2^K, and the same divided by (4/3)^K")
print(f"{'K':>3} " + " ".join(f"{'u='+str(u):>11}" for u in US) + f"{'total':>11}")
prof = {}
for K in (6, 8, 10, 12, 14):
    m, c = block_weights(K)
    cum = np.cumsum(c)
    row, nrm = [], (4.0 / 3.0) ** K
    for u in US:
        j = np.searchsorted(m, u * 2 ** K, side="right")
        row.append(cum[j - 1] if j > 0 else 0.0)
    prof[K] = [r / nrm for r in row]
    print(f"{K:>3} " + " ".join(f"{r:>11.4f}" for r in row) + f"{c.sum():>11.4f}")
print()
print("normalised by (4/3)^K -- a FIXED profile means the window cannot help:")
print(f"{'K':>3} " + " ".join(f"{'u='+str(u):>11}" for u in US))
for K in sorted(prof):
    print(f"{K:>3} " + " ".join(f"{v:>11.5f}" for v in prof[K]))
print()
print("ratios between consecutive K (2 steps apart), at each u -- (4/3)^2 = 1.7778:")
Ks = sorted(prof)
for a, b in zip(Ks, Ks[1:]):
    ma, _ = block_weights(a); mb, _ = block_weights(b)
    ca, cb = np.cumsum(block_weights(a)[1]), np.cumsum(block_weights(b)[1])
    r = []
    for u in US:
        ja = np.searchsorted(ma, u * 2 ** a, side="right")
        jb = np.searchsorted(mb, u * 2 ** b, side="right")
        va = ca[ja - 1] if ja > 0 else np.nan
        vb = cb[jb - 1] if jb > 0 else np.nan
        r.append(vb / va)
    print(f"K {a}->{b}: " + " ".join(f"{x:>9.4f}" for x in r))

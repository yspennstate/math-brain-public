"""Mandatory falsifiers from COUNTEREXAMPLES.md replayed against SEL-1 / SEL-2 (selector = the physical bit):
X001 parity lift f(x,z) = g(x_1 z, ..., x_n z) (selector z), X002 parity splice (bent g0, g1 = (-1)^{y_m} g0),
X003 sparse activation splice, X004 overlapping supports (zy)."""
import math
import numpy as np
from rlib import wht, ent, h2, popcount_table, LOG2E, K_of_c

def mux_stats(g0, g1, n):
    """one selector bit (low), data n bits; F[z + 2y]"""
    F = np.empty(2 << n, dtype=np.int64); F[0::2] = g0; F[1::2] = g1
    P = (wht(F).astype(np.float64) / (2 << n)) ** 2
    HF = float(ent(P)); IF = float((P * popcount_table(n + 1)).sum())
    Hg = [float(ent((wht(g).astype(np.float64) / (1 << n)) ** 2)) for g in (g0, g1)]
    Ig = [float(((wht(g).astype(np.float64) / (1 << n)) ** 2 * popcount_table(n)).sum()) for g in (g0, g1)]
    pi = float(np.mean(g0 != g1))
    cost = HF - sum(Hg) / 2
    bound = float(h2(pi)) + min(float(h2(pi)), 2 * LOG2E * pi)
    C = max([h / i if i > 1e-12 else 0.0 for h, i in zip(Hg, Ig)])
    clos = max(C, K_of_c(pi)) * IF if pi > 0 else float("inf")
    return cost, bound, HF, clos, pi

rng = np.random.default_rng(8)
def bent(m):
    idx = np.arange(1 << m); s = np.zeros(1 << m, dtype=np.int64)
    for k in range(0, m - 1, 2): s ^= ((idx >> k) & 1) & ((idx >> (k + 1)) & 1)
    return 1 - 2 * s

rows = []
# X001: parity lift; as a multiplexer in z: g_{z=+1}(x) = g(x), g_{z=-1}(x) = g(-x)
for n in (3, 5, 7, 9):
    for t in range(3):
        g = rng.choice([-1, 1], size=1 << n)
        neg = g[(np.arange(1 << n) ^ ((1 << n) - 1))]
        rows.append(("X001 n=%d" % n,) + mux_stats(g, neg, n))
# X002: bent splice on m+? bits: g0(y) = b(y1+ym, ..., y_{m-1}+y_m), g1 = (-1)^{y_m} g0, odd m
for m in (3, 5, 7, 9, 11):
    idx = np.arange(1 << m)
    ym = (idx >> (m - 1)) & 1
    tt = np.zeros(1 << m, dtype=np.int64)
    for j in range(m - 1):
        tt |= (((idx >> j) & 1) ^ ym) << j
    b = bent(m - 1)
    g0 = b[tt]; g1 = np.where(ym == 1, -g0, g0)
    rows.append(("X002 m=%d" % m,) + mux_stats(g0, g1, m))
# X003: sparse activation children G = 1 + A(b-1), H = 1 + A(b'-1), A = 1_{z=0} on r fresh bits
for k in (4, 6):
    r = 2 * k if 2 * k + k <= 18 else 8
    r = min(r, 18 - k)
    b = bent(k); bp = b.copy(); bp[0] = -bp[0]
    n = k + r
    idx = np.arange(1 << n)
    zpart = idx >> k; xpart = idx & ((1 << k) - 1)
    A = (zpart == 0)
    G = np.where(A, b[xpart], 1); Hh = np.where(A, bp[xpart], 1)
    rows.append(("X003 k=%d r=%d" % (k, r),) + mux_stats(G, Hh, n))
# X004: F = z y
rows.append(("X004 zy",) + mux_stats(np.array([1, -1]), np.array([-1, 1]), 1))
worst1 = max(r[1] - r[2] for r in rows)
worst2 = max(r[3] - r[4] for r in rows)
for r in rows:
    print("%-16s cost=%.6f bound=%.6f ratio=%.4f  pi=%.3e  H-closure=%.4f" % (r[0], r[1], r[2], r[1] / r[2] if r[2] > 0 else float('nan'), r[5], r[3] - r[4]))
print("max cost - SEL1 bound = %.2e ; max H - max(C,K(pi)) I = %.3f" % (worst1, worst2))

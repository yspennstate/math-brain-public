"""Erasure along the amplification tower of Numaro's g:  G_1 = g,  G_k = g(G_{k-1}, ..., G_{k-1}).

g is balanced and monotone, so by the balanced composition law (Theorem 3) for a leaf w in outer block j,
  B_w(G_k)   = Inf_j(g) B_w(G_{k-1}) + Xi_j(c_w^2),    Xi_j(c^2) = sum_{T not ni j} E(ghat(T)^2, c^2 ghat(T+j)^2),
  Inf_w(G_k) = Inf_j(g) Inf_w(G_{k-1}),                c_w = level-1 coefficient of G_{k-1} at w = Inf_w(G_{k-1}).
Hence ratio_k(path) = ratio_{k-1}(tail) + Xi_j(P^2)/(Inf_j P), P = Inf of the tail.  P depends only on the
numbers (a, b) of core and auxiliary positions in the tail, so the minimum over leaves (existential ratio) and
the sum over leaves (B) are dynamic programmes over (a, b).  Also H(G_k)/I(G_k) from the composition identity.
"""
import sys, os, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *
from math import comb

set_polite()
g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy")).astype(np.float64)
n = 18
gh = wht(g[None, :])[0]
p = gh ** 2
cq = coord_quantities(gh[None, :], n)
Inf = cq["Inf"][0]; Bg = cq["B"][0]
H1 = float(entropy(p)); I1 = float(total_influence(p[None, :], n)[0])
lvl1 = np.array([gh[1 << j] for j in range(n)])
assert abs(gh[0]) < 1e-12, "g must be balanced"
core = [j for j in range(n) if abs(abs(lvl1[j]) - 57 / 256) < 1e-12]
aux = [j for j in range(n) if abs(abs(lvl1[j]) - 1 / 256) < 1e-12]
assert len(core) == 9 and len(aux) == 9
assert np.allclose(np.abs(lvl1), Inf), "monotone: Inf_j = |ghat({j})|"
S = np.arange(1 << n)
lows = [S[((S >> j) & 1) == 0] for j in range(n)]


def Xi(j, c2):
    lo = lows[j]
    a = p[lo]; b = c2 * p[lo | (1 << j)]
    return float((phi(a) + phi(b) - phi(a + b)).sum())


ic, ia = 57 / 256, 1 / 256
K = 7
rows = []
# best[(a,b)] = minimal ratio over tails with a core and b aux positions (tail = the inner part, a+b = depth)
best = {}
for j in range(n):
    key = (1, 0) if j in core else (0, 1)
    r = Bg[j] / Inf[j]
    best[key] = min(best.get(key, np.inf), r)
# B sums: Bsum[(a,b)] = total B over leaves of the tail-type (a,b) in G_depth
Bsum = {}
cnt = {}
for j in range(n):
    key = (1, 0) if j in core else (0, 1)
    Bsum[key] = Bsum.get(key, 0.0) + Bg[j]
    cnt[key] = cnt.get(key, 0) + 1
Hk, Ik = H1, I1
xi_cache = {}
for depth in range(1, K + 1):
    Btot = sum(Bsum.values())
    exist = min(best.values())
    rows.append(dict(k=depth, n=18 ** depth, H_over_I=Hk / Ik, B_over_I=Btot / Ik, exist_min_ratio=exist))
    print(json.dumps(rows[-1])); sys.stdout.flush()
    if depth == K:
        break
    nb, nB, nc = {}, {}, {}
    for (a, b), r in best.items():
        P = ic ** a * ia ** b
        for j in range(n):
            ck = (j, a, b)
            if ck not in xi_cache:
                xi_cache[ck] = Xi(j, P * P)
            add = xi_cache[ck] / (Inf[j] * P)
            key = (a + 1, b) if j in core else (a, b + 1)
            nb[key] = min(nb.get(key, np.inf), r + add)
            # B over leaves: each leaf of the tail type (a,b) sits in each outer block j
            nB[key] = nB.get(key, 0.0) + Inf[j] * Bsum[(a, b)] + cnt[(a, b)] * xi_cache[ck]
            nc[key] = nc.get(key, 0) + cnt[(a, b)]
    best, Bsum, cnt = nb, nB, nc
    # H, I of the balanced self-composition: H_k = H(g) + I(g) H_{k-1}, I_k = I(g) I_{k-1}
    Hk, Ik = H1 + I1 * Hk, I1 * Ik
json.dump(rows, open(os.path.join(HERE, "..", "logs", "tower_erasure.json"), "w"), indent=1)
print("limit H/I = H(g)/(I(g)-1) =", H1 / (I1 - 1))

"""SEL-15c check: random members of M_4 generated from dictators by F = Mux_{h(x)}(G_1(y), G_2(y)),
h, G_1, G_2 in the class, G_1 orthogonal to G_2 (shared variables allowed), h on fresh variables.
Verify H(F) <= 4 (I(F) - 1) and balancedness; also the exact two-cell bound H(F) <= 2 + H(h)/2 + avg H(G)."""
import numpy as np
from fei_lib import fwht_int, entropy_from_W, influence_from_W
rng = np.random.default_rng(8)
def stats(t, n):
    W = fwht_int(t); return entropy_from_W(W, n), float(influence_from_W(W, n))
# a member is (table over its own k variables, k)
def dictator(): return (np.array([1, -1], dtype=np.int64), 1)
def embed(tab, k, n, positions):
    """table on n variables reading its k inputs from 'positions' (list of k distinct coordinates)."""
    idx = np.arange(1 << n); sub = np.zeros(1 << n, dtype=np.int64)
    for j, pos in enumerate(positions): sub |= ((idx >> pos) & 1) << j
    return tab[sub]
pool = [dictator()]
worst = -9; worst_two = -9; count = 0
for step in range(3000):
    h = pool[rng.integers(len(pool))]
    g1 = pool[rng.integers(len(pool))]; g2 = pool[rng.integers(len(pool))]
    # place G1, G2 on a shared data cube of size d (overlapping positions), h on fresh variables
    d = max(g1[1], g2[1]) + int(rng.integers(0, 2))
    if h[1] + d > 13: continue
    p1 = list(rng.choice(d, size=g1[1], replace=False)); p2 = list(rng.choice(d, size=g2[1], replace=False))
    G1 = embed(g1[0], g1[1], d, p1); G2 = embed(g2[0], g2[1], d, p2)
    if int(np.dot(G1, G2)) != 0: continue
    n = h[1] + d
    Hx = embed(h[0], h[1], n, list(range(h[1])))
    Y1 = embed(G1, d, n, list(range(h[1], n))); Y2 = embed(G2, d, n, list(range(h[1], n)))
    F = np.where(Hx == 1, Y1, Y2)
    HF, IF = stats(F, n)
    assert abs(F.mean()) < 1e-12
    worst = max(worst, HF - 4*(IF - 1))
    Hh, _ = stats(h[0], h[1]); H1, _ = stats(G1, d); H2, _ = stats(G2, d)
    worst_two = max(worst_two, HF - (2 + Hh/2 + (H1 + H2)/2))
    count += 1
    # keep F only if it is small enough to reuse
    if n <= 7: pool.append((F, n))
print('members built', count, ' pool size', len(pool))
print('max H - 4(I-1) =', worst, '   max H - [2 + H(h)/2 + avg H(G)] =', worst_two)

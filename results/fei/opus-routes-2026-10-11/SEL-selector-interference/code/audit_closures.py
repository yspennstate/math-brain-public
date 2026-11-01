"""Second-path audit of the proved closure statements on random instances (exact influences, float entropies).
 A. SEL-7: H(F) <= 2H(p)+sum p_k[H(q_k)+H(G_k)];  I_sel = (1/4) sum I(h_k);  I_data = sum p_k I(G_k);
           H(F) <= max(C_s+6, C_g) I(F) with C_s = max H(h_k)/I(h_k), C_g = max H(G_k)/I(G_k).
 B. SEL-10: affine cells, delta = 1 - max correlation over adjacent distinct cells:
           I_sel >= (delta/2) sum p_j r_j  and  H(F) <= max(4/delta, C) I(F).
 C. SEL-12(b): decision-tree cells: cost <= K(delta/2) I_sel.
 D. SEL-2: random multiplexers: H(F) <= max(C, K(c)) I(F), c = I_sel/a.
"""
import numpy as np
from fractions import Fraction
from fei_lib import fwht_int, entropy_from_W, influence_from_W, coord_influences_from_W, fwht_float, entropy_probs
from affine_c1 import all_affine, random_affine_partition, codim

LN2 = np.log(2)
def h2(t):
    return 0.0 if t <= 0 or t >= 1 else float(-t*np.log2(t) - (1-t)*np.log2(1-t))
def K(c):
    c = min(max(c, 1e-300), 1.0)
    return min(2*h2(c)/c, h2(c)/c + 2/LN2)
def HI(t, n):
    W = fwht_int(t); return entropy_from_W(W, n), influence_from_W(W, n)
def build(lab, leaves, a, n):
    B = np.array([leaves[lab[b]] for b in range(1 << a)])
    return B.T.reshape(-1)
rng = np.random.default_rng(77)
fails = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
# ---- A
from t1_orthogonal import leaf_family, random_partition
for trial in range(400):
    a = int(rng.integers(1, 4)); n = int(rng.integers(2, 5)); m = int(rng.integers(2, min(1 << a, 1 << n) + 1))
    leaves = leaf_family('chi_shift' if trial % 2 else 'random', m, n, rng)
    if leaves is None: continue
    lab = random_partition(a, m, rng)
    F = build(lab, leaves, a, n); HF, IF = HI(F, a + n)
    W = fwht_int(F); inf = coord_influences_from_W(W, a + n)
    Isel = sum(inf[:a]); Idata = sum(inf[a:])
    p = [Fraction(int(np.sum(lab == k)), 1 << a) for k in range(m)]
    hk = [np.where(lab == k, -1, 1) for k in range(m)]
    Ih = [HI(h, a)[1] for h in hk]; Hh = [HI(h, a)[0] for h in hk]
    HG = [HI(g, n)[0] for g in leaves]; IG = [HI(g, n)[1] for g in leaves]
    ok = (Isel == sum(Ih) / 4) and (Idata == sum(pk*ig for pk, ig in zip(p, IG)))
    Cs = max((Hh[k]/float(Ih[k]) for k in range(m) if Ih[k] > 0), default=0)
    Cg = max((HG[k]/float(IG[k]) for k in range(m) if IG[k] > 0), default=0)
    ok = ok and HF <= max(Cs + 6, Cg) * float(IF) + 1e-9
    counts['A'] += 1; fails['A'] += (not ok)
# ---- B and C
aff3 = sorted(all_affine(3), key=lambda s: (len(s), sorted(s)))
for trial in range(400):
    a = 3; n = 3
    cells = random_affine_partition(a, rng, aff3, prefer_large=rng.random())
    m = len(cells)
    lab = np.empty(8, dtype=np.int64)
    for j, A in enumerate(cells):
        for pnt in A: lab[pnt] = j
    base = rng.choice([-1, 1], size=8)
    leaves = []
    for j in range(m):
        g = base.copy(); k = rng.integers(0, 4); idx = rng.choice(8, size=k, replace=False); g[idx] *= -1
        leaves.append(g * rng.choice([-1, 1]) if rng.random() < 0.2 else g)
    # delta over adjacent distinct cells
    corr = -1.0
    for x in range(8):
        for i in range(3):
            y = x ^ (1 << i)
            if lab[x] != lab[y]:
                corr = max(corr, float(np.mean(leaves[lab[x]] * leaves[lab[y]])))
    delta = 1 - corr
    if delta <= 1e-12: continue
    F = build(lab, leaves, a, n); HF, IF = HI(F, a + n)
    W = fwht_int(F); inf = coord_influences_from_W(W, a + n); Isel = float(sum(inf[:a]))
    # r_j: coordinates whose flip leaves the cell
    rsum = 0.0
    for j, A in enumerate(cells):
        rj = sum(1 for i in range(3) if any(lab[pnt ^ (1 << i)] != j for pnt in A))
        rsum += len(A)/8 * rj
    C = max((HI(g, n)[0]/float(HI(g, n)[1]) for g in leaves if HI(g, n)[1] > 0), default=0)
    okB = (Isel >= min(delta, 1.0)/2 * rsum - 1e-12) and (HF <= max(4/min(delta, 1.0), C) * float(IF) + 1e-9)
    counts['B'] += 1; fails['B'] += (not okB)
# decision-tree cells: cells of a random decision tree on 3 bits
def random_dt(vars_left, rng, depth=0):
    if not vars_left or rng.random() < 0.25 * depth:
        return None
    v = vars_left[rng.integers(len(vars_left))]
    rest = [u for u in vars_left if u != v]
    return (v, random_dt(rest, rng, depth + 1), random_dt(rest, rng, depth + 1))
def dt_label(tree, x, path=()):
    if tree is None: return path
    v, l, r = tree
    bit = (x >> v) & 1
    return dt_label(l if bit == 0 else r, x, path + ((v, bit),))
for trial in range(400):
    a = 3; n = 3
    tree = random_dt([0, 1, 2], rng)
    paths = sorted({dt_label(tree, x) for x in range(8)})
    lab = np.array([paths.index(dt_label(tree, x)) for x in range(8)])
    m = len(paths)
    base = rng.choice([-1, 1], size=8)
    leaves = []
    for j in range(m):
        g = base.copy(); k = rng.integers(0, 3); idx = rng.choice(8, size=k, replace=False); g[idx] *= -1; leaves.append(g)
    corr = -1.0
    for x in range(8):
        for i in range(3):
            y = x ^ (1 << i)
            if lab[x] != lab[y]: corr = max(corr, float(np.mean(leaves[lab[x]] * leaves[lab[y]])))
    delta = 1 - corr
    if m == 1 or delta <= 1e-12: continue
    F = build(lab, leaves, a, n); HF, IF = HI(F, a + n)
    W = fwht_int(F); inf = coord_influences_from_W(W, a + n); Isel = float(sum(inf[:a]))
    avgH = float(np.mean([HI(leaves[lab[b]], n)[0] for b in range(8)]))
    cost = HF - avgH
    okC = cost <= K(min(delta, 1.0)/2) * Isel + 1e-9
    counts['C'] += 1; fails['C'] += (not okC)
# ---- D
for trial in range(400):
    a = int(rng.integers(1, 4)); n = int(rng.integers(2, 5))
    base = rng.choice([-1, 1], size=1 << n)
    Bm = np.tile(base, (1 << a, 1)); Bm = np.where(rng.random(Bm.shape) < rng.random()*0.3, -Bm, Bm)
    F = Bm.T.reshape(-1); HF, IF = HI(F, a + n)
    W = fwht_int(F); inf = coord_influences_from_W(W, a + n); Isel = float(sum(inf[:a]))
    if Isel <= 0: continue
    C = max((HI(g, n)[0]/float(HI(g, n)[1]) for g in Bm if HI(g, n)[1] > 0), default=0)
    okD = HF <= max(C, K(Isel/a)) * float(IF) + 1e-9
    counts['D'] += 1; fails['D'] += (not okD)
print('instances:', counts); print('failures :', fails)

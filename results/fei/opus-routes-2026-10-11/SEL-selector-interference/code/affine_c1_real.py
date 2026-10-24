"""SEL-9 weighted form with REAL leaves of arbitrary norms: H(Fhat^2) <= H(w) + sum w_j c_j + sum w_j H(Lambda_j)."""
import numpy as np
from fei_lib import fwht_float, entropy_probs
from affine_c1 import all_affine, random_affine_partition, codim
rng = np.random.default_rng(31)
worst = -9
for a in (3, 4):
    aff = sorted(all_affine(a), key=lambda s: (len(s), sorted(s)))
    for trial in range(300 if a == 3 else 150):
        cells = random_affine_partition(a, rng, aff, prefer_large=rng.random())
        m = len(cells); n = 3; N = 1 << a
        leaves = [rng.standard_normal(1 << n) * (rng.random() ** 2) for _ in range(m)]
        lab = np.empty(N, dtype=np.int64)
        for j, A in enumerate(cells):
            for p in A: lab[p] = j
        Bm = np.array([leaves[lab[b]] for b in range(N)]); F = Bm.T.reshape(-1)
        F = F / np.sqrt(np.mean(F**2))
        sc = np.sqrt(np.mean(np.array([leaves[lab[b]] for b in range(N)])**2))
        lv = [g / sc for g in leaves]
        p = np.array([len(A)/N for A in cells]); c = np.array([codim(A, a) for A in cells])
        l = np.array([np.mean(g**2) for g in lv]); w = p*l
        Lam = [(fwht_float(g)/(1 << n))**2 / np.mean(g**2) for g in lv]
        rhs = entropy_probs(w) + np.sum(w*c) + sum(w[j]*entropy_probs(Lam[j]) for j in range(m))
        lhs = entropy_probs((fwht_float(F)/(1 << (a+n)))**2)
        worst = max(worst, lhs - rhs)
print('max lhs - rhs over real-leaf instances:', worst)

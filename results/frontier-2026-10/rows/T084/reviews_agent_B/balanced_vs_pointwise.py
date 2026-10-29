# T084, agent B: for random simple binary matroids on <= 8 elements: is the pointwise q-statement (all pairs) equivalent to
# being BALANCED (Feder-Mihail: every minor's uniform basis measure is pairwise negatively correlated)?
import numpy as np, itertools, json, sys
sys.path.insert(0, '.')
from binary_sweep import ranks, run
rng = np.random.default_rng(int(sys.argv[1])); n_it = int(sys.argv[2])
def balanced(rk, m):
    X = np.arange(1 << m); pc = np.array([bin(x).count('1') for x in X]); bits = ((X[:, None] >> np.arange(m)) & 1)
    for C in range(1 << m):
        rC = rk[C]; rest = ((1 << m) - 1) ^ C
        D = rest
        while True:                       # D ranges over subsets of rest
            E2 = rest ^ D
            if bin(E2).count('1') >= 2:
                sub = (X & ~E2) == 0      # subsets of the minor's ground set
                Rm = rk[E2 | C] - rC
                bas = sub & (rk[X | C] - rC == Rm) & (pc == Rm)
                Bm = bits[bas][:, [i for i in range(m) if (E2 >> i) & 1]]
                n = len(Bm)
                if n:
                    s = Bm.sum(0); P = Bm.T @ Bm
                    viol = n * P - np.outer(s, s); np.fill_diagonal(viol, -1)
                    if viol.max() > 0: return False, (C, D)
            if D == 0: break
            D = (D - 1) & rest
    return True, None
tab = {}; ex = []
for it in range(n_it):
    r = int(rng.integers(3, 5)); m = int(rng.integers(r + 3, min(2 ** r - 1, 8) + 1))
    pool = [v for v in range(1, 1 << r) if bin(v).count('1') >= 2]; rng.shuffle(pool)
    cols = [1 << i for i in range(r)] + pool[:m - r]
    rk = ranks(cols, m); bal, where = balanced(rk, m)
    pw = all(not bad for _, bad in run(cols))
    key = f'balanced={bal} pointwise={pw}'; tab[key] = tab.get(key, 0) + 1
    if bal != pw and len(ex) < 5: ex.append((cols, bal, pw, where))
print(json.dumps({'table': tab, 'mismatches': ex}))

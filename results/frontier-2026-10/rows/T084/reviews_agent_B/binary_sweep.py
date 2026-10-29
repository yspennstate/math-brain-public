# T084, agent B: random simple binary matroids [I_r | A]; for each pair: basis-balanced? pointwise q-statement holds?
# and if it fails, at which lam-level (0 = bases). Vectorised with np.add.at.
import numpy as np, itertools, json, sys
from scipy.signal import convolve2d
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def ranks(cols, m):
    out = np.zeros(1 << m, dtype=np.int64)
    for x in range(1 << m):
        piv = {}
        for i in range(m):
            if (x >> i) & 1:
                v = cols[i]
                while v:
                    t = v.bit_length() - 1
                    if t not in piv: piv[t] = v; break
                    v ^= piv[t]
        out[x] = len(piv)
    return out
def run(cols):
    m = len(cols); rk = ranks(cols, m); R = rk[-1]; k = R - rk
    X = np.arange(1 << m); pc = np.array([bin(x).count('1') for x in X]); res = []
    for e, f in itertools.combinations(range(m), 2):
        be, bf = (X >> e) & 1, (X >> f) & 1; Z = {}
        for a in (0, 1):
            for c in (0, 1):
                s = (be == a) & (bf == c); H = np.zeros((m - 1, R + 2), dtype=np.int64)
                np.add.at(H, (pc[s] - a - c, k[s]), 1); Z[(a, c)] = H
        N = convolve2d(Z[(1, 0)], Z[(0, 1)]).astype(np.int64) - convolve2d(Z[(0, 0)], Z[(1, 1)]).astype(np.int64)
        c1 = np.cumsum(N, axis=1); bad = np.nonzero((c1 < 0).any(axis=1))[0]
        bas = (k == 0) & (pc == R); n = bas.sum(); ne = (bas & (be == 1)).sum(); nf = (bas & (bf == 1)).sum(); nef = (bas & (be == 1) & (bf == 1)).sum()
        res.append((bool(n * nef > ne * nf), [int(b) - (2 * int(R) - 2) for b in bad]))
    return res
stats = {'matroids': 0, 'pairs': 0, 'unbal': 0, 'fail': 0, 'fail_balanced': 0, 'fail_unbal': 0, 'unbal_nofail': 0, 'fail_above_bottom_only': 0, 'examples': []}
for it in range(int(sys.argv[2]) if len(sys.argv) > 2 else 200):
    r = int(rng.integers(3, 6)); m = int(rng.integers(r + 3, min(2 ** r - 1, 10) + 1))
    pool = [v for v in range(1, 1 << r) if bin(v).count('1') >= 2]; rng.shuffle(pool)
    cols = [1 << i for i in range(r)] + pool[:m - r]
    res = run(cols); stats['matroids'] += 1
    for (unb, bad) in res:
        stats['pairs'] += 1; stats['unbal'] += unb
        if bad:
            stats['fail'] += 1
            if unb: stats['fail_unbal'] += 1
            else:
                stats['fail_balanced'] += 1
                if len(stats['examples']) < 5: stats['examples'].append((cols, bad))
            stats.setdefault('levels_rel_bases', []).append(bad) if len(stats.get('levels_rel_bases', [])) < 13 else None
            if 0 not in bad: stats['fail_above_bottom_only'] += 1
        elif unb: stats['unbal_nofail'] += 1
print(json.dumps(stats))

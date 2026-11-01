# T084, agent B: adversarial search for a negative N on regular matroids. Minimise N(w, q)/[Z10 Z01](w, q) over log-weights
# (box [-9, 5]) and logit q, Nelder-Mead from 40 random starts per pair class; all pairs. Control: the unbalanced binary 8-element matroid.
import numpy as np, itertools, sys, re
from scipy.optimize import minimize
sys.argv = ['x', '0', '0']
from binary_sweep import ranks
rng = np.random.default_rng(11)
def graph_cols(E): return [(1 << a) | (1 << b) for a, b in E]
def dual_rank(rk, m):
    R = rk[-1]; full = (1 << m) - 1; X = np.arange(1 << m); pc = np.array([bin(x).count('1') for x in X])
    return pc - R + rk[full ^ X]
def search(name, rk, m, starts=40, pairs=None):
    X = np.arange(1 << m); R = int(rk[-1]); k = (R - rk).astype(float); bits = ((X[:, None] >> np.arange(m)) & 1).astype(float)
    best = (np.inf, None)
    for e, f in (pairs or itertools.combinations(range(m), 2)):
        be, bf = (X >> e) & 1, (X >> f) & 1; S = {(a, c): (be == a) & (bf == c) for a in (0, 1) for c in (0, 1)}
        def obj(z):
            lw = np.clip(z[:m], -9, 5); lq = -np.logaddexp(0, -z[m]); L = bits @ lw + k * lq
            Z = {key: np.logaddexp.reduce(L[s]) for key, s in S.items()}
            return -np.expm1((Z[(0, 0)] + Z[(1, 1)]) - (Z[(1, 0)] + Z[(0, 1)]))
        for s in range(starts):
            z0 = np.concatenate([rng.uniform(-6, 3, m), [rng.uniform(-6, 4)]])
            r = minimize(obj, z0, method='Nelder-Mead', options={'maxiter': 3000, 'xatol': 1e-6, 'fatol': 1e-12})
            if r.fun < best[0]: best = (r.fun, (e, f, np.round(r.x, 2).tolist()))
    print(f'{name}: min N/(Z10 Z01) = {best[0]:.3e} at pair {best[1][:2]}', flush=True); return best
K5 = list(itertools.combinations(range(5), 2)); K33 = [(a, b) for a in range(3) for b in range(3, 6)]
A8 = [(13726 >> (4 * c)) & 15 for c in range(4)]
search('control: unbalanced binary 8, bad pair', ranks([1, 2, 4, 8] + A8, 8), 8, pairs=[(0, 4)])
A = [0b11001, 0b11100, 0b01110, 0b00111, 0b10011]
colsR10 = [1 << i for i in range(5)] + [sum(((A[row] >> (4 - c)) & 1) << row for row in range(5)) for c in range(5)]
search('R10 (transitive: pairs (0,1) and (0,5) up to symmetry checked by all pairs)', ranks(colsR10, 10), 10, starts=8)
rk5 = ranks(graph_cols(K5), 10); search('M*(K5)', dual_rank(rk5, 10), 10, starts=8, pairs=[(0, 1), (0, 9)])
rk33 = ranks(graph_cols(K33), 9); search('M*(K3,3)', dual_rank(rk33, 9), 9, starts=8, pairs=[(0, 1), (0, 4)])
search('M(K5)', rk5, 10, starts=8, pairs=[(0, 1), (0, 9)])

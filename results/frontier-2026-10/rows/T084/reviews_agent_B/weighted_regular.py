# T084, agent B: weighted version. Edge weights w_e (log-uniform in [1e-2, 1e2]); Z_ab(q) = sum_{A: e in A iff a, f in A iff b}
# prod_{g in A} w_g q^{corank(A)}. N(q) = Z10 Z01 - Z00 Z11 (polynomial in q). Checks: (i) N(q) >= 0 on q in (0,1) (the conjecture's
# matroid analogue), (ii) the partial sums of N's q-coefficients >= 0 (pointwise, levels merged). Relative tolerance 1e-9.
import numpy as np, itertools, json, sys
sys.argv = ['x', '0', '0']
from binary_sweep import ranks
rng = np.random.default_rng(5)
def graph_cols(E): return [(1 << a) | (1 << b) for a, b in E]
def dual_rank(rk, m):
    R = rk[-1]; full = (1 << m) - 1; X = np.arange(1 << m); pc = np.array([bin(x).count('1') for x in X])
    return pc - R + rk[full ^ X]
def test(name, rk, m, trials=600, pair=None):
    X = np.arange(1 << m); R = rk[-1]; k = R - rk; bits = ((X[:, None] >> np.arange(m)) & 1).astype(float)
    qs = np.linspace(0.001, 0.999, 400); f1 = f2 = 0; worst = 0.0
    for t in range(trials):
        w = np.exp(rng.uniform(np.log(1e-3), np.log(1e1)) + rng.uniform(-1.5, 1.5, m)); W = np.exp(bits @ np.log(w))
        e, f = pair if pair else sorted(rng.choice(m, 2, replace=False)); be, bf = (X >> e) & 1, (X >> f) & 1; P = {}
        for a in (0, 1):
            for c in (0, 1):
                s = (be == a) & (bf == c); P[(a, c)] = np.bincount(k[s], weights=W[s], minlength=R + 1)
        N = np.convolve(P[(1, 0)], P[(0, 1)]) - np.convolve(P[(0, 0)], P[(1, 1)])
        scale = np.convolve(P[(1, 0)], P[(0, 1)]).sum()
        val = np.polyval(N[::-1], qs) / scale; cs = np.cumsum(N) / scale
        if val.min() < -1e-9: f1 += 1; worst = min(worst, val.min())
        if cs.min() < -1e-9: f2 += 1
    print(f'{name}: trials {trials} N<0 somewhere on (0,1): {f1}  partial-sum fails: {f2}  worst N/scale {worst:.2e}', flush=True)
K4 = list(itertools.combinations(range(4), 2)); K5 = list(itertools.combinations(range(5), 2)); K33 = [(a, b) for a in range(3) for b in range(3, 6)]
for nm, E in (('M(K4)', K4), ('M(K5)', K5), ('M(K3,3)', K33)):
    rk = ranks(graph_cols(E), len(E)); test(nm, rk, len(E)); test(nm.replace('M(', 'M*('), dual_rank(rk, len(E)), len(E))
A = [0b11001, 0b11100, 0b01110, 0b00111, 0b10011]
colsR10 = [1 << i for i in range(5)] + [sum(((A[row] >> (4 - c)) & 1) << row for row in range(5)) for c in range(5)]
test('R10', ranks(colsR10, 10), 10)
A8 = [(13726 >> (4 * c)) & 15 for c in range(4)]; test('unbalanced binary 8, its bad pair (control)', ranks([1, 2, 4, 8] + A8, 8), 8, pair=(0, 4))
F7 = [1, 2, 4, 3, 5, 6, 7]; test('F7', ranks(F7, 7), 7); test('F7*', dual_rank(ranks(F7, 7), 7), 7)

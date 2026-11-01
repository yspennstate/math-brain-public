# T084, agent B: the pointwise q-statement with k(A) replaced by the corank r(E) - r(A), on regular matroids that are not
# graphic: M*(K5), M*(K3,3), R10; and on M(K5), M(K3,3) as controls. N = Z10 Z01 - Z00 Z11 as a polynomial in (lam, q);
# pointwise = every first partial sum in q of every lam-level is >= 0.
import numpy as np, itertools
from scipy.signal import convolve2d
def rk_binary(cols):
    def r(mask):
        piv = {}
        for i, v in enumerate(cols):
            if not (mask >> i) & 1: continue
            while v:
                t = v.bit_length() - 1
                if t not in piv: piv[t] = v; break
                v ^= piv[t]
        return len(piv)
    return r
def graph_cols(n, edges): return [(1 << a) | (1 << b) for a, b in edges]
def test(m, r, name):
    R = r((1 << m) - 1); full = (1 << m) - 1
    k = [R - r(x) for x in range(1 << m)]
    fails1 = fails2 = 0; worst = None
    for e, f in itertools.combinations(range(m), 2):
        Z = {}
        for a in (0, 1):
            for c in (0, 1):
                H = np.zeros((m - 1, R + 2), dtype=np.int64)
                for x in range(1 << m):
                    if ((x >> e) & 1) == a and ((x >> f) & 1) == c: H[bin(x).count('1') - a - c, k[x]] += 1
                Z[(a, c)] = H
        N = convolve2d(Z[(1, 0)], Z[(0, 1)]).astype(np.int64) - convolve2d(Z[(0, 0)], Z[(1, 1)]).astype(np.int64)
        c1 = np.cumsum(N, axis=1); c2 = np.cumsum(c1, axis=1)
        if c1.min() < 0: fails1 += 1; worst = (e, f, int(c1.min()), np.unravel_index(int(c1.argmin()), c1.shape))
        if c2.min() < 0: fails2 += 1
    print(f'{name}: m {m} rank {R} pairs {m*(m-1)//2} pointwise fails {fails1} second-order fails {fails2} worst {worst}', flush=True)
def dual(m, r):
    R = r((1 << m) - 1); full = (1 << m) - 1
    return lambda x: bin(x).count('1') - R + r(full ^ x)
K5 = list(itertools.combinations(range(5), 2)); K33 = [(a, b) for a in range(3) for b in range(3, 6)]
for nm, E in (('M(K5)', K5), ('M(K3,3)', K33)):
    r = rk_binary(graph_cols(6, E)); test(len(E), r, nm); test(len(E), dual(len(E), r), nm.replace('M(', 'M*('))
A = [0b11001, 0b11100, 0b01110, 0b00111, 0b10011]
colsR10 = [1 << i for i in range(5)] + [sum(((A[row] >> (4 - c)) & 1) << row for row in range(5)) for c in range(5)]
test(10, rk_binary(colsR10), 'R10')

# T084, agent B: is the pointwise q-statement purely matroidal? Replace k(A) by r(E) - r(A) and test binary matroids with a
# pair that is positively correlated for uniform bases (S8-type, Seymour-Welsh). The bottom lam-level is the basis Rayleigh pair.
import numpy as np, itertools, json
def rank2(cols):
    piv = {}
    for v in cols:
        while v:
            t = v.bit_length() - 1
            if t not in piv: piv[t] = v; break
            v ^= piv[t]
    return len(piv)
def test(M, name):
    m = M.shape[1]; cols = [int(''.join(map(str, c)), 2) for c in zip(*M)]
    R = rank2(cols); k = [R - rank2([cols[i] for i in range(m) if (x >> i) & 1]) for x in range(1 << m)]
    nb = lambda cond: sum(1 for x in range(1 << m) if k[x] == 0 and bin(x).count('1') == R and cond(x))
    out = []
    for e, f in itertools.combinations(range(m), 2):
        E, F = 1 << e, 1 << f
        b, be, bf, bef = nb(lambda x: 1), nb(lambda x: x & E), nb(lambda x: x & F), nb(lambda x: x & E and x & F)
        Z = {}
        for a in (0, 1):
            for c in (0, 1):
                H = np.zeros((m - 1, R + 2), dtype=np.int64)
                for x in range(1 << m):
                    if ((x >> e) & 1) == a and ((x >> f) & 1) == c: H[bin(x).count('1') - a - c, k[x]] += 1
                Z[(a, c)] = H
        from scipy.signal import convolve2d
        N = convolve2d(Z[(1, 0)], Z[(0, 1)]).astype(np.int64) - convolve2d(Z[(0, 0)], Z[(1, 1)]).astype(np.int64)
        p1 = min(int(x) for s in range(N.shape[0]) for x in np.cumsum(N[s]))
        p2 = min(int(x) for s in range(N.shape[0]) for x in np.cumsum(np.cumsum(N[s])))
        out.append((e, f, be * bf - b * bef, p1, p2))
    pos = [o for o in out if o[2] < 0]
    print(name, 'pairs', len(out), 'basis-positively-correlated', len(pos), 'pointwise fails', sum(o[3] < 0 for o in out), 'second-order fails', sum(o[4] < 0 for o in out))
    for o in pos[:3]: print('  ', o)
I4 = np.eye(4, dtype=int)
cands = {'S8?': [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,1]], 'AG32': [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]], 'F7*+': [[1,1,0,1],[1,0,1,1],[0,1,1,1],[0,0,0,1]]}
for nm, A in cands.items(): test(np.hstack([I4, np.array(A)]), nm)
def from_code(code):
    A = [(code >> (4 * c)) & 15 for c in range(4)]
    M = np.zeros((4, 8), dtype=int)
    for i in range(4): M[3 - i, i] = 1
    for c in range(4):
        for r in range(4): M[3 - r, 4 + c] = (A[c] >> r) & 1
    return M
for code in (13726, 13801): test(from_code(code), f'unbalanced {code}')

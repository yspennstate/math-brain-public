import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np, itertools, numba as nb

@nb.njit(cache=True)
def is_aut(c0, perm, m, neg, comp):
    N = 1 << m
    full = N - 1
    for x in range(N):
        y = 0
        for i in range(m):
            if (x >> i) & 1:
                y |= 1 << perm[i]
        if comp:
            y ^= full
        v = c0[x]
        if neg:
            v = -v
        if c0[y] != v:
            return False
    return True

def aut_group(c0, m, allow_dual=True):
    auts = []
    for perm in itertools.permutations(range(m)):
        p = np.array(perm, dtype=np.int64)
        if is_aut(c0, p, m, False, False):
            auts.append((perm, 'plain'))
        if allow_dual and is_aut(c0, p, m, True, True):
            auts.append((perm, 'dual'))
    return auts

if __name__ == '__main__':
    c0 = np.load('../logs/numaro_core_c0.npy').astype(np.int64)
    A = aut_group(c0, 9)
    print('automorphisms (perm, type):', len(A), ' plain:', sum(1 for a in A if a[1]=='plain'), ' dual (x->~x, c->-c):', sum(1 for a in A if a[1]=='dual'))
    print(A[:5])

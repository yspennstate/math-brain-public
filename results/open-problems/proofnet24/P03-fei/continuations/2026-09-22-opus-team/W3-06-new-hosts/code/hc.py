"""Core-with-coins evaluator (float64, numba) with the optimal coin grouping.

A core is c0 : {0,1}^m -> {-1,0,+1} (index x, bit i = core variable i; -1 = TRUE, +1 = FALSE, 0 = hole), sum c0 = 0.
Holes are filled by fresh uniform coins.  By the formulas of F2 Section 1 (proved there):
    a singleton hole group carries entropy 2m/N and adds (m+2)/(2N) to I,
    a group of two cells carries entropy 4(m-1)/N and adds ((m+2)*2 - 2e)/(2N) to I (e = 1 if the cells are
    cube-adjacent, else 0),
    larger groups lose (e.g. a 3-path loses 3.17/N entropy for 1/N influence, a 2-face 8/N for 2/N).
For a target ratio above 4 the best grouping is therefore a MAXIMUM MATCHING of the hole-induced subgraph of Q_m
(each matched adjacent pair: -4/N entropy, -1/N influence against two singletons), the rest singletons.  Non-adjacent
pairs are dominated by singletons (same influence, 4/N less entropy).
    H = sum_S phi(W0(S)/N) + (2m h - 4M)/N
    I = [ sum_{cube edges xy} (c0(x)-c0(y))^2 + (m+2) h - 2M ] / (2N)
h = number of holes, M = maximum matching size.
"""
import numpy as np
import numba as nb

try:
    import psutil
    _p = psutil.Process()
    _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
except Exception:
    pass


@nb.njit(cache=True)
def fwht(a):
    a = a.astype(np.int64).copy()
    n = a.shape[0]
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x = a[j]; y = a[j + h]
                a[j] = x + y; a[j + h] = x - y
        h *= 2
    return a


def phi_table(N):
    v = np.arange(N + 1, dtype=np.float64)
    p = (v / N) ** 2
    t = np.zeros(N + 1)
    t[1:] = -p[1:] * np.log2(p[1:])
    return t


@nb.njit(cache=True)
def dirichlet(c0, m):
    N = c0.shape[0]
    s = 0
    for x in range(N):
        for i in range(m):
            y = x ^ (1 << i)
            if y > x:
                d = c0[x] - c0[y]
                s += d * d
    return s


@nb.njit(cache=True)
def popc(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


@nb.njit(cache=True)
def hole_matching(c0, m):
    """Maximum matching in the subgraph of Q_m induced by the holes (Hopcroft-Karp style with BFS layering,
    implemented as repeated DFS augmentation from free even-parity holes; Q_m is bipartite by parity).
    Returns (M, mate) with mate[x] = partner or -1."""
    N = c0.shape[0]
    mate = -np.ones(N, dtype=np.int64)
    # list of even holes
    ev = np.empty(N, dtype=np.int64)
    ne = 0
    for x in range(N):
        if c0[x] == 0 and (popc(x) & 1) == 0:
            ev[ne] = x
            ne += 1
    # greedy init
    M = 0
    for a in range(ne):
        x = ev[a]
        for i in range(m):
            y = x ^ (1 << i)
            if c0[y] == 0 and mate[y] < 0:
                mate[x] = y; mate[y] = x; M += 1
                break
    # augmenting paths (Kuhn with visited stamps)
    visited = np.zeros(N, dtype=np.int64)
    stamp = 0
    stack_x = np.empty(N, dtype=np.int64)
    stack_i = np.empty(N, dtype=np.int64)
    parent = -np.ones(N, dtype=np.int64)
    improved = True
    while improved:
        improved = False
        for a in range(ne):
            s = ev[a]
            if mate[s] >= 0:
                continue
            stamp += 1
            # iterative DFS over even vertices; from even x try odd neighbours y
            top = 0
            stack_x[0] = s; stack_i[0] = 0; visited[s] = stamp; parent[s] = -1
            found = -1
            while top >= 0:
                x = stack_x[top]
                i = stack_i[top]
                if i >= m:
                    top -= 1
                    continue
                stack_i[top] = i + 1
                y = x ^ (1 << i)
                if c0[y] != 0 or visited[y] == stamp:
                    continue
                visited[y] = stamp
                if mate[y] < 0:
                    # augment along the stack
                    found = y
                    # path: s=stack_x[0] -> y0 -> mate(y0)=stack_x[1] -> ... -> stack_x[top] -> y
                    yy = y
                    for t in range(top, -1, -1):
                        xx = stack_x[t]
                        nxt = mate[xx]
                        mate[xx] = yy; mate[yy] = xx
                        yy = nxt
                    M += 1
                    improved = True
                    break
                else:
                    z = mate[y]
                    if visited[z] != stamp:
                        visited[z] = stamp
                        top += 1
                        stack_x[top] = z; stack_i[top] = 0
    return M, mate


@nb.njit(cache=True)
def evaluate_nb(c0, m, phi):
    N = c0.shape[0]
    W = fwht(c0)
    Hc = 0.0
    for S in range(N):
        v = W[S]
        if v < 0:
            v = -v
        Hc += phi[v]
    D = dirichlet(c0, m)
    h = 0
    for x in range(N):
        if c0[x] == 0:
            h += 1
    M, mate = hole_matching(c0, m)
    H = Hc + (2.0 * m * h - 4.0 * M) / N
    I = (D + (m + 2) * h - 2 * M) / (2.0 * N)
    return H, I, Hc, D, h, M


def evaluate(c0, m, phi=None):
    c0 = np.asarray(c0, dtype=np.int64)
    N = 1 << m
    if phi is None:
        phi = phi_table(N)
    H, I, Hc, D, h, M = evaluate_nb(c0, m, phi)
    bal = int(c0.sum())
    R = H / (I - 1.0) if I > 1 else float('nan')
    return dict(H=H, I=I, R=R, Hc=Hc, D=int(D), holes=int(h), pairs=int(M), singles=int(h - 2 * M),
                nvars=m + int(h - M), balance=bal)


def groups_from_matching(c0, m):
    c0 = np.asarray(c0, dtype=np.int64)
    M, mate = hole_matching(c0, m)
    groups = []
    seen = set()
    for x in range(len(c0)):
        if c0[x] == 0 and x not in seen:
            if mate[x] >= 0:
                groups.append([int(x), int(mate[x])]); seen.add(x); seen.add(int(mate[x]))
            else:
                groups.append([int(x)]); seen.add(x)
    return groups


def core_string(c0):
    return ''.join({1: '+', -1: '-', 0: '0'}[int(v)] for v in c0)


if __name__ == '__main__':
    import os, time
    base = os.path.dirname(os.path.abspath(__file__))
    c = np.load(os.path.join(base, '..', '..', 'F2-new-gates', 'logs', 'numaro_core_c0.npy')).astype(np.int64)
    t = time.time()
    print(evaluate(c, 9), time.time() - t)

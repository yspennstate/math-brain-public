"""
HARD10-02 reproducible certificate for the 2026-09-15T14:35:47Z report.

Contents
--------
1. Exact rational implementation of the edgewise first-crossing formula
   for the first derivative at c=1.
2. Exhaustive exact check of all connected labeled simple graphs on six
   vertices, root=0, target=5, every non-target root-neighbor start.
3. Numerical square-annulus experiment using the closed Green formula.

No floating-point sign decision is used in the n=6 certificate.
The square-annulus table is numerical evidence only.
"""

from fractions import Fraction as F
from itertools import combinations
import math


def solve_frac(A, b):
    n = len(b)
    if n == 0:
        return []
    M = [[F(A[i][j]) for j in range(n)] + [F(b[i])] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col])
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
        p = M[col][col]
        if p != 1:
            for j in range(col, n + 1):
                M[col][j] /= p
        for r in range(n):
            if r == col:
                continue
            q = M[r][col]
            if q:
                for j in range(col, n + 1):
                    M[r][j] -= q * M[col][j]
    return [M[i][-1] for i in range(n)]


def connected(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def exact_graph_Ds(n, edges, root=0, target=None):
    """Return D and h(start) for every admissible root-neighbor start.

    Formula: for each fresh edge e={u,v}, orient as stored, solve
        A_e q_e = 1_u - 1_v
    on the interior, where A_e keeps original degree diagonals but removes
    the off-diagonal continuation across e. Then
        D = sum_{e != initial old edge} (h(v)-h(u))*q_e(start).
    """
    if target is None:
        target = n - 1

    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
    deg = [len(adj[v]) for v in range(n)]
    interior = [v for v in range(n) if v not in (root, target)]
    ix = {v: i for i, v in enumerate(interior)}
    mI = len(interior)

    # SRW equilibrium voltage h, target value 1 and root value 0.
    L = [[0] * mI for _ in range(mI)]
    rhs = [0] * mI
    for z in interior:
        L[ix[z]][ix[z]] = deg[z]
    for u, v in edges:
        if u in ix and v in ix:
            L[ix[u]][ix[v]] -= 1
            L[ix[v]][ix[u]] -= 1
        elif u in ix and v == target:
            rhs[ix[u]] += 1
        elif v in ix and u == target:
            rhs[ix[v]] += 1
    hs = solve_frac(L, rhs)
    h = {root: F(0), target: F(1)}
    for v in interior:
        h[v] = hs[ix[v]]

    # q_e vector for every edge, exact first-crossing orientation bias.
    qvec = {}
    for ei, (u, v) in enumerate(edges):
        Ae = [[0] * mI for _ in range(mI)]
        br = [0] * mI
        for z in interior:
            Ae[ix[z]][ix[z]] = deg[z]
        for fj, (p, q) in enumerate(edges):
            if fj == ei:
                continue
            if p in ix and q in ix:
                Ae[ix[p]][ix[q]] -= 1
                Ae[ix[q]][ix[p]] -= 1
        if u in ix:
            br[ix[u]] += 1
        if v in ix:
            br[ix[v]] -= 1
        qvec[ei] = solve_frac(Ae, br)

    eidx = {e: i for i, e in enumerate(edges)}
    out = {}
    for s in range(1, n - 1):
        if (0, s) not in eidx:
            continue
        initial = eidx[(0, s)]
        total = F(0)
        for ei, (u, v) in enumerate(edges):
            if ei == initial:
                continue
            total += (h[v] - h[u]) * qvec[ei][ix[s]]
        out[s] = (total, h[s])
    return out


def exhaustive_n6():
    n = 6
    all_edges = list(combinations(range(n), 2))
    graphs = cases = zeros = 0
    minpos = None
    by_m = {}

    for mask in range(1, 1 << len(all_edges)):
        edges = [all_edges[i] for i in range(len(all_edges)) if (mask >> i) & 1]
        if not connected(n, edges):
            continue
        graphs += 1
        out = exact_graph_Ds(n, edges)
        m = len(edges)
        row = by_m.setdefault(m, [0, 0, 0, None])
        row[0] += 1

        for s, (D, hs) in out.items():
            cases += 1
            row[1] += 1
            if D < 0:
                raise AssertionError(("negative D", D, edges, s, hs))
            if D == 0:
                zeros += 1
                row[2] += 1
            else:
                if minpos is None or D < minpos[0]:
                    minpos = (D, edges, s, hs)
                if row[3] is None or D < row[3]:
                    row[3] = D

    assert graphs == 26704
    assert cases == 57120
    assert zeros == 5808
    assert minpos[0] == F(574, 18785)

    print("EXACT n=6 CERTIFICATE PASSED")
    print("connected graphs:", graphs)
    print("root-neighbor cases:", cases)
    print("zero D cases:", zeros)
    print("minimum positive:", minpos)
    print("by edge count:")
    for m in sorted(by_m):
        print(m, by_m[m])


def square_annulus_table(max_R=25):
    """Numerical Green-kernel experiment; requires numpy.

    Domain: [-R,R]^2, root=(0,0), outer square boundary absorbing,
    start=(1,0), root-start edge excluded as initially old.
    """
    import numpy as np

    def one_R(R):
        vertices = [(i, j) for i in range(-R, R + 1) for j in range(-R, R + 1)]
        root = (0, 0)
        boundary = {v for v in vertices if max(abs(v[0]), abs(v[1])) == R}
        interior = [v for v in vertices if v != root and v not in boundary]
        ix = {v: k for k, v in enumerate(interior)}
        n = len(interior)
        L = np.zeros((n, n))
        sB = np.zeros(n)
        nbrs = [(1,0),(-1,0),(0,1),(0,-1)]
        for v in interior:
            i = ix[v]
            L[i, i] = 4.0
            for d in nbrs:
                w = (v[0] + d[0], v[1] + d[1])
                if w in ix:
                    L[i, ix[w]] -= 1.0
                elif w in boundary:
                    sB[i] += 1.0
        hvec = np.linalg.solve(L, sB)
        G = np.linalg.inv(L)
        start = (1, 0)
        sx = ix[start]

        def h(v):
            if v == root:
                return 0.0
            if v in boundary:
                return 1.0
            return hvec[ix[v]]

        D = 0.0
        seen = set()
        for v in interior:
            for d in nbrs:
                w = (v[0] + d[0], v[1] + d[1])
                e = tuple(sorted((v, w)))
                if e in seen:
                    continue
                seen.add(e)
                if set(e) == set((root, start)):
                    continue

                if w in ix:
                    u = v
                    A = G[ix[u], ix[u]]
                    B = G[ix[w], ix[w]]
                    C = G[ix[u], ix[w]]
                    X = G[sx, ix[u]]
                    Y = G[sx, ix[w]]
                    den = (1.0 + C) ** 2 - A * B
                    q = ((1.0 + C + B) * X - (1.0 + C + A) * Y) / den
                    D += (h(w) - h(u)) * q
                elif w == root or w in boundary:
                    # Boundary edge: q = G(start, v), orientation v -> w.
                    q = G[sx, ix[v]]
                    D += (h(w) - h(v)) * q

        return n, hvec[sx], D

    print("R interior h_start D D/h")
    selected = {2,5,10,15,20,25}
    for R in range(2, max_R + 1):
        if R not in selected and R != max_R:
            continue
        n, hs, D = one_R(R)
        print(R, n, hs, D, D / hs)


if __name__ == "__main__":
    exhaustive_n6()
    square_annulus_table(25)

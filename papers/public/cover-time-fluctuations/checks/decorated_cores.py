"""Exact checks for Section 9 (decorated cores) and the two-vertex core of Section 10.

For each core F in a list of small graphs and each k in 1..4 (and several unequal
leaf-count vectors), the decorated graph is built explicitly and all discrete
hitting times are solved exactly. The core quantities T_F (rate-one-per-edge
continuous chain) and H_F (discrete walk) are solved from their own Dirichlet
systems. Then (9.1), (9.2), (9.3), (9.11) and t_hit(D_k) = 6k+3 are compared.
The Moore-Penrose pseudoinverse of the two-vertex Laplacian is checked exactly,
and the pseudoinverse of every core is checked against the four Penrose equations.
"""
from fractions import Fraction as Fr
import itertools

from clique_star_exact import solve_linear, hitting_times


def laplacian(q, edges):
    L = [[Fr(0)] * q for _ in range(q)]
    for a, b in edges:
        L[a][a] += 1; L[b][b] += 1; L[a][b] -= 1; L[b][a] -= 1
    return L


def dirichlet(q, edges, target, rhs):
    """Solve (L h)_u = rhs[u] for u != target, h_target = 0."""
    L = laplacian(q, edges)
    others = [u for u in range(q) if u != target]
    A = [[L[u][w] for w in others] for u in others]
    b = [rhs[u] for u in others]
    sol = solve_linear(A, b)
    h = [Fr(0)] * q
    for i, u in enumerate(others):
        h[u] = sol[i]
    return h


def decorate(q, edges, kv):
    """Core vertices 0..q-1; leaf (v, i) for i < kv[v]."""
    V = list(range(q)) + [(v, i) for v in range(q) for i in range(kv[v])]
    adj = {x: set() for x in V}
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    for v in range(q):
        for i in range(kv[v]):
            adj[v].add((v, i)); adj[(v, i)].add(v)
    return V, adj


def matmul(A, B):
    return [[sum(A[i][l] * B[l][j] for l in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def pseudoinverse(L):
    """Moore-Penrose inverse of a Laplacian of a connected graph: (L + J/q)^{-1} - J/q."""
    q = len(L)
    J = [[Fr(1, q)] * q for _ in range(q)]
    M = [[L[i][j] + J[i][j] for j in range(q)] for i in range(q)]
    # invert M by solving q systems
    inv = [[Fr(0)] * q for _ in range(q)]
    for col in range(q):
        e = [Fr(1) if i == col else Fr(0) for i in range(q)]
        x = solve_linear([row[:] for row in M], e)
        for i in range(q):
            inv[i][col] = x[i]
    return [[inv[i][j] - J[i][j] for j in range(q)] for i in range(q)]


CORES = {
    'edge': (2, [(0, 1)]),
    'path3': (3, [(0, 1), (1, 2)]),
    'triangle': (3, [(0, 1), (1, 2), (0, 2)]),
    'path4': (4, [(0, 1), (1, 2), (2, 3)]),
    'star3': (4, [(0, 1), (0, 2), (0, 3)]),
    'cycle4': (4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
    'K4': (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]),
    'paw': (4, [(0, 1), (1, 2), (0, 2), (2, 3)]),
    'cycle5': (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]),
}


def check_core(name, q, edges, kv):
    e = len(edges)
    V, adj = decorate(q, edges, kv)
    K = sum(kv)
    # core quantities
    TF = {}; HF = {}; Tk = {}
    for v in range(q):
        deg = [sum(1 for a, b in edges if v2 in (a, b)) for v2 in range(q)]
        TF[v] = dirichlet(q, edges, v, [Fr(1)] * q)
        HF[v] = dirichlet(q, edges, v, [Fr(d) for d in deg])
        Tk[v] = dirichlet(q, edges, v, [Fr(kv[u]) for u in range(q)])
    thit = Fr(0)
    for target in V:
        H = hitting_times(V, adj, target)
        thit = max(thit, max(H.values()))
        if isinstance(target, int):
            v = target
            for u in range(q):
                assert H[u] == 2 * Tk[v][u] + HF[v][u], (name, kv, 'core target', u, v)
            for (u, i) in [x for x in V if not isinstance(x, int)]:
                assert H[(u, i)] == 1 + H[u]
        else:
            v, _ = target
            for u in range(q):
                # (9.1) generalised: h_u = 2K + 2e - 1 + 2 T_k(u,v) + H_F(u,v)
                assert H[u] == 2 * K + 2 * e - 1 + 2 * Tk[v][u] + HF[v][u], (name, kv, 'leaf target', u, v)
            for (u, i) in [x for x in V if not isinstance(x, int)]:
                if (u, i) != target:
                    assert H[(u, i)] == 1 + H[u]
    # (9.3)/(9.11)
    m = max(2 * Tk[v][u] + HF[v][u] for u in range(q) for v in range(q))
    assert thit == 2 * K + 2 * e + m, (name, kv, thit, 2 * K + 2 * e + m)
    return thit


def main():
    print("== pseudoinverse of the two-vertex Laplacian")
    L = laplacian(2, [(0, 1)])
    Lp = pseudoinverse(L)
    assert Lp == [[Fr(1, 4), Fr(-1, 4)], [Fr(-1, 4), Fr(1, 4)]]
    print("   L^+ = (1/4) [[1,-1],[-1,1]]  ok")
    print("== Penrose equations for L^+ of every core")
    for name, (q, edges) in CORES.items():
        L = laplacian(q, edges); Lp = pseudoinverse(L)
        assert matmul(matmul(L, Lp), L) == L and matmul(matmul(Lp, L), Lp) == Lp
        LLp = matmul(L, Lp); LpL = matmul(Lp, L)
        assert LLp == [list(r) for r in zip(*LLp)] and LpL == [list(r) for r in zip(*LpL)]
        assert all(sum(row) == 0 for row in Lp)
        print(f"   {name}: L L+ L = L, L+ L L+ = L+, both products symmetric, L+ 1 = 0  ok")
    print("== (9.1)-(9.3): equal decorations, k = 1..4")
    for name, (q, edges) in CORES.items():
        for kk in range(1, 5):
            th = check_core(name, q, edges, [kk] * q)
        print(f"   {name}: (9.1), (9.2), leaf-start rule and (9.3) hold for k = 1..4; t_hit at k=4 is {th}")
    print("== (9.11): unequal decorations")
    for name, (q, edges) in CORES.items():
        for kv in itertools.product([1, 2, 3], repeat=q):
            check_core(name, q, edges, list(kv))
        print(f"   {name}: (9.11) and the generalised (9.1) hold for all leaf vectors in {{1,2,3}}^{q}")
    print("== double star: t_hit(D_k) = 6k + 3 for k = 1..25")
    for kk in range(1, 26):
        th = check_core('edge', 2, [(0, 1)], [kk, kk])
        assert th == 6 * kk + 3, (kk, th)
    print("   ok")
    print("== path3 core closed forms: t_hit(P3^(k)) = 12k + 8, H(a, c) = 6k + 4")
    for kk in range(1, 8):
        q, edges = CORES['path3']
        V, adj = decorate(q, edges, [kk] * 3)
        H = hitting_times(V, adj, 2)
        assert H[0] == 6 * kk + 4
        assert check_core('path3', q, edges, [kk] * 3) == 12 * kk + 8
    print("   ok")
    print("DECORATED_CORE_CHECKS_PASS")


if __name__ == '__main__':
    main()

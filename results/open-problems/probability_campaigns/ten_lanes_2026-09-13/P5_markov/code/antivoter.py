"""Antivoter model: exact stationary variance of the spin sum.

Two independent routes, used to check each other.

Route A (brute force): build the 2^n-state antivoter transition matrix on the
2^n - 2 non-constant configurations, solve for the stationary law exactly over
the rationals, and read off Var(sum of spins) and every pair correlation.

Route B (duality): E[X_i X_j] = E[(-1)^{tau_ij}] where tau_ij is the number of
steps taken by the annihilating pair walk started at {i,j}.  This gives a linear
system in C(n,2) unknowns:
    g(i,j) = -(1/(2r)) [ sum_{k~i} g(k,j) + sum_{l~j} g(i,l) ],   g(x,x) := 1.
"""
from fractions import Fraction as F
import itertools, sys

def solve_exact(A, b):
    """Gaussian elimination over Fraction. A is list of lists, b list."""
    m = len(A); n = len(A[0])
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    piv = []
    r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if M[i][c] != 0:
                p = i; break
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * bb for a, bb in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == m: break
    x = [F(0)] * n
    for i, c in enumerate(piv):
        x[c] = M[i][n]
    return x

# ---------------- Route B ----------------
def pair_correlations(adj):
    """adj: list of sets. Returns dict {(i,j): Fraction} for i<j, = E[X_i X_j]."""
    n = len(adj)
    r = len(adj[0])
    assert all(len(a) == r for a in adj), "not regular"
    idx = {}
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            idx[(i, j)] = len(pairs); pairs.append((i, j))
    N = len(pairs)
    def key(a, b):
        return (a, b) if a < b else (b, a)
    A = [[F(0)] * N for _ in range(N)]
    bvec = [F(0)] * N
    c = F(1, 2 * r)
    for t, (i, j) in enumerate(pairs):
        A[t][t] += 1
        # g(i,j) + c*sum_{k~i} g(k,j) + c*sum_{l~j} g(i,l) = -c*(#absorbing terms)
        for k in adj[i]:
            if k == j:
                bvec[t] -= c            # g(j,j)=1 moves to RHS
            else:
                A[t][idx[key(k, j)]] += c
        for l in adj[j]:
            if l == i:
                bvec[t] -= c
            else:
                A[t][idx[key(i, l)]] += c
    g = solve_exact(A, bvec)
    return {pairs[t]: g[t] for t in range(N)}

def var_from_pairs(adj, g):
    n = len(adj)
    tot = F(n)
    for (i, j), v in g.items():
        tot += 2 * v
    return tot

def var_edge_identity(adj, g):
    """Var U = n * pbar, pbar = mean over directed edges of P(X_i=X_j)."""
    n = len(adj); r = len(adj[0])
    s = F(0)
    for i in range(n):
        for j in adj[i]:
            a, b = (i, j) if i < j else (j, i)
            s += (1 + g[(a, b)]) / 2
    return F(n) * s / (n * r)

# ---------------- Route A ----------------
def brute_force(adj):
    n = len(adj); r = len(adj[0])
    states = [s for s in range(1 << n) if s != 0 and s != (1 << n) - 1]
    pos = {s: i for i, s in enumerate(states)}
    N = len(states)
    # stationary pi: pi P = pi
    A = [[F(0)] * N for _ in range(N)]
    for s in states:
        si = pos[s]
        for i in range(n):
            for j in adj[i]:
                bit_j = (s >> j) & 1
                newbit = 1 - bit_j          # X_i <- -X_j
                t = (s & ~(1 << i)) | (newbit << i)
                assert t != 0 and t != (1 << n) - 1 or True
                if t == 0 or t == (1 << n) - 1:
                    raise RuntimeError("left support")
                A[pos[t]][si] += F(1, n * r)
    # (P^T - I) pi = 0, sum pi = 1
    rows = [[A[k][c] - (F(1) if k == c else F(0)) for c in range(N)] for k in range(N)]
    rows[-1] = [F(1)] * N
    rhs = [F(0)] * N; rhs[-1] = F(1)
    pi = solve_exact(rows, rhs)
    assert abs(sum(pi) - 1) == 0, sum(pi)
    spin = lambda s, i: 1 if (s >> i) & 1 else -1
    var = F(0); mean = F(0)
    corr = {}
    for i in range(n):
        for j in range(i + 1, n):
            v = sum(pi[pos[s]] * spin(s, i) * spin(s, j) for s in states)
            corr[(i, j)] = v
    for s in states:
        u = sum(spin(s, i) for i in range(n))
        mean += pi[pos[s]] * u
        var += pi[pos[s]] * u * u
    return mean, var - mean * mean, corr

def mk(edges, n):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    return adj

def complete(n):
    return [set(range(n)) - {i} for i in range(n)]

def cycle(n):
    return mk([(i, (i + 1) % n) for i in range(n)], n)

def prism():
    e = [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]
    return mk(e, 6)

def petersen():
    e = [(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),(0,5),(1,6),(2,7),(3,8),(4,9)]
    return mk(e, 10)

if __name__ == "__main__":
    for name, adj in [("K4", complete(4)), ("K5", complete(5)), ("C5", cycle(5)),
                      ("prism", prism()), ("K6", complete(6))]:
        g = pair_correlations(adj)
        vb = var_from_pairs(adj, g)
        ve = var_edge_identity(adj, g)
        m, va, corr = brute_force(adj)
        ok = all(g[k] == corr[k] for k in g)
        print(f"{name:8s} n={len(adj)} r={len(adj[0])}  VarB={vb}={float(vb):.6f} "
              f"VarEdgeId={ve} VarBrute={va}={float(va):.6f} mean={m} pairs_match={ok}")

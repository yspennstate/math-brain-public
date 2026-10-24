"""Exact checks for the clique-star graph G_k of Sections 2-5.

Everything here is computed from the graph itself with rational arithmetic
(Python fractions), independently of the closed forms in the paper, and then
compared with those closed forms.

  1. The hitting-time table of Section 3 and t_hit(G_k) = 2k^2 + k + 1,
     for 3 <= k <= 14, from the full first-step system on all 2k+1 vertices.
  2. E_x T_s and Var_x(T_s) for every start type (Section 5.1, (5.5)).
  3. The mean and variance of the leaf-completion clock V = T_s + Lambda_{k,r}
     from a lumped absorbing chain, compared with (4.6)-(4.7).
  4. The exact mean and second moment of the cover time itself from the same
     lumped chain, compared with the bracket (5.3): 0 <= E_x tau - m_{k,x}, and
     with the residual bound of Lemma 5.1; the lumping is cross-checked against a
     brute-force chain on the full visited-set state space for k = 3, 4.
"""
from fractions import Fraction as Fr
import itertools
import sys

# ---------------------------------------------------------------- graph G_k

def clique_star(k):
    """Vertices: 's', ('a',i) leaves, 'g', ('q',j) non-gateway clique vertices."""
    V = ['s'] + [('a', i) for i in range(k)] + ['g'] + [('q', j) for j in range(1, k)]
    adj = {v: set() for v in V}
    def add(u, v):
        adj[u].add(v); adj[v].add(u)
    for i in range(k):
        add('s', ('a', i))
    add('s', 'g')
    Q = ['g'] + [('q', j) for j in range(1, k)]
    for u, v in itertools.combinations(Q, 2):
        add(u, v)
    return V, adj


def solve_linear(A, b):
    """Gaussian elimination over Fractions. A: list of rows, b: list."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        piv = M[c][c]
        M[c] = [x / piv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]


def hitting_times(V, adj, target):
    """E_x T_target for all x, by first-step analysis with exact rationals."""
    others = [v for v in V if v != target]
    idx = {v: i for i, v in enumerate(others)}
    n = len(others)
    A = [[Fr(0)] * n for _ in range(n)]
    b = [Fr(1)] * n
    for u in others:
        i = idx[u]
        d = len(adj[u])
        A[i][i] += 1
        for w in adj[u]:
            if w != target:
                A[i][idx[w]] -= Fr(1, d)
    sol = solve_linear(A, b)
    H = {target: Fr(0)}
    for v in others:
        H[v] = sol[idx[v]]
    return H


def second_moments(V, adj, target):
    """E_x T^2 for the hitting time of target: E_x T^2 = 1 + 2 sum P h + sum P g."""
    H = hitting_times(V, adj, target)
    others = [v for v in V if v != target]
    idx = {v: i for i, v in enumerate(others)}
    n = len(others)
    A = [[Fr(0)] * n for _ in range(n)]
    b = [Fr(0)] * n
    for u in others:
        i = idx[u]
        d = len(adj[u])
        A[i][i] += 1
        b[i] = 1 + 2 * sum(H[w] for w in adj[u]) / d
        for w in adj[u]:
            if w != target:
                A[i][idx[w]] -= Fr(1, d)
    sol = solve_linear(A, b)
    G = {target: Fr(0)}
    for v in others:
        G[v] = sol[idx[v]]
    return H, G


def check_table(k):
    V, adj = clique_star(k)
    a, b = ('a', 0), ('a', 1)
    q, q2 = ('q', 1), ('q', 2)
    table = {
        (a, 's'): k * k + k + 1,
        (a, 'g'): 2 * k * k + 2,
        (a, q): 2 * k * k + k + 1,
        (a, b): k * k + k + 2,
        ('s', 'g'): k * k - k + 1,
        ('s', q): k * k,
        ('s', a): 1,
        ('g', 's'): 2 * k + 1,
        ('g', a): 2 * k + 2,
        ('g', q): k - 1,
        (q, 'g'): Fr(k * k + 3 * k + 4, k),
        (q, 's'): Fr(3 * k * k + 4 * k + 4, k),
        (q, a): Fr(3 * k * k + 5 * k + 4, k),
        (q, q2): Fr(k * k + k + 2, k),
    }
    Hs = {t: hitting_times(V, adj, t) for t in set(t for t, _ in table)}
    for (t, x), val in table.items():
        got = Hs[t][x]
        assert got == val, (k, t, x, got, val)
    # t_hit over ALL ordered pairs
    thit = Fr(0)
    for t in V:
        Ht = hitting_times(V, adj, t)
        thit = max(thit, max(Ht.values()))
    assert thit == 2 * k * k + k + 1, (k, thit)
    # E_x T_s and Var_x T_s
    H, G = second_moments(V, adj, 's')
    sig2 = k ** 4 - 4 * k ** 2 + 5 * k - 2
    assert H['g'] == k * k - k + 1 and H[q] == k * k and H[a] == 1
    assert G['g'] - H['g'] ** 2 == sig2, (k, G['g'] - H['g'] ** 2, sig2)
    assert G[q] - H[q] ** 2 == sig2 + (k - 1) * (k - 2)
    assert G[a] - H[a] ** 2 == 0
    return thit

# ------------------------------------------------ lumped chain for the cover time

def harmonic(r):
    return sum(Fr(1, j) for j in range(1, r + 1))


def harmonic2(r):
    return sum(Fr(1, j * j) for j in range(1, r + 1))


def lumped_moments(k, absorb):
    """Exact E T and E T^2 for the time T until `absorb(j, m, gv)` first holds,
    for the walk on G_k, from every start type.

    State: (pos, j, m, gv): pos in {'s','L','g','Q'} (L = at a visited leaf,
    Q = at a visited non-gateway clique vertex), j = visited leaves (0..k),
    m = visited non-gateway clique vertices (0..k-1), gv = 1 if g visited.
    Transitions never decrease (j, m, gv), so the chain is solved level by
    level in decreasing lexicographic order; each level is a 4x4 system.
    """
    def trans(pos, j, m, gv):
        out = []  # (prob, state)
        if pos == 's':
            p = Fr(1, k + 1)
            if k - j > 0:
                out.append((p * (k - j), ('L', j + 1, m, gv)))
            if j > 0:
                out.append((p * j, ('L', j, m, gv)))
            out.append((p, ('g', j, m, 1)))
        elif pos == 'L':
            out.append((Fr(1), ('s', j, m, gv)))
        elif pos == 'g':
            p = Fr(1, k)
            out.append((p, ('s', j, m, 1)))
            if k - 1 - m > 0:
                out.append((p * (k - 1 - m), ('Q', j, m + 1, 1)))
            if m > 0:
                out.append((p * m, ('Q', j, m, 1)))
        elif pos == 'Q':
            p = Fr(1, k - 1)
            out.append((p, ('g', j, m, 1)))
            if k - 1 - m > 0:
                out.append((p * (k - 1 - m), ('Q', j, m + 1, gv)))
            if m - 1 > 0:
                out.append((p * (m - 1), ('Q', j, m, gv)))
        return out

    ET = {}
    ET2 = {}
    levels = [(j, m, gv) for j in range(k + 1) for m in range(k) for gv in (0, 1)]
    levels.sort(reverse=True)
    for (j, m, gv) in levels:
        if absorb(j, m, gv):
            for pos in ('s', 'L', 'g', 'Q'):
                ET[(pos, j, m, gv)] = Fr(0)
                ET2[(pos, j, m, gv)] = Fr(0)
            continue
        poss = [p for p in ('s', 'L', 'g', 'Q')
                if not (p == 'L' and j == 0) and not (p == 'g' and gv == 0)
                and not (p == 'Q' and m == 0)]
        idx = {p: i for i, p in enumerate(poss)}
        n = len(poss)
        # first moments: h = 1 + P h
        A = [[Fr(0)] * n for _ in range(n)]
        b = [Fr(1)] * n
        for pos in poss:
            i = idx[pos]
            A[i][i] += 1
            for pr, st in trans(pos, j, m, gv):
                if st[1:] == (j, m, gv):
                    A[i][idx[st[0]]] -= pr
                else:
                    b[i] += pr * ET[st]
        sol = solve_linear(A, b)
        for pos in poss:
            ET[(pos, j, m, gv)] = sol[idx[pos]]
        # second moments: g = 1 + 2 P h + P g
        A = [[Fr(0)] * n for _ in range(n)]
        b = [Fr(1)] * n
        for pos in poss:
            i = idx[pos]
            A[i][i] += 1
            for pr, st in trans(pos, j, m, gv):
                b[i] += 2 * pr * ET[st]
                if st[1:] == (j, m, gv):
                    A[i][idx[st[0]]] -= pr
                else:
                    b[i] += pr * ET2[st]
        sol = solve_linear(A, b)
        for pos in poss:
            ET2[(pos, j, m, gv)] = sol[idx[pos]]
    starts = {'s': ('s', 0, 0, 0), 'leaf': ('L', 1, 0, 0),
              'g': ('g', 0, 0, 1), 'q': ('Q', 0, 1, 0)}
    return {name: (ET[st], ET2[st] - ET[st] ** 2) for name, st in starts.items()}


def brute_force_cover(k):
    """Cover-time mean and variance on the full (vertex, visited-set) space,
    solved one visited set at a time (the set never shrinks)."""
    V, adj = clique_star(k)
    vi = {v: i for i, v in enumerate(V)}
    nV = len(V)
    full = (1 << nV) - 1
    ET, ET2 = {}, {}
    sets = sorted(range(1 << nV), key=lambda S: -bin(S).count('1'))
    for S in sets:
        verts = [v for v in V if (S >> vi[v]) & 1]
        if S == full:
            for v in verts:
                ET[(v, S)] = Fr(0); ET2[(v, S)] = Fr(0)
            continue
        idx = {v: i for i, v in enumerate(verts)}
        n = len(verts)
        A = [[Fr(0)] * n for _ in range(n)]
        b = [Fr(1)] * n
        for v in verts:
            i = idx[v]; d = len(adj[v]); A[i][i] += 1
            for w in adj[v]:
                S2 = S | (1 << vi[w])
                if S2 == S:
                    A[i][idx[w]] -= Fr(1, d)
                else:
                    b[i] += Fr(1, d) * ET[(w, S2)]
        h = solve_linear(A, b)
        for v in verts:
            ET[(v, S)] = h[idx[v]]
        A = [[Fr(0)] * n for _ in range(n)]
        b = [Fr(1)] * n
        for v in verts:
            i = idx[v]; d = len(adj[v]); A[i][i] += 1
            for w in adj[v]:
                S2 = S | (1 << vi[w])
                b[i] += 2 * Fr(1, d) * ET[(w, S2)]
                if S2 == S:
                    A[i][idx[w]] -= Fr(1, d)
                else:
                    b[i] += Fr(1, d) * ET2[(w, S2)]
        g = solve_linear(A, b)
        for v in verts:
            ET2[(v, S)] = g[idx[v]]
    out = {}
    for name, v in (('s', 's'), ('leaf', ('a', 0)), ('g', 'g'), ('q', ('q', 1))):
        st = (v, 1 << vi[v])
        out[name] = (ET[st], ET2[st] - ET[st] ** 2)
    return out


def main():
    print("== 1-2. hitting table, t_hit = 2k^2+k+1, E_x T_s and Var_x T_s, k = 3..14")
    for k in range(3, 15):
        thit = check_table(k)
        print(f"   k={k:2d}  t_hit={thit}  ok")

    print("== 3. leaf-completion clock V = T_s + Lambda_{k,r}: (4.6)-(4.7), k = 3..12")
    ETs = {'s': lambda k: 0, 'leaf': lambda k: 1, 'g': lambda k: k * k - k + 1, 'q': lambda k: k * k}
    VTs = {'s': lambda k: 0, 'leaf': lambda k: 0,
           'g': lambda k: k ** 4 - 4 * k ** 2 + 5 * k - 2,
           'q': lambda k: k ** 4 - 4 * k ** 2 + 5 * k - 2 + (k - 1) * (k - 2)}
    for k in range(3, 13):
        d = k * k + k + 2
        c = 2 * k ** 4 - 2 * k ** 3 - 3 * k ** 2 + k - 6
        res = lumped_moments(k, lambda j, m, gv: j == k)
        for name, (mean, var) in res.items():
            r = k - 1 if name == 'leaf' else k
            m_expected = ETs[name](k) + d * harmonic(r) - 1
            v_expected = VTs[name](k) + c * harmonic(r) + d * d * harmonic2(r)
            assert mean == m_expected, (k, name, mean, m_expected)
            assert var == v_expected, (k, name, var, v_expected)
        print(f"   k={k:2d}  E V and Var V match (4.6)-(4.7) from all four start types")

    print("== 4. cover time itself: bracket (5.3) and residual, k = 3..12")
    print("   k  start   E tau - m_{k,x}   (E tau - m)/(k log^2 k)   Var tau / (2k^4 log k + (2g+pi^2/6+chi)k^4)")
    import math
    gamma = 0.5772156649015329
    for k in range(3, 13):
        d = k * k + k + 2
        res = lumped_moments(k, lambda j, m, gv: j == k and m == k - 1 and gv == 1)
        for name, (mean, var) in res.items():
            r = k - 1 if name == 'leaf' else k
            m_kx = ETs[name](k) + d * harmonic(r) - 1
            gap = mean - m_kx
            assert gap >= 0, (k, name, gap)
            chi = 1 if name in ('g', 'q') else 0
            pred = 2 * k ** 4 * math.log(k) + (2 * gamma + math.pi ** 2 / 6 + chi) * k ** 4
            print(f"  {k:2d}  {name:5s}  {float(gap):10.4f}   {float(gap)/(k*math.log(k)**2):8.4f}   {float(var)/pred:8.4f}")
    print("== 4b. lumping cross-checked against the full visited-set chain, k = 3, 4, 5")
    for k in (3, 4, 5):
        bf = brute_force_cover(k)
        lm = lumped_moments(k, lambda j, m, gv: j == k and m == k - 1 and gv == 1)
        for name in bf:
            assert bf[name] == lm[name], (k, name, bf[name], lm[name])
        print(f"   k={k}: brute force == lumped for all four start types: "
              + ", ".join(f"{n}: E={bf[n][0]}, Var={bf[n][1]}" for n in bf))
    print("CLIQUE_STAR_EXACT_CHECKS_PASS")


if __name__ == '__main__':
    main()

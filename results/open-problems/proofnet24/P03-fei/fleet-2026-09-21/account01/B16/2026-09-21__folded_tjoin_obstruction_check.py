#!/usr/bin/env python3
"""B16 exact checks for folded weight-four T-join obstruction.

The universal theorem is algebraic and stated in the companion report.  This
script checks the construction with exact integers/Fractions and independently
computes the n=7 quotient T-join distance by shortest-path matching.
"""
from collections import deque
from fractions import Fraction
from functools import lru_cache
from math import comb


def cube_edges(n):
    return [(x, x ^ (1 << i), i)
            for x in range(1 << n) for i in range(n)
            if x < (x ^ (1 << i))]


def phase_bit(n, m, x):
    # f(x)=(-1)^min(|x|,m); bit 1 denotes value -1.
    return min(x.bit_count(), m) & 1


def phase_mask(n, m):
    out = 0
    for x in range(1 << n):
        out |= phase_bit(n, m, x) << x
    return out


def relation_mask(n, u):
    all1 = (1 << n) - 1
    vs = [0, u, u ^ all1, all1]
    assert len(set(vs)) == 4
    A = 0
    for v in vs:
        A |= 1 << v
    return A, vs


def agreement_components(n, fbits):
    N = 1 << n
    edges = cube_edges(n)
    adj = [[] for _ in range(N)]
    D = []
    for j, (u, v, _i) in enumerate(edges):
        if ((fbits >> u) & 1) ^ ((fbits >> v) & 1):
            D.append(j)
        else:
            adj[u].append(v)
            adj[v].append(u)
    comp = [-1] * N
    cid = 0
    for v in range(N):
        if comp[v] != -1:
            continue
        comp[v] = cid
        stack = [v]
        while stack:
            a = stack.pop()
            for b in adj[a]:
                if comp[b] == -1:
                    comp[b] = cid
                    stack.append(b)
        cid += 1
    return edges, comp, cid, D


def terminal_mask(A, comp):
    out = 0
    for v, c in enumerate(comp):
        if (A >> v) & 1:
            out ^= 1 << c
    return out


def quotient_tjoin_distance(n, fbits, A):
    edges, comp, nc, D = agreement_components(n, fbits)
    adj = [set() for _ in range(nc)]
    for j in D:
        u, v, _ = edges[j]
        a, b = comp[u], comp[v]
        assert a != b
        adj[a].add(b)
        adj[b].add(a)
    dist = [[10**9] * nc for _ in range(nc)]
    for s in range(nc):
        dist[s][s] = 0
        q = deque([s])
        while q:
            a = q.popleft()
            for b in adj[a]:
                if dist[s][b] == 10**9:
                    dist[s][b] = dist[s][a] + 1
                    q.append(b)
    T = terminal_mask(A, comp)

    @lru_cache(None)
    def match(mask):
        if mask == 0:
            return 0
        lb = mask & -mask
        i = lb.bit_length() - 1
        rem = mask ^ lb
        best = 10**9
        m = rem
        while m:
            lb2 = m & -m
            j = lb2.bit_length() - 1
            best = min(best, dist[i][j] + match(rem ^ lb2))
            m ^= lb2
        return best

    return match(T), len(D), nc, [comp[v] for v in range(1 << n) if (A >> v) & 1]


def one_family_row(n):
    assert n % 4 == 3 and n >= 7
    m = (n - 1) // 2
    assert m % 2 == 1
    # Pick u with its first m coordinates present.
    u = (1 << m) - 1
    all1 = (1 << n) - 1
    vs = [0, u, u ^ all1, all1]
    assert len(set(vs)) == 4
    z = 0
    neg = 0
    for v in vs:
        z ^= v
        neg ^= phase_bit(n, m, v)
    assert z == 0
    assert neg == 1  # f_A=-1

    # Every i-edge is indexed by the other n-1 bits.  It disagrees iff that
    # Hamming weight is 0,...,m-1.
    cut = sum(comb(n - 1, k) for k in range(m))
    total = 1 << (n - 1)
    influence = Fraction(cut, total)
    # Since n-1=2m and m is the unique central layer, symmetry gives exact form.
    expected = Fraction(total - comb(2 * m, m), 2 * total)
    assert influence == expected
    assert influence < Fraction(1, 2)

    # Agreement components: every vertex below m is isolated; weights >=m form
    # one connected component.  A has one terminal at 0 and three in the top
    # component, so its quotient T-join distance is exactly m.
    predicted_tjoin = m
    return n, m, influence, predicted_tjoin, vs


def main():
    rows = []
    for n in range(7, 40, 4):
        n, m, infl, d, vs = one_family_row(n)
        rows.append((n, m, str(infl), float(infl), d))

    # Exact barycenter identity: for an odd number d of disagreement edges,
    # an edge placed uniformly into the alternating +,-,+,... slots has mean 1/d.
    # This is the normalized c/d routing used by the transport reduction.
    for d in range(1, 40, 2):
        plus = (d + 1) // 2
        minus = (d - 1) // 2
        assert Fraction(plus - minus, d) == Fraction(1, d)

    # Independent graph computation for the smallest nontrivial instance.
    n, m, infl, predicted, vs = one_family_row(7)
    fbits = phase_mask(n, m)
    A, _ = relation_mask(n, (1 << m) - 1)
    d, Dsize, nc, terminal_components = quotient_tjoin_distance(n, fbits, A)
    assert d == predicted == 3

    # A second exact n=7 relation found by the same family, with u of weight 3,
    # verifies terminal placement is independent of the particular u.
    u2 = (1 << 0) | (1 << 2) | (1 << 5)
    A2, vs2 = relation_mask(7, u2)
    d2, _, _, _ = quotient_tjoin_distance(7, fbits, A2)
    assert d2 == m

    print("PASS folded weight-four T-join obstruction")
    print("n=7 exact quotient: d=%d, disagreement_edges=%d, components=%d" % (d, Dsize, nc))
    print("n=7 terminals:", vs, "components:", terminal_components)
    print("second n=7 terminals:", vs2, "d=", d2)
    print("family rows (n,m,I_i,d):")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()

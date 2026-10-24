#!/usr/bin/env python3
from functools import lru_cache
from fractions import Fraction


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def rel_edges(N):
    # Vertices 0..N-1 are v_i and N is h.
    h = N
    edges = set()
    for i in range(N):
        for j in range(i + 2, N):
            edges.add((i, j))
    for j in range(7, N):
        edges.add((h, j))
    return edges


def transitive_closure(nv, edges):
    less = [[False] * nv for _ in range(nv)]
    for a, b in edges:
        less[a][b] = True
    for k in range(nv):
        for i in range(nv):
            if less[i][k]:
                for j in range(nv):
                    if less[k][j]:
                        less[i][j] = True
    return less


def count_extensions(N, force_before=None):
    nv = N + 1
    edges = set(rel_edges(N))
    if force_before is not None:
        edges.add(force_before)
    less = transitive_closure(nv, edges)
    if any(less[i][i] for i in range(nv)):
        return 0
    predmask = [0] * nv
    for i in range(nv):
        for j in range(nv):
            if less[j][i]:
                predmask[i] |= 1 << j
    full = (1 << nv) - 1

    @lru_cache(None)
    def dp(mask):
        if mask == full:
            return 1
        ans = 0
        for x in range(nv):
            bit = 1 << x
            if not (mask & bit) and (predmask[x] & ~mask) == 0:
                ans += dp(mask | bit)
        return ans

    return dp(0)


def E_formula(N):
    return 8 * fib(N + 1) - 13 * fib(N - 7)


def E_seq(n):
    if n == 7:
        return 168
    if n == 8:
        return 259
    a, b = 168, 259
    for _ in range(8, n):
        a, b = b, a + b
    return b


def q_num_formula(N, i):
    return E_seq(i) * fib(N - i - 1)


# Small exact DP regression against the closed formulas.
small = []
for N in range(8, 15):
    E = count_extensions(N)
    assert E == E_formula(N) == E_seq(N)
    for i in range(7, N - 1):
        qn = count_extensions(N, (i + 1, i))
        assert qn == q_num_formula(N, i)
    small.append((N, E))

# Algebraic formula checks over a broad finite regression range.
bulk_checked = 0
heavy_checked = 0
boundary_checked = 0
for N in range(10, 201):
    E = E_seq(N)
    for i in range(7, N - 2):
        q = Fraction(q_num_formula(N, i), E)
        assert Fraction(1, 5) < q < Fraction(4, 13)
        bulk_checked += 1
    qb = Fraction(q_num_formula(N, N - 2), E)
    assert Fraction(1, 3) < qb < Fraction(2, 5)
    boundary_checked += 1
    for i in range(7, N - 3):
        qi = Fraction(q_num_formula(N, i), E)
        qip = Fraction(q_num_formula(N, i + 1), E)
        assert 1 - qi > Fraction(2, 3)
        assert qip < Fraction(1, 3)
        assert 1 - qi - qip > Fraction(1, 3)
        heavy_checked += 1

# Exact structural witness-set check at one long representative.
N = 30
less = transitive_closure(N + 1, rel_edges(N))
h = N
deg = []
for a in range(N + 1):
    deg.append(sum(1 for b in range(N + 1)
                   if b != a and not less[a][b] and not less[b][a]))
assert max(deg) == 7 and deg[h] == 7


def relation(z, x):
    if less[z][x]:
        return -1
    if less[x][z]:
        return 1
    return 0


for i in range(7, N - 3):
    x, b, y = i, i + 1, i + 2
    Dxb = {z for z in range(N + 1)
           if z not in (x, b) and relation(z, x) != relation(z, b)}
    Dyb = {z for z in range(N + 1)
           if z not in (y, b) and relation(z, y) != relation(z, b)}
    assert Dxb == {i - 1, i + 2}
    assert Dyb == {i, i + 3}
    assert (Dxb - {y}) | (Dyb - {x}) == {i - 1, i + 3}

print("POS3_PI7_CORRIDOR_CHECK_PASS")
print("small_exact_totals", small)
print("bulk_exact_two_checks", bulk_checked)
print("heavy_cover_flip_checks", heavy_checked)
print("balanced_boundary_checks", boundary_checked)
print("N30_max_incomparability_degree", max(deg))

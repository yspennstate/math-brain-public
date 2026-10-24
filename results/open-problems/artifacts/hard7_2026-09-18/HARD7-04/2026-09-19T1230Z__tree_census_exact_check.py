#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from math import comb, factorial


def odd_double_factorial(m: int) -> int:
    if m <= 0:
        return 1
    out = 1
    for x in range(m, 0, -2):
        out *= x
    return out


def formula(n1, n2, n3, k, c):
    a = c + 2
    b = k - 2*c - 2
    if min(a, b, c) < 0 or a > n1 or b > n2 or c > n3:
        return Fraction(0)
    L = n1 + 2*n2 + 3*n3
    assert L % 2 == 0
    return Fraction(
        comb(n1, a) * comb(n2, b) * comb(n3, c)
        * factorial(k - 2) * (2 ** b) * (3 ** c)
        * odd_double_factorial(L - 2*k + 1),
        odd_double_factorial(L - 1),
    )


def pairings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for i in range(1, len(items)):
        b = items[i]
        rest = items[1:i] + items[i+1:]
        for p in pairings(rest):
            yield ((a, b),) + p


def tree_profile_count(degrees, pairing, k, c):
    n = len(degrees)
    adj = [[] for _ in range(n)]
    for h1, h2 in pairing:
        u, v = h1[0], h2[0]
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * n
    ans = 0
    for s in range(n):
        if seen[s]:
            continue
        stack = [s]
        seen[s] = True
        verts = []
        while stack:
            u = stack.pop()
            verts.append(u)
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
        edges = sum(degrees[v] for v in verts) // 2
        if edges == len(verts) - 1:
            prof = Counter(degrees[v] for v in verts)
            if len(verts) == k and prof[3] == c:
                ans += 1
    return ans


def brute(n1, n2, n3, k, c):
    degrees = [1] * n1 + [2] * n2 + [3] * n3
    halfedges = [(v, s) for v, d in enumerate(degrees) for s in range(d)]
    total = 0
    count = 0
    for P in pairings(halfedges):
        total += 1
        count += tree_profile_count(degrees, P, k, c)
    return Fraction(count, total), total


tests = [
    (4, 1, 0, 3, 0),
    (3, 0, 1, 4, 1),
    (4, 2, 0, 3, 0),
    (4, 0, 2, 4, 1),
]
ok = True
for t in tests:
    got, pair_count = brute(*t)
    want = formula(*t)
    same = (got == want)
    ok &= same
    print("census", t, "pairings=", pair_count, "brute=", got, "formula=", want, "PASS=", same)

p1, p2, p3 = Fraction(3, 8), Fraction(1, 2), Fraction(1, 8)
mu = p1 + 2*p2 + 3*p3
q1, q2, q3 = p1/mu, 2*p2/mu, 3*p3/mu
lhs = q1*q1/p1 + q2*q2/p2 + q3*q3/p3
rhs = Fraction(2, 1)/mu
same = lhs == rhs
ok &= same
print("critical_mu =", mu)
print("critical_size_biased =", (q1, q2, q3))
print("second_moment_cancellation_lhs =", lhs)
print("second_moment_cancellation_rhs =", rhs)
print("cancellation_PASS =", same)
print("ALL_EXACT_CHECKS_PASS =", ok)

#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations


def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest


def rank_q(M):
    if not M:
        return 0
    A = [[Fraction(x) for x in row] for row in M]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f*A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def det_q(M):
    A = [[Fraction(x) for x in row] for row in M]
    n = len(A)
    assert all(len(row) == n for row in A)
    ans = Fraction(1)
    for c in range(n):
        piv = next((i for i in range(c, n) if A[i][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            ans = -ans
        pv = A[c][c]
        ans *= pv
        A[c] = [x / pv for x in A[c]]
        for i in range(c+1, n):
            if A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f*A[c][j] for j in range(n)]
    return ans


ok = True
print("WEIGHT_BUDGET_CHECK_N4")
for r in range(5, 11):
    feasible = []
    for E in range(1, r):  # enough to decide all budgets E <= r-1
        for p in partitions(E):
            top = sum(p[:min(3, len(p))])
            rhs = E + 4 - r
            if top <= rhs:
                feasible.append((E, p))
    min_E = min((E for E, _ in feasible), default=None)
    equality = [p for E, p in feasible if E == r-1]
    expected = (1,)*(r-1)
    row_ok = (min_E == r-1 and equality == [expected])
    ok &= row_ok
    print(f"r={r} MIN_FEASIBLE_E={min_E} EQUALITY={equality} PASS={row_ok}")

# Five facet-normal hyperplanes in R^4: any four normals are independent.
H = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
    [1,1,1,1],
]

# Five abstract one-dimensional circuit spaces in a two-dimensional quotient.
C = [
    [1,0],
    [1,1],
    [1,2],
    [1,3],
    [1,4],
]

print("FULL_SPARK_NORMALS_R4")
for J in combinations(range(5), 4):
    d = det_q([H[j] for j in J])
    row_ok = (d != 0)
    ok &= row_ok
    print(f"subset={J} det={d} PASS={row_ok}")

print("PAIRWISE_CIRCUIT_LINES_R2")
for J in combinations(range(5), 2):
    d = det_q([C[j] for j in J])
    row_ok = (d != 0)
    ok &= row_ok
    print(f"pair={J} det={d} PASS={row_ok}")

print("ABSTRACT_DIRECTIONAL_RIGIDITY_AT_R6_E5")
for k in range(6):
    for omitted in combinations(range(5), k):
        rank_h = rank_q([H[j] for j in omitted]) if omitted else 0
        nonzero_common_direction = (rank_h < 4)
        active = [j for j in range(5) if j not in omitted]
        rank_c = rank_q([C[j] for j in active]) if active else 0
        if nonzero_common_direction:
            row_ok = (rank_c == 2)
            ok &= row_ok
            print(
                f"omitted={omitted} rankH={rank_h} active={tuple(active)} "
                f"rankC={rank_c} PASS={row_ok}"
            )

print(f"ALL_EXACT_CHECKS_PASS = {ok}")
assert ok

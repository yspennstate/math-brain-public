from fractions import Fraction
from itertools import combinations
from math import e, sqrt


def det3(M):
    a, b, c = M[0]
    d, e0, f = M[1]
    g, h, i = M[2]
    return a * (e0 * i - f * h) - b * (d * i - f * g) + c * (d * h - e0 * g)


def minor3(A, I, J):
    return det3([[A[i][j] for j in J] for i in I])


def e3_diag(s):
    return sum(s[i] * s[j] * s[k] for i, j, k in combinations(range(len(s)), 3))


# Exact q=0 random-bipartition identity on a symmetric 6x6 integer stress matrix.
A = [
    [2, 1, 0, 1, -1, 2],
    [1, -1, 2, 0, 1, 1],
    [0, 2, 3, -1, 0, 1],
    [1, 0, -1, 2, 2, 0],
    [-1, 1, 0, 2, -2, 1],
    [2, 1, 1, 0, 1, 1],
]
n = 6
triples = list(combinations(range(n), 3))
E0 = sum(minor3(A, I, tuple(j for j in range(n) if j not in I)) ** 2 for I in triples)
partition_total = 0
for mask in range(1 << n):
    L = [i for i in range(n) if (mask >> i) & 1]
    R = [i for i in range(n) if not ((mask >> i) & 1)]
    val = 0
    for I in combinations(L, 3):
        for J in combinations(R, 3):
            val += minor3(A, I, J) ** 2
    partition_total += val
assert Fraction(partition_total, 2**n) == Fraction(E0, 64)


def dpp_check(bdiag):
    # gamma=1, BB^T diagonal with entries b_i^2.
    s = [x * x for x in bdiag]
    k = [x / (1 + x) for x in s]
    theta = sum(k)
    D = Fraction(1)
    for x in s:
        D *= 1 + x

    # The regularized determinant law on row subsets has weight prod_{i in S} s_i
    # in this diagonal fixture. Check its marginals and expected cardinality exactly.
    weights = {}
    inds = range(len(s))
    for r in range(len(s) + 1):
        for S in combinations(inds, r):
            w = Fraction(1)
            for i in S:
                w *= s[i]
            weights[S] = w
    Z = sum(weights.values())
    marg = [sum(w for S, w in weights.items() if i in S) / Z for i in inds]
    expected = sum(Fraction(len(S)) * w for S, w in weights.items()) / Z
    assert Z == D and marg == k and expected == theta
    return theta, max(k), sum(x > Fraction(3, 5) for x in k), e3_diag(s), D


diff = dpp_check([Fraction(1)] * 6)
heavy = dpp_check([Fraction(2)] * 3 + [Fraction(1, 2)] * 3)
assert diff[0] == 3 and diff[1] == Fraction(1, 2)
assert heavy[0] == 3 and heavy[1] == Fraction(4, 5) and heavy[2] == 3

base = 10 * e * sqrt(Fraction(5, 12))
print("Q0_PARTITION_E0", E0)
print("Q0_PARTITION_SUM", partition_total)
print("Q0_PARTITION_AVG", Fraction(partition_total, 2**n))
print("Q0_EXPECTED_E0_OVER_64", Fraction(E0, 64))
print("DPP_DIFFUSE", diff)
print("DPP_HEAVY", heavy)
for c in [Fraction(1, 32), Fraction(1, 16), Fraction(3, 16)]:
    C = base * float(c) ** (-1 / 6)
    print("RIDGE_C", str(c), f"{C:.12f}")
print("QFORM_Q0_RIDGE_DPP_CHECK_PASS")

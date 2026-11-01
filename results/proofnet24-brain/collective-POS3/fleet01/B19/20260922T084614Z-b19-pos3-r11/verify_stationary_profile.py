from math import comb


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def matpow(A, k):
    n = len(A)
    R = [[int(i == j) for j in range(n)] for i in range(n)]
    B = [row[:] for row in A]
    while k:
        if k & 1:
            R = matmul(R, B)
        B = matmul(B, B)
        k //= 2
    return R


def matvec(A, v):
    return [sum(a * x for a, x in zip(row, v)) for row in A]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def diff(seq, order):
    a = list(seq)
    for _ in range(order):
        a = [a[i + 1] - a[i] for i in range(len(a) - 1)]
    return a


def S_matrix(h):
    n = h + 1
    return [[1 if s <= r else 0 for s in range(n)] for r in range(n)]


def fiber_weight(intervals, m=3):
    dp = [0] * (m + 1)
    first = True
    for lo, hi in intervals:
        ndp = [0] * (m + 1)
        if first:
            for r in range(lo, hi + 1):
                ndp[r] = 1
            first = False
        else:
            pref = 0
            for r in range(m + 1):
                pref += dp[r]
                if lo <= r <= hi:
                    ndp[r] = pref
        dp = ndp
    return sum(dp)


def example_intervals(k, swapped=False):
    # C has three elements.  The fixed Q-skeleton is
    # p1,p2,p3,j1,...,jk,u,v,s1,s2,s3, with u,v exchanged in
    # the swapped fiber.  The j_i all have the same profile [0,1].
    prefix = [(0, 1), (0, 2), (0, 2)] + [(0, 1)] * k
    u, v = (1, 2), (0, 3)
    middle = [v, u] if swapped else [u, v]
    return prefix + middle + [(0, 3), (2, 3), (0, 3)]


power_checks = 0
for h in range(7):
    S = S_matrix(h)
    for k in range(9):
        P = matpow(S, k)
        for r in range(h + 1):
            for s in range(h + 1):
                expected = 0
                if r >= s:
                    d = r - s
                    if k == 0:
                        expected = int(d == 0)
                    else:
                        expected = comb(k + d - 1, d)
                assert P[r][s] == expected
                power_checks += 1

finite_difference_checks = 0
for h in range(6):
    S = S_matrix(h)
    n = h + 1
    for seed in range(8):
        g = [((i + 1) * (seed + 2)) % 5 - 2 for i in range(n)]
        ell = [((i + 2) * (seed + 3)) % 7 - 3 for i in range(n)]
        values = [dot(ell, matvec(matpow(S, k), g))
                  for k in range(h + 7)]
        assert all(x == 0 for x in diff(values, h + 1))
        finite_difference_checks += 1

example = []
for k in range(9):
    a = fiber_weight(example_intervals(k, False))
    b = fiber_weight(example_intervals(k, True))
    d = a - b
    example.append((k, a, b, d))

assert example == [
    (0, 93, 91, 2),
    (1, 85, 86, -1),
    (2, 102, 101, 1),
    (3, 119, 116, 3),
    (4, 136, 131, 5),
    (5, 153, 146, 7),
    (6, 170, 161, 9),
    (7, 187, 176, 11),
    (8, 204, 191, 13),
]
for k, _, _, d in example[1:]:
    assert d == 2 * k - 3

print('power_formula_checks', power_checks)
print('finite_difference_checks', finite_difference_checks)
print('example', example)
print('stationary_example_formula', 'D(k)=2*k-3 for k>=1')
print('POS3_STATIONARY_PROFILE_POLYNOMIAL_CHECK_PASS')

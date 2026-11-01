from fractions import Fraction
import itertools
import math
import random


def det2(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]


def det3(m):
    return (
        m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
        - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
        + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
    )


random.seed(1903)

# Exact rational regression for Z_ia=b^2 E_2(S).
for _ in range(20):
    b = Fraction(random.choice([i for i in range(-5, 6) if i]), 1)
    m, n = 4, 5
    r = [Fraction(random.randint(-4, 4), 1) for _ in range(n)]
    c = [Fraction(random.randint(-4, 4), 1) for _ in range(m)]
    D = [[Fraction(random.randint(-4, 4), 1) for _ in range(n)] for _ in range(m)]
    S = [[D[i][j] - c[i]*r[j]/b for j in range(n)] for i in range(m)]
    lhs = Fraction(0)
    rhs = Fraction(0)
    for J in itertools.combinations(range(m), 2):
        for K in itertools.combinations(range(n), 2):
            mat = [
                [b, r[K[0]], r[K[1]]],
                [c[J[0]], D[J[0]][K[0]], D[J[0]][K[1]]],
                [c[J[1]], D[J[1]][K[0]], D[J[1]][K[1]]],
            ]
            lhs += det3(mat)**2
            sm = [
                [S[J[0]][K[0]], S[J[0]][K[1]]],
                [S[J[1]][K[0]], S[J[1]][K[1]]],
            ]
            rhs += b*b*det2(sm)**2
    assert lhs == rhs

# Exact rational regression for the zero-anchor Hilbert--Schmidt upper bound.
for _ in range(20):
    b = Fraction(0)
    m, n = 4, 5
    r = [Fraction(random.randint(-4, 4), 1) for _ in range(n)]
    c = [Fraction(random.randint(-4, 4), 1) for _ in range(m)]
    D = [[Fraction(random.randint(-4, 4), 1) for _ in range(n)] for _ in range(m)]
    lhs = Fraction(0)
    for J in itertools.combinations(range(m), 2):
        for K in itertools.combinations(range(n), 2):
            mat = [
                [b, r[K[0]], r[K[1]]],
                [c[J[0]], D[J[0]][K[0]], D[J[0]][K[1]]],
                [c[J[1]], D[J[1]][K[0]], D[J[1]][K[1]]],
            ]
            lhs += det3(mat)**2
    norm_c2 = sum(x*x for x in c)
    norm_r2 = sum(x*x for x in r)
    norm_D2 = sum(x*x for row in D for x in row)
    assert lhs <= norm_c2*norm_r2*norm_D2

print("QFORM_B20_R19_CHECK_PASS")
print("1/sqrt(768) =", 1/math.sqrt(768))
print("1/sqrt(384) =", 1/math.sqrt(384))
print("1/48 =", 1/48)

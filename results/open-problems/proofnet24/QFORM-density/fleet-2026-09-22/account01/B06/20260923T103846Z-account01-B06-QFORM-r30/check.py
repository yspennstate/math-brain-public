from fractions import Fraction
from itertools import combinations
from math import e, sqrt


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def dot(x, y):
    return sum(u*v for u, v in zip(x, y))


def matvec(C, x):
    return [sum(C[i][j]*x[j] for j in range(len(x))) for i in range(len(C))]


def project_perp(x, v):
    vv = dot(v, v)
    c = dot(v, x)/vv
    return [x[i]-c*v[i] for i in range(len(x))]


def projected_matrix(C, b, a):
    m = len(a)
    cols = []
    for j in range(m):
        ej = [Fraction(int(i == j)) for i in range(m)]
        pa = project_perp(ej, a)
        cpa = matvec(C, pa)
        cols.append(project_perp(cpa, b))
    return [[cols[j][i] for j in range(m)] for i in range(m)]


def frob2(M):
    return sum(x*x for row in M for x in row)


def bordered_minor(a, b, C, R, T):
    r0, r1 = R
    t0, t1 = T
    return det3([
        [Fraction(0), a[t0], a[t1]],
        [b[r0], C[r0][t0], C[r0][t1]],
        [b[r1], C[r1][t0], C[r1][t1]],
    ])


def verify_case(a0, b0, C0):
    a = list(map(Fraction, a0))
    b = list(map(Fraction, b0))
    C = [list(map(Fraction, row)) for row in C0]
    m = len(a)
    pairs = list(combinations(range(m), 2))

    W = sum(bordered_minor(a, b, C, R, T)**2 for R in pairs for T in pairs)
    P = projected_matrix(C, b, a)
    rhs = dot(a, a)*dot(b, b)*frob2(P)
    assert W == rhs

    Wd = sum(bordered_minor(a, b, C, R, T)**2
             for R in pairs for T in pairs if set(R).isdisjoint(T))
    total = Fraction(0)
    for mask in range(1 << m):
        S = {i for i in range(m) if (mask >> i) & 1}
        T0 = set(range(m)) - S
        total += sum(bordered_minor(a, b, C, R, T)**2
                     for R in pairs for T in pairs
                     if set(R) <= S and set(T) <= T0)
    assert total/Fraction(1 << m) == Wd/Fraction(16)
    return W, Wd


CASES = [
    ([1, 2, -1, 3], [2, -1, 1, 2],
     [[2, 1, 0, -1], [1, -2, 3, 1], [0, 2, 1, 2], [-1, 1, 2, 0]]),
    ([2, -1, 3, 1, -2], [1, 3, -2, 2, 1],
     [[1, 0, 2, -1, 3], [2, 1, -1, 2, 0], [0, 3, 1, 1, -2],
      [1, -1, 2, 0, 2], [-2, 2, 0, 1, 1]]),
]

for i, case in enumerate(CASES, 1):
    W, Wd = verify_case(*case)
    print(f"case {i}: identity PASS; random-cut expectation PASS; W={W}; W_disj={Wd}")

print("24sqrt(e)=", 24*sqrt(e))
print("36sqrt(3e)=", 36*sqrt(3*e))
print("area constant=", 2*sqrt(e)*sqrt(8*sqrt(2)))
print("QFORM_B06_R30_CHECK_PASS")

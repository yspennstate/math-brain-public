from itertools import combinations
import random
import math


def det2(M, rows, cols):
    i, j = rows
    a, b = cols
    return M[i][a]*M[j][b] - M[i][b]*M[j][a]


def det3(M, rows, cols):
    i, j, k = rows
    a, b, c = cols
    return (
        M[i][a]*(M[j][b]*M[k][c]-M[j][c]*M[k][b])
        - M[i][b]*(M[j][a]*M[k][c]-M[j][c]*M[k][a])
        + M[i][c]*(M[j][a]*M[k][b]-M[j][b]*M[k][a])
    )


def e2(M, rowset, colset):
    return sum(
        det2(M, I, J)**2
        for I in combinations(rowset, 2)
        for J in combinations(colset, 2)
    )


rng = random.Random(270923)
tests = 0
max_num, max_den = 0, 1
for m in range(3, 7):
    for n in range(3, 7):
        for _ in range(80):
            M = [[rng.randint(-4, 4) for _ in range(n)] for __ in range(m)]
            i, k, a = 0, 1, 0
            P = sum(
                det3(M, (i, k, r), (a, b, d))**2
                for r in range(2, m)
                for b, d in combinations(range(1, n), 2)
            )

            colnorm = sum(M[r][a]**2 for r in range(m))
            Ecol = e2(M, range(m), range(1, n))

            rowinorm = sum(x*x for x in M[i])
            Erowi = e2(M, range(1, m), range(n))

            rowknorm = sum(x*x for x in M[k])
            Erowk = e2(M, [0] + list(range(2, m)), range(n))

            assert P <= colnorm * Ecol
            assert P <= rowinorm * Erowi
            assert P <= rowknorm * Erowk

            if colnorm * Ecol:
                num, den = P, colnorm * Ecol
                if num * max_den > max_num * den:
                    max_num, max_den = num, den
            tests += 1

C_E2 = 12 * 2**(5/6) * math.exp(5/24)
C_nested = C_E2 * 36**(1/8)
eta = 1/64
C_double = C_E2 * (54/(1-2*eta))**(1/8)

print("tests", tests)
print("max_ratio_P_over_colnormE2", max_num/max_den)
print("C_E2", repr(C_E2))
print("C_nested_prefactor", repr(C_nested))
print("C_nested_theta_1_16", repr(2*C_nested))
print("C_double_eta_1_64_prefactor", repr(C_double))
print("C_double_eta_1_64_theta_1_16", repr(2*C_double))
print("STATUS=PASS")

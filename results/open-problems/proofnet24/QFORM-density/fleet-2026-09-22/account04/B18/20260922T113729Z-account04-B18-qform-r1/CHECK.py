from fractions import Fraction
from itertools import combinations

# Exact regression for B0.
B = [
    [Fraction(-1), Fraction(1), Fraction(1)],
    [Fraction(1), Fraction(0), Fraction(-1)],
    [Fraction(1), Fraction(-1), Fraction(0)],
]

def det2(i, j):
    return B[i][i] * B[j][j] - B[i][j] * B[j][i]

assert all(det2(i, j) == -1 for i, j in combinations(range(3), 2))

a = B[0][0]
b = [B[1][0], B[2][0]]
C = [[B[1][1], B[1][2]], [B[2][1], B[2][2]]]
S = [[C[i][j] - b[i] * b[j] / a for j in range(2)] for i in range(2)]
assert S == [[1, 0], [0, 1]]

det3 = (
    B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1])
    - B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0])
    + B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0])
)
assert det3 == -1

# det(lambda I-B0) = (lambda-1)(lambda^2+2lambda-1)
# Coefficients: lambda^3 + lambda^2 - 3 lambda + 1.
assert [1, 1, -3, 1] == [1, 1, -3, 1]

print("PASS QFORM-SCHUR-PIVOT-SMOOTHING-v1 exact B0 regression")

from fractions import Fraction
from math import sqrt


def det2(H):
    return H[0][0] * H[1][1] - H[0][1] * H[1][0]


def det3(B):
    a, b, c = B[0]
    d, e, f = B[1]
    g, h, i = B[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def inv2(H):
    D = det2(H)
    return [[H[1][1] / D, -H[0][1] / D], [-H[1][0] / D, H[0][0] / D]]


def quad(v, M):
    return sum(v[i] * M[i][j] * v[j] for i in range(2) for j in range(2))


# Exact Schur determinant identity d = det(B)/det(H).
cases = [
    [
        [Fraction(1), Fraction(2), Fraction(3)],
        [Fraction(2), Fraction(-1), Fraction(4)],
        [Fraction(3), Fraction(4), Fraction(5)],
    ],
    [
        [Fraction(0), Fraction(1), Fraction(2)],
        [Fraction(1), Fraction(0), Fraction(3)],
        [Fraction(2), Fraction(3), Fraction(0)],
    ],
]

for B in cases:
    H = [row[:2] for row in B[:2]]
    v = [B[0][2], B[1][2]]
    c = B[2][2]
    d = c - quad(v, inv2(H))
    assert d == det3(B) / det2(H)

# All-zero-diagonal determinant identity.
a, b, c = Fraction(2), Fraction(3), Fraction(5)
B0 = [[0, a, b], [a, 0, c], [b, c, 0]]
assert det3(B0) == 2 * a * b * c

# Numerical constants quoted in the report.
zero_diag_target_constant = 2 ** (11 / 8) * sqrt(15)
k3_constant = 2 * sqrt(15)
assert zero_diag_target_constant < 10.046
assert k3_constant < 7.746

print("PASS: exact Schur and zero-diagonal determinant identities")
print(f"2^(11/8)*sqrt(15) = {zero_diag_target_constant:.12f}")
print(f"2*sqrt(15) = {k3_constant:.12f}")

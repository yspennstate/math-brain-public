import math


def det3(M):
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def cof3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return [
        [e * i - f * h, -(d * i - f * g), d * h - e * g],
        [-(b * i - c * h), a * i - c * g, -(a * h - b * g)],
        [b * f - c * e, -(a * f - c * d), a * e - b * d],
    ]


def inner(A, B):
    return sum(A[i][j] * B[i][j] for i in range(3) for j in range(3))


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]


tests = [
    (
        [[1, 2, 0], [-1, 3, 1], [2, 0, 4]],
        [[2, -1, 1], [0, 1, 3], [1, 2, -2]],
    ),
    (
        [[0, 1, 2], [3, -1, 0], [1, 4, 2]],
        [[1, 0, -2], [2, 3, 1], [-1, 2, 1]],
    ),
    (
        [[2, 0, 1], [1, 1, 0], [0, -1, 3]],
        [[-1, 2, 0], [0, 1, 1], [2, 0, 1]],
    ),
]

for C, N in tests:
    lhs = det3(add(C, N))
    rhs = det3(C) + inner(cof3(C), N) + inner(C, cof3(N)) + det3(N)
    assert lhs == rhs

rho = math.sqrt(3.0 / 5.0)
c = 0.5 * rho
beta = (3.0 / 16.0) * rho
partner_grades = [c**3, c * c * beta, c * beta * beta, beta**3]
ledger_grades = [0.25, rho / 4.0, rho * rho / 4.0, rho**3 / 4.0]

B = math.gamma(1.0 / 6.0) * math.gamma(1.0 / 12.0) / math.gamma(1.0 / 4.0)
base = math.e / (6.0 * math.sqrt(2.0)) * B
ledger_cross_density = base * 16.0 ** (1.0 / 6.0) / rho
partner_zero_child_density = base / beta

assert abs(rho - 0.7745966692414834) < 1e-15
assert abs(c - 0.3872983346207417) < 1e-15
assert abs(beta - 0.14523687548277814) < 1e-15
assert abs(partner_grades[0] - 0.05809475019311126) < 1e-15
assert abs(partner_grades[1] - 0.021785531322416726) < 1e-15
assert abs(partner_grades[2] - 0.00816957424590627) < 1e-15
assert abs(partner_grades[3] - 0.0030635903422148517) < 1e-15
assert abs(ledger_grades[1] - 0.19364916731037085) < 1e-15
assert abs(ledger_grades[2] - 0.15) < 1e-15
assert abs(ledger_grades[3] - 0.11618950038622251) < 1e-15
assert abs(ledger_cross_density - 11.590503445296413) < 1e-12
assert abs(partner_zero_child_density - 38.941651385621334) < 1e-12

print("determinant_grade_identity=PASS")
print(f"rho={rho:.15f}")
print(f"c={c:.15f}")
print(f"beta={beta:.15f}")
print("partner_grades=" + ",".join(f"{x:.15f}" for x in partner_grades))
print("ledger_grades=" + ",".join(f"{x:.15f}" for x in ledger_grades))
print(f"ledger_cross_density_constant={ledger_cross_density:.15f}")
print(f"partner_zero_child_density_constant={partner_zero_child_density:.15f}")
print("QFORM_B08_R22_CHECK_PASS")

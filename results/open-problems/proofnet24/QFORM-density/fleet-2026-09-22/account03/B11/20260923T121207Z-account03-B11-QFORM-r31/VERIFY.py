import math


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


rt2 = math.sqrt(2.0)
rows = [
    (1 / rt2, 0.0, 0.0),
    (1 / rt2, 0.0, 0.0),
    (0.0, 1 / rt2, 0.0),
    (0.0, 1 / rt2, 0.0),
    (0.0, 0.0, 1 / rt2),
    (0.0, 0.0, 1 / rt2),
]
G = [[sum(r[a] * r[b] for r in rows) for b in range(3)] for a in range(3)]
assert max(abs(G[i][j] - (1.0 if i == j else 0.0)) for i in range(3) for j in range(3)) < 1e-12

M = [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]]
assert abs(det3(M) + 1.0) < 1e-12


def volume(ids):
    return det3([rows[i] for i in ids]) ** 2


v_left = volume([0, 2, 4])
v_right = volume([1, 3, 5])
assert abs(v_left - 1 / 8) < 1e-12
assert abs(v_right - 1 / 8) < 1e-12

partner_bound = 3.0 * (v_left * v_right) ** (-1.0 / 6.0)
assert abs(partner_bound - 6.0) < 1e-12
zero_bank_constant = 6.0 * math.exp(2.0 / 3.0)

# Check det M0 = -m23^2 beta in the zero-bank normal form.
m11, m12, m13, m23 = 3.0, 2.0, -0.5, 1.25
beta = m11 - 2.0 * m12 * m13 / m23
M0 = [[m11, m12, m13], [m12, 0.0, m23], [m13, m23, 0.0]]
assert abs(det3(M0) + m23 * m23 * beta) < 1e-12

print("parseval_max_error=", max(abs(G[i][j] - (1.0 if i == j else 0.0)) for i in range(3) for j in range(3)))
print("det_M=", det3(M))
print("triple_volumes=", v_left, v_right)
print("partner_bound=", partner_bound)
print("zero_bank_constant=", zero_bank_constant)
print("generic_beta=", beta)
print("generic_det_identity_error=", abs(det3(M0) + m23 * m23 * beta))
print("QFORM_B11_R31_EXACT_NULL_ZERO_BANK_CHECK_PASS")

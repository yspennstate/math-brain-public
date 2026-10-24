import math


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


# Section 4: account02/B16 constant with M=1, gamma=sqrt(2), kappa=2.
sharp = 3 * 2 ** (2 / 3) * 4 ** (-1 / 3)
assert abs(sharp - 3.0) < 1e-12

# Section 5: designated account04/B16 transverse branch, G=1 and gamma^2*kappa=4.
partner = 12 * 4 ** (-1 / 3)
assert partner < 7.56

# The stronger pair-cap corollary for M=2.
paircap = 3 * 2 ** (2 / 3)
assert paircap < 4.763

# Distributed (L,V) frame: four nonzero physical rows each have leverage 1/2.
leverages = [(1 / 2) ** 2 + (1 / 2) ** 2 for _ in range(4)] + [0.0]
assert all(x <= 0.5 for x in leverages)
assert all(abs(x - 0.5) < 1e-15 for x in leverages[:4])

# Sharp barrier after fixing the outer hub and X4: quadratic matrix in (X2,X1,X3).
B = [[0.0, 1.0, -1.0], [1.0, 1.0, 1.0], [-1.0, 1.0, 1.0]]
trace = sum(B[i][i] for i in range(3))
pair_sum = (
    B[0][0] * B[1][1] - B[0][1] * B[1][0]
    + B[0][0] * B[2][2] - B[0][2] * B[2][0]
    + B[1][1] * B[2][2] - B[1][2] * B[2][1]
)
determinant = det3(B)
# char poly = lambda^3 - trace lambda^2 + pair_sum lambda - determinant
#            = lambda^3 - 2 lambda^2 - 2 lambda + 4
#            = (lambda-2)(lambda^2-2).
assert abs(trace - 2.0) < 1e-15
assert abs(pair_sum + 2.0) < 1e-15
assert abs(determinant + 4.0) < 1e-15

print(f"sharp_paircap_constant={sharp:.15f}")
print(f"designated_partner_constant={partner:.15f}")
print(f"orthogonal_paircap_constant={paircap:.15f}")
print(f"distributed_row_leverages={leverages}")
print(f"conditional_B_trace={trace:.1f}")
print(f"conditional_B_pair_sum={pair_sum:.1f}")
print(f"conditional_B_det={determinant:.1f}")
print("conditional_B_charpoly=(lambda-2)(lambda^2-2)")
print("STATUS=PASS")

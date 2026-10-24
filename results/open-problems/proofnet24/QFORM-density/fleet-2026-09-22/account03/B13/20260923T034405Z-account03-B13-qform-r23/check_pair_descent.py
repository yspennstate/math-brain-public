from fractions import Fraction
import math
import random

# Analytic constants from REPORT.md.
A0 = 5.2
u0 = 10.0
Jhyp = (32.0 * math.exp(-u0) * math.sqrt(2.0)
        * ((A0 + u0) ** 1.5 + math.gamma(2.5))
        + math.sqrt(A0 + u0))
Chyp_to_a = Jhyp ** (2.0 / 3.0) * (4.0 / 3.0) ** (1.0 / 6.0)
Cpair = 2.0 ** (5.0 / 3.0)
h = 3.0 / 5.0
q = 2.0 * h
A_h = (6.0 * math.sqrt(math.e / q) / (3.0 - 2.0 * q)) ** (2.0 / 3.0)
paid_L3 = A_h * 4.0 ** (1.0 / 6.0)
resource = 31.0 / 512.0
residual_Z_coeff = paid_L3 * resource ** (-1.0 / 6.0)
isolated_Linf_Z = Cpair * residual_Z_coeff

assert Chyp_to_a < 2.654
assert Chyp_to_a < Cpair
assert paid_L3 < 7.681
assert residual_Z_coeff < 12.257
assert isolated_Linf_Z < 38.912
assert abs((1.0 - 2.0 / 4.0) / 9.0 - 1.0 / 18.0) < 1e-15


def det2(a, b, c, d):
    return a * d - b * c


def joint_pair_mass(M, i, j):
    ans = Fraction(0)
    for k in range(len(M)):
        if k == i:
            continue
        for l in range(len(M[0])):
            if l == j:
                continue
            ans += det2(M[i][j], M[i][l], M[k][j], M[k][l]) ** 2
    return ans

# Exact-rational checks of E_ij = ||bT-qp^T||_F^2,
# including both zero-edge and nonzero-edge cases.
for seed in range(23, 123):
    random.seed(seed)
    M = [[Fraction(random.randint(-4, 4)) for _ in range(5)] for _ in range(4)]
    i, j = 1, 2
    lhs = joint_pair_mass(M, i, j)
    b = M[i][j]
    rhs = Fraction(0)
    for k in range(len(M)):
        if k == i:
            continue
        for l in range(len(M[0])):
            if l == j:
                continue
            rhs += (b * M[k][l] - M[k][j] * M[i][l]) ** 2
    assert lhs == rhs
    if b != 0:
        schur = Fraction(0)
        for k in range(len(M)):
            if k == i:
                continue
            for l in range(len(M[0])):
                if l == j:
                    continue
                s = M[k][l] - M[k][j] * M[i][l] / b
                schur += s * s
        assert lhs == b * b * schur
    else:
        p2 = sum(M[i][l] ** 2 for l in range(len(M[0])) if l != j)
        q2 = sum(M[k][j] ** 2 for k in range(len(M)) if k != i)
        assert lhs == p2 * q2

print(f"Jhyp_upper={Jhyp:.15f}")
print(f"hyperbolic_cross_constant={Chyp_to_a:.15f}")
print(f"pair_L32_constant={Cpair:.15f}")
print(f"E2_paid_L3_constant={paid_L3:.15f}")
print(f"Schur_residual_Z_constant={residual_Z_coeff:.15f}")
print(f"independent_pair_Linf_Z_constant={isolated_Linf_Z:.15f}")
print("exact_joint_pair_identity_trials=100")
print("QFORM_B13_R23_PAIR_DESCENT_CHECK_PASS")

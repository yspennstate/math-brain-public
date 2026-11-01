from fractions import Fraction


def convergents(digits):
    p_nm2, p_nm1 = 0, 1
    q_nm2, q_nm1 = 1, 0
    ps, qs = [], []
    for a in digits:
        p = a * p_nm1 + p_nm2
        q = a * q_nm1 + q_nm2
        ps.append(p)
        qs.append(q)
        p_nm2, p_nm1 = p_nm1, p
        q_nm2, q_nm1 = q_nm1, q
    return ps, qs


def cf_value(digits):
    x = Fraction(digits[-1], 1)
    for a in reversed(digits[:-1]):
        x = Fraction(a, 1) + 1 / x
    return x


def dist_to_integer(x):
    n = x.numerator // x.denominator
    f = x - n
    return min(f, 1 - f)


ALPHA_DIGITS = [
    0, 2, 1, 3, 2, 2, 1, 3, 1, 2, 3, 2, 1, 2,
    2, 3, 1, 2, 3, 1, 2, 2, 3, 1, 2, 3, 2, 1,
]
BETA_DIGITS = [
    0, 1, 2, 3, 1, 2, 2, 1, 3, 2, 1, 2, 3, 1, 1,
    2, 3, 2, 1, 3, 2, 2, 1, 3, 1, 2, 3, 2, 1, 2,
]

A_num, B_den = convergents(ALPHA_DIGITS)
C_num, D_den = convergents(BETA_DIGITS)
alpha = cf_value(ALPHA_DIGITS)
beta = cf_value(BETA_DIGITS)
A_alpha = max(ALPHA_DIGITS[1:])
A_beta = max(BETA_DIGITS[1:])
C_beta = A_beta + 2

portal_checks = 0
tail_identity_checks = 0
phase_difference_checks = 0
modular_zero_checks = 0
strip_population_checks = 0

for n in range(2, 12):
    eta = cf_value(BETA_DIGITS[n + 2 :])
    reconstructed = (
        Fraction(C_num[n + 1], 1) * eta + C_num[n]
    ) / (
        Fraction(D_den[n + 1], 1) * eta + D_den[n]
    )
    assert reconstructed == beta

    P_tail, Q_tail = convergents(BETA_DIGITS[n + 2 :])
    for j in range(min(6, len(P_tail))):
        assert (
            Q_tail[j] * D_den[n] + P_tail[j] * D_den[n + 1]
            == D_den[n + j + 2]
        )
        tail_identity_checks += 1

    D = D_den[n]
    matches = [
        m
        for m in range(len(B_den) - 2)
        if B_den[m + 1] <= D < B_den[m + 2]
    ]
    if not matches:
        continue
    m = matches[-1]
    M = B_den[m + 1]
    A_mp1 = A_num[m + 1]

    for z in range(-8, 9):
        for v in range(-8, 9):
            if z == 0 and v == 0:
                continue
            q0 = z * D_den[n] + v * D_den[n + 1]
            if q0 == 0:
                continue
            q = abs(q0)
            R = max(abs(z), abs(v))
            s = abs(Fraction(v, 1) - Fraction(z, 1) * eta)
            Dcal = Fraction(D_den[n + 1], 1) * eta + D_den[n]
            exact_beta_error = abs(
                Fraction(q0, 1) * beta
                - Fraction(z * C_num[n] + v * C_num[n + 1], 1)
            )
            assert exact_beta_error == s / Dcal

            rho = dist_to_integer(Fraction(q * A_mp1, M))
            lhs = q * dist_to_integer(q * alpha) * dist_to_integer(q * beta)
            rhs = (
                2 * C_beta * R * s * rho
                + C_beta**2 * R**2 * D * s / Fraction(M * M, 1)
            )
            assert lhs <= rhs
            portal_checks += 1

            if q0 % M == 0:
                det = D_den[n + 1] * v + D_den[n] * z
                assert det == q0
                assert Fraction(R, 1) >= Fraction(M, D_den[n] + D_den[n + 1])
                modular_zero_checks += 1

    vectors = [
        (z, v)
        for z in range(-4, 5)
        for v in range(-4, 5)
        if (z, v) != (0, 0)
    ]
    for i in range(0, len(vectors), 7):
        for j in range(i + 1, min(i + 8, len(vectors))):
            z, v = vectors[i]
            zp, vp = vectors[j]
            q01 = z * D_den[n] + v * D_den[n + 1]
            q02 = zp * D_den[n] + vp * D_den[n + 1]
            phase_distance = dist_to_integer(
                Fraction((q01 - q02) * A_mp1, M)
            )
            dz, dv = z - zp, v - vp
            qdiff = abs(dz * D_den[n] + dv * D_den[n + 1])
            rho_diff = dist_to_integer(Fraction(qdiff * A_mp1, M))
            assert phase_distance == rho_diff
            phase_difference_checks += 1

for n in range(2, 10):
    eta = cf_value(BETA_DIGITS[n + 2 :])
    _, Q_tail = convergents(BETA_DIGITS[n + 2 :])
    for j in range(1, min(6, len(Q_tail) - 1)):
        Q = Q_tail[j]
        Qnext = Q_tail[j + 1]
        if Qnext <= Q + 1:
            continue
        test_Z = {Q, min(Qnext - 1, Q + 3), (Q + Qnext - 1) // 2}
        for Z in test_Z:
            if not (Q <= Z < Qnext) or Z < 8:
                continue
            for S in [Fraction(1, 4), Fraction(1, 5), Fraction(1, 6), Fraction(2, Z)]:
                if S > Fraction(1, 4) or S < Fraction(2, Z):
                    continue
                count = sum(
                    1
                    for z in range(1, Q)
                    if dist_to_integer(Fraction(z, 1) * eta) <= S
                )
                assert Fraction(count, 1) >= 2 * Q * S - 7
                strip_population_checks += 1

print("HARD8-07 anisotropic portal verifier: PASS")
print(f"portal_checks={portal_checks}")
print(f"tail_identity_checks={tail_identity_checks}")
print(f"phase_difference_checks={phase_difference_checks}")
print(f"modular_zero_checks={modular_zero_checks}")
print(f"strip_population_checks={strip_population_checks}")

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


ALPHA_DIGITS = [0, 2, 1, 3, 2, 2, 1, 3, 1, 2, 3, 2, 1, 2, 2, 3, 1, 2]
BETA_DIGITS = [0, 1, 2, 3, 1, 2, 2, 1, 3, 2, 1, 2, 3, 1, 1, 2, 3, 2, 1, 3, 2]
A_num, B_den = convergents(ALPHA_DIGITS)
C_num, D_den = convergents(BETA_DIGITS)
A_beta = max(BETA_DIGITS[1:])

checks = 0
phase_checks = 0
norm_checks = 0

for n in range(1, 10):
    a = BETA_DIGITS[n + 2]
    eta_n = cf_value(BETA_DIGITS[n + 2 :])
    eta_np1 = cf_value(BETA_DIGITS[n + 3 :])
    assert eta_n == a + 1 / eta_np1

    for z in range(-12, 13):
        for v in range(-12, 13):
            if z == 0 and v == 0:
                continue
            zp = v - a * z
            vp = z
            q_old = z * D_den[n] + v * D_den[n + 1]
            q_new = zp * D_den[n + 1] + vp * D_den[n + 2]
            assert q_old == q_new

            ell_old = Fraction(v, 1) - Fraction(z, 1) * eta_n
            ell_new = Fraction(vp, 1) - Fraction(zp, 1) * eta_np1
            assert ell_new == -eta_np1 * ell_old

            R = max(abs(z), abs(v))
            Rp = max(abs(zp), abs(vp))
            assert Rp <= (A_beta + 1) * R
            assert z == vp
            assert v == zp + a * vp
            assert R <= (A_beta + 1) * Rp
            norm_checks += 1

            for m in range(0, min(8, len(B_den) - 1)):
                M = B_den[m + 1]
                A = A_num[m + 1]
                phase_old = Fraction(q_old * A, M)
                phase_new = Fraction(q_new * A, M)
                assert dist_to_integer(phase_old - phase_new) == 0
                phase_checks += 1
            checks += 1

print("HARD8-07 adjacent-frame conjugacy verifier: PASS")
print(f"coordinate_checks={checks}")
print(f"phase_checks={phase_checks}")
print(f"norm_distortion_checks={norm_checks}")

#!/usr/bin/env python3
"""Exact integer verifier for the HARD8-07 matched-scale strengthening.

Checks the matched denominator selection B_{m+1} <= D_n < B_{m+2},
its bounded-type comparison, and the centered modular coordinate identity.
This is a finite algebraic check, not a proof of Littlewood's conjecture.
"""

from fractions import Fraction


def convergents_zero(digits):
    p_nm2, p_nm1 = 0, 1
    q_nm2, q_nm1 = 1, 0
    out = []
    for a in [0] + list(digits):
        p = a * p_nm1 + p_nm2
        q = a * q_nm1 + q_nm2
        out.append((p, q))
        p_nm2, p_nm1 = p_nm1, p
        q_nm2, q_nm1 = q_nm1, q
    return out


def main():
    alpha_sets = [
        [1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 1, 3],
        [2] * 12,
        [3, 1, 2, 3, 1, 1, 2, 2, 3, 1, 2, 1],
    ]
    beta_sets = [
        [2, 1, 3, 2, 1, 2, 3, 1, 2, 1, 3, 2],
        [1] * 12,
        [3, 2, 1, 3, 2, 2, 1, 1, 3, 2, 1, 2],
    ]

    matched_scale_checks = 0
    modular_checks = 0

    for alpha_digits in alpha_sets:
        alpha_conv = convergents_zero(alpha_digits)
        A_alpha = max(alpha_digits)

        for beta_digits in beta_sets:
            beta_conv = convergents_zero(beta_digits)

            for n in range(4, min(len(beta_conv) - 1, 10)):
                _, D = beta_conv[n]
                _, Dp = beta_conv[n + 1]

                candidates = []
                for m in range(1, len(alpha_conv) - 2):
                    M = alpha_conv[m + 1][1]
                    Mnext = alpha_conv[m + 2][1]
                    if M <= D < Mnext:
                        candidates.append(m)
                if not candidates:
                    continue

                m = candidates[0]
                A_m, B_m = alpha_conv[m]
                A_mp1, M = alpha_conv[m + 1]
                _, Mnext = alpha_conv[m + 2]

                assert Fraction(D, A_alpha + 1) < M <= D < Mnext
                assert abs(A_mp1 * B_m - A_m * M) == 1
                matched_scale_checks += 1

                for R in range(1, min(5, D - 1) + 1):
                    for z in range(-R, R + 1):
                        for v in range(-R, R + 1):
                            if z == 0 and v == 0:
                                continue

                            q = abs(z * D + v * Dp)
                            inv_Bm = pow(B_m, -1, M)
                            residue = (q * inv_Bm) % M
                            x_centered = residue if residue <= M // 2 else residue - M

                            r = (q * A_mp1) % M
                            norm_num = min(r, M - r)
                            assert abs(x_centered) == norm_num
                            modular_checks += 1

    print("HARD8-07 matched-scale exact verifier: PASS")
    print(f"matched_scale_checks={matched_scale_checks}")
    print(f"modular_checks={modular_checks}")


if __name__ == "__main__":
    main()

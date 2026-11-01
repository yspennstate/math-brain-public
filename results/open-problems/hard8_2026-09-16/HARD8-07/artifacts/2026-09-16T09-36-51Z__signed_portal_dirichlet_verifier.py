#!/usr/bin/env python3
"""Exact finite verifier for the HARD8-07 signed-portal checkpoint.

This script uses only Python standard-library integer arithmetic and
fractions.Fraction.  It checks finite continued-fraction instances of the
integer identities and inequalities used in the report.  It does NOT prove
Littlewood's conjecture and it does not use solver timeouts as evidence.
"""

from fractions import Fraction
from itertools import product


def cf_value(digits):
    """Exact [0; digits]."""
    x = Fraction(digits[-1], 1)
    for a in reversed(digits[:-1]):
        x = a + 1 / x
    return 1 / x


def convergents_zero(digits):
    """Convergents to [0; digits], including 0/1 as entry 0."""
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


def centered_norm_num(a, m):
    r = a % m
    return min(r, m - r)


def main():
    lemma_checks = 0
    portal_checks = 0
    modular_checks = 0
    dirichlet_checks = 0

    # Exhaustive finite check of Lemma 5.1 for bounded finite CFs.
    for A in range(1, 5):
        for length in range(1, 6):
            for digits in product(range(1, A + 1), repeat=length):
                x = cf_value(digits)
                P, Q = x.numerator, x.denominator
                for b in range(1, Q):
                    lhs = Fraction(centered_norm_num(b * P, Q), Q)
                    rhs = Fraction(1, (A + 2) * b)
                    assert lhs >= rhs, (A, digits, P, Q, b, lhs, rhs)
                    lemma_checks += 1

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

    for alpha_digits in alpha_sets:
        alpha_conv = convergents_zero(alpha_digits)
        for beta_digits in beta_sets:
            beta_conv = convergents_zero(beta_digits)
            A_beta = max(beta_digits)

            for n in range(4, min(len(beta_conv) - 1, 10)):
                _, D = beta_conv[n]
                _, Dp = beta_conv[n + 1]

                # Exact canonical choice M^3 <= D^2 < B_next^3, when
                # this finite truncation contains such an index.
                candidates = []
                for m in range(1, len(alpha_conv) - 2):
                    M = alpha_conv[m + 1][1]
                    Bnext = alpha_conv[m + 2][1]
                    if M ** 3 <= D ** 2 < Bnext ** 3:
                        candidates.append(m)
                if not candidates:
                    continue

                m = candidates[0]
                A_m, B_m = alpha_conv[m]
                A_mp1, M = alpha_conv[m + 1]
                assert abs(A_mp1 * B_m - A_m * M) == 1

                for R in range(1, min(5, D - 1) + 1):
                    theta1_num = (D * A_mp1) % M
                    theta2_num = (Dp * A_mp1) % M
                    best = None

                    for z in range(-R, R + 1):
                        for v in range(-R, R + 1):
                            if z == 0 and v == 0:
                                continue

                            q = abs(z * D + v * Dp)

                            # Report equation (5.2).
                            assert Fraction(q, 1) >= Fraction(
                                D, (A_beta + 2) * R
                            ), (beta_digits, n, R, z, v, D, Dp, q)
                            portal_checks += 1

                            # Report equation (6.3): centered alpha-frame
                            # coefficient equals the modular norm with A_{m+1}.
                            inv_Bm = pow(B_m, -1, M)
                            residue = (q * inv_Bm) % M
                            x_centered = residue if residue <= M // 2 else residue - M
                            norm_num = centered_norm_num(q * A_mp1, M)
                            assert abs(x_centered) == norm_num
                            modular_checks += 1

                            # Exact finite check of the two-dimensional
                            # Dirichlet scale used in (8.4).
                            rr = (z * theta1_num + v * theta2_num) % M
                            val = Fraction(centered_norm_num(rr, M), M)
                            if best is None or val < best:
                                best = val

                    assert best is not None
                    assert R * R * best <= 1
                    dirichlet_checks += 1

    print("HARD8-07 signed-portal exact verifier: PASS")
    print(f"lemma_checks={lemma_checks}")
    print(f"portal_checks={portal_checks}")
    print(f"modular_checks={modular_checks}")
    print(f"dirichlet_checks={dirichlet_checks}")


if __name__ == "__main__":
    main()

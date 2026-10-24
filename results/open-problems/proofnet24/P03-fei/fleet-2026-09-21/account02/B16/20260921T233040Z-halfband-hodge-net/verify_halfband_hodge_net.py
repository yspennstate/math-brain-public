#!/usr/bin/env python3
from fractions import Fraction
import json, math


def main():
    eps = Fraction(11, 288)
    assert eps == Fraction(11, 192) * Fraction(2, 3)

    exact_checks = 0
    for a_num in range(-7, 8):
        for c_num in range(-7, 8):
            for x_num in (1, 2, 3, 5, 7):
                x = Fraction(x_num, 11)
                a = Fraction(a_num, 5)
                c = Fraction(c_num, 7)
                H = a + x * c
                K = -x * a * c
                assert a * a - K == a * H
                assert K == Fraction(1, 2) * (a * a + x * x * c * c - H * H)
                exact_checks += 2

    rows = []
    for D in (128, 129, 160, 192, 256, 512):
        n = D - 1
        d = (D + 1) // 2
        m = 2 ** (d - 1) - 1
        T = (2 * n) ** -0.5

        # Terminal Hodge-defect energy from the collision theorem.
        E_H = 16 * math.pi * T**3 / math.sqrt(m)

        # Half-band source condition gives E_1/T^6 <= 21/524288.
        terminal_ratio = 21 / 524288
        retained_energy = (1 + math.sqrt(terminal_ratio)) ** 2 * T**6
        coarse_retained_envelope = Fraction(33, 32) * T**6
        assert retained_energy <= coarse_retained_envelope

        # Four charged triples, epsilon*=11/288.
        residual_bound = (11 / 288) * 4 * math.sqrt(float(coarse_retained_envelope) * E_H)
        closed_form = (
            (11 / 18)
            * math.sqrt(33 * math.pi / 32)
            * T ** 4.5
            * m ** -0.25
        )
        assert math.isclose(residual_bound, closed_form, rel_tol=1e-13, abs_tol=1e-30)

        central_asymptotic = 11 / (864 * n**3)
        J = 8 * n / 2**D
        rows.append(
            {
                "D": D,
                "n": n,
                "d": d,
                "m_bits": d - 1,
                "residual_bound": residual_bound,
                "central_asymptotic": central_asymptotic,
                "residual_over_central_asymptotic": residual_bound / central_asymptotic,
                "J": J,
                "residual_over_J": residual_bound / J,
            }
        )

    print(
        json.dumps(
            {
                "status": "PASS",
                "exact_algebra_checks": exact_checks,
                "central_multiplier": str(eps),
                "ward_lock": "(11/192)*(2/3)=11/288",
                "rows": rows,
                "note": (
                    "Finite arithmetic checks support the displayed algebra and constants. "
                    "They are not an independent proof of FEI or of compiler booking/nonreuse."
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

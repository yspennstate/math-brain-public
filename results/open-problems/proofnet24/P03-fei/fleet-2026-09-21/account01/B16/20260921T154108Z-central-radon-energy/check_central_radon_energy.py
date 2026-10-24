#!/usr/bin/env python3
"""Exact checks for the B16 central Radon energy-distance payment.

This is a finite exact checker for the new source-side lemma.  It does not
check the read-once certificate and does not claim full FEI.
"""
from fractions import Fraction
from itertools import product
import json

def fwht_int(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def hats(vals):
    N = len(vals)
    return [Fraction(x, N) for x in fwht_int(vals)]

def qflip_profile(vals):
    N = len(vals)
    return [
        Fraction(sum(vals[x] != vals[x ^ w] for x in range(N)), N)
        for w in range(N)
    ]

def central_bank(vals):
    m = len(vals).bit_length() - 1
    h = hats(vals)
    odd = [
        (U, h[U] * h[U], U.bit_count())
        for U in range(1, 1 << m)
        if U.bit_count() % 2
    ]
    T = Fraction(1, 2)
    B = Fraction(0)
    for _, a, k in odd:
        for _, b, ell in odd:
            r = k + ell
            integ = T ** (r + 3) / ((r + 2) * (r + 3))
            B += 16 * a * b * integ
    alpha = h[0]
    E = alpha * (1 - alpha)
    damped = sum(a * Fraction(1, 2 ** (k - 1)) for _, a, k in odd)
    return B, E, damped, h

def eta_coord_from_f(bits, n, i):
    others = [j for j in range(n) if j != i]
    vals = []
    for y in range(1 << (n - 1)):
        x = 0
        for r, j in enumerate(others):
            if (y >> r) & 1:
                x |= 1 << j
        vals.append(1 if bits[x] != bits[x ^ (1 << i)] else 0)
    return tuple(vals)

def main():
    eta_functions = 0
    pointwise_t_checks = 0
    max_E2_ratio = Fraction(0)
    max_E2_case = None

    for m in range(1, 4):
        N = 1 << m
        for vals in product((0, 1), repeat=N):
            h = hats(vals)
            alpha = h[0]
            E = alpha * (1 - alpha)
            p = qflip_profile(vals)
            hp = hats(p)

            assert hp[0] == 2 * E
            for U in range(1, N):
                assert hp[U] == -2 * h[U] * h[U]

            for t in (
                Fraction(0), Fraction(1, 8), Fraction(1, 4),
                Fraction(3, 8), Fraction(1, 2)
            ):
                delta = sum(
                    hp[U] * (t ** U.bit_count() - (-t) ** U.bit_count())
                    for U in range(N)
                )
                delta_formula = -4 * sum(
                    h[U] * h[U] * t ** U.bit_count()
                    for U in range(1, N)
                    if U.bit_count() % 2
                )
                assert delta == delta_formula

                energy_distance = 8 * sum(
                    h[U] * h[U] * t ** (2 * U.bit_count())
                    for U in range(1, N)
                    if U.bit_count() % 2
                )
                assert delta * delta <= 2 * E * energy_distance
                pointwise_t_checks += 1

            B, E2, damped, _ = central_bank(vals)
            assert E2 == E
            if E:
                assert B <= E * E / 40
                ratio = B / (E * E)
                if ratio > max_E2_ratio:
                    max_E2_ratio = ratio
                    max_E2_case = {
                        "m": m,
                        "alpha": str(alpha),
                        "bank": str(B),
                        "ratio": str(ratio),
                    }
            else:
                assert B == 0
            if damped:
                assert B <= damped * damped / 40
            else:
                assert B == 0

            eta_functions += 1

    boolean_functions = 0
    coordinate_cuts = 0
    max_J_ratio = Fraction(0)
    max_J_case = None

    for n in range(1, 4):
        N = 1 << n
        for bits in product((0, 1), repeat=N):
            total_B = Fraction(0)
            J = Fraction(0)
            for i in range(n):
                eta = eta_coord_from_f(bits, n, i)
                B, _, _, h = central_bank(eta)
                alpha = h[0]
                beta = min(alpha, 1 - alpha)
                total_B += B
                J += beta
                coordinate_cuts += 1

            if J:
                assert total_B <= J / 270
                ratio = total_B / J
                if ratio > max_J_ratio:
                    max_J_ratio = ratio
                    max_J_case = {
                        "n": n,
                        "bank": str(total_B),
                        "J": str(J),
                        "ratio": str(ratio),
                    }
            else:
                assert total_B == 0
            boolean_functions += 1

    # Sharpness of B <= E^2/40 at a one-bit affine cut eta=(0,1).
    B, E, _, _ = central_bank((0, 1))
    assert B == E * E / 40

    result = {
        "status": "PASS",
        "eta_functions_exact": eta_functions,
        "pointwise_rational_t_checks": pointwise_t_checks,
        "boolean_functions_exact": boolean_functions,
        "coordinate_cut_checks": coordinate_cuts,
        "max_bank_over_E2": str(max_E2_ratio),
        "max_bank_over_E2_float": float(max_E2_ratio),
        "sharp_E2_case": max_E2_case,
        "max_observed_bank_over_J_n_le_3": str(max_J_ratio),
        "max_observed_bank_over_J_n_le_3_float": float(max_J_ratio),
        "max_J_case": max_J_case,
        "proved_uniform_J_bound": "1/270",
        "read_once_certificate_rerun": False,
        "full_FEI_claimed": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()

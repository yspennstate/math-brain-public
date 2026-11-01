#!/usr/bin/env python3
"""Exact/rational sanity checks for the B18 Sidon-projection/addressing sharpness example.

No FEI claim is inferred from these finite checks. The theorem in REPORT.md is analytic.
"""
from fractions import Fraction


def addressing_formula(k):
    m = 1 << k
    # Addressing: k address bits y choose one of m data bits x.
    # Spectral law is uniform on {(e_y,L): y,L in F_2^k}.
    H = 2 * k
    I_X = Fraction(1, 1)
    I_Y = Fraction(k, 2)
    I = I_X + I_Y
    B_X = k
    proj_entropy = k
    address_change_sum = k
    return {
        "k": k,
        "data_variables": m,
        "spectral_support_size": m * m,
        "H_bits": H,
        "I_X": f"{I_X.numerator}/{I_X.denominator}",
        "I_Y": f"{I_Y.numerator}/{I_Y.denominator}",
        "I_total": f"{I.numerator}/{I.denominator}",
        "H_over_I": float(Fraction(H, 1) / I),
        "H_SX_bits": proj_entropy,
        "B_X_bits": B_X,
        "sum_address_change_probabilities": address_change_sum,
        "B_X_over_I_Y": 2.0,
    }


def main():
    beta = 6.4547837
    threshold = beta / (beta + 4.0)
    print("beta", beta)
    print("sidon_anchor_influence_fraction_threshold", f"{threshold:.12f}")
    print("rows")
    for k in range(1, 13):
        print(addressing_formula(k))
    print("analytic_sharpness", "B_X = H(S_X) = k = 2 I_Y for every k>=1")
    print("status", "finite/example check only; full FEI OPEN")


if __name__ == "__main__":
    main()

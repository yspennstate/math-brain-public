#!/usr/bin/env python3
"""Descriptive checker for B15 level-conditioned negative entropy credit.

The proof is analytic in REPORT.md. This script checks the exact finite-family
formulas numerically and the identity U-U_level = mutual-information credit as
implemented from the two coding expressions. Standard library only.
"""

from math import comb, log2, lgamma, log

LN2 = log(2.0)
LOG2E = 1.0 / LN2


def family(m: int):
    a = 2.0 ** (1 - m)
    delta = m * a
    I = 1.0 + delta

    p1 = (1.0 - a) ** 2
    tail = (2**m - 1) * a * a
    H = -p1 * log2(p1) - tail * log2(a * a)

    P = [0.0] * (m + 2)
    P[1] = p1
    for r in range(1, m + 1):
        P[r + 1] = comb(m, r) * a * a

    HK = -sum(x * log2(x) for x in P if x > 0.0)
    IHq = I * log2(I) + delta * (m - 1)
    Elogfac = sum(P[k] * lgamma(k + 1) / LN2 for k in range(1, m + 2))
    U = HK + IHq - Elogfac

    Ulev = HK
    for r in range(1, m + 1):
        k = r + 1
        qroot = 1.0 / k
        qleaf = r / (m * k)
        Hqk = -qroot * log2(qroot) - m * qleaf * log2(qleaf)
        Ulev += P[k] * (k * Hqk - lgamma(k + 1) / LN2)

    credit = U - Ulev
    assert H <= Ulev + 1e-12
    assert Ulev <= U + 1e-12

    return {
        "m": m,
        "delta": delta,
        "H/delta": H / delta,
        "U/delta": U / delta,
        "Ulev/delta": Ulev / delta,
        "credit/delta": credit / delta,
    }


def main():
    print("target_H_ratio", 4.0)
    print("target_Ulev_ratio", 3.0 + LOG2E)
    print("m delta H/delta U/delta Ulev/delta credit/delta")
    for m in (4, 8, 12, 16, 20, 30, 40):
        z = family(m)
        print(
            z["m"],
            f'{z["delta"]:.17g}',
            f'{z["H/delta"]:.15f}',
            f'{z["U/delta"]:.15f}',
            f'{z["Ulev/delta"]:.15f}',
            f'{z["credit/delta"]:.15f}',
        )
    print("PASS")


if __name__ == "__main__":
    main()

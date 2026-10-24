#!/usr/bin/env python3
"""Exact-arithmetic self-check for R14/P0157 growing staircase family.

This verifies only finite algebraic identities/sanity checks. It is not a
certificate of the asymptotic probability theorem.
"""
from fractions import Fraction


def family(k, m):
    assert k >= 2 and m % 2 == 0
    n = 8 * m ** (2*k + 6)
    M = m ** (2*k - 1)
    d = m*m
    numer_x = M * (d-1)**2
    assert numer_x % 4 == 0
    x = 3 * m ** (2*k + 5) + numer_x // 4
    N3 = 2 * m ** (2*k + 6) - x
    N1 = 6 * m ** (2*k + 6) + x - M
    assert N1 >= 0 and N3 >= 0 and N1 + N3 + M == n

    ell = N1 + 3*N3 + d*M
    P = 24*m**7 - 12*m**6 - m**4 + 4*m**2 - 3
    ell_formula = (m ** (2*k - 1) * P) // 2
    assert ell == ell_formula
    assert ell % 2 == 0

    s2 = 6*N3 + d*(d-1)*M
    deficit = ell - s2
    assert deficit == 12 * m ** (2*k + 5)
    delta = Fraction(deficit, ell)
    assert delta == Fraction(24*m**6, P)

    exi2 = Fraction(12*N3 + d*(d-1)**2*M, ell)
    mean = Fraction(s2, ell)
    var = exi2 - mean*mean
    Q = var / (d*delta)

    qnum = (
        576*m**14 - 528*m**13 - 456*m**12 - 240*m**11
        + 118*m**10 + 336*m**9 - 151*m**8 - 144*m**7
        + 20*m**6 + 70*m**4 - 42*m**2 + 9
    )
    qformula = Fraction(qnum, 24*m**8*P)
    assert Q == qformula

    third_sum = N1 + 27*N3 + d**3*M
    assert Fraction(d**3*M, n) == Fraction(1, 8*m)

    def exponent(r):
        return r*(2*k-1) + (2*r-2)*2 - (r-1)*(2*k+5)
    for r in range(2, k+3):
        assert exponent(r) == 2*k + 1 - 2*r
    assert exponent(k) == 1
    assert exponent(k+1) == -1

    return {
        "k": k, "m": m, "n": n, "M": M, "d": d,
        "N1": N1, "N3": N3, "ell": ell,
        "delta": delta, "Q": Q, "third_sum": third_sum,
        "exp_k": exponent(k), "exp_k1": exponent(k+1),
    }


def main():
    for m in (10, 12, 20):
        qs = []
        for k in range(2, 9):
            row = family(k, m)
            qs.append(row["Q"])
        assert all(q == qs[0] for q in qs)

    print("P0157 growing-staircase exact self-check")
    print("checked k=2..8 and m in {10,12,20}")
    for m in (10, 12, 20):
        row = family(2, m)
        print(
            f"m={m}: delta={row['delta']} "
            f"Q={row['Q']} ~= {float(row['Q']):.15f}; "
            f"hub-tree exponents r=k:{row['exp_k']}, r=k+1:{row['exp_k1']}"
        )
    print("Q is exactly independent of k on the checked grid.")
    print("All exact family identities and exponent identities pass.")
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()

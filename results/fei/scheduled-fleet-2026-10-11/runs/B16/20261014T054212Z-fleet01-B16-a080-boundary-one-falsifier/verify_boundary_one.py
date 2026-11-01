#!/usr/bin/env python3
"""High-precision reconstruction of the A080 boundary-one family.

The analytic sign is proved in BOUNDARY_ONE_FALSIFIER.tex.  This program
reconstructs the exact closed formulas, the unequal-child GU expression,
and the exact middle-term identity at 100 Decimal digits.
"""

from decimal import Decimal as D, getcontext

getcontext().prec = 100
ONE, TWO, FOUR = D(1), D(2), D(4)
LN2 = TWO.ln()


def log2(x):
    return x.ln() / LN2


def cent(x):
    return D(0) if x == 0 else -x * log2(x)


def u_types(types):
    P = ONE
    for r, k in types:
        P *= (ONE - TWO ** (-r)) ** k
    p0 = (TWO * P - ONE) ** 2
    U = cent(p0)
    for r, k in types:
        e = TWO ** (-r)
        om = ONE - e
        L = -log2(om)
        d = D(r) - D(r) / (TWO * om)
        U += D(k) * (FOUR * P * e * d + FOUR * P * L * (om - P))
    return U


def stats(r):
    e = TWO ** (-r)
    k = 2 ** r
    P = (ONE - e) ** k
    I = TWO * P * D(k * r) * e / (ONE - e)
    U = u_types([(r, k)])
    short = u_types([(r - 1, 1), (r, k - 1)])
    deleted = u_types([(r, k - 1)])
    G = D(k * r) * (U - (short + deleted) / TWO)

    d = D(r) - D(r) / (TWO * (ONE - e))
    M = FOUR * P * D(k) * e * d
    Pm = P / (ONE - e)
    Pp = P * (ONE - TWO * e) / (ONE - e)
    ds = D(r - 1) - D(r - 1) / (TWO * (ONE - TWO * e))
    Mm = FOUR * Pm * D(k - 1) * e * d
    Mp = FOUR * Pp * (TWO * e * ds + D(k - 1) * e * d)
    delta_M = M - (Mm + Mp) / TWO
    exact_delta = TWO * P * e / (ONE - e) * (ONE + TWO * e * D(r - 2))
    assert abs(delta_M - exact_delta) < D("1e-80")
    Gm = D(k * r) * delta_M
    assert abs(Gm - I * (ONE + TWO * e * D(r - 2))) < D("1e-72")
    return P, I, U, G, Gm


def main():
    minimum = None
    for r in range(2, 61):
        P, I, U, G, Gm = stats(r)
        residual = G - I
        minimum = residual if minimum is None else min(minimum, residual)
        assert residual > 0
        if r in (2, 4, 8, 12, 16, 20, 30, 40, 50, 60):
            e = TWO ** (-r)
            scale = FOUR * (-ONE).exp() * D(r * r) * e
            print(f"r={r} k={2**r} G/I={G/I:.24g} U/I={U/I:.24g} scaled_excess={residual/scale:.24g}")
    print("BOUNDARY_ONE_FAMILY_CHECK_PASS")
    print("checked_r=2..60")
    print("all_G_minus_I_positive=yes")
    print("exact_middle_decrement_identity=yes")
    print("minimum_decimal_residual", minimum)
    print("finite_table_used_as_universal_proof=no")


if __name__ == "__main__":
    main()


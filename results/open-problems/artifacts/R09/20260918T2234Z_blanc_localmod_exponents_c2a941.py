from fractions import Fraction
from math import ceil


def fmt(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


for d in (7, 8, 9, 10):
    kappa = max(Fraction(2, d - 4), Fraction(3, d - 6))

    # C-exponents of the two r-tail terms after r = R C^kappa.
    tail10 = Fraction(2) + kappa * Fraction(4 - d)
    tail11a = Fraction(3) + kappa * Fraction(6 - d)

    # C-exponents that chi must dominate in the finite-r terms:
    #   r^d/chi,
    #   C^2 r^4/chi,
    #   C^3 r^6/chi,
    #   C^2 r^(d+4)/chi^2.
    # The last contributes C r^((d+4)/2) to a sufficient chi threshold.
    denom = [
        kappa * d,
        Fraction(2) + 4 * kappa,
        Fraction(3) + 6 * kappa,
        Fraction(1) + kappa * Fraction(d + 4, 2),
    ]
    q = ceil(max(denom))

    assert tail10 <= 0
    assert tail11a <= 0
    assert all(e <= q for e in denom)

    print(
        f"d={d} kappa={fmt(kappa)} "
        f"tail10_Cexp={fmt(tail10)} tail11a_Cexp={fmt(tail11a)} "
        f"denom_Cexps={[fmt(x) for x in denom]} q={q}"
    )

print("ALL_EXACT_EXPONENT_CHECKS_PASS")

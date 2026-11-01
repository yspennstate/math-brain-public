#!/usr/bin/env python3
"""Independent high-precision audit of B10's two-bit half-tax asymptotic.

This file was written independently of B10's verifier.  It checks the exact
closed formulas on joint approaches to (p,q)=(0,1/4), including scales for
which eta^2 log(1/p) vanishes, stays bounded, and diverges.
"""

from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 220
D = Decimal
LN2 = D(2).ln()
C0 = D(1) - D(1) / (D(2) * LN2)


def hnat(x: Decimal) -> Decimal:
    if x == 0 or x == 1:
        return D(0)
    return -x * x.ln() - (D(1) - x) * (D(1) - x).ln()


def h2(x: Decimal) -> Decimal:
    return hnat(x) / LN2


def exact_R(p: Decimal, q: Decimal) -> Decimal:
    s = D(4) * q * (D(1) - q)
    c = D(4) * q * q
    j = h2(s * p) - p * h2(s)
    r = c * p * (D(1) - p) / (D(1) - s * p)
    m = (D(1) - s * p) * h2(r) + s * p * h2(p)
    delta = p * ((D(1) - p) / p).ln() / LN2
    return m + delta / D(2) - j


def exact_polynomial_checks() -> None:
    # Exact rational check of c+1/2-s=8(q-1/4)^2.
    for q in [Fraction(1, 8), Fraction(1, 4), Fraction(1, 3), Fraction(3, 8)]:
        s = 4 * q * (1 - q)
        c = 4 * q * q
        assert c + Fraction(1, 2) - s == 8 * (q - Fraction(1, 4)) ** 2


def eta_for(name: str, L: Decimal) -> Decimal:
    if name == "center":
        return D(0)
    if name == "+invL":
        return D(1) / L
    if name == "-invL":
        return -D(1) / L
    if name == "+invsqrtL":
        return D(1) / L.sqrt()
    if name == "-halfinvsqrtL":
        return -D(1) / (D(2) * L.sqrt())
    if name == "+quarter_diverging":
        return D(1) / (D(4) * L.sqrt().sqrt())
    raise KeyError(name)


def main() -> None:
    exact_polynomial_checks()
    scales = [
        "center",
        "+invL",
        "-invL",
        "+invsqrtL",
        "-halfinvsqrtL",
        "+quarter_diverging",
    ]
    ks = [40, 80, 160, 320]
    errors = {name: [] for name in scales}
    min_ratio = None
    print(f"center_constant_bits={C0}")
    print("exact_polynomial_identity=PASS")
    for name in scales:
        for k in ks:
            p = D(2) ** (-k)
            L = -p.ln()
            eta = eta_for(name, L)
            q = D(1) / D(4) + eta
            assert D(0) < q < D(1)
            ratio = exact_R(p, q) / p
            prediction = D(8) * eta * eta * (L / LN2) + C0
            error = ratio - prediction
            errors[name].append(abs(error))
            min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
            print(
                f"scale={name:21s} k={k:3d} q={q:.18E} "
                f"R_over_p={ratio:.24E} prediction={prediction:.24E} "
                f"error={error:.8E}"
            )
        # A sequence-level consequence of the claimed o(1): the terminal
        # absolute error is smaller than the initial one.  The proof, not this
        # finite test, supplies uniformity.
        assert errors[name][-1] < errors[name][0] or errors[name][-1] < D("1e-80")
    assert min_ratio is not None and min_ratio > 0
    print(f"minimum_R_over_p={min_ratio}")
    print("PASS: 24 independent joint-scaling checks; all R/p positive")


if __name__ == "__main__":
    main()

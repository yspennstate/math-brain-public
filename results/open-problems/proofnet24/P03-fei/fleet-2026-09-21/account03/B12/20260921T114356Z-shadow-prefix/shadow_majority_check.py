#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
from math import comb

getcontext().prec = 80
LN2 = Decimal(2).ln()

def log2_fraction(x: Fraction) -> Decimal:
    y = Decimal(x.numerator) / Decimal(x.denominator)
    return y.ln() / LN2

def majority_weights(n: int):
    if n % 2 != 1:
        raise ValueError("n must be odd")
    m = (n - 1) // 2
    central = Fraction(comb(n - 1, m), 2 ** (n - 1))
    W = [Fraction(0, 1) for _ in range(n + 1)]
    for k in range(1, n + 1, 2):
        h = central * Fraction(comb(m, (k - 1) // 2), comb(n - 1, k - 1))
        W[k] = comb(n, k) * h * h
    assert sum(W, Fraction(0, 1)) == 1
    return W

def metrics(W):
    n = len(W) - 1
    I = sum((Fraction(k, 1) * W[k] for k in range(n + 1)), Fraction(0, 1))
    Bcan = Decimal(0)
    Bsh = Decimal(0)
    for a, wa in enumerate(W):
        if wa == 0:
            continue
        tau = sum(W[a:], Fraction(0, 1))
        factorial_moment = sum(
            (Fraction(comb(b, a), 1) * W[b] for b in range(a, n + 1)),
            Fraction(0, 1),
        )
        wad = Decimal(wa.numerator) / Decimal(wa.denominator)
        Bcan += wad * log2_fraction(factorial_moment / wa)
        Bsh += wad * log2_fraction(tau / wa)
    Id = Decimal(I.numerator) / Decimal(I.denominator)
    return {
        "I": Id,
        "Bcan_over_I": Bcan / Id,
        "Bsh_over_I": Bsh / Id,
        "M_over_I": (Bcan - Bsh) / Id,
    }

beta = Decimal("6.4547837")
log2e = Decimal(1) / LN2
sharp_residual_cap = (beta - (Decimal(2) + Decimal(2) * log2e)) / Decimal(2)

print("beta_input =", beta)
print("log2(e) =", log2e)
print("sharp_residual_cap =", sharp_residual_cap)
for n in (13, 151, 251):
    out = metrics(majority_weights(n))
    print("n =", n)
    for k, v in out.items():
        print(" ", k, "=", v)

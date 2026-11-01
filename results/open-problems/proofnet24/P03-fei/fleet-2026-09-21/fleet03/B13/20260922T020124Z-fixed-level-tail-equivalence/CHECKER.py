#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
import json

getcontext().prec = 70
LN2 = Decimal(2).ln()

def dfrac(q):
    return Decimal(q.numerator) / Decimal(q.denominator)

def log2(x):
    return x.ln() / LN2

# Exact singleton coefficient magnitudes from the source-certified monotone G_10.
coeffs = [(Fraction(29,128), 8), (Fraction(49,256), 1), (Fraction(1,256), 1)]
W = sum(Fraction(mult) * c*c for c,mult in coeffs)
assert W == Fraction(14657,32768)
H1 = Decimal(0)
for c,mult in coeffs:
    w = dfrac(c*c)
    H1 += Decimal(mult) * w * (-log2(w))

# Exact influence from the peer certificate; R_LO is a certified strict lower endpoint.
a = Fraction(257,128)
R_LO = Decimal("6.4593722816378554")

def depth_row(d):
    Wd = dfrac(W) ** (d-1)
    h1d = Decimal(d) * Wd * H1
    denom = dfrac(a) ** d - Decimal(1)
    singleton_ratio = h1d / denom
    tail_lower = R_LO - singleton_ratio
    return {
        "depth": d,
        "singleton_entropy": str(+h1d),
        "I_minus_1": str(+denom),
        "singleton_ratio": str(+singleton_ratio),
        "level_ge_2_ratio_lower": str(+tail_lower),
    }

rows = [depth_row(d) for d in [1,2,4,6,8,12]]
assert Decimal(rows[0]["singleton_ratio"]) > Decimal("1.91924")
assert Decimal(rows[-1]["singleton_ratio"]) < Decimal("0.000001")
assert Decimal(rows[-1]["level_ge_2_ratio_lower"]) > Decimal("6.4593715")

out = {
    "status": "PASS",
    "W1_exact": str(W),
    "W1_decimal": str(dfrac(W)),
    "H1_decimal": str(+H1),
    "I_exact": str(a),
    "R_certified_lower_used": str(R_LO),
    "rows": rows,
    "scope": "Arithmetic self-check of the concrete G_10 singleton-tail application only; Theorem 2.1 is analytic.",
}
print(json.dumps(out, indent=2, sort_keys=True))

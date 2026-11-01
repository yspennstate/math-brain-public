from fractions import Fraction

# Exact self-check for the parameter choice used in
# P24-AV-P3-NO-UNIFORM-RIGHT-EXTRAPOLATION-60.
# This is not the proof of the theorem; the theorem is proved in the report.

def certify(p: Fraction, r: Fraction):
    assert Fraction(2) <= p < r
    q = (p + r) / 2
    beta2 = Fraction(2) / (q - 1)
    pc = 1 + Fraction(2) / beta2
    margin = 1 - beta2 / 2
    assert p < q < r
    assert Fraction(0) < beta2 < Fraction(2)
    assert margin > 0
    assert pc == q
    assert p < pc < r
    return q, beta2, margin

samples = [
    (Fraction(2), Fraction(5, 2)),
    (Fraction(5, 2), Fraction(8, 3)),
    (Fraction(3), Fraction(10, 3)),
    (Fraction(7, 2), Fraction(4)),
    (Fraction(10), Fraction(101, 10)),
]

for p, r in samples:
    q, beta2, margin = certify(p, r)
    print(
        f"p={p}, r={r}, pc=q={q}, beta^2={beta2}, "
        f"coercivity_margin={margin}: PASS"
    )

print("ALL_EXACT_CHECKS_PASS")

from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 50

delta = Fraction(1, 17)
L = Fraction(1, 8)
b_lower = L - delta
kappa_lower = b_lower - delta
P_lower = Fraction(1, 4)

assert b_lower == Fraction(9, 136)
assert kappa_lower == Fraction(1, 136)
assert P_lower * kappa_lower == Fraction(1, 544)
assert delta * delta - b_lower * b_lower < 0

cp = Decimal(128) * (Decimal(34) ** (Decimal(1) / Decimal(4)))
cq = Decimal(8) * Decimal(5).sqrt() * (Decimal(544) ** (Decimal(1) / Decimal(4)))

assert cp < Decimal(310)
assert cq < Decimal(87)

print("PASS")
print("delta=", delta)
print("b_lower=", b_lower)
print("kappa_lower=", kappa_lower)
print("P*kappa lower=", P_lower * kappa_lower)
print("det upper threshold=", delta * delta - b_lower * b_lower)
print("pivot constant=", cp)
print("pair constant=", cq)

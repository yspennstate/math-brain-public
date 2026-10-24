from decimal import Decimal, getcontext

getcontext().prec = 80

sqrt2 = Decimal(2).sqrt()
eps = Decimal(1) / Decimal(16)
delta = Decimal(1) / Decimal(2) - eps - (Decimal(2) * eps).sqrt()
ell = eps / delta
q = Decimal(149) / Decimal(100)
eps_star = (Decimal(39) - Decimal(6) * Decimal(30).sqrt()) / Decimal(98)

# Exact algebra behind ell < 149/200:
# ell = (7 + 4 sqrt(2))/17, and
# 200(7+4sqrt(2)) < 17*149 iff 800sqrt(2) < 1133.
# Squaring is legal because both sides are positive.
assert 800 * 800 * 2 < 1133 * 1133
assert ell < q / 2
assert eps < eps_star
assert delta > 0
assert q < Decimal(3) / Decimal(2)

# e is only used here for a readable numerical constant; the proof in REPORT.md
# keeps e symbolic.
e_approx = Decimal("2.71828182845904523536028747135266249775724709369995")
C = Decimal(3) * e_approx / ((Decimal(2) * q).sqrt() * delta * (Decimal(3) - Decimal(2) * q))

print("epsilon*=", eps_star)
print("epsilon=", eps)
print("delta=", delta)
print("leverage_after_partition=", ell)
print("q/2=", q / 2)
print("C/e=", Decimal(3) / ((Decimal(2) * q).sqrt() * delta * (Decimal(3) - Decimal(2) * q)))
print("C approx=", C)

from fractions import Fraction
import math

c = Fraction(6221, 6450)
eps = Fraction(3, 200)
tau = Fraction(1, 4)
tau0 = (eps / c) ** 2
delta = Fraction(4, 5) * (c * Fraction(1, 2) - eps)
lev = tau + Fraction(229, 6450)
C = 8 * 2**0.25 / 3**0.25 * float(delta)**(-0.25)

assert tau > tau0
assert delta == Fraction(2411, 6450)
assert lev == Fraction(3683, 12900)
assert C < 9.25

print(f"tau0={tau0}={float(tau0):.15f}")
print(f"delta={delta}={float(delta):.15f}")
print(f"outer_constant={C:.15f}")
print(f"survivor_nonanchor_leverage={lev}={float(lev):.15f}")
print("QFORM_B06_R23_CHECK_PASS")

from fractions import Fraction
from decimal import Decimal, getcontext

s = 7
c = Fraction(9, 121)
a = Fraction(3, 11)

assert a * a == c

ordinary_psd_reduced = Fraction(1, 1) - (2 * s - 1) * c
spectral_cap_reduced = Fraction(1, 1) - (2 * s + 1) * c
lead_bound = Fraction(1, 2 * s - 1)
new_bound_polynomial = c * c + 2 * s * c - 1

getcontext().prec = 30
new_bound_decimal = Decimal(s * s + 1).sqrt() - Decimal(s)

print(f"s={s}")
print(f"c={c} ~ {float(c):.12f}")
print(f"a={a}; a^2=c: {a*a == c}")
print(f"ordinary_psd_symmetric_reduced={ordinary_psd_reduced}")
print(f"spectral_cap_symmetric_reduced={spectral_cap_reduced}")
print(f"lead_bound=1/(2s-1)={lead_bound} ~ {float(lead_bound):.12f}")
print(f"new_bound=sqrt(s^2+1)-s ~ {new_bound_decimal}")
print(f"new_bound_polynomial_value(c)=c^2+2sc-1={new_bound_polynomial}")

assert ordinary_psd_reduced >= 0
assert c <= lead_bound
assert spectral_cap_reduced < 0
assert new_bound_polynomial > 0

print("ORDINARY_PSD_CONTROL_PASS")
print("OLD_BOUND_CONTROL_PASS")
print("NEW_SPECTRAL_CAP_REJECTS_CONTROL")

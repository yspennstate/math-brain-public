from fractions import Fraction
import json

# Source-certified decimal lower bounds are represented as exact rationals.
C0 = Fraction(64548, 10000)                 # base center 6.4548
AND_PAYMENT = Fraction(1, 100)              # certified c=0.01 read-once margin
G10_R_LO = Fraction(6459372281637855731, 10**18)
F5_R_LO = Fraction(65218509495457, 10**13)


def c_lower(r):
    # For a balanced gate at uniform input biases,
    # c_G = 4 * ( H/(I-1) - C0 ).
    return 4 * (r - C0)


g10 = c_lower(G10_R_LO)
f5 = c_lower(F5_R_LO)

assert G10_R_LO > Fraction(64573, 10000)     # read-once theorem center 6.4573
assert g10 > AND_PAYMENT
assert f5 > AND_PAYMENT
assert f5 > g10

out = {
    "status": "PASS",
    "C0": "6.4548",
    "read_once_certified_center": "6.4573",
    "and_certified_payment": "0.01",
    "g10_ratio_lower": "6.459372281637855731",
    "g10_c_lower_fraction": f"{g10.numerator}/{g10.denominator}",
    "g10_c_lower_decimal": "0.018289126551422924",
    "g10_factor_over_and_payment": "1.8289126551422924",
    "f5_ratio_lower": "6.5218509495457",
    "f5_c_lower_fraction": f"{f5.numerator}/{f5.denominator}",
    "f5_c_lower_decimal": "0.2682037981828",
    "f5_factor_over_and_payment": "26.82037981828",
}
print(json.dumps(out, sort_keys=True, indent=2))

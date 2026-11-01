from fractions import Fraction

# Source-bound decimal constants from the cited reports.
a = Fraction(268204856, 10**9)       # quadratic lift a^dagger
delta = Fraction(258204856, 10**9)   # a^dagger - 0.01
c = Fraction(49096, 10000)           # 4.9096
G_upper0 = Fraction(862812, 100000)  # 8.62812
G_lower0 = Fraction(222922, 100000)  # 2.22922

# |Gamma^dagger|' on the segment, after x <= L-4,
# using |G'|<31 and 1/ln2<3/2.
deriv_const = G_upper0 + 31 * Fraction(3, 2) + a - 4 * c
assert deriv_const == Fraction(4469740607, 125000000)

# Refined spectral-entropy movement: 6 p y + (25/4) p y + 3 y.
pre_gamma_const = deriv_const + Fraction(49, 4)
after_gamma_const = pre_gamma_const - G_lower0
assert pre_gamma_const == Fraction(6000990607, 125000000)
assert after_gamma_const == Fraction(5722338107, 125000000)

# Elementary exact certification log_2(160) > 7.3:
# raising 2^(73/10) < 160 to the tenth power.
assert 2**73 < 160**10

# At L=8, y <= 1/2560.  This is the worst point of the monotone
# scalar envelope for the denominator-20 theorem.
worst_B = (
    c * (Fraction(4) - Fraction(73, 10))
    + after_gamma_const
    - a * Fraction(2559, 2560)
)
assert worst_B > 0
worst_rate = (Fraction(12) + worst_B) / 160
margin = delta - worst_rate
assert margin == Fraction(1232701593, 51200000000000)
assert margin > 0

# If the p-coefficient has already turned negative, the envelope is
# 12/(20 L), whose maximum at L=8 is also safely below delta.
assert Fraction(12, 160) < delta

print("derivative_constant", float(deriv_const))
print("pre_gamma_constant", float(pre_gamma_const))
print("after_gamma_constant", float(after_gamma_const))
print("worst_rate", float(worst_rate))
print("delta", float(delta))
print("certified_margin", float(margin))
print("exact_margin", f"{margin.numerator}/{margin.denominator}")
print("PASS denominator-20 scalar certificate")

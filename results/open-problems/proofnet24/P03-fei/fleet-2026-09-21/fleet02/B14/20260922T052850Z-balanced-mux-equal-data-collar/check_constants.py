from fractions import Fraction

Cminus6 = Fraction(521851214, 10**9)
a = Fraction(268204856, 10**9)
rho = Fraction(1, 128)

same_upper = Fraction(93, 2) * rho + (Fraction(93, 4) + a / 2) * rho * rho
same_margin = Cminus6 - same_upper
same_per_m = same_margin / 2

straddle_margin = Cminus6 * (1 - Fraction(1, 129**2)) / 2 - Fraction(31, 128)

assert same_margin == Fraction(643656546937, 4096000000000)
assert straddle_margin == Fraction(15577995649, 832050000000)
assert same_per_m > Fraction(187, 10000)
assert straddle_margin > Fraction(187, 10000)

print("PASS")
print("same_upper =", same_upper, float(same_upper))
print("same_margin =", same_margin, float(same_margin))
print("same_margin_per_m =", same_per_m, float(same_per_m))
print("straddle_margin =", straddle_margin, float(straddle_margin))
print("global_margin_per_m_gt = 187/10000")

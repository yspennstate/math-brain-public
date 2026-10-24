from fractions import Fraction
from math import sqrt, e

theta_hi = Fraction(201, 100)
f_half = Fraction(128, 129)

S_all = Fraction(129, 256) * theta_hi
gap_all = Fraction(2, 3) - S_all * S_all / 2
assert gap_all > 0

S_tail = Fraction(129, 256) * (theta_hi - f_half)
gap_tail = Fraction(2, 3) - (S_tail + S_tail * S_tail / 2)
assert gap_tail > 0

delta = theta_hi - 2 * f_half
assert delta == Fraction(329, 12900)

tail_ratio_g2 = delta / (1 - delta)
assert tail_ratio_g2 == Fraction(329, 12571)

tail_ratio_gamma2 = tail_ratio_g2 / 256
assert tail_ratio_gamma2 == Fraction(329, 3218176)

top_plane_leverage = Fraction(99, 100) - delta
assert top_plane_leverage == Fraction(6221, 6450)

A0 = f_half * f_half * top_plane_leverage * top_plane_leverage
B0 = 2 * delta + delta * delta / 2
assert A0 == Fraction(158518644736, 173076800625)
assert B0 == Fraction(17084641, 332820000)

c = Fraction(1067, 2000)
radicand_test = (A0 + B0 - c) ** 2 - 4 * A0 * B0
assert A0 + B0 - c > 0
assert radicand_test > 0
assert radicand_test == Fraction(
    1583861310111679009321,
    30674512808536064400000000,
)

C2 = (2 ** (4 / 3) + 1) * sqrt(3 * e) * (3 / 2) ** (1 / 8)
assert C2 < 10.575

print('gap_all =', gap_all, float(gap_all))
print('gap_tail =', gap_tail, float(gap_tail))
print('delta =', delta, float(delta))
print('tail_ratio_g2 =', tail_ratio_g2, float(tail_ratio_g2))
print('tail_ratio_gamma2 =', tail_ratio_gamma2, float(tail_ratio_gamma2))
print('tail_HS_over_gamma <', sqrt(float(tail_ratio_gamma2)))
print('h3_over_h2 <', sqrt(2 * float(tail_ratio_gamma2)))
print('top_plane_leverage >', top_plane_leverage, float(top_plane_leverage))
print('A0 =', A0, float(A0))
print('B0 =', B0, float(B0))
print('exterior_bank_lower =', (sqrt(float(A0)) - sqrt(float(B0))) ** 2)
print('radicand_test =', radicand_test, float(radicand_test))
print('exact_rank2_constant =', C2)
print('QFORM_B08_R20_CHECK_PASS')

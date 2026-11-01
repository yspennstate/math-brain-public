from fractions import Fraction
import math

M2 = Fraction(1023, 4096)
eta = Fraction(1, 4)

# Stable-alignment aggregate energy:
# ||E||op >= 1/2 and ||E||F^2 <= 8/(eta*M^2) sum Delta_j^2.
sum_delta_lb = eta * M2 * Fraction(1, 4) / 8
assert sum_delta_lb == Fraction(1023, 524288)

# Random physical cut captures one eighth of the aggregate.
cut_E2_lb = sum_delta_lb / 8
assert cut_E2_lb == Fraction(1023, 4194304)

# q=4/3 third-volume receiver, using s3(B)>=1/64.
C_tail = 9.0 * math.sqrt(3.0) * math.e / 2.0
Z_lb = float(cut_E2_lb) * (1.0 / 64.0) ** 2 / 3.0
volume_bound = C_tail * Z_lb ** (-1.0 / 6.0)
assert volume_bound < 408.0

# Designated fleet04/B20 conditioned-whitened branch.
partner_bound = 27.0 / 0.25
assert partner_bound == 108.0

# Failure of whitened diffuseness gives c_j>1/128.
# If the physical diagonal is <1/32, the remaining star is fixed.
second_star_sq = Fraction(1, 128) - Fraction(1, 32) ** 2
assert second_star_sq == Fraction(7, 1024)
compound_half = second_star_sq / 2
assert compound_half == Fraction(7, 2048)
disjoint_cut = compound_half / 8
assert disjoint_cut == Fraction(7, 16384)

# Scalar-pivot branch at c_j>1/128, |A_jj|>=1/32.
pivot_bound = 128.0 * (4096.0 ** 0.25)
assert pivot_bound == 1024.0

print('QFORM_B20_R25_CHECK_PASS')
print('sum_delta_lb=', sum_delta_lb, float(sum_delta_lb))
print('cut_E2_lb=', cut_E2_lb, float(cut_E2_lb))
print('volume_bound=', volume_bound)
print('partner_bound=', partner_bound)
print('second_star_sq=', second_star_sq, float(second_star_sq))
print('disjoint_cut=', disjoint_cut, float(disjoint_cut))
print('pivot_bound=', pivot_bound)

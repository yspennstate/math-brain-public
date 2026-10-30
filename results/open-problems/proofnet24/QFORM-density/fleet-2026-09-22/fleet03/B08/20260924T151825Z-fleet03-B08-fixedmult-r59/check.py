from fractions import Fraction as F

# Exact rational audit margins used in REPORT.md.
delta_lower = F(6779, 8000)
assert delta_lower > F(4, 5)

g_lower = F(8, 25)
two_high_lower = g_lower / 3
cross_sq_upper = F(10201, 25_000_000)
assert two_high_lower > cross_sq_upper

H5 = max(F(70), F(80), F(1) + F(4) * F(142, 5))
assert H5 == F(573, 5)
assert 10 * H5 == F(1146)

indef = F(10) * (F(6) + F(14, 5) + F(54, 5)) + F(1, 2)
assert indef == F(393, 2)
assert indef < F(197)

W_lower = g_lower / 48
assert W_lower == F(1, 150)

print('QFORM_B08_R59_S8_REVIEW_CHECK_PASS')
print('delta_lower=', delta_lower, float(delta_lower))
print('g_lower=', g_lower, float(g_lower))
print('two_high_lower=', two_high_lower, float(two_high_lower))
print('cross_sq_upper=', cross_sq_upper, float(cross_sq_upper))
print('contradiction_ratio=', float(two_high_lower / cross_sq_upper))
print('H5=', H5, float(H5), 'scalar_outer=', float(10*H5))
print('indef=', indef, float(indef))
print('W_lower=', W_lower, float(W_lower))

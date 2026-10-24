from fractions import Fraction as Q


def tent(x):
    return abs(1 - 2*x)

x = Q(5, 228)
xs = [x]
for _ in range(11):
    xs.append(tent(xs[-1]))

expected = [
    Q(5,228), Q(109,114), Q(52,57), Q(47,57), Q(37,57),
    Q(17,57), Q(23,57), Q(11,57), Q(35,57), Q(13,57),
    Q(31,57), Q(5,57)
]
assert xs == expected
assert tent(xs[11]) == xs[3]

# For a symmetric nonnegative universally gate-safe direction F normalized by F(0)=1,
# the source-valid selector with children (-1, balanced literal) gives
#   F(x) <= 1-x + 1/2 F(|1-2x|).
# Iterate this exact inequality around the period-9 tent-map cycle x_3,...,x_11.
cycle_sum = sum(Q(1, 2**r) * (1-xs[3+r]) for r in range(9))
y3 = cycle_sum / (1-Q(1,2**9))
assert y3 == Q(6640,9709)

# Propagate the equality envelope around the cycle and verify every recursion exactly.
y = {3: y3}
for j in range(3,11):
    y[j+1] = 2*(y[j] - (1-xs[j]))
for j in range(3,12):
    nxt = y[3] if j == 11 else y[j+1]
    assert y[j] == (1-xs[j]) + Q(1,2)*nxt

# Propagate backwards to x_0=5/228.
yb = y3
for j in (2,1,0):
    yb = (1-xs[j]) + Q(1,2)*yb
y0 = yb
assert y0 == Q(129023,116508)

# A second genuine Boolean selector construction with child means -x,+x,
# minimal disagreement x, and balanced selector gives F(x) >= (1-x)F(0).
out_mean = Q(5,1024)
yout_lower = 1-out_mean
assert yout_lower == Q(1019,1024)

# Strong Numaro witness response per unit center of any such safe direction.
eff = Q(57,256)*y0 + Q(465,256) - yout_lower
assert eff == Q(279387,261632)

# Rigorous peer defect D_{Gamma^dagger} < -38023/10^6.
deficit = Q(38023,10**6)
center_increment = deficit / eff
assert center_increment == Q(155438024,4365421875)

base_center = Q(6521851214,10**9)
total_center = base_center + center_increment
assert total_center == Q(916034239330909,139693500000000)

# Owner-comparable quadratic margin lower bound for the same strong witness.
p1 = Q(223,456)
pout = Q(1019,2048)
alpha1 = Q(57,256)
alpha_rest = Q(465,256)
W = alpha1*p1*(1-p1) + alpha_rest*Q(1,4) - pout*(1-pout)
assert W == Q(62098577,239075328)
a_dagger = Q(268204856,10**9)
margin_lower = a_dagger + deficit/W
assert margin_lower == Q(3218187637329239,7762322125000000)

print('PASS')
print('tent_orbit=', ','.join(f'{z.numerator}/{z.denominator}' for z in xs))
print('cycle_y3=', y3, float(y3))
print('F_5_228_over_F0_upper=', y0, float(y0))
print('F_5_1024_over_F0_lower=', yout_lower, float(yout_lower))
print('safe_payment_per_center_upper=', eff, float(eff))
print('required_center_increment_lower=', center_increment, float(center_increment))
print('fixed_seed_repaired_center_lower=', total_center, float(total_center))
print('strong_witness_W=', W, float(W))
print('strong_witness_quadratic_margin_lower=', margin_lower, float(margin_lower))

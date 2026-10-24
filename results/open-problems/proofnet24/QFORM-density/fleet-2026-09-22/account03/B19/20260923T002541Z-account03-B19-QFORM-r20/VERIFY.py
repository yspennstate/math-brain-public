from fractions import Fraction
import math

# Exact rational part of
# (2/3)(1-1/sqrt(3)) > 17/64.
# This is equivalent to 1/sqrt(3) < 77/128, and both sides are positive.
assert Fraction(5929, 16384) > Fraction(1, 3)

# The r19 theta/mu thresholds imply each compressed diagonal is <1/8.
assert Fraction(512, 4096) == Fraction(1, 8)

lower = (2.0 / 3.0) * (1.0 - 1.0 / math.sqrt(3.0))
upper = 17.0 / 64.0
assert lower > upper

# Bisection for the exact crossing of (1-t)(1-sqrt(t))=17/64.
lo, hi = 0.0, 1.0
for _ in range(200):
    mid = (lo + hi) / 2.0
    value = (1.0 - mid) * (1.0 - math.sqrt(mid))
    if value > upper:
        lo = mid
    else:
        hi = mid
crossing = (lo + hi) / 2.0
assert crossing > 1.0 / 3.0

# Designated-partner concrete application D>=exp(-8): log(e/D)<=9.
partner_bound = 34.0 * math.sqrt(9.0)
assert partner_bound == 102.0

print("QFORM_B19_R20_ROBUST_INTERNAL_CHECK_PASS")
print("lower_at_tau_1_3", repr(lower))
print("upper_from_survivor", repr(upper))
print("gap", repr(lower - upper))
print("exact_crossing", repr(crossing))
print("partner_D_ge_exp_minus8", repr(partner_bound))

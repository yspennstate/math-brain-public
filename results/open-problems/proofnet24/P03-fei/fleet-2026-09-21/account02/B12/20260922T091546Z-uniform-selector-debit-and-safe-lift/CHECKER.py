from fractions import Fraction
import math

OLD = Fraction(268204856, 10**9)
NEW = Fraction(337, 1000)
W = Fraction(1078193, 4194304)
NEGATIVE_MAG_UPPER = Fraction(17611420, 10**9)
BASE_CENTER = Fraction(16137, 2500)  # 6.4548

added = (NEW - OLD) * W
reserve_lower = added - NEGATIVE_MAG_UPPER
center = BASE_CENTER + NEW / 4

assert reserve_lower > 0
assert center == Fraction(130781, 20000)

def h(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

# Deterministic sanity grid only; the report gives analytic proofs.
max_coeff_ratio = 0.0
max_channel_gap = -1e100
for a in range(1, 2000):
    s = a / 2000.0
    V = 4.0*s*(1.0-s)
    if abs(s-0.5) < 1e-15:
        kappaV = 2.0/math.log(2.0)
    else:
        kappa = math.log((1.0-s)/s)/((1.0-2.0*s)*math.log(2.0))
        kappaV = kappa*V
    max_coeff_ratio = max(max_coeff_ratio, kappaV/(2.0/math.log(2.0)))
    for b in range(1, 200):
        d = b/200.0
        gap = h(V*d)-d*h(V)-h(d)
        max_channel_gap = max(max_channel_gap, gap)

assert max_coeff_ratio <= 1.0 + 1e-12
assert max_channel_gap <= 1e-12

print("PASS")
print("old_coefficient", OLD, float(OLD))
print("new_coefficient", NEW, float(NEW))
print("coefficient_increment", NEW-OLD, float(NEW-OLD))
print("prime_W", W, float(W))
print("added_prime_defect", added, float(added))
print("certified_reserve_lower", reserve_lower, float(reserve_lower))
print("new_center", center, float(center))
print("grid_max_kappaV_over_2_over_ln2", f"{max_coeff_ratio:.16f}")
print("grid_max_channel_information_gap", f"{max_channel_gap:.3e}")

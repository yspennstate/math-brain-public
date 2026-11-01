import math

# Sanity check only: the erf envelope used in the analytic proof.
min_margin = float('inf')
worst_y = None
for k in range(1, 20001):
    t = (k - 1) / 19999
    y = math.exp(math.log(1e-6) * (1 - t) + math.log(20.0) * t)
    lhs = math.erf(y)
    rhs = (2 * y / math.sqrt(math.pi)) / math.sqrt(1 + 2 * y * y / 3)
    margin = rhs - lhs
    if margin < min_margin:
        min_margin = margin
        worst_y = y

# Exact two-heavy collinear limiting constant.
c2 = -2 + 2 * math.exp(-3) + 2 * math.sqrt(3 * math.pi) * math.erf(math.sqrt(3))
baseline = 3 * math.sqrt(2)
partner = 4.06307061680603726012548442259

# Floating noise at tiny y can be around 1e-20; the inequality itself is proved analytically.
assert min_margin > -1e-15
assert c2 < baseline
assert c2 > partner

print(f"min_erf_grid_margin={min_margin:.18e} at y={worst_y:.18e}")
print(f"two_heavy_limit={c2:.16f}")
print(f"three_sqrt_two={baseline:.16f}")
print(f"gap_to_three_sqrt_two={baseline-c2:.16f}")
print(f"gain_over_partner_six_variable={c2-partner:.16f}")
print("PASS")

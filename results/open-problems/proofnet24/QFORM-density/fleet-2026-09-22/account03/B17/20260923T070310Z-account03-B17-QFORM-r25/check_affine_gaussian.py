import math


def r(k, l):
    return math.gamma(k + l + 0.5) / (
        2 ** (k + l) * math.factorial(k) * math.gamma(l + 0.5)
    )

mx = (0.0, None, None)
for k in range(30):
    for l in range(30):
        if k == 0 and l == 0:
            continue
        val = r(k, l)
        if val > mx[0]:
            mx = (val, k, l)

assert abs(mx[0] - 0.5) < 1e-14 and mx[1:] == (0, 1)
assert abs(3 * math.sqrt(2) - 4.242640687119286) < 1e-14

ratio = (1 + math.exp(-6)) / 2
bound = 3 * math.sqrt(2) * ratio

print("three_sqrt_two =", 3 * math.sqrt(2))
print("max_r_grid_0_29_excluding_00 =", mx)
print("zero_ratio_hnorm1_v1_12 =", ratio)
print("zero_density_bound_hnorm1_v1_12 =", bound)

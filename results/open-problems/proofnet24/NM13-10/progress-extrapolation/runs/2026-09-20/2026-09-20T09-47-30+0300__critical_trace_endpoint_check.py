#!/usr/bin/env python3
import math


def c1_norm(p):
    # Remainder coefficient after (p-1)a^(p-1)b with absorption delta/4.
    return (4.0 ** (p - 1.0)) * ((p - 1.0) ** (2.0 * p - 1.0)) / (p ** p)


def c2_norm(p):
    # Remainder coefficient after (p-1)/2 a^(p-2)b^2 with absorption delta/4,
    # before the factor delta^{-(p-2)/2}.
    c2 = (2.0 / p) * (((p - 2.0) / p) ** ((p - 2.0) / 2.0)) if p > 2 else 1.0
    return 0.5 * (p - 1.0) * c2 * ((2.0 * (p - 1.0)) ** ((p - 2.0) / 2.0))


max_c1 = (-1.0, None)
max_c2 = (-1.0, None)
max_young = (-1.0, None)
for i in range(1, 20000):
    p = 2.5 + (3.0 - 2.5) * i / 20000.0
    delta = (3.0 - p) / 2.0
    v1 = c1_norm(p)
    v2 = c2_norm(p)
    if v1 > max_c1[0]:
        max_c1 = (v1, p)
    if v2 > max_c2[0]:
        max_c2 = (v2, p)
    for j in range(241):
        lr = -12.0 + 24.0 * j / 240.0
        r = 10.0 ** lr
        lhs = (p - 1.0) * r + 0.5 * (p - 1.0) * r * r
        rhs = delta / 2.0 + 520.0 * (delta ** (-(p - 1.0))) * (r ** p)
        ratio = lhs / rhs
        if ratio > max_young[0]:
            max_young = (ratio, (p, delta, r))

max_endpoint = (-1.0, None)
for i in range(20000):
    a = math.log(12.0)
    b = math.log(1.0e8)
    L = math.exp(a + (b - a) * i / 19999.0)
    eps = 6.0 / L
    p = 3.0 - eps
    ap = (p - 1.0) / p
    ratio = ((520.0 * p) ** (1.0 / p)) * ((L / 3.0) ** ap) * math.exp(2.0 / p) / (L ** (2.0 / 3.0))
    if ratio > max_endpoint[0]:
        max_endpoint = (ratio, L)

moderate = math.sqrt(2.0) * math.exp(2.0)

print("TRACE_ENDPOINT_CHECK")
print(f"max_c1_norm_grid={max_c1[0]:.12f} at p={max_c1[1]:.9f}")
print(f"max_c2_norm_grid={max_c2[0]:.12f} at p={max_c2[1]:.9f}")
print("analytic_coarse_bounds: c1_norm<=512, c2_norm<=3")
print(f"max_combined_young_ratio_grid={max_young[0]:.12f} at p,delta,r={max_young[1]}")
print("combined_target_bound: lhs <= delta/2 + 520 delta^{-(p-1)} r^p")
print(f"max_large_log_endpoint_ratio_grid={max_endpoint[0]:.12f} at L={max_endpoint[1]:.9f}")
print(f"moderate_log_p2_constant=sqrt(2)*e^2={moderate:.12f}")
print("claimed_universal_scalar_trace_constant=22")
for eps in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
    p = 3.0 - eps
    delta = eps / 2.0
    k = ((520.0 * p) ** (1.0 / p)) * (delta ** (-(p - 1.0) / p))
    print(f"eps={eps:.6f} p={p:.6f} trace_factor={k:.12f} eps^(2/3)*factor={eps ** (2.0 / 3.0) * k:.12f}")

assert max_c1[0] < 512.0
assert max_c2[0] < 3.0
assert max_young[0] < 1.0
assert max_endpoint[0] < 22.0
assert moderate < 22.0
print("CHECK_PASS")

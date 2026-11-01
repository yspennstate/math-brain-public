import math
import numpy as np

L = 1.0
theta = 2.0**-21
m = 2**15
eta = 2.0**-20
beta0 = 4.0*math.sqrt(2.0)*eta
g = 0.5 - 1.0/(4.0*math.sqrt(2.0))
endpoint = 128.0*(64.0**0.25)

d_zero = g*(1.0-beta0)-beta0
d_bank = d_zero-eta
assert d_bank > 0.3232
assert theta/math.sqrt(2.0) < eta
assert theta < beta0
assert endpoint/d_zero < 1120.114
assert eta**2/d_bank < 2.814e-12

K = np.array([
    [0.0, math.sqrt(2.0), 0.0, theta],
    [math.sqrt(2.0), 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [theta, 0.0, 0.0, 0.0],
])
e = np.linalg.eigvalsh(K)
assert sum(abs(x) >= 1.0-1e-12 for x in e) == 3

KB = np.array([
    [0.0, 1.0, 0.0, theta/math.sqrt(2.0)],
    [1.0, 0.5, 0.0, 0.0],
    [0.0, 0.0, 0.5, 0.0],
    [theta/math.sqrt(2.0), 0.0, 0.0, 0.0],
])
eb = np.linalg.eigvalsh(KB)
assert abs(sorted((abs(x) for x in eb), reverse=True)[2] - 0.5) < 1e-12

hub_pair_bound = (math.sqrt(2.0)+theta)/math.sqrt(m)
child_pair_bound = 4.0/m
assert hub_pair_bound < 1.0/64.0
assert child_pair_bound < 1.0/64.0

Gaug = np.array([
    [1.0, 0.0, math.sqrt(2.0)],
    [0.0, 1.0, 0.0],
    [math.sqrt(2.0), 0.0, 2.0+theta**2],
])
assert abs(np.linalg.det(Gaug)-theta**2) < 1e-15
assert 3.0/m < 0.5

fixed_source_H_constant = 4.0*math.sqrt(2.0)/math.sqrt(theta)
assert abs(fixed_source_H_constant-8192.0) < 1e-10

print(f"g={g:.15f}")
print(f"beta0={beta0:.16e}")
print(f"bank_residual={theta/math.sqrt(2.0):.16e}")
print(f"bank_s3_gate={d_bank:.15f}")
print(f"bank_s4_gate={eta**2/d_bank:.16e}")
print(f"zero_residual_density_constant={endpoint/d_zero:.12f}")
print("full_core_eigenvalues=" + ",".join(f"{x:.16e}" for x in e))
print("bank_core_eigenvalues=" + ",".join(f"{x:.16e}" for x in eb))
print(f"hub_pair_bound={hub_pair_bound:.16e}")
print(f"child_pair_bound={child_pair_bound:.16e}")
print(f"augmented_leverage={3.0/m:.16e}")
print(f"theorem_H_density_constant={fixed_source_H_constant:.1f}")
print("QFORM_B08_R38_BANK_PUNCTURE_CHECK_PASS")

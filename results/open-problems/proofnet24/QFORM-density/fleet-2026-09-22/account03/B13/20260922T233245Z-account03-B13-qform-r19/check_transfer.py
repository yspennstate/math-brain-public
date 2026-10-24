from math import exp, log, pi, sqrt

def log_plus(x: float) -> float:
    return max(0.0, log(x))

tau = 1.0 / 16.0
K_tau = (2.0 / sqrt(tau)) * (6.2 + log_plus(16.0 * sqrt(tau)))
H_floor = 1.0 + 3.0 * K_tau
C0_coefficient = tau ** (-0.5) * 2.0 * exp(pi)
full_floor = tau ** (-0.5) * H_floor

print(f"tau={tau:.16g}")
print(f"K_tau={K_tau:.15f}")
print(f"1+3K_tau={H_floor:.15f}")
print(f"C0_coefficient={C0_coefficient:.15f}")
print(f"full_floor={full_floor:.15f}")
print("QFORM_B13_R19_TRANSFER_CHECK_PASS")

assert abs(tau - 0.0625) < 1e-15
assert K_tau > 60.69 and K_tau < 60.70
assert H_floor > 183.07 and H_floor < 183.08
assert C0_coefficient > 185.12 and C0_coefficient < 185.13
assert full_floor > 732.28 and full_floor < 732.29

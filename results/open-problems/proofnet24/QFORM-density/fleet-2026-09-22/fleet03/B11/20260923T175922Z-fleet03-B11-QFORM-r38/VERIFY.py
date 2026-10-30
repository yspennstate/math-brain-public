import math

# Deterministic arithmetic checks for REPORT.md.
delta = 17.0 / 288.0
lambda_H = delta * 34.0 / 111.0
kappa0 = (34.0 / 111.0) * delta ** 1.5

Cstar = (
    10.0 / (2.0 * math.pi * 8.0 ** (4.0 / 5.0))
    * (math.pi * 6.0 ** (3.0 / 4.0) * (16.0 * math.pi) ** 0.25) ** (4.0 / 5.0)
)

# Product projection caps: M_X = 2^(3/2), M_Y = 2, hence
# (M_X M_Y)^(2/5) = 2 exactly.
projection_factor = ((2.0 ** 1.5) * 2.0) ** (2.0 / 5.0)
base = Cstar * projection_factor * kappa0 ** (-2.0 / 5.0)
theta_001 = base * (0.01) ** (-1.0 / 5.0)
partner = 2048.0 * math.sqrt(2.0 / 7.0)

print(f"delta={delta:.15f}")
print(f"lambda_H_lower={lambda_H:.15f}")
print(f"kappa0={kappa0:.15f}")
print(f"Cstar={Cstar:.15f}")
print(f"projection_factor={projection_factor:.15f}")
print(f"continuous_branch_base={base:.15f}")
print(f"continuous_branch_theta_1_over_100={theta_001:.15f}")
print(f"partner_pair_area_exit={partner:.15f}")

assert Cstar < 4.833
assert abs(projection_factor - 2.0) < 1e-12
assert base < 84.752
assert theta_001 < 212.886
assert partner < 1094.703

# Algebraic checks used in the proof.
# 1/(64*delta)=9/34 and 3+9/34=111/34.
assert abs(1.0 / (64.0 * delta) - 9.0 / 34.0) < 1e-12
assert abs(3.0 + 9.0 / 34.0 - 111.0 / 34.0) < 1e-12

# Optimizer for 2T+B T^(-1/4): T=(B/8)^(4/5).
# Normalize B=1 and verify the closed-form value.
T = (1.0 / 8.0) ** (4.0 / 5.0)
value = 2.0 * T + T ** (-1.0 / 4.0)
closed = 10.0 * 8.0 ** (-4.0 / 5.0)
assert abs(value - closed) < 1e-12

print("QFORM_B11_R38_INTERNAL_SQUARE_L4_CHECK_PASS")

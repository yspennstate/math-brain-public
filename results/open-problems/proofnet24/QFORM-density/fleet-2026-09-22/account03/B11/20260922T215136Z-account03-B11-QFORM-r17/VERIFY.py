import math

# Normalize tau=s=1 for the dimensionless ridge calculation.
tau = 1.0
gamma = tau / math.sqrt(6.0)
row_cap = tau / math.sqrt(12.0)
kii_cap = row_cap**2 / gamma**2
theta_lower = 3.0 * tau**2 / (gamma**2 + tau**2)
ridge_constant = math.sqrt(math.e) / (math.sqrt(2.0) * gamma) * theta_lower / (theta_lower - 2.0)
pair_constant = 3.0 * 400.0**(1.0/3.0)

assert abs(kii_cap - 0.5) < 1e-12
assert abs(theta_lower - 18.0/7.0) < 1e-12
assert theta_lower > 2.0
assert abs(ridge_constant - (9.0/2.0)*math.sqrt(3.0*math.e)) < 1e-12

print(f"Kii_cap={kii_cap:.15f}")
print(f"theta_lower={theta_lower:.15f}")
print(f"ridge_density_constant={ridge_constant:.15f}")
print(f"pair_density_constant={pair_constant:.15f}")
print(f"ridge_trace_constant={2*ridge_constant:.15f}")
print(f"pair_trace_constant={2*pair_constant:.15f}")
print("QFORM_B11_PAIR_OR_RIDGE_CHECK_PASS")

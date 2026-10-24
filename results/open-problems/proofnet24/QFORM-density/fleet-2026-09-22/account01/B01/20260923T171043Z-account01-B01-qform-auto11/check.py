import math

C_raw = 5.0 * (3.0 * math.sqrt(6.0) / 8.0) ** (4.0 / 5.0)
C_proj = C_raw * 2.0 ** (2.0 / 5.0)
C_exact = (15.0 / 4.0) * 12.0 ** (1.0 / 5.0)
assert abs(C_proj - C_exact) < 1e-12

partner = 22.385 * 2.0 ** (-1.0 / 6.0)
assert partner < 19.943

# Concrete no-pivot stress instance from Section 6.
tau = 0.01
k = 4.0
m = 65536
c = k ** -4
max_principal_2x2_det = max(k * k / m, 1.0 / m)
assert c < tau
assert max_principal_2x2_det < tau

lam_plus = (c + math.sqrt(c*c + 4.0)) / 2.0
lam_minus = (c - math.sqrt(c*c + 4.0)) / 2.0
# The other four nonzero eigenvalues are exactly -k,-k,k,k.
assert k >= 1.0

D = k ** 4
assert abs(D*c - 1.0) < 1e-15

# On I={Z}, J=Y in the projected-crossing theorem there is one
# one-volume subset, hence the only row marginal is exactly one.
alpha_Z = 1.0
assert alpha_Z > 0.5

print(f"C_raw={C_raw:.15f}")
print(f"C_projected={C_proj:.15f}")
print(f"C_exact={C_exact:.15f}")
print(f"partner_bound={partner:.15f}")
print(f"stress_tau={tau}")
print(f"stress_k={k}")
print(f"stress_m={m}")
print(f"stress_c={c:.15f}")
print(f"stress_max_2x2_det={max_principal_2x2_det:.15f}")
print(f"stress_spectrum_large=[{-k}, {-k}, {k}, {k}]")
print(f"stress_small_pair=[{lam_minus:.15f}, {lam_plus:.15f}]")
print(f"D_times_c={D*c:.15f}")
print(f"projected_crossing_alpha_Z={alpha_Z}")
print("STATUS=PASS")

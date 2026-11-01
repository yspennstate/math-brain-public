import math
import numpy as np

# New theorem constants.
ell = (1 / math.sqrt(7) + math.sqrt(6) / 13) ** 2
theta_min = 12 / 7
beta_min = theta_min / 2
C_H = (192 / (5 * math.sqrt(13))) * (12 * math.e) ** 0.25
C_pivot32 = C_H * math.sqrt(32)
C_example = C_H / math.sqrt(2)

# Partner-result application constant.
M3 = 288 * math.sqrt(3 * math.e) / 13
C_partner = 2 * math.sqrt(M3)

assert ell < 0.5
assert theta_min > 1
assert beta_min > 0.5
assert C_H < 25.453
assert C_pivot32 < 143.981
assert C_example < 17.998
assert C_partner < 15.908

# Full-rank target example from the report.
m = 64
u = np.zeros(m)
u[:32] = 1 / math.sqrt(32)
v = np.zeros(m)
v[32:] = 1 / math.sqrt(32)
P = np.outer(u, u) + np.outer(v, v)
S = 2 * np.outer(u, u) - 2 * np.outer(v, v) + (1 / 128) * (np.eye(m) - P)
a = 2.0
b = 0.01 * u
C = S + np.outer(b, b) / a
A = np.block([[np.array([[a]]), b.reshape(1, -1)], [b.reshape(-1, 1), C]])

# Schur complement and window leverage.
S_recovered = C - np.outer(b, b) / a
assert np.linalg.norm(S_recovered - S, 2) < 1e-12
assert np.max(np.diag(P)) <= 1 / 32 + 1e-12

eigs = np.linalg.eigvalsh(A)
abs_eigs = np.sort(np.abs(eigs))[::-1]
assert abs_eigs[2] > 1
assert np.min(np.abs(eigs)) > 0

print('STATUS=PASS')
print(f'ridge_leverage_upper={ell:.15f}')
print(f'theta_min={theta_min:.15f}')
print(f'beta_min={beta_min:.15f}')
print(f'C_H={C_H:.15f}')
print(f'C_pivot_abs_a_ge_1_over_32={C_pivot32:.15f}')
print(f'C_full_rank_example={C_example:.15f}')
print(f'partner_residual_density_M3={M3:.15f}')
print(f'partner_square_smoothing_constant={C_partner:.15f}')
print('largest_abs_eigenvalues=' + ','.join(f'{x:.15f}' for x in abs_eigs[:5]))
print(f'min_abs_eigenvalue={np.min(np.abs(eigs)):.15f}')

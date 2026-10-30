#!/usr/bin/env python3
import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923)
rows, cols = 11, 9
U, _ = np.linalg.qr(rng.normal(size=(rows, 2)))
V, _ = np.linalg.qr(rng.normal(size=(cols, 2)))
s = np.array([2.3, 0.7])
M = U @ np.diag(s) @ V.T

Z = 0.0
alpha_raw = np.zeros(rows)
beta_raw = np.zeros(cols)
for S in itertools.combinations(range(rows), 2):
    for T in itertools.combinations(range(cols), 2):
        d = np.linalg.det(M[np.ix_(S, T)])
        w = d*d
        Z += w
        for i in S:
            alpha_raw[i] += w
        for j in T:
            beta_raw[j] += w
alpha = alpha_raw/Z
beta = beta_raw/Z

sv = np.linalg.svd(M, compute_uv=False)
Z_spec = sum((sv[i]**2)*(sv[j]**2)
             for i in range(len(sv)) for j in range(i+1, len(sv)))
lev = np.sum(U**2, axis=1)

C_diffuse = 4*math.sqrt(2*math.e)
C_h34 = 4*math.sqrt(2*math.e)*(1.5**(-0.25))/(2-1.5)

print(f"Z_enum={Z:.16g}")
print(f"Z_spectral={Z_spec:.16g}")
print(f"Z_relative_error={abs(Z-Z_spec)/Z_spec:.3e}")
print(f"sum_alpha={alpha.sum():.16g}")
print(f"sum_beta={beta.sum():.16g}")
print(f"max_alpha_minus_exact_rank2_leverage={np.max(np.abs(alpha-lev)):.3e}")
print(f"max_alpha={alpha.max():.16g}")
print(f"C_diffuse={C_diffuse:.15f}")
print(f"C_h_le_3_over_4={C_h34:.15f}")
assert abs(Z-Z_spec)/Z_spec < 1e-12
assert abs(alpha.sum()-2) < 1e-12
assert abs(beta.sum()-2) < 1e-12
assert np.max(np.abs(alpha-lev)) < 1e-12
assert C_diffuse < 9.327
assert C_h34 < 16.856
print("STATUS=PASS")

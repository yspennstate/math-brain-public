import math
import numpy as np

N, M = 9, 16
u = np.ones(N) / math.sqrt(N)
v = np.ones(M) / math.sqrt(M)
n = 2 + N + M + 1
A = np.zeros((n, n))
ix, iy, iz = 0, 1, n - 1

for j, val in enumerate(u, start=2):
    A[ix, j] = A[j, ix] = val
    A[iy, j] = A[j, iy] = val
for j, val in enumerate(v, start=2 + N):
    A[ix, j] = A[j, ix] = val
    A[iy, j] = A[j, iy] = val
A[iz, iz] = 1.0

ev = np.linalg.eigvalsh(A)
nz = ev[np.abs(ev) > 1e-10]
partner_currency = np.linalg.norm(u) ** 2 * np.linalg.norm(v) ** 2
a = np.concatenate([u, v])
b = a.copy()
area = math.sqrt(max(0.0, np.dot(a,a)*np.dot(b,b)-np.dot(a,b)**2))
kappa = 0.8047423425494107
K_L = math.sqrt(math.e / 2.0)
claude_bound = 4 * 2**(3/4) * kappa * K_L**(3/4)
partner_prefactor = math.sqrt(math.e) / (127/800)**(1/8)

print("nonzero_eigenvalues", [round(float(x), 12) for x in nz])
print("cross_anchor_currency", round(partner_currency, 12))
print("shared_row_A_B", round(np.linalg.norm(a), 12), round(np.linalg.norm(b), 12))
print("shared_row_area", round(area, 12))
print("linear_form_cap", round(K_L, 12))
print("claude_collinear_bound", round(claude_bound, 12))
print("partner_transverse_prefactor", round(partner_prefactor, 12))
print("eta_1_bound_constant", round(4*partner_prefactor, 12))

import math
import numpy as np

# Constants from the grouped-hub theorem.
for h, r in [(2, 0), (3, 0), (1, 1), (2, 1)]:
    assert r + 2*h > 2
    C = math.e * (r + 2*h) / (r + 2*h - 2)
    print(f"h={h} r={r} product_corollary_constant={C:.15f}")

# Target-valid diffuse grouped-cross family.
N = 32
m = 16
s = np.ones(N)
s[N//2:] = -1.0
P = np.column_stack([np.ones(N), s]) / math.sqrt(N)
C = np.zeros((2*m, 2))
C[:m, 0] = 1.0 / math.sqrt(m)
C[m:, 1] = 1.0 / math.sqrt(m)
assert np.allclose(P.T @ P, np.eye(2))
assert np.allclose(C.T @ C, np.eye(2))
B = P @ C.T
A = np.block([[np.zeros((N, N)), B], [B.T, np.zeros((2*m, 2*m))]])
evals = np.linalg.eigvalsh(A)
nonzero = evals[np.abs(evals) > 1e-9]
assert np.allclose(nonzero, np.array([-1.0, -1.0, 1.0, 1.0]), atol=1e-8)

rho = (1.0 - 1.0/m)**2
bound = 2.0 * math.e * rho**(-0.25)
print(f"rho={rho:.15f}")
print(f"m16_grouped_bound={bound:.15f}")
assert bound < 5.615

# Literal physical hub pair determinants: zero for equal signs, 4/N^2 for opposite signs.
row_gram_dets = []
for j in range(N):
    for k in range(j+1, N):
        R = B[[j, k], :]
        row_gram_dets.append(np.linalg.det(R @ R.T))
vals = sorted(set(round(float(x), 14) for x in row_gram_dets))
print("literal_pair_gram_determinants=", vals)
assert max(row_gram_dets) <= 4.0/N**2 + 1e-12
assert min(row_gram_dets) >= -1e-12

# Exponential cancellation in the product-law corollary.
for h, r in [(1, 1), (2, 0), (2, 3), (3, 0), (4, 2)]:
    lhs = math.exp((r+h)/(r+2*h)) * math.exp((h/2)*(2/(r+2*h)))
    assert abs(lhs - math.e) < 1e-12

print("PASS QFORM fleet03/B09 r29 grouped-hub checks")

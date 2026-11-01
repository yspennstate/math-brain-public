import itertools
import math
import numpy as np


def harmonic(m):
    j = np.arange(m, dtype=float)
    b = np.sqrt(2.0 / m) * np.cos(2.0 * np.pi * j / m)
    d = np.sqrt(2.0 / m) * np.sin(2.0 * np.pi * j / m)
    A = np.zeros((m + 1, m + 1))
    A[0, 1:] = b
    A[1:, 0] = b
    A[1:, 1:] = np.outer(d, d)
    return b, d, A


m = 8
b, d, A = harmonic(m)
G = np.array([[b @ b, b @ d], [b @ d, d @ d]])
assert np.allclose(G, np.eye(2), atol=1e-12)
lev = b * b + d * d
assert np.allclose(lev, np.full(m, 2.0 / m), atol=1e-12)

eig = np.linalg.eigvalsh(A)
assert np.allclose(eig[[0, -2, -1]], [-1.0, 1.0, 1.0], atol=1e-12)
assert np.max(np.abs(eig[1:-2])) < 1e-12

pair_scales = []
for j in range(m):
    P = A[np.ix_([0, j + 1], [0, j + 1])]
    pe = np.linalg.eigvalsh(P)
    D = abs(np.linalg.det(P))
    kappa = np.min(np.abs(pe))
    zeta = (D * D * kappa) ** 0.2 if D > 1e-15 and kappa > 1e-15 else 0.0
    pair_scales.append(zeta)
assert abs(max(pair_scales) - math.sqrt(2.0 / m)) < 1e-12

# Exhaustively enumerate all disjoint cuts for n=9 for which a third singular
# value could exist. The analytic rank-at-most-two proof is in REPORT.md; this
# is only a finite algebraic regression of the harmonic witness.
max_s3 = 0.0
cuts = 0
n = m + 1
for assignment in itertools.product((0, 1, 2), repeat=n):
    I = [i for i, a in enumerate(assignment) if a == 1]
    J = [i for i, a in enumerate(assignment) if a == 2]
    if len(I) < 3 or len(J) < 3:
        continue
    s = np.linalg.svd(A[np.ix_(I, J)], compute_uv=False)
    max_s3 = max(max_s3, float(s[2]))
    cuts += 1
assert max_s3 < 1e-12

kappa0 = (math.sqrt(17.0) - 1.0) / 8.0
delta0 = (kappa0 / 16.0) ** 0.2
pair_constant = 3.0 * (400.0 ** (1.0 / 3.0)) * delta0 ** (-5.0 / 6.0)
diffuse_constant = 3.0 * math.exp(2.0 / 3.0)
assert pair_constant < 41.044
assert diffuse_constant < 5.844
assert max(256.0, pair_constant, diffuse_constant) == 256.0

print('m', m)
print('gram', G.tolist())
print('max_row_leverage', float(lev.max()))
print('nonzero_eigenvalues', [float(eig[0]), float(eig[-2]), float(eig[-1])])
print('max_partner_pair_scale', max(pair_scales))
print('predicted_max_pair_scale', math.sqrt(2.0 / m))
print('cuts_checked', cuts)
print('max_cross_cut_s3', max_s3)
print('diffuse_constant', diffuse_constant)
print('heavy_pair_kappa0', kappa0)
print('heavy_pair_delta0', delta0)
print('heavy_pair_constant', pair_constant)
print('global_subclass_constant', 256.0)
print('QFORM_HUB_FRESNEL_R16_CHECK_PASS')

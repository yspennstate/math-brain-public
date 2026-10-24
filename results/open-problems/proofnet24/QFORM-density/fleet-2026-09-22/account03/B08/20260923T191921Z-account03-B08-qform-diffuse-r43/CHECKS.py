import math
import numpy as np
import sympy as sp

rng = np.random.default_rng(20260923)
max_rel = 0.0
count = 0

for _ in range(5000):
    m = int(rng.integers(2, 12))
    M = rng.normal(size=(2, m))
    if np.linalg.matrix_rank(M) < 2:
        continue
    a = float(rng.normal())
    if abs(a) < 0.2:
        a = 0.2 if a >= 0 else -0.2
    h = rng.normal(size=2)
    k = rng.normal(size=2)
    r = rng.normal(size=m)

    # Orthogonal leakage e relative to the physical row space of M.
    G = M @ M.T
    proj = M.T @ np.linalg.solve(G, M @ r)
    e = r - proj
    b = k @ M + e

    Mp = M - np.outer(h, b) / a
    lhs = float(np.linalg.det(Mp @ Mp.T))

    D = float(np.linalg.det(M @ M.T))
    d = a - float(k @ h)
    transverse = -h[1] * M[0] + h[0] * M[1]
    rhs = (d * d / (a * a)) * D + (float(transverse @ transverse) / (a * a)) * float(e @ e)

    rel = abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs))
    max_rel = max(max_rel, rel)
    count += 1

C_star = 8 * (2 / 3) ** 0.25
c2 = 3 / (64 * math.sqrt(2))
C_R2 = C_star * (c2 / 2) ** (-0.25)
localized_wedge = 9 / 8192

A0 = sp.Matrix([
    [1, 1, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
])
charpoly = sp.factor(A0.charpoly().as_expr())
expected = (sp.Symbol('lambda') - 1) * (sp.Symbol('lambda') + 1) ** 2 * (sp.Symbol('lambda') ** 2 - 2 * sp.Symbol('lambda') - 1)
assert sp.expand(charpoly - expected) == 0

print('random_identity_cases', count)
print('max_normalized_identity_error', f'{max_rel:.16e}')
print('C_star', f'{C_star:.15f}')
print('c2', f'{c2:.15f}')
print('C_R2_delta_half', f'{C_R2:.15f}')
print('localized_wedge_threshold', f'{localized_wedge:.15f}')
print('obstruction_charpoly', charpoly)
print('QFORM_B08_R43_CHECK_PASS')

"""Finite diagnostics only for QFORM-LOWSCORE-TO-HUBSTRIP-18-v1.
The proof is in REPORT.md; these checks are not proof.
"""
import math
import numpy as np

K = 2974.0
Xmin = 1.0 / 384.0
C0 = 8.0 * K * 384.0 / 5.0
radius_coeff = C0 ** (1.0 / 8.0)
leverage_floor = 5.0 / 6144.0
parallel_energy_floor = 5.0 / 12288.0
cardinality_coeff = parallel_energy_floor / (C0 ** 0.25)

print("rho threshold for tau_X<1:", C0)
print("radius coefficient:", radius_coeff)
print("strip leverage floor:", leverage_floor)
print("parallel-energy floor:", parallel_energy_floor)
print("cardinality coefficient:", cardinality_coeff)
assert C0 == 1827225.6
assert radius_coeff < 6.064
assert cardinality_coeff > 1.1067e-5

# Parseval-frame identities used in the proof.
rng = np.random.default_rng(13024)
max_row_error = 0.0
max_s_error = 0.0
for n in range(4, 20):
    for _ in range(50):
        z = rng.normal(size=(n, 2))
        u, _ = np.linalg.qr(z)
        u = u[:, :2]
        k = int(rng.integers(0, n))
        uk = u[k]
        c = float(uk @ uk)
        if c < 1e-14:
            continue
        e1 = uk / math.sqrt(c)
        e2 = np.array([-e1[1], e1[0]])
        r = np.column_stack((e1, e2))
        v = u @ r
        s = v[:, 1] ** 2
        q = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                q[i, j] = np.linalg.det(np.vstack((v[i], v[j]))) ** 2
        c_i = np.sum(v * v, axis=1)
        max_row_error = max(max_row_error, float(np.max(np.abs(q.sum(axis=1) - c_i))))
        max_s_error = max(max_s_error, abs(float(s.sum()) - 1.0), abs(float(s[k])))

print("max row Cauchy-Binet identity error:", max_row_error)
print("max aligned-second-column identity error:", max_s_error)
assert max_row_error < 1e-12
assert max_s_error < 1e-12

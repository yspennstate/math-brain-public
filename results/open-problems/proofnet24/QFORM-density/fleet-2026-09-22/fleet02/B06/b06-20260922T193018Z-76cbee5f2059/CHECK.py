import math
import numpy as np

epsilon = 1.0 / 32.0
C0 = 4.0 + 2.0 * math.sqrt(3.0)
g = math.sqrt(epsilon / C0)
N = 64
M = 64

u = np.ones(M) / math.sqrt(M)
v = np.concatenate([np.ones(M // 2), -np.ones(M // 2)]) / math.sqrt(M)
assert abs(float(u @ u) - 1.0) < 1e-12
assert abs(float(v @ v) - 1.0) < 1e-12
assert abs(float(u @ v)) < 1e-12

H = np.vstack([u] + [v / math.sqrt(N) for _ in range(N)])
sv = np.linalg.svd(H, compute_uv=False)
assert abs(sv[0] - 1.0) < 1e-12 and abs(sv[1] - 1.0) < 1e-12
assert np.max(sv[2:]) < 1e-12

A = np.block([[np.zeros((N + 1, N + 1)), H],[H.T, np.zeros((M, M))]])
ev = np.linalg.eigvalsh(A)
large = [x for x in ev if abs(x) > 0.5]
assert len(large) == 4
assert np.max(np.abs(np.sort(large) - np.array([-1.0, -1.0, 1.0, 1.0]))) < 1e-11

G = H.T @ H + (g * g) * np.eye(M)
K = H @ np.linalg.solve(G, H.T)
s = 1.0 / (1.0 + g * g)
assert abs(float(np.trace(K)) - 2.0 * s) < 1e-11
assert abs(float(K[0, 0]) - s) < 1e-11
assert K[0, 0] > 1.0 - epsilon
assert np.trace(K) >= 2.0 - epsilon

pair_dets = []
for j in range(1, N + 1):
    d = float(np.linalg.det(K[np.ix_([0, j], [0, j])]))
    pair_dets.append(d)
assert max(abs(d - s * s / N) for d in pair_dets) < 1e-11
assert abs(sum(pair_dets) - s * s) < 1e-10
assert np.max(np.abs(H)) <= 1.0 / math.sqrt(M) + 1e-12

bilinear_bound = math.e * math.sqrt(2.0 * math.pi)
print("QFORM_B06_NEAR_COLOOP_BANK_CHECK_PASS")
print(f"epsilon={epsilon:.12f}")
print(f"C0={C0:.12f}")
print(f"g={g:.12f}")
print(f"s={s:.12f}")
print(f"traceK={np.trace(K):.12f}")
print(f"K00={K[0,0]:.12f}")
print(f"pair_det_each={pair_dets[0]:.12f}")
print(f"pair_det_sum={sum(pair_dets):.12f}")
print(f"max_abs_H_entry={np.max(np.abs(H)):.12f}")
print(f"bilinear_density_bound={bilinear_bound:.12f}")

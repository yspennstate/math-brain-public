import math
import numpy as np

SEED = 520926
rng = np.random.default_rng(SEED)
max_minor_error = 0.0
max_star_error = 0.0
min_sampled_cross_ratio = float('inf')
instances = 0

for N in [3, 4, 8, 16, 64]:
    for _ in range(200):
        Z = rng.normal(size=(N, 2))
        V, _ = np.linalg.qr(Z)
        V = V[:, :2]

        R, _ = np.linalg.qr(rng.normal(size=(3, 3)))
        lam = np.array([
            1.0 + 3.0*rng.random(),
            -(1.0 + 3.0*rng.random()),
            1.0 + 3.0*rng.random(),
        ])
        K = R @ np.diag(lam) @ R.T

        U = np.zeros((N+1, 3))
        U[0, 0] = 1.0
        U[1:, 1:] = V
        A = U @ K @ U.T
        detK = float(np.linalg.det(K))

        weights = []
        star = 0.0
        for j in range(N):
            for k in range(j+1, N):
                idx = [0, j+1, k+1]
                detA = float(np.linalg.det(A[np.ix_(idx, idx)]))
                pl = float(np.linalg.det(np.vstack([V[j], V[k]])))
                pred = detK * pl * pl
                scale = max(1.0, abs(detA), abs(pred))
                max_minor_error = max(max_minor_error, abs(detA-pred)/scale)
                star += abs(detA)
                weights.append((j, k, abs(detA)))

        max_star_error = max(
            max_star_error,
            abs(star-abs(detK))/max(1.0, abs(detK)),
        )

        # The analytic half-cut proof is expectation-based. This finite random
        # search is only a regression check that sampled cuts comfortably find
        # cross mass above the guaranteed 1/2 threshold.
        best = 0.0
        for _ in range(200):
            mask = rng.integers(0, 2, size=N)
            cross = sum(w for j, k, w in weights if mask[j] != mask[k])
            best = max(best, cross)
        min_sampled_cross_ratio = min(min_sampled_cross_ratio, best/abs(detK))
        instances += 1

C_heavy = 128.0 * 64.0**0.25
C_null = 3.0 * 2.0**(4.0/3.0)
m0 = math.sqrt(47.0/48.0)
strong_row = m0/(4.0*math.sqrt(2.0))
partner_row = 1.0/32768.0

assert max_minor_error < 1e-12
assert max_star_error < 1e-12
assert min_sampled_cross_ratio >= 0.5
assert C_heavy < 362.039
assert C_null < 7.560

print('QFORM_B08_R52_ALIGNED_ENDPOINT_CHECK_PASS')
print(f'seed={SEED}')
print(f'instances={instances}')
print(f'max_minor_relative_error={max_minor_error:.17g}')
print(f'max_star_relative_error={max_star_error:.17g}')
print(f'min_sampled_cross_ratio={min_sampled_cross_ratio:.17g}')
print(f'C_heavy={C_heavy:.15f}')
print(f'C_null={C_null:.15f}')
print(f'm0={m0:.15f}')
print(f'top2_localized_row_constant={strong_row:.15f}')
print(f'partner_fixed_scale_row_constant={partner_row:.15f}')

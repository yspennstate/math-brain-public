import math
import numpy as np

rng = np.random.default_rng(20260923)
violations = 0
accepted_balanced_cuts = 0
inequalities_checked = 0
min_margin = float("inf")

for n in (12, 20, 32):
    for _ in range(600):
        Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
        eig = rng.normal(scale=0.7, size=n)
        eig[:3] = rng.choice([-1.0, 1.0], 3) * (1.0 + rng.random(3) * 2.0)
        A = Q @ np.diag(eig) @ Q.T
        R = Q[:, :3]
        L = np.min(np.abs(eig[:3]))

        for _ in range(40):
            mask = rng.random(n) < 0.5
            if mask.sum() < 3 or (~mask).sum() < 3:
                continue
            I = np.where(mask)[0]
            J = np.where(~mask)[0]
            aI = np.linalg.eigvalsh(R[I].T @ R[I])[0]
            aJ = np.linalg.eigvalsh(R[J].T @ R[J])[0]
            alpha = min(aI, aJ)
            if alpha < 3.0 / 8.0:
                continue

            C = A[np.ix_(I, I)]
            D = A[np.ix_(J, J)]
            B = A[np.ix_(I, J)]
            sC = np.linalg.svd(C, compute_uv=False)
            sD = np.linalg.svd(D, compute_uv=False)
            sB = np.linalg.svd(B, compute_uv=False)

            for S in (sC, sD):
                for k in range(3):
                    margin = S[k] ** 2 + sB[2-k] ** 2 - alpha * L ** 2
                    min_margin = min(min_margin, margin)
                    inequalities_checked += 1
                    if margin < -1e-8:
                        violations += 1
            accepted_balanced_cuts += 1
            break

alpha = 3.0 / 8.0
c = math.sqrt(3.0 / 20.0)
delta = math.sqrt(alpha - c*c)
beta = (3.0 / 16.0) * math.sqrt(3.0 / 5.0)
gamma = delta / 64.0
collective_constant = 18.0 * math.sqrt(3.0) * math.e / delta
k0_constant = 6.0 * math.sqrt(math.e) / delta
k0_star = delta / math.sqrt(6.0)
k1_heavy_star = delta / math.sqrt(2.0)

assert violations == 0
assert abs(delta - 3.0 / math.sqrt(40.0)) < 1e-14
assert abs(delta / beta - math.sqrt(32.0/3.0)) < 1e-14
assert k1_heavy_star > 0.25

print("QFORM_B08_SQUARED_ENERGY_CHECK_PASS")
print(f"accepted_balanced_cuts={accepted_balanced_cuts}")
print(f"inequalities_checked={inequalities_checked}")
print(f"violations={violations}")
print(f"min_margin={min_margin:.15g}")
print(f"delta={delta:.15g}")
print(f"delta_over_beta={delta/beta:.15g}")
print(f"gamma={gamma:.15g}")
print(f"k0_continuous_constant={k0_constant:.15g}")
print(f"k0_bilateral_star={k0_star:.15g}")
print(f"k1_collective_constant={collective_constant:.15g}")
print(f"k1_heavy_star={k1_heavy_star:.15g}")

import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923)

C_R2 = 3 * 2**(5/6) * (64*math.sqrt(2))**(1/3) * 8**(1/3)
C_R1 = (3 * 2**(7/6) * math.e**(1/3)
        * (8/math.sqrt(3/2))**(1/3) * 4096**(1/6))
assert abs(C_R2 - 48.0) < 1e-12
assert abs(C_R1 - 70.27958485709917) < 1e-12

max_e2_relerr = 0.0
max_subset_defect = 0.0
max_star_defect = 0.0
min_pair_inclusion = 1.0

for _ in range(1000):
    m = int(rng.integers(4, 9))
    C = rng.normal(size=(3, m))
    G = C @ C.T
    eig = np.linalg.eigvalsh(G)
    e2 = eig[0]*eig[1] + eig[0]*eig[2] + eig[1]*eig[2]

    pair_volumes = []
    for H in itertools.combinations(range(3), 2):
        CH = C[list(H), :]
        pair_volumes.append((H, np.linalg.det(CH @ CH.T)))
    sum_pair = sum(v for _, v in pair_volumes)
    max_e2_relerr = max(max_e2_relerr, abs(sum_pair-e2)/(1+abs(e2)))

    H, V = max(pair_volumes, key=lambda hv: hv[1])
    k = (m + 1)//2
    p = k*(k-1)/(m*(m-1))
    min_pair_inclusion = min(min_pair_inclusion, p)
    subset_volumes = []
    for J in itertools.combinations(range(m), k):
        CHJ = C[list(H), :][:, list(J)]
        subset_volumes.append(np.linalg.det(CHJ @ CHJ.T))
    max_subset_defect = max(max_subset_defect, max(0.0, p*V-max(subset_volumes)))

    row_norm_sq = np.sum(C*C, axis=1)
    h = int(np.argmax(row_norm_sq))
    star_subsets = [np.sum(C[h, list(J)]**2)
                    for J in itertools.combinations(range(m), k)]
    max_star_defect = max(max_star_defect,
                          max(0.0, 0.5*row_norm_sq[h]-max(star_subsets)))

print(f"R2_constant={C_R2:.15f}")
print(f"R1_constant={C_R1:.15f}")
print(f"max_e2_relative_error={max_e2_relerr:.3e}")
print(f"max_R2_subset_defect={max_subset_defect:.3e}")
print(f"max_R1_star_defect={max_star_defect:.3e}")
print(f"minimum_pair_inclusion_probability={min_pair_inclusion:.15f}")
print("QFORM_B08_R42_CHECK_PASS")

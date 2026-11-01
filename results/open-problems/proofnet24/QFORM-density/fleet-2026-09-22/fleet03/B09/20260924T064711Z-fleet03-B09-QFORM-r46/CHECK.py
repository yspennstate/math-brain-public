import math
import numpy as np

SEED = 20260924
N = 2000
rng = np.random.default_rng(SEED)

max_detB = 0.0
max_id_rel = 0.0
min_ratio = float('inf')
checked = 0

for _ in range(N):
    # Exact algebraic rank-one semidefinite pair: b=c^2/a.
    a = rng.choice([-1.0, 1.0]) * rng.uniform(0.5, 2.0)
    c = rng.uniform(-1.5, 1.5)
    b = c * c / a
    if abs(a) < abs(b):
        a, b = b, a

    u, v, d = rng.uniform(-2.0, 2.0, size=3)
    P = np.array([[a, c, u], [c, b, v], [u, v, d]], dtype=float)

    detB = a * b - c * c
    detP = np.linalg.det(P)
    H = a * v - c * u

    max_detB = max(max_detB, abs(detB))
    rel = abs(H * H + a * detP) / max(1.0, abs(H * H), abs(a * detP))
    max_id_rel = max(max_id_rel, rel)

    eig = np.linalg.eigvalsh(P)
    sigma = float(np.min(np.abs(eig)))
    if sigma > 1e-7:
        assert abs(a) + 1e-9 >= sigma / 2.0
        ratio = abs(H) / (sigma * sigma)
        assert ratio + 1e-8 >= 1.0 / math.sqrt(2.0)
        min_ratio = min(min_ratio, ratio)
        checked += 1

# r45 exact no-go family, epsilon=1/2.
eps = 0.5
P = 2.0 * np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1]], dtype=float)
C = eps * np.array([[1, 0], [0, 1], [0, 0]], dtype=float)
A = np.block([[P, C], [C.T, np.zeros((2, 2))]])
eigA = np.linalg.eigvalsh(A)
assert np.sum(np.abs(eigA) >= 1.0 - 1e-12) == 3

a, c = P[0, 0], P[0, 1]
u = np.r_[P[0, 2], C[0]]
v = np.r_[P[1, 2], C[1]]
Hvec = a * v - c * u
assert np.allclose(Hvec, np.array([-8.0, -1.0, 1.0]))
Hnorm = np.linalg.norm(Hvec)
direct = 2.0 ** (11.0 / 4.0) / math.sqrt(Hnorm)
sigmaP = float(np.min(np.abs(np.linalg.eigvalsh(P))))
local = 8.0 / sigmaP

# Designated fleet04/B09 partner regression.
K = np.diag([3.0, 2.0, 1.0])
Across = np.block([[np.zeros((3, 3)), K], [K, np.zeros((3, 3))]])
eigCross = np.linalg.eigvalsh(Across)
assert np.allclose(eigCross, np.array([-3.0, -2.0, -1.0, 1.0, 2.0, 3.0]))
partner = 3.0 * np.linalg.det(K) ** (-1.0 / 3.0)

print(f"seed={SEED}")
print(f"random_trials={N}")
print(f"usable_nondegenerate_triples={checked}")
print(f"max_abs_singular_pair_det={max_detB:.17g}")
print(f"max_relative_H2_plus_a_detP_error={max_id_rel:.17g}")
print(f"minimum_observed_absH_over_sigma2={min_ratio:.15g}")
print(f"theoretical_lower_bound_1_over_sqrt2={1/math.sqrt(2):.15g}")
print()
print(f"r45_no_go_eps={eps}")
print(f"r45_no_go_full_spectrum={eigA.tolist()}")
print(f"r45_no_go_target_large_count={int(np.sum(np.abs(eigA)>=1-1e-12))}")
print(f"r45_pair_polynomial_star={Hvec.tolist()}")
print(f"r45_pair_polynomial_star_norm={Hnorm:.15g}")
print(f"r45_direct_singular_star_density_bound={direct:.15g}")
print(f"r45_local3_sigma={sigmaP:.15g}")
print(f"r45_local3_universal_density_bound_8_over_sigma={local:.15g}")
print()
print(f"partner_K_det={np.linalg.det(K):.15g}")
print(f"partner_full_spectrum={eigCross.tolist()}")
print(f"partner_density_bound_3_detK_minus_1_over_3={partner:.15g}")
print()
print("ALL_ASSERTIONS_PASSED")

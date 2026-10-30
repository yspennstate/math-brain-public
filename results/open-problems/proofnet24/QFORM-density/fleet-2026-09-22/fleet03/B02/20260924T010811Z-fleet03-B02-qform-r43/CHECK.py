import math
import numpy as np

SEED = 2026092401
CASES = 3000
THETA = 1.0 / 4.0
rng = np.random.default_rng(SEED)

viol_s = 0
viol_spec = 0
max_s_ratio = 0.0
min_spec_ratio = float("inf")

for _ in range(CASES):
    nl = int(rng.integers(1, 7))
    nr = int(rng.integers(1, 7))
    nh = int(rng.integers(1, 7))

    N = rng.normal(size=(nl, nr))
    C = rng.normal(size=(nl, nh))
    R = rng.normal(size=(nr, nh))

    S = 0.0
    for h in range(nh):
        c = C[:, h]
        r = R[:, h]
        nc2 = float(c @ c)
        nr2 = float(r @ r)
        Pc = np.eye(nl) if nc2 == 0 else np.eye(nl) - np.outer(c, c) / nc2
        Pr = np.eye(nr) if nr2 == 0 else np.eye(nr) - np.outer(r, r) / nr2
        S += nc2 * nr2 * np.linalg.norm(Pc @ N @ Pr, "fro") ** 2

    E_star = np.linalg.norm(np.vstack([C, R]), "fro") ** 2
    E_N = np.linalg.norm(N, "fro") ** 2
    rhs = 0.25 * E_N * E_star ** 2
    if S > rhs + 1e-9 * (1.0 + rhs):
        viol_s += 1
    if rhs > 0:
        max_s_ratio = max(max_s_ratio, S / rhs)

    m = int(rng.integers(3, 9))
    n = int(rng.integers(3, 9))
    M = rng.normal(size=(m, n))
    x = np.linalg.svd(M, compute_uv=False) ** 2
    E = float(x.sum())
    x2 = float(x[1]) if len(x) > 1 else 0.0
    T2 = float(x[2:].sum()) if len(x) > 2 else 0.0

    e3 = 0.0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            for k in range(j + 1, len(x)):
                e3 += float(x[i] * x[j] * x[k])

    if x2 >= THETA * E and T2 >= THETA * E:
        floor = THETA ** 3 * E ** 3
        if e3 + 1e-9 * (1.0 + floor) < floor:
            viol_spec += 1
        min_spec_ratio = min(min_spec_ratio, e3 / floor)

C3 = 3 * 2 ** (4 / 3) * math.e ** (1 / 3)
strong_cut = 11907 / 16384

print({
    "seed": SEED,
    "cases": CASES,
    "theta": THETA,
    "S_inequality_violations": viol_s,
    "max_observed_S_over_rhs": max_s_ratio,
    "spectral_dichotomy_violations": viol_spec,
    "min_observed_e3_over_theta3E3_on_nontube": min_spec_ratio,
    "C3": C3,
    "grouped_density_constant_theta_quarter_S": 6 * math.e ** (1 / 3) * THETA ** (-1 / 2),
    "V1_density_coefficient_theta_quarter": 3 * 2 ** (2 / 3) * 5 ** (5 / 6) * math.e ** (1 / 3) * THETA ** (-1 / 2),
    "V1_absolute_density_bound_when_V1_gt_quarter": 6 * 5 ** (5 / 6) * math.e ** (1 / 3) * THETA ** (-1 / 2),
    "partner_hybrid_front_coefficient": 2 ** (29 / 12) * 3 ** (1 / 4) * math.e ** (1 / 4),
    "partner_strongcut_consistency_density": C3 * (1048576 / 63) ** (1 / 6) * strong_cut ** (-1 / 2),
})

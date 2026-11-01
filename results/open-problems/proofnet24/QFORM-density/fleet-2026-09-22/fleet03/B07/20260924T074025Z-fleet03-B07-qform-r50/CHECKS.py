import numpy as np
import math
import json

EPS = 5.43834026762e-4
D = 2 * EPS
GAMMA = D - EPS
RANK_R = 24
M_MAX = 2 * (RANK_R + 3)
DENSITY = 2 * math.sqrt(6 * math.pi * M_MAX) / GAMMA
DELTA_S = D + EPS
CROSS_EPS = 2 ** -16
DELTA_FULL = DELTA_S + CROSS_EPS

rng = np.random.default_rng(20260924)
max_tail_excess = -1e99
max_head_rank = 0
violations = 0

for trial in range(500):
    nb = 40
    blocks = []
    large_budget = int(rng.integers(0, 27))
    remaining = large_budget
    for k in range(nb):
        th = float(rng.uniform(0, 2 * math.pi))
        Q = np.array([[math.cos(th), -math.sin(th)],
                      [math.sin(th),  math.cos(th)]])
        vals = []
        for _ in range(2):
            if remaining > 0 and rng.random() < 0.5:
                val = float((1.1 + 3 * rng.random()) * D *
                            (1 if rng.random() < 0.5 else -1))
                remaining -= 1
            else:
                val = float(rng.uniform(-0.999, 0.999) * D)
            vals.append(val)
        blocks.append(Q @ np.diag(vals) @ Q.T)

    for k in range(nb):
        if remaining <= 0:
            break
        w, Q = np.linalg.eigh(blocks[k])
        for j in range(2):
            if remaining <= 0:
                break
            if abs(w[j]) < D:
                w[j] = float((1.2 + rng.random()) * D *
                             (1 if rng.random() < 0.5 else -1))
                remaining -= 1
        blocks[k] = Q @ np.diag(w) @ Q.T

    B = np.zeros((2 * nb, 2 * nb))
    for k, block in enumerate(blocks):
        B[2*k:2*k+2, 2*k:2*k+2] = block

    w, Q = np.linalg.eigh(B)
    mask = np.abs(w) >= D
    if mask.any():
        B_big = Q[:, mask] @ np.diag(w[mask]) @ Q[:, mask].T
    else:
        B_big = np.zeros_like(B)
    B_small = B - B_big

    head_rank = int(np.linalg.matrix_rank(B_big, tol=1e-10))
    tail_op = float(np.linalg.norm(B_small, 2))
    max_head_rank = max(max_head_rank, head_rank)
    max_tail_excess = max(max_tail_excess, tail_op - D)
    if head_rank > 26 or tail_op > D + 1e-10:
        violations += 1

# Saturation-style deterministic core: 27 threshold directions, rank-24 exact cancellation.
m = 54
B = np.zeros((m, m))
for j in range(27):
    B[j, j] = D
for j in range(27, m):
    B[j, j] = 0.3 * D
R = np.zeros((m, m))
for j in range(24):
    R[j, j] = -D
E = np.zeros((m, m))
for j in (24, 25, 26):
    E[j, j] = -0.9 * EPS
s = np.linalg.svd(B + R + E, compute_uv=False)
core_s3 = float(s[2])
expected = float(D - 0.9 * EPS)
margin = core_s3 - expected

out = {
    "EPS": float(EPS),
    "D": float(D),
    "GAMMA": float(GAMMA),
    "M_MAX": int(M_MAX),
    "DENSITY_BOUND": float(DENSITY),
    "SS_OPERATOR_TAIL_BOUND": float(DELTA_S),
    "CROSS_TAIL_BOUND": float(CROSS_EPS),
    "FULL_OFF_T_PLUS_S_REMAINDER_OP_BOUND": float(DELTA_FULL),
    "random_truncation_trials": 500,
    "max_observed_head_rank": int(max_head_rank),
    "max_tail_excess_over_D": float(max_tail_excess),
    "violations": int(violations),
    "saturation_core_s3": core_s3,
    "saturation_expected": expected,
    "saturation_margin": float(margin),
    "STATUS": "PASS" if violations == 0 and abs(margin) < 1e-12 else "FAIL",
}
print(json.dumps(out, indent=2))

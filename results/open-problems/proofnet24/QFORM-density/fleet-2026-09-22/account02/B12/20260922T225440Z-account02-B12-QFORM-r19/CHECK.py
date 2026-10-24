import json
import math
import numpy as np

rng = np.random.default_rng(20260922)

reserve_trials = 0
reserve_min_margin = float("inf")
for d in range(5, 13):
    max_r = min(4, d - 3)
    for r in range(1, max_r + 1):
        for _ in range(120):
            Q, _ = np.linalg.qr(rng.normal(size=(d, d)))
            vals = (1.0 + rng.random(d)) * rng.choice([-1.0, 1.0], size=d)
            H0 = Q @ np.diag(vals) @ Q.T
            U = rng.normal(size=(d, r))
            C = rng.normal(size=(r, r))
            C = (C + C.T) / 2
            E = (10.0 ** rng.uniform(-1, 3)) * U @ C @ U.T
            s0 = np.linalg.svd(H0, compute_uv=False)
            sf = np.linalg.svd(H0 + E, compute_uv=False)
            margin = float(sf[2] - s0[2 + r])
            if margin < -1e-9:
                raise AssertionError((d, r, margin))
            reserve_min_margin = min(reserve_min_margin, margin)
            reserve_trials += 1

pair_trials = 0
pair_min_gap_margin = float("inf")
for _ in range(3000):
    beta0 = 0.4 + rng.random() * 1.5
    a = beta0 + rng.random() * 2
    b = beta0 + rng.random() * 2
    th = rng.random() * 2 * np.pi
    O = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    B0 = O @ np.diag([a, -b]) @ O.T
    delta = beta0 * (0.05 + 0.8 * rng.random())
    F = rng.normal(size=(2, 2))
    F = (F + F.T) / 2
    F *= delta / np.linalg.norm(F, 2)
    B = B0 + F
    eig = np.linalg.eigvalsh(B)
    if not (eig[0] < 0 < eig[1]):
        raise AssertionError((beta0, delta, eig.tolist()))
    smin = np.linalg.svd(B, compute_uv=False)[-1]
    margin = float(smin - (beta0 - delta))
    if margin < -1e-9:
        raise AssertionError((beta0, delta, margin))
    pair_min_gap_margin = min(pair_min_gap_margin, margin)
    pair_trials += 1

explicit_r_max = 12
explicit_cases = 0
explicit_min_s3 = float("inf")
for r in range(1, explicit_r_max + 1):
    for _ in range(80):
        mus = rng.uniform(-1e6, 1e6, size=r)
        diag = np.concatenate(([1.0, -1.0, 1.0], mus))
        s = np.sort(np.abs(diag))[::-1]
        if s[2] < 1 - 1e-12:
            raise AssertionError((r, mus.tolist(), s.tolist()))
        explicit_min_s3 = min(explicit_min_s3, float(s[2]))
        explicit_cases += 1

result = {
    "status": "PASS",
    "check": "QFORM_RANK_RESERVE_PAIR_COMPRESSION_CHECK_PASS",
    "constant_indefinite_unit_gap": 6 * (400 ** (1 / 3)),
    "reserve_random_trials": reserve_trials,
    "reserve_min_margin": reserve_min_margin,
    "pair_inertia_random_trials": pair_trials,
    "pair_min_gap_margin": pair_min_gap_margin,
    "explicit_eigenvalue_replacement_cases": explicit_cases,
    "explicit_r_max": explicit_r_max,
    "explicit_min_s3": explicit_min_s3,
    "note": "Randomized checks are sanity checks only. The proof in REPORT.md is exact; small positive margins are floating-point observations."
}
print(json.dumps(result, indent=2, sort_keys=True))

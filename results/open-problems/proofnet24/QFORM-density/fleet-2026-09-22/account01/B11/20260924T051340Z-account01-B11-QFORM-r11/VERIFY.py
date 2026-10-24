#!/usr/bin/env python3
"""Regression checks for QFORM-NEARCOLOOP-SPECTRAL-DEFECT-LADDER-v1.
The proof itself is exact algebra in REPORT.md.
"""
import math
import json
import numpy as np

rng = np.random.default_rng(20260924)
N = 20000
worst1 = worst2 = worst3 = float("inf")
max_det_rel = 0.0
violations = 0

for _ in range(N):
    O, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    vals = np.array([
        1 + 7*rng.random(),
        1 + 7*rng.random(),
        -(1 + 7*rng.random()),
    ])
    M = O @ np.diag(vals) @ O.T
    s = float(np.min(np.abs(vals)))
    q = float(rng.uniform(0.500001, 0.999999))
    delta = 1-q
    P = np.diag([math.sqrt(delta), 1.0, 1.0])
    B = P @ M @ P
    sv = np.linalg.svd(B, compute_uv=False)

    r1 = sv[0]/s
    r2 = sv[1]/(s*math.sqrt(delta))
    r3 = sv[2]/(s*delta)
    worst1 = min(worst1, r1)
    worst2 = min(worst2, r2)
    worst3 = min(worst3, r3)

    expected = delta*np.linalg.det(M)
    det_rel = abs(np.linalg.det(B)-expected)/max(abs(expected), 1e-300)
    max_det_rel = max(max_det_rel, det_rel)

    if r1 < 1-1e-10 or r2 < 1-1e-10 or r3 < 1-1e-10:
        violations += 1

out = {
    "tests": N,
    "min_s1_over_s": worst1,
    "min_s2_over_s_sqrtdelta": worst2,
    "min_s3_over_s_delta": worst3,
    "max_relative_det_error": max_det_rel,
    "violations": violations,
}
print(json.dumps(out, indent=2))
if violations:
    raise SystemExit("QFORM_B11_DEFECT_LADDER_CHECK_FAIL")
print("QFORM_B11_DEFECT_LADDER_CHECK_PASS")

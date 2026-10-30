#!/usr/bin/env python3
"""Finite sanity check for Lemma 4.1; not a proof."""

import json
import numpy as np

rng = np.random.default_rng(20260923)
max_det_error = 0.0
min_gate_slack = float("inf")
trials = 20000

for _ in range(trials):
    z = rng.normal(size=(3, 3))
    q, _ = np.linalg.qr(z)
    lam = rng.uniform(0.05, 5.0, size=2) * rng.choice([-1.0, 1.0], size=2)
    b = q[:, :2] @ np.diag(lam) @ q[:, :2].T
    k = q[:, 2]
    c = rng.normal(size=3)
    d = rng.normal()
    h = np.block([[b, c[:, None]], [c[None, :], np.array([[d]])]])
    a = float(k @ c)
    target = abs(lam[0] * lam[1]) * a * a
    det_error = abs(abs(np.linalg.det(h)) - target)
    max_det_error = max(max_det_error, det_error)
    s = np.linalg.svd(h, compute_uv=False)
    gate = abs(a) * np.sqrt(abs(lam[0] * lam[1])) / np.sqrt(s[0] * s[1])
    min_gate_slack = min(min_gate_slack, float(s[2] - gate))

print(json.dumps({
    "seed": 20260923,
    "trials": trials,
    "max_abs_det_identity_error": max_det_error,
    "minimum_s3_minus_gate": min_gate_slack,
    "status": "PASS" if min_gate_slack >= -1e-10 and max_det_error < 1e-9 else "FAIL",
}, indent=2))

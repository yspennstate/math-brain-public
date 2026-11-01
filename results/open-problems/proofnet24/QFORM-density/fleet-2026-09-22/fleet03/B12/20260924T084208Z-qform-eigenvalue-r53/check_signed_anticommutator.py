#!/usr/bin/env python3
"""Deterministic consistency checks for fleet03/B12 r53.

These tests do not prove the theorem.  They check the finite-dimensional
singular-value inequalities used in REPORT.md on seeded symmetric matrices.
"""
import json
import math
import numpy as np

SEED = 202609240842
rng = np.random.default_rng(SEED)


def svals(a):
    return np.linalg.svd(a, compute_uv=False)


def active_basis(m, tol=1e-10):
    _, s, vt = np.linalg.svd(m, full_matrices=False)
    r = int(np.sum(s > tol))
    return vt[:r].T, s[:r]


def theorem_data(m, n):
    v, _ = active_basis(m)
    r = v.shape[1]
    gram = v.T @ m.T @ m @ v
    ew, q = np.linalg.eigh(gram)
    gram_mhalf = q @ np.diag(1.0 / np.sqrt(ew)) @ q.T
    u = m @ v @ gram_mhalf
    b = u.T @ n @ v @ gram_mhalf
    h = (b + b.T) / 2.0
    mu = np.linalg.eigvalsh(h)
    return r, math.sqrt(float(ew.min())), mu, svals(m + n)


single_violations = 0
single_min_margin = float("inf")
single_tests = 0
for _ in range(10000):
    n = 12
    m = 6
    a = rng.normal(size=(n, n))
    a = (a + a.T) / 2.0
    a += np.diag(np.linspace(2.0, 4.0, n))
    e = rng.normal(size=(n, n))
    e = (e + e.T) / 2.0
    carrier = a[:, :m]
    added = e[:, :m]
    r, g, mu, sv = theorem_data(carrier, added)
    if r < m:
        continue
    for q in range(r):
        rhs = g * max(1.0 + float(mu[q]), 0.0)
        lhs = float(sv[r - q - 1])
        margin = lhs - rhs
        single_min_margin = min(single_min_margin, margin)
        single_tests += 1
        if margin < -1e-8:
            single_violations += 1


multi_violations = 0
multi_min_margin = float("inf")
positive_rhs = 0
for _ in range(10000):
    n = 12
    m = 6
    a = rng.normal(size=(n, n))
    a = (a + a.T) / 2.0
    a += np.diag(np.linspace(2.0, 4.0, n))
    carrier = a[:, :m]
    v, _ = active_basis(carrier)
    if v.shape[1] < m:
        continue
    gram = v.T @ carrier.T @ carrier @ v
    ew, q = np.linalg.eigh(gram)
    gram_mhalf = q @ np.diag(1.0 / np.sqrt(ew)) @ q.T
    u = carrier @ v @ gram_mhalf
    total_added = np.zeros_like(carrier)
    etas = []
    for _packet in range(3):
        e = rng.normal(size=(n, n))
        e = 0.18 * (e + e.T) / 2.0
        added = e[:, :m]
        total_added += added
        b = u.T @ added @ v @ gram_mhalf
        h = (b + b.T) / 2.0
        heig = np.linalg.eigvalsh(h)
        destructive = np.sort(np.maximum(-heig, 0.0))[::-1]
        etas.append(float(destructive[1]))  # spend q_l=1
    eta = sum(etas)
    g = math.sqrt(float(ew.min()))
    rhs = g * max(1.0 - eta, 0.0)
    lhs = float(svals(carrier + total_added)[2])  # s_3; m-Q=6-3
    if rhs > 0.0:
        positive_rhs += 1
    margin = lhs - rhs
    multi_min_margin = min(multi_min_margin, margin)
    if margin < -1e-8:
        multi_violations += 1


k3 = 3.0 * 2.0 ** (4.0 / 3.0) * math.exp(1.0 / 3.0)
c6 = math.sqrt(24.0 * math.pi * 6.0 + k3 * k3)
l = 1_000_000.0
kappa = np.array([-1.0, -0.25, l, l**2, 3.0, l**3])
explicit_sv = sorted((2.0 * np.abs(1.0 + kappa)).tolist(), reverse=True)

results = {
    "seed": SEED,
    "single_packet": {
        "random_instances": 10000,
        "all_q_tests": single_tests,
        "violations": single_violations,
        "minimum_margin": single_min_margin,
    },
    "three_packet_q1_each": {
        "random_instances": 10000,
        "positive_rhs_instances": positive_rhs,
        "violations": multi_violations,
        "minimum_margin": multi_min_margin,
    },
    "explicit_partner_family": {
        "L": l,
        "kappa": kappa.tolist(),
        "carrier_singular_values_desc": explicit_sv,
        "s5_exact": explicit_sv[4],
        "theorem_s5_lower": 1.5,
        "with_tail_0p1_lower": 1.4,
        "K3": k3,
        "C6": c6,
        "density_bound_no_tail": c6 / 1.5,
        "density_bound_tail_0p1": c6 / 1.4,
    },
}

print(json.dumps(results, indent=2, sort_keys=True))

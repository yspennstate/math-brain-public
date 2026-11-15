"""Bounded, standard-library-only checks for PROOF.md; no training library."""

import json
import math
import os
import random
import resource
import signal
import sys
from fractions import Fraction as F
from pathlib import Path


limit_notes = []
data_soft, data_hard = resource.getrlimit(resource.RLIMIT_DATA)
memory_cap = 768 * 1024**2 if data_hard == resource.RLIM_INFINITY else min(768 * 1024**2, data_hard)
try:
    resource.setrlimit(resource.RLIMIT_DATA, (memory_cap, data_hard))
except (ValueError, OSError) as error:
    limit_notes.append("RLIMIT_DATA: " + str(error))
cpu_soft, cpu_hard = resource.getrlimit(resource.RLIMIT_CPU)
cpu_cap = 15 if cpu_hard == resource.RLIM_INFINITY else min(15, cpu_hard)
try:
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_cap, cpu_hard))
except (ValueError, OSError) as error:
    limit_notes.append("RLIMIT_CPU: " + str(error))
signal.alarm(30)
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, ("Refusing numerical work at insufficient nice value", priority)
assert os.environ.get("OMP_NUM_THREADS") == "1"


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def transpose_times(w, a):
    return [sum(w[i][j] * a[i] for i in range(len(a))) for j in range(len(w[0]))]


def state(a, w, b):
    v = transpose_times(w, a)
    r = [x - y for x, y in zip(v, b)]
    ga = [dot(row, r) for row in w]
    gw = [[x * y for y in r] for x in a]
    s = dot(a, a) + sum(dot(row, row) for row in w)
    return v, r, ga, gw, s, dot(r, r) / 2


def step(a, w, b, eta):
    v, r, ga, gw, s, loss = state(a, w, b)
    return ([x - eta * y for x, y in zip(a, ga)],
            [[x - eta * y for x, y in zip(row, grow)] for row, grow in zip(w, gw)])


def imbalance(a, w):
    return [[dot(w[i], w[j]) - a[i] * a[j] for j in range(len(a))]
            for i in range(len(a))]


def hessian(a, w, b):
    m, d = len(a), len(b)
    v, r, *_ = state(a, w, b)
    p = m + m * d
    h = [[0 for _ in range(p)] for _ in range(p)]
    for i in range(m):
        for k in range(m):
            h[i][k] = dot(w[i], w[k])
        for k in range(m):
            for ell in range(d):
                cross = (r[ell] if i == k else 0) + a[k] * w[i][ell]
                h[i][m + k * d + ell] = cross
                h[m + k * d + ell][i] = cross
    for i in range(m):
        for k in range(m):
            for j in range(d):
                h[m + i * d + j][m + k * d + j] = a[i] * a[k]
    return h


def flatten(a, w):
    return list(a) + [x for row in w for x in row]


def unflatten(theta, m, d):
    return theta[:m], [theta[m + i * d:m + (i + 1) * d] for i in range(m)]


def gradient_flat(theta, m, d, b):
    a, w = unflatten(theta, m, d)
    _, _, ga, gw, *_ = state(a, w, b)
    return flatten(ga, gw)


rng = random.Random(22620261114)
exact_count = 0
for case in range(24):
    m, d = 3, 2
    a = [F(rng.randrange(-9, 10), 7) for _ in range(m)]
    w = [[F(rng.randrange(-9, 10), 11) for _ in range(d)] for _ in range(m)]
    b = [F(rng.randrange(-5, 6), 3) for _ in range(d)]
    eta = F(1, 997)
    v, r, ga, gw, s, loss = state(a, w, b)
    an, wn = step(a, w, b, eta)
    vn, rn, _, _, sn, lossn = state(an, wn, b)
    old_b, new_b = imbalance(a, w), imbalance(an, wn)
    for i in range(m):
        for j in range(m):
            assert new_b[i][j] - old_b[i][j] == eta**2 * (dot(gw[i], gw[j]) - ga[i] * ga[j])
    q = dot(a, a)
    z = [x + q * y for x, y in zip(transpose_times(w, ga), r)]
    c = dot(v, r)
    assert rn == [x - eta * y + eta**2 * c * x for x, y in zip(r, z)]
    g2 = dot(ga, ga) + sum(dot(row, row) for row in gw)
    assert g2 == dot(r, z)
    assert sn - s == -4 * eta * dot(v, r) + eta**2 * g2
    expansion = (-eta * dot(r, z) + eta**2 * (c * dot(r, r) + dot(z, z) / 2)
                 - eta**3 * c * dot(r, z) + eta**4 * c**2 * dot(r, r) / 2)
    assert lossn - loss == expansion
    h = hessian(a, w, b)
    u = [F(rng.randrange(-5, 6), 5) for _ in range(m)]
    perturb_w = [[F(rng.randrange(-5, 6), 5) for _ in range(d)] for _ in range(m)]
    perturb = flatten(u, perturb_w)
    direct = sum(perturb[i] * dot(h[i], perturb) for i in range(len(perturb)))
    jh = [x + y for x, y in zip(transpose_times(w, u), transpose_times(perturb_w, a))]
    assert direct == dot(jh, jh) + 2 * sum(u[i] * dot(perturb_w[i], r) for i in range(m))
    assert abs(direct) <= (s + sum(abs(x) for x in r)) * dot(perturb, perturb)
    exact_count += 1

constants = {
    "norm_bootstrap": str(F(5) + F(3, 128)),
    "segment_squared_norm": str(6 * F(65, 64)**2),
    "segment_hessian_bound": str(F(25, 2)),
    "eta_times_segment_bound": str(F(13, 32)),
    "iterate_hessian_bound": str(F(19, 2)),
    "eta_times_sharpness_bound": str(F(10, 32)),
    "gaussian_cutoff": str(F(1, 32) - F(2, 128)),
    "tail_exponent": str(F(1, 64) * F(1, 4)),
}
assert F(5) + F(3, 128) < 6
assert 6 * F(65, 64)**2 < 8
assert F(25, 2) < 13
assert F(13, 32) < 1
assert F(19, 2) < 10
assert F(10, 32) == F(5, 16)
assert F(1, 32) - F(2, 128) == F(1, 64)

# Differentiate the explicit gradient numerically, independently of the
# quadratic-form identity used above.
a = [0.7, -0.4, 1.1]
w = [[0.2, -0.8], [1.3, 0.6], [-0.9, 0.1]]
b = [1.0, -0.3]
theta = flatten(a, w)
h = hessian(a, w, b)
delta = 1e-5
fd_error = 0.0
for j in range(len(theta)):
    plus, minus = theta[:], theta[:]
    plus[j] += delta
    minus[j] -= delta
    gp = gradient_flat(plus, 3, 2, b)
    gm = gradient_flat(minus, 3, 2, b)
    for i in range(len(theta)):
        fd_error = max(fd_error, abs((gp[i] - gm[i]) / (2 * delta) - h[i][j]))
assert fd_error < 1e-8

records = []
for case in range(32):
    m, d = (16, 8) if case < 16 else (3, 2)
    scale = (0.01, 0.2, 1.0, 3.0)[case % 4]
    a = [rng.gauss(0, scale) for _ in range(m)]
    w = [[rng.gauss(0, scale) for _ in range(d)] for _ in range(m)]
    b = [0.0] * d if case % 5 == 0 else [rng.gauss(0, 1) for _ in range(d)]
    beta = math.sqrt(dot(b, b))
    s0 = state(a, w, b)[4]
    radius = s0 + 2 * beta
    eta = 1 / (32 * radius)
    max_ratio = s0 / radius
    min_descent = math.inf
    for iteration in range(500):
        v, r, ga, gw, s, loss = state(a, w, b)
        an, wn = step(a, w, b, eta)
        lossn = state(an, wn, b)[5]
        g2 = dot(ga, ga) + sum(dot(row, row) for row in gw)
        assert s <= 6 * radius * (1 + 1e-12)
        assert s + math.sqrt(dot(r, r)) <= 10 * radius
        assert lossn <= loss - eta * g2 / 2 + 1e-12 * (1 + loss)
        if eta * g2 > 1e-12 * (1 + loss):
            min_descent = min(min_descent, (loss - lossn) / (eta * g2))
        max_ratio = max(max_ratio, s / radius)
        a, w = an, wn
    records.append({"case": case, "m": m, "d": d, "scale": scale,
                    "zero_target": beta == 0, "S0": s0, "R": radius,
                    "eta": eta, "max_S_over_R": max_ratio,
                    "min_normalized_descent": min_descent,
                    "final_loss": state(a, w, b)[5]})

# Degenerate R=0 and stationary zero initialization with a nonzero target.
for b in ([0.0, 0.0], [1.0, 0.0]):
    a, w = [0.0] * 3, [[0.0, 0.0] for _ in range(3)]
    assert step(a, w, b, 0.001) == (a, w)

# A family of exact global minima has arbitrarily large sharpness. Check an
# eigenpair of the full parameter Hessian against the output-space formula.
c = F(3)
b = [F(2), F(-1)]
a = [c, F(0), F(0)]
w = [[x / c for x in b], [F(0), F(0)], [F(0), F(0)]]
v, r, *_ = state(a, w, b)
assert r == [0, 0]
top_eigenvalue = c**2 + dot(b, b) / c**2
eigenvector = flatten([dot(row, b) for row in w], [[x * y for y in b] for x in a])
h = hessian(a, w, b)
assert [dot(row, eigenvector) for row in h] == [top_eigenvalue * x for x in eigenvector]

usage = resource.getrusage(resource.RUSAGE_SELF)
peak_rss_bytes = usage.ru_maxrss if sys.platform == "darwin" else usage.ru_maxrss * 1024
assert peak_rss_bytes < 1024**3
summary = {
    "effective_nice": priority,
    "requested_data_limit_bytes": memory_cap,
    "cpu_limit_seconds": cpu_cap,
    "limit_notes": limit_notes,
    "peak_rss_bytes": peak_rss_bytes,
    "seed": 22620261114,
    "exact_fraction_cases": exact_count,
    "finite_difference_hessian_max_error": fd_error,
    "trajectory_cases": len(records),
    "steps_per_trajectory": 500,
    "max_S_over_R": max(row["max_S_over_R"] for row in records),
    "minimum_normalized_descent": min(row["min_normalized_descent"] for row in records),
    "rational_constants": constants,
    "exact_minimum_eigenvalue_example": str(top_eigenvalue),
    "status": "PASS",
}
result = {"summary": summary, "trajectories": records}
Path(__file__).with_name("verification.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(summary, indent=2))

#!/usr/bin/env python3
"""Exact finite-state audits of PROOF.md; Python standard library only.

Run: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
     nice -n 15 python3 check_bounds.py
All output files are written next to this script. No distribution is truncated.
"""
import csv
import itertools
import json
import os
import random
import resource
import signal
from fractions import Fraction as F
from pathlib import Path


# Less than the author's 1 GB and 20 minute limits, even in a bad invocation.
# Darwin's sandbox rejects RLIMIT_AS / RLIMIT_DATA changes. The data sizes here
# are fixed and small; check actual resident usage on every convolution instead.
resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
signal.alarm(240)
ROOT = Path(__file__).resolve().parent


def convolve(a, b):
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 768 * 1024**2
    assert len(a) + len(b) < 2000
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c[i + j] += x * y
    return c


def step(p, m):
    c = [F(1)]
    for _ in range(m):
        c = convolve(c, p)
    return [c[0] + c[1]] + c[2:]


def enumerate_step(p, m):
    out = [F(0)] * (m * (len(p) - 1))
    for inputs in itertools.product(range(len(p)), repeat=m):
        w = F(1)
        for i in inputs:
            w *= p[i]
        out[max(sum(inputs) - 1, 0)] += w
    return out


def at(v, i):
    return v[i] if 0 <= i < len(v) else F(0)


def l1(v):
    return sum(map(abs, v), F(0))


def add_shift(out, v, shift=0, scale=F(1)):
    for k, x in enumerate(v):
        out[k + shift] += scale * x


def q(p):
    return 1 - p[0]


def tv(p, m):
    """Exact distance including the entire infinite geometric tail."""
    z = q(p)
    top = len(p) - 1
    assert z > 0
    return (sum((abs(p[k] / z - F(m - 1, m**k))
                 for k in range(1, top + 1)), F(0))
            + F(1, m**top)) / 2


cases = [
    ("m2_critical_02", 2, [F(4, 5), F(0), F(1, 5)], 7, True),
    ("m3_critical_01", 3, [F(3, 4), F(1, 4)], 4, True),
    ("m3_critical_02", 3, [F(27, 28), F(0), F(1, 28)], 4, True),
    ("m4_critical_01", 4, [F(8, 9), F(1, 9)], 3, True),
    ("m2_exception", 2, [F(0), F(1)], 5, True),
    ("m2_noncritical", 2, [F(2, 5), F(1, 5), F(2, 5)], 5, False),
    ("m2_bernoulli", 2, [F(1, 2), F(1, 2)], 5, False),
    ("m3_zero", 3, [F(1), F(0)], 3, False),
]
rng = random.Random(177)
for i in range(16):
    m = 2 + i % 4
    w = [rng.randrange(1, 8) for _ in range(4)]
    cases.append((f"random_{i:02d}_m{m}", m,
                  [F(x, sum(w)) for x in w], 2, False))

rows = []
counts = dict(models=len(cases), exact_one_step=0, independent_enumerations=0,
              critical_moment_checks=0, finite_window_identities=0,
              finite_window_bounds=0, simplified_bounds=0,
              collision_bounds=0, first_correction_constants=0)
model_data = []
for name, m, initial, depth, critical in cases:
    laws = [initial]
    for _ in range(depth):
        laws.append(step(laws[-1], m))
    for p in laws:
        assert sum(p) == 1 and min(p) >= 0
        if critical:
            tilted_mass = sum((x * m**k for k, x in enumerate(p)), F(0))
            tilted_first = sum((k * x * m**k for k, x in enumerate(p)), F(0))
            assert (m - 1) * tilted_first == tilted_mass
            counts["critical_moment_checks"] += 1
    errors = []
    for n, (p, pn) in enumerate(zip(laws, laws[1:])):
        if len(p)**m <= 5000:
            assert pn == enumerate_step(p, m)
            counts["independent_enumerations"] += 1
        z = q(p)
        size = max(len(p), len(pn) + 1)
        r = [F(0)] * size
        b = [F(0)] * size
        e = [F(0)] * size
        for k in range(1, size):
            r[k] = at(pn, k) - m * p[0]**(m - 1) * at(p, k + 1)
            b[k] = m * (1 - p[0]**(m - 1)) * at(p, k + 1)
            e[k] = at(pn, k) - m * at(p, k + 1)
            assert e[k] == r[k] - b[k]
        assert min(r) >= 0 and min(b) >= 0
        R = 1 - (1 - z)**m - m * z * (1 - z)**(m - 1)
        B = m * (1 - (1 - z)**(m - 1)) * (z - at(p, 1))
        assert sum(r) == R and sum(b) == B
        assert R <= F(m * (m - 1), 2) * z**2
        assert B <= m * (m - 1) * z**2
        d_event = [F(0)] * (size + 1)
        d_event[1] = sum(e) / m
        add_shift(d_event, e, shift=1, scale=F(-1, m))
        d_direct = [F(0)] * (size + 1)
        add_shift(d_direct, p)
        d_direct[0] = 0
        d_direct[1] -= z - q(pn) / m
        pp = pn.copy()
        pp[0] = 0
        add_shift(d_direct, pp, shift=1, scale=F(-1, m))
        assert d_event == d_direct
        assert sum(d_direct) == 0
        assert l1(d_direct) / 2 <= (m - 1) * z**2
        errors.append(d_direct)
        counts["exact_one_step"] += 1
        counts["collision_bounds"] += 1

    for n in range(depth):
        z = q(laws[n])
        if z == 0:
            continue
        actual = tv(laws[n], m)
        for L in range(1, depth - n + 1):
            size = max(len(laws[n + j]) + j for j in range(L + 1))
            size = max(size, max(len(errors[n + j]) + j for j in range(L)))
            reconstructed = [F(0)] * size
            for j in range(L):
                reconstructed[j + 1] += F(1, m**j) * (
                    q(laws[n + j]) - q(laws[n + j + 1]) / m)
                add_shift(reconstructed, errors[n + j], j, F(1, m**j))
            boundary = laws[n + L].copy()
            boundary[0] = 0
            add_shift(reconstructed, boundary, L, F(1, m**L))
            expected = [F(0)] * size
            add_shift(expected, laws[n])
            expected[0] = 0
            assert reconstructed == expected
            counts["finite_window_identities"] += 1
            variation = sum((F(1, m**j) * abs(q(laws[n + j]) - z)
                             for j in range(1, L)), F(0))
            boundary_bound = F(1, m**L) * max(q(laws[n + L]), z)
            collision = (m - 1) * sum((F(1, m**j) * q(laws[n + j])**2
                                       for j in range(L)), F(0))
            bound = (variation + boundary_bound + collision) / z
            assert actual <= bound
            counts["finite_window_bounds"] += 1
            delta = max(abs(q(laws[n + j]) / z - 1) for j in range(L + 1))
            simple = delta / (m - 1) + (1 + delta) / m**L + m * (1 + delta)**2 * z
            assert bound <= simple
            counts["simplified_bounds"] += 1
            rows.append(dict(model=name, m=m, n=n, L=L, q_exact=str(z),
                             tv_exact=str(actual), bound_exact=str(bound),
                             tv_decimal=f"{float(actual):.12g}",
                             bound_decimal=f"{float(bound):.12g}"))
    model_data.append(dict(name=name, m=m, initial=[str(x) for x in initial],
                           depth=depth, critical=critical,
                           last_support_max=len(laws[-1]) - 1))

# Independent geometric-series audit of h_beta's mass and TV constant.
# Two geometric sums give the total signed mass, while signs give positive mass.
for m in range(2, 13):
    for beta in [F(1), F(2), F(7, 3)]:
        r = F(1, m)
        total_mass = beta * (m * r / (1 - r) - (m - 1) * r / (1 - r)**2)
        assert total_mass == 0
        h = [beta * F(m - (m - 1) * k, m**k) for k in range(1, 101)]
        assert h[0] == beta / m and max(h[1:]) <= 0
        # Independent derivation from the linearized one-step recursion:
        # h(k) - m h(k+1) = beta g(k).
        for k in range(1, 100):
            assert h[k - 1] - m * h[k] == beta * F(m - 1, m**k)
        # The remaining tail is nonpositive and equals -sum(h).
        tail = -sum(h)
        assert tail <= 0
        exact_norm = l1(h) - tail
        assert exact_norm == 2 * beta / m
        counts["first_correction_constants"] += 1

with (ROOT / "exact_checks.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
summary = dict(status="PASS", arithmetic="exact fractions; no truncation",
               counts=counts, models=model_data,
               max_support=max(x["last_support_max"] for x in model_data),
               deterministic_exception_tv="1/2",
               actual_nice=os.getpriority(os.PRIO_PROCESS, 0),
               peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
assert tv([F(0), F(1)], 2) == F(1, 2)
(ROOT / "audit_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print("PASS: exact rational audits; no distribution truncation")
for key, value in counts.items():
    print(f"{key}: {value}")
print(f"max_support: {summary['max_support']}")
print("deterministic_exception_tv: 1/2")
print(f"actual_nice: {summary['actual_nice']}")
print(f"peak_rss_bytes: {summary['peak_rss_bytes']}")
print("data: exact_checks.csv, audit_summary.json")

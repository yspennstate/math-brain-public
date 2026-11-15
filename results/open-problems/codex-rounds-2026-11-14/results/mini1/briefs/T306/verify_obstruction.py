#!/usr/bin/env python3
"""Small deterministic checks of PROOF.md; standard library only."""
import csv
import json
import math
import os
import resource
import time
from pathlib import Path

GUARDS = {}
for name, value in (("RLIMIT_AS", 512 * 1024**2), ("RLIMIT_CPU", 60)):
    try:
        resource.setrlimit(getattr(resource, name), (value, value))
        GUARDS[name] = value
    except (OSError, ValueError) as exc:
        GUARDS[name] = str(exc)
# All grids are streamed through fsum; no grid-sized array is allocated.
# Actual peak RSS is reported and checked on this macOS host.
assert os.environ.get("OMP_NUM_THREADS") == "1"
START = time.monotonic()
ROOT = Path(__file__).resolve().parent
PI = math.pi


def midpoint_mean(fun, n):
    return math.fsum(fun(2 * PI * (j + 0.5) / n) for j in range(n)) / n


def phi(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * PI)


def phase_map(theta, c):
    # theta in [0,2*pi]. atan2 chooses the continuous increasing branch.
    return 2 * math.atan2(math.exp(c) * math.sin(theta / 2), math.cos(theta / 2))


def phase_jac(theta, c):
    return 1 / (math.cosh(c) - math.sinh(c) * math.cos(theta))


def gaussian_tv(k, c, resolution):
    # Integrate in source coordinates: 1/2 int |phi(x)-phi(F(x))*F'(x)| dx.
    # The number of points scales with k, resolving every period uniformly.
    radius = 9.0
    n = max(8192, math.ceil(2 * radius * k * resolution / (2 * PI)))
    dx = 2 * radius / n

    def summand(j):
        x = -radius + (j + 0.5) * dx
        phase = (k * x) % (2 * PI)
        y = x + (phase_map(phase, c) - phase) / k
        return abs(phi(x) - phi(y) * phase_jac(phase, c))

    return 0.5 * dx * math.fsum(summand(j) for j in range(n)), n


def rk4(theta, c, steps):
    # Integrate both the phase and its variational equation independently
    # of the half-angle closed form.
    h = 1 / steps
    jac = 1.0

    def rhs(t, j):
        return c * math.sin(t), c * math.cos(t) * j

    for _ in range(steps):
        a, aj = rhs(theta, jac)
        b, bj = rhs(theta + h * a / 2, jac + h * aj / 2)
        d, dj = rhs(theta + h * b / 2, jac + h * bj / 2)
        e, ej = rhs(theta + h * d, jac + h * dj)
        theta += h * (a + 2 * b + 2 * d + e) / 6
        jac += h * (aj + 2 * bj + 2 * dj + ej) / 6
    return theta, jac


phase_rows = []
for c in (0.1, 0.5, 0.9):
    exact_a = 4 / PI * math.atan(math.exp(c / 2)) - 1
    exact_b = 2 / PI * math.asin(math.tanh(c / 2))
    target_quad = 0.5 * midpoint_mean(
        lambda t: abs(1 / (math.cosh(c) + math.sinh(c) * math.cos(t)) - 1),
        131072,
    )
    source_quad = 0.5 * midpoint_mean(lambda t: abs(1 - phase_jac(t, c)), 131072)
    cos_witness = midpoint_mean(lambda t: math.cos(phase_map(t, c)), 131072)
    assert abs(exact_a - exact_b) < 1e-14
    assert abs(exact_a - target_quad) < 1e-9
    assert abs(exact_a - source_quad) < 1e-9
    assert abs(cos_witness + math.tanh(c / 2)) < 1e-12
    max_flow_err = max_jac_err = 0.0
    for j in range(128):
        theta = 2 * PI * (j + 0.5) / 128
        val, jac = rk4(theta, c, 128)
        max_flow_err = max(max_flow_err, abs(val - phase_map(theta, c)))
        max_jac_err = max(max_jac_err, abs(jac - phase_jac(theta, c)))
    assert max_flow_err < 1e-9 and max_jac_err < 1e-9
    phase_rows.append(dict(c=c, D_arctan=exact_a, D_arcsin=exact_b,
                           target_quadrature=target_quad, source_quadrature=source_quad,
                           cos_witness=cos_witness, rk4_flow_error=max_flow_err,
                           rk4_jacobian_error=max_jac_err))

gaussian_rows = []
c = 0.5
limit = 2 / PI * math.asin(math.tanh(c / 2))
for k in (1, 2, 4, 8, 16, 32, 64, 128, 1000):
    coarse, nc = gaussian_tv(k, c, 256)
    fine, nf = gaussian_tv(k, c, 512)
    bound = math.sqrt(2 * PI) / k
    score_rms = c / k * math.sqrt((1 - math.exp(-2 * k * k)) / 2)
    assert abs(fine - limit) <= bound + 1e-5
    assert abs(fine - coarse) < 5e-6, (k, coarse, fine, abs(fine - coarse))
    gaussian_rows.append(dict(k=k, c=c, score_rms=score_rms,
                              tv_coarse=coarse, tv_fine=fine,
                              grid_difference=abs(fine - coarse), D_limit=limit,
                              theorem_error_bound=bound, fine_grid_points=nf))

euler_rows = []
for c in (0.1, 0.5, 0.9):
    bound = c * (1 - c / 2) * math.exp(-c) / 4
    for steps in (1, 2, 4, 16, 64, 256):
        phase_count = 4096
        a = c / steps
        tv_terms, cos_terms = [], []
        max_jac = 0.0
        for j in range(phase_count):
            theta = 2 * PI * (j + 0.5) / phase_count
            jac = 1.0
            for _ in range(steps):
                jac *= 1 + a * math.cos(theta)
                theta += a * math.sin(theta)
            tv_terms.append(abs(1 - jac))
            cos_terms.append(math.cos(theta))
            max_jac = max(max_jac, jac)
        phase_tv = math.fsum(tv_terms) / (2 * phase_count)
        cos_mean = math.fsum(cos_terms) / phase_count
        assert phase_tv >= bound - 1e-7
        assert -cos_mean / 2 >= bound - 1e-7
        assert max_jac <= math.exp(c) + 1e-12
        if steps == 1:
            assert abs(phase_tv - c / PI) < 1e-7
        euler_rows.append(dict(c=c, steps=steps, phase_tv=phase_tv,
                              half_cosine_difference=-cos_mean / 2,
                              uniform_lower_bound=bound, max_jacobian=max_jac))

score_rows = []
for k in (1, 4, 1000):
    c = 0.5
    n = max(8192, math.ceil(18 * k * 64 / (2 * PI)))
    dx = 18 / n
    numerical = math.sqrt(dx * math.fsum(
        (c / k * math.sin(k * (-9 + (j + 0.5) * dx)))**2 * phi(-9 + (j + 0.5) * dx)
        for j in range(n)))
    exact = c / k * math.sqrt((1 - math.exp(-2 * k * k)) / 2)
    assert abs(numerical - exact) < 1e-12
    score_rows.append(dict(k=k, numerical_rms=numerical, analytic_rms=exact,
                           absolute_difference=abs(numerical - exact)))

for filename, rows in (("phase_checks.csv", phase_rows), ("gaussian_checks.csv", gaussian_rows),
                       ("euler_checks.csv", euler_rows), ("score_checks.csv", score_rows)):
    with (ROOT / filename).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

try:
    priority = os.getpriority(os.PRIO_PROCESS, 0)
except OSError as exc:
    priority = str(exc)
peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert peak_rss < 512 * 1024**2
meta = dict(seconds=time.monotonic() - START, peak_rss_raw=peak_rss,
            rss_units="bytes on macOS", nice_priority=priority, OMP_NUM_THREADS=os.environ["OMP_NUM_THREADS"],
            requested_resource_guards=GUARDS,
            gaussian_tail_bound=0.5 * (math.erfc(9 / math.sqrt(2)) + math.erfc(8.5 / math.sqrt(2))),
            note="Quadrature is a numerical check, not a certified integration bound; PROOF.md is analytic.")
(ROOT / "verification_metadata.json").write_text(json.dumps(meta, indent=2) + "\n")
print("All deterministic checks passed.")
print(f"D(1/2) = {limit:.15f}")
print(f"k=1000: RMS score error = {gaussian_rows[-1]['score_rms']:.15g}")
print(f"k=1000: numerical TV = {gaussian_rows[-1]['tv_fine']:.15f}")
print(f"k=1000: analytic TV lower bound = {limit-math.sqrt(2*PI)/1000:.15f}")
print(f"maximum RK4 phase error = {max(r['rk4_flow_error'] for r in phase_rows):.3g}")
print(f"maximum RK4 Jacobian error = {max(r['rk4_jacobian_error'] for r in phase_rows):.3g}")
print(f"Euler uniform bound at c=1/2, k=1000 = {3*math.exp(-0.5)/32-math.sqrt(2*PI)/1000:.15f}")
print("Euler checks passed for c=0.1,0.5,0.9 and N=1,2,4,16,64,256.")
print("Independent Gaussian score-error quadrature passed for k=1,4,1000.")
print(json.dumps(meta, sort_keys=True))

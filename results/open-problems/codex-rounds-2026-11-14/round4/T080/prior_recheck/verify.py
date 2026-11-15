#!/usr/bin/env python3
"""Independent audits of the earlier density formula and the vacant-seam lemma.

Run with OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py.
Standard library only. Numerical agreement is not a proof certificate.
"""

import csv
from fractions import Fraction as F
import itertools
import json
import math
import os
from pathlib import Path
import resource
import sys
import time


START = time.monotonic()
ROOT = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
# This managed Mac rejects AS/DATA limit changes. The workload has fixed small
# lists (fewer than 1200 entries); record peak RSS and reject it above 768 MiB.
PRIORITY = os.getpriority(os.PRIO_PROCESS, 0)
assert PRIORITY >= 15, PRIORITY
for variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    assert os.environ.get(variable) == "1", (variable, os.environ.get(variable))


def gauss_nodes(n=24):
    """Legendre nodes and weights, obtained from recurrence and Newton iteration."""
    nodes = []
    for j in range(1, n + 1):
        x = math.cos(math.pi * (j - 0.25) / (n + 0.5))
        for _ in range(30):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            derivative = n * (x * p1 - p0) / (x * x - 1)
            step = p1 / derivative
            x -= step
            if abs(step) < 2e-16:
                break
        else:
            raise ArithmeticError("Legendre root did not converge")
        # Re-evaluate derivative at the updated root.
        p0, p1 = 1.0, x
        for k in range(2, n + 1):
            p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
        derivative = n * (x * p1 - p0) / (x * x - 1)
        nodes.append((x, 2 / ((1 - x * x) * derivative * derivative)))
    return nodes


NODES = gauss_nodes()
for k in range(41):
    found = math.fsum(weight * x**k for x, weight in NODES)
    exact = 0.0 if k % 2 else 2 / (k + 1)
    assert abs(found - exact) < 4e-14, (k, found, exact)


def integrate(function, low, high):
    panels = max(1, math.ceil((high - low) * 4))
    contributions = []
    for j in range(panels):
        left = low + (high - low) * j / panels
        right = low + (high - low) * (j + 1) / panels
        middle, scale = (left + right) / 2, (right - left) / 2
        contributions.append(scale * math.fsum(
            weight * function(middle + scale * x) for x, weight in NODES))
    return math.fsum(contributions)


def vball(d):
    return math.pi ** (d / 2) / math.gamma(1 + d / 2)


def grid_count(length, radius):
    h = 1 + 2 * radius
    return max(0, 1 + math.floor((length - 2 * (1 + radius)) / h))


def log_exp_sum(t, cap):
    terms = [n * math.log(t) - math.lgamma(n + 1) for n in range(cap + 1)]
    largest = max(terms)
    return largest + math.log(math.fsum(math.exp(x - largest) for x in terms))


def tilt_bound(t, cap):
    return t if t <= cap else cap * (1 + math.log(t / cap))


def main():
    print("Standard-library independent audit; floating-point checks support the proof.")
    print(f"nice_priority={PRIORITY}; thread_environment=1; memory_check=peak RSS <768 MiB; cpu_limit_seconds=60")
    print("Earlier density formula: original integral vs conditional second-arrival integral")
    density_rows = []
    for d in (2, 3, 4, 8):
        for t in (0.0, 1e-4, 0.01, 0.1, 0.5, 1.0):
            original = integrate(lambda u: d * u**(d - 1) * math.exp(-(u + t)**d), 0, 8)
            second = integrate(lambda s: d * (s - t)**d * s**(d - 1) * math.exp(-s**d), t, 8)
            error = abs(original - second)
            assert error < 2e-13, (d, t, original, second)
            if d == 2:
                erfc = math.exp(-t*t) - math.sqrt(math.pi) * t * math.erfc(t)
                assert abs(original - erfc) < 2e-13, (t, original, erfc)
            constant = (d - 1) * math.gamma(1 - 1/d)
            assert original >= 1 - constant * t - 2e-13
            density_rows.append(dict(d=d, t=t, original=original,
                                     second_arrival=second, absolute_error=error))
    max_density_error = max(row["absolute_error"] for row in density_rows)
    print(f"density_pairs={len(density_rows)}; maximum_absolute_error={max_density_error:.3g}")
    for d in (2, 3, 4, 8):
        from_shift = d * (d - 1) * integrate(lambda s: s**(d - 2) * math.exp(-s**d), 0, 8)
        from_original = d*d * integrate(lambda u: u**(2*d - 2) * math.exp(-u**d), 0, 8)
        gamma = d * math.gamma(2 - 1/d)
        assert abs(from_shift - gamma) < 2e-12
        assert abs(from_original - gamma) < 2e-12
        print(f"d={d}: loss_constant={gamma:.12g}; two_integral_errors={abs(from_shift-gamma):.3g},{abs(from_original-gamma):.3g}")

    # Exact rational threshold and geometry checks, without floating-point floors.
    threshold_checks = 0
    for a in (F(1, 10), F(1, 4), F(2, 5)):
        h, margin = 1 + 2*a, 1 + a
        lengths = [F(1, 10), F(1), 2 * margin]
        lengths += [2*margin + j*h + delta for j in range(8)
                    for delta in (F(-1, 100), F(0), F(1, 100))]
        for length in lengths:
            predicted = grid_count(length, a)
            # Independent count by scanning potential grid coordinates.
            direct = sum(margin + j*h <= length - margin for j in range(100))
            assert predicted == direct, (a, length, predicted, direct)
            threshold_checks += 1
        for d in (2, 3):
            lengths_d = [2*margin + (i + 1)*h for i in range(d)]
            axes = [[margin + j*h for j in range(grid_count(length, a))]
                    for length in lengths_d]
            centers = list(itertools.product(*axes))
            for center in centers:
                assert all(margin <= x <= length - margin for x, length in zip(center, lengths_d))
            for p, q in itertools.combinations(centers, 2):
                assert sum((x-y)**2 for x, y in zip(p, q)) >= h*h
    print(f"exact_grid_threshold_checks={threshold_checks}; rational_margin_and_pair_distance_checks=PASS")

    # A weighted discrete analogue of the continuum label assignment integral.
    volumes = (F(1, 7), F(2, 9), F(3, 11), F(1, 13))
    for activity in (F(1, 2), F(1), F(3)):
        labeled_sum = F(0)
        wrong_without_factorial = F(0)
        for n in range(len(volumes) + 1):
            sector = sum((math.prod(volumes[j] for j in assignment)
                          for assignment in itertools.permutations(range(len(volumes)), n)), F(0))
            labeled_sum += activity**n * sector / math.factorial(n)
            wrong_without_factorial += activity**n * sector
        product = math.prod(1 + activity*b for b in volumes)
        assert labeled_sum == product
        assert wrong_without_factorial > product  # The negative control must fail.
    print("exact_n_factorial_cancellation=PASS; missing_factorial_negative_control=detected")

    # Check upper tilt against a separately evaluated finite partition polynomial.
    tilt_cases = 0
    for cap in (1, 2, 5, 20, 100, 1000):
        for ratio in (1e-5, 0.01, 0.5, 1.0, 1.01, 2, 100, 1e8):
            t = cap * ratio
            exact_log = log_exp_sum(t, cap)
            upper = tilt_bound(t, cap)
            assert exact_log <= upper + 2e-10, (cap, t, exact_log, upper)
            # Independent coefficient-wise upper bound via the chosen r.
            r = min(1.0, cap / t)
            assert abs(upper - (r*t - cap*math.log(r))) < 2e-10
            tilt_cases += 1
    print(f"truncated_exponential_and_tilt_cases={tilt_cases}; all_bounds=PASS")

    print("Seam example: a=1/4, W=4, L=10; lower <= exact truncated-sum upper <= tilt upper")
    seam_rows = []
    for d in (2, 3):
        a, width, length = F(1, 4), F(4), F(10)
        m = grid_count(length, a)**(d-1) * grid_count(width, a)
        area, volume = float(length**(d-1)), float(width * length**(d-1))
        cap = math.floor(float((length + 1)**(d-1) * (width + 1)) / (vball(d)/2**d))
        b = vball(d) * float(a)**d
        for z in (1.0, 100.0, 1e6):
            lower = m * math.log1p(z*b)
            upper_poly = log_exp_sum(z * volume, cap)
            upper_tilt = tilt_bound(z * volume, cap)
            assert lower <= upper_poly <= upper_tilt + 2e-9
            row = dict(d=d, a=float(a), W=float(width), L=float(length), z=z,
                       insertion_count=m, packing_cap=cap,
                       lower_cost=lower, polynomial_upper_cost=upper_poly,
                       tilt_upper_cost=upper_tilt, area=area)
            seam_rows.append(row)
            print(f"d={d}, z={z:g}, m={m}, M={cap}: {lower:.9g} <= {upper_poly:.9g} <= {upper_tilt:.9g}")

    # Independent finite-L enumeration of the surface coefficients.
    surface_errors = []
    for d in (2, 3):
        a, width = F(1, 4), F(4)
        h = 1 + 2*a
        alpha = float(grid_count(width, a) / h**(d-1))
        kappa = float(width + 1) / (vball(d) / 2**d)
        length = F(10000)
        area = float(length**(d-1))
        m = grid_count(length, a)**(d-1) * grid_count(width, a)
        cap = math.floor(float((length + 1)**(d-1) * (width + 1)) / (vball(d)/2**d))
        assert abs(m / area - alpha) < 0.001
        assert abs(cap / area - kappa) < 0.003
        surface_errors.append(dict(d=d, alpha=alpha, observed_m_per_area=m/area,
                                   kappa=kappa, observed_M_per_area=cap/area))
        print(f"surface d={d}: alpha={alpha:.12g}, m/A={m/area:.12g}; kappa={kappa:.12g}, M/A={cap/area:.12g}")

    # Exact thin-strip obstruction and a check on the direction of its threshold.
    narrow = F(4, 5)
    bound_squared = F(1, 4) + narrow*narrow
    assert bound_squared == F(89, 100) < 1
    witness_y = F(89, 100)
    assert witness_y < F(9, 10)
    assert F(1, 4) + witness_y*witness_y > 1
    print("thin_strip W=4/5: maximum_distance_squared_bound=89/100<1, so Z=1")
    print("wider_strip W=9/10: (x,y)=(1/2,89/100) is allowed by that exterior row")

    with (ROOT / "density_audit.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(density_rows[0]))
        writer.writeheader()
        writer.writerows(density_rows)
    with (ROOT / "seam_bounds.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(seam_rows[0]))
        writer.writeheader()
        writer.writerows(seam_rows)
    elapsed = time.monotonic() - START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_mib = rss / (1024**2 if sys.platform == "darwin" else 1024)
    assert peak_mib < 768
    result = dict(status="PASS", nice_priority=PRIORITY, density_pairs=len(density_rows),
                  max_density_error=max_density_error, exact_grid_checks=threshold_checks,
                  tilt_cases=tilt_cases, seam_examples=seam_rows,
                  surface_checks=surface_errors, elapsed_seconds=elapsed, peak_rss_mib=peak_mib)
    (ROOT / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS; elapsed_seconds={elapsed:.3f}; peak_rss_mib={peak_mib:.3f}")
    print("Wrote density_audit.csv, seam_bounds.csv, verification.json")


if __name__ == "__main__":
    main()

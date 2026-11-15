#!/usr/bin/env python3
"""Exact rational audits of PROOF.md; standard library only, one process."""

import itertools
import json
import os
from pathlib import Path
from fractions import Fraction as Q
import resource
import time

STARTED = time.monotonic()


def resource_guard():
    # Darwin's sandbox rejects setrlimit here. Check actual RSS and elapsed
    # time between these fixed, tiny cases; no large arrays are allocated.
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss >= 256 * 1024**2:
        raise RuntimeError("RSS guard reached 256 MiB")
    if time.monotonic() - STARTED > 120:
        raise RuntimeError("Wall time guard reached 120 seconds")


def preflight():
    if os.environ.get("OMP_NUM_THREADS") != "1":
        raise RuntimeError("Set OMP_NUM_THREADS=1")
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    if priority < 15:
        raise RuntimeError(f"Expected nice >= 15, got {priority}")
    resource_guard()
    return priority


def gaps(points, width):
    return [b - a for a, b in zip(points, points[1:])] + [
        width - points[-1] + points[0]
    ]


def cdf(gs, s):
    return Q(sum(g <= s for g in gs), len(gs))


def void_hinges(gs, width, s):
    return sum((max(g - s, Q(0)) for g in gs), Q(0)) / width


def geometric_void(points, width, s, cyclic):
    """Integrate the indicator using event breakpoints, without gap lengths."""
    if s == 0:
        return Q(1)
    if cyclic and s >= width:
        return Q(0)
    end = width if cyclic else width - s
    if end <= 0:
        raise ValueError("nonwrapping start interval must have positive length")
    breaks = {Q(0), end}
    for p in points:
        for event in (p, p - s):
            event = event % width if cyclic else event
            if 0 < event < end:
                breaks.add(event)
    total = Q(0)
    for left, right in itertools.pairwise(sorted(breaks)):
        mid = (left + right) / 2
        occupied = any(
            0 < ((p - mid) % width) <= s if cyclic else mid < p <= mid + s
            for p in points
        )
        if not occupied:
            total += right - left
    return total / end


def integrated_void(gs, width, s):
    """Equation (9), integrating the step CDF from its exact breakpoints."""
    cuts = sorted({Q(0), s} | {g for g in gs if 0 < g < s})
    survival_integral = sum(
        ((b - a) * (1 - cdf(gs, (a + b) / 2))
         for a, b in itertools.pairwise(cuts)), Q(0)
    )
    return 1 - Q(len(gs), 1) / width * survival_integral


def target_cdf(s):
    return max(Q(0), min(Q(1), s / 2))


def target_void(s):
    if s <= 0:
        return 1 - s
    if s >= 2:
        return Q(0)
    return (2 - s) ** 2 / 4


def exact_empty_error(gs, width, right):
    """Find all extrema: piecewise linear V minus quadratic E on [0,2]."""
    cuts = sorted({Q(0), Q(right), Q(2)} |
                  {g for g in gs if 0 <= g <= right})
    cuts = [x for x in cuts if 0 <= x <= right]
    candidates = set(cuts)
    # On a hinge-free cell below 2, D' = -#{g>s}/W + 1-s/2.
    for a, b in itertools.pairwise(cuts):
        mid = (a + b) / 2
        if mid < 2:
            root = 2 * (1 - Q(sum(g > mid for g in gs), 1) / width)
            if a <= root <= b:
                candidates.add(root)
    return max(abs(void_hinges(gs, width, s) - target_void(s))
               for s in candidates)


def exact_cdf_error(gs):
    # Check both limits at every jump; the target is linear between jumps.
    candidates = {Q(0), Q(2)} | set(gs)
    return max(
        abs(Q(sum(g < s if left else g <= s for g in gs), len(gs)) -
            target_cdf(s))
        for s in candidates for left in (False, True)
    )


def audit_small():
    counts = dict(configurations=0, void_geometry=0, integral_identity=0,
                  right_derivative=0, edge_bound=0, cyclic_gap_cdf=0,
                  theorem_bound=0, grid_certificate=0)
    max_edge_ratio = Q(0)
    max_boundary_scaled = Q(0)
    width = Q(6)
    thresholds = [Q(i, 4) for i in range(25)]
    for n in range(2, 6):
        for raw in itertools.combinations_with_replacement(range(6), n):
            resource_guard()
            points = list(map(Q, raw))
            gs = gaps(points, width)
            counts["configurations"] += 1
            assert sum(gs) == width
            for s in thresholds:
                direct = void_hinges(gs, width, s)
                assert direct == geometric_void(points, width, s, True)
                counts["void_geometry"] += 1
                assert direct == integrated_void(gs, width, s)
                counts["integral_identity"] += 1
                later = [g - s for g in gs if g > s]
                step = min([Q(1, 16)] + [d / 2 for d in later])
                slope = (void_hinges(gs, width, s + step) - direct) / step
                assert slope == Q(n, 1) / width * (cdf(gs, s) - 1)
                counts["right_derivative"] += 1
                diff = abs(cdf(gs[:-1], s) - cdf(gs, s))
                assert diff <= Q(1, n)
                max_boundary_scaled = max(max_boundary_scaled, diff * n)
                counts["cyclic_gap_cdf"] += 1
                if s < width:
                    ordinary = geometric_void(points, width, s, False)
                    assert abs(ordinary - direct) <= s / width
                    if s:
                        max_edge_ratio = max(max_edge_ratio,
                                             abs(ordinary - direct) / (s / width))
                    counts["edge_bound"] += 1
            rho = Q(n, 1) / width
            for h in (Q(1, 4), Q(1, 2), Q(1)):
                right = Q(2) + h
                delta = exact_empty_error(gs, width, right)
                bound = Q(1, n) + (2 * delta / h + h / 2 + abs(rho - 1)) / rho
                for s in (Q(i, 4) for i in range(9)):
                    assert abs(cdf(gs[:-1], s) - target_cdf(s)) <= bound
                    counts["theorem_bound"] += 1
                mesh = [Q(i, 4) for i in range(int(4 * right) + 1)]
                eps = max(abs(void_hinges(gs, width, s) - target_void(s))
                          for s in mesh)
                assert delta <= eps + Q(1, 4)
                counts["grid_certificate"] += 1
    return {"counts": counts, "max_edge_bound_ratio": str(max_edge_ratio),
            "max_cyclic_gap_bound_ratio": str(max_boundary_scaled)}


def audit_sharpness():
    rows = []
    for n in (4, 8, 16, 32, 64, 128):
        for k in sorted({1, n // 4, n // 2}):
            resource_guard()
            gs = [Q(2 * j - 1, n) for j in range(1, n + 1)]
            gs[n // 2 - k:n // 2 + k] = [Q(1)] * (2 * k)
            assert sum(gs) == n
            delta = exact_empty_error(gs, Q(n), Q(3))
            discrepancy = exact_cdf_error(gs)
            assert delta == Q(k, n) ** 2
            assert discrepancy == Q(k, n)
            # Independent midpoint-rule calculation at s=1.
            positive_odd_sum = sum(2 * j - 1 for j in range(1, k + 1))
            assert positive_odd_sum == k * k
            assert abs(void_hinges(gs, Q(n), Q(1)) - Q(1, 4)) == delta
            rows.append({"N": n, "k": k, "empty_error": str(delta),
                         "cdf_error": str(discrepancy),
                         "cdf_squared_equals_empty_error": discrepancy ** 2 == delta})
    return rows


def audit_nontrivial_bounds():
    cases = 0
    nonvacuous = 0
    below_one = 0
    above_one = 0
    # Both signs of the density error, and cases where the theorem is < 1.
    for n in (32, 64, 128):
        for k in (1, n // 4):
            base = [Q(2 * j - 1, n) for j in range(1, n + 1)]
            base[n // 2 - k:n // 2 + k] = [Q(1)] * (2 * k)
            for scale in (Q(1, 2), Q(9, 10), Q(1), Q(11, 10), Q(2)):
                resource_guard()
                gs = [scale * g for g in base]
                width = n * scale
                rho = Q(n, 1) / width
                cyclic_error = exact_cdf_error(gs)
                internal_error = exact_cdf_error(gs[:-1])
                for h in (Q(1, 16), Q(1, 8), Q(1, 4), Q(1, 2)):
                    delta = exact_empty_error(gs, width, 2 + h)
                    cyclic_bound = (2 * delta / h + h / 2 + abs(rho - 1)) / rho
                    assert cyclic_error <= cyclic_bound
                    assert internal_error <= cyclic_bound + Q(1, n)
                    cases += 1
                    nonvacuous += cyclic_bound + Q(1, n) < 1
                    below_one += rho < 1
                    above_one += rho > 1
    return {"cases": cases, "internal_bound_less_than_one": nonvacuous,
            "density_below_one_cases": below_one,
            "density_above_one_cases": above_one,
            "cdf_supremum_checked_at_all_jumps_and_both_limits": True}


def audit_missing_assumptions():
    # Density-one requirement: unit lattice with the wrong unfolding, spacing 2.
    gs = [Q(2)] * 8
    rho = Q(8, 16)
    assert rho == Q(1, 2)
    assert cdf(gs, Q(3, 2)) == 0
    # Multiplicities: seven coincident points and one cyclic gap of length 6.
    repeated = [Q(0)] * 7
    assert cdf(gaps(repeated, Q(6)), Q(0)) == Q(6, 7)
    # An internal gap sample omits exactly one cyclic gap, attaining 1/N.
    gs = [Q(0), Q(6)]
    assert abs(cdf(gs[:-1], Q(0)) - cdf(gs, Q(0))) == Q(1, 2)
    return {"wrong_density_detected": True, "zero_gaps_checked": True,
            "one_over_N_boundary_constant_attained": True,
            "large_cyclic_gap_checked": True}


def main():
    started = time.monotonic()
    priority = preflight()
    result = {"small_exact_audit": audit_small(),
              "sharpness": audit_sharpness(),
              "nontrivial_bounds": audit_nontrivial_bounds(),
              "assumption_checks": audit_missing_assumptions()}
    elapsed = time.monotonic() - started
    result["resources"] = {"nice": priority, "OMP_NUM_THREADS": "1",
                           "elapsed_seconds": round(elapsed, 3),
                           "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                           "rss_guard_bytes": 256 * 1024**2,
                           "elapsed_guard_seconds": 120,
                           "os_hard_memory_cap": False}
    Path(__file__).with_name("audit_data.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print("All exact rational checks passed.")
    print(json.dumps(result["small_exact_audit"], sort_keys=True))
    print(f"Sharpness cases: {len(result['sharpness'])}; all D^2 = delta exactly.")
    print(json.dumps(result["nontrivial_bounds"], sort_keys=True))
    print(json.dumps(result["assumption_checks"], sort_keys=True))
    print(json.dumps(result["resources"], sort_keys=True))


if __name__ == "__main__":
    main()

"""Independent exact integration and finite-product coupling controls."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import time


def integrate_product(a, b):
    result = Q(0)
    points = sorted({Q(0), a, b, Q(1)})
    for left, right in zip(points, points[1:]):
        mid = (left + right) / 2
        c0, c1 = (Q(0), Q(1)) if mid < a else (a, Q(0))
        d0, d1 = (Q(0), Q(1)) if mid < b else (b, Q(0))
        coefficients = (c0 * d0, c0 * d1 + c1 * d0, c1 * d1)
        for degree, coefficient in enumerate(coefficients):
            result += coefficient * (right ** (degree + 1) - left ** (degree + 1)) / (degree + 1)
    return result - (a - a * a / 2) * (b - b * b / 2)


def formula(a, b):
    small, large = sorted((a, b))
    return small * small * (large * (2 - large) / 4 - small / 6)


def passage(bits):
    return min(2 + bits[0] + bits[1], 2 + bits[2] + bits[3])


def coordinate_delta(edge, rest):
    low = list(rest)
    low.insert(edge, 0)
    high = low.copy()
    high[edge] = 1
    return passage(high) - passage(low)


def transition(left, right, retention):
    result = Q(1)
    for x, y in zip(left, right):
        result *= (1 + retention) / 2 if x == y else (1 - retention) / 2
    return result


def main():
    started = time.perf_counter()
    grid = [Q(k, 8) for k in range(9)]
    for a, b in product(grid, repeat=2):
        exact = integrate_product(a, b)
        assert formula(a, b) == exact
        assert Q(0) <= exact <= Q(1, 12)
    assert formula(Q(0), Q(1)) == 0 and formula(Q(1), Q(1)) == Q(1, 12)
    environments = list(product((0, 1), repeat=4))
    off_environments = list(product((0, 1), repeat=3))
    mean = Q(sum(passage(x) for x in environments), 16)
    variance = Q(sum(passage(x) ** 2 for x in environments), 16) - mean * mean
    masses = defaultdict(Q)
    for mask in range(1, 16):
        included = [j for j in range(4) if mask & (1 << j)]
        coefficient = Q(0)
        for bits in environments:
            sign = 1
            for j in included:
                sign *= 2 * bits[j] - 1
            coefficient += Q(passage(bits) * sign, 16)
        masses[len(included)] += coefficient * coefficient
    assert variance == sum(masses.values()) == Q(23, 64)
    checks = []
    for retention in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
        direct_covariance = sum(
            Q(1, 16) * transition(x, y, retention) * (passage(x) - mean) * (passage(y) - mean)
            for x, y in product(environments, repeat=2)
        )
        spectral_covariance = sum(mass * retention ** k for k, mass in masses.items())
        assert direct_covariance == spectral_covariance
        # An explicit off-edge coupling gives the threshold covariance.
        H = Q(0)
        for edge in range(4):
            for x, y in product(off_environments, repeat=2):
                H += Q(1, 8) * transition(x, y, retention) * Q(coordinate_delta(edge, x) * coordinate_delta(edge, y), 4)
        I = sum(k * mass * retention ** k for k, mass in masses.items())
        assert retention * H == I
        assert H == sum(k * mass * retention ** (k - 1) for k, mass in masses.items())
        checks.append({"retention": str(retention), "H": str(H), "retention_times_H": str(I), "covariance": str(direct_covariance)})
    # H(r) = sum k mass_k r^(k-1); integrating against dr gives variance.
    correct_integral = sum(Q(k) * mass / k for k, mass in masses.items())
    assert correct_integral == variance
    # With r=exp(-t), omitting r leaves a positive first-level limit as t grows.
    assert masses[1] == Q(1, 4)
    receipt = {
        "command": "python -X utf8 -B verify_kernel.py",
        "uniform_kernel_pairs_checked": 81,
        "binary_square_environments": 16,
        "coupling_retention_points_checked": 5,
        "spectral_level_masses": {str(k): str(v) for k, v in sorted(masses.items())},
        "covariance_and_threshold_controls": checks,
        "correct_integrated_variance": str(correct_integral),
        "missing_retention_factor_large_time_floor": str(masses[1]),
        "missing_retention_factor_integral": "diverges",
        "method": "Exact rational polynomial integration, independently constructed joint coupling, and Walsh decomposition; not a formal proof receipt",
        "independent_review": "pending w362",
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    Path("KERNEL_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()

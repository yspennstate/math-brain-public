"""Exact certificate and independent decimal audit for PROOF.md.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_certificate.py
The assertions certifying the theorem use Fraction/integer arithmetic only.
"""

import ctypes
from decimal import Decimal, localcontext
from fractions import Fraction as F
import json
import math
import os
from pathlib import Path
import resource
import sys


def guard():
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    lib = ctypes.CDLL(None, use_errno=True)
    ctypes.set_errno(0)
    priority = lib.getpriority(0, 0)
    assert ctypes.get_errno() == 0 and priority >= 15
    print(f"niceness={priority}; OMP_NUM_THREADS=1; CPU limit=60s")


def exp_lower(x, degree):
    return sum((x ** j / math.factorial(j) for j in range(degree + 1)), F(0))


def atan_partial(x, terms):
    return sum(((-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
                for j in range(terms)), F(0))


def log_bounds(x, terms=80):
    """For rational x>1, exact bounds via log x=2 atanh((x-1)/(x+1))."""
    assert x > 1
    z = (x - 1) / (x + 1)
    lower = 2 * sum((z ** (2 * j + 1) / (2 * j + 1)
                     for j in range(terms)), F(0))
    # Bound all omitted denominators below by the first omitted one.
    error = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + error


def dec(x):
    if isinstance(x, F):
        return Decimal(x.numerator) / Decimal(x.denominator)
    return Decimal(x)


def main():
    guard()
    e75 = exp_lower(F(15, 2), 30)
    pi_lower = 16 * atan_partial(F(1, 5), 8) - 4 * atan_partial(F(1, 239), 5)
    e11 = exp_lower(F(11, 10), 6)
    assert e75 > 1800
    assert pi_lower > F(177, 100) ** 2
    assert e11 > 3

    p = F(63, 500)
    p_upper = F(1, 120) + F(104, 885)
    assert p - p_upper == F(9, 59000)
    lhs = 775 ** 31 * 225 ** 9
    rhs = 3 ** 40 * 126 ** 31 * 874 ** 9
    assert lhs > rhs
    h, q = F(13, 16500), F(9, 40)
    green_distance = F(1, 3) - F(3, 11)
    green_image = F(1, 1 + 2) - F(3, 3 * 3 + 2)
    assert green_distance == green_image == F(2, 33)
    assert green_distance * F(13, 1000) == h
    delta_coarse = q * h / F(11, 10)
    assert delta_coarse == F(39, 242000) > F(1, 6250)

    # Independent rational logarithm audit of the Chernoff comparison.
    l1, u1 = log_bounds(F(775, 126))
    l2, u2 = log_bounds(F(874, 225))
    l3, u3 = log_bounds(F(3))
    margin_lower = F(31, 40) * l1 - F(9, 40) * u2 - u3
    margin_upper = F(31, 40) * u1 - F(9, 40) * l2 - l3
    assert 0 < margin_lower < margin_upper
    lh, uh = log_bounds(F(16500, 16487))
    delta_lower, delta_upper = q * lh / u3, q * uh / l3
    assert F(1, 6250) < delta_lower < delta_upper

    # Independent high-precision evaluation, using Decimal's own ln/exp/sqrt.
    with localcontext() as ctx:
        ctx.prec = 65
        # A pi interval from a different truncation length.
        pi_lo2 = 16 * atan_partial(F(1, 5), 24) - 4 * atan_partial(F(1, 239), 13)
        pi_hi2 = 16 * atan_partial(F(1, 5), 25) - 4 * atan_partial(F(1, 239), 12)
        assert pi_lower < pi_lo2 < pi_hi2
        pi_mid = (dec(pi_lo2) + dec(pi_hi2)) / 2
        exit_bound = 6 * Decimal(6).sqrt() * (Decimal(-15) / 2).exp()
        energy = 16 / pi_mid.sqrt()
        p_actual = exit_bound + dec(F(13, 1000)) * energy
        a = dec(F(31, 40))
        p_dec = dec(p)
        d = a * (a / p_dec).ln() + (1 - a) * ((1 - a) / (1 - p_dec)).ln()
        b = d / Decimal(3).ln()
        delta = -dec(q) * (1 - dec(h)).ln() / Decimal(3).ln()
        assert dec(delta_lower) <= delta <= dec(delta_upper)
        assert dec(margin_lower) <= d - Decimal(3).ln() <= dec(margin_upper)
        data = {
            "exact_checks": {
                "exp_7.5_partial_sum_gt_1800": True,
                "pi_lower_gt_1.77_squared": True,
                "exp_1.1_partial_sum_gt_3": True,
                "failure_probability_rational_margin": str(p - p_upper),
                "chernoff_integer_lhs": str(lhs),
                "chernoff_integer_rhs": str(rhs),
                "chernoff_integer_difference_positive": lhs > rhs,
                "green_constant_two_ways": str(green_distance),
                "hit_probability": str(h),
                "delta_coarse_lower_bound": str(delta_coarse),
                "delta_coarse_margin_above_1_over_6250": str(delta_coarse - F(1, 6250)),
                "chernoff_log_series_margin_positive": True,
            },
            "decimal_crosscheck": {
                "exit_failure_bound": str(exit_bound),
                "expected_energy_times_r": str(energy),
                "failure_probability_bound_before_rounding": str(p_actual),
                "rounded_failure_probability": str(p_dec),
                "chernoff_tail_exponent_with_rounded_p": str(b),
                "chernoff_log_margin": str(d - Decimal(3).ln()),
                "log_margin_rational_lower": str(dec(margin_lower)),
                "log_margin_rational_upper": str(dec(margin_upper)),
                "delta": str(delta),
                "delta_rational_interval_lower": str(dec(delta_lower)),
                "delta_rational_interval_upper": str(dec(delta_upper)),
                "xi_upper_bound": str(1 - delta),
            },
        }
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    data["peak_RSS_bytes"] = rss if sys.platform == "darwin" else rss * 1024
    assert data["peak_RSS_bytes"] < 1024 ** 3
    Path("certificate.json").write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(data, indent=2))
    print("ALL EXACT CERTIFICATE CHECKS PASSED")


if __name__ == "__main__":
    main()

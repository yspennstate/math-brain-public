#!/usr/bin/env python3
"""Independent rational-interval repair for the B09 two-bit AND certificate.

Source: yspennstate/math-open-problems@adb671ffcda143fa68347806bb96e8c305621a7d
reports/fei-2026-10-11/runs/B09/
20261011T195500Z-account01-B09-biased-restriction-uncertainty/
check_biased_and_counterexample.py

The atanh series and remainder are retained. Division now takes the extrema
of all four endpoint quotients, including negative logarithm numerators.
No floating-point arithmetic is used in the mathematical checks.
"""

from fractions import Fraction as Q
from functools import lru_cache
import json


@lru_cache(maxsize=None)
def ln_interval(x, terms=1200):
    """Closed rational enclosure of ln(x), with an explicit series remainder."""
    x = Q(x)
    if x <= 0:
        raise ValueError("ln requires a strictly positive argument")
    if not isinstance(terms, int) or terms < 1:
        raise ValueError("the number of terms must be a positive integer")
    if x == 1:
        return Q(0), Q(0)
    if x < 1:
        lo, hi = ln_interval(1 / x, terms)
        return -hi, -lo
    z = (x - 1) / (x + 1)
    s = sum(z ** (2 * k + 1) / (2 * k + 1) for k in range(terms)) * 2
    rem = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return s, s + rem


def divide_by_positive_interval(numerator, denominator):
    lo, hi = numerator
    d_lo, d_hi = denominator
    if lo > hi or not 0 < d_lo <= d_hi:
        raise ValueError("ordered intervals and a strictly positive denominator required")
    quotients = (lo / d_lo, lo / d_hi, hi / d_lo, hi / d_hi)
    return min(quotients), max(quotients)


def log2_interval(x, terms=1200):
    return divide_by_positive_interval(ln_interval(Q(x), terms),
                                       ln_interval(Q(2), terms))


def entropy_interval(probs, terms=1200):
    probs = tuple(Q(p) for p in probs)
    if any(p < 0 or p > 1 for p in probs) or sum(probs) != 1:
        raise ValueError("entropy requires a probability distribution")
    lo = hi = Q(0)
    for p in probs:
        if p == 0:
            continue
        lower_log, upper_log = log2_interval(p, terms)
        lo -= p * upper_log
        hi -= p * lower_log
    assert lo <= hi
    return lo, hi


def sub(a, b):
    return a[0] - b[1], a[1] - b[0]


def scale(c, a):
    c = Q(c)
    products = c * a[0], c * a[1]
    return min(products), max(products)


def decimal_bounds(a, digits=18):
    """Outward rounding of both signed rational endpoints, as decimal strings."""
    factor = 10 ** digits
    lower = a[0].numerator * factor // a[0].denominator
    upper = -((-a[1].numerator * factor) // a[1].denominator)
    def render(integer):
        sign = "-" if integer < 0 else ""
        integer = abs(integer)
        return f"{sign}{integer // factor}.{integer % factor:0{digits}d}"
    return render(lower), render(upper)


def regression_checks():
    # The old formula actually reverses the endpoints on a probability used
    # in the original counterexample, at a small independently inspectable
    # truncation depth. Correct interval division must remain ordered.
    source_probability = Q(225, 256)
    lo, hi = ln_interval(source_probability, 12)
    d_lo, d_hi = ln_interval(Q(2), 12)
    old = lo / d_hi, hi / d_lo
    assert old[0] > old[1]
    repaired = log2_interval(source_probability, 12)
    assert repaired[0] < repaired[1] < 0

    # Exact logarithms in both sign domains, independently known as integers.
    for exponent in range(-5, 6):
        bounds = log2_interval(Q(2) ** exponent, 12)
        assert bounds[0] <= exponent <= bounds[1]

    # A coarse exact quotient test makes the sign issue visible without
    # any transcendental calculation or numerical reference.
    assert divide_by_positive_interval((Q(-3), Q(-2)), (Q(1), Q(2))) == (Q(-3), Q(-1))
    assert divide_by_positive_interval((Q(2), Q(3)), (Q(1), Q(2))) == (Q(1), Q(3))
    assert divide_by_positive_interval((Q(-1), Q(1)), (Q(1), Q(2))) == (Q(-1), Q(1))
    assert log2_interval(Q(1), 12) == (Q(0), Q(0))
    assert entropy_interval([Q(0), Q(1)], 12) == (Q(0), Q(0))
    half_entropy = entropy_interval([Q(1, 2), Q(1, 2)], 12)
    assert half_entropy[0] <= 1 <= half_entropy[1]

    invalid_cases = 0
    for value in (Q(0), Q(-1)):
        try:
            log2_interval(value, 12)
        except ValueError:
            invalid_cases += 1
        else:
            raise AssertionError("nonpositive logarithm argument was accepted")
    for probs in ([Q(-1, 8), Q(9, 8)], [Q(1, 4), Q(1, 4)]):
        try:
            entropy_interval(probs, 12)
        except ValueError:
            invalid_cases += 1
        else:
            raise AssertionError("invalid probability law was accepted")
    assert invalid_cases == 4
    return {
        "status": "PASS",
        "original_endpoint_inversion_reproduced": True,
        "original_inversion_argument": "225/256",
        "original_inversion_terms": 12,
        "exact_power_of_two_logarithm_cases": 11,
        "sign_sensitive_exact_quotient_cases": 3,
        "zero_one_probability_cases": "PASS",
        "invalid_domain_cases_rejected": invalid_cases,
    }


def main():
    regression = regression_checks()
    probabilities = [Q(225, 256), Q(7, 256), Q(3, 256), Q(21, 256)]
    assert sum(probabilities) == 1
    parent_entropy = entropy_interval(probabilities)
    residual_entropy = entropy_interval([Q(3, 32), Q(29, 32)])
    child_entropy = entropy_interval([Q(3, 4), Q(1, 4)])
    M = sub(parent_entropy, residual_entropy)
    J = sub(residual_entropy, scale(Q(1, 8), child_entropy))
    gap = sub(J, M)
    assert gap[0] > Q(1195, 10000)
    for interval in (parent_entropy, residual_entropy, child_entropy, M, J, gap):
        assert interval[0] <= interval[1]
    print(json.dumps({
        "status": "PASS",
        "randomness": "NONE",
        "arithmetic": "fractions.Fraction; rational atanh remainder; four endpoint quotients",
        "terms": 1200,
        "source_commit": "adb671ffcda143fa68347806bb96e8c305621a7d",
        "source_script_blob": "d8a3849f1fed3f2c879aa4c6cd12407d08e6f383",
        "source_script_sha256": "3147bc3d2dfeb54a2ecabce7c074131d9985a22fcd55b9a9fda3c4656b5af1fc",
        "regression_checks": regression,
        "gate": "(-1)^(X*Y)",
        "p": "1/8",
        "q": "1/4",
        "block": ["X"],
        "squared_biased_fourier_masses": [str(p) for p in probabilities],
        "M_interval": decimal_bounds(M),
        "J_interval": decimal_bounds(J),
        "J_minus_M_interval": decimal_bounds(gap),
        "certified_strict_lower_bound": "1195/10000 bits = 0.1195 bits",
        "certificate_scope": "Only the biased two-bit AND counterexample to J_A<=M_A and repaired interval arithmetic.",
        "full_B09_theorem_audit": "NOT_COMPLETED",
        "full_FEI": "OPEN",
        "execution_class": "interactive_independent_repair; not a natural scheduled B18 run",
    }, indent=2))


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""Independent attained-cut/tie checks for balanced finite-crossing FEI.

The author checker intentionally places cuts strictly between attained score
levels.  This separate suite puts cuts both on and between score levels,
enumerates every legal adjacent-label tie choice, and checks the patched
discrete-to-Gaussian label-set comparison.  Rational arithmetic is used for
the score law and label probabilities; normal CDF evaluations are numerical.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
import json
from math import erf, sqrt
from pathlib import Path


TOL = 2e-15


def phi(x):
    return (1.0 + erf(x / sqrt(2.0))) / 2.0


def score_law(weights):
    out = Counter({Q(0): 1})
    for weight in weights:
        nxt = Counter()
        for score, count in out.items():
            nxt[score - weight] += count
            nxt[score + weight] += count
        out = nxt
    return out


def label(score, cuts, ties):
    for j, cut in enumerate(cuts):
        if score == cut:
            return ties[j]
    return 1 if sum(cut < score for cut in cuts) % 2 == 0 else -1


def gaussian_open_label_probability(cuts, sign, sigma):
    endpoints = [float("-inf")]
    endpoints += [float(cut) / sigma for cut in cuts]
    endpoints += [float("inf")]
    answer = 0.0
    for j, (left, right) in enumerate(zip(endpoints, endpoints[1:])):
        interval_sign = 1 if j % 2 == 0 else -1
        if interval_sign != sign:
            continue
        left_cdf = 0.0 if left == float("-inf") else phi(left)
        right_cdf = 1.0 if right == float("inf") else phi(right)
        answer += right_cdf - left_cdf
    return answer


def observed_kolmogorov_distance(distribution, sigma):
    """Exact discrete left/right CDFs versus numerical continuous Gaussian."""
    total = sum(distribution.values())
    below = 0
    distance = 0.0
    for score in sorted(distribution):
        left = below / total
        right = (below + distribution[score]) / total
        gaussian = phi(float(score) / sigma)
        distance = max(distance, abs(left - gaussian), abs(right - gaussian))
        below += distribution[score]
    return distance


def main():
    weight_vectors = [
        (Q(1), Q(1)),
        (Q(0), Q(1), Q(1)),
        (Q(1), Q(2), Q(2)),
        (Q(1), Q(1), Q(2), Q(3)),
        (Q(0), Q(1), Q(2), Q(3), Q(3)),
    ]
    families = 0
    label_inequalities = 0
    attained_cut_occurrences = 0
    endpoint_assignments = 0
    worst_fraction = 0.0

    for weights in weight_vectors:
        distribution = score_law(weights)
        total = sum(distribution.values())
        sigma = sqrt(float(sum(weight * weight for weight in weights)))
        levels = sorted(distribution)
        midpoints = [(left + right) / 2
                     for left, right in zip(levels, levels[1:])]
        cut_pool = sorted(set(levels + midpoints))
        delta = observed_kolmogorov_distance(distribution, sigma)

        for crossing_count in range(1, min(3, len(cut_pool)) + 1):
            for cuts in combinations(cut_pool, crossing_count):
                attained_cut_occurrences += sum(cut in distribution
                                                for cut in cuts)
                for side_bits in product((0, 1), repeat=crossing_count):
                    # At crossing j, bit zero selects its left adjacent label
                    # and bit one selects its right adjacent label.
                    ties = tuple(
                        (1 if j % 2 == 0 else -1)
                        * (1 if side_bit == 0 else -1)
                        for j, side_bit in enumerate(side_bits)
                    )
                    endpoint_assignments += crossing_count
                    for sign in (-1, 1):
                        exact_count = sum(
                            count for score, count in distribution.items()
                            if label(score, cuts, ties) == sign
                        )
                        discrete_probability = exact_count / total
                        gaussian_probability = gaussian_open_label_probability(
                            cuts, sign, sigma
                        )
                        error = abs(discrete_probability - gaussian_probability)
                        bound = 2 * (crossing_count + 1) * delta
                        assert error <= bound + TOL
                        if bound:
                            worst_fraction = max(worst_fraction, error / bound)
                        label_inequalities += 1
                    families += 1

    report = {
        "status": "PASS independent attained-cut and legal-tie checks",
        "counts": {
            "weight_vectors": len(weight_vectors),
            "cut_and_tie_families": families,
            "label_inequalities": label_inequalities,
            "attained_cut_occurrences": attained_cut_occurrences,
            "legal_endpoint_assignments": endpoint_assignments,
        },
        "maximum_observed_error_fraction_of_2mplus2_delta_bound": worst_fraction,
        "exact": [
            "weighted-sign score distributions",
            "discrete label probabilities under every legal adjacent-label tie choice",
            "left and right discrete CDF values at every attained score",
        ],
        "numerical": [
            "Gaussian CDF values",
            "discrete-to-Gaussian interval-union comparison",
        ],
        "scope": (
            "Supplements the analytic CDF/left-limit proof of equation (8); "
            "does not prove Berry-Esseen, the large-N0 theorem, or novelty"
        ),
        "tolerance": TOL,
    }
    output = Path(__file__).with_name(
        "independent_input_regular_balanced_finite_crossing_endpoint_checks.json"
    )
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

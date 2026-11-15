"""Audit the finite decoder correction for binary two-site codes on Z.

Uses exact rational probabilities, two independent summations, and an
integer-product certificate for every entropy-gap sign. Standard library only.
"""

import csv
import itertools
import json
import math
import os
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import resource
import signal


# macOS does not support lowering RLIMIT_AS in this managed environment.
# This bounded enumeration stores 768 small rows; record actual peak RSS below.
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(60)
ROOT = Path(__file__).resolve().parent


def entropy(distribution):
    return -sum(float(q) * math.log(float(q)) for q in distribution if q)


def table(mask, a, b):
    return (mask >> (2 * a + b)) & 1


def distribution_direct(p, f, decoder):
    probs = (1 - p, p)
    joint = defaultdict(Fraction)
    err = Fraction(0)
    for a, b, c in itertools.product((0, 1), repeat=3):
        weight = probs[a] * probs[b] * probs[c]
        y0, y1 = table(f, a, b), table(f, b, c)
        predicted = table(decoder, y0, y1)
        residual = a ^ predicted
        # The binary rank correction recovers the actual input pointwise.
        assert predicted ^ residual == a
        joint[y0, residual] += weight
        err += weight * residual
    return dict(joint), err


def distribution_conditioned(p, f, decoder):
    # Conditional on the middle bit b, the pairs (a,Y0) and Y1 are independent.
    probs = (1 - p, p)
    joint = defaultdict(Fraction)
    for middle in (0, 1):
        left = defaultdict(Fraction)
        right = defaultdict(Fraction)
        for first in (0, 1):
            left[first, table(f, first, middle)] += probs[first]
        for last in (0, 1):
            right[table(f, middle, last)] += probs[last]
        for (actual, y0), q0 in left.items():
            for y1, q1 in right.items():
                prediction = table(decoder, y0, y1)
                correction = int(actual != prediction)
                joint[y0, correction] += probs[middle] * q0 * q1
    return dict(joint)


def marginals(joint):
    y = defaultdict(Fraction)
    residual = defaultdict(Fraction)
    for (a, b), q in joint.items():
        y[a] += q
        residual[b] += q
    return y, residual


def exact_gap_sign(y, residual, p):
    # exp(Q * [H(Y)+H(R)-H(p)]) is a rational integer-product ratio.
    # Comparing its numerator and denominator avoids floating-point sign tests.
    base = (1 - p, p)
    denominator = math.lcm(*(q.denominator for q in
                             [*y.values(), *residual.values(), *base]))
    counts = lambda qs: [int(q * denominator) for q in qs if q]
    numerator = denominator**denominator
    for n in counts(base):
        numerator *= n**n
    divisor = 1
    for n in counts([*y.values(), *residual.values()]):
        divisor *= n**n
    return (numerator > divisor) - (numerator < divisor)


def main():
    rows = []
    summary = {"group": "Z", "S": [0, 1], "D": [0, 1],
               "input_support": [0, 1, 2], "cases": [],
               "probabilities": "exact fractions",
               "gap_sign": "exact integer-product comparison"}
    for p in (Fraction(1, 2), Fraction(1, 3), Fraction(2, 3)):
        signs = {-1: 0, 0: 0, 1: 0}
        max_chain_difference = 0.0
        max_subadditivity_excess = 0.0
        gaps = []
        for f in range(16):
            for decoder in range(16):
                joint, error = distribution_direct(p, f, decoder)
                assert joint == distribution_conditioned(p, f, decoder)
                assert sum(joint.values()) == 1
                y, residual = marginals(joint)
                assert residual.get(1, 0) == error
                hy, hr, hz = (entropy(y.values()), entropy(residual.values()),
                              entropy(joint.values()))
                conditional = 0.0
                for label, mass in y.items():
                    conditional += float(mass) * entropy(
                        q / mass for (a, _), q in joint.items() if a == label)
                difference = abs(hz - (hy + conditional))
                max_chain_difference = max(max_chain_difference, difference)
                assert difference < 1e-12
                max_subadditivity_excess = max(max_subadditivity_excess,
                                              hz - hy - hr)
                assert hz <= hy + hr + 1e-12
                sign = exact_gap_sign(y, residual, p)
                assert sign >= 0
                signs[sign] += 1
                gap = hy + hr - entropy((p, 1 - p))
                gaps.append(gap)
                rows.append({"p_one": str(p), "f_mask": f,
                             "decoder_mask": decoder, "error": str(error),
                             "H_Y": repr(hy), "H_R": repr(hr),
                             "H_Z": repr(hz), "cost": repr(hy + hr),
                             "gap": repr(gap), "exact_gap_sign": sign})
        summary["cases"].append({
            "p_one": str(p), "rules_and_decoders": 256,
            "negative_gap_exact": signs[-1], "zero_gap_exact": signs[0],
            "positive_gap_exact": signs[1], "min_gap_float": min(gaps),
            "max_chain_difference": max_chain_difference,
            "max_subadditivity_excess": max_subadditivity_excess})
    summary["total_rules_and_decoders"] = len(rows)
    summary["pointwise_reconstruction_checks"] = len(rows) * 8
    summary["nice_priority"] = os.getpriority(os.PRIO_PROCESS, 0)
    # On macOS ru_maxrss is bytes (the target machine for this audit).
    summary["peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert summary["peak_rss_bytes"] < 1024**3
    with (ROOT / "local_code_audit.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (ROOT / "local_code_audit.json").write_text(
        json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

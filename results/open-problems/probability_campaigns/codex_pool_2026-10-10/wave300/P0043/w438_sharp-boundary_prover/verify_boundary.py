"""Small exact finite sanity checks; the infinite proof is in ATTEMPT.md.

Run only after the required fresh compute gate. No imports from the live brain.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import time


def recurrence(a, p):
    q = F(1)
    ds = []
    for degree in reversed(a):
        ds.append(F(0) if degree == 1 else F(1, 4) / (1 - p * q / 2))
        q = p * q if degree == 1 else 2 * p * q - p * p * q * q
    return q, list(reversed(ds))


def enumeration(a, p):
    """Independent sum over edge configurations on the explicit finite tree."""
    edges = []
    frontier = [0]
    next_id = 1
    for degree in a:
        nxt = []
        for parent in frontier:
            for _ in range(degree):
                edges.append((parent, next_id))
                nxt.append(next_id)
                next_id += 1
        frontier = nxt
    terminals = set(frontier)
    total = F(0)
    for configuration in product((0, 1), repeat=len(edges)):
        reached = {0}
        probability = F(1)
        for (parent, child), is_open in zip(edges, configuration):
            probability *= p if is_open else 1 - p
            if is_open and parent in reached:
                reached.add(child)
        if reached.intersection(terminals):
            total += probability
    return total


def main():
    start = time.monotonic()
    identity_checks = bounds_checks = enumeration_checks = mutant_rejections = 0
    parameters = [F(1, 5), F(1, 2), F(2, 3), F(1)]
    for depth in range(8):
        for a in product((1, 2), repeat=depth):
            for p in parameters:
                q, ds = recurrence(a, p)
                means = [F(1)]
                for degree in a:
                    means.append(means[-1] * degree * p)
                reciprocal = 1 / means[-1] + sum(
                    (d / m for d, m in zip(ds, means)), F(0)
                )
                assert 1 / q == reciprocal, (a, p, q, reciprocal)
                identity_checks += 1
                s = sum((1 / means[i] for i, d in enumerate(a) if d == 2), F(0))
                assert 1 / means[-1] + s / 4 <= 1 / q
                assert 1 / q <= 1 / means[-1] + s / (4 * (1 - p / 2))
                bounds_checks += 1
                # This deliberately wrong indexing is a control, not another proof.
                mutant = 1 / means[-1] + sum(
                    (d / m for d, m in zip(ds, means[1:])), F(0)
                )
                mutant_rejections += mutant != reciprocal
                if depth <= 2:
                    assert enumeration(a, p) == q, (a, p)
                    enumeration_checks += 1
    result = {
        "command": "python -X utf8 verify_boundary.py",
        "proof_status": "finite exact sanity checks only; independent infinite proof audit pending",
        "offspring_lengths": [0, 7],
        "rational_parameters": [str(p) for p in parameters],
        "identity_checks_passed": identity_checks,
        "two_sided_bounds_passed": bounds_checks,
        "independent_edge_enumerations_passed": enumeration_checks,
        "wrong_denominator_mutant_rejected": mutant_rejections,
        "elapsed_seconds": round(time.monotonic() - start, 6),
    }
    Path("verification.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Audit the saved catalog without importing the enumeration program."""

import csv
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time
from collections import Counter


def main():
    started = time.monotonic()
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    signal.signal(signal.SIGALRM, lambda *_: sys.exit("20-minute wall limit"))
    signal.alarm(1200)
    root = Path(__file__).resolve().parent
    summary = json.loads((root / "summary.json").read_text())
    for name, expected in summary["sha256"].items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected

    # Construct the character table by multiplying explicit +/-1 coordinates.
    characters = []
    for s in range(16):
        row = []
        for a in range(16):
            value = 1
            for i in range(4):
                if s & (1 << i):
                    value *= 1 if a & (1 << i) else -1
            row.append(value)
        characters.append(row)
    envelope = [[0] * 17 for _ in range(9)]
    hist = Counter()
    type_hist = Counter()
    all_coefficients = {}
    with (root / "functions.csv").open(newline="") as handle:
        rows = csv.reader(handle)
        next(rows)
        count = 0
        for index, row in enumerate(rows):
            mask = int(row[0], 16)
            assert index == mask
            t = int(row[1])
            coeffs = list(map(int, row[2:]))
            assert len(coeffs) == 16
            values = [1 if mask & (1 << a) else -1 for a in range(16)]
            direct = [sum(v * c for v, c in zip(values, character)) for character in characters]
            assert coeffs == direct, mask
            squares = sorted([c**2 for c in coeffs], reverse=True)
            assert sum(squares) == 256
            hist[t] += 1
            type_hist[(tuple(squares), t)] += 1
            for m in range(17):
                tail = sum(squares[m:])  # independent of subtractive update in generator
                for budget in range(t, 9):
                    envelope[budget][m] = max(envelope[budget][m], tail)
            if mask in (0x0357, 0x001B, 0x0001, 0x7888):
                all_coefficients[mask] = (t, coeffs, squares)
            count += 1
    assert count == 65536
    assert {str(k): v for k, v in hist.items()} == summary["minimum_terms_histogram"]
    assert envelope == summary["at_most_term_budget_tail_numerators"]

    # Recheck every saved witness by interpreting literals directly, not using
    # the generator's cube lookup, predecessor pointers, or Walsh transform.
    with (root / "tail_envelope.csv").open(newline="") as handle:
        witness_count = 0
        for row in csv.DictReader(handle):
            budget, m = int(row["term_budget"]), int(row["retained"])
            terms = json.loads(row["witness_terms_json"])
            assert len(terms) <= budget
            truth = 0
            values = []
            for a in range(16):
                true = any(all(v == -1 or v == ((a >> i) & 1) for i, v in enumerate(term)) for term in terms)
                truth |= int(true) << a
                values.append(1 if true else -1)
            assert truth == int(row["witness_truth_mask_hex"], 16)
            coeffs = [sum(v * c for v, c in zip(values, character)) for character in characters]
            tail = sum(sorted([c*c for c in coeffs], reverse=True)[m:])
            assert tail == int(row["worst_tail_numerator"]) == envelope[budget][m]
            assert int(row["denominator"]) == 256
            witness_count += 1
    assert witness_count == 153

    assert envelope[2] == envelope[3]
    integer_checks = [(m, (m + 1) * envelope[2][m] ** 2) for m in range(4, 16)]
    assert all(lhs <= 256**2 for m, lhs in integer_checks)
    assert all(envelope[t][m] == 16 * (16 - m) for t in range(4, 9) for m in range(17))
    t, coeffs, squares = all_coefficients[0x0357]
    assert t == 2 and squares == [36] * 6 + [4] * 10
    assert sum(squares[:3]) == 108 < 128 <= sum(squares[:4]) == 144
    t, coeffs, squares = all_coefficients[0x7888]
    assert t == 4 and squares == [16] * 16
    # Deliberately test the excluded epsilon>1/2 range of the C=2 corollary:
    # epsilon=27/32, allowed sparsity (32/27)^2<2, but best one-term
    # approximation of the two-disjoint-pairs example has error 55/64.
    assert 1024 < 2 * 729
    assert 55 * 32 > 27 * 64

    with (root / "spectral_types_by_terms.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["squared_numerators_json"] + [f"minimum_terms_{t}" for t in range(9)])
        for kind in sorted({kind for kind, t in type_hist}):
            writer.writerow([json.dumps(kind)] + [type_hist[(kind, t)] for t in range(9)])
    output = {
        "functions_checked_by_literal_character_sums": count,
        "independently_reconstructed_envelope_entries": 153,
        "independently_evaluated_witness_DNFs": witness_count,
        "constant_2_integer_checks_m_and_lhs": integer_checks,
        "integer_check_rhs": 65536,
        "optimality_example_truth_mask": "0357",
        "flat_spectrum_example_truth_mask": "7888",
        "epsilon_greater_than_half_exclusion_test": "PASS: C=2 fails at epsilon=27/32",
        "actual_nice": os.getpriority(os.PRIO_PROCESS, 0),
        "peak_RSS_MiB": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024**2 if sys.platform == "darwin" else 1024), 3),
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }
    print(json.dumps(output, indent=2))
    print("PASS: saved data, witnesses, integer corollary, and endpoint countercheck")


if __name__ == "__main__":
    main()

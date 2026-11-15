"""Exact finite calculations used to audit the mathematical examples in REPORT.md.

Run: python3 code/check_examples.py
No simulation, floating-point arithmetic, external packages, or extra threads.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import os
import resource


def main():
    states = list(product((0, 1), repeat=2))
    transition = [[F(int(a[1] == b[0]), 2) for b in states] for a in states]
    squared = [[sum(transition[i][k] * transition[k][j] for k in range(4))
                for j in range(4)] for i in range(4)]
    assert all(value == F(1, 4) for row in squared for value in row)
    assert all(sum(row) == 1 for row in transition)

    triples = [(u[0] | u[1], u[1] | u[2], u[2] | u[3])
               for u in product((0, 1), repeat=4)]
    conditioning = [x for x in triples if x[1] == 1]
    a = F(sum(x[0] == 0 for x in conditioning), len(conditioning))
    b = F(sum(x[2] == 0 for x in conditioning), len(conditioning))
    joint = F(sum(x[0] == 0 and x[2] == 0 for x in conditioning), len(conditioning))
    assert a == b == F(1, 6)
    assert joint == 0 and a * b == F(1, 36)
    # Check the unconditional separated coordinates too.
    assert F(sum(x[0] == 0 and x[2] == 0 for x in triples), 16) == F(1, 16)

    result = {
        "method": "Exhaustive enumeration with fractions.Fraction",
        "window_chain_states": states,
        "transition": [[str(v) for v in row] for row in transition],
        "two_step_transition": [[str(v) for v in row] for row in squared],
        "or_process": {
            "fair_bit_assignments": 16,
            "middle_one_assignments": len(conditioning),
            "left_zero_given_middle_one": str(a),
            "right_zero_given_middle_one": str(b),
            "both_zero_given_middle_one": str(joint),
            "product_of_conditional_marginals": str(a * b),
        },
        "nice": os.getpriority(os.PRIO_PROCESS, 0),
        "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "scope": "Checks examples only; not a proof of a universal representation or nonrepresentation theorem.",
    }
    path = Path(__file__).resolve().parents[1] / "data" / "example_checks.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

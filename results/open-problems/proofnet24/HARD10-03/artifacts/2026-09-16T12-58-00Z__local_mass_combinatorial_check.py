#!/usr/bin/env python3
"""Exhaustive sanity check for the deterministic cyclic occupancy lemma in NEW-L90.

A binary word marks which cycle vertices lie in a fixed spatial ball. A cyclic
start is declared bad when its H+1 window contains at least two marked vertices.
For H >= L, the actual cyclic point window repeats a cycle vertex, so every start
is bad; this is encoded explicitly.

The theorem checked is
    |S|/L <= (# bad starts)/L + 1/(H+1).
This is only a finite combinatorial certificate; the analytic proof is in the
main report.
"""

import itertools
import json

MAX_L = 10

total = 0
failures = []

for L in range(1, MAX_L + 1):
    for H in range(1, MAX_L + 1):
        for bits in itertools.product((0, 1), repeat=L):
            total += 1
            marked = sum(bits)
            bad = []
            for j in range(L):
                if H >= L:
                    is_bad = 1
                else:
                    count = sum(bits[(j + t) % L] for t in range(H + 1))
                    is_bad = int(count >= 2)
                bad.append(is_bad)

            lhs = marked / L
            rhs = sum(bad) / L + 1.0 / (H + 1)
            if lhs > rhs + 1e-12:
                failures.append(
                    {
                        "L": L,
                        "H": H,
                        "bits": bits,
                        "lhs": lhs,
                        "rhs": rhs,
                    }
                )
                break
        if failures:
            break
    if failures:
        break

print(
    json.dumps(
        {
            "max_L": MAX_L,
            "cases_checked": total,
            "failures": failures,
            "status": "PASS" if not failures else "FAIL",
        },
        indent=2,
        sort_keys=True,
    )
)

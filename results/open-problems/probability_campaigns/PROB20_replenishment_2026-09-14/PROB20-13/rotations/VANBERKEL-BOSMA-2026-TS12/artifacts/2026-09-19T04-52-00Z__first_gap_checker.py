#!/usr/bin/env python3
"""Exact first-gap checker for VANBERKEL-BOSMA-2026-TS12.

This is a deliberately small independent checker. It implements the definition
of a greedy strict 3-sumfree sequence directly, using exact integer arithmetic,
only through the first interval not covered by Step 2 of Theorem 19.
"""
from itertools import combinations

CASES = [
    (4,6,17),(4,5,19),(1,9,24),(7,9,26),(1,11,29),(1,12,31),
    (5,7,26),(6,13,37),(6,7,27),(5,6,31),(7,13,38),(1,15,38),
]

def greedy_set(f, g, h, N):
    S = [f, g, h]
    for n in range(h + 1, N + 1):
        if not any(a + b + c == n for a, b, c in combinations(S, 3)):
            S.append(n)
    return set(S)

print("case q=f+g delta=d+1-q A gap_in gap_out")
for f, g, h in CASES:
    d = h - g
    q = f + g
    delta = d + 1 - q
    A = 2*q + h
    assert 0 < delta <= 2*q
    end = A + delta - 1
    S = greedy_set(f, g, h, end)

    predicted_in = list(range(A, A + min(delta, q)))
    predicted_out = list(range(A + q, A + delta)) if delta > q else []
    actual_in = [n for n in range(A, end + 1) if n in S]
    actual_out = [n for n in range(A, end + 1) if n not in S]

    assert actual_in == predicted_in
    assert actual_out == predicted_out
    print(
        f"{(f,g,h)} q={q} delta={delta} A={A} "
        f"in={actual_in} out={actual_out}"
    )

assert sum(1 for f,g,h in CASES if (h-g)+1-(f+g) <= f+g) == 11
assert [c for c in CASES if (c[2]-c[1])+1-(c[0]+c[1]) > c[0]+c[1]] == [(5,6,31)]
print("ELEVEN_FULL_GAP_CASES=11")
print("UNIQUE_PARTIAL_GAP_CASE=(5, 6, 31)")
print("ALL_EXACT_CHECKS_PASS")

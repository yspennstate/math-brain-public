#!/usr/bin/env python3
"""Exact Williamson row-sum filter for the candidate order 4*515 = 2060.

For a Williamson quadruple of four symmetric circulant ±1 matrices A,B,C,D
of odd order n=515 satisfying
    A A^T + B B^T + C C^T + D D^T = 4 n I,
let a,b,c,d be their (constant) row sums.  Applying the identity to the
all-ones vector gives a^2+b^2+c^2+d^2 = 4n.  Since n is odd, each row sum
is odd and nonzero.  Negating a whole sequence and permuting the four
sequences preserve the Williamson equations, so the absolute row sums
may be taken positive and nondecreasing.

This program exhaustively enumerates the resulting exact necessary
row-sum signatures.  It does NOT prove existence or nonexistence of a
Williamson quadruple or a Hadamard matrix.
"""

from itertools import combinations_with_replacement
import hashlib
import json

n = 515
target = 4 * n

# Every absolute row sum is a positive odd integer, and its square <= target.
max_abs = int(target ** 0.5)
odds = list(range(1, max_abs + 1, 2))

solutions = []
for q in combinations_with_replacement(odds, 4):
    if sum(x * x for x in q) == target:
        solutions.append(q)

# Independent exact self-checks.
assert len(solutions) == len(set(solutions))
assert solutions == sorted(solutions)
assert all(tuple(sorted(q)) == q for q in solutions)
assert all(all(x > 0 and x % 2 == 1 for x in q) for q in solutions)
assert all(sum(x*x for x in q) == target for q in solutions)

payload = "\n".join(",".join(map(str, q)) for q in solutions) + "\n"
digest = hashlib.sha256(payload.encode("ascii")).hexdigest()

print(f"williamson_base_order={n}")
print(f"hadamard_order_if_constructed={4*n}")
print(f"row_sum_square_target={target}")
print(f"max_abs_row_sum={max_abs}")
print(f"positive_odd_candidates={len(odds)}")
print(f"sorted_abs_rowsum_signature_count={len(solutions)}")
for q in solutions:
    print("signature=" + ",".join(map(str, q)))
print(f"signature_payload_sha256={digest}")
print("SCOPE=exact necessary row-sum filter only; no Williamson/Hadamard existence claim")
print("ALL_EXACT_ROWSUM_CHECKS_PASSED")

#!/usr/bin/env python3
"""Deterministic regression checks for POS3 initial-ideal chain deletion lemmas."""

from itertools import product


def weight_from_lambdas(seq, m):
    """Count nondecreasing t_i in {0,...,m} with t_i >= seq[i]."""
    if not seq:
        return 1
    dp = [1 if t >= seq[0] else 0 for t in range(m + 1)]
    for lam in seq[1:]:
        pref = []
        total = 0
        for x in dp:
            total += x
            pref.append(total)
        dp = [pref[t] if t >= lam else 0 for t in range(m + 1)]
    return sum(dp)


rank1_cases = 0
for m in range(0, 21):
    for a in range(m + 1):
        for b in range(a, m + 1):
            for s in range(m + 1):
                for t in range(m + 1):
                    lhs = (
                        int(a <= s <= m and b <= t <= m and s <= t)
                        - int(b <= s <= m and a <= t <= m and s <= t)
                    )
                    rhs = int(a <= s < b) * int(b <= t <= m)
                    assert lhs == rhs, (m, a, b, s, t, lhs, rhs)
            rank1_cases += 1

swap_cases = 0
for m in range(1, 6):
    values = range(m + 1)
    for n in range(2, 7):
        for seq in product(values, repeat=n):
            w = weight_from_lambdas(seq, m)
            for i in range(n - 1):
                if seq[i] > seq[i + 1]:
                    swapped = list(seq)
                    swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
                    w2 = weight_from_lambdas(tuple(swapped), m)
                    assert w2 >= w, (m, seq, i, w, w2)
                    swap_cases += 1

# Source-valid scalar-transfer warning:
# P consists of c1<c2<v plus u incomparable with c1,c2,v.
# Delete the ideal chain C={c1,c2}.  Q={u,v} is an antichain.
m = 2
w_uv = weight_from_lambdas((0, 2), m)
w_vu = weight_from_lambdas((2, 0), m)
assert (w_uv, w_vu) == (3, 1)
assert (w_uv + w_vu) / 2 == 2
assert w_uv / (w_uv + w_vu) == 3 / 4

print("rank1_matrix_interval_pairs", rank1_cases)
print("adjacent_inversion_cases", swap_cases)
print("scalar_transfer_example_weights", w_uv, w_vu)
print("scalar_transfer_example_uniform_probability", "1/2")
print("scalar_transfer_example_weighted_probability", "3/4")
print("POS3_IDEAL_BLOCK_RECURRENCE_CHECK_PASS")

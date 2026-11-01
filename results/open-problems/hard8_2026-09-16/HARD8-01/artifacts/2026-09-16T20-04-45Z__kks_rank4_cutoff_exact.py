N = 8
TARGET = (N - 1) ** 2


def theorem3_bound(start_rank: int, start_length: int):
    """Exact arithmetic specialization of the source-ported Pin/KKS Theorem 3 recurrence."""
    u = start_length
    trace = [(start_rank, u)]
    for r in range(start_rank, 1, -1):
        u = 2 * u + N - r + 1
        trace.append((r - 1, u))
    return u, trace


expected = {
    (2, 1): 9,
    (3, 1): 23,
    (4, 1): 47,
    (5, 1): 87,
}
for key, val in expected.items():
    got, _ = theorem3_bound(*key)
    assert got == val, (key, got, val)

safe_caps = {}
for r in (2, 3, 4, 5, 6, 7, 8):
    safe = [L for L in range(0, 100) if theorem3_bound(r, L)[0] <= TARGET]
    safe_caps[r] = max(safe) if safe else None

assert safe_caps[2] == 21
assert safe_caps[3] == 7
assert safe_caps[4] == 1
assert safe_caps[5] is None

rank4_bound, rank4_trace = theorem3_bound(4, 1)
assert rank4_trace == [(4, 1), (3, 7), (2, 20), (1, 47)]
assert rank4_bound == 47 < TARGET

print(f"N={N} TARGET={TARGET}")
for r in range(2, 9):
    b, tr = theorem3_bound(r, 1)
    print(f"LETTER_RANK_{r}_BOUND={b} SAFE_START_LENGTH_CAP={safe_caps[r]} TRACE={tr}")
print("COUNTEREXAMPLE_NECESSARY: every letter has rank >= 5")
print("COUNTEREXAMPLE_NECESSARY: no rank<=3 word of length <= 7")
print("COUNTEREXAMPLE_NECESSARY: no rank<=2 word of length <= 21")
print("RANK4_LETTER_COROLLARY: reset threshold <= 47 < 49")
print("ALL_EXACT_KKS_SHORT_RANK_CHECKS_PASSED")

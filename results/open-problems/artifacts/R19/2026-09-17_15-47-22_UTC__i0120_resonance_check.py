from itertools import product
from math import gcd

P = 37
THRESH_DEN = 15

# The level-30 e_5=2 survivor from the preceding R19 report.
FULL0 = [570, 30, 610, 580, 590, 230, 560, 40, 620, 10, 600, 50, 1, 557]
FULL_MOD0 = 1110  # 37 * 30
CORE0 = [x // 5 for x in FULL0[:12]]
CORE_MOD0 = 222  # FULL_MOD0 / 5
R0 = [x // 2 for x in CORE0]
BASE_DEN = 111


def good_mask(x, M):
    mask = 0
    for a in range(M):
        r = (a * x) % M
        d = min(r, M - r)
        if THRESH_DEN * d >= M:
            mask |= 1 << a
    return mask


def witness_count(v, M):
    mask = (1 << M) - 1
    for x in v:
        mask &= good_mask(x % M, M)
        if mask == 0:
            return 0
    return mask.bit_count()


def gcd_proper(v, level):
    for omit in range(len(v)):
        g = level
        for j, x in enumerate(v):
            if j != omit:
                g = gcd(g, x)
        if g > 1:
            return True
    return False


def ord_mod(a, m):
    x = 1
    for n in range(1, 10000):
        x = (x * a) % m
        if x == 1:
            return n
    raise AssertionError("order not found")


print("R19 I0120 exact resonance check")
print("arithmetic = exact integer / bitset")
print("full_base_modulus =", FULL_MOD0)
print("core_base_modulus =", CORE_MOD0)
print("base_denominator =", BASE_DEN)

assert all(x % 5 == 0 for x in FULL0[:12])
assert FULL0[12] % 5 and FULL0[13] % 5
assert (FULL0[1] - 2 * FULL0[0]) % FULL_MOD0 == 0
assert not gcd_proper(FULL0, 30)
assert witness_count(FULL0, FULL_MOD0) == 0
assert CORE0 == [114, 6, 122, 116, 118, 46, 112, 8, 124, 2, 120, 10]
assert R0 == [57, 3, 61, 58, 59, 23, 56, 4, 62, 1, 60, 5]
assert witness_count(R0, BASE_DEN) == 0
assert (R0[1] - 2 * R0[0]) % BASE_DEN == 0
print("base_e5_boundary = PASS")
print("base_core_witness_count_mod111 = 0")

# Binary persistence: 2 has exact order 36 mod 111.  The normalized core
# states are r_n = 2^{-n} r_0 (mod 111), so checking one whole period is
# an exact finite audit of the periodic orbit used in the proof.
order2 = ord_mod(2, BASE_DEN)
assert order2 == 36
period_counts = []
for n in range(order2):
    inv = pow(pow(2, n, BASE_DEN), -1, BASE_DEN)
    rn = [(inv * x) % BASE_DEN for x in R0]
    assert (rn[1] - 2 * rn[0]) % BASE_DEN == 0
    wc = witness_count(rn, BASE_DEN)
    period_counts.append(wc)
    assert wc == 0
print("binary_projective_period =", order2)
print("binary_period_all_no_witness = PASS")

# Exhaust every relation-preserving factor-3 lift of CORE0 from modulus
# 222 to 666.  There are 3^11 = 177147 because one linear relation
# determines the second lift digit from the other eleven digits.
M0 = CORE_MOD0
M = 3 * M0
lift_good = []
for i, x0 in enumerate(CORE0):
    lift_good.append([good_mask(x0 + M0 * b, M) for b in range(3)])

valid_pairs = []
for b0 in range(3):
    for b1 in range(3):
        y0 = CORE0[0] + M0 * b0
        y1 = CORE0[1] + M0 * b1
        if (y1 - 2 * y0) % M == 0:
            valid_pairs.append((b0, b1))
assert valid_pairs == [(0, 1), (1, 0), (2, 2)]

hist = {}
minimum = M + 1
minimum_examples = []
total = 0
for b0, b1 in valid_pairs:
    pair_mask = lift_good[0][b0] & lift_good[1][b1]
    for rest in product(range(3), repeat=10):
        mask = pair_mask
        for i, b in zip(range(2, 12), rest):
            mask &= lift_good[i][b]
        wc = mask.bit_count()
        total += 1
        hist[wc] = hist.get(wc, 0) + 1
        if wc < minimum:
            minimum = wc
            minimum_examples = [((b0, b1) + rest, mask)]
        elif wc == minimum and len(minimum_examples) < 3:
            minimum_examples.append(((b0, b1) + rest, mask))

assert total == 3 ** 11 == 177147
assert minimum == 24
assert 0 not in hist
assert hist[24] == 9
assert max(hist) == 128 and hist[128] == 6
print("factor3_relation_lifts_checked =", total)
print("factor3_min_core_witness_count =", minimum)
print("factor3_minimizers =", hist[minimum])
print("factor3_max_core_witness_count =", max(hist))
print("factor3_histogram =", sorted(hist.items()))
print("factor3_all_core_lifts_have_witness = PASS")

# The proof shows every core witness has five numerator lifts in the full
# q=5 fiber, and each of the two exceptional coordinates can exclude at
# most one because 2/15 < 1/5. Hence at least 3 survive per core witness.
full_lower_bound = 3 * minimum
assert full_lower_bound == 72
print("phase_completion_safe_shifts_per_core_witness >= 3")
print("factor3_full_descendant_witness_lower_bound =", full_lower_bound)
print("ALL_EXACT_CHECKS_PASS")

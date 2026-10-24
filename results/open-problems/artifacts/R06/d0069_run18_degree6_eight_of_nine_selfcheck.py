def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for p in range(max_part, 0, -1):
        for tail in partitions(n - p, p):
            yield (p,) + tail


p6 = [p for p in partitions(6) if len(p) >= 2]
expected = [
    (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1),
    (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1),
    (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1),
]
assert p6 == expected
nonsimple = [p for p in p6 if p != (1, 1, 1, 1, 1, 1)]
covered = {
    (5, 1), (4, 2), (3, 3), (3, 2, 1), (3, 1, 1, 1),
    (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1),
}
assert set(nonsimple) - covered == {(4, 1, 1)}
assert len(covered) == 8

bad = []
for a in range(0, 12, 2):
    for b in range(0, 12, 2):
        if a + b >= 4 and 2 * a + b < 6:
            bad.append((a, b))
assert bad == [(0, 4)]

for a in range(0, 12):
    for b in range(0, 14, 2):
        if a + b >= 5:
            assert 2 * a + b >= 6

assert 64 * 5 > 12 * 12
assert 16 * 5 > 5 * 5
assert 12 * 12 > 25 * 5
assert 64 * 5 < 20 * 20
for m in (1, 2, 3):
    assert m * (6 - m) >= 5
assert 8 > 5

print('D0069 run18 exact self-check')
print('degree6_nonsimple_partitions=', nonsimple)
print('source_matching_covered=', sorted(covered, reverse=True))
print('aux_C6=8/9; sole_remaining=(4,1,1)')
print('cut_2211_unique_bad_profile=(0,4)')
print('K4_transfer_match_gt1: 320>144')
print('K4_transfer_adjacent_gt1: 80>25')
print('321_cycle_transfer_gt1: 144>125')
print('411_scalar_blue_barrier: 320<400')
print('SELF_CHECK_PASS')

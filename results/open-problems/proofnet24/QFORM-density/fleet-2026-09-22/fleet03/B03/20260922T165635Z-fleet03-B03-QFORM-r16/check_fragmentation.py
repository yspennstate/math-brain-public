from itertools import combinations_with_replacement

C_OFF = 4.8117455951457755


def check_sum_intervals(N, M=10):
    centers = [M**k for k in range(1, N + 1)]
    sums = sorted((centers[i] + centers[j], i, j)
                  for i in range(N) for j in range(i, N))
    assert len(sums) == N * (N + 1) // 2
    assert len({s[0] for s in sums}) == len(sums)
    if len(sums) > 1:
        min_gap = min(sums[k + 1][0] - sums[k][0]
                      for k in range(len(sums) - 1))
        assert min_gap > 2 / N
    support_measure = len(sums) * (2 / N)
    expected = N + 1
    assert abs(support_measure - expected) < 1e-12
    F = support_measure / 2
    assert abs(F - (N + 1) / 2) < 1e-12
    return len(sums), support_measure, F


for N in range(1, 13):
    print(N, check_sum_intervals(N))

large_atom_bound = C_OFF * 32 ** (1 / 3)
print("large_atom_bound", repr(large_atom_bound))
assert abs(large_atom_bound - 15.276340039075507) < 1e-12
print("QFORM_B03_R16_CHECK_PASS")

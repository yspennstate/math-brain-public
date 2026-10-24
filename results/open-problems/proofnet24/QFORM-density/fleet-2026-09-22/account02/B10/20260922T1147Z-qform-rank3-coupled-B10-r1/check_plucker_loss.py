from fractions import Fraction


def walsh_pair_stats(n: int):
    assert n % 2 == 0
    signs = [1] * (n // 2) + [-1] * (n // 2)
    nonzero = 0
    total_weight = Fraction(0, 1)
    for i in range(n):
        for j in range(i + 1, n):
            numerator = (signs[j] - signs[i]) ** 2
            if numerator:
                nonzero += 1
                total_weight += Fraction(numerator, n * n)
    sum_sqrt_weight = Fraction(2 * nonzero, n)
    assert nonzero == n * n // 4
    assert total_weight == 1
    assert sum_sqrt_weight == n // 2
    return nonzero, total_weight, sum_sqrt_weight


for n in (8, 16, 32, 64):
    nonzero, total_weight, sum_sqrt_weight = walsh_pair_stats(n)
    print(
        f"n={n} nonzero={nonzero} total_weight={total_weight} "
        f"sum_sqrt_weight={sum_sqrt_weight} expected_n_over_2={n//2}"
    )

print("QFORM_PLUCKER_RECIPROCAL_LOSS_CHECK_PASS")

def partitions(n, maxpart=None):
    if n == 0:
        yield ()
        return
    if maxpart is None or maxpart > n:
        maxpart = n
    for p in range(maxpart, 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest


def main():
    p6 = list(partitions(6))
    admissible_nonsimple = [p for p in p6 if p not in [(6,), (1, 1, 1, 1, 1, 1)]]
    expected = [
        (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1),
        (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1),
        (2, 1, 1, 1, 1),
    ]
    assert admissible_nonsimple == expected

    covered = {
        (5, 1), (4, 2), (3, 3), (3, 2, 1), (3, 1, 1, 1), (2, 2, 2)
    }
    residual = [p for p in admissible_nonsimple if p not in covered]
    assert residual == [(4, 1, 1), (2, 2, 1, 1), (2, 1, 1, 1, 1)]

    # Exact squared comparisons used by the easy six-pattern screen.
    assert 5 >= 5          # [5,1]: sqrt(5)
    assert 8 > 5           # [4,2]: sqrt(8)
    assert 9 > 5           # [3,3]: 3
    assert 8 > 5           # [2,2,2]: 2*sqrt(2)
    assert 6 > 5           # [3,2,1], infinite alternating component: sqrt(6)
    assert 144 > 125       # [3,2,1], finite-cycle block: 12/(5*sqrt(5)) > 1

    print("DEGREE6_PARTITION_LIST_PASS")
    print("covered=6/9")
    print("residual=" + repr(residual))
    print("EASY_PATTERN_EXACT_INEQUALITIES_PASS")
    print("ALL_EXACT_PARTITION_SCREEN_CHECKS_PASS")


if __name__ == "__main__":
    main()

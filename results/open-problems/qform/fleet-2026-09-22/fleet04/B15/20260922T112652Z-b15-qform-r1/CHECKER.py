#!/usr/bin/env python3
"""Exact Hadamard regression for fleet04/B15 qform run."""
from fractions import Fraction
from itertools import combinations


def parity(x: int) -> int:
    return x.bit_count() & 1


def walsh_row(mask: int, n: int):
    return [1 if parity(mask & x) == 0 else -1 for x in range(n)]


def det3(cols):
    (a, b, c), (d, e, f), (g, h, i) = cols
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def check(n: int) -> None:
    rows = [walsh_row(mask, n) for mask in (0, 1, 2)]
    for a in range(3):
        for b in range(3):
            dot = sum(rows[a][x] * rows[b][x] for x in range(n))
            assert dot == (n if a == b else 0)

    # A entries are represented as integer numerators over n.
    anum = [[rows[0][a] * rows[0][b] + rows[1][a] * rows[1][b]
             - rows[2][a] * rows[2][b] for b in range(n)] for a in range(n)]
    assert all(anum[a][a] == 1 for a in range(n))
    max_pair_det_num = None
    for a, b in combinations(range(n), 2):
        det_num = anum[a][a] * anum[b][b] - anum[a][b] ** 2
        assert det_num <= 0
        max_pair_det_num = det_num if max_pair_det_num is None else max(max_pair_det_num, det_num)

    # Verify the three nonzero eigenvectors at numerator level.
    for k, sign in ((0, 1), (1, 1), (2, -1)):
        for a in range(n):
            lhs = sum(anum[a][b] * rows[k][b] for b in range(n))
            assert lhs == sign * n * rows[k][a]

    cb = 0
    max_abs_det = 0
    for J in combinations(range(n), 3):
        matrix = [[rows[r][j] for j in J] for r in range(3)]
        d = det3(matrix)
        cb += d * d
        max_abs_det = max(max_abs_det, abs(d))
    assert cb == n ** 3
    normalized_max = Fraction(max_abs_det, 1) / (n ** Fraction(3, 2)) if False else max_abs_det / (n ** 1.5)
    print(f"n={n} max_pair_det_num={max_pair_det_num} cauchy_binet={cb} max_abs_det={max_abs_det} normalized_max={normalized_max:.12g}")


def main() -> None:
    for n in (4, 8, 16, 32, 64):
        check(n)
    print("PASS")


if __name__ == "__main__":
    main()

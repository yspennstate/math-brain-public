"""Exact finite-type interval branching bound for T_3 x Z.

The lower process keeps only one contiguous interval in each reached vertical
fiber. Type m means that the fiber contains a reachable interval of length m,
with type M meaning length at least M. From a parent interval of length m, a
child fiber receives open horizontal seeds from the m sites, then expands those
seeds through independent vertical percolation on Z. The retained child type is
the capped length of the longest contiguous reached interval.

For a fixed cap M and rational p=a/b, the transition probabilities are exact:
to determine the capped child type it is enough to inspect vertical edges in
the window [-(M-1), m-1+(M-1)]. If the reached set hits the boundary, the
capped type is already M.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def longest_reached_type(m: int, cap: int, seeds_mask: int, edge_mask: int) -> int:
    if seeds_mask == 0:
        return 0

    left = -(cap - 1)
    right = (m - 1) + (cap - 1)
    reached = {i for i in range(m) if (seeds_mask >> i) & 1}
    stack = list(reached)

    while stack:
        h = stack.pop()
        if left <= h < right:
            edge_index = h - left
            if (edge_mask >> edge_index) & 1 and h + 1 not in reached:
                reached.add(h + 1)
                stack.append(h + 1)
        if left < h <= right:
            edge_index = (h - 1) - left
            if (edge_mask >> edge_index) & 1 and h - 1 not in reached:
                reached.add(h - 1)
                stack.append(h - 1)

    values = sorted(reached)
    best = 1
    current = 1
    for x, y in zip(values, values[1:]):
        if y == x + 1:
            current += 1
        else:
            best = max(best, current)
            current = 1
    return min(cap, max(best, current))


def transition_counts(cap: int, p_num: int, p_den: int) -> tuple[list[list[int]], list[int]]:
    q_num = p_den - p_num
    max_variables = 4 * cap + 10
    pow_p = [1] * max_variables
    pow_q = [1] * max_variables
    pow_den = [1] * max_variables
    for i in range(1, max_variables):
        pow_p[i] = pow_p[i - 1] * p_num
        pow_q[i] = pow_q[i - 1] * q_num
        pow_den[i] = pow_den[i - 1] * p_den

    rows: list[list[int]] = []
    denoms: list[int] = []
    for m in range(1, cap + 1):
        edge_count = m + 2 * cap - 3
        denominator = pow_den[m + edge_count]
        counts = [0] * (cap + 1)

        for seeds_mask in range(1 << m):
            seed_count = seeds_mask.bit_count()
            if seeds_mask == 0:
                counts[0] += pow_q[m] * pow_den[edge_count]
                continue

            seed_weight = pow_p[seed_count] * pow_q[m - seed_count]
            for edge_mask in range(1 << edge_count):
                open_edges = edge_mask.bit_count()
                child_type = longest_reached_type(m, cap, seeds_mask, edge_mask)
                counts[child_type] += (
                    seed_weight
                    * pow_p[open_edges]
                    * pow_q[edge_count - open_edges]
                )

        if sum(counts) != denominator:
            raise ArithmeticError("transition probabilities do not sum to one")
        rows.append(counts)
        denoms.append(denominator)

    return rows, denoms


def mean_matrix_float(
    rows: list[list[int]], denoms: list[int], forward_degree: int
) -> list[list[float]]:
    cap = len(rows)
    return [
        [forward_degree * rows[i][j + 1] / denoms[i] for j in range(cap)]
        for i in range(cap)
    ]


def power_right(matrix: list[list[float]], iterations: int = 1000) -> tuple[list[float], float]:
    n = len(matrix)
    vector = [1.0 / n] * n
    for _ in range(iterations):
        image = [sum(matrix[i][j] * vector[j] for j in range(n)) for i in range(n)]
        total = sum(image)
        vector = [x / total for x in image]

    image = [sum(matrix[i][j] * vector[j] for j in range(n)) for i in range(n)]
    min_ratio = min(image[i] / vector[i] for i in range(n))
    return vector, min_ratio


def rational_certificate(
    rows: list[list[int]],
    denoms: list[int],
    forward_degree: int,
    vector_float: list[float],
    scale: int,
) -> tuple[list[int], list[Fraction]]:
    cap = len(rows)
    vector = [max(1, round(x * scale)) for x in vector_float]
    ratios = []
    for i in range(cap):
        lhs = forward_degree * sum(rows[i][j + 1] * vector[j] for j in range(cap))
        rhs = denoms[i] * vector[i]
        ratios.append(Fraction(lhs, rhs))
    return vector, ratios


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cap", type=int, default=6)
    parser.add_argument("--p-num", type=int, default=61)
    parser.add_argument("--p-den", type=int, default=200)
    parser.add_argument("--forward-degree", type=int, default=2)
    parser.add_argument("--scale", type=int, default=100000)
    args = parser.parse_args()

    rows, denoms = transition_counts(args.cap, args.p_num, args.p_den)
    matrix = mean_matrix_float(rows, denoms, args.forward_degree)
    vector_float, spectral_lower_float = power_right(matrix)
    vector, ratios = rational_certificate(
        rows, denoms, args.forward_degree, vector_float, args.scale
    )

    print(f"cap={args.cap}")
    print(f"p={args.p_num}/{args.p_den}={args.p_num / args.p_den:.12g}")
    print(f"forward_degree={args.forward_degree}")
    print(f"spectral_lower_float={spectral_lower_float:.12g}")
    print(f"certificate_vector={vector}")
    print(f"certificate_min_ratio={float(min(ratios)):.12g}")
    print("certificate_ratios=[" + ", ".join(f"{float(r):.12g}" for r in ratios) + "]")
    print("row_sums=[" + ", ".join(f"{sum(row):.12g}" for row in matrix) + "]")
    if min(ratios) > 1:
        print("CERTIFIED: spectral_radius > 1")
    else:
        print("NOT CERTIFIED: this vector does not prove spectral_radius > 1")


if __name__ == "__main__":
    main()

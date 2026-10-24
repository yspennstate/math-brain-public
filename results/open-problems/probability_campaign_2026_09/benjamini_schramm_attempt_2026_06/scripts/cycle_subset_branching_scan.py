"""Floating-point reached-subset branching scans for T_3 x C_m.

For a finite cycle fibre C_m, a type is a non-empty reached subset of the
cycle.  From a parent type S, a child fibre receives independent horizontal
seeds on the sites of S and then expands those seeds through independent
vertical percolation on C_m.  Multiplication by the two forward tree children
gives the mean matrix for a finite-type lower branching process.

This is a diagnostic script, not a rational certificate.
"""

from __future__ import annotations

import argparse
from functools import lru_cache


def reached_from(seed_mask: int, edge_mask: int, m: int) -> int:
    if seed_mask == 0:
        return 0

    reached = seed_mask
    changed = True
    while changed:
        changed = False
        for site in range(m):
            if not ((edge_mask >> site) & 1):
                continue
            neighbor = (site + 1) % m
            site_reached = (reached >> site) & 1
            neighbor_reached = (reached >> neighbor) & 1
            if site_reached and not neighbor_reached:
                reached |= 1 << neighbor
                changed = True
            elif neighbor_reached and not site_reached:
                reached |= 1 << site
                changed = True
    return reached


@lru_cache(maxsize=None)
def edge_reached_counts(m: int) -> dict[int, dict[tuple[int, int], int]]:
    counts: dict[int, dict[tuple[int, int], int]] = {}
    for seed_mask in range(1, 1 << m):
        distribution: dict[tuple[int, int], int] = {}
        for edge_mask in range(1 << m):
            reached = reached_from(seed_mask, edge_mask, m)
            open_edges = edge_mask.bit_count()
            key = (reached, open_edges)
            distribution[key] = distribution.get(key, 0) + 1
        counts[seed_mask] = distribution
    return counts


def submasks(mask: int) -> list[int]:
    output = []
    submask = mask
    while True:
        output.append(submask)
        if submask == 0:
            return output
        submask = (submask - 1) & mask


def transition_distribution(parent_mask: int, m: int, p: float) -> dict[int, float]:
    q = 1.0 - p
    parent_size = parent_mask.bit_count()
    distribution: dict[int, float] = {}
    reached_counts = edge_reached_counts(m)

    for seed_mask in submasks(parent_mask):
        if seed_mask == 0:
            continue
        seed_size = seed_mask.bit_count()
        seed_probability = (p**seed_size) * (q ** (parent_size - seed_size))
        for (child_mask, open_edges), count in reached_counts[seed_mask].items():
            probability = seed_probability * count * (p**open_edges) * (q ** (m - open_edges))
            distribution[child_mask] = distribution.get(child_mask, 0.0) + probability
    return distribution


SparseRows = list[list[tuple[int, float]]]


def mean_rows(m: int, p: float, forward_degree: int) -> tuple[list[int], SparseRows]:
    masks = list(range(1, 1 << m))
    index = {mask: i for i, mask in enumerate(masks)}
    rows: SparseRows = []

    for parent_mask in masks:
        row_entries: dict[int, float] = {}
        for child_mask, probability in transition_distribution(parent_mask, m, p).items():
            child_index = index[child_mask]
            row_entries[child_index] = row_entries.get(child_index, 0.0) + (
                forward_degree * probability
            )
        rows.append(list(row_entries.items()))
    return masks, rows


def perron_lower(rows: SparseRows, iterations: int) -> float:
    size = len(rows)
    vector = [1.0 / size for _ in range(size)]
    for _ in range(iterations):
        image = [sum(value * vector[col] for col, value in row) for row in rows]
        total = sum(image)
        if total == 0.0:
            return 0.0
        vector = [entry / total for entry in image]

    image = [sum(value * vector[col] for col, value in row) for row in rows]
    return min(image[row] / vector[row] for row in range(size) if vector[row] > 0.0)


def threshold(m: int, forward_degree: int, iterations: int) -> float:
    lo = 0.0
    hi = 0.5
    for _ in range(45):
        mid = (lo + hi) / 2.0
        _masks, rows = mean_rows(m, mid, forward_degree)
        if perron_lower(rows, iterations) > 1.0:
            hi = mid
        else:
            lo = mid
    return hi


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int)
    parser.add_argument("--max-m", type=int, default=6)
    parser.add_argument("--p", type=float)
    parser.add_argument("--forward-degree", type=int, default=2)
    parser.add_argument("--iterations", type=int, default=300)
    parser.add_argument("--thresholds", action="store_true")
    args = parser.parse_args()

    if args.thresholds:
        for m in range(3, args.max_m + 1):
            p = threshold(m, args.forward_degree, args.iterations)
            _masks, rows = mean_rows(m, p, args.forward_degree)
            lower = perron_lower(rows, args.iterations)
            print(
                f"m={m} types={(1 << m) - 1} threshold_upper={p:.12g} "
                f"inverse={1 / p:.12g} lower_at_threshold={lower:.12g}"
            )
        return

    if args.m is None or args.p is None:
        raise SystemExit("provide --m and --p, or use --thresholds")

    masks, rows = mean_rows(args.m, args.p, args.forward_degree)
    print(f"m={args.m}")
    print(f"types={len(masks)}")
    print(f"p={args.p:.12g}")
    print(f"forward_degree={args.forward_degree}")
    print(f"spectral_lower_float={perron_lower(rows, args.iterations):.12g}")
    row_sums = [sum(value for _col, value in row) for row in rows]
    print(
        "row_sum_range="
        f"[{min(row_sums):.12g}, {max(row_sums):.12g}]"
    )


if __name__ == "__main__":
    main()

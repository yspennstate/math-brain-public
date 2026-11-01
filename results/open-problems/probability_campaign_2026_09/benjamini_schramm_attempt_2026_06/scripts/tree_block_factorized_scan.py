"""Factorized depth-two tree-block scan for T_3 x Z.

For the two-generation lower process, only the mean matrix is needed.  This
script exploits that fact: from a parent type S, compute the full finite-window
distribution of the reached set R in a middle fiber, then compose with the
one-fiber distribution from R to a retained leaf type.  The mean contribution
is multiplied by four, the number of depth-two descendants in T_3.

This captures the depth-two advantage seen in Monte Carlo without keeping a
seven-fiber row-frontier state.  The current implementation is floating point;
the same factorization is suitable for a rational certificate at a fixed p.
"""

from __future__ import annotations

import argparse
from functools import lru_cache

from subset_branching_scan import mask_score, mask_span, type_masks


def normalize_mask(mask: int) -> int:
    return mask >> ((mask & -mask).bit_length() - 1)


def retained_type(reached_mask: int, type_width: int) -> int:
    best = 0
    submask = reached_mask
    while submask:
        if mask_span(submask) <= type_width:
            normalized = normalize_mask(submask)
            if mask_score(normalized) > mask_score(best):
                best = normalized
        submask = (submask - 1) & reached_mask
    return best


def component_masks(height_count: int, edge_mask: int) -> list[int]:
    components = []
    current = 1
    for height in range(height_count - 1):
        if (edge_mask >> height) & 1:
            current |= 1 << (height + 1)
        else:
            components.append(current)
            current = 1 << (height + 1)
    components.append(current)
    return components


def add_distribution(
    output: dict[int, float],
    mask: int,
    probability: float,
) -> None:
    output[mask] = output.get(mask, 0.0) + probability


@lru_cache(maxsize=None)
def reached_distribution(
    source_mask: int,
    height_count: int,
    p_key: int,
    scale: int,
) -> tuple[tuple[int, float], ...]:
    p = p_key / scale
    q = 1.0 - p
    distribution: dict[int, float] = {}
    edge_count = height_count - 1

    for edge_mask in range(1 << edge_count):
        open_edges = edge_mask.bit_count()
        edge_probability = (p ** open_edges) * (q ** (edge_count - open_edges))
        component_options: list[tuple[int, float]] = [(0, edge_probability)]

        for component in component_masks(height_count, edge_mask):
            source_count = (component & source_mask).bit_count()
            reached_probability = 0.0 if source_count == 0 else 1.0 - q ** source_count
            if reached_probability == 0.0:
                continue

            next_options = []
            for reached_mask, probability in component_options:
                next_options.append((reached_mask, probability * (1.0 - reached_probability)))
                next_options.append((reached_mask | component, probability * reached_probability))
            component_options = next_options

        for reached_mask, probability in component_options:
            add_distribution(distribution, reached_mask, probability)

    total = sum(distribution.values())
    if abs(total - 1.0) > 1e-9:
        raise ArithmeticError(f"distribution sums to {total}")
    return tuple(sorted(distribution.items()))


def retained_distribution(
    source_mask: int,
    height_count: int,
    type_width: int,
    p_key: int,
    scale: int,
) -> dict[int, float]:
    output: dict[int, float] = {}
    for reached_mask, probability in reached_distribution(
        source_mask, height_count, p_key, scale
    ):
        child = retained_type(reached_mask, type_width)
        if child:
            add_distribution(output, child, probability)
    return output


def mean_matrix(
    type_width: int,
    margin: int,
    p: float,
    scale: int,
) -> tuple[list[int], list[list[float]]]:
    p_key = round(p * scale)
    p = p_key / scale
    height_count = type_width + 1 + 2 * margin
    masks = type_masks(type_width)
    index = {mask: row for row, mask in enumerate(masks)}
    matrix = [[0.0] * len(masks) for _ in masks]

    leaf_cache: dict[int, dict[int, float]] = {}
    for row, parent in enumerate(masks):
        parent_source = parent << margin
        for middle_reached, middle_probability in reached_distribution(
            parent_source, height_count, p_key, scale
        ):
            if middle_reached not in leaf_cache:
                leaf_cache[middle_reached] = retained_distribution(
                    middle_reached, height_count, type_width, p_key, scale
                )
            for child, child_probability in leaf_cache[middle_reached].items():
                matrix[row][index[child]] += 4.0 * middle_probability * child_probability

    return masks, matrix


def perron_bounds(matrix: list[list[float]], iterations: int) -> tuple[float, float]:
    size = len(matrix)
    vector = [1.0 / size] * size
    for _ in range(iterations):
        image = [sum(matrix[row][col] * vector[col] for col in range(size)) for row in range(size)]
        total = sum(image)
        vector = [entry / total for entry in image]
    image = [sum(matrix[row][col] * vector[col] for col in range(size)) for row in range(size)]
    ratios = [image[row] / vector[row] for row in range(size)]
    return min(ratios), max(ratios)


def spectral_lower(
    type_width: int,
    margin: int,
    p: float,
    scale: int,
    iterations: int,
) -> float:
    _masks, matrix = mean_matrix(type_width, margin, p, scale)
    return perron_bounds(matrix, iterations)[0]


def find_threshold(
    type_width: int,
    margin: int,
    scale: int,
    iterations: int,
) -> float:
    lo = 0.0
    hi = 0.5
    for _ in range(45):
        mid = (lo + hi) / 2.0
        if spectral_lower(type_width, margin, mid, scale, iterations) > 1.0:
            hi = mid
        else:
            lo = mid
    return hi


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type-width", type=int, default=5)
    parser.add_argument("--margin", type=int, default=2)
    parser.add_argument("--p", type=float)
    parser.add_argument("--scale", type=int, default=10**12)
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--threshold", action="store_true")
    args = parser.parse_args()

    if args.threshold:
        threshold = find_threshold(
            args.type_width,
            args.margin,
            args.scale,
            args.iterations,
        )
        print(f"type_width={args.type_width}")
        print(f"types={len(type_masks(args.type_width))}")
        print(f"margin={args.margin}")
        print(f"threshold_upper={threshold:.12g}")
        print(
            "spectral_lower_at_threshold="
            f"{spectral_lower(args.type_width, args.margin, threshold, args.scale, args.iterations):.12g}"
        )
        return

    if args.p is None:
        raise SystemExit("--p is required unless --threshold is set")

    masks, matrix = mean_matrix(args.type_width, args.margin, args.p, args.scale)
    lower, upper = perron_bounds(matrix, args.iterations)
    print(f"type_width={args.type_width}")
    print(f"types={len(masks)}")
    print(f"margin={args.margin}")
    print(f"p={round(args.p * args.scale) / args.scale:.12g}")
    print(f"height_count={args.type_width + 1 + 2 * args.margin}")
    print(f"factorized_min_image_over_v={lower:.12g}")
    print(f"factorized_max_image_over_v={upper:.12g}")
    print(
        "row_sum_range="
        f"[{min(sum(row) for row in matrix):.12g}, {max(sum(row) for row in matrix):.12g}]"
    )
    if lower > 1.0:
        print("FLOAT-CERTIFIED-DIAGNOSTIC: factorized block mean has ratio > 1")
    else:
        print("NOT CERTIFIED: factorized block ratio is not > 1")


if __name__ == "__main__":
    main()

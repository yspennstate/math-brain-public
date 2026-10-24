"""Regenerative depth-two tree-block scan for T_3 x Z.

The state is a finite set of reached seed heights in a boundary fiber whose
vertical edges have not yet been exposed.  One block performs:

1. expose vertical edges in the root fiber and expand the seed set;
2. for each of two middle fibers, cross by horizontal edges and expose middle
   vertical edges;
3. for each of four boundary fibers, cross by horizontal edges but do not
   expose boundary vertical edges.

The retained boundary seed sets start independent copies of the same process,
so this is a regenerative finite-type lower-process diagnostic.  The current
implementation is floating point, but it uses exact finite sums over masks.
"""

from __future__ import annotations

import argparse
from functools import lru_cache

from subset_branching_scan import mask_score, mask_span, type_masks


def normalize_mask(mask: int) -> int:
    return mask >> ((mask & -mask).bit_length() - 1)


def retained_type(mask: int, type_width: int) -> int:
    best = 0
    submask = mask
    while submask:
        if mask_span(submask) <= type_width:
            normalized = normalize_mask(submask)
            if mask_score(normalized) > mask_score(best):
                best = normalized
        submask = (submask - 1) & mask
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


def add_distribution(output: dict[int, float], mask: int, probability: float) -> None:
    output[mask] = output.get(mask, 0.0) + probability


@lru_cache(maxsize=None)
def vertical_expand_distribution(
    seed_mask: int,
    height_count: int,
    p_key: int,
    scale: int,
) -> tuple[tuple[int, float], ...]:
    p = p_key / scale
    q = 1.0 - p
    edge_count = height_count - 1
    distribution: dict[int, float] = {}
    for edge_mask in range(1 << edge_count):
        reached = 0
        for component in component_masks(height_count, edge_mask):
            if component & seed_mask:
                reached |= component
        probability = p ** edge_mask.bit_count() * q ** (edge_count - edge_mask.bit_count())
        add_distribution(distribution, reached, probability)
    return tuple(sorted(distribution.items()))


@lru_cache(maxsize=None)
def horizontal_seed_distribution(
    source_mask: int,
    p_key: int,
    scale: int,
) -> tuple[tuple[int, float], ...]:
    p = p_key / scale
    q = 1.0 - p
    bits = [height for height in range(source_mask.bit_length()) if (source_mask >> height) & 1]
    distribution: dict[int, float] = {}
    for choice in range(1 << len(bits)):
        seed = 0
        open_count = choice.bit_count()
        for index, height in enumerate(bits):
            if (choice >> index) & 1:
                seed |= 1 << height
        probability = p ** open_count * q ** (len(bits) - open_count)
        add_distribution(distribution, seed, probability)
    return tuple(sorted(distribution.items()))


@lru_cache(maxsize=None)
def cross_and_expand_distribution(
    source_mask: int,
    height_count: int,
    p_key: int,
    scale: int,
) -> tuple[tuple[int, float], ...]:
    distribution: dict[int, float] = {}
    for seed_mask, seed_probability in horizontal_seed_distribution(source_mask, p_key, scale):
        if seed_mask == 0:
            add_distribution(distribution, 0, seed_probability)
            continue
        for reached, vertical_probability in vertical_expand_distribution(
            seed_mask, height_count, p_key, scale
        ):
            add_distribution(distribution, reached, seed_probability * vertical_probability)
    return tuple(sorted(distribution.items()))


def retained_seed_distribution(
    source_mask: int,
    type_width: int,
    p_key: int,
    scale: int,
) -> dict[int, float]:
    distribution: dict[int, float] = {}
    for seed_mask, probability in horizontal_seed_distribution(source_mask, p_key, scale):
        child = retained_type(seed_mask, type_width)
        if child:
            add_distribution(distribution, child, probability)
    return distribution


def mean_matrix(
    type_width: int,
    margin: int,
    p: float,
    scale: int,
) -> tuple[list[int], list[list[float]]]:
    p_key = round(p * scale)
    height_count = type_width + 1 + 2 * margin
    masks = type_masks(type_width)
    index = {mask: row for row, mask in enumerate(masks)}
    matrix = [[0.0] * len(masks) for _ in masks]
    leaf_cache: dict[int, dict[int, float]] = {}

    for row, parent in enumerate(masks):
        root_seed = parent << margin
        for root_reached, root_probability in vertical_expand_distribution(
            root_seed, height_count, p_key, scale
        ):
            for middle_reached, middle_probability in cross_and_expand_distribution(
                root_reached, height_count, p_key, scale
            ):
                if middle_reached not in leaf_cache:
                    leaf_cache[middle_reached] = retained_seed_distribution(
                        middle_reached, type_width, p_key, scale
                    )
                for child, child_probability in leaf_cache[middle_reached].items():
                    matrix[row][index[child]] += (
                        4.0 * root_probability * middle_probability * child_probability
                    )
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


def find_threshold(type_width: int, margin: int, scale: int, iterations: int) -> float:
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
        threshold = find_threshold(args.type_width, args.margin, args.scale, args.iterations)
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
    print(f"regenerative_min_image_over_v={lower:.12g}")
    print(f"regenerative_max_image_over_v={upper:.12g}")
    print(
        "row_sum_range="
        f"[{min(sum(row) for row in matrix):.12g}, {max(sum(row) for row in matrix):.12g}]"
    )
    if lower > 1.0:
        print("FLOAT-CERTIFIED-DIAGNOSTIC: regenerative block mean has ratio > 1")
    else:
        print("NOT CERTIFIED: regenerative block ratio is not > 1")


if __name__ == "__main__":
    main()

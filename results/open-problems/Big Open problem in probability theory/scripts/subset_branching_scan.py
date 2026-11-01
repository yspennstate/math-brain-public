"""Finite-subset branching scans for T_3 x Z.

This is a floating-point diagnostic for a richer lower process than the
one-interval process.  A type is a non-empty subset of {0,...,W} containing 0,
representing a reached vertical subset up to translation with span at most W.

Given a parent type S, a child fiber receives independent horizontal seeds on
the heights in S, then vertical percolation on Z expands those seeds into open
line components.  From the resulting reached child set, the lower process keeps
the densest reached subset lying in a window of span W, normalized by its
minimum.  This retained set is always a subset of the true reached set, so the
finite-type process is a legitimate lower-process diagnostic.  The script is
not an exact certificate.
"""

from __future__ import annotations

import argparse
from functools import lru_cache


def mask_span(mask: int) -> int:
    return mask.bit_length() - 1


def mask_score(mask: int) -> tuple[int, int, int]:
    if mask == 0:
        return (0, 0, 0)
    return (mask.bit_count(), mask_span(mask), mask)


def better_mask(first: int, second: int) -> int:
    return first if mask_score(first) >= mask_score(second) else second


def type_masks(width: int) -> list[int]:
    return [mask for mask in range(1, 1 << (width + 1)) if mask & 1]


def append_bit(
    best: int,
    recent: int,
    recent_len: int,
    bit: int,
    width: int,
) -> tuple[int, int, int]:
    max_len = width + 1
    if recent_len < max_len:
        recent |= bit << recent_len
        recent_len += 1
    else:
        recent = (recent >> 1) | (bit << width)

    if bit == 0:
        return best, recent, recent_len

    for suffix_len in range(1, recent_len + 1):
        suffix = (recent >> (recent_len - suffix_len)) & ((1 << suffix_len) - 1)
        if suffix == 0:
            continue
        first_one = (suffix & -suffix).bit_length() - 1
        candidate = suffix >> first_one
        best = better_mask(best, candidate)

    return best, recent, recent_len


@lru_cache(maxsize=None)
def append_run(
    best: int,
    recent: int,
    recent_len: int,
    bit: int,
    length: int,
    width: int,
) -> tuple[int, int, int]:
    for _ in range(length):
        best, recent, recent_len = append_bit(best, recent, recent_len, bit, width)
    return best, recent, recent_len


def add_state(
    output: dict[tuple[int, int, int, int, int], float],
    state: tuple[int, int, int, int, int],
    mass: float,
) -> None:
    output[state] = output.get(state, 0.0) + mass


def finalize_component(
    output: dict[tuple[int, int, int, int, int], float],
    best: int,
    recent: int,
    recent_len: int,
    comp_len: int,
    parent_count: int,
    mass: float,
    p: float,
    width: int,
) -> None:
    seed_probability = 0.0 if parent_count == 0 else 1.0 - (1.0 - p) ** parent_count

    if seed_probability:
        if comp_len >= width + 1:
            seeded_state = ((1 << (width + 1)) - 1, recent, recent_len, 0, 0)
        else:
            seeded_state = (*append_run(best, recent, recent_len, 1, comp_len, width), 0, 0)
        add_state(output, seeded_state, mass * seed_probability)

    unseeded_probability = 1.0 - seed_probability
    if unseeded_probability:
        unseeded_state = (*append_run(best, recent, recent_len, 0, comp_len, width), 0, 0)
        add_state(output, unseeded_state, mass * unseeded_probability)


def transition_probabilities(parent_mask: int, width: int, p: float) -> dict[int, float]:
    parent_span = mask_span(parent_mask)
    left = -width
    right = parent_span + width
    parent_sites = {site for site in range(parent_span + 1) if (parent_mask >> site) & 1}

    def is_parent_site(site: int) -> int:
        return 1 if site in parent_sites else 0

    # State entries are (best_mask, recent_bits, recent_len, component_len,
    # parent_sites_in_current_component).
    states: dict[tuple[int, int, int, int, int], float] = {
        (0, 0, 0, 1, is_parent_site(left)): 1.0
    }
    q = 1.0 - p

    for site in range(left, right):
        next_site = site + 1
        next_parent = is_parent_site(next_site)
        next_states: dict[tuple[int, int, int, int, int], float] = {}

        for (best, recent, recent_len, comp_len, parent_count), mass in states.items():
            open_state = (
                best,
                recent,
                recent_len,
                min(width + 1, comp_len + 1),
                min(width + 1, parent_count + next_parent),
            )
            add_state(next_states, open_state, mass * p)

            finalized: dict[tuple[int, int, int, int, int], float] = {}
            finalize_component(
                finalized,
                best,
                recent,
                recent_len,
                comp_len,
                parent_count,
                mass * q,
                p,
                width,
            )
            for final_state, final_mass in finalized.items():
                final_best, final_recent, final_recent_len, _zero_len, _zero_parent = final_state
                add_state(
                    next_states,
                    (final_best, final_recent, final_recent_len, 1, next_parent),
                    final_mass,
                )

        states = next_states

    distribution: dict[int, float] = {}
    for (best, recent, recent_len, comp_len, parent_count), mass in states.items():
        finalized: dict[tuple[int, int, int, int, int], float] = {}
        finalize_component(
            finalized,
            best,
            recent,
            recent_len,
            comp_len,
            parent_count,
            mass,
            p,
            width,
        )
        for (final_best, _recent, _recent_len, _zero_len, _zero_parent), final_mass in finalized.items():
            if final_best:
                distribution[final_best] = distribution.get(final_best, 0.0) + final_mass

    total = sum(distribution.values())
    extinction = max(0.0, 1.0 - total)
    if abs(total + extinction - 1.0) > 1e-8:
        raise ArithmeticError("transition probabilities do not sum to one")
    return distribution


def mean_matrix(width: int, p: float, forward_degree: int) -> tuple[list[int], list[list[float]]]:
    masks = type_masks(width)
    index = {mask: i for i, mask in enumerate(masks)}
    matrix = [[0.0] * len(masks) for _ in masks]

    for row, parent in enumerate(masks):
        distribution = transition_probabilities(parent, width, p)
        for child, probability in distribution.items():
            if child not in index:
                raise ArithmeticError(f"child mask {child:b} is not a type")
            matrix[row][index[child]] += forward_degree * probability

    return masks, matrix


def perron_lower(matrix: list[list[float]], iterations: int) -> float:
    size = len(matrix)
    vector = [1.0 / size] * size
    for _ in range(iterations):
        image = [sum(matrix[row][col] * vector[col] for col in range(size)) for row in range(size)]
        total = sum(image)
        vector = [entry / total for entry in image]
    image = [sum(matrix[row][col] * vector[col] for col in range(size)) for row in range(size)]
    return min(image[row] / vector[row] for row in range(size))


def spectral_lower(width: int, p: float, forward_degree: int, iterations: int) -> float:
    _masks, matrix = mean_matrix(width, p, forward_degree)
    return perron_lower(matrix, iterations)


def find_threshold(width: int, forward_degree: int, iterations: int) -> float:
    lo = 0.0
    hi = 0.5
    for _ in range(45):
        mid = (lo + hi) / 2.0
        if spectral_lower(width, mid, forward_degree, iterations) > 1.0:
            hi = mid
        else:
            lo = mid
    return hi


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=5)
    parser.add_argument("--p", type=float)
    parser.add_argument("--forward-degree", type=int, default=2)
    parser.add_argument("--iterations", type=int, default=800)
    parser.add_argument("--threshold", action="store_true")
    args = parser.parse_args()

    if args.threshold:
        threshold = find_threshold(args.width, args.forward_degree, args.iterations)
        print(f"width={args.width}")
        print(f"types={len(type_masks(args.width))}")
        print(f"threshold_upper={threshold:.12g}")
        print(
            "spectral_lower_at_threshold="
            f"{spectral_lower(args.width, threshold, args.forward_degree, args.iterations):.12g}"
        )
        return

    if args.p is None:
        raise SystemExit("--p is required unless --threshold is set")

    masks, matrix = mean_matrix(args.width, args.p, args.forward_degree)
    print(f"width={args.width}")
    print(f"types={len(masks)}")
    print(f"p={args.p:.12g}")
    print(f"forward_degree={args.forward_degree}")
    print(f"spectral_lower_float={perron_lower(matrix, args.iterations):.12g}")
    print(
        "row_sum_range="
        f"[{min(sum(row) for row in matrix):.12g}, {max(sum(row) for row in matrix):.12g}]"
    )


if __name__ == "__main__":
    main()

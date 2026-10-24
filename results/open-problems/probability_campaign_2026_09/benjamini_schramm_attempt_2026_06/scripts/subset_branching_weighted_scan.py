"""Weighted finite-subset branching scans for T_3 x Z.

This diagnostic strengthens subset_branching_scan.py.  For a positive weight
vector v on finite subset types, the retained child type is chosen to maximize
v among all reached subsets of span at most W.  If the resulting image satisfies

    2 E[max_T v_T] > v_S

for every parent type S, then the selector defined by v gives a finite-type
branching lower process with spectral radius larger than one.  The computation
here is floating-point only; it is a search tool for candidate certificates.
"""

from __future__ import annotations

import argparse

from subset_branching_scan import mask_score, mask_span, type_masks


def better_mask(first: int, second: int, weights: dict[int, float]) -> int:
    first_score = (weights.get(first, 0.0), *mask_score(first))
    second_score = (weights.get(second, 0.0), *mask_score(second))
    return first if first_score >= second_score else second


def append_bit(
    best: int,
    recent: int,
    recent_len: int,
    bit: int,
    width: int,
    weights: dict[int, float],
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
        best = better_mask(best, candidate, weights)

    return best, recent, recent_len


def append_run(
    best: int,
    recent: int,
    recent_len: int,
    bit: int,
    length: int,
    width: int,
    weights: dict[int, float],
) -> tuple[int, int, int]:
    for _ in range(length):
        best, recent, recent_len = append_bit(best, recent, recent_len, bit, width, weights)
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
    weights: dict[int, float],
) -> None:
    seed_probability = 0.0 if parent_count == 0 else 1.0 - (1.0 - p) ** parent_count
    full_mask = (1 << (width + 1)) - 1

    if seed_probability:
        if comp_len >= width + 1:
            seeded_best = better_mask(best, full_mask, weights)
            seeded_state = (seeded_best, recent, recent_len, 0, 0)
        else:
            seeded_state = (*append_run(best, recent, recent_len, 1, comp_len, width, weights), 0, 0)
        add_state(output, seeded_state, mass * seed_probability)

    unseeded_probability = 1.0 - seed_probability
    if unseeded_probability:
        unseeded_state = (*append_run(best, recent, recent_len, 0, comp_len, width, weights), 0, 0)
        add_state(output, unseeded_state, mass * unseeded_probability)


def expected_weight(parent_mask: int, width: int, p: float, weights: dict[int, float]) -> float:
    parent_span = mask_span(parent_mask)
    left = -width
    right = parent_span + width
    parent_sites = {site for site in range(parent_span + 1) if (parent_mask >> site) & 1}

    def is_parent_site(site: int) -> int:
        return 1 if site in parent_sites else 0

    states: dict[tuple[int, int, int, int, int], float] = {
        (0, 0, 0, 1, is_parent_site(left)): 1.0
    }
    q = 1.0 - p

    for site in range(left, right):
        next_site = site + 1
        next_parent = is_parent_site(next_site)
        next_states: dict[tuple[int, int, int, int, int], float] = {}

        for (best, recent, recent_len, comp_len, parent_count), mass in states.items():
            add_state(
                next_states,
                (
                    best,
                    recent,
                    recent_len,
                    min(width + 1, comp_len + 1),
                    min(width + 1, parent_count + next_parent),
                ),
                mass * p,
            )

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
                weights,
            )
            for final_state, final_mass in finalized.items():
                final_best, final_recent, final_recent_len, _zero_len, _zero_parent = final_state
                add_state(
                    next_states,
                    (final_best, final_recent, final_recent_len, 1, next_parent),
                    final_mass,
                )

        states = next_states

    total = 0.0
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
            weights,
        )
        for (final_best, _recent, _recent_len, _zero_len, _zero_parent), final_mass in finalized.items():
            total += final_mass * weights.get(final_best, 0.0)
    return total


def image_vector(
    masks: list[int],
    width: int,
    p: float,
    forward_degree: int,
    vector: list[float],
) -> list[float]:
    weights = {mask: vector[index] for index, mask in enumerate(masks)}
    return [
        forward_degree * expected_weight(parent, width, p, weights)
        for parent in masks
    ]


def nonlinear_power(
    width: int,
    p: float,
    forward_degree: int,
    iterations: int,
) -> tuple[list[int], list[float], float, float]:
    masks = type_masks(width)
    vector = [mask.bit_count() / sum(mask.bit_count() for mask in masks) for mask in masks]

    for _ in range(iterations):
        image = image_vector(masks, width, p, forward_degree, vector)
        total = sum(image)
        vector = [entry / total for entry in image]

    image = image_vector(masks, width, p, forward_degree, vector)
    ratios = [image[index] / vector[index] for index in range(len(masks))]
    return masks, vector, min(ratios), max(ratios)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=5)
    parser.add_argument("--p", type=float, required=True)
    parser.add_argument("--forward-degree", type=int, default=2)
    parser.add_argument("--iterations", type=int, default=30)
    args = parser.parse_args()

    masks, vector, min_ratio, max_ratio = nonlinear_power(
        args.width,
        args.p,
        args.forward_degree,
        args.iterations,
    )
    print(f"width={args.width}")
    print(f"types={len(masks)}")
    print(f"p={args.p:.12g}")
    print(f"iterations={args.iterations}")
    print(f"weighted_min_image_over_v={min_ratio:.12g}")
    print(f"weighted_max_image_over_v={max_ratio:.12g}")
    print(f"vector_sum={sum(vector):.12g}")
    if min_ratio > 1.0:
        print("FLOAT-CERTIFIED-DIAGNOSTIC: weighted selector has ratio > 1")
    else:
        print("NOT CERTIFIED: weighted selector ratio is not > 1")


if __name__ == "__main__":
    main()

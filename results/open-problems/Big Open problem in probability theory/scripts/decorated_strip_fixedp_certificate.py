"""Fixed-rational decorated-strip certificate for T_3 x Z.

This is a faster exact checker for the side-depth-one decorated strip at one
chosen rational p.  Unlike decorated_strip_bound.py, it does not keep the whole
polynomial in p for every transition.  It propagates integer numerators with a
common denominator p_den^(3h-2), then checks 2 M v > v exactly.
"""

from __future__ import annotations

import argparse
import time


LadderState = tuple[int, bool, bool, int, bool, int]


def initial_states(seed_mask: int, p_num: int, q_num: int) -> dict[LadderState, int]:
    root_seed = (seed_mask & 1) != 0
    return {
        (0, False, root_seed, 1, False, 0): q_num,
        (0, True, root_seed, 1, False, 0): p_num,
    }


def advance_state(
    state: LadderState,
    next_height: int,
    seed_mask: int,
    p_num: int,
    q_num: int,
) -> list[tuple[LadderState, int]]:
    output, same, root_seeded, root_mask, side_seeded, side_mask = state
    next_states: list[tuple[LadderState, int]] = []

    for edge_mask in range(8):
        parent = [0, 0 if same else 1, 2, 3]
        data = [
            (root_seeded, root_mask),
            (root_seeded, root_mask) if same else (side_seeded, side_mask),
            (((seed_mask >> next_height) & 1) != 0, 1 << next_height),
            (False, 0),
        ]

        def find(item: int) -> int:
            while parent[item] != item:
                parent[item] = parent[parent[item]]
                item = parent[item]
            return item

        def union(first: int, second: int) -> None:
            first_root = find(first)
            second_root = find(second)
            if first_root == second_root:
                return
            first_seeded, first_mask = data[first_root]
            second_seeded, second_mask = data[second_root]
            parent[second_root] = first_root
            data[first_root] = (
                first_seeded or second_seeded,
                first_mask | second_mask,
            )

        if edge_mask & 1:
            union(0, 2)  # old root to new root
        if edge_mask & 2:
            union(1, 3)  # old side to new side
        if edge_mask & 4:
            union(2, 3)  # new rung

        members: dict[int, list[int]] = {}
        for vertex in range(4):
            root = find(vertex)
            members.setdefault(root, []).append(vertex)

        next_output = output
        for root, component_vertices in members.items():
            if 2 not in component_vertices and 3 not in component_vertices:
                seeded, mask = data[find(root)]
                if seeded:
                    next_output |= mask

        root_component = find(2)
        side_component = find(3)
        root_data = data[root_component]
        open_count = edge_mask.bit_count()
        weight = (p_num**open_count) * (q_num ** (3 - open_count))

        if root_component == side_component:
            next_states.append(
                (
                    (
                        next_output,
                        True,
                        root_data[0],
                        root_data[1],
                        False,
                        0,
                    ),
                    weight,
                )
            )
        else:
            side_data = data[side_component]
            next_states.append(
                (
                    (
                        next_output,
                        False,
                        root_data[0],
                        root_data[1],
                        side_data[0],
                        side_data[1],
                    ),
                    weight,
                )
            )

    return next_states


def closure_numerators(
    height_count: int,
    p_num: int,
    p_den: int,
    show_progress: bool,
) -> tuple[list[dict[int, int]], int]:
    q_num = p_den - p_num
    state_count = 1 << height_count
    closures: list[dict[int, int]] = []
    advance_cache: dict[tuple[LadderState, int, bool], list[tuple[LadderState, int]]] = {}
    start = time.time()

    for seed_mask in range(state_count):
        states = initial_states(seed_mask, p_num, q_num)
        for next_height in range(1, height_count):
            next_states: dict[LadderState, int] = {}
            for state, mass in states.items():
                next_seeded = bool((seed_mask >> next_height) & 1)
                cache_key = (state, next_height, next_seeded)
                if cache_key not in advance_cache:
                    synthetic_seed = (1 << next_height) if next_seeded else 0
                    advance_cache[cache_key] = advance_state(
                        state, next_height, synthetic_seed, p_num, q_num
                    )
                for advanced, weight in advance_cache[cache_key]:
                    next_states[advanced] = next_states.get(advanced, 0) + mass * weight
            states = next_states

        seed_closure: dict[int, int] = {}
        for state, mass in states.items():
            output, same, root_seeded, root_mask, side_seeded, side_mask = state
            if root_seeded:
                output |= root_mask
            if not same and side_seeded:
                output |= side_mask
            seed_closure[output] = seed_closure.get(output, 0) + mass
        closures.append(seed_closure)

        if show_progress and seed_mask % 128 == 0:
            print(
                f"seed_masks={seed_mask}/{state_count} states={len(states)} "
                f"outputs={len(seed_closure)} elapsed={time.time() - start:.3f}",
                flush=True,
            )

    return closures, 3 * height_count - 2


def apply_float(
    closures: list[dict[int, int]],
    closure_denominator: int,
    height_count: int,
    p_num: int,
    p_den: int,
    vector: list[float],
) -> list[float]:
    state_count = 1 << height_count
    p = p_num / p_den
    q = 1.0 - p
    seed_values = [0.0] * state_count
    for seed, seed_closure in enumerate(closures):
        total = 0.0
        for output, numerator in seed_closure.items():
            if output:
                total += (numerator / closure_denominator) * vector[output - 1]
        seed_values[seed] = total

    ratio = p / q
    weighted = [
        seed_values[seed] * (ratio ** seed.bit_count())
        for seed in range(state_count)
    ]
    for bit in range(height_count):
        step = 1 << bit
        for mask in range(state_count):
            if mask & step:
                weighted[mask] += weighted[mask ^ step]

    return [
        (q ** current.bit_count()) * weighted[current]
        for current in range(1, state_count)
    ]


def right_perron_vector(
    closures: list[dict[int, int]],
    closure_denominator: int,
    height_count: int,
    p_num: int,
    p_den: int,
    iterations: int,
) -> tuple[list[float], float]:
    size = (1 << height_count) - 1
    vector = [1.0 / size] * size
    for _ in range(iterations):
        image = apply_float(
            closures, closure_denominator, height_count, p_num, p_den, vector
        )
        total = sum(image)
        vector = [entry / total for entry in image]

    image = apply_float(closures, closure_denominator, height_count, p_num, p_den, vector)
    min_ratio = min(image[row] / vector[row] for row in range(size))
    return vector, min_ratio


def exact_certificate_check(
    closures: list[dict[int, int]],
    edge_count: int,
    height_count: int,
    p_num: int,
    p_den: int,
    vector: list[int],
) -> tuple[bool, float, float, int]:
    state_count = 1 << height_count
    q_num = p_den - p_num

    pow_p = [1] * (height_count + 1)
    pow_q = [1] * (height_count + 1)
    pow_den = [1] * (edge_count + height_count + 1)
    for i in range(1, height_count + 1):
        pow_p[i] = pow_p[i - 1] * p_num
        pow_q[i] = pow_q[i - 1] * q_num
    for i in range(1, edge_count + height_count + 1):
        pow_den[i] = pow_den[i - 1] * p_den

    seed_values = [0] * state_count
    for seed, seed_closure in enumerate(closures):
        total = 0
        for output, closure_num in seed_closure.items():
            if output:
                total += closure_num * vector[output - 1]
        seed_values[seed] = total

    min_margin: int | None = None
    min_ratio = float("inf")
    max_ratio = 0.0

    for current in range(1, state_count):
        current_size = current.bit_count()
        numerator = 0
        seed = current
        while True:
            seed_size = seed.bit_count()
            numerator += (
                pow_p[seed_size]
                * pow_q[current_size - seed_size]
                * seed_values[seed]
            )
            if seed == 0:
                break
            seed = (seed - 1) & current

        denominator = pow_den[edge_count + current_size]
        margin = 2 * numerator - denominator * vector[current - 1]
        min_margin = margin if min_margin is None else min(min_margin, margin)
        ratio = (2 * numerator) / (denominator * vector[current - 1])
        min_ratio = min(min_ratio, ratio)
        max_ratio = max(max_ratio, ratio)

    assert min_margin is not None
    return min_margin > 0, min_ratio, max_ratio, min_margin


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--height-count", type=int, default=11)
    parser.add_argument("--p-num", type=int, default=589)
    parser.add_argument("--p-den", type=int, default=2000)
    parser.add_argument("--scale", type=int, default=100_000_000)
    parser.add_argument("--iterations", type=int, default=800)
    parser.add_argument("--progress", action="store_true")
    args = parser.parse_args()

    start = time.time()
    closures, edge_count = closure_numerators(
        args.height_count, args.p_num, args.p_den, args.progress
    )
    closure_denominator = args.p_den**edge_count
    vector_float, spectral_lower = right_perron_vector(
        closures,
        closure_denominator,
        args.height_count,
        args.p_num,
        args.p_den,
        args.iterations,
    )
    vector = [max(1, round(entry * args.scale)) for entry in vector_float]
    certified, min_ratio, max_ratio, min_margin = exact_certificate_check(
        closures,
        edge_count,
        args.height_count,
        args.p_num,
        args.p_den,
        vector,
    )

    print(f"height_count={args.height_count}")
    print("side_depth=1")
    print(f"edge_count={edge_count}")
    print(f"p={args.p_num}/{args.p_den}={args.p_num / args.p_den:.12g}")
    print(f"matrix_size={(1 << args.height_count) - 1}")
    print("mode=fixed-rational")
    print(f"float_spectral_radius_lower={spectral_lower:.12g}")
    print(f"certificate_scale={args.scale}")
    print(f"certificate_vector_sum={sum(vector)}")
    print(f"certificate_min_2Mv_over_v={min_ratio:.12g}")
    print(f"certificate_max_2Mv_over_v={max_ratio:.12g}")
    print(f"certificate_min_integer_margin={min_margin}")
    print(f"elapsed_seconds={time.time() - start:.3f}")
    if certified:
        print("CERTIFIED: spectral_radius > 1/2")
    else:
        print("NOT CERTIFIED: this vector does not prove spectral_radius > 1/2")


if __name__ == "__main__":
    main()

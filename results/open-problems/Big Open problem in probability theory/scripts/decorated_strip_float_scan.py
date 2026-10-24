"""Floating-point decorated-strip scans for pc(T_3 x Z).

This is a diagnostic companion to decorated_strip_bound.py.  It uses the same
row-frontier connectivity state, but accumulates probabilities at a fixed
floating-point p instead of exact counts by open-edge number.  The result is
not a certificate; it is a fast way to find finite decorated strips worth
rerunning with the exact rational checker.
"""

from __future__ import annotations

import argparse
import time

from decorated_strip_bound import DataDSU, side_tree_row_edges


FrontierState = tuple[int, tuple[int, ...], tuple[tuple[bool, int], ...]]
LadderState = tuple[int, bool, bool, int, bool, int]


def initial_ladder_states(seed_mask: int, p: float) -> dict[LadderState, float]:
    root_seed = (seed_mask & 1) != 0
    q = 1.0 - p
    return {
        (0, False, root_seed, 1, False, 0): q,
        (0, True, root_seed, 1, False, 0): p,
    }


def advance_ladder_state(
    state: LadderState,
    next_height: int,
    seed_mask: int,
    p: float,
) -> list[tuple[LadderState, float]]:
    output, same, root_seeded, root_mask, side_seeded, side_mask = state
    next_states: list[tuple[LadderState, float]] = []
    q = 1.0 - p

    for edge_mask in range(8):
        # Temporary vertices are old root, old side, new root, new side.
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
        probability = (p ** edge_mask.bit_count()) * (q ** (3 - edge_mask.bit_count()))

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
                    probability,
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
                    probability,
                )
            )

    return next_states


def ladder_closure_probabilities(
    height_count: int,
    p: float,
    show_progress: bool,
) -> list[dict[int, float]]:
    state_count = 1 << height_count
    closures: list[dict[int, float]] = []
    advance_cache: dict[
        tuple[LadderState, int, bool], list[tuple[LadderState, float]]
    ] = {}
    start = time.time()

    for seed_mask in range(state_count):
        states = initial_ladder_states(seed_mask, p)
        for next_height in range(1, height_count):
            next_states: dict[LadderState, float] = {}
            for state, mass in states.items():
                next_seeded = bool((seed_mask >> next_height) & 1)
                cache_key = (state, next_height, next_seeded)
                if cache_key not in advance_cache:
                    synthetic_seed = (1 << next_height) if next_seeded else 0
                    advance_cache[cache_key] = advance_ladder_state(
                        state, next_height, synthetic_seed, p
                    )
                for advanced, probability in advance_cache[cache_key]:
                    next_states[advanced] = (
                        next_states.get(advanced, 0.0) + mass * probability
                    )
            states = next_states

        seed_closure: dict[int, float] = {}
        for state, mass in states.items():
            output, same, root_seeded, root_mask, side_seeded, side_mask = state
            if root_seeded:
                output |= root_mask
            if not same and side_seeded:
                output |= side_mask
            seed_closure[output] = seed_closure.get(output, 0.0) + mass
        closures.append(seed_closure)

        if show_progress and seed_mask % 128 == 0:
            print(
                f"seed_masks={seed_mask}/{state_count} states={len(states)} "
                f"outputs={len(seed_closure)} elapsed={time.time() - start:.3f}",
                flush=True,
            )

    return closures


def canonical_state(
    output: int,
    labels: list[int],
    component_data: dict[int, tuple[bool, int]],
) -> FrontierState:
    label_map: dict[int, int] = {}
    next_label = 0
    canonical_labels = []
    canonical_data: list[tuple[bool, int]] = []
    for label in labels:
        if label not in label_map:
            label_map[label] = next_label
            canonical_data.append(component_data[label])
            next_label += 1
        canonical_labels.append(label_map[label])
    return output, tuple(canonical_labels), tuple(canonical_data)


def initial_states(
    seed_mask: int,
    width: int,
    row_edges: list[tuple[int, int]],
    p: float,
) -> dict[FrontierState, float]:
    states: dict[FrontierState, float] = {}
    q = 1.0 - p
    edge_options = 1 << len(row_edges)
    for edge_mask in range(edge_options):
        seeded = [False] * width
        root_masks = [0] * width
        seeded[0] = bool(seed_mask & 1)
        root_masks[0] = 1
        dsu = DataDSU(seeded, root_masks)
        for edge_index, (first, second) in enumerate(row_edges):
            if (edge_mask >> edge_index) & 1:
                dsu.union(first, second)

        labels = [dsu.find(vertex) for vertex in range(width)]
        component_data = {
            label: (dsu.seeded[label], dsu.root_masks[label]) for label in set(labels)
        }
        state = canonical_state(0, labels, component_data)
        probability = p ** edge_mask.bit_count() * q ** (
            len(row_edges) - edge_mask.bit_count()
        )
        states[state] = states.get(state, 0.0) + probability
    return states


def advance_state(
    state: FrontierState,
    next_height: int,
    seed_mask: int,
    width: int,
    row_edges: list[tuple[int, int]],
    p: float,
) -> list[tuple[FrontierState, float]]:
    output, old_labels, old_data = state
    next_states: list[tuple[FrontierState, float]] = []
    q = 1.0 - p
    edge_count = width + len(row_edges)
    edge_options = 1 << edge_count

    for edge_mask in range(edge_options):
        seeded = [False] * (2 * width)
        root_masks = [0] * (2 * width)

        for vertex, label in enumerate(old_labels):
            seeded[vertex], root_masks[vertex] = old_data[label]

        seeded[width] = bool((seed_mask >> next_height) & 1)
        root_masks[width] = 1 << next_height

        dsu = DataDSU(seeded, root_masks)

        representatives: dict[int, int] = {}
        for vertex, label in enumerate(old_labels):
            if label in representatives:
                dsu.union(representatives[label], vertex)
            else:
                representatives[label] = vertex

        for vertex in range(width):
            if (edge_mask >> vertex) & 1:
                dsu.union(vertex, width + vertex)

        row_edge_mask = edge_mask >> width
        for edge_index, (first, second) in enumerate(row_edges):
            if (row_edge_mask >> edge_index) & 1:
                dsu.union(width + first, width + second)

        new_roots = {dsu.find(width + vertex) for vertex in range(width)}
        next_output = output
        for root in {dsu.find(vertex) for vertex in range(2 * width)} - new_roots:
            if dsu.seeded[root]:
                next_output |= dsu.root_masks[root]

        labels = [dsu.find(width + vertex) for vertex in range(width)]
        component_data = {
            label: (dsu.seeded[label], dsu.root_masks[label]) for label in set(labels)
        }
        next_state = canonical_state(next_output, labels, component_data)
        probability = p ** edge_mask.bit_count() * q ** (edge_count - edge_mask.bit_count())
        next_states.append((next_state, probability))

    return next_states


def closure_probabilities(
    height_count: int,
    side_depth: int,
    p: float,
    show_progress: bool,
) -> list[dict[int, float]]:
    width, row_edges = side_tree_row_edges(side_depth)
    state_count = 1 << height_count
    closures: list[dict[int, float]] = []
    start = time.time()

    for seed_mask in range(state_count):
        states = initial_states(seed_mask, width, row_edges, p)
        for next_height in range(1, height_count):
            next_states: dict[FrontierState, float] = {}
            for state, mass in states.items():
                for advanced, probability in advance_state(
                    state, next_height, seed_mask, width, row_edges, p
                ):
                    next_states[advanced] = next_states.get(advanced, 0.0) + mass * probability
            states = next_states

        seed_closure: dict[int, float] = {}
        for state, mass in states.items():
            output, _labels, component_data = state
            final_output = output
            for seeded, root_mask in component_data:
                if seeded:
                    final_output |= root_mask
            seed_closure[final_output] = seed_closure.get(final_output, 0.0) + mass
        closures.append(seed_closure)

        if show_progress and seed_mask % 32 == 0:
            print(
                f"seed_masks={seed_mask}/{state_count} states={len(states)} "
                f"outputs={len(seed_closure)} elapsed={time.time() - start:.3f}",
                flush=True,
            )

    return closures


def apply_matrix(
    closures: list[dict[int, float]],
    height_count: int,
    p: float,
    vector: list[float],
) -> list[float]:
    state_count = 1 << height_count
    q = 1.0 - p

    seed_values = [0.0] * state_count
    for seed, seed_closure in enumerate(closures):
        seed_values[seed] = sum(
            probability * vector[output - 1]
            for output, probability in seed_closure.items()
            if output
        )

    if q == 0.0:
        return [seed_values[current] for current in range(1, state_count)]

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


def perron_lower(
    closures: list[dict[int, float]],
    height_count: int,
    p: float,
    iterations: int,
) -> float:
    size = (1 << height_count) - 1
    vector = [1.0 / size] * size
    for _ in range(iterations):
        image = apply_matrix(closures, height_count, p, vector)
        total = sum(image)
        vector = [entry / total for entry in image]

    image = apply_matrix(closures, height_count, p, vector)
    return min(image[row] / vector[row] for row in range(size))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--height-count", type=int, default=6)
    parser.add_argument("--side-depth", type=int, default=2)
    parser.add_argument("--p", type=float, default=0.3)
    parser.add_argument("--iterations", type=int, default=800)
    parser.add_argument("--progress", action="store_true")
    args = parser.parse_args()

    start = time.time()
    if args.side_depth == 1:
        closures = ladder_closure_probabilities(args.height_count, args.p, args.progress)
    else:
        closures = closure_probabilities(
            args.height_count, args.side_depth, args.p, args.progress
        )
    spectral_lower = perron_lower(
        closures, args.height_count, args.p, args.iterations
    )
    print(f"height_count={args.height_count}")
    print(f"side_depth={args.side_depth}")
    print(f"p={args.p:.12g}")
    print(f"matrix_size={(1 << args.height_count) - 1}")
    print(f"float_spectral_radius_lower={spectral_lower:.12g}")
    print(f"elapsed_seconds={time.time() - start:.3f}")


if __name__ == "__main__":
    main()

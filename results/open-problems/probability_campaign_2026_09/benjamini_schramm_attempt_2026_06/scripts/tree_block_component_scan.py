"""Deterministic component-selector tree-block scans for T_3 x Z.

This is a conservative finite tree-block lower process.  It exposes a finite
forward binary tree of vertical fibers, but in each boundary fiber it keeps
only the best single reached connected component of bounded span.  This is
weaker than keeping the best subset of the union of all reached boundary
components, but it gives a tractable row-frontier transfer and remains a
valid lower process.
"""

from __future__ import annotations

import argparse

from subset_branching_scan import mask_score, mask_span, type_masks


ComponentData = tuple[bool, tuple[int, ...]]
State = tuple[tuple[int, ...], tuple[int, ...], tuple[ComponentData, ...]]


def tree_edges(depth: int) -> tuple[int, list[tuple[int, int]], list[int]]:
    node_count = (1 << (depth + 1)) - 1
    edges = []
    for parent in range((1 << depth) - 1):
        edges.append((parent, 2 * parent + 1))
        edges.append((parent, 2 * parent + 2))
    boundary = list(range((1 << depth) - 1, node_count))
    return node_count, edges, boundary


class DSU:
    def __init__(self, seeded: list[bool], boundary_masks: list[list[int]]) -> None:
        self.parent = list(range(len(seeded)))
        self.rank = [0] * len(seeded)
        self.seeded = seeded[:]
        self.boundary_masks = [masks[:] for masks in boundary_masks]

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, first: int, second: int) -> None:
        first_root = self.find(first)
        second_root = self.find(second)
        if first_root == second_root:
            return
        if self.rank[first_root] < self.rank[second_root]:
            first_root, second_root = second_root, first_root
        self.parent[second_root] = first_root
        self.seeded[first_root] = self.seeded[first_root] or self.seeded[second_root]
        for index, mask in enumerate(self.boundary_masks[second_root]):
            self.boundary_masks[first_root][index] |= mask
        if self.rank[first_root] == self.rank[second_root]:
            self.rank[first_root] += 1


def normalize_mask(mask: int) -> int:
    return mask >> ((mask & -mask).bit_length() - 1)


def best_component_type(mask: int, type_width: int) -> int:
    if mask == 0:
        return 0
    if mask_span(mask) <= type_width:
        return normalize_mask(mask)
    best = 0
    submask = mask
    while submask:
        if mask_span(submask) <= type_width:
            normalized = normalize_mask(submask)
            if mask_score(normalized) > mask_score(best):
                best = normalized
        submask = (submask - 1) & mask
    return best


def better_type(first: int, second: int, weights: dict[int, float]) -> int:
    first_score = (weights.get(first, 0.0), *mask_score(first))
    second_score = (weights.get(second, 0.0), *mask_score(second))
    return first if first_score >= second_score else second


def close_component(
    outputs: list[int],
    seeded: bool,
    boundary_masks: tuple[int, ...],
    type_width: int,
    weights: dict[int, float],
) -> None:
    if not seeded:
        return
    for index, mask in enumerate(boundary_masks):
        child_type = best_component_type(mask, type_width)
        if child_type:
            outputs[index] = better_type(outputs[index], child_type, weights)


def canonical_state(
    outputs: tuple[int, ...],
    labels: list[int],
    data: dict[int, ComponentData],
) -> State:
    label_map: dict[int, int] = {}
    next_label = 0
    canonical_labels = []
    canonical_data: list[ComponentData] = []
    for label in labels:
        if label not in label_map:
            label_map[label] = next_label
            canonical_data.append(data[label])
            next_label += 1
        canonical_labels.append(label_map[label])
    return outputs, tuple(canonical_labels), tuple(canonical_data)


def add_state(states: dict[State, float], state: State, mass: float) -> None:
    states[state] = states.get(state, 0.0) + mass


def initial_states(
    parent_mask: int,
    margin: int,
    block_depth: int,
    p: float,
) -> dict[State, float]:
    node_count, row_edges, boundary = tree_edges(block_depth)
    boundary_index = {node: index for index, node in enumerate(boundary)}
    boundary_count = len(boundary)
    seed_mask = parent_mask << margin
    q = 1.0 - p
    states: dict[State, float] = {}

    for edge_mask in range(1 << len(row_edges)):
        seeded = [False] * node_count
        boundary_masks = [[0] * boundary_count for _ in range(node_count)]
        seeded[0] = bool(seed_mask & 1)
        for node in boundary:
            boundary_masks[node][boundary_index[node]] = 1

        dsu = DSU(seeded, boundary_masks)
        for edge_index, (first, second) in enumerate(row_edges):
            if (edge_mask >> edge_index) & 1:
                dsu.union(first, second)

        labels = [dsu.find(node) for node in range(node_count)]
        data = {
            label: (dsu.seeded[label], tuple(dsu.boundary_masks[label]))
            for label in set(labels)
        }
        probability = p ** edge_mask.bit_count() * q ** (
            len(row_edges) - edge_mask.bit_count()
        )
        add_state(
            states,
            canonical_state(tuple([0] * boundary_count), labels, data),
            probability,
        )
    return states


def advance_state(
    state: State,
    height: int,
    parent_mask: int,
    margin: int,
    block_depth: int,
    p: float,
    type_width: int,
    weights: dict[int, float],
) -> list[tuple[State, float]]:
    old_outputs, old_labels, old_data = state
    node_count, row_edges, boundary = tree_edges(block_depth)
    boundary_index = {node: index for index, node in enumerate(boundary)}
    boundary_count = len(boundary)
    seed_mask = parent_mask << margin
    q = 1.0 - p

    edge_count = node_count + len(row_edges)
    next_states: list[tuple[State, float]] = []
    for edge_mask in range(1 << edge_count):
        seeded = [False] * (2 * node_count)
        boundary_masks = [[0] * boundary_count for _ in range(2 * node_count)]

        for node, label in enumerate(old_labels):
            old_seeded, old_boundary_masks = old_data[label]
            seeded[node] = old_seeded
            boundary_masks[node] = list(old_boundary_masks)

        seeded[node_count] = bool((seed_mask >> height) & 1)
        for node in boundary:
            boundary_masks[node_count + node][boundary_index[node]] = 1 << height

        dsu = DSU(seeded, boundary_masks)

        representatives: dict[int, int] = {}
        for node, label in enumerate(old_labels):
            if label in representatives:
                dsu.union(representatives[label], node)
            else:
                representatives[label] = node

        for node in range(node_count):
            if (edge_mask >> node) & 1:
                dsu.union(node, node_count + node)

        row_edge_mask = edge_mask >> node_count
        for edge_index, (first, second) in enumerate(row_edges):
            if (row_edge_mask >> edge_index) & 1:
                dsu.union(node_count + first, node_count + second)

        new_roots = {dsu.find(node_count + node) for node in range(node_count)}
        outputs = list(old_outputs)
        for root in {dsu.find(node) for node in range(2 * node_count)} - new_roots:
            close_component(
                outputs,
                dsu.seeded[root],
                tuple(dsu.boundary_masks[root]),
                type_width,
                weights,
            )

        labels = [dsu.find(node_count + node) for node in range(node_count)]
        data = {
            label: (dsu.seeded[label], tuple(dsu.boundary_masks[label]))
            for label in set(labels)
        }
        probability = p ** edge_mask.bit_count() * q ** (edge_count - edge_mask.bit_count())
        next_states.append((canonical_state(tuple(outputs), labels, data), probability))

    return next_states


def expected_weight(
    parent_mask: int,
    type_width: int,
    margin: int,
    block_depth: int,
    p: float,
    weights: dict[int, float],
) -> float:
    height_count = type_width + 1 + 2 * margin
    states = initial_states(parent_mask, margin, block_depth, p)
    for height in range(1, height_count):
        next_states: dict[State, float] = {}
        for state, mass in states.items():
            for advanced, probability in advance_state(
                state, height, parent_mask, margin, block_depth, p, type_width, weights
            ):
                add_state(next_states, advanced, mass * probability)
        states = next_states

    total = 0.0
    for state, mass in states.items():
        outputs, _labels, component_data = state
        final_outputs = list(outputs)
        for seeded, boundary_masks in component_data:
            close_component(final_outputs, seeded, boundary_masks, type_width, weights)
        total += mass * sum(weights.get(child, 0.0) for child in final_outputs)
    return total


def image_vector(
    masks: list[int],
    type_width: int,
    margin: int,
    block_depth: int,
    p: float,
    vector: list[float],
) -> list[float]:
    weights = {mask: vector[index] for index, mask in enumerate(masks)}
    return [
        expected_weight(parent, type_width, margin, block_depth, p, weights)
        for parent in masks
    ]


def nonlinear_power(
    type_width: int,
    margin: int,
    block_depth: int,
    p: float,
    iterations: int,
) -> tuple[list[int], float, float]:
    masks = type_masks(type_width)
    denominator = sum(mask.bit_count() for mask in masks)
    vector = [mask.bit_count() / denominator for mask in masks]

    for _ in range(iterations):
        image = image_vector(masks, type_width, margin, block_depth, p, vector)
        total = sum(image)
        vector = [entry / total for entry in image]

    image = image_vector(masks, type_width, margin, block_depth, p, vector)
    ratios = [image[index] / vector[index] for index in range(len(masks))]
    return masks, min(ratios), max(ratios)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type-width", type=int, default=2)
    parser.add_argument("--margin", type=int, default=0)
    parser.add_argument("--block-depth", type=int, default=2)
    parser.add_argument("--p", type=float, required=True)
    parser.add_argument("--iterations", type=int, default=5)
    args = parser.parse_args()

    masks, min_ratio, max_ratio = nonlinear_power(
        args.type_width,
        args.margin,
        args.block_depth,
        args.p,
        args.iterations,
    )
    print(f"type_width={args.type_width}")
    print(f"types={len(masks)}")
    print(f"margin={args.margin}")
    print(f"block_depth={args.block_depth}")
    print(f"p={args.p:.12g}")
    print(f"component_min_image_over_v={min_ratio:.12g}")
    print(f"component_max_image_over_v={max_ratio:.12g}")
    if min_ratio > 1.0:
        print("FLOAT-CERTIFIED-DIAGNOSTIC: component selector has ratio > 1")
    else:
        print("NOT CERTIFIED: component selector ratio is not > 1")


if __name__ == "__main__":
    main()

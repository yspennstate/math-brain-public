"""Finite tree-block branching scans for T_3 x Z.

This diagnostic exposes a finite forward binary tree of vertical fibers at
once.  A parent type is a finite vertical subset.  After percolation is exposed
in a depth-L forward tree block, each boundary fiber contributes the best
retained reached subset of bounded span.  If a positive test vector v satisfies

    E[sum_boundary max_T v_T] > v_parent

for every parent type, the associated selector gives a finite-type
Galton-Watson lower process with mean operator larger than one.

The computation is floating point and intended to find promising finite
certificates, not as a final exact proof.
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


def add_state(states: dict[State, float], state: State, mass: float) -> None:
    states[state] = states.get(state, 0.0) + mass


def initial_states(
    parent_mask: int,
    type_width: int,
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
            if dsu.seeded[root]:
                for index, mask in enumerate(dsu.boundary_masks[root]):
                    outputs[index] |= mask

        labels = [dsu.find(node_count + node) for node in range(node_count)]
        data = {
            label: (dsu.seeded[label], tuple(dsu.boundary_masks[label]))
            for label in set(labels)
        }
        probability = p ** edge_mask.bit_count() * q ** (edge_count - edge_mask.bit_count())
        next_states.append((canonical_state(tuple(outputs), labels, data), probability))

    return next_states


def final_outputs(
    parent_mask: int,
    type_width: int,
    margin: int,
    block_depth: int,
    p: float,
) -> dict[tuple[int, ...], float]:
    height_count = type_width + 1 + 2 * margin
    states = initial_states(parent_mask, type_width, margin, block_depth, p)
    for height in range(1, height_count):
        next_states: dict[State, float] = {}
        for state, mass in states.items():
            for advanced, probability in advance_state(
                state, height, parent_mask, margin, block_depth, p
            ):
                add_state(next_states, advanced, mass * probability)
        states = next_states

    output_distribution: dict[tuple[int, ...], float] = {}
    for state, mass in states.items():
        outputs, _labels, component_data = state
        final = list(outputs)
        for seeded, boundary_masks in component_data:
            if seeded:
                for index, mask in enumerate(boundary_masks):
                    final[index] |= mask
        final_tuple = tuple(final)
        output_distribution[final_tuple] = output_distribution.get(final_tuple, 0.0) + mass
    return output_distribution


def best_weight(mask: int, type_width: int, weights: dict[int, float]) -> float:
    best = 0.0
    submask = mask
    while submask:
        span = mask_span(submask)
        if span <= type_width:
            normalized = submask >> ((submask & -submask).bit_length() - 1)
            best = max(best, weights.get(normalized, 0.0))
        submask = (submask - 1) & mask
    return best


def image_vector(
    type_width: int,
    margin: int,
    masks: list[int],
    vector: list[float],
    distributions: list[dict[tuple[int, ...], float]],
) -> list[float]:
    weights = {mask: vector[index] for index, mask in enumerate(masks)}
    image = []
    for distribution in distributions:
        total = 0.0
        for outputs, probability in distribution.items():
            total += probability * sum(
                best_weight(mask, type_width, weights) for mask in outputs
            )
        image.append(total)
    return image


def nonlinear_power(
    type_width: int,
    margin: int,
    block_depth: int,
    p: float,
    iterations: int,
) -> tuple[list[int], float, float]:
    masks = type_masks(type_width)
    distributions = [
        final_outputs(parent, type_width, margin, block_depth, p)
        for parent in masks
    ]
    denominator = sum(mask.bit_count() for mask in masks)
    vector = [mask.bit_count() / denominator for mask in masks]

    for _ in range(iterations):
        image = image_vector(type_width, margin, masks, vector, distributions)
        total = sum(image)
        vector = [entry / total for entry in image]

    image = image_vector(type_width, margin, masks, vector, distributions)
    ratios = [image[index] / vector[index] for index in range(len(masks))]
    return masks, min(ratios), max(ratios)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type-width", type=int, default=3)
    parser.add_argument("--margin", type=int, default=1)
    parser.add_argument("--block-depth", type=int, default=2)
    parser.add_argument("--p", type=float, required=True)
    parser.add_argument("--iterations", type=int, default=10)
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
    print(f"block_min_image_over_v={min_ratio:.12g}")
    print(f"block_max_image_over_v={max_ratio:.12g}")
    if min_ratio > 1.0:
        print("FLOAT-CERTIFIED-DIAGNOSTIC: block selector has ratio > 1")
    else:
        print("NOT CERTIFIED: block selector ratio is not > 1")


if __name__ == "__main__":
    main()

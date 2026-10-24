"""Monte Carlo scans for finite tree-block branching on T_3 x Z.

This is only a screening tool.  It estimates the mean matrix of a lower
process that exposes a finite forward binary tree of fibers and keeps the
largest reached boundary subset of bounded span in each boundary fiber.
"""

from __future__ import annotations

import argparse
import random

from subset_branching_scan import mask_score, mask_span, type_masks


def tree_edges(depth: int) -> tuple[int, list[tuple[int, int]], list[int]]:
    node_count = (1 << (depth + 1)) - 1
    edges = []
    for parent in range((1 << depth) - 1):
        edges.append((parent, 2 * parent + 1))
        edges.append((parent, 2 * parent + 2))
    boundary = list(range((1 << depth) - 1, node_count))
    return node_count, edges, boundary


def best_type(reached_mask: int, type_width: int) -> int:
    best = 0
    submask = reached_mask
    while submask:
        span = mask_span(submask)
        if span <= type_width:
            normalized = submask >> ((submask & -submask).bit_length() - 1)
            if mask_score(normalized) > mask_score(best):
                best = normalized
        submask = (submask - 1) & reached_mask
    return best


class DSU:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

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
        if self.rank[first_root] == self.rank[second_root]:
            self.rank[first_root] += 1


def sample_children(
    parent_mask: int,
    type_width: int,
    margin: int,
    block_depth: int,
    p: float,
    rng: random.Random,
) -> list[int]:
    height_count = type_width + 1 + 2 * margin
    seed_mask = parent_mask << margin
    node_count, horizontal_edges, boundary = tree_edges(block_depth)

    def vertex(node: int, height: int) -> int:
        return node * height_count + height

    dsu = DSU(node_count * height_count)
    for node in range(node_count):
        for height in range(height_count - 1):
            if rng.random() < p:
                dsu.union(vertex(node, height), vertex(node, height + 1))
    for first, second in horizontal_edges:
        for height in range(height_count):
            if rng.random() < p:
                dsu.union(vertex(first, height), vertex(second, height))

    seeded_roots = {
        dsu.find(vertex(0, height))
        for height in range(height_count)
        if (seed_mask >> height) & 1
    }

    children = []
    for node in boundary:
        reached = 0
        for height in range(height_count):
            if dsu.find(vertex(node, height)) in seeded_roots:
                reached |= 1 << height
        child = best_type(reached, type_width)
        if child:
            children.append(child)
    return children


def estimate_matrix(
    type_width: int,
    margin: int,
    block_depth: int,
    p: float,
    samples: int,
    seed: int,
) -> tuple[list[int], list[list[float]]]:
    rng = random.Random(seed)
    masks = type_masks(type_width)
    index = {mask: row for row, mask in enumerate(masks)}
    matrix = [[0.0] * len(masks) for _ in masks]

    for row, parent in enumerate(masks):
        counts = [0] * len(masks)
        for _ in range(samples):
            for child in sample_children(parent, type_width, margin, block_depth, p, rng):
                counts[index[child]] += 1
        matrix[row] = [count / samples for count in counts]
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type-width", type=int, default=4)
    parser.add_argument("--margin", type=int, default=2)
    parser.add_argument("--block-depth", type=int, default=2)
    parser.add_argument("--p", type=float, required=True)
    parser.add_argument("--samples", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--iterations", type=int, default=500)
    args = parser.parse_args()

    masks, matrix = estimate_matrix(
        args.type_width,
        args.margin,
        args.block_depth,
        args.p,
        args.samples,
        args.seed,
    )
    print(f"type_width={args.type_width}")
    print(f"types={len(masks)}")
    print(f"margin={args.margin}")
    print(f"block_depth={args.block_depth}")
    print(f"p={args.p:.12g}")
    print(f"samples_per_type={args.samples}")
    print(f"estimated_spectral_lower={perron_lower(matrix, args.iterations):.12g}")
    print(
        "row_sum_range="
        f"[{min(sum(row) for row in matrix):.12g}, {max(sum(row) for row in matrix):.12g}]"
    )


if __name__ == "__main__":
    main()

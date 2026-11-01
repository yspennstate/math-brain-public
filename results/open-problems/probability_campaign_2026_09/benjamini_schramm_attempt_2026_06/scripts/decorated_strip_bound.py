"""Exact decorated-strip transfer bound for pc(T_3 x Z).

This script gives a computer-checkable lower bound on the fixed-direction
connection exponent alpha(p) used by Yamamoto's characterization of
pc(T_d x Z).  The strip is a geodesic in T_3 times a finite height window, with
one side branch of tree-depth 1 attached to each geodesic fiber.  Connections
inside each decorated column are integrated out exactly.

The default parameters certify that the finite strip transfer matrix M at
p=5909/20000 has spectral radius larger than 1/2 by producing an integer
vector v with 2 M v > v coordinatewise.  Thus alpha(5909/20000)>1/2, and
Yamamoto's criterion gives pc(T_3 x Z)<5909/20000.
"""

from __future__ import annotations

import argparse
import time


class DSU:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item: int) -> int:
        parent = self.parent
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
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


class DataDSU:
    def __init__(self, seeded: list[bool], root_masks: list[int]) -> None:
        self.parent = list(range(len(seeded)))
        self.rank = [0] * len(seeded)
        self.seeded = seeded[:]
        self.root_masks = root_masks[:]

    def find(self, item: int) -> int:
        parent = self.parent
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
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
        self.root_masks[first_root] |= self.root_masks[second_root]
        if self.rank[first_root] == self.rank[second_root]:
            self.rank[first_root] += 1


def side_tree_edges(height_count: int, side_depth: int) -> tuple[int, list[tuple[int, int]]]:
    """Return column gadget vertices and edges.

    Tree node 0 is the geodesic fiber.  If side_depth=1, node 1 is the single
    side branch attached to this geodesic vertex.  Larger depths attach a finite
    binary tree beyond that side branch.
    """

    tree_nodes = [0]
    tree_edges: list[tuple[int, int]] = []
    next_id = 1

    if side_depth >= 1:
        tree_nodes.append(next_id)
        tree_edges.append((0, next_id))
        frontier = [next_id]
        next_id += 1
        for _level in range(2, side_depth + 1):
            next_frontier = []
            for parent in frontier:
                for _ in range(2):
                    tree_nodes.append(next_id)
                    tree_edges.append((parent, next_id))
                    next_frontier.append(next_id)
                    next_id += 1
            frontier = next_frontier

    def index(tree_node: int, height: int) -> int:
        return tree_node * height_count + height

    edges: list[tuple[int, int]] = []
    for tree_node in tree_nodes:
        for height in range(height_count - 1):
            edges.append((index(tree_node, height), index(tree_node, height + 1)))
    for first, second in tree_edges:
        for height in range(height_count):
            edges.append((index(first, height), index(second, height)))

    return len(tree_nodes), edges


def side_tree_row_edges(side_depth: int) -> tuple[int, list[tuple[int, int]]]:
    """Return the side-tree cross-section at a single height."""

    width, column_edges = side_tree_edges(1, side_depth)
    return width, column_edges


def closure_counts(
    height_count: int, side_depth: int, show_progress: bool
) -> tuple[list[list[list[int]]], int]:
    if side_depth == 1:
        return ladder_closure_counts(height_count, show_progress)

    tree_node_count, edges = side_tree_edges(height_count, side_depth)
    edge_count = len(edges)
    state_count = 1 << height_count
    counts = [
        [[0] * (edge_count + 1) for _ in range(state_count)]
        for __ in range(state_count)
    ]

    start = time.time()
    for edge_mask in range(1 << edge_count):
        dsu = DSU(tree_node_count * height_count)
        remaining = edge_mask
        while remaining:
            bit = remaining & -remaining
            edge_index = bit.bit_length() - 1
            first, second = edges[edge_index]
            dsu.union(first, second)
            remaining -= bit

        root_component_masks: dict[int, int] = {}
        for height in range(height_count):
            root = dsu.find(height)
            root_component_masks[root] = root_component_masks.get(root, 0) | (1 << height)

        open_edge_count = edge_mask.bit_count()
        for seed_mask in range(state_count):
            output_mask = 0
            remaining_seed = seed_mask
            while remaining_seed:
                bit = remaining_seed & -remaining_seed
                height = bit.bit_length() - 1
                output_mask |= root_component_masks[dsu.find(height)]
                remaining_seed -= bit
            counts[seed_mask][output_mask][open_edge_count] += 1

        if show_progress and edge_mask and edge_mask % 100000 == 0:
            print(
                f"edge_masks={edge_mask}/{1 << edge_count} "
                f"elapsed={time.time() - start:.3f}",
                flush=True,
            )

    return counts, edge_count


def initial_ladder_states(height_count: int, seed_mask: int) -> dict[tuple[int, bool, bool, int, bool, int, int], int]:
    root_seed = (seed_mask & 1) != 0
    states: dict[tuple[int, bool, bool, int, bool, int, int], int] = {}

    # State entries are
    # (final_output, same_component, root_seeded, root_mask,
    #  side_seeded, side_mask, open_edge_count).
    states[(0, False, root_seed, 1, False, 0, 0)] = 1
    states[(0, True, root_seed, 1, False, 0, 1)] = 1
    return states


def advance_ladder_state(
    state: tuple[int, bool, bool, int, bool, int, int],
    next_height: int,
    seed_mask: int,
) -> list[tuple[int, bool, bool, int, bool, int, int]]:
    output, same, root_seeded, root_mask, side_seeded, side_mask, open_count = state
    next_states = []

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
        next_open_count = open_count + edge_mask.bit_count()

        if root_component == side_component:
            next_states.append(
                (
                    next_output,
                    True,
                    root_data[0],
                    root_data[1],
                    False,
                    0,
                    next_open_count,
                )
            )
        else:
            side_data = data[side_component]
            next_states.append(
                (
                    next_output,
                    False,
                    root_data[0],
                    root_data[1],
                    side_data[0],
                    side_data[1],
                    next_open_count,
                )
            )

    return next_states


def ladder_closure_counts(
    height_count: int, show_progress: bool
) -> tuple[list[list[list[int]]], int]:
    edge_count = 3 * height_count - 2
    state_count = 1 << height_count
    counts = [
        [[0] * (edge_count + 1) for _ in range(state_count)]
        for __ in range(state_count)
    ]

    start = time.time()
    for seed_mask in range(state_count):
        states = initial_ladder_states(height_count, seed_mask)
        for next_height in range(1, height_count):
            next_states: dict[tuple[int, bool, bool, int, bool, int, int], int] = {}
            for state, count in states.items():
                for advanced in advance_ladder_state(state, next_height, seed_mask):
                    next_states[advanced] = next_states.get(advanced, 0) + count
            states = next_states

        for state, count in states.items():
            output, same, root_seeded, root_mask, side_seeded, side_mask, open_edges = state
            if root_seeded:
                output |= root_mask
            if not same and side_seeded:
                output |= side_mask
            counts[seed_mask][output][open_edges] += count

        if show_progress and seed_mask % 64 == 0:
            print(
                f"seed_masks={seed_mask}/{state_count} states={len(states)} "
                f"elapsed={time.time() - start:.3f}",
                flush=True,
            )

    return counts, edge_count


def sparse_ladder_closure_counts(
    height_count: int, show_progress: bool
) -> tuple[list[dict[int, list[int]]], int]:
    edge_count = 3 * height_count - 2
    state_count = 1 << height_count
    counts: list[dict[int, list[int]]] = []

    start = time.time()
    for seed_mask in range(state_count):
        states = initial_ladder_states(height_count, seed_mask)
        for next_height in range(1, height_count):
            next_states: dict[tuple[int, bool, bool, int, bool, int, int], int] = {}
            for state, count in states.items():
                for advanced in advance_ladder_state(state, next_height, seed_mask):
                    next_states[advanced] = next_states.get(advanced, 0) + count
            states = next_states

        seed_counts: dict[int, list[int]] = {}
        for state, count in states.items():
            output, same, root_seeded, root_mask, side_seeded, side_mask, open_edges = state
            if root_seeded:
                output |= root_mask
            if not same and side_seeded:
                output |= side_mask
            if output not in seed_counts:
                seed_counts[output] = [0] * (edge_count + 1)
            seed_counts[output][open_edges] += count
        counts.append(seed_counts)

        if show_progress and seed_mask % 128 == 0:
            print(
                f"seed_masks={seed_mask}/{state_count} states={len(states)} "
                f"outputs={len(seed_counts)} elapsed={time.time() - start:.3f}",
                flush=True,
            )

    return counts, edge_count


FrontierState = tuple[int, tuple[int, ...], tuple[tuple[bool, int], ...], int]


def canonical_frontier_state(
    output: int,
    labels: list[int],
    component_data: dict[int, tuple[bool, int]],
    open_count: int,
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
    return output, tuple(canonical_labels), tuple(canonical_data), open_count


def initial_frontier_states(
    seed_mask: int,
    width: int,
    row_edges: list[tuple[int, int]],
) -> dict[FrontierState, int]:
    states: dict[FrontierState, int] = {}
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
        state = canonical_frontier_state(0, labels, component_data, edge_mask.bit_count())
        states[state] = states.get(state, 0) + 1
    return states


def advance_frontier_state(
    state: FrontierState,
    next_height: int,
    seed_mask: int,
    width: int,
    row_edges: list[tuple[int, int]],
) -> list[FrontierState]:
    output, old_labels, old_data, open_count = state
    next_states: list[FrontierState] = []
    edge_options = 1 << (width + len(row_edges))

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
        all_roots = {dsu.find(vertex) for vertex in range(2 * width)}
        for root in all_roots - new_roots:
            if dsu.seeded[root]:
                next_output |= dsu.root_masks[root]

        labels = [dsu.find(width + vertex) for vertex in range(width)]
        component_data = {
            label: (dsu.seeded[label], dsu.root_masks[label]) for label in set(labels)
        }
        next_states.append(
            canonical_frontier_state(
                next_output,
                labels,
                component_data,
                open_count + edge_mask.bit_count(),
            )
        )

    return next_states


def frontier_closure_counts(
    height_count: int, side_depth: int, show_progress: bool
) -> tuple[list[dict[int, list[int]]], int]:
    width, row_edges = side_tree_row_edges(side_depth)
    edge_count = width * (height_count - 1) + len(row_edges) * height_count
    state_count = 1 << height_count
    counts: list[dict[int, list[int]]] = []

    start = time.time()
    for seed_mask in range(state_count):
        states = initial_frontier_states(seed_mask, width, row_edges)
        for next_height in range(1, height_count):
            next_states: dict[FrontierState, int] = {}
            for state, count in states.items():
                for advanced in advance_frontier_state(
                    state, next_height, seed_mask, width, row_edges
                ):
                    next_states[advanced] = next_states.get(advanced, 0) + count
            states = next_states

        seed_counts: dict[int, list[int]] = {}
        for state, count in states.items():
            output, _labels, component_data, open_edges = state
            final_output = output
            for seeded, root_mask in component_data:
                if seeded:
                    final_output |= root_mask
            if final_output not in seed_counts:
                seed_counts[final_output] = [0] * (edge_count + 1)
            seed_counts[final_output][open_edges] += count
        counts.append(seed_counts)

        if show_progress and seed_mask % 32 == 0:
            print(
                f"seed_masks={seed_mask}/{state_count} states={len(states)} "
                f"outputs={len(seed_counts)} elapsed={time.time() - start:.3f}",
                flush=True,
            )

    return counts, edge_count


def apply_sparse_matrix(
    counts: list[dict[int, list[int]]],
    edge_count: int,
    height_count: int,
    p_num: int,
    p_den: int,
    vector: list[float],
) -> list[float]:
    state_count = 1 << height_count
    p = p_num / p_den
    q = 1.0 - p

    pow_p = [1.0] * (edge_count + height_count + 1)
    pow_q = [1.0] * (edge_count + height_count + 1)
    for i in range(1, len(pow_p)):
        pow_p[i] = pow_p[i - 1] * p
        pow_q[i] = pow_q[i - 1] * q

    seed_values = [0.0] * state_count
    for seed, seed_counts in enumerate(counts):
        total = 0.0
        for output, edge_counts in seed_counts.items():
            if output == 0:
                continue
            probability = 0.0
            for open_edges, count in enumerate(edge_counts):
                if count:
                    probability += count * pow_p[open_edges] * pow_q[edge_count - open_edges]
            total += probability * vector[output - 1]
        seed_values[seed] = total

    image = [0.0] * (state_count - 1)
    for current in range(1, state_count):
        total = 0.0
        current_size = current.bit_count()
        seed = current
        while True:
            total += (
                pow_p[seed.bit_count()]
                * pow_q[current_size - seed.bit_count()]
                * seed_values[seed]
            )
            if seed == 0:
                break
            seed = (seed - 1) & current
        image[current - 1] = total

    return image


def sparse_right_perron_vector(
    counts: list[dict[int, list[int]]],
    edge_count: int,
    height_count: int,
    p_num: int,
    p_den: int,
    iterations: int = 800,
) -> tuple[list[float], float]:
    size = (1 << height_count) - 1
    vector = [1.0 / size] * size
    for _ in range(iterations):
        image = apply_sparse_matrix(
            counts, edge_count, height_count, p_num, p_den, vector
        )
        total = sum(image)
        vector = [entry / total for entry in image]

    image = apply_sparse_matrix(counts, edge_count, height_count, p_num, p_den, vector)
    min_ratio = min(image[row] / vector[row] for row in range(size))
    return vector, min_ratio


def sparse_exact_certificate_check(
    counts: list[dict[int, list[int]]],
    edge_count: int,
    height_count: int,
    p_num: int,
    p_den: int,
    vector: list[int],
) -> tuple[bool, float, float, int]:
    state_count = 1 << height_count
    q_num = p_den - p_num
    max_power = edge_count + height_count + 1
    pow_p = [1] * max_power
    pow_q = [1] * max_power
    pow_den = [1] * max_power
    for i in range(1, max_power):
        pow_p[i] = pow_p[i - 1] * p_num
        pow_q[i] = pow_q[i - 1] * q_num
        pow_den[i] = pow_den[i - 1] * p_den

    seed_values = [0] * state_count
    for seed, seed_counts in enumerate(counts):
        total = 0
        for output, edge_counts in seed_counts.items():
            if output == 0:
                continue
            closure_sum = 0
            for open_edges, count in enumerate(edge_counts):
                if count:
                    closure_sum += count * pow_p[open_edges] * pow_q[edge_count - open_edges]
            if closure_sum:
                total += closure_sum * vector[output - 1]
        seed_values[seed] = total

    min_margin: int | None = None
    min_ratio = float("inf")
    max_ratio = 0.0
    for current in range(1, state_count):
        current_size = current.bit_count()
        numerator = 0
        seed = current
        while True:
            numerator += (
                pow_p[seed.bit_count()]
                * pow_q[current_size - seed.bit_count()]
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


def float_matrix(
    counts: list[list[list[int]]],
    edge_count: int,
    height_count: int,
    p_num: int,
    p_den: int,
) -> list[list[float]]:
    state_count = 1 << height_count
    matrix_size = state_count - 1
    p = p_num / p_den
    q = 1.0 - p

    pow_p = [1.0] * (edge_count + height_count + 1)
    pow_q = [1.0] * (edge_count + height_count + 1)
    for i in range(1, len(pow_p)):
        pow_p[i] = pow_p[i - 1] * p
        pow_q[i] = pow_q[i - 1] * q

    closure_probability = [[0.0] * state_count for _ in range(state_count)]
    for seed in range(state_count):
        for output in range(state_count):
            total = 0.0
            for open_edges, count in enumerate(counts[seed][output]):
                if count:
                    total += count * pow_p[open_edges] * pow_q[edge_count - open_edges]
            closure_probability[seed][output] = total

    matrix = [[0.0] * matrix_size for _ in range(matrix_size)]
    for current in range(1, state_count):
        row = matrix[current - 1]
        current_size = current.bit_count()
        seed = current
        while True:
            seed_weight = (
                pow_p[seed.bit_count()]
                * pow_q[current_size - seed.bit_count()]
            )
            if seed_weight:
                for output, probability in enumerate(closure_probability[seed]):
                    if output and probability:
                        row[output - 1] += seed_weight * probability
            if seed == 0:
                break
            seed = (seed - 1) & current

    return matrix


def right_perron_vector(matrix: list[list[float]], iterations: int = 2000) -> tuple[list[float], float]:
    size = len(matrix)
    vector = [1.0 / size] * size
    for _ in range(iterations):
        image = [
            sum(matrix[row][column] * vector[column] for column in range(size))
            for row in range(size)
        ]
        total = sum(image)
        vector = [entry / total for entry in image]

    image = [
        sum(matrix[row][column] * vector[column] for column in range(size))
        for row in range(size)
    ]
    min_ratio = min(image[row] / vector[row] for row in range(size))
    return vector, min_ratio


def exact_certificate_check(
    counts: list[list[list[int]]],
    edge_count: int,
    height_count: int,
    p_num: int,
    p_den: int,
    vector: list[int],
) -> tuple[bool, float, float, int]:
    state_count = 1 << height_count
    q_num = p_den - p_num
    max_power = edge_count + height_count + 1
    pow_p = [1] * max_power
    pow_q = [1] * max_power
    pow_den = [1] * max_power
    for i in range(1, max_power):
        pow_p[i] = pow_p[i - 1] * p_num
        pow_q[i] = pow_q[i - 1] * q_num
        pow_den[i] = pow_den[i - 1] * p_den

    min_margin: int | None = None
    min_ratio = float("inf")
    max_ratio = 0.0

    for current in range(1, state_count):
        current_size = current.bit_count()
        denominator = pow_den[edge_count + current_size]
        numerator = 0
        seed = current
        while True:
            seed_factor = (
                pow_p[seed.bit_count()]
                * pow_q[current_size - seed.bit_count()]
            )
            if seed_factor:
                for output in range(1, state_count):
                    closure_sum = 0
                    for open_edges, count in enumerate(counts[seed][output]):
                        if count:
                            closure_sum += (
                                count
                                * pow_p[open_edges]
                                * pow_q[edge_count - open_edges]
                            )
                    if closure_sum:
                        numerator += seed_factor * closure_sum * vector[output - 1]
            if seed == 0:
                break
            seed = (seed - 1) & current

        # Certify Mv > (1/2)v, i.e. 2*numerator > denominator*v_current.
        margin = 2 * numerator - denominator * vector[current - 1]
        min_margin = margin if min_margin is None else min(min_margin, margin)
        ratio = (2 * numerator) / (denominator * vector[current - 1])
        min_ratio = min(min_ratio, ratio)
        max_ratio = max(max_ratio, ratio)

    assert min_margin is not None
    return min_margin > 0, min_ratio, max_ratio, min_margin


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--height-count", type=int, default=10)
    parser.add_argument("--side-depth", type=int, default=1)
    parser.add_argument("--p-num", type=int, default=5909)
    parser.add_argument("--p-den", type=int, default=20000)
    parser.add_argument("--scale", type=int, default=100_000_000)
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--dense", action="store_true")
    args = parser.parse_args()

    start = time.time()
    use_sparse = not args.dense
    if use_sparse:
        if args.side_depth == 1:
            counts, edge_count = sparse_ladder_closure_counts(args.height_count, args.progress)
        else:
            counts, edge_count = frontier_closure_counts(
                args.height_count, args.side_depth, args.progress
            )
        vector_float, spectral_lower = sparse_right_perron_vector(
            counts, edge_count, args.height_count, args.p_num, args.p_den
        )
        vector = [max(1, round(entry * args.scale)) for entry in vector_float]
        certified, min_ratio, max_ratio, min_margin = sparse_exact_certificate_check(
            counts,
            edge_count,
            args.height_count,
            args.p_num,
            args.p_den,
            vector,
        )
    else:
        counts, edge_count = closure_counts(args.height_count, args.side_depth, args.progress)
        matrix = float_matrix(
            counts, edge_count, args.height_count, args.p_num, args.p_den
        )
        vector_float, spectral_lower = right_perron_vector(matrix)
        vector = [max(1, round(entry * args.scale)) for entry in vector_float]
        certified, min_ratio, max_ratio, min_margin = exact_certificate_check(
            counts,
            edge_count,
            args.height_count,
            args.p_num,
            args.p_den,
            vector,
        )

    print(f"height_count={args.height_count}")
    print(f"side_depth={args.side_depth}")
    print(f"edge_count={edge_count}")
    print(f"p={args.p_num}/{args.p_den}={args.p_num / args.p_den:.12g}")
    print(f"matrix_size={(1 << args.height_count) - 1}")
    print(f"mode={'sparse' if use_sparse else 'dense'}")
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

"""Finite-memory walk row-growth bounds on T_3 x Z.

A memory-m walk is a walk that is not allowed to step onto any of the previous
m vertices.  Every self-avoiding walk is a memory-m walk, so the row-sum growth
of this finite-state walk class is an upper bound for the ordinary connective
constant and, a fortiori, a crude upper bound for the SAW operator growth.

This is only a diagnostic: row-sum bounds are much weaker than L2 operator
bounds, but they measure how much local self-avoidance can plausibly improve
over nonbacktracking.
"""

from __future__ import annotations

import argparse
from collections import defaultdict, deque

TreeWord = tuple[int, ...]
Vertex = tuple[TreeWord, int]
State = tuple[Vertex, ...]


TREE_GENERATORS = (0, 1, 2)
MOVES: tuple[tuple[TreeWord, int], ...] = (
    ((0,), 0),
    ((1,), 0),
    ((2,), 0),
    ((), 1),
    ((), -1),
)


def multiply_tree(left: TreeWord, right: TreeWord) -> TreeWord:
    word = list(left)
    for generator in right:
        if word and word[-1] == generator:
            word.pop()
        else:
            word.append(generator)
    return tuple(word)


def inverse_vertex(vertex: Vertex) -> Vertex:
    word, height = vertex
    return tuple(reversed(word)), -height


def multiply_vertex(left: Vertex, right: Vertex) -> Vertex:
    left_word, left_height = left
    right_word, right_height = right
    return multiply_tree(left_word, right_word), left_height + right_height


def canonical_tree_words(words: list[TreeWord]) -> list[TreeWord]:
    label_map: dict[int, int] = {}
    next_label = 0
    output = []
    for word in words:
        canonical = []
        for generator in word:
            if generator not in label_map:
                label_map[generator] = next_label
                next_label += 1
            canonical.append(label_map[generator])
        output.append(tuple(canonical))
    return output


def canonical_state(vertices: list[Vertex]) -> State:
    words = canonical_tree_words([word for word, _height in vertices])
    return tuple((word, vertices[index][1]) for index, word in enumerate(words))


def initial_state() -> State:
    return ((((), 0)),)


def next_states(state: State, memory: int) -> list[State]:
    forbidden = set(state[:memory])
    output = []
    for move in MOVES:
        if move in forbidden:
            continue
        inverse_move = inverse_vertex(move)
        shifted = [multiply_vertex(inverse_move, vertex) for vertex in state[:memory]]
        output.append(canonical_state([(((), 0))] + shifted))
    return output


def build_state_graph(memory: int) -> tuple[list[State], list[list[int]]]:
    start = initial_state()
    index = {start: 0}
    states = [start]
    edges: list[list[int]] = []
    queue = deque([start])

    while queue:
        state = queue.popleft()
        state_edges = []
        for next_state in next_states(state, memory):
            if next_state not in index:
                index[next_state] = len(states)
                states.append(next_state)
                queue.append(next_state)
            state_edges.append(index[next_state])
        edges.append(state_edges)

    return states, edges


def spectral_radius(edges: list[list[int]], iterations: int) -> tuple[float, float]:
    size = len(edges)
    vector = [1.0 / size] * size
    for _ in range(iterations):
        image = [0.0] * size
        for row, row_edges in enumerate(edges):
            value = vector[row]
            for column in row_edges:
                image[column] += value
        total = sum(image)
        vector = [entry / total for entry in image]

    image = [0.0] * size
    for row, row_edges in enumerate(edges):
        value = vector[row]
        for column in row_edges:
            image[column] += value

    ratios = [
        image[index] / vector[index]
        for index in range(size)
        if vector[index] > 0
    ]
    return min(ratios), max(ratios)


def exact_counts(edges: list[list[int]], length: int) -> int:
    counts = [0] * len(edges)
    counts[0] = 1
    for _ in range(length):
        next_counts = [0] * len(edges)
        for state, count in enumerate(counts):
            if count:
                for next_state in edges[state]:
                    next_counts[next_state] += count
        counts = next_counts
    return sum(counts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--memory", type=int, default=4)
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--length", type=int, default=30)
    args = parser.parse_args()

    states, edges = build_state_graph(args.memory)
    lower, upper = spectral_radius(edges, args.iterations)
    count = exact_counts(edges, args.length)

    print(f"memory={args.memory}")
    print(f"states={len(states)}")
    print(f"min_out_degree={min(len(row) for row in edges)}")
    print(f"max_out_degree={max(len(row) for row in edges)}")
    print(f"spectral_radius_lower={lower:.12g}")
    print(f"spectral_radius_upper={upper:.12g}")
    print(f"count_length_{args.length}={count}")
    print(f"count_root_{args.length}={count ** (1 / args.length):.12g}")


if __name__ == "__main__":
    main()

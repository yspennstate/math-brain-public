"""Finite-length spherical bounds for finite-memory walks on T_3 x Z.

A memory-m walk is forbidden to step onto any of its previous m vertices.  This
class contains every self-avoiding walk, so its endpoint kernel gives an upper
bound for the length-n SAW endpoint kernel.  Unlike memory_walk_row_bound.py,
this script evaluates the radial/Fourier L2 spherical bound rather than the
ordinary row-sum growth.
"""

from __future__ import annotations

import argparse
import math
import time
from collections import defaultdict

TreeWord = tuple[int, ...]
Vertex = tuple[TreeWord, int]
State = tuple[Vertex, ...]


def move_word(word: TreeWord, generator: int) -> TreeWord:
    if word and word[-1] == generator:
        return word[:-1]
    return word + (generator,)


def canonicalize(vertices: list[Vertex]) -> State:
    label_map: dict[int, int] = {}
    next_label = 0
    output: list[Vertex] = []
    for word, height in vertices:
        canonical_word = []
        for generator in word:
            if generator not in label_map:
                label_map[generator] = next_label
                next_label += 1
            canonical_word.append(label_map[generator])
        output.append((tuple(canonical_word), height))
    return tuple(output)


def used_generator_count(state: State) -> int:
    used = set()
    for word, _height in state:
        used.update(word)
    return len(used)


def transitions(state: State, memory: int, degree: int) -> list[tuple[int, State]]:
    current_word, current_height = state[0]
    forbidden = set(state[:memory])
    output: list[tuple[int, State]] = []

    used_count = used_generator_count(state)
    for generator in range(used_count):
        next_vertex = (move_word(current_word, generator), current_height)
        if next_vertex not in forbidden:
            output.append((1, canonicalize([next_vertex] + list(state[: memory - 1]))))

    if used_count < degree:
        next_vertex = (current_word + (used_count,), current_height)
        if next_vertex not in forbidden:
            output.append(
                (
                    degree - used_count,
                    canonicalize([next_vertex] + list(state[: memory - 1])),
                )
            )

    for delta in (-1, 1):
        next_vertex = (current_word, current_height + delta)
        if next_vertex not in forbidden:
            output.append((1, canonicalize([next_vertex] + list(state[: memory - 1]))))

    return output


def endpoint_totals(
    degree: int,
    memory: int,
    length: int,
    show_progress: bool,
) -> dict[tuple[int, int], int]:
    states: dict[State, int] = {((((), 0)),): 1}
    start = time.time()

    for step in range(length):
        next_states: dict[State, int] = defaultdict(int)
        for state, count in states.items():
            for multiplicity, next_state in transitions(state, memory, degree):
                next_states[next_state] += count * multiplicity
        states = dict(next_states)
        if show_progress:
            print(
                f"step={step + 1} states={len(states)} "
                f"walks={sum(states.values())} elapsed={time.time() - start:.3f}",
                flush=True,
            )

    totals: dict[tuple[int, int], int] = defaultdict(int)
    for state, count in states.items():
        word, height = state[0]
        totals[(len(word), height)] += count
    return totals


def endpoint_coefficients(
    degree: int,
    memory: int,
    length: int,
    show_progress: bool,
) -> dict[tuple[int, int], int]:
    totals = endpoint_totals(degree, memory, length, show_progress)
    coefficients: dict[tuple[int, int], int] = {}
    q = degree - 1
    for (radius, height), total in totals.items():
        sphere_size = 1 if radius == 0 else degree * q ** (radius - 1)
        if total % sphere_size != 0:
            raise ArithmeticError(
                f"endpoint count {total} is not divisible by sphere size "
                f"{sphere_size} for radius={radius}, height={height}"
            )
        coefficients[(radius, height)] = total // sphere_size
    return coefficients


def tree_sphere_norms(degree: int, length: int) -> list[float]:
    q = degree - 1
    edge = 2.0 * math.sqrt(q)
    values = [0.0] * (length + 1)
    values[0] = 1.0
    if length >= 1:
        values[1] = edge
    if length >= 2:
        values[2] = edge * edge - degree
    for radius in range(2, length):
        values[radius + 1] = edge * values[radius] - q * values[radius - 1]
    return values


def tree_sphere_norms_d3_exact(length: int) -> list[tuple[int, int]]:
    values: list[tuple[int, int]] = [(1, 0)]
    if length >= 1:
        values.append((0, 2))
    if length >= 2:
        values.append((5, 0))
    for radius in range(2, length):
        a, b = values[radius]
        c, e = values[radius - 1]
        values.append((4 * b - 2 * c, 2 * a - 2 * e))
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--degree", type=int, default=3)
    parser.add_argument("--memory", type=int, default=4)
    parser.add_argument("--length", type=int, default=12)
    parser.add_argument("--progress", action="store_true")
    args = parser.parse_args()

    start = time.time()
    coefficients = endpoint_coefficients(
        args.degree, args.memory, args.length, args.progress
    )
    elapsed = time.time() - start

    norms = tree_sphere_norms(args.degree, args.length)
    bound = sum(coeff * norms[radius] for (radius, _height), coeff in coefficients.items())

    print(f"degree={args.degree}")
    print(f"memory={args.memory}")
    print(f"length={args.length}")
    print(f"terms={len(coefficients)}")
    print(f"operator_norm_bound={bound:.15g}")
    print(f"root={bound ** (1 / args.length):.15g}")
    print(f"elapsed_seconds={elapsed:.3f}")

    if args.degree == 3:
        exact_norms = tree_sphere_norms_d3_exact(args.length)
        a_total = 0
        b_total = 0
        for (radius, _height), coeff in coefficients.items():
            a, b = exact_norms[radius]
            a_total += coeff * a
            b_total += coeff * b
        print(f"exact=A+B*sqrt(2), A={a_total}, B={b_total}")


if __name__ == "__main__":
    main()

"""Exact quotient-state SAW spherical bounds on T_d x Z.

This script computes the same endpoint coefficients as saw_spherical_bound.py,
but quotients out the labels of the regular tree.  A state is the finite rooted
tree of visited fibers, decorated by the set of visited heights in each fiber
and by the current fiber/height.  Children are unordered.  Moving to a new
child carries the multiplicity of unused child slots: d at the root and d-1 at
all other tree vertices.

The quotient dynamic program still counts labelled self-avoiding walks exactly,
but it can reach length 15 for T_3 x Z on this machine, whereas the direct DFS
enumerator stalls there.
"""

from __future__ import annotations

import argparse
import math
import time
from collections import defaultdict
from typing import Optional

Node = tuple[tuple[int, ...], Optional[int], tuple["Node", ...]]


def sort_children(children: tuple[Node, ...]) -> tuple[Node, ...]:
    # repr gives a total order even though the current marker may be None.
    return tuple(sorted(children, key=repr))


def replace_child(children: tuple[Node, ...], index: int, child: Node) -> tuple[Node, ...]:
    next_children = list(children)
    next_children[index] = child
    return sort_children(tuple(next_children))


def current_depth_height(node: Node, depth: int = 0) -> tuple[int, int] | None:
    heights, marker, children = node
    if marker is not None:
        return depth, marker
    for child in children:
        result = current_depth_height(child, depth + 1)
        if result is not None:
            return result
    return None


def vertical_move(node: Node, delta: int) -> Node | None:
    heights, marker, children = node
    if marker is not None:
        next_height = marker + delta
        if next_height in heights:
            return None
        return (tuple(sorted(heights + (next_height,))), next_height, children)

    for index, child in enumerate(children):
        next_child = vertical_move(child, delta)
        if next_child is not None:
            return (heights, None, replace_child(children, index, next_child))
    return None


def parent_move(node: Node) -> Node | None:
    heights, marker, children = node
    for index, child in enumerate(children):
        child_heights, child_marker, grand_children = child
        if child_marker is not None:
            height = child_marker
            if height in heights:
                return None
            unmarked_child = (child_heights, None, grand_children)
            return (
                tuple(sorted(heights + (height,))),
                height,
                replace_child(children, index, unmarked_child),
            )

        moved_child = parent_move(child)
        if moved_child is not None:
            return (heights, None, replace_child(children, index, moved_child))
    return None


def child_moves(node: Node, root_degree: int, current_is_root: bool = True) -> list[tuple[int, Node]]:
    heights, marker, children = node
    output: list[tuple[int, Node]] = []

    if marker is not None:
        height = marker
        aggregated: dict[Node, int] = defaultdict(int)

        for index, child in enumerate(children):
            child_heights, _child_marker, grand_children = child
            if height in child_heights:
                continue
            next_child = (tuple(sorted(child_heights + (height,))), height, grand_children)
            next_state = (heights, None, replace_child(children, index, next_child))
            aggregated[next_state] += 1

        output.extend((multiplicity, state) for state, multiplicity in aggregated.items())

        child_capacity = root_degree if current_is_root else root_degree - 1
        free_slots = child_capacity - len(children)
        if free_slots > 0:
            next_child = ((height,), height, ())
            next_state = (heights, None, sort_children(children + (next_child,)))
            output.append((free_slots, next_state))

        return output

    for index, child in enumerate(children):
        moved_children = child_moves(child, root_degree, current_is_root=False)
        if moved_children:
            for multiplicity, moved_child in moved_children:
                output.append(
                    (multiplicity, (heights, None, replace_child(children, index, moved_child)))
                )
            break

    return output


def transitions(state: Node, degree: int) -> list[tuple[int, Node]]:
    output: list[tuple[int, Node]] = []
    for delta in (-1, 1):
        next_state = vertical_move(state, delta)
        if next_state is not None:
            output.append((1, next_state))

    next_state = parent_move(state)
    if next_state is not None:
        output.append((1, next_state))

    output.extend(child_moves(state, degree))
    return output


def endpoint_totals(degree: int, length: int, show_progress: bool) -> dict[tuple[int, int], int]:
    states: dict[Node, int] = {((0,), 0, ()): 1}
    start = time.time()

    for step in range(length):
        next_states: dict[Node, int] = defaultdict(int)
        for state, count in states.items():
            for multiplicity, next_state in transitions(state, degree):
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
        result = current_depth_height(state)
        if result is None:
            raise RuntimeError("state has no current marker")
        totals[result] += count
    return totals


def endpoint_coefficients(degree: int, length: int, show_progress: bool) -> dict[tuple[int, int], int]:
    totals = endpoint_totals(degree, length, show_progress)
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
    parser.add_argument("--length", type=int, default=12)
    parser.add_argument("--progress", action="store_true")
    args = parser.parse_args()

    start = time.time()
    coefficients = endpoint_coefficients(args.degree, args.length, args.progress)
    elapsed = time.time() - start

    norms = tree_sphere_norms(args.degree, args.length)
    bound = sum(coeff * norms[radius] for (radius, _height), coeff in coefficients.items())

    print(f"degree={args.degree}")
    print(f"length={args.length}")
    print(f"terms={len(coefficients)}")
    print(f"operator_norm={bound:.15g}")
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

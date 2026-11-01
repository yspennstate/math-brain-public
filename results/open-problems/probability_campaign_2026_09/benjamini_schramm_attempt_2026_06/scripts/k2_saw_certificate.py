"""Exact certificate for the T_3 x K_2 finite-length SAW bound.

The script verifies the two computer-checkable claims used in the manuscript:

1. The finite-subset branching process for T_3 x K_2 is supercritical at
   p = 39/100.
2. The length-15 self-avoiding-walk endpoint operator on T_3 x K_2 has the
   spherical bound

       ||C_15|| <= 639862 + 452048 sqrt(2) < (100/39)^15.

The self-avoiding walks are counted by a quotient dynamic program.  Tree
labels are forgotten up to rooted isomorphism; each visited tree fibre records
which of the two K_2 layers have been visited and which vertex is current.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from typing import Optional

Node = tuple[tuple[int, ...], Optional[int], tuple["Node", ...]]


def sort_children(children: tuple[Node, ...]) -> tuple[Node, ...]:
    return tuple(sorted(children, key=repr))


def replace_child(children: tuple[Node, ...], index: int, child: Node) -> tuple[Node, ...]:
    next_children = list(children)
    next_children[index] = child
    return sort_children(tuple(next_children))


def current_depth_layer(node: Node, depth: int = 0) -> tuple[int, int] | None:
    layers, marker, children = node
    if marker is not None:
        return depth, marker
    for child in children:
        result = current_depth_layer(child, depth + 1)
        if result is not None:
            return result
    return None


def vertical_move(node: Node) -> Node | None:
    layers, marker, children = node
    if marker is not None:
        next_layer = 1 - marker
        if next_layer in layers:
            return None
        return (tuple(sorted(layers + (next_layer,))), next_layer, children)

    for index, child in enumerate(children):
        next_child = vertical_move(child)
        if next_child is not None:
            return (layers, None, replace_child(children, index, next_child))
    return None


def parent_move(node: Node) -> Node | None:
    layers, marker, children = node
    for index, child in enumerate(children):
        child_layers, child_marker, grand_children = child
        if child_marker is not None:
            layer = child_marker
            if layer in layers:
                return None
            unmarked_child = (child_layers, None, grand_children)
            return (
                tuple(sorted(layers + (layer,))),
                layer,
                replace_child(children, index, unmarked_child),
            )

        moved_child = parent_move(child)
        if moved_child is not None:
            return (layers, None, replace_child(children, index, moved_child))
    return None


def child_moves(node: Node, degree: int, current_is_root: bool = True) -> list[tuple[int, Node]]:
    layers, marker, children = node
    output: list[tuple[int, Node]] = []

    if marker is not None:
        layer = marker
        aggregated: dict[Node, int] = defaultdict(int)
        for index, child in enumerate(children):
            child_layers, _child_marker, grand_children = child
            if layer in child_layers:
                continue
            next_child = (tuple(sorted(child_layers + (layer,))), layer, grand_children)
            next_state = (layers, None, replace_child(children, index, next_child))
            aggregated[next_state] += 1

        output.extend((multiplicity, state) for state, multiplicity in aggregated.items())

        child_capacity = degree if current_is_root else degree - 1
        free_slots = child_capacity - len(children)
        if free_slots > 0:
            next_child = ((layer,), layer, ())
            next_state = (layers, None, sort_children(children + (next_child,)))
            output.append((free_slots, next_state))
        return output

    for index, child in enumerate(children):
        moved_children = child_moves(child, degree, current_is_root=False)
        if moved_children:
            for multiplicity, moved_child in moved_children:
                output.append(
                    (multiplicity, (layers, None, replace_child(children, index, moved_child)))
                )
            break
    return output


def transitions(state: Node, degree: int) -> list[tuple[int, Node]]:
    output: list[tuple[int, Node]] = []
    next_state = vertical_move(state)
    if next_state is not None:
        output.append((1, next_state))

    next_state = parent_move(state)
    if next_state is not None:
        output.append((1, next_state))

    output.extend(child_moves(state, degree))
    return output


def endpoint_coefficients(degree: int, length: int) -> dict[tuple[int, int], int]:
    states: dict[Node, int] = {((0,), 0, ()): 1}
    for _step in range(length):
        next_states: dict[Node, int] = defaultdict(int)
        for state, count in states.items():
            for multiplicity, next_state in transitions(state, degree):
                next_states[next_state] += count * multiplicity
        states = dict(next_states)

    totals: dict[tuple[int, int], int] = defaultdict(int)
    for state, count in states.items():
        result = current_depth_layer(state)
        if result is None:
            raise RuntimeError("state has no current marker")
        totals[result] += count

    coefficients: dict[tuple[int, int], int] = {}
    q = degree - 1
    for (radius, layer), total in totals.items():
        sphere_size = 1 if radius == 0 else degree * q ** (radius - 1)
        if total % sphere_size != 0:
            raise ArithmeticError(
                f"endpoint count {total} is not divisible by sphere size "
                f"{sphere_size} for radius={radius}, layer={layer}"
            )
        coefficients[(radius, layer)] = total // sphere_size
    return coefficients


def tree_sphere_norms_d3_exact(length: int) -> list[tuple[int, int]]:
    """Return pairs (a, b) representing a + b sqrt(2)."""
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


def saw_bound_a_b(length: int = 15) -> tuple[int, int, dict[tuple[int, int], int]]:
    coefficients = endpoint_coefficients(3, length)
    sphere_norms = tree_sphere_norms_d3_exact(length)
    a_total = 0
    b_total = 0
    for (radius, _layer), coefficient in coefficients.items():
        a_part, b_part = sphere_norms[radius]
        a_total += coefficient * a_part
        b_total += coefficient * b_part
    return a_total, b_total, coefficients


def verify_branching() -> None:
    p = Fraction(39, 100)
    matrix = [
        [2 * p * (1 - p), 2 * p * p],
        [4 * p * (1 - p) * (1 - p), 2 * (3 * p * p - 2 * p * p * p)],
    ]
    vector = [Fraction(1), Fraction(7, 4)]
    product = [
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    ]
    if not (product[0] > vector[0] and product[1] > vector[1]):
        raise AssertionError("branching Collatz lower bound failed")
    print("branching_matrix=")
    for row in matrix:
        print("  " + " ".join(str(entry) for entry in row))
    print(f"branching_vector={vector[0]} {vector[1]}")
    print(f"branching_product={product[0]} {product[1]}")


def verify_saw_bound() -> None:
    a_total, b_total, coefficients = saw_bound_a_b(15)
    if (a_total, b_total) != (639862, 452048):
        raise AssertionError(f"unexpected A+B sqrt(2) values: {a_total}, {b_total}")

    sqrt2_upper = Fraction(99, 70)
    lhs = Fraction(a_total) + b_total * sqrt2_upper
    rhs = Fraction(100, 39) ** 15
    if not lhs < rhs:
        raise AssertionError("length-15 SAW bound does not beat (100/39)^15")

    print("endpoint_coefficients=")
    for key in sorted(coefficients):
        print(f"  {key}: {coefficients[key]}")
    print(f"saw_bound=A+B*sqrt(2), A={a_total}, B={b_total}")
    print(f"rational_upper_using_99_over_70={lhs}")
    print(f"target=(100/39)^15={rhs}")


def main() -> None:
    verify_branching()
    verify_saw_bound()
    print("T_3 x K_2 certificate checks passed")


if __name__ == "__main__":
    main()

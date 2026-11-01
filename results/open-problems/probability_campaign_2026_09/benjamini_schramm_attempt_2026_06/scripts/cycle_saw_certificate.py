"""Exact certificate for T_4 x C_m finite-cycle bounds.

This verifies the arithmetic used for the manuscript's T_4 x C_m corollary.
The length-11 SAW endpoint coefficients are recomputed by a quotient dynamic
program and then checked against the coefficient certificates used in the
operator inequalities.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from typing import Optional

Node = tuple[tuple[int, ...], Optional[int], tuple["Node", ...]]


SPHERE_NORMS_D4 = [
    (1, 0),
    (0, 2),
    (8, 0),
    (0, 10),
    (36, 0),
    (0, 42),
    (144, 0),
    (0, 162),
    (540, 0),
    (0, 594),
    (1944, 0),
    (0, 2106),
]

COEFFICIENTS = {
    "C3": [15288, 23538, 27544, 26398, 20924, 13860, 7488, 3202, 1000, 200, 22, 1],
    "C4": [64320, 61356, 60716, 47806, 32046, 18262, 8736, 3426, 1018, 200, 22, 1],
    "Cge5": [
        141050,
        120742,
        92376,
        61444,
        36592,
        19364,
        8918,
        3442,
        1018,
        200,
        22,
        1,
    ],
}


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


def vertical_moves(node: Node, m: int) -> list[tuple[int, Node]]:
    layers, marker, children = node
    if marker is not None:
        output: dict[Node, int] = defaultdict(int)
        for delta in (-1, 1):
            next_layer = (marker + delta) % m
            if next_layer in layers:
                continue
            next_layers = tuple(sorted(layers + (next_layer,)))
            output[(next_layers, next_layer, children)] += 1
        return [(multiplicity, state) for state, multiplicity in output.items()]

    for index, child in enumerate(children):
        moved_children = vertical_moves(child, m)
        if moved_children:
            return [
                (multiplicity, (layers, None, replace_child(children, index, moved_child)))
                for multiplicity, moved_child in moved_children
            ]
    return []


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


def transitions(state: Node, degree: int, m: int) -> list[tuple[int, Node]]:
    output = vertical_moves(state, m)

    next_state = parent_move(state)
    if next_state is not None:
        output.append((1, next_state))

    output.extend(child_moves(state, degree))
    return output


def endpoint_radius_coefficients(degree: int, m: int, length: int) -> list[int]:
    states: dict[Node, int] = {((0,), 0, ()): 1}
    for _step in range(length):
        next_states: dict[Node, int] = defaultdict(int)
        for state, count in states.items():
            for multiplicity, next_state in transitions(state, degree, m):
                next_states[next_state] += count * multiplicity
        states = dict(next_states)

    totals: dict[tuple[int, int], int] = defaultdict(int)
    for state, count in states.items():
        result = current_depth_layer(state)
        if result is None:
            raise RuntimeError("state has no current marker")
        totals[result] += count

    radius_totals = [0 for _ in range(length + 1)]
    q = degree - 1
    for (radius, _layer), total in totals.items():
        sphere_size = 1 if radius == 0 else degree * q ** (radius - 1)
        if total % sphere_size != 0:
            raise ArithmeticError(
                f"endpoint count {total} is not divisible by sphere size "
                f"{sphere_size} for radius={radius}"
            )
        radius_totals[radius] += total // sphere_size
    return radius_totals


def cycle_cluster_phi(m: int, p: Fraction) -> Fraction:
    total = Fraction(0)
    for size in range(1, m):
        probability = size * (1 - p) ** 2 * p ** (size - 1)
        total += probability * (1 - (1 - p) ** size)
    full_probability = p ** (m - 1) * (m - (m - 1) * p)
    total += full_probability * (1 - (1 - p) ** m)
    return total


def local_cluster_phi(p: Fraction, depth: int) -> Fraction:
    probabilities = [p**k * (1 - p) for k in range(depth)] + [p**depth]
    total = Fraction(0)
    for left, left_probability in enumerate(probabilities):
        for right, right_probability in enumerate(probabilities):
            size = 1 + left + right
            total += left_probability * right_probability * (1 - (1 - p) ** size)
    return total


def operator_bound(coefficients: list[int]) -> tuple[int, int]:
    a_total = 0
    b_total = 0
    for coefficient, (a_part, b_part) in zip(coefficients, SPHERE_NORMS_D4):
        a_total += coefficient * a_part
        b_total += coefficient * b_part
    return a_total, b_total


def check_operator(name: str, target: Fraction, expected: tuple[int, int]) -> None:
    a_total, b_total = operator_bound(COEFFICIENTS[name])
    if (a_total, b_total) != expected:
        raise AssertionError(f"{name}: unexpected A+B sqrt(3) values {(a_total, b_total)}")
    sqrt3_upper = Fraction(97, 56)
    lhs = Fraction(a_total) + b_total * sqrt3_upper
    rhs = target**11
    if not lhs < rhs:
        raise AssertionError(f"{name}: operator bound does not beat {target}^11")
    print(f"{name}: A={a_total}, B={b_total}, rational_upper={lhs}, target={rhs}")


def verify_endpoint_certificates() -> None:
    exact_c3 = endpoint_radius_coefficients(4, 3, 11)
    if exact_c3 != COEFFICIENTS["C3"]:
        raise AssertionError(f"C3: endpoint coefficients changed: {exact_c3}")
    print(f"C3: endpoint_coefficients={exact_c3}")

    exact_c4 = endpoint_radius_coefficients(4, 4, 11)
    if exact_c4 != COEFFICIENTS["C4"]:
        raise AssertionError(f"C4: endpoint coefficients changed: {exact_c4}")
    print(f"C4: endpoint_coefficients={exact_c4}")

    majorant = COEFFICIENTS["Cge5"]
    for m in range(5, 13):
        coefficients = endpoint_radius_coefficients(4, m, 11)
        if any(coefficient > bound for coefficient, bound in zip(coefficients, majorant)):
            raise AssertionError(f"C{m}: coefficients exceed majorant: {coefficients}")
        print(f"C{m}: endpoint_coefficients<={majorant}")


def main() -> None:
    p_c3 = Fraction(6, 25)
    p_c4 = Fraction(19, 80)
    p_cge5 = Fraction(47, 200)

    verify_endpoint_certificates()

    checks = [
        ("C3", 3 * cycle_cluster_phi(3, p_c3), Fraction(1), 1 / p_c3, (2649944, 1532806)),
        ("C4", 3 * cycle_cluster_phi(4, p_c4), Fraction(1), 1 / p_c4, (3554176, 2043694)),
        (
            "C5",
            3 * cycle_cluster_phi(5, p_cge5),
            Fraction(1),
            1 / p_cge5,
            (4074050, 2347722),
        ),
        (
            "C6",
            3 * cycle_cluster_phi(6, p_cge5),
            Fraction(1),
            1 / p_cge5,
            (4074050, 2347722),
        ),
        (
            "Cge7-local",
            3 * local_cluster_phi(p_cge5, 3),
            Fraction(1),
            1 / p_cge5,
            (4074050, 2347722),
        ),
    ]

    for name, value, threshold, target, expected_operator in checks:
        if value <= threshold:
            raise AssertionError(f"{name}: cluster branching check failed: {value}")
        print(f"{name}: cluster_value={value}")
        operator_name = "Cge5" if name in {"C5", "C6", "Cge7-local"} else name
        check_operator(operator_name, target, expected_operator)

    print("T_4 x C_m certificate checks passed")


if __name__ == "__main__":
    main()

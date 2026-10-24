"""Exact verifier for finite-state nonbacktracking certificate algebra.

This checks the Collatz-Wielandt algebra in the finite-state certificate
criteria from the manuscript.  It verifies, using exact rational arithmetic,
that a nonnegative matrix M has spectral radius at most a claimed lambda via a
positive vector v satisfying Mv <= lambda v, and then checks either

    (q * (D - 1) * lambda)^2 * R < 1.

for the regular bridge-probability criterion, or

    (q * lambda)^2 * R < 1.

for the bounded-degree detour-count criterion.

Here q is an upper bound on p_c and R is an upper bound on
rho_{sph,2}(G)^2.

The script does not generally verify the graph-specific majorization
inequality.  That part must be justified by the finite-state construction
producing the certificate, except for the built-in regular-tree one-state
calibration checks.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(value: Any) -> Fraction:
    if isinstance(value, int):
        return Fraction(value, 1)
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError(f"expected integer or rational string, got {value!r}")


def parse_vector(values: list[Any], name: str) -> list[Fraction]:
    if not isinstance(values, list) or not values:
        raise ValueError(f"{name} must be a non-empty list")
    return [parse_fraction(value) for value in values]


def parse_matrix(values: list[list[Any]]) -> list[list[Fraction]]:
    if not isinstance(values, list) or not values:
        raise ValueError("matrix must be a non-empty list of rows")
    matrix = [[parse_fraction(value) for value in row] for row in values]
    width = len(matrix[0])
    if width == 0:
        raise ValueError("matrix rows must be non-empty")
    for index, row in enumerate(matrix):
        if len(row) != width:
            raise ValueError(f"matrix row {index} has length {len(row)}, expected {width}")
    if len(matrix) != width:
        raise ValueError(f"matrix must be square, got {len(matrix)}x{width}")
    return matrix


def dot(row: list[Fraction], vector: list[Fraction]) -> Fraction:
    return sum((entry * value for entry, value in zip(row, vector)), Fraction(0))


def require_field(data: dict[str, Any], key: str) -> Any:
    if key not in data:
        raise ValueError(f"missing required field {key!r}")
    return data[key]


def check_dimension(vector: list[Fraction], name: str, expected: int) -> None:
    if len(vector) != expected:
        raise ValueError(f"{name} has length {len(vector)}, expected {expected}")


def check_nonnegative_vector(vector: list[Fraction], name: str) -> None:
    if any(value < 0 for value in vector):
        raise ValueError(f"{name} entries must be nonnegative")
    if all(value == 0 for value in vector):
        raise ValueError(f"{name} must have at least one positive entry")


def verify_regular_tree_one_state_majorization(
    degree: int,
    matrix: list[list[Fraction]],
    left_vector: list[Fraction],
    right_vector: list[Fraction],
) -> None:
    if len(matrix) != 1:
        raise ValueError("regular_tree_one_state majorization requires one state")

    transition = matrix[0][0]
    amplitude = left_vector[0] * right_vector[0]
    tree_rate = Fraction(1, degree - 1)
    tree_prefactor = Fraction(degree - 1, degree)

    if transition <= 0:
        raise ValueError("regular_tree_one_state transition must be positive")

    if transition < tree_rate:
        raise ValueError(
            "regular_tree_one_state majorization fails: "
            f"transition {transition} < tree bridge rate {tree_rate}"
        )

    if transition == tree_rate:
        if amplitude < tree_prefactor:
            raise ValueError(
                "regular_tree_one_state majorization fails: "
                f"left*right = {amplitude} < {tree_prefactor}"
            )
        return

    if amplitude * transition < tree_prefactor * tree_rate:
        raise ValueError(
            "regular_tree_one_state majorization fails at n=1: "
            f"left*right*transition = {amplitude * transition} "
            f"< {tree_prefactor * tree_rate}"
        )


def verify_tree_count_one_state_majorization(
    matrix: list[list[Fraction]],
    left_vector: list[Fraction],
    right_vector: list[Fraction],
) -> None:
    if len(matrix) != 1:
        raise ValueError("tree_count_one_state majorization requires one state")

    transition = matrix[0][0]
    amplitude = left_vector[0] * right_vector[0]
    if transition < 1:
        raise ValueError(
            "tree_count_one_state majorization fails: "
            f"transition {transition} < 1"
        )
    if amplitude < 1:
        raise ValueError(
            "tree_count_one_state majorization fails: "
            f"left*right = {amplitude} < 1"
        )


def verify_certificate(data: dict[str, Any]) -> dict[str, Fraction]:
    criterion = data.get("criterion", "regular_bridge")
    if criterion not in {"regular_bridge", "bounded_degree_detour"}:
        raise ValueError(
            f"unsupported criterion {criterion!r}; "
            "supported: 'regular_bridge', 'bounded_degree_detour'"
        )

    degree = int(require_field(data, "degree"))
    if degree < 3:
        raise ValueError("degree must be at least 3")

    q = parse_fraction(require_field(data, "pc_upper"))
    if not (0 < q < 1):
        raise ValueError("pc_upper must be in (0, 1)")

    rho_sphere_sq = parse_fraction(require_field(data, "rho_sphere_upper_sq"))
    if rho_sphere_sq <= 0:
        raise ValueError("rho_sphere_upper_sq must be positive")

    lambda_upper = parse_fraction(require_field(data, "lambda_upper"))
    if lambda_upper <= 0:
        raise ValueError("lambda_upper must be positive")

    matrix = parse_matrix(require_field(data, "matrix"))
    dimension = len(matrix)

    left_vector = parse_vector(require_field(data, "left_vector"), "left_vector")
    right_vector = parse_vector(require_field(data, "right_vector"), "right_vector")
    check_dimension(left_vector, "left_vector", dimension)
    check_dimension(right_vector, "right_vector", dimension)
    check_nonnegative_vector(left_vector, "left_vector")
    check_nonnegative_vector(right_vector, "right_vector")

    vector = parse_vector(require_field(data, "positive_vector"), "positive_vector")
    check_dimension(vector, "positive_vector", dimension)
    if any(value <= 0 for value in vector):
        raise ValueError("positive_vector entries must be strictly positive")

    for row_index, row in enumerate(matrix):
        for col_index, entry in enumerate(row):
            if entry < 0:
                raise ValueError(
                    f"matrix entry ({row_index}, {col_index}) is negative: {entry}"
                )

    for row_index, row in enumerate(matrix):
        lhs = dot(row, vector)
        rhs = lambda_upper * vector[row_index]
        if lhs > rhs:
            raise ValueError(
                f"Collatz-Wielandt inequality fails at row {row_index}: "
                f"{lhs} > {rhs}"
            )

    majorization_checked = Fraction(0, 1)
    bridge_majorization = data.get("bridge_majorization")
    if bridge_majorization is not None:
        if bridge_majorization != "regular_tree_one_state":
            raise ValueError(
                "unsupported bridge_majorization "
                f"{bridge_majorization!r}; supported: 'regular_tree_one_state'"
            )
        verify_regular_tree_one_state_majorization(
            degree,
            matrix,
            left_vector,
            right_vector,
        )
        majorization_checked = Fraction(1, 1)

    detour_majorization = data.get("detour_majorization")
    if detour_majorization is not None:
        if detour_majorization not in {
            "tree_count_one_state",
            "regular_tree_count_one_state",
        }:
            raise ValueError(
                "unsupported detour_majorization "
                f"{detour_majorization!r}; supported: 'tree_count_one_state'"
            )
        if criterion != "bounded_degree_detour":
            raise ValueError(
                "detour_majorization requires criterion 'bounded_degree_detour'"
            )
        verify_tree_count_one_state_majorization(
            matrix,
            left_vector,
            right_vector,
        )
        majorization_checked = Fraction(1, 1)

    criterion_scale = Fraction(degree - 1, 1)
    if criterion == "bounded_degree_detour":
        criterion_scale = Fraction(1, 1)

    scale = q * criterion_scale * lambda_upper
    final_value = scale * scale * rho_sphere_sq
    if final_value >= 1:
        raise ValueError(
            "final strict inequality fails: "
            f"(q*scale*lambda)^2*R = {final_value} >= 1"
        )

    return {
        "degree": Fraction(degree, 1),
        "states": Fraction(dimension, 1),
        "criterion_scale": criterion_scale,
        "pc_upper": q,
        "lambda_upper": lambda_upper,
        "rho_sphere_upper_sq": rho_sphere_sq,
        "final_value": final_value,
        "majorization_checked": majorization_checked,
    }


def verify_path(path: Path) -> dict[str, Fraction]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("certificate JSON must be an object")
    return verify_certificate(data)


def run_self_tests() -> None:
    valid = {
        "criterion": "regular_bridge",
        "degree": 3,
        "pc_upper": "1/2",
        "rho_sphere_upper_sq": "2",
        "lambda_upper": "1/2",
        "matrix": [["1/2"]],
        "left_vector": ["1"],
        "right_vector": ["1"],
        "positive_vector": ["1"],
        "bridge_majorization": "regular_tree_one_state",
    }
    result = verify_certificate(valid)
    if result["final_value"] != Fraction(1, 2):
        raise AssertionError("valid certificate produced unexpected final value")

    valid_detour = {
        "criterion": "bounded_degree_detour",
        "degree": 3,
        "pc_upper": "1/2",
        "rho_sphere_upper_sq": "2",
        "lambda_upper": "1",
        "matrix": [["1"]],
        "left_vector": ["1"],
        "right_vector": ["1"],
        "positive_vector": ["1"],
        "detour_majorization": "tree_count_one_state",
    }
    result = verify_certificate(valid_detour)
    if result["final_value"] != Fraction(1, 2):
        raise AssertionError("valid detour certificate produced unexpected final value")

    failures = [
        (
            "unsupported criterion",
            {
                **valid,
                "criterion": "unknown_criterion",
            },
        ),
        (
            "negative matrix entry",
            {
                **valid,
                "matrix": [["-1/2"]],
            },
        ),
        (
            "nonpositive vector entry",
            {
                **valid,
                "positive_vector": ["0"],
            },
        ),
        (
            "negative left vector entry",
            {
                **valid,
                "left_vector": ["-1"],
            },
        ),
        (
            "zero right vector",
            {
                **valid,
                "right_vector": ["0"],
            },
        ),
        (
            "missing boundary vector",
            {
                key: value for key, value in valid.items() if key != "left_vector"
            },
        ),
        (
            "unsupported bridge majorization",
            {
                **valid,
                "bridge_majorization": "unknown_model",
            },
        ),
        (
            "regular tree transition too small",
            {
                **valid,
                "matrix": [["1/3"]],
            },
        ),
        (
            "regular tree boundary too small",
            {
                **valid,
                "left_vector": ["1/2"],
            },
        ),
        (
            "detour majorization with regular criterion",
            {
                **valid_detour,
                "criterion": "regular_bridge",
            },
        ),
        (
            "regular tree count transition too small",
            {
                **valid_detour,
                "matrix": [["1/2"]],
            },
        ),
        (
            "regular tree count boundary too small",
            {
                **valid_detour,
                "right_vector": ["1/2"],
            },
        ),
        (
            "Collatz inequality failure",
            {
                **valid,
                "lambda_upper": "1/3",
            },
        ),
        (
            "final strict inequality failure",
            {
                **valid,
                "lambda_upper": "1",
            },
        ),
    ]
    for name, certificate in failures:
        try:
            verify_certificate(certificate)
        except ValueError:
            continue
        raise AssertionError(f"expected failure for {name}")

    print("self-tests passed")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path, nargs="?", help="JSON certificate file")
    parser.add_argument(
        "--directory",
        type=Path,
        help="verify all JSON certificate files in this directory",
    )
    parser.add_argument("--self-test", action="store_true", help="run built-in verifier tests")
    args = parser.parse_args()

    if args.self_test:
        run_self_tests()
        return

    if args.certificate is not None and args.directory is not None:
        parser.error("use either a certificate file or --directory, not both")

    if args.directory is not None:
        paths = sorted(path for path in args.directory.glob("*.json") if path.is_file())
        if not paths:
            parser.error(f"no JSON certificate files found in {args.directory}")
        failures = 0
        for path in paths:
            try:
                result = verify_path(path)
            except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
                failures += 1
                print(f"{path}: failed: {exc}")
                continue
            print(
                f"{path}: verified; final_value: {result['final_value']}; "
                f"majorization_checked: {result['majorization_checked']}"
            )
        if failures:
            raise SystemExit(1)
        print(f"verified {len(paths)} certificate(s)")
        return

    if args.certificate is None:
        parser.error("certificate is required unless --self-test or --directory is used")

    result = verify_path(args.certificate)
    print("certificate algebra verified")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()

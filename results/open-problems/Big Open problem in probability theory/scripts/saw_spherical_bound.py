"""Finite-length SAW spherical bounds on T_d x Z.

This diagnostic enumerates length-n self-avoiding walks from the origin in
T_d x Z, groups endpoints by tree distance and height, and evaluates the
radial transform bound

    ||C_n|| <= sum_{r,h} a_{r,h} ||R_r||

where a_{r,h} is the number of SAWs from the origin to a fixed endpoint at
tree distance r and height h, and R_r is the tree sphere kernel.

For T_d x Z this bound is attained by the spherical/Fourier character at the
edge of the tree spectrum and at vertical frequency 0 or pi, since every
length-n endpoint has r+h congruent to n modulo 2.

For d=3 the tree-sphere norms lie in Z + Z sqrt(2), so the script also reports
the exact A + B sqrt(2) form.
"""

from __future__ import annotations

import argparse
import math
import time
from collections import defaultdict


def move_word(word: tuple[int, ...], generator: int) -> tuple[int, ...]:
    if word and word[-1] == generator:
        return word[:-1]
    return word + (generator,)


def enumerate_saw_endpoint_coefficients(d: int, n: int) -> dict[tuple[int, int], int]:
    counts: dict[tuple[int, int], int] = defaultdict(int)
    visited = {((), 0)}

    def rec(word: tuple[int, ...], height: int, steps: int) -> None:
        if steps == n:
            counts[(len(word), height)] += 1
            return

        for generator in range(d):
            next_word = move_word(word, generator)
            vertex = (next_word, height)
            if vertex not in visited:
                visited.add(vertex)
                rec(next_word, height, steps + 1)
                visited.remove(vertex)

        for delta in (-1, 1):
            vertex = (word, height + delta)
            if vertex not in visited:
                visited.add(vertex)
                rec(word, height + delta, steps + 1)
                visited.remove(vertex)

    rec((), 0, 0)

    q = d - 1
    coefficients: dict[tuple[int, int], int] = {}
    for (radius, height), total in counts.items():
        sphere_size = 1 if radius == 0 else d * q ** (radius - 1)
        if total % sphere_size != 0:
            raise ArithmeticError(
                f"endpoint count {total} is not divisible by sphere size "
                f"{sphere_size} for radius={radius}, height={height}"
            )
        coefficients[(radius, height)] = total // sphere_size
    return coefficients


def tree_sphere_norms(d: int, n: int) -> list[float]:
    q = d - 1
    edge = 2.0 * math.sqrt(q)
    values = [0.0] * (n + 1)
    values[0] = 1.0
    if n >= 1:
        values[1] = edge
    if n >= 2:
        values[2] = edge * edge - d
    for radius in range(2, n):
        values[radius + 1] = edge * values[radius] - q * values[radius - 1]
    return values


def tree_sphere_norms_d3_exact(n: int) -> list[tuple[int, int]]:
    """Return pairs (a,b) representing a + b sqrt(2) for d=3."""
    values: list[tuple[int, int]] = [(1, 0)]
    if n >= 1:
        values.append((0, 2))
    if n >= 2:
        values.append((5, 0))
    for radius in range(2, n):
        a, b = values[radius]
        c, e = values[radius - 1]
        # P_{r+1} = 2 sqrt(2) P_r - 2 P_{r-1}.
        values.append((4 * b - 2 * c, 2 * a - 2 * e))
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--degree", type=int, default=3)
    parser.add_argument("--length", type=int, default=12)
    args = parser.parse_args()

    start = time.time()
    coefficients = enumerate_saw_endpoint_coefficients(args.degree, args.length)
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

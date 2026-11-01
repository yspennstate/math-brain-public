#!/usr/bin/env python3
"""Exact finite-box check of the two-tag contact Green identity.

Uses Fraction arithmetic and independently constructs (i) killed discrete SRW
and (ii) the relative process of two chronological interchange labels.
Finite calculation only; the infinite-volume proof is in agents/004.md.
"""
from fractions import Fraction as F
from itertools import product
import json


def solve(matrix, rhs):
    a = [[F(x) for x in row] + [F(y)] for row, y in zip(matrix, rhs)]
    n = len(a)
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        factor = a[col][col]
        a[col] = [x / factor for x in a[col]]
        for row in range(n):
            if row != col and a[row][col]:
                factor = a[row][col]
                a[row] = [x - factor * y for x, y in zip(a[row], a[col])]
    return [row[-1] for row in a]


def check(dimension=3, radius=1):
    origin = (0,) * dimension
    box = list(product(range(-radius, radius + 1), repeat=dimension))
    index = {x: i for i, x in enumerate(box)}
    steps = []
    for axis in range(dimension):
        for sign in (-1, 1):
            e = [0] * dimension
            e[axis] = sign
            steps.append(tuple(e))

    # G = (I - P_killed)^(-1) delta_0, discrete time SRW normalization.
    n = len(box)
    matrix = [[F(i == j) for j in range(n)] for i in range(n)]
    for x, i in index.items():
        for e in steps:
            y = tuple(a + b for a, b in zip(x, e))
            if y in index:
                matrix[i][index[y]] -= F(1, 2 * dimension)
    green = solve(matrix, [x == origin for x in box])

    # The pair-relative chain never visits zero. Adjacent labels swap at rate
    # one; every other allowed nearest-neighbor relative move has rate two.
    states = [x for x in box if x != origin]
    pair_index = {x: i for i, x in enumerate(states)}
    m = len(states)
    negative_generator = [[F(0) for _ in states] for _ in states]
    for x, i in pair_index.items():
        for e in steps:
            y = tuple(a + b for a, b in zip(x, e))
            if y == origin:
                continue
            negative_generator[i][i] += 2
            if y in pair_index:
                negative_generator[i][pair_index[y]] -= 2
        if sum(map(abs, x)) == 1:
            y = tuple(-a for a in x)
            negative_generator[i][i] += 1
            negative_generator[i][pair_index[y]] -= 1
    contact = solve(negative_generator, [sum(map(abs, x)) == 1 for x in states])
    for x, i in pair_index.items():
        assert contact[i] == green[index[x]] / 2, x
    a = (1,) + (0,) * (dimension - 1)
    assert green[index[origin]] - green[index[a]] == 1
    assert negative_generator[pair_index[a]][pair_index[a]] == 4 * dimension - 1
    return {
        "dimension": dimension,
        "box_radius": radius,
        "srw_states": n,
        "pair_states": m,
        "G_box_0": str(green[index[origin]]),
        "G_box_e1": str(green[index[a]]),
        "pair_adjacency_mean_e1": str(contact[pair_index[a]]),
        "all_states_G_over_2": True,
        "arithmetic": "exact rational",
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

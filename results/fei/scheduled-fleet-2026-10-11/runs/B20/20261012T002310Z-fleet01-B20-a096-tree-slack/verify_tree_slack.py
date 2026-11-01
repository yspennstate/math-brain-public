#!/usr/bin/env python3
"""Deterministic diagnostics for the fixed-root restriction-tree telescope.

The all-dimensional theorem is algebraic.  This script checks conventions on
genuine Boolean truth tables: every function through 3 variables and one
representative of each output-complement pair on 4 variables.
"""

from functools import lru_cache
from itertools import combinations, product
from math import ceil, log2

TOL = 2.0e-10


def fwht(values):
    a = values[:]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2 * h):
            for k in range(j, j + h):
                x, y = a[k], a[k + h]
                a[k], a[k + h] = x + y, x - y
        h *= 2
    return a


@lru_cache(None)
def metrics(n, mask):
    size = 1 << n
    vals = [1 if (mask >> x) & 1 else -1 for x in range(size)]
    sums = fwht(vals)
    denom = float(size * size)
    probs = [(z * z) / denom for z in sums]
    entropy = -sum(p * log2(p) for p in probs if p)
    influence = sum(s.bit_count() * probs[s] for s in range(size))
    directional = tuple(
        sum(probs[s] for s in range(size) if (s >> i) & 1)
        for i in range(n)
    )
    return entropy, influence, directional


@lru_cache(None)
def restrict_mask(n, mask, coordinate, value):
    assert 0 <= coordinate < n and value in (0, 1)
    child = 0
    for y in range(1 << (n - 1)):
        low = y & ((1 << coordinate) - 1)
        high = y >> coordinate
        x = low | (value << coordinate) | (high << (coordinate + 1))
        if (mask >> x) & 1:
            child |= 1 << y
    return child


def deficit(R, n, mask):
    H, I, _ = metrics(n, mask)
    return R * I - H


def local_slack(R, n, mask, i):
    H, I, Is = metrics(n, mask)
    children = [restrict_mask(n, mask, i, b) for b in (0, 1)]
    Hbar = sum(metrics(n - 1, c)[0] for c in children) / 2.0
    return H - Hbar - R * Is[i], children


def choose_coordinate(n, mask):
    directional = metrics(n, mask)[2]
    return max(range(n), key=lambda i: (directional[i], -i))


def tree_account(R, n, mask, max_depth, depth=0, weight=1.0):
    H, I, _ = metrics(n, mask)
    if n == 0 or I <= TOL or depth >= max_depth:
        return weight * deficit(R, n, mask), 0.0, 1, 0
    i = choose_coordinate(n, mask)
    slack, children = local_slack(R, n, mask, i)
    leaf_D = 0.0
    internal = weight * slack
    leaves = 0
    nodes = 1
    for child in children:
        d, s, l, q = tree_account(
            R, n - 1, child, max_depth, depth + 1, weight / 2.0
        )
        leaf_D += d
        internal += s
        leaves += l
        nodes += q
    return leaf_D, internal, leaves, nodes


def all_physical_descendant_ratios(n, mask):
    ratios = []
    coords = range(n)
    for k in range(1, n + 1):
        for fixed in combinations(coords, k):
            for bits in product((0, 1), repeat=k):
                nn, mm = n, mask
                # Remove coordinates in descending order so indices remain valid.
                for i, b in sorted(zip(fixed, bits), reverse=True):
                    mm = restrict_mask(nn, mm, i, b)
                    nn -= 1
                H, I, _ = metrics(nn, mm)
                if I > TOL:
                    ratios.append(H / I)
    return ratios


def main():
    roots = local_edges = tree_nodes = pruned_leaves = critical_roots = 0
    max_local_error = max_tree_error = max_full_error = 0.0
    min_critical_terminal = float("inf")
    for n in range(1, 5):
        masks = range(1 << (1 << n))
        if n == 4:
            # Output complementation preserves every tested quantity.
            masks = range(0, 1 << (1 << n), 2)
        for mask in masks:
            H, I, Is = metrics(n, mask)
            if I <= TOL:
                continue
            roots += 1
            R = H / I
            for i in range(n):
                if Is[i] <= TOL:
                    continue
                s, children = local_slack(R, n, mask, i)
                rhs = sum(deficit(R, n - 1, c) for c in children) / 2.0
                err = abs((deficit(R, n, mask) + s) - rhs)
                max_local_error = max(max_local_error, err)
                assert err <= TOL
                local_edges += 1

            stop = ceil(n / 2)
            leaf_D, slack_sum, leaves, nodes = tree_account(R, n, mask, stop)
            err = abs(leaf_D - slack_sum)  # root deficit is exactly zero.
            max_tree_error = max(max_tree_error, err)
            assert err <= 5 * TOL
            pruned_leaves += leaves
            tree_nodes += nodes

            full_D, full_slack, _, nodes = tree_account(R, n, mask, n)
            err = max(abs(full_D), abs(full_slack), abs(full_D - full_slack))
            max_full_error = max(max_full_error, err)
            assert err <= 10 * TOL
            tree_nodes += nodes

            descendants = all_physical_descendant_ratios(n, mask)
            if not descendants or max(descendants) <= R + TOL:
                critical_roots += 1
                min_critical_terminal = min(min_critical_terminal, leaf_D)
                assert leaf_D >= -5 * TOL
                assert slack_sum >= -5 * TOL

    print("PASS fixed-root restriction-tree telescope")
    print(f"genuine Boolean roots checked: {roots}")
    print(f"relevant local edge identities: {local_edges}")
    print(f"tree nodes visited: {tree_nodes}")
    print(f"pruned leaves checked: {pruned_leaves}")
    print(f"descendant-critical roots: {critical_roots}")
    print(f"max local identity error: {max_local_error:.3e}")
    print(f"max pruned telescope error: {max_tree_error:.3e}")
    print(f"max full-tree zero error: {max_full_error:.3e}")
    print(f"minimum critical terminal deficit: {min_critical_terminal:.3e}")


if __name__ == "__main__":
    main()

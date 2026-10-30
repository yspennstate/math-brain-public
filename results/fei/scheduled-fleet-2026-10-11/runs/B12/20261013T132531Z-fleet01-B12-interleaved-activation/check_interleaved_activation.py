#!/usr/bin/env python3
"""Exhaustive controls for the disjoint interleaved-activation theorem."""

from __future__ import annotations

from functools import lru_cache
import math


def psi(t: float) -> float:
    z = t * t
    return 0.0 if z == 0.0 else z * math.log(1.0 / z)


def kernel(x: float, y: float) -> float:
    return psi(x) + psi(y) - 0.5 * (psi(x + y) + psi(x - y))


@lru_cache(maxsize=None)
def walsh(values: tuple[float, ...]) -> tuple[float, ...]:
    a = list(values)
    n = len(a)
    step = 1
    while step < n:
        for start in range(0, n, 2 * step):
            for j in range(start, start + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return tuple(x / n for x in a)


@lru_cache(maxsize=None)
def entropy(values: tuple[float, ...]) -> float:
    return sum(psi(c) for c in walsh(values))


def restrict(values: tuple[float, ...], coordinate: int, bit: int) -> tuple[float, ...]:
    return tuple(v for idx, v in enumerate(values) if ((idx >> coordinate) & 1) == bit)


def tensor_composite(a: tuple[float, ...], b: tuple[float, ...], h: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(aa + hh * bb for hh in h for aa, bb in zip(a, b))


def defect(a: tuple[float, ...], b: tuple[float, ...], h: tuple[float, ...]) -> float:
    q = sum(x * x for x in b) / len(b)
    return entropy(tensor_composite(a, b, h)) - q * entropy(h)


def activation_decrement(a: tuple[float, ...], b: tuple[float, ...], h: tuple[float, ...], j: int) -> float:
    f = tensor_composite(a, b, h)
    m = int(math.log2(len(a)))
    # Activation coordinates occupy the low-order bits in tensor_composite.
    return entropy(f) - 0.5 * (
        entropy(restrict(f, j, 0)) + entropy(restrict(f, j, 1))
    )


def adaptive_extrema(a: tuple[float, ...], b: tuple[float, ...], h: tuple[float, ...]):
    """Min/max source-remainder sum over all adaptive next-coordinate choices."""

    @lru_cache(maxsize=None)
    def rec(a, b, h):
        nw = int(math.log2(len(a)))
        nx = int(math.log2(len(h)))
        if nx == 0:
            return 0.0, 0.0, 1
        vals = []
        policies = 0
        j0 = defect(a, b, h)
        for i in range(nx):
            h0, h1 = restrict(h, i, 0), restrict(h, i, 1)
            r = j0 - 0.5 * (defect(a, b, h0) + defect(a, b, h1))
            lo0, hi0, c0 = rec(a, b, h0)
            lo1, hi1, c1 = rec(a, b, h1)
            vals.append((r + 0.5 * (lo0 + lo1), r + 0.5 * (hi0 + hi1)))
            policies += c0 * c1
        for j in range(nw):
            a0, a1 = restrict(a, j, 0), restrict(a, j, 1)
            b0, b1 = restrict(b, j, 0), restrict(b, j, 1)
            lo0, hi0, c0 = rec(a0, b0, h)
            lo1, hi1, c1 = rec(a1, b1, h)
            vals.append((0.5 * (lo0 + lo1), 0.5 * (hi0 + hi1)))
            policies += c0 * c1
        return min(x[0] for x in vals), max(x[1] for x in vals), policies

    return rec(a, b, h)


def signs(n: int):
    size = 1 << n
    for mask in range(1 << size):
        yield tuple(1.0 if ((mask >> j) & 1) else -1.0 for j in range(size))


def main() -> None:
    # Scalar nonnegativity and sharp upper envelope on a dense feasible grid.
    min_k = (1.0, None)
    max_env = (-1.0, None)
    grid = 1_000_000
    for j in range(grid + 1):
        t = j / grid
        x, y = 0.5 * (1.0 + t), 0.5 * (1.0 - t)
        k = kernel(x, y)
        if k < min_k[0]:
            min_k = (k, t)
        # Avoid cancellation in this diagnostic ratio when y is below the
        # double-precision resolution relevant to the numerator.
        if y >= 1e-4:
            env = (k - psi(y)) / (y * y)
            if env > max_env[0]:
                max_env = (env, t)
        if k < -2e-14:
            raise AssertionError(("negative kernel", t, k))

    triples = 0
    activation_nodes = 0
    max_bound_excess = -1e99
    min_activation_decrement = 1e99
    max_selector_ratio = 0.0

    for nw in range(3):
        branches = list(signs(nw))
        for fp in branches:
            for fm in branches:
                a = tuple((x + y) / 2.0 for x, y in zip(fp, fm))
                b = tuple((x - y) / 2.0 for x, y in zip(fp, fm))
                for nx in range(3):
                    for h in signs(nx):
                        triples += 1
                        root = defect(a, b, h)
                        lo, hi, _ = adaptive_extrema(a, b, h)
                        excess = hi - root
                        max_bound_excess = max(max_bound_excess, excess)
                        if excess > 2e-13:
                            raise AssertionError(("adaptive bound", nw, nx, fp, fm, h, root, hi))
                        for j in range(nw):
                            dz = activation_decrement(a, b, h, j)
                            min_activation_decrement = min(min_activation_decrement, dz)
                            activation_nodes += 1
                            if dz < -3e-13:
                                raise AssertionError(("activation decrement", dz))

    # Arbitrary selector sources through four variables, including all possible
    # interleavings with the selector coordinate.
    selector_functions = 0
    a = (0.0, 1.0)  # low bit convention: x=-1,+1 up to harmless orientation
    b = (1.0, 0.0)
    for nx in range(5):
        source_list = list(signs(nx))
        if nx == 4:
            size = 1 << nx
            selected_masks = (1, (1 << size) - 2, (1 << (size // 2)) - 1, 0x6996)
            source_list = [
                tuple(1.0 if ((mask >> j) & 1) else -1.0 for j in range(size))
                for mask in selected_masks
            ]
        for h in source_list:
            selector_functions += 1
            _, hi, _ = adaptive_extrema(a, b, h)
            p = sum(1 for z in h if z == 1.0) / len(h)
            denom = 8.0 * p * math.log(2.0)
            if denom > 0:
                max_selector_ratio = max(max_selector_ratio, hi / denom)
            if hi > denom + 3e-13:
                raise AssertionError(("selector reserve", nx, p, hi, denom))

    print(f"Scalar boundary grid points: {grid + 1}")
    print(f"Minimum feasible kernel on grid: {min_k[0]:.17g} at t={min_k[1]}")
    print(f"Largest (K-psi(y))/y^2 on boundary grid: {max_env[0]:.15f}")
    print(f"Boolean activation/source triples checked: {triples}")
    print(f"Activation-node decrements checked: {activation_nodes}")
    print(f"Minimum activation decrement: {min_activation_decrement:.3e}")
    print(f"Maximum adaptive-sum minus root-defect excess: {max_bound_excess:.3e}")
    print(f"Selector source functions checked: {selector_functions}")
    print(f"Maximum interleaved selector ratio to 8 p ln2: {max_selector_ratio:.15f}")
    print("PASS")


if __name__ == "__main__":
    main()

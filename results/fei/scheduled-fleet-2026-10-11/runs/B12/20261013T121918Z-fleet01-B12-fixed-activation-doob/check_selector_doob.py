#!/usr/bin/env python3
"""Deterministic checks for the fixed-activation Doob bridge.

No random seed is used.  Fourier transforms use the uniform Walsh basis.
"""

from __future__ import annotations

import itertools
import math


LN2 = math.log(2.0)


def psi(t: float) -> float:
    if t == 0.0:
        return 0.0
    z = t * t
    return z * math.log(1.0 / z)


def kernel(x: float, y: float) -> float:
    return psi(x) + psi(y) - 0.5 * (psi(x + y) + psi(x - y))


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


def entropy(values: tuple[float, ...]) -> float:
    return sum(psi(c) for c in walsh(values))


def restrict(values: tuple[float, ...], coordinate: int, bit: int) -> tuple[float, ...]:
    return tuple(v for idx, v in enumerate(values) if ((idx >> coordinate) & 1) == bit)


def selector_entropy(h: tuple[float, ...]) -> float:
    hc = walsh(h)
    out = []
    for mask, c in enumerate(hc):
        delta = 1.0 if mask == 0 else 0.0
        out.append(0.5 * (delta + c))
        out.append(0.5 * (delta - c))
    return sum(psi(c) for c in out)


def defect(h: tuple[float, ...]) -> float:
    return selector_entropy(h) - 0.5 * entropy(h)


def q_scalar(p: float) -> float:
    return (
        psi(p)
        + psi(1.0 - p)
        - 0.5 * psi(2.0 * p - 1.0)
        + 4.0 * p * (1.0 - p) * LN2
    )


def local_kernel_remainder(h: tuple[float, ...], coordinate: int) -> float:
    hc = walsh(h)
    mu = hc[0]
    alpha = hc[1 << coordinate]
    # a=(1+x)/2 and b=(1-x)/2 have ratios a_T/b_T equal to +1,-1
    # and squared b-coefficients 1/4,1/4.
    return 0.25 * (
        kernel(1.0 + mu, alpha)
        + kernel(-1.0 + mu, alpha)
        - 2.0 * kernel(mu, alpha)
    )


def tree_kernel_sum(h: tuple[float, ...], order: tuple[int, ...], weight: float = 1.0) -> float:
    if not order:
        return 0.0
    i = order[0]
    r = weight * local_kernel_remainder(h, i)
    h0, h1 = restrict(h, i, 0), restrict(h, i, 1)
    tail = tuple(j - (j > i) for j in order[1:])
    return r + tree_kernel_sum(h0, tail, weight / 2.0) + tree_kernel_sum(h1, tail, weight / 2.0)


def main() -> None:
    functions = 0
    local_checks = 0
    tree_checks = 0
    max_scalar_residual = 0.0
    max_local_residual = 0.0
    max_tree_residual = 0.0
    max_bound_ratio = 0.0

    selected = []
    for n in range(5):
        size = 1 << n
        for mask in range(1 << size):
            h = tuple(1.0 if ((mask >> j) & 1) else -1.0 for j in range(size))
            functions += 1
            p = sum(1 for x in h if x == 1.0) / size
            jh = defect(h)
            qs = q_scalar(p)
            max_scalar_residual = max(max_scalar_residual, abs(jh - qs))
            denom = 8.0 * p * LN2
            if denom > 0:
                max_bound_ratio = max(max_bound_ratio, qs / denom)
            if qs > denom + 2e-13:
                raise AssertionError(("scalar bound", n, mask, qs, denom))

            for i in range(n):
                h0, h1 = restrict(h, i, 0), restrict(h, i, 1)
                doob = jh - 0.5 * (defect(h0) + defect(h1))
                kr = local_kernel_remainder(h, i)
                max_local_residual = max(max_local_residual, abs(doob - kr))
                local_checks += 1

            if n <= 3 or mask in (1, (1 << size) - 2, (1 << (size // 2)) - 1):
                selected.append((n, h))

    for n, h in selected:
        for order in itertools.permutations(range(n)):
            got = tree_kernel_sum(h, order)
            want = defect(h)  # both terminal defects vanish
            max_tree_residual = max(max_tree_residual, abs(got - want))
            tree_checks += 1

    if max_scalar_residual > 2e-13:
        raise AssertionError(("scalar formula", max_scalar_residual))
    if max_local_residual > 3e-13:
        raise AssertionError(("local bridge", max_local_residual))
    if max_tree_residual > 5e-13:
        raise AssertionError(("tree telescope", max_tree_residual))

    # Independent dense scalar scan for the analytic envelope.
    dense_max = (0.0, 0.0)
    for j in range(1, 1_000_000):
        p = j / 1_000_000.0
        ratio = q_scalar(p) / (8.0 * p * LN2)
        if ratio > dense_max[0]:
            dense_max = (ratio, p)
        if ratio > 1.0 + 1e-12:
            raise AssertionError(("dense bound", p, ratio))

    print(f"Boolean functions checked: {functions}")
    print(f"Local kernel/Doob checks: {local_checks}")
    print(f"Complete ordered-tree checks: {tree_checks}")
    print(f"Maximum selector scalar identity residual: {max_scalar_residual:.3e}")
    print(f"Maximum local kernel identity residual: {max_local_residual:.3e}")
    print(f"Maximum full-tree telescope residual: {max_tree_residual:.3e}")
    print(f"Maximum Boolean-grid Q/(8 p ln2): {max_bound_ratio:.15f}")
    print(f"Dense scalar maximum Q/(8 p ln2): {dense_max[0]:.15f} at p={dense_max[1]:.6f}")
    print("PASS")


if __name__ == "__main__":
    main()

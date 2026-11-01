#!/usr/bin/env python3
"""Deterministic audit for the B12 changing-witness potential theorem.

Natural-log normalization.  The exhaustive phase checks every ordered pair
of Boolean source branches on two bits and every Boolean child through three
bits.  A dynamic program maximizes the accumulated exact coherent remainder
over all optional-stopping, adaptive, nonreusing interleavings of source and
child queries.
"""

from functools import lru_cache
from itertools import product
from math import e, log

C0 = 4.0 + 2.0 * log(2.0)
C = C0 + 2.0 / e
TOL = 2.0e-11


def psi(x):
    if x == 0.0:
        return 0.0
    return x * x * log(1.0 / (x * x))


def kernel(x, y):
    return psi(x) + psi(y) - 0.5 * (psi(x + y) + psi(x - y))


@lru_cache(maxsize=None)
def walsh(vals):
    a = list(map(float, vals))
    n = len(a)
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            for j in range(base, base + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return tuple(x / n for x in a)


def restrict(vals, n, coord, bit):
    return tuple(vals[k] for k in range(1 << n) if ((k >> coord) & 1) == bit)


@lru_cache(maxsize=None)
def source_data(gp, gm):
    ah = walsh(tuple((x + y) / 2.0 for x, y in zip(gp, gm)))
    bh = walsh(tuple((x - y) / 2.0 for x, y in zip(gp, gm)))
    q = sum(x * x for x in bh)
    z = sum(psi(x) for x in bh)
    reserve = sum(
        2.0 * b * b * log(abs(a) / abs(b))
        for a, b in zip(ah, bh)
        if b != 0.0 and abs(a) > abs(b)
    )
    return ah, bh, q, z, reserve


@lru_cache(maxsize=None)
def child_data(h):
    hh = walsh(h)
    mu = hh[0]
    var = 1.0 - mu * mu
    influence = sum(index.bit_count() * x * x for index, x in enumerate(hh))
    return hh, mu, var, influence


def inf_coordinate(h, coord):
    hh = walsh(h)
    return sum(x * x for index, x in enumerate(hh) if (index >> coord) & 1)


def remainder(gp, gm, h, coord):
    ah, bh, _, _, _ = source_data(gp, gm)
    hh, mu, _, _ = child_data(h)
    alpha = hh[1 << coord]
    return sum(
        kernel(a + mu * b, alpha * b) - b * b * kernel(mu, alpha)
        for a, b in zip(ah, bh)
    )


def potential(gp, gm, h):
    _, _, q, z, _ = source_data(gp, gm)
    _, _, var, influence = child_data(h)
    return C * q * influence + var * z


@lru_cache(maxsize=None)
def optimum(gp, gm, h, m, n):
    """Maximum future sum of exact R over every adaptive interleaving."""
    best = 0.0  # optional stopping
    for j in range(m):
        value = 0.5 * (
            optimum(restrict(gp, m, j, 0), restrict(gm, m, j, 0), h, m - 1, n)
            + optimum(restrict(gp, m, j, 1), restrict(gm, m, j, 1), h, m - 1, n)
        )
        best = max(best, value)
    for i in range(n):
        value = remainder(gp, gm, h, i) + 0.5 * (
            optimum(gp, gm, restrict(h, n, i, 0), m, n - 1)
            + optimum(gp, gm, restrict(h, n, i, 1), m, n - 1)
        )
        best = max(best, value)
    return best


def all_functions(n):
    return list(product((-1.0, 1.0), repeat=1 << n))


def main():
    local_source_checks = 0
    local_child_checks = 0
    max_source_error = 0.0
    max_child_error = 0.0
    min_local_slack = float("inf")
    max_reserve_excess = -float("inf")

    # Check all local source transitions through three source bits.
    for m in range(1, 4):
        fs = all_functions(m)
        for gp in fs:
            for gm in fs:
                _, _, q, z, reserve = source_data(gp, gm)
                max_reserve_excess = max(max_reserve_excess, reserve - z)
                for j in range(m):
                    children = [
                        source_data(restrict(gp, m, j, bit), restrict(gm, m, j, bit))
                        for bit in (0, 1)
                    ]
                    qbar = 0.5 * (children[0][2] + children[1][2])
                    zbar = 0.5 * (children[0][3] + children[1][3])
                    max_source_error = max(max_source_error, abs(q - qbar))
                    if zbar > z + TOL:
                        raise AssertionError(("source entropy increased", m, j, z, zbar))
                    local_source_checks += 1

    # Check the local Bellman inequality for all source pairs through two bits
    # and all child functions through three bits.
    source_pairs = []
    for m in range(0, 3):
        fs = all_functions(m)
        source_pairs.extend((m, gp, gm) for gp in fs for gm in fs)
    for m, gp, gm in source_pairs:
        ah, bh, q, z, reserve = source_data(gp, gm)
        max_reserve_excess = max(max_reserve_excess, reserve - z)
        for n in range(1, 4):
            for h in all_functions(n):
                _, _, var, influence = child_data(h)
                p = C * q * influence + var * z
                for i in range(n):
                    alpha = walsh(h)[1 << i]
                    infi = inf_coordinate(h, i)
                    kids = [child_data(restrict(h, n, i, bit)) for bit in (0, 1)]
                    varbar = 0.5 * (kids[0][2] + kids[1][2])
                    ibar = 0.5 * (kids[0][3] + kids[1][3])
                    max_child_error = max(
                        max_child_error,
                        abs((var - varbar) - alpha * alpha),
                        abs((influence - ibar) - infi),
                    )
                    r = remainder(gp, gm, h, i)
                    pbar = C * q * ibar + z * varbar
                    slack = p - pbar - r
                    min_local_slack = min(min_local_slack, slack)
                    if slack < -TOL:
                        raise AssertionError(("local potential failure", m, n, i, slack))
                    local_child_checks += 1

    # Full all-tree dynamic program: every two-bit source pair and every child
    # through three bits, including optional stopping and branch-dependent order.
    fs = all_functions(2)
    hs = all_functions(3)
    roots = 0
    min_global_slack = float("inf")
    max_ratio = 0.0
    argmax = None
    for gp in fs:
        for gm in fs:
            for h in hs:
                opt = optimum(gp, gm, h, 2, 3)
                p = potential(gp, gm, h)
                slack = p - opt
                min_global_slack = min(min_global_slack, slack)
                if p > TOL and opt / p > max_ratio:
                    max_ratio = opt / p
                    argmax = (gp, gm, h, opt, p)
                if slack < -TOL:
                    raise AssertionError(("global tree failure", slack, gp, gm, h, opt, p))
                roots += 1

    print("PASS")
    print(f"C_nats={C:.15f}")
    print(f"local_source_transitions={local_source_checks}")
    print(f"local_child_transitions={local_child_checks}")
    print(f"adaptive_interleaving_roots={roots}")
    print(f"max_source_parseval_error={max_source_error:.3e}")
    print(f"max_child_telescope_error={max_child_error:.3e}")
    print(f"max_M_minus_Eraw={max_reserve_excess:.3e}")
    print(f"min_local_potential_slack={min_local_slack:.15g}")
    print(f"min_global_potential_slack={min_global_slack:.15g}")
    print(f"max_optimum_over_potential={max_ratio:.15g}")
    print(f"argmax={argmax}")


if __name__ == "__main__":
    main()

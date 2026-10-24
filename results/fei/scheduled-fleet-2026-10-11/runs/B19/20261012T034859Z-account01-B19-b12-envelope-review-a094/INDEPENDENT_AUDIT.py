#!/usr/bin/env python3
"""Independent finite audit of the B12 uniform coherent-kernel envelope.

This does not prove an all-dimensional statement.  It reconstructs the
Fourier decrement from truth tables, compares it with the closed kernel
formula, checks the one-node envelope exhaustively for two outer bits and
children through three bits, and independently maximizes the signed charge
over every adaptive nonreusing restriction tree in the same finite scope.
Natural logarithms are used, as in the reviewed B12 claim.
"""

from functools import lru_cache
from itertools import product
from math import e, log

TOL = 2.0e-11


def psi(x):
    if x == 0.0:
        return 0.0
    return x * x * log(1.0 / (x * x))


def kernel(x, y):
    return psi(x) + psi(y) - 0.5 * (psi(x + y) + psi(x - y))


def fwht(values):
    a = [float(x) for x in values]
    step = 1
    while step < len(a):
        for base in range(0, len(a), 2 * step):
            for j in range(step):
                u, v = a[base + j], a[base + j + step]
                a[base + j], a[base + j + step] = u + v, u - v
        step *= 2
    scale = 1.0 / len(a)
    return [x * scale for x in a]


def raw_entropy(coeff):
    return sum(psi(x) for x in coeff)


def split_decrement_from_coeff(coeff, coordinate):
    bit = 1 << coordinate
    u, v = [], []
    for mask in range(len(coeff)):
        if not (mask & bit):
            u.append(coeff[mask])
            v.append(coeff[mask | bit])
    return raw_entropy(u) + raw_entropy(v) - 0.5 * (
        raw_entropy([x + y for x, y in zip(u, v)])
        + raw_entropy([x - y for x, y in zip(u, v)])
    )


def influence(coeff):
    return sum(x * x * mask.bit_count() for mask, x in enumerate(coeff))


def restrict_table(values, coordinate, sign_bit):
    bit = 1 << coordinate
    return tuple(v for idx, v in enumerate(values) if ((idx & bit) != 0) == bool(sign_bit))


def outer_data(plus, minus):
    p, m = fwht(plus), fwht(minus)
    a = [(x + y) / 2.0 for x, y in zip(p, m)]
    b = [(x - y) / 2.0 for x, y in zip(p, m)]
    q = sum(x * x for x in b)
    M = 2.0 * sum(
        bt * bt * max(0.0, log(abs(at / bt)))
        for at, bt in zip(a, b) if bt != 0.0 and at != 0.0
    )
    return a, b, q, M


def closed_remainder(a, b, mu, alpha):
    total = 0.0
    for at, bt in zip(a, b):
        if bt:
            total += bt * bt * (
                kernel(at / bt + mu, alpha) - kernel(mu, alpha)
            )
    return total


def direct_splice(plus, minus, child):
    # Outer coordinates are low bits; child coordinates are high bits.
    out = []
    for x, hx in enumerate(child):
        branch = plus if hx == 1 else minus
        out.extend(branch)
    return out


def main():
    outer_functions = list(product((-1, 1), repeat=4))
    outer_pairs = []
    for plus in outer_functions:
        for minus in outer_functions:
            a, b, q, M = outer_data(plus, minus)
            outer_pairs.append((plus, minus, a, b, q, M))

    exact_cases = 0
    max_identity_err = 0.0
    max_envelope_excess = -1e100
    worst_identity = None
    worst_envelope = None

    for n in (1, 2, 3):
        for child in product((-1, 1), repeat=1 << n):
            hc = fwht(child)
            mu = hc[0]
            for i in range(n):
                alpha = hc[1 << i]
                dh = split_decrement_from_coeff(hc, i)
                for plus, minus, a, b, q, M in outer_pairs:
                    fc = fwht(direct_splice(plus, minus, child))
                    direct = split_decrement_from_coeff(fc, 2 + i) - q * dh
                    closed = closed_remainder(a, b, mu, alpha)
                    err = abs(direct - closed)
                    if err > max_identity_err:
                        max_identity_err = err
                        worst_identity = (n, i, child, plus, minus, direct, closed)
                    rhs = (
                        q * psi(alpha)
                        + (4.0 + 2.0 * log(2.0)) * q * alpha * alpha
                        + M * alpha * alpha
                    )
                    excess = closed - rhs
                    if excess > max_envelope_excess:
                        max_envelope_excess = excess
                        worst_envelope = (n, i, child, plus, minus, closed, rhs)
                    exact_cases += 1

    assert max_identity_err <= TOL, worst_identity
    assert max_envelope_excess <= TOL, worst_envelope

    # For every two-bit outer pair and every Boolean child through 3 bits,
    # maximize over all adaptive, branch-dependent, nonreusing trees.  A tree
    # may stop at any node.  This is independent of the author's sampled-tree
    # checker and directly tests the full finite tree class in this scope.
    hierarchy_cases = 0
    max_hierarchy_excess = -1e100
    max_psi_excess = -1e100
    max_sq_excess = -1e100
    worst_hierarchy = None

    for plus, minus, a, b, q, M in outer_pairs:
        Csrc = M + (4.0 + 2.0 * log(2.0) + 2.0 / e) * q

        @lru_cache(maxsize=None)
        def tree_dp(vals):
            m = (len(vals).bit_length() - 1)
            if m == 0:
                return (0.0, 0.0, 0.0)
            hc = fwht(vals)
            mu = hc[0]
            best_r = best_p = best_s = 0.0
            for i in range(m):
                alpha = hc[1 << i]
                lo = restrict_table(vals, i, 0)
                hi = restrict_table(vals, i, 1)
                l = tree_dp(lo)
                h = tree_dp(hi)
                best_r = max(best_r, closed_remainder(a, b, mu, alpha) + 0.5 * (l[0] + h[0]))
                best_p = max(best_p, psi(alpha) + 0.5 * (l[1] + h[1]))
                best_s = max(best_s, alpha * alpha + 0.5 * (l[2] + h[2]))
            return best_r, best_p, best_s

        for n in (1, 2, 3):
            for child in product((-1, 1), repeat=1 << n):
                coeff = fwht(child)
                inf = influence(coeff)
                best_r, best_p, best_s = tree_dp(tuple(child))
                ex = best_r - Csrc * inf
                pex = best_p - (2.0 / e) * inf
                sex = best_s - inf
                if ex > max_hierarchy_excess:
                    max_hierarchy_excess = ex
                    worst_hierarchy = (n, child, plus, minus, best_r, Csrc * inf)
                max_psi_excess = max(max_psi_excess, pex)
                max_sq_excess = max(max_sq_excess, sex)
                hierarchy_cases += 1

    assert max_hierarchy_excess <= TOL, worst_hierarchy
    assert max_psi_excess <= TOL
    assert max_sq_excess <= TOL

    # Deterministic logarithmic-grid checks of the scalar estimates, including
    # the near-collision and large-r regimes.  These are stress tests, while
    # the report supplies the analytic proof.
    grid = [0.0]
    for sign in (-1.0, 1.0):
        for j in range(-60, 61):
            grid.append(sign * (2.0 ** (j / 4.0)))
        grid.extend([sign * (1.0 + 2.0 ** (-j)) for j in range(2, 45)])
    max_scalar_upper = max_scalar_lower = max_difference = -1e100
    for r in grid:
        kval = kernel(r, 1.0)
        max_scalar_upper = max(max_scalar_upper, kval - (2.0 * log(1.0 + abs(r)) + 3.0))
        max_scalar_lower = max(max_scalar_lower, (2.0 * log(1.0 + abs(r)) - 1.0) - kval)
    for r in grid:
        kr = kernel(r, 1.0)
        for s in grid:
            max_difference = max(
                max_difference,
                kr - kernel(s, 1.0) - (4.0 + 2.0 * log(1.0 + abs(r - s))),
            )
    assert max_scalar_upper <= TOL
    assert max_scalar_lower <= TOL
    assert max_difference <= TOL

    print("B12 independent coherent-kernel audit: PASS")
    print(f"direct truth-table split cases: {exact_cases}")
    print(f"adaptive tree roots (all trees optimized): {hierarchy_cases}")
    print(f"scalar grid points: {len(grid)}; ordered pairs: {len(grid)**2}")
    print(f"max |direct remainder - closed kernel|: {max_identity_err:.3e}")
    print(f"max one-node envelope excess: {max_envelope_excess:.3e}")
    print(f"max fixed-source hierarchy excess: {max_hierarchy_excess:.3e}")
    print(f"max alpha-log ledger excess: {max_psi_excess:.3e}")
    print(f"max alpha-square ledger excess: {max_sq_excess:.3e}")
    print(f"max scalar upper-bound excess: {max_scalar_upper:.3e}")
    print(f"max scalar lower-bound excess: {max_scalar_lower:.3e}")
    print(f"max scalar difference-bound excess: {max_difference:.3e}")


if __name__ == "__main__":
    main()

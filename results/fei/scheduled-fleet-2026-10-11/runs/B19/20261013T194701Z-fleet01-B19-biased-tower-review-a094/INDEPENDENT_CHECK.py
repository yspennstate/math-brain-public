#!/usr/bin/env python3
"""Independent direct-Walsh audit of B05's biased activation tower.

This intentionally uses a naive Walsh transform, not the author's FWHT code.
It checks the exact activation recurrences on exhaustive small Boolean bases,
the endpoint inequality, fixed-subset restriction payments, tensor additivity,
rare point-defect regimes, and the advertised failure of restriction closure.
"""

from itertools import product
from math import log2

TOL = 2.0e-10
C = 48.0 / 35.0


def popcount(x):
    return x.bit_count()


def walsh(values):
    n = (len(values)).bit_length() - 1
    scale = 1.0 / len(values)
    out = []
    for mask in range(1 << n):
        total = 0.0
        for x, fx in enumerate(values):
            total += fx * (-1.0 if popcount(mask & x) & 1 else 1.0)
        out.append(total * scale)
    return out


def stats(values):
    n = (len(values)).bit_length() - 1
    hats = walsh(values)
    p = [a * a for a in hats]
    u = 0.0
    for s, ps in enumerate(p):
        if ps == 0.0:
            continue
        cap = sum(p[t] for t in range(1 << n) if (t & s) == s)
        u += ps * log2(cap / ps)
    influence = sum(popcount(s) * ps for s, ps in enumerate(p))
    return sum(values) / len(values), u, influence


def tensor(a, b):
    # Variables of a are low-order; variables of b are high-order.
    return [a[x] * b[y] for y in range(len(b)) for x in range(len(a))]


def activate(q):
    # New selector z is low-order: z=+1 at bit 0, z=-1 at bit 1.
    ans = []
    for qx in q:
        ans.extend((1, qx))
    return ans


B = [-1, -1, -1, 1]
W = [1, -1]


def tower(base, depth):
    f = activate(tensor(W, base))
    for _ in range(2, depth + 1):
        f = activate(tensor(f, B))
    return f


def restrict(values, fixed):
    """fixed maps old variable index to bit 0(+1) or 1(-1)."""
    n = (len(values)).bit_length() - 1
    free = [i for i in range(n) if i not in fixed]
    ans = []
    for y in range(1 << len(free)):
        x = 0
        for i, bit in fixed.items():
            x |= bit << i
        for j, i in enumerate(free):
            x |= ((y >> j) & 1) << i
        ans.append(values[x])
    return ans


def average_restricted_u(values, coords):
    total = 0.0
    for bits in product((0, 1), repeat=len(coords)):
        _, u, _ = stats(restrict(values, dict(zip(coords, bits))))
        total += u
    return total / (1 << len(coords))


def scalar_terms(t):
    def xlog(x):
        return 0.0 if x == 0.0 else x * log2(1.0 / x)

    e = xlog((1 + t) ** 2 / 4.0)
    y = (1 - t) ** 2 / 4.0
    if y:
        e += y * log2(2.0 / (1.0 - t))
    u = 0.0 if t == 0.0 else t * t * log2(1.0 / (t * t))
    return e - 0.5 * u + 0.25 * (1 - t * t)


def main():
    mb, ub, ib = stats(B)
    assert abs(mb + 0.5) < TOL and abs(ub - 1.0) < TOL and abs(ib - 1.0) < TOL

    grid_max = max(scalar_terms(-j / 20000.0) for j in range(20001))
    assert grid_max <= 1.0 + TOL

    exhaustive_bases = 0
    eligible_checks = 0
    recurrence_checks = 0
    payment_checks = 0
    max_endpoint_excess = -1e100
    max_recurrence_error = 0.0

    for n in range(4):
        size = 1 << n
        for truth_bits in range(1 << size):
            base = [1 if ((truth_bits >> x) & 1) else -1 for x in range(size)]
            exhaustive_bases += 1
            mp, up, ip = stats(base)
            f1 = tower(base, 1)
            m1, u1, i1 = stats(f1)
            max_recurrence_error = max(
                max_recurrence_error,
                abs(m1 - 0.5),
                abs(u1 - (1.0 + 0.5 * up)),
                abs(i1 - (1.0 + 0.5 * ip)),
            )
            recurrence_checks += 3

            f2 = tower(base, 2)
            m2, u2, i2 = stats(f2)
            r = scalar_terms(-m1 / 2.0)
            max_recurrence_error = max(
                max_recurrence_error,
                abs(m2 - (0.5 - m1 / 4.0)),
                abs(u2 - (0.5 * u1 + 0.5 + r)),
                abs(i2 - (0.5 * i1 + 1.0 + m1 / 4.0)),
            )
            recurrence_checks += 3

            if up <= C * ip + TOL:
                eligible_checks += 2
                max_endpoint_excess = max(max_endpoint_excess, u1 - C * i1, u2 - C * i2)
                assert u1 <= C * i1 + TOL
                assert u2 <= C * i2 + TOL

            # A fixed-subset reveal is a complete balanced restriction tree.
            # Test both the outer selector alone and two mixed coordinates.
            for f in (f1, f2):
                _, uf, inf = stats(f)
                coord_sets = [(0,)]
                if len(f) >= 4:
                    coord_sets.append((0, (len(f).bit_length() - 2)))
                for coords in coord_sets:
                    debt = uf - average_restricted_u(f, coords)
                    assert debt <= C * inf + TOL
                    payment_checks += 1

    # Rare one-point defects, including endpoint means close to +/-1.
    rare_checks = 0
    for n in range(1, 8):
        size = 1 << n
        for background in (-1, 1):
            base = [background] * size
            base[-1] = -background
            mp, up, ip = stats(base)
            for depth in (1, 2 if n <= 5 else 1):
                f = tower(base, depth)
                _, uf, inf = stats(f)
                if up <= C * ip + TOL:
                    assert uf <= C * inf + TOL
                rare_checks += 1

    # Independent direct check of common-core cancellation via tensor additivity.
    terminal = [-1, -1, -1, 1]
    f = tower([-1, 1, 1, 1], 2)
    _, uf, inf = stats(f)
    _, uh, ih = stats(terminal)
    _, uf_h, if_h = stats(tensor(f, terminal))
    assert abs(uf_h - uf - uh) < TOL
    assert abs(if_h - inf - ih) < TOL

    # Positive-depth tower class is not restriction-closed: P=1 and w=-1
    # leave A(-1), a selector dictator, with (U,I)=(0,1).
    f1_const = tower([1], 1)
    restricted = restrict(f1_const, {1: 1})  # variable 1 is w; set w=-1
    _, ures, ires = stats(restricted)
    assert abs(ures) < TOL and abs(ires - 1.0) < TOL

    assert max_recurrence_error < TOL
    assert max_endpoint_excess <= TOL
    print("PASS independent direct-Walsh biased-tower audit")
    print(f"exhaustive Boolean bases: {exhaustive_bases} (all dimensions 0..3)")
    print(f"recurrence equalities checked: {recurrence_checks}")
    print(f"eligible endpoint checks at c=48/35: {eligible_checks}")
    print(f"fixed-subset tree payment checks: {payment_checks}")
    print(f"rare one-point-defect tower checks: {rare_checks}")
    print(f"maximum scalar R on 20001-point [-1,0] grid: {grid_max:.17g}")
    print(f"maximum recurrence absolute error: {max_recurrence_error:.3e}")
    print(f"maximum endpoint excess U-(48/35)I: {max_endpoint_excess:.17g}")
    print("tensor U/I additivity: PASS")
    print("restriction non-closure witness: PASS (restricted U=0, I=1)")


if __name__ == "__main__":
    main()

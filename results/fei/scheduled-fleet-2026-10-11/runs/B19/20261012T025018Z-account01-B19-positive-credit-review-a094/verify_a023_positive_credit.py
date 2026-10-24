#!/usr/bin/env python3
"""Independent exact-interval stress review of B05 A023 positive credit.

This file imports no submitted B05 code.  Rational probabilities are exact;
logarithms use a rational atanh enclosure with an explicit geometric tail.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, permutations

NTERMS = 56


@lru_cache(None)
def log_bounds(x: Q):
    assert x > 0
    shift = 0
    z = x
    while z < 1:
        z *= 2
        shift -= 1
    while z >= 2:
        z /= 2
        shift += 1

    def core(u):
        w = (u - 1) / (u + 1)
        total = Q(0)
        power = w
        for k in range(NTERMS):
            total += 2 * power / (2 * k + 1)
            power *= w * w
        err = 2 * abs(power) / ((2 * NTERMS + 1) * (1 - w * w))
        return total - err, total + err

    lo, hi = core(z)
    l2, u2 = core(Q(2))
    if shift >= 0:
        return lo + shift * l2, hi + shift * u2
    return lo + shift * u2, hi + shift * l2


LN2 = log_bounds(Q(2))


def plus(a, b): return a[0] + b[0], a[1] + b[1]
def minus(a, b): return a[0] - b[1], a[1] - b[0]
def times(c, a): return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])


def quotient(a, b):
    assert b[0] > 0
    corners = [a[i] / b[j] for i in (0, 1) for j in (0, 1)]
    return min(corners), max(corners)


@lru_cache(None)
def neg_t_log2_t(t):
    if t == 0:
        return Q(0), Q(0)
    lo, hi = log_bounds(t)
    return quotient((-t * hi, -t * lo), LN2)


@lru_cache(None)
def packet(p):
    """The already accepted complete L+Q scalar packet F(p)."""
    if p == Q(1, 2):
        return Q(2), Q(2)
    one = Q(1)
    base = (4*p*(one-p),) * 2
    label = plus(times(2*(one-p), neg_t_log2_t(one-p)),
                 times(2*p, neg_t_log2_t(p)))
    d = one - 2*p
    phase = times(-d*d, neg_t_log2_t(d))
    return plus(base, plus(label, phase))


def odd_probability(ds):
    bias = Q(1)
    for n in ds:
        bias *= 1 - Q(2, 1 << n)
    return (1 - bias) / 2


@lru_cache(None)
def residual_packet(ds):
    return packet(odd_probability(ds)) if ds else (Q(0), Q(0))


def local_credit(m, rest):
    parent = residual_packet((m,) + rest)
    continuing = residual_packet(((m-1,) + rest) if m > 1 else rest)
    off_path = residual_packet(rest)
    return minus(parent, times(Q(1, 2), plus(continuing, off_path)))


def stage_positive(a, rest):
    total = Q(0)
    for m in range(1, a + 1):
        g = local_credit(m, rest)
        total += Q(1 << m, 1 << a) * max(Q(0), g[1])
    return total


def influence(n): return Q(2*n, 1 << n)


def ordered_total(ds, order):
    alive = list(range(len(ds)))
    total = Q(0)
    rows = []
    for i in order:
        rest = tuple(ds[j] for j in alive if j != i)
        value = stage_positive(ds[i], rest)
        rows.append((ds[i], rest, value))
        total += value
        alive.remove(i)
    return total, rows


def main():
    checks = 0
    ledgers = 0
    stages = 0
    worst = (Q(0), None)

    assert LN2[0] > Q(2, 3)
    checks += 1

    # Exhaust all orders for up to three factors, including unequal dimensions.
    for r in range(1, 4):
        for ds in product(range(1, 6), repeat=r):
            for order in sorted(set(permutations(range(r)))):
                total, rows = ordered_total(ds, order)
                denom = sum((influence(n) for n in ds), Q(0))
                assert total < 24 * denom
                checks += 1
                ledgers += 1
                for n, rest, value in rows:
                    assert value < 48 * Q(1, 1 << n)
                    checks += 1
                    stages += 1
                ratio = total / denom
                if ratio > worst[0]:
                    worst = ratio, (ds, order, total, denom)

    # Hard endpoint and strongly unequal cases, with all orders where modest.
    cases = [
        (1, 1, 1, 1), (1, 2, 5, 9), (1, 3, 7, 13),
        (2, 4, 8, 16), (1, 2, 3, 7, 13), (1, 1, 2, 8, 31),
        (1, 3, 9, 27, 63), (12, 12, 12, 12, 12, 12),
    ]
    for ds in cases:
        if len(ds) <= 4:
            orders = sorted(set(permutations(range(len(ds)))))
        else:
            orders = [tuple(range(len(ds))), tuple(reversed(range(len(ds)))),
                      tuple(sorted(range(len(ds)), key=lambda i: (ds[i] % 3, -ds[i])))]
        for order in orders:
            total, rows = ordered_total(ds, order)
            denom = sum((influence(n) for n in ds), Q(0))
            assert total < 24 * denom
            checks += 1
            ledgers += 1
            for n, rest, value in rows:
                assert value < 48 * Q(1, 1 << n)
                checks += 1
                stages += 1
            ratio = total / denom
            if ratio > worst[0]:
                worst = ratio, (ds, order, total, denom)

    # Independent algebraic check behind F'''<0: after a common denominator,
    # -4p(1-p)-(1-p)(1-2p)+p(1-2p) is identically -1.
    for k in range(1, 10000):
        p = Q(k, 20000)
        numerator = -4*p*(1-p) - (1-p)*(1-2*p) + p*(1-2*p)
        assert numerator == -1
        checks += 1

    ds, order, total, denom = worst[1]
    print("PASS")
    print(f"checks={checks}")
    print(f"ledgers={ledgers}")
    print(f"stages={stages}")
    print("randomness=NONE")
    print("submitted_code_imported=NO")
    print("arithmetic=Fraction plus rigorous rational log intervals")
    print(f"worst_ratio={float(worst[0]):.15f}")
    print(f"worst_dims={ds}")
    print(f"worst_order={order}")
    print(f"worst_positive_upper={float(total):.15f}")
    print(f"worst_influence={float(denom):.15f}")


if __name__ == "__main__":
    main()

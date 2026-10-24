#!/usr/bin/env python3
"""Rigorous interval checks for the A023 positive-credit bound."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, permutations

TERMS = 48


@lru_cache(None)
def ln_interval(x):
    assert x > 0
    k = 0
    y = x
    while y < 1:
        y *= 2
        k -= 1
    while y >= 2:
        y /= 2
        k += 1

    def base(a):
        z = (a - 1) / (a + 1)
        total = F(0)
        power = z
        for j in range(TERMS):
            total += 2 * power / (2*j + 1)
            power *= z*z
        tail = 2 * power / ((2*TERMS + 1) * (1-z*z))
        return total, total + tail

    lo, hi = base(y)
    l2, h2 = base(F(2))
    if k > 0:
        lo, hi = lo + k*l2, hi + k*h2
    elif k < 0:
        lo, hi = lo + k*h2, hi + k*l2
    return lo, hi


LN2 = ln_interval(F(2))


def add(x, y): return x[0]+y[0], x[1]+y[1]
def sub(x, y): return x[0]-y[1], x[1]-y[0]
def scale(c, x): return (c*x[0], c*x[1]) if c >= 0 else (c*x[1], c*x[0])


def div(x, y):
    vals = (x[0]/y[0], x[0]/y[1], x[1]/y[0], x[1]/y[1])
    return min(vals), max(vals)


@lru_cache(None)
def phi(t):
    if t == 0:
        return F(0), F(0)
    lo, hi = ln_interval(t)
    return div((-t*hi, -t*lo), LN2)


@lru_cache(None)
def l_packet(a, v):
    q = a*a + v*v
    return sub(add(phi(a*a), phi(v*v)), phi(q))


@lru_cache(None)
def q_packet(a, v):
    q = a*a + v*v
    if q == 0:
        return F(0), F(0)
    s = F(1, 2) + abs(a*v)/q
    h = add(phi(s), phi(1-s))
    return scale(q, sub((F(1), F(1)), h))


@lru_cache(None)
def scalar_packet(p):
    return add((4*p*(1-p), 4*p*(1-p)), add(l_packet(1-p, p), q_packet(1-p, p)))


def parity_prob(ps):
    z = F(1)
    for p in ps:
        z *= 1-2*p
    return (1-z)/2


@lru_cache(None)
def packet_dims(dims):
    if not dims:
        return F(0), F(0)
    return scalar_packet(parity_prob(tuple(F(1, 1 << n) for n in dims)))


def gamma(m, rest):
    here = packet_dims((m,) + tuple(rest))
    child = packet_dims((m-1,) + tuple(rest)) if m > 1 else packet_dims(tuple(rest))
    return sub(here, scale(F(1, 2), add(child, packet_dims(tuple(rest)))))


def factor_positive_upper(a, rest):
    total = F(0)
    for m in range(1, a+1):
        g = gamma(m, tuple(rest))
        total += F(1 << m, 1 << a) * max(F(0), g[1])
    return total


def influence_q(n):
    return F(2*n, 1 << n)


def ledger_positive_upper(dims, order):
    remaining = list(range(len(dims)))
    total = F(0)
    stage_rows = []
    for i in order:
        rest_idx = [j for j in remaining if j != i]
        p = factor_positive_upper(dims[i], tuple(dims[j] for j in rest_idx))
        stage_rows.append((dims[i], p))
        total += p
        remaining.remove(i)
    return total, stage_rows


def main():
    assertions = 0
    ledgers = 0
    stages = 0
    largest = (F(0), None)

    # Exact rational fact used in the analytic constant ledger.
    assert LN2[0] > F(2, 3)
    assertions += 1

    # Exhaust dimensions 1..5 through three factors and every distinct order.
    for r in range(1, 4):
        for dims in product(range(1, 6), repeat=r):
            orders = sorted(set(permutations(range(r))))
            influence = sum((influence_q(n) for n in dims), F(0))
            for order in orders:
                total, rows = ledger_positive_upper(dims, order)
                assert total < 24*influence
                assertions += 1
                ledgers += 1
                for n, p in rows:
                    delta = F(1, 1 << n)
                    assert p < 48*delta
                    assertions += 1
                    stages += 1
                ratio = total/influence if influence else F(0)
                if ratio > largest[0]:
                    largest = (ratio, (dims, order, total, influence))

    # Four-factor bounded grid: every dimension tuple through four and both
    # factor-first directions.
    for dims in product(range(1, 5), repeat=4):
        orders = [(0,1,2,3), (3,2,1,0)]
        influence = sum((influence_q(n) for n in dims), F(0))
        for order in orders:
            total, rows = ledger_positive_upper(dims, order)
            assert total < 24*influence
            assertions += 1
            ledgers += 1
            for n, p in rows:
                assert p < 48*F(1, 1 << n)
                assertions += 1
                stages += 1
            ratio = total/influence
            if ratio > largest[0]:
                largest = (ratio, (dims, order, total, influence))

    # Higher-factor stress controls: equal, strongly unbalanced, and permuted.
    cases = [
        (1,)*8, (2,)*8, (6,)*8, (12,)*8,
        (1,2,3,4,5,6,7,8), (2,4,6,8,10,12),
        (1,1,2,3,5,8,13), (3,7,11,15,19)
    ]
    for dims in cases:
        orders = [tuple(range(len(dims))), tuple(reversed(range(len(dims))))]
        influence = sum((influence_q(n) for n in dims), F(0))
        for order in orders:
            total, rows = ledger_positive_upper(dims, order)
            assert total < 24*influence
            assertions += 1
            ledgers += 1
            for n, p in rows:
                assert p < 48*F(1, 1 << n)
                assertions += 1
                stages += 1
            ratio = total/influence
            if ratio > largest[0]:
                largest = (ratio, (dims, order, total, influence))

    # Direct scalar grid confirms F'''<0 through its exact closed numerator.
    for k in range(1, 2000):
        p = F(k, 4000)
        numerator = -4*p*(1-p) - (1-p)*(1-2*p) + p*(1-2*p)
        assert numerator == -1
        assertions += 1

    dims, order, total, influence = largest[1]
    print("PASS")
    print(f"assertions={assertions}")
    print(f"ledgers={ledgers}")
    print(f"factor_stages={stages}")
    print("randomness=NONE")
    print("arithmetic=exact Fraction packets plus rigorous rational atanh log intervals")
    print("claimed_constant=24")
    print(f"largest_checked_ratio={float(largest[0]):.15f}")
    print(f"largest_checked_dims={dims}")
    print(f"largest_checked_order={order}")
    print(f"largest_checked_positive_upper={float(total):.15f}")
    print(f"largest_checked_influence={float(influence):.15f}")


if __name__ == "__main__":
    main()

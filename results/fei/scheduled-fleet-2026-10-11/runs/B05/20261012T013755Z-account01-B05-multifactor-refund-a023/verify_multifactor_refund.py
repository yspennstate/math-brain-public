#!/usr/bin/env python3
"""Rigorous finite checks for the A023 multifactor point-defect refund ledger."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from math import comb, factorial

TERMS = 40


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
def pair_packet(a, v): return add(l_packet(a, v), q_packet(a, v))


@lru_cache(None)
def scalar_packet(p):
    return add((4*p*(1-p), 4*p*(1-p)), pair_packet(1-p, p))


def parity_prob(ps):
    prod = F(1)
    for p in ps:
        prod *= 1-2*p
    return (1-prod)/2


@lru_cache(None)
def packet_dims(dims):
    if not dims:
        return F(0), F(0)
    return scalar_packet(parity_prob(tuple(F(1, 1 << n) for n in dims)))


@lru_cache(None)
def mobius(dims):
    """Full interaction of precisely the listed factors."""
    r = len(dims)
    ans = (F(0), F(0))
    for mask in range(1, 1 << r):
        subdims = tuple(dims[j] for j in range(r) if (mask >> j) & 1)
        sign = -1 if ((r-mask.bit_count()) & 1) else 1
        ans = add(ans, scale(sign, packet_dims(subdims)))
    return ans


@lru_cache(None)
def mobius_equal(n, r):
    ans = (F(0), F(0))
    for j in range(1, r+1):
        ans = add(ans, scale(((-1)**(r-j))*comb(r, j), packet_dims((n,)*j)))
    return ans


def gamma(m, rest):
    rest = tuple(rest)
    here = packet_dims((m,) + rest)
    child = packet_dims((m-1,) + rest) if m > 1 else packet_dims(rest)
    return sub(here, scale(F(1, 2), add(child, packet_dims(rest))))


def factor_chain(a, rest):
    signed = (F(0), F(0))
    pos = (F(0), F(0))
    neg = (F(0), F(0))
    for m in range(1, a+1):
        w = F(1 << m, 1 << a)
        g = gamma(m, tuple(rest))
        signed = add(signed, scale(w, g))
        if g[0] > 0:
            pos = add(pos, scale(w, g))
        elif g[1] < 0:
            neg = add(neg, scale(w, scale(-1, g)))
        else:
            raise AssertionError("credit interval straddles zero")
    return signed, pos, neg


def recursive_ledger(dims, order):
    remaining = list(range(len(dims)))
    pos = (F(0), F(0))
    neg = (F(0), F(0))
    signed = (F(0), F(0))
    for i in order:
        rest_idx = [j for j in remaining if j != i]
        s, p, n = factor_chain(dims[i], tuple(dims[j] for j in rest_idx))
        signed, pos, neg = add(signed, s), add(pos, p), add(neg, n)
        remaining.remove(i)
    return signed, pos, neg


def overlap(x, y): return x[0] <= y[1] and y[0] <= x[1]


def fwht(vals):
    vals = list(vals)
    step = 1
    while step < len(vals):
        for base in range(0, len(vals), 2*step):
            for j in range(step):
                x, y = vals[base+j], vals[base+j+step]
                vals[base+j], vals[base+j+step] = x+y, x-y
        step *= 2
    return vals


def q_truth(n): return [1] + [-1]*((1 << n)-1)


def product_truth(dims):
    vals = [1]
    for n in dims:
        q = q_truth(n)
        vals = [x*y for x in vals for y in q]
    return vals


def packet_from_truth(vals, baseline=F(1)):
    raw = fwht(vals)
    N = len(vals)
    ans = (F(0), F(0))
    for s, r in enumerate(raw):
        bh = F(r, N)
        if s == 0:
            a, v = (bh+baseline)/2, (bh-baseline)/2
        else:
            a = v = bh/2
        ans = add(ans, pair_packet(a, v))
    return ans


def coeff(r):
    """Leading delta^2 coefficient for the r-way equal-factor interaction."""
    ans = (F(0), F(0))
    for j in range(1, r+1):
        lj = ln_interval(F(j))
        log2j = div(lj, LN2)
        ans = add(ans, scale(-2*((-1)**(r-j))*comb(r, j)*j*j, log2j))
    return ans


def decimal(iv): return float(iv[0]), float(iv[1])


def main():
    assertions = 0

    # Genuine Boolean/Walsh reconstruction for small three- and four-factor products.
    for dims in ((2,2,2), (2,2,3), (2,3,2), (2,2,2,2)):
        assert overlap(packet_from_truth(product_truth(dims)), packet_dims(tuple(dims)))
        assertions += 1

    # Möbius reconstruction and order-specific first-owner rule.
    cases = ((2,3,4), (3,3,3), (2,3,4,5), (3,3,3,3), (2,2,3,3,4))
    for dims in cases:
        r = len(dims)
        total = (F(0), F(0))
        for mask in range(1, 1 << r):
            sd = tuple(dims[j] for j in range(r) if (mask >> j) & 1)
            total = add(total, mobius(sd))
        assert overlap(total, packet_dims(tuple(dims)))
        assertions += 1

        orders = list(permutations(range(r))) if r <= 4 else [tuple(range(r)), tuple(reversed(range(r)))]
        for order in orders:
            # Every interaction is assigned to the earliest member in the order.
            owned_total = (F(0), F(0))
            for owner in order:
                owned = (F(0), F(0))
                for mask in range(1, 1 << r):
                    members = [j for j in range(r) if (mask >> j) & 1]
                    earliest = min(members, key=order.index)
                    if earliest == owner:
                        owned = add(owned, mobius(tuple(dims[j] for j in members)))
                rest = tuple(dims[j] for j in range(r) if j != owner and order.index(j) > order.index(owner))
                # At this stage earlier factors are gone; ownership equals R_current-R_rest.
                current = (dims[owner],) + rest
                assert overlap(owned, sub(packet_dims(current), packet_dims(rest)))
                owned_total = add(owned_total, owned)
                assertions += 1
            assert overlap(owned_total, packet_dims(tuple(dims)))
            assertions += 1

            signed, pos, neg = recursive_ledger(tuple(dims), order)
            assert overlap(signed, packet_dims(tuple(dims)))
            assert overlap(add(packet_dims(tuple(dims)), neg), pos)
            assertions += 2

    # Nonzero alternating higher-order interactions for equal rare factors.
    for r in range(3, 9):
        c = coeff(r)
        assert c[1] < 0 if r % 2 else c[0] > 0
        assertions += 1
        for n in range(12, 31):
            om = mobius_equal(n, r)
            assert om[1] < 0 if r % 2 else om[0] > 0
            assertions += 1
        for n in (20, 30):
            delta = F(1, 1 << n)
            scaled = scale(1/(delta*delta), mobius_equal(n, r))
            assert abs(float(scaled[0])-float(c[0])) < 0.04
            assertions += 1

    c3 = coeff(3)
    target3 = 24 - 18*(ln_interval(F(3))[0]/LN2[0])
    assert abs(float(c3[0])-float(target3)) < 1e-12
    assertions += 1

    print("PASS")
    print(f"assertions={assertions}")
    print("randomness=NONE")
    print("arithmetic=exact Fraction Walsh plus rigorous rational log intervals")
    print("r coefficient_lower coefficient_upper omega_n20_scaled_lower omega_n20_scaled_upper")
    for r in range(3, 9):
        d = F(1, 1 << 20)
        print(r, *decimal(coeff(r)), *decimal(scale(1/(d*d), mobius_equal(20, r))))


if __name__ == "__main__":
    main()

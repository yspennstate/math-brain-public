#!/usr/bin/env python3
"""Rigorous checks for the A023 two-factor q_a tensor q_b refund ledger.

All asserted logarithmic signs use rational outward intervals from the atanh
series.  Walsh transforms and reach probabilities use exact Fraction arithmetic.
"""
from fractions import Fraction as F
from functools import lru_cache

TERMS = 45


@lru_cache(None)
def ln_interval(x):
    assert x > 0
    power2 = 0
    y = x
    while y < 1:
        y *= 2
        power2 -= 1
    while y >= 2:
        y /= 2
        power2 += 1
    def base(arg):
        z = (arg - 1) / (arg + 1)
        total = F(0)
        power = z
        for j in range(TERMS):
            total += 2 * power / (2*j + 1)
            power *= z*z
        tail = 2 * power / ((2*TERMS + 1) * (1-z*z))
        return total, total + tail

    lo, hi = base(y)
    l2, h2 = base(F(2))
    if power2 > 0:
        lo, hi = lo + power2*l2, hi + power2*h2
    elif power2 < 0:
        lo, hi = lo + power2*h2, hi + power2*l2
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
    q = a*a+v*v
    return sub(add(phi(a*a), phi(v*v)), phi(q))


@lru_cache(None)
def q_packet(a, v):
    q = a*a+v*v
    if q == 0:
        return F(0), F(0)
    s = F(1, 2) + abs(a*v)/q
    h = add(phi(s), phi(1-s))
    return scale(q, sub((F(1), F(1)), h))


@lru_cache(None)
def pair_packet(a, v):
    return add(l_packet(a, v), q_packet(a, v))


@lru_cache(None)
def scalar_packet(p):
    """Complete selector packet for a Boolean child differing from a constant on mass p."""
    return add((4*p*(1-p), 4*p*(1-p)), pair_packet(1-p, p))


@lru_cache(None)
def scalar_closed(p):
    r = (1-2*p)*(1-2*p)
    ans = (4*p*(1-p), 4*p*(1-p))
    ans = add(ans, phi((1-p)*(1-p)))
    ans = add(ans, phi(p*p))
    return sub(ans, scale(F(1, 2), phi(r)))


def xor_prob(x, y): return x+y-2*x*y


@lru_cache(None)
def tensor_packet(a, b):
    return scalar_packet(xor_prob(F(1, 1 << a), F(1, 1 << b)))


@lru_cache(None)
def single_packet(a): return scalar_packet(F(1, 1 << a))


@lru_cache(None)
def cross(a, b): return sub(sub(tensor_packet(a, b), single_packet(a)), single_packet(b))


@lru_cache(None)
def gamma(m, b):
    child = tensor_packet(m-1, b) if m > 1 else single_packet(b)
    return sub(tensor_packet(m, b), scale(F(1, 2), add(child, single_packet(b))))


@lru_cache(None)
def signed_phase_sum(a, b):
    ans = (F(0), F(0))
    for m in range(1, a+1):
        ans = add(ans, scale(F(1 << m, 1 << a), gamma(m, b)))
    return ans


@lru_cache(None)
def pos_neg_phase(a, b):
    pos = (F(0), F(0))
    neg = (F(0), F(0))
    for m in range(1, a+1):
        g = gamma(m, b)
        w = F(1 << m, 1 << a)
        if g[0] > 0:
            pos = add(pos, scale(w, g))
        elif g[1] < 0:
            neg = add(neg, scale(w, scale(-1, g)))
        else:
            raise AssertionError("credit interval straddles zero")
    return pos, neg


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


def q_truth(n): return [1]+[-1]*((1 << n)-1)


def tensor_truth(a, b):
    qa, qb = q_truth(a), q_truth(b)
    return [qa[x]*qb[y] for x in range(1 << a) for y in range(1 << b)]


def packet_from_truth(vals, baseline):
    raw = fwht(vals)
    N = len(vals)
    ans = (F(0), F(0))
    for s, r in enumerate(raw):
        bh = F(r, N)
        if s == 0:
            aa, vv = (bh+baseline)/2, (bh-baseline)/2
        else:
            aa = vv = bh/2
        ans = add(ans, pair_packet(aa, vv))
    return ans


def decimal(iv): return float(iv[0]), float(iv[1])


def main():
    assertions = 0

    for k in range(33):
        p = F(k, 32)
        assert overlap(scalar_packet(p), scalar_closed(p))
        assert overlap(scalar_packet(p), scalar_packet(1-p))
        assertions += 2

    # Exact Boolean/Walsh reconstruction of the scalarization and symmetry.
    for a in range(2, 5):
        for b in range(2, 5):
            truth = tensor_truth(a, b)
            direct = packet_from_truth(truth, F(1))
            assert overlap(direct, tensor_packet(a, b))
            assertions += 1
            # Each full first-factor leaf is either q_b or -q_b against the
            # inherited constant; both have the same complete packet.
            assert overlap(packet_from_truth(q_truth(b), F(-1)), single_packet(b))
            assert overlap(packet_from_truth([-x for x in q_truth(b)], F(1)), single_packet(b))
            assert overlap(packet_from_truth(q_truth(b), F(1)), single_packet(b))
            assertions += 3

    # Both factor-first telescopes and their positive/negative single-use ledgers.
    for a in range(2, 13):
        for b in range(2, 13):
            sa = signed_phase_sum(a, b)
            sb = signed_phase_sum(b, a)
            assert overlap(sa, sub(tensor_packet(a, b), single_packet(b)))
            assert overlap(sb, sub(tensor_packet(a, b), single_packet(a)))
            assertions += 2
            pa, na = pos_neg_phase(a, b)
            pb, nb = pos_neg_phase(b, a)
            assert overlap(add(tensor_packet(a, b), na), add(single_packet(b), pa))
            assert overlap(add(tensor_packet(a, b), nb), add(single_packet(a), pb))
            assertions += 2

    # The cross term is real and changes sign; naive additive factor payment
    # can therefore both overpay and underpay.
    assert cross(4, 4)[1] < F(-1038, 100000)
    assert cross(5, 5)[0] > F(239, 100000)
    assertions += 2
    for n in range(5, 61):
        assert cross(n, n)[0] > 0
        assertions += 1

    # Check the leading asymptotic coefficient at large finite n.  The report
    # proves it analytically by expanding the exact scalar formula.
    for n in (20, 30, 40, 60):
        d = F(1, 1 << n)
        ratio = scale(1/(d*d), cross(n, n))
        lead = F(4*n-24, 1) + div((F(6), F(6)), LN2)[0]
        assert abs(float(ratio[0])-float(lead)) < 0.01
        assertions += 1

    print("PASS")
    print(f"assertions={assertions}")
    print("randomness=NONE")
    print("arithmetic=exact Fraction Walsh plus rigorous rational log intervals")
    print("a b cross lower upper Afirst_signed Bfirst_signed")
    for a, b in ((4,4),(4,5),(5,5),(5,8),(8,8),(12,12),(20,20)):
        print(a, b, *decimal(cross(a,b)), *decimal(signed_phase_sum(a,b)), *decimal(signed_phase_sum(b,a)))


if __name__ == "__main__":
    main()

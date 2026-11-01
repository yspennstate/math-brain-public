#!/usr/bin/env python3
"""Independent A094 audit of B05's two-factor refund theorem.

No target code is imported.  The principal scalar identity is checked by
building the full selector truth table and comparing its spectral-entropy
increment with F(p).  Formal cancellation is checked over an exact symbolic
basis.  Logarithmic signs use exact rational outward intervals.
"""

from fractions import Fraction as Q
from functools import lru_cache

TERMS = 48


def iv_add(a, b): return a[0] + b[0], a[1] + b[1]
def iv_sub(a, b): return a[0] - b[1], a[1] - b[0]
def iv_scale(c, a): return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])


def iv_div(a, b):
    vals = (a[0]/b[0], a[0]/b[1], a[1]/b[0], a[1]/b[1])
    return min(vals), max(vals)


@lru_cache(None)
def ln_iv(x):
    """Rigorous ln(x) enclosure from 2*atanh((x-1)/(x+1))."""
    assert x > 0
    e = 0
    y = x
    while y < 1:
        y *= 2
        e -= 1
    while y >= 2:
        y /= 2
        e += 1

    def core(t):
        z = (t-1)/(t+1)
        z2 = z*z
        power = z
        total = Q(0)
        for k in range(TERMS):
            total += 2*power/(2*k+1)
            power *= z2
        tail = 2*power/((2*TERMS+1)*(1-z2))
        return total, total+tail

    lo, hi = core(y)
    l2, h2 = core(Q(2))
    if e >= 0:
        return lo+e*l2, hi+e*h2
    return lo+e*h2, hi+e*l2


LN2 = ln_iv(Q(2))


@lru_cache(None)
def ent_atom(t):
    if t == 0:
        return Q(0), Q(0)
    lo, hi = ln_iv(t)
    return iv_div((-t*hi, -t*lo), LN2)


def spectral_entropy(truth):
    raw = fwht(truth)
    n = len(truth)
    out = (Q(0), Q(0))
    for r in raw:
        mass = Q(r*r, n*n)
        out = iv_add(out, ent_atom(mass))
    return out


def fwht(values):
    a = list(values)
    step = 1
    while step < len(a):
        for base in range(0, len(a), 2*step):
            for j in range(step):
                x, y = a[base+j], a[base+j+step]
                a[base+j], a[base+j+step] = x+y, x-y
        step *= 2
    return a


def q_truth(n):
    return [1] + [-1]*((1 << n)-1)


def tensor_truth(a, b):
    qa, qb = q_truth(a), q_truth(b)
    return [qa[i]*qb[j] for i in range(1 << a) for j in range(1 << b)]


def selector_truth(child, constant=1):
    # z=0 branch is the child, z=1 branch the constant.
    return list(child) + [constant]*len(child)


@lru_cache(None)
def scalar_F(p):
    out = (4*p*(1-p), 4*p*(1-p))
    out = iv_add(out, ent_atom((1-p)*(1-p)))
    out = iv_add(out, ent_atom(p*p))
    r = (1-2*p)*(1-2*p)
    # + r log_2 sqrt(r) = -1/2 * phi(r).
    out = iv_sub(out, iv_scale(Q(1, 2), ent_atom(r)))
    return out


def packet_direct(child, constant=1):
    parent = spectral_entropy(selector_truth(child, constant))
    average_child = iv_scale(Q(1, 2), spectral_entropy(child))
    return iv_sub(parent, average_child)


def overlap(a, b): return a[0] <= b[1] and b[0] <= a[1]


def xor_prob(x, y): return x+y-2*x*y


def R(a, b):
    return scalar_F(xor_prob(Q(1, 1 << a), Q(1, 1 << b)))


def D(a): return scalar_F(Q(1, 1 << a))


def cross(a, b): return iv_sub(iv_sub(R(a, b), D(a)), D(b))


def formal_telescope(a):
    """Coefficients in sum 2^(m-a)(R_m-(R_(m-1)+D)/2)."""
    coeff = {}
    def add(name, c):
        coeff[name] = coeff.get(name, Q(0)) + c
        if coeff[name] == 0:
            del coeff[name]
    for m in range(1, a+1):
        w = Q(1 << m, 1 << a)
        add(("R", m), w)
        add(("R", m-1), -w/2)
        add(("D", 0), -w/2)
    # R_0 is D, so identify it before comparing with R_a-D.
    c0 = coeff.pop(("R", 0), Q(0))
    add(("D", 0), c0)
    add(("R", a), -1)
    add(("D", 0), 1)
    return coeff


def main():
    checks = 0

    # Exact Boolean reconstruction and entropy-increment scalarization.
    for a in range(2, 5):
        for b in range(2, 5):
            child = tensor_truth(a, b)
            x, y = Q(1, 1 << a), Q(1, 1 << b)
            assert overlap(packet_direct(child), scalar_F(xor_prob(x, y)))
            assert overlap(packet_direct([-v for v in child], -1),
                           scalar_F(xor_prob(x, y)))
            checks += 2

    # Endpoint/symmetry, including the p=1/2 removable singularity.
    for k in range(65):
        p = Q(k, 64)
        assert overlap(scalar_F(p), scalar_F(1-p))
        checks += 1
    assert scalar_F(Q(0)) == (Q(0), Q(0))
    assert scalar_F(Q(1)) == (Q(0), Q(0))
    checks += 2

    # The weighted telescope is a pure formal cancellation for all depths.
    for a in range(1, 201):
        assert formal_telescope(a) == {}
        checks += 1

    # Direct numerical interval replay of both orders and split identities.
    for a in range(2, 11):
        for b in range(2, 11):
            for first, second in ((a, b), (b, a)):
                signed = (Q(0), Q(0))
                pos = (Q(0), Q(0))
                neg = (Q(0), Q(0))
                terminal = D(second)
                for m in range(1, first+1):
                    child = terminal if m == 1 else R(m-1, second)
                    gamma = iv_sub(R(m, second),
                                   iv_scale(Q(1, 2), iv_add(child, terminal)))
                    w = Q(1 << m, 1 << first)
                    signed = iv_add(signed, iv_scale(w, gamma))
                    if gamma[0] > 0:
                        pos = iv_add(pos, iv_scale(w, gamma))
                    elif gamma[1] < 0:
                        neg = iv_add(neg, iv_scale(-w, gamma))
                    else:
                        raise AssertionError("credit sign unresolved")
                target = iv_sub(R(first, second), terminal)
                assert overlap(signed, target)
                assert overlap(iv_add(R(first, second), neg),
                               iv_add(terminal, pos))
                checks += 2

    # Independent rigorous witnesses for failure of naive additivity.
    c44, c55 = cross(4, 4), cross(5, 5)
    assert c44[1] < Q(-1038, 100000)
    assert c55[0] > Q(239, 100000)
    checks += 2

    # Finite corroboration only; the infinite statement is proved by expansion.
    for n in range(5, 41):
        assert cross(n, n)[0] > 0
        checks += 1

    print("status=PASS")
    print(f"checks={checks}")
    print("randomness=NONE")
    print("method=truth-table spectral entropy + exact symbolic cancellation + rational log intervals")
    print(f"Xi_4_4=[{float(c44[0]):.12f},{float(c44[1]):.12f}]")
    print(f"Xi_5_5=[{float(c55[0]):.12f},{float(c55[1]):.12f}]")


if __name__ == "__main__":
    main()

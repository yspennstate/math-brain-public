#!/usr/bin/env python3
"""Finite/aggregated checks for B05 A023 rare-order transport.

No random search.  Direct Walsh checks use k=2,4; aggregated formulas scale farther.
All logarithms are base 2.
"""

import math


def phi(t):
    return 0.0 if t == 0.0 else t * math.log2(1.0 / t)


def h2(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -t * math.log2(t) - (1.0 - t) * math.log2(1.0 - t)


def jphase(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return 1.0 - h2(0.5 + math.sqrt(t * (1.0 - t)))


def fwht(values):
    out = [float(x) for x in values]
    n = len(out)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                a, b = out[j], out[j + step]
                out[j], out[j + step] = a + b, a - b
        step *= 2
    return [x / n for x in out]


def bent_values(k):
    assert k % 2 == 0
    vals = []
    for x in range(1 << k):
        exponent = 0
        for i in range(0, k, 2):
            exponent ^= ((x >> i) & 1) & ((x >> (i + 1)) & 1)
        vals.append(-1.0 if exponent else 1.0)
    return vals


def activate(values, r):
    # Bit layout: data bits first, then control bits. Activation at z=0.
    nk = len(values)
    out = []
    for z in range(1 << r):
        for x in range(nk):
            out.append(values[x] if z == 0 else 1.0)
    return out


def entropy_from_hat(hat):
    return sum(phi(a * a) for a in hat)


def pair_packets(uhat, vhat):
    L = Q = 0.0
    for u, v in zip(uhat, vhat):
        mid = 0.5 * (u + v)
        dif = 0.5 * (u - v)
        q = mid * mid + dif * dif
        if q == 0.0:
            continue
        theta = dif * dif / q
        L += q * h2(theta)
        Q += q * jphase(theta)
    return L, Q


def parent_entropy(uhat, vhat):
    coeffs = []
    for u, v in zip(uhat, vhat):
        coeffs.extend((0.5 * (u + v), 0.5 * (u - v)))
    return entropy_from_hat(coeffs)


def activation_overhead(p, a):
    R = math.log2(1.0 / p)
    m = 1.0 - a
    return (
        phi((1.0 - p * m) ** 2)
        + p * (1.0 - p) * m * m * (2.0 * R + math.log2(1.0 / (m * m)))
        + 2.0 * p * R * (1.0 - a * a)
        - p * phi(a * a)
    )


def aggregated(k):
    delta = 2.0 ** (-k)
    p = delta * delta
    c = math.sqrt(delta)
    # Bent coefficients all have |c|.  The flipped point is x=0, so every
    # coefficient shifts by -2 delta; signs comprise equal magnitude packets.
    Lcore = Qcore = Lroot = Qroot = 0.0
    for idx in range(1 << k):
        # For the standard quadratic bent function, compute the sign directly.
        # Its transform sign is obtained by a small FWHT once below for safety.
        pass
    bhat = fwht(bent_values(k))
    for T, bt in enumerate(bhat):
        mid = bt - delta
        e = delta * delta
        q = mid * mid + e
        theta = e / q
        Lcore += q * h2(theta)
        Qcore += q * jphase(theta)
        if T != 0:
            Lroot += p * q * h2(theta)
            Qroot += p * q * jphase(theta)
    # Empty-data activation packets.
    e = p * p * delta * delta
    mid_nonempty_control = p * (c - delta - 1.0)
    q1 = mid_nonempty_control ** 2 + e
    th1 = e / q1
    multiplicity = 1.0 / p - 1.0
    Lroot += multiplicity * q1 * h2(th1)
    Qroot += multiplicity * q1 * jphase(th1)
    mid_empty = 1.0 + p * (c - delta - 1.0)
    q0 = mid_empty ** 2 + e
    th0 = e / q0
    Lroot += q0 * h2(th0)
    Qroot += q0 * jphase(th0)
    return delta, p, Lcore, Qcore, Lroot, Qroot


def direct_check(k):
    r = 2 * k
    b = bent_values(k)
    bp = b[:]
    bp[0] *= -1.0
    bh, bph = fwht(b), fwht(bp)
    G, H = activate(b, r), activate(bp, r)
    Gh, Hh = fwht(G), fwht(H)
    Lc, Qc = pair_packets(bh, bph)
    Lr, Qr = pair_packets(Gh, Hh)
    delta = 2.0 ** (-k)
    p = delta * delta
    dcore = parent_entropy(bh, bph) - 0.5 * (entropy_from_hat(bh) + entropy_from_hat(bph))
    droot = parent_entropy(Gh, Hh) - 0.5 * (entropy_from_hat(Gh) + entropy_from_hat(Hh))
    am = math.sqrt(delta) - delta
    ab = math.sqrt(delta)
    abp = math.sqrt(delta) - 2.0 * delta
    swap_scalar = activation_overhead(p, am) - 0.5 * (
        activation_overhead(p, ab) + activation_overhead(p, abp)
    )
    assert abs(dcore - (Lc + Qc)) < 2e-12
    assert abs(droot - (Lr + Qr)) < 2e-11
    assert abs((droot - p * dcore) - swap_scalar) < 2e-11
    ag = aggregated(k)
    assert abs(Lr - ag[4]) < 2e-11
    assert abs(Qr - ag[5]) < 2e-11
    return {
        "k": k,
        "delta": delta,
        "p": p,
        "L_core": Lc,
        "L_root": Lr,
        "L_root_over_pL_core": Lr / (p * Lc),
        "L_correction_over_p_delta2_k": (Lr - p * Lc) / (p * delta * delta * k),
        "total_swap": droot - p * dcore,
        "scalar_swap": swap_scalar,
    }


if __name__ == "__main__":
    print("DIRECT WALSH CHECKS")
    for kval in (2, 4):
        print(direct_check(kval))
    print("AGGREGATED ASYMPTOTICS")
    for kval in (4, 6, 8, 10, 12, 16, 20):
        delta, p, Lc, Qc, Lr, Qr = aggregated(kval)
        d = p * delta
        print({
            "k": kval,
            "L_core/delta": Lc / delta,
            "L_root/d": Lr / d,
            "pL_core/d": p * Lc / d,
            "relative_order_error": (Lr - p * Lc) / (p * Lc),
            "bound_ratio": abs(Lr - p * Lc) / (p * delta * delta * (3 * kval + 7)),
            "Q_root/d": Qr / d,
        })

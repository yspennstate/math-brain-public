#!/usr/bin/env python3
"""Finite audit for the nested fresh-activation U identity.

No randomness. Enumerates every Boolean terminal core through 4 variables and
activation depths 1..8.  Logs are floating-point here; the report's theorem is
analytic and this program is only a formula/transcription check.
"""

from itertools import product
from math import log2, e, log


def walsh(vals):
    n = (len(vals)).bit_length() - 1
    out = []
    for mask in range(1 << n):
        s = 0
        for x, value in enumerate(vals):
            parity = (mask & x).bit_count() & 1
            s += value * (-1 if parity else 1)
        out.append(s / (1 << n))
    return out


def upper_u(vals):
    hats = walsh(vals)
    n = (len(vals)).bit_length() - 1
    ps = [h * h for h in hats]
    ans = 0.0
    for s, mass in enumerate(ps):
        if mass == 0:
            continue
        upper = sum(ps[t] for t in range(1 << n) if (t & s) == s)
        ans += mass * log2(upper / mass)
    return ans


def influence(vals):
    hats = walsh(vals)
    return sum(mask.bit_count() * h * h for mask, h in enumerate(hats))


def mean_packet(theta):
    y = abs(1 - 2 * theta)
    return 0.0 if y == 0 else y * y * log2(1 / (y * y))


def predicted_u(gvals, d):
    r = sum(v == -1 for v in gvals) / len(gvals)
    p = 2.0 ** (-d)
    mu = 1 - 2 * r
    e0 = 0.0 if mu == 0 else mu * mu * log2(1 / (mu * mu))
    lr = 0.0 if r == 0 else log2(1 / r)
    return (
        mean_packet(p * r)
        + 2 * r * p * d
        + p * (upper_u(gvals) - e0)
        + 4 * p * r * r * lr
        - (0.0 if p * r == 0 else 4 * p * p * r * r * log2(1 / (p * r)))
    )


def activate(gvals, d):
    # Variable encoding uses 0 as the active bit.  The sole active control
    # point is z=0; elsewhere the function is +1.
    return [gvals[x] if z == 0 else 1 for z in range(1 << d) for x in range(len(gvals))]


def node_charge(r, m):
    p = 2.0 ** (-m)
    last = 0.0 if p * r == 0 else 4 * p * p * r * r * (log2(1 / (p * r)) - 2)
    return mean_packet(p * r) - 0.5 * mean_packet(2 * p * r) + 2 * r * p + last


def main():
    assertions = 0
    max_ratio = 0.0
    argmax = None
    families = []
    for n in range(4):
        families.extend((n, bits) for bits in product((-1, 1), repeat=1 << n))
    # Deterministic structured 4-bit terminals: constants, parity, thresholds,
    # point/adjacent defects, and 32 affine-indexed sign tables.
    for mask in range(32):
        bits = tuple(-1 if (((x * 73 + mask * 29) ^ (x >> 1)) & 511).bit_count() & 1 else 1 for x in range(16))
        families.append((4, bits))
    families.extend([
        (4, tuple(1 for _ in range(16))),
        (4, tuple(-1 for _ in range(16))),
        (4, tuple(-1 if x == 0 else 1 for x in range(16))),
        (4, tuple(-1 if x in (0, 1) else 1 for x in range(16))),
        (4, tuple(-1 if x.bit_count() >= 2 else 1 for x in range(16))),
    ])
    for n, bits in families:
            ug = upper_u(bits)
            ig = influence(bits)
            r = sum(v == -1 for v in bits) / len(bits)
            for d in range(1, 6):
                fvals = activate(bits, d)
                direct = upper_u(fvals)
                pred = predicted_u(bits, d)
                assert abs(direct - pred) < 2e-10, (n, d, direct, pred)
                assertions += 1

                p = 2.0 ** (-d)
                signed = direct - p * ug
                telescoped = sum((2.0 ** (-(d - m))) * node_charge(r, m) for m in range(1, d + 1))
                assert abs(signed - telescoped) < 2e-10, (n, d, signed, telescoped)
                assertions += 1

                ictl = 2 * r * p * d
                if ictl:
                    cstar = 1 + 2 * (1 + 1 / e) / log(2)
                    assert signed <= cstar * ictl + 2e-12, (n, d, signed, ictl)
                    ratio = signed / ictl
                    if ratio > max_ratio:
                        max_ratio = ratio
                        argmax = (n, bits, d, r)
                    assertions += 1

                expected_i = p * ig + ictl
                assert abs(influence(fvals) - expected_i) < 2e-10
                assertions += 1

    print("PASS")
    print(f"assertions={assertions}")
    print(f"max_signed_charge_over_control_influence={max_ratio:.15f}")
    print(f"argmax=(terminal_n,depth,r)={(argmax[0],argmax[2],argmax[3]) if argmax else None}")
    print(f"analytic_constant={1 + 2 * (1 + 1 / e) / log(2):.15f}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact m=6 check for the balanced two-point bent-selector obstruction.

Standard-library only. Integer FWHT verifies the Walsh histograms; Fraction
arithmetic verifies the rigorous lower bounds. Floating logs are diagnostics
only and are not used to certify the inequalities.
"""
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math


def fwht_int(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def bent_sign(x, m):
    q = 0
    for j in range(0, m, 2):
        q ^= ((x >> j) & 1) & ((x >> (j + 1)) & 1)
    return 1 if q == 0 else -1


def entropy_from_walsh(W, nbits):
    den = float((1 << nbits) ** 2)
    ans = 0.0
    for w in W:
        if w:
            p = (w * w) / den
            ans -= p * math.log2(p)
    return ans


def main():
    m = 6
    N = 1 << m
    z = 3  # (1,1,0,...,0), where the quadratic bent sign is -1
    f0 = [bent_sign(x, m) for x in range(N)]
    assert f0[0] == 1 and f0[z] == -1
    f1 = list(f0)
    f1[0] *= -1
    f1[z] *= -1

    # Two flips of opposite original signs preserve the mean exactly.
    assert sum(f0) == sum(f1)
    delta = Fraction(2, N)

    W0 = fwht_int(f0)
    W1 = fwht_int(f1)
    parent = f0 + f1
    WP = fwht_int(parent)

    h0 = Counter(map(abs, W0))
    h1 = Counter(map(abs, W1))
    hp = Counter(map(abs, WP))
    assert h0 == Counter({8: 64})
    assert h1 == Counter({8: 32, 4: 20, 12: 12})
    assert hp == Counter({16: 32, 0: 32, 4: 32, 12: 20, 20: 12})

    # Exact entropy formulas:
    # H0 = 6
    # H1 = 7 - (27/64) log2 9
    # HP = 8 - (45/256) log2 9 - (75/256) log2 25
    # E/delta = 48 + (9/4) log2 3 - (75/4) log2 5.
    # Rigorous elementary bounds log2 3 > 3/2 and log2 5 < 7/3 give
    # E/delta > 61/8.
    edelta_lb = Fraction(61, 8)
    assert 3**2 > 2**3
    assert 5**3 < 2**7

    live_center = Fraction(4076157, 625000)  # 6.5218512
    base_center = Fraction(16137, 2500)      # 6.4548
    live_local_upper = delta * (live_center - edelta_lb)
    base_margin_lower = 4 * (edelta_lb - base_center)
    live_a = Fraction(41907, 156250)         # 0.2682048

    assert live_local_upper == Fraction(-172367, 5000000)
    assert live_local_upper < 0
    assert base_margin_lower == Fraction(5851, 1250)
    assert base_margin_lower > live_a

    # Diagnostics from the exact integer Walsh histograms.
    H0 = entropy_from_walsh(W0, m)
    H1 = entropy_from_walsh(W1, m)
    HP = entropy_from_walsh(WP, m + 1)
    E = HP - 0.5 * (H0 + H1)
    edelta = E / float(delta)
    base_margin = 4.0 * (edelta - float(base_center))
    live_local = float(delta) * (float(live_center) - edelta)

    payload = {
        "status": "PASS",
        "m": m,
        "N": N,
        "delta": str(delta),
        "equal_child_mean": sum(f0) == sum(f1),
        "walsh_abs_hist_f0": dict(sorted(h0.items())),
        "walsh_abs_hist_f1": dict(sorted(h1.items())),
        "walsh_abs_hist_parent": dict(sorted(hp.items())),
        "rigorous_E_over_delta_lower": str(edelta_lb),
        "live_center": str(live_center),
        "rigorous_live_local_contribution_upper": str(live_local_upper),
        "base_local_margin_lower": str(base_margin_lower),
        "live_quadratic_lift_a": str(live_a),
        "diagnostic_H0": H0,
        "diagnostic_H1": H1,
        "diagnostic_Hparent": HP,
        "diagnostic_E": E,
        "diagnostic_E_over_delta": edelta,
        "diagnostic_base_local_margin": base_margin,
        "diagnostic_live_local_contribution": live_local,
    }
    body = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(body.encode()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
